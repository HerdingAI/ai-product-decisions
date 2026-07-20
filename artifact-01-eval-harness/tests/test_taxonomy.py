"""Characterization tests for the failure taxonomy and the two-tier ship gate —
the machinery that turns per-criterion results into a named failure class and a
ship / no-ship verdict.
"""
from eval_harness.criteria import CaseVerdict, CriterionResult
from eval_harness.taxonomy import (
    classify,
    MetricSummary,
    Threshold,
    ship_gate,
)


def _verdict(*failed_criteria):
    results = [CriterionResult(name, name not in failed_criteria) for name in
               ("tool_correct", "no_wrong_tool", "no_fabrication",
                "idk_when_no_tool", "answers_question", "cites_source")]
    return CaseVerdict(case_id="c", query="q", group="routing", results=results)


def test_fabrication_failure_classifies_as_hallucination():
    tags = classify(_verdict("no_fabrication"))
    assert "hallucination" in tags


def test_wrong_tool_failure_classifies_as_wrong_tool():
    tags = classify(_verdict("tool_correct"))
    assert "wrong_tool" in tags


def test_clean_verdict_has_no_failure_tags():
    assert classify(_verdict()) == []


def test_ship_gate_blocks_when_a_blocker_threshold_is_missed():
    missed = MetricSummary(
        criterion="no_fabrication", pass_rate=0.45, passed=5, total=11,
        against_threshold=Threshold("no_fabrication", 1.0, True, "x"),
        meets_threshold=False, blocker=True,
    )
    decision = ship_gate([missed])
    assert decision.ship is False


def test_ship_gate_passes_when_all_thresholds_met():
    met = MetricSummary(
        criterion="tool_correct", pass_rate=0.95, passed=19, total=20,
        against_threshold=Threshold("tool_correct", 0.90, True, "x"),
        meets_threshold=True, blocker=False,
    )
    decision = ship_gate([met])
    assert decision.ship is True
