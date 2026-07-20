"""Criteria drift is the failure mode where the *eval itself* is wrong: the
judge (faithful to the rubric) and the human systematically disagree on a
criterion, which means the criterion/labels stopped matching what's actually
wanted. Detecting it is objective — compare per-case judge verdicts to human
labels and look for high, one-directional disagreement. Pinned here.
"""
from flywheel.drift import analyze_criterion, drift_report


def _case(cid, judge, human):
    return {"id": cid,
            "results": {"c": judge},
            "human_labels": {"c": human}}


def test_high_one_directional_disagreement_flags_drift():
    # judge says False, human says True, on 8/10 cases -> systematic drift.
    cases = ([_case(f"a{i}", False, True) for i in range(8)]
             + [_case("b", True, True), _case("c", False, False)])
    r = analyze_criterion(cases, "c")
    assert r["n"] == 10
    assert r["disagreements"] == 8
    assert r["direction"] == "judge_stricter"
    assert r["drift"] is True


def test_low_disagreement_does_not_flag():
    cases = [_case(f"a{i}", True, True) for i in range(9)] + [_case("b", False, True)]
    r = analyze_criterion(cases, "c")
    assert r["agreement_rate"] == 0.9
    assert r["drift"] is False


def test_mixed_direction_disagreement_is_noise_not_drift():
    # disagreements split both ways -> not systematic -> not drift even if freq high
    cases = ([_case(f"a{i}", False, True) for i in range(3)]
             + [_case(f"b{i}", True, False) for i in range(3)]
             + [_case("c", True, True), _case("d", False, False)])
    r = analyze_criterion(cases, "c")
    assert r["disagreements"] == 6
    assert r["drift"] is False  # skew below threshold


def test_drift_report_ranks_criteria_worst_first():
    cases = [
        {"id": "x", "results": {"good": True, "bad": False},
         "human_labels": {"good": True, "bad": True}},
        {"id": "y", "results": {"good": True, "bad": False},
         "human_labels": {"good": True, "bad": True}},
    ]
    rep = drift_report(cases, ["good", "bad"])
    assert [r["criterion"] for r in rep][0] == "bad"   # worst agreement first
    assert rep[0]["drift"] is True
    assert rep[-1]["criterion"] == "good"
