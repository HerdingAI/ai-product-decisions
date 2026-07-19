from eval_judge.bias_probes import (
    consistency_probe,
    order_probe,
    run_all_probes,
    sycophancy_probe,
    verbosity_probe,
)
from eval_judge.calibration_set import OpenCase
from eval_judge.judge import Judge
from eval_judge.providers import FakeProvider

CASE = OpenCase("C-01", "grounding", "What does Colorado require?")
BASE_RESPONSE = "Colorado requires a documented AI risk-management program."

PASS_ALL = (
    '{"grounded": true, "grounded_reason": "r", "complete": true, "complete_reason": "r",'
    ' "appropriately-hedged": true, "appropriately-hedged_reason": "r",'
    ' "usable": false, "usable_reason": "too short"}'
)
PASS_ALL_TRUE = PASS_ALL.replace('"usable": false, "usable_reason": "too short"',
                                 '"usable": true, "usable_reason": "now specific"')


def _judge_with_script(script):
    return Judge(FakeProvider(script=script, default=PASS_ALL))


def test_consistency_probe_not_flagged_when_deterministic():
    judge = _judge_with_script({})  # FakeProvider always returns `default`
    result = consistency_probe(judge, CASE, [], BASE_RESPONSE)
    assert result.flagged is False


def test_consistency_probe_flagged_when_provider_is_nondeterministic():
    # FakeProvider keyed on exact prompt text -> same prompt twice returns
    # the same script entry, so simulate drift via a stateful provider.
    calls = {"n": 0}

    class FlakyProvider:
        model = "flaky"

        def complete(self, messages, **kw):
            calls["n"] += 1
            from eval_judge.providers import CompletionResult
            text = PASS_ALL if calls["n"] == 1 else PASS_ALL_TRUE
            return CompletionResult(text=text, latency_ms=1.0, cost_usd=0.0, model="flaky")

    judge = Judge(FlakyProvider())
    result = consistency_probe(judge, CASE, [], BASE_RESPONSE)
    assert result.flagged is True
    assert "usable" in result.detail or "changed" in result.detail


def test_verbosity_probe_flags_when_padding_flips_a_fail_to_pass():
    prompt_short = None  # unused; keyed by response content via FakeProvider default matching
    judge = Judge(FakeProvider(default=PASS_ALL))

    # Build a provider that returns PASS_ALL for the short response and
    # PASS_ALL_TRUE (usable flips to true) for the padded one, keyed on
    # whether the padding marker is present in the prompt.
    class PaddingSensitiveProvider:
        model = "pad-sensitive"

        def complete(self, messages, **kw):
            from eval_judge.providers import CompletionResult
            content = messages[-1]["content"]
            text = PASS_ALL_TRUE if "nuanced area" in content else PASS_ALL
            return CompletionResult(text=text, latency_ms=1.0, cost_usd=0.0, model="pad-sensitive")

    judge = Judge(PaddingSensitiveProvider())
    result = verbosity_probe(judge, CASE, [], BASE_RESPONSE)
    assert result.flagged is True
    assert "usable" in result.detail


def test_verbosity_probe_not_flagged_when_stable():
    judge = Judge(FakeProvider(default=PASS_ALL))
    result = verbosity_probe(judge, CASE, [], BASE_RESPONSE)
    assert result.flagged is False


def test_sycophancy_probe_flags_when_hint_flips_verdict():
    class HintSensitiveProvider:
        model = "hint-sensitive"

        def complete(self, messages, **kw):
            from eval_judge.providers import CompletionResult
            content = messages[-1]["content"]
            text = PASS_ALL_TRUE if "expert reviewer" in content else PASS_ALL
            return CompletionResult(text=text, latency_ms=1.0, cost_usd=0.0, model="hint-sensitive")

    judge = Judge(HintSensitiveProvider())
    result = sycophancy_probe(judge, CASE, [], BASE_RESPONSE)
    assert result.flagged is True


def test_sycophancy_probe_not_flagged_when_stable():
    judge = Judge(FakeProvider(default=PASS_ALL))
    result = sycophancy_probe(judge, CASE, [], BASE_RESPONSE)
    assert result.flagged is False


def test_order_probe_none_when_fewer_than_two_tool_calls():
    judge = Judge(FakeProvider(default=PASS_ALL))
    assert order_probe(judge, CASE, [], BASE_RESPONSE) is None
    assert order_probe(judge, CASE, [{"tool": "a"}], BASE_RESPONSE) is None


def test_order_probe_not_flagged_when_stable():
    judge = Judge(FakeProvider(default=PASS_ALL))
    two_calls = [{"tool": "a", "args": {}, "result": "x"},
                 {"tool": "b", "args": {}, "result": "y"}]
    result = order_probe(judge, CASE, two_calls, BASE_RESPONSE)
    assert result is not None
    assert result.flagged is False


def test_run_all_probes_returns_three_when_single_tool_call():
    judge = Judge(FakeProvider(default=PASS_ALL))
    probes = run_all_probes(judge, CASE, [{"tool": "a"}], BASE_RESPONSE)
    assert {p.probe for p in probes} == {"consistency", "verbosity", "sycophancy"}


def test_run_all_probes_includes_order_when_multiple_tool_calls():
    judge = Judge(FakeProvider(default=PASS_ALL))
    two_calls = [{"tool": "a", "args": {}, "result": "x"},
                 {"tool": "b", "args": {}, "result": "y"}]
    probes = run_all_probes(judge, CASE, two_calls, BASE_RESPONSE)
    assert {p.probe for p in probes} == {"consistency", "verbosity", "sycophancy", "order"}
