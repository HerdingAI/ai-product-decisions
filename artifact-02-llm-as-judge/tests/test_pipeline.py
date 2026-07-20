"""The judge pass must tolerate a per-case failure (e.g. a truncated,
unparseable verdict from a reasoning model) without aborting the whole
run — a multi-case pass is expensive, so one bad case should be recorded
and skipped, not fatal.
"""
from eval_judge.judge import Judge
from eval_judge.pipeline import evaluate
from eval_judge.providers import CompletionResult

GOOD = (
    '{"grounded": true, "grounded_reason": "x", "complete": true, '
    '"complete_reason": "x", "appropriately-hedged": true, '
    '"appropriately-hedged_reason": "x", "usable": true, "usable_reason": "x"}'
)
TRUNCATED = '{"grounded": true, "grounded_reason": "unterminated'  # invalid JSON


class FlakyProvider:
    """Returns truncated JSON whenever the prompt mentions the bad case's
    query; valid JSON otherwise."""
    model = "fake/flaky"

    def __init__(self, bad_marker: str):
        self.bad_marker = bad_marker

    def complete(self, messages, *, temperature=0.0, max_tokens=1024):
        content = messages[-1]["content"]
        text = TRUNCATED if self.bad_marker in content else GOOD
        return CompletionResult(text=text, latency_ms=0.1, cost_usd=0.0, model=self.model)


def _rec(cid, group, query, labels):
    return {"id": cid, "group": group, "query": query, "note": "", "ok": True,
            "response": f"response for {query}", "tool_calls": [], "human_labels": labels}


def test_evaluate_skips_a_failing_case_and_keeps_going():
    records = [
        _rec("A", "grounding", "good query", {"grounded": True, "complete": True,
             "appropriately-hedged": True, "usable": True}),
        _rec("B", "grounding", "poison query", {"grounded": False, "complete": True,
             "appropriately-hedged": True, "usable": True}),
        _rec("C", "usability", "another good query", None),  # unlabeled (null labels)
    ]
    judge = Judge(FlakyProvider(bad_marker="poison query"), prompt_version="v1")

    verdicts, probes, human_labels, failures = evaluate(judge, records, run_probes=False)

    judged_ids = {v.case_id for v in verdicts}
    assert judged_ids == {"A", "C"}                # B skipped, others judged
    assert [cid for cid, _ in failures] == ["B"]   # B recorded as a failure
    assert set(human_labels) == {"A"}              # C's null labels excluded, B failed


def test_evaluate_is_order_stable_and_complete_when_parallelized():
    # With many cases and a thread pool, every case must still be judged and
    # results must come back in input order (agreement stats are per-case).
    labels = {"grounded": True, "complete": True,
              "appropriately-hedged": True, "usable": True}
    records = [_rec(f"N{i}", "grounding", f"query {i}", labels) for i in range(12)]
    judge = Judge(FlakyProvider(bad_marker="never"), prompt_version="v1")

    verdicts, _, human_labels, failures = evaluate(
        judge, records, run_probes=False, max_workers=4)

    assert [v.case_id for v in verdicts] == [f"N{i}" for i in range(12)]
    assert len(human_labels) == 12
    assert failures == []


def test_evaluate_handles_records_with_null_human_labels_without_crashing():
    records = [_rec("C", "usability", "q", None)]
    judge = Judge(FlakyProvider(bad_marker="never"), prompt_version="v1")
    verdicts, _, human_labels, failures = evaluate(judge, records, run_probes=False)
    assert [v.case_id for v in verdicts] == ["C"]
    assert human_labels == {}
    assert failures == []
