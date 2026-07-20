import pytest

from eval_judge.calibration_set import OpenCase
from eval_judge.judge import Judge, JudgeParseError, build_user_prompt, load_prompt, parse_verdict
from eval_judge.providers import CompletionResult, FakeProvider

CASE = OpenCase("C-01", "grounding", "What does Colorado require?")
TOOL_CALLS = [{"tool": "query_by_jurisdiction", "args": {"jurisdiction": "Colorado"},
               "result": "Colorado (CO) — Status: adopted"}]

VALID_JSON = (
    '{"grounded": true, "grounded_reason": "cites Colorado status",'
    ' "complete": true, "complete_reason": "answers the ask",'
    ' "appropriately-hedged": true, "appropriately-hedged_reason": "no overclaim",'
    ' "usable": false, "usable_reason": "too generic"}'
)


def test_judge_defaults_to_generous_token_budget_for_reasoning_models():
    # A reasoning judge spends completion tokens on its reasoning trace before
    # emitting the JSON verdict; too small a budget truncates the JSON. The
    # default must leave room so verdicts don't get cut off mid-string.
    provider = FakeProvider()
    Judge(provider, prompt_version="v1").judge(CASE, TOOL_CALLS, "resp")
    assert provider.max_tokens_seen[-1] >= 4096


def test_judge_forwards_configured_max_tokens():
    provider = FakeProvider()
    Judge(provider, prompt_version="v1", max_tokens=8000).judge(CASE, TOOL_CALLS, "resp")
    assert provider.max_tokens_seen[-1] == 8000


def test_load_prompt_v1_exists_and_mentions_all_criteria():
    text = load_prompt("v1")
    for c in ("grounded", "complete", "appropriately-hedged", "usable"):
        assert c in text


def test_load_prompt_missing_version_raises():
    with pytest.raises(FileNotFoundError):
        load_prompt("v99")


def test_build_user_prompt_includes_query_and_tool_trace():
    prompt = build_user_prompt(CASE, TOOL_CALLS, "Colorado requires X.")
    assert "What does Colorado require?" in prompt
    assert "query_by_jurisdiction" in prompt
    assert "Colorado requires X." in prompt


def test_build_user_prompt_handles_no_tool_calls():
    prompt = build_user_prompt(CASE, [], "I don't have that.")
    assert "no tool was called" in prompt


def test_parse_verdict_happy_path():
    result = CompletionResult(text=VALID_JSON, latency_ms=12.0, cost_usd=0.001, model="m")
    v = parse_verdict("C-01", "v1", result)
    assert v.passed is False  # usable=false
    assert v.results["grounded"] is True
    assert v.results["usable"] is False
    assert v.reasons["usable"] == "too generic"


def test_parse_verdict_strips_markdown_fences():
    fenced = "```json\n" + VALID_JSON + "\n```"
    result = CompletionResult(text=fenced, latency_ms=1.0, cost_usd=0.0, model="m")
    v = parse_verdict("C-01", "v1", result)
    assert v.results["grounded"] is True


def test_parse_verdict_invalid_json_raises():
    result = CompletionResult(text="not json at all", latency_ms=1.0, cost_usd=0.0, model="m")
    with pytest.raises(JudgeParseError):
        parse_verdict("C-01", "v1", result)


def test_parse_verdict_missing_criterion_raises():
    bad = '{"grounded": true, "complete": true, "usable": true}'
    result = CompletionResult(text=bad, latency_ms=1.0, cost_usd=0.0, model="m")
    with pytest.raises(JudgeParseError, match="appropriately-hedged"):
        parse_verdict("C-01", "v1", result)


def test_judge_end_to_end_with_fake_provider():
    prompt = build_user_prompt(CASE, TOOL_CALLS, "Colorado requires X.")
    provider = FakeProvider(script={prompt: VALID_JSON})
    judge = Judge(provider)
    verdict = judge.judge(CASE, TOOL_CALLS, "Colorado requires X.")
    assert verdict.results["grounded"] is True
    assert verdict.results["usable"] is False
    assert verdict.prompt_version == "v1"
    # system prompt was sent
    assert provider.calls[0][0]["role"] == "system"
