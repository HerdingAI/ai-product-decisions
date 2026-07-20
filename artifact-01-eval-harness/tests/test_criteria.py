"""Characterization tests for the deterministic criteria — the rule-based
scoring functions that decide each case. These pin the behavior the committed
results depend on.
"""
from eval_harness.golden_set import GoldenCase
from eval_harness.criteria import (
    crit_no_wrong_tool,
    crit_answers_question,
    crit_cites_source,
)


def _case(**kw):
    base = dict(id="t", group="routing", query="q")
    base.update(kw)
    return GoldenCase(**base)


def _calls(*names):
    return [{"tool": n} for n in names]


def test_no_wrong_tool_flags_a_forbidden_call():
    case = _case(must_not_tools=["query_by_model"])
    r = crit_no_wrong_tool(case, "answer", _calls("query_by_model"))
    assert r.passed is False


def test_no_wrong_tool_passes_when_no_forbidden_call():
    case = _case(must_not_tools=["query_by_model"])
    r = crit_no_wrong_tool(case, "answer", _calls("get_article"))
    assert r.passed is True


def test_answers_question_fails_on_empty_response_when_tool_expected():
    case = _case(expected_tools=["get_article"])
    assert crit_answers_question(case, "   ", _calls("get_article")).passed is False


def test_answers_question_passes_on_real_answer():
    case = _case(expected_tools=["get_article"])
    assert crit_answers_question(case, "The effective date is Jan 1.", _calls("get_article")).passed is True


def test_cites_source_fails_on_ungrounded_tool_backed_answer():
    case = _case(expected_tools=["get_article"])
    # No grounding marker (no jurisdiction tag / Status: / Article N / Source).
    assert crit_cites_source(case, "It is allowed.", _calls("get_article")).passed is False


def test_cites_source_passes_when_grounding_marker_present():
    case = _case(expected_tools=["get_article"])
    assert crit_cites_source(case, "Per Article 9, testing is required.", _calls("get_article")).passed is True
