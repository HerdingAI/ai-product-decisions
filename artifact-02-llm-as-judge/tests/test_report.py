from eval_judge.bias_probes import ProbeResult
from eval_judge.judge import JudgeVerdict
from eval_judge.report import (
    cohen_kappa,
    cost_latency_summary,
    disagreements,
    per_criterion_agreement,
    probe_summary,
    results_json,
    summary_md,
)


def _verdict(case_id, **results):
    return JudgeVerdict(
        case_id=case_id, prompt_version="v1", results=results,
        reasons={k: "r" for k in results}, latency_ms=100.0, cost_usd=0.001,
        raw_text="{}",
    )


def test_cohen_kappa_perfect_agreement():
    a = [True, True, False, False, True]
    b = [True, True, False, False, True]
    assert cohen_kappa(a, b) == 1.0


def test_cohen_kappa_chance_agreement_near_zero():
    # Deliberately anti-correlated -> kappa should be negative or near zero, not 1.
    a = [True, True, True, True, False, False, False, False]
    b = [False, False, False, False, True, True, True, True]
    assert cohen_kappa(a, b) < 0


def test_cohen_kappa_handles_all_same_label():
    # No variance in either rater -> defined as 1.0 if they fully agree.
    assert cohen_kappa([True, True, True], [True, True, True]) == 1.0


def test_per_criterion_agreement_computes_rate_and_kappa():
    verdicts = [
        _verdict("C-01", grounded=True, complete=True),
        _verdict("C-02", grounded=False, complete=True),
        _verdict("C-03", grounded=True, complete=False),
    ]
    human = {
        "C-01": {"grounded": True, "complete": True},
        "C-02": {"grounded": False, "complete": True},
        "C-03": {"grounded": False, "complete": False},  # disagreement on grounded
    }
    result = per_criterion_agreement(verdicts, human)
    assert result["grounded"]["n"] == 3
    assert result["grounded"]["agreement_rate"] == 2 / 3
    assert result["complete"]["agreement_rate"] == 1.0


def test_per_criterion_agreement_skips_unlabeled_cases():
    verdicts = [_verdict("C-01", grounded=True), _verdict("C-02", grounded=False)]
    human = {"C-01": {"grounded": True}}  # C-02 not yet labeled
    result = per_criterion_agreement(verdicts, human)
    assert result["grounded"]["n"] == 1


def test_per_criterion_agreement_empty_when_no_labels():
    verdicts = [_verdict("C-01", grounded=True)]
    result = per_criterion_agreement(verdicts, {})
    assert result["grounded"]["n"] == 0
    assert result["grounded"]["agreement_rate"] is None


def test_cost_latency_summary_aggregates():
    verdicts = [
        _verdict("C-01", grounded=True),
        _verdict("C-02", grounded=True),
    ]
    verdicts[0].latency_ms = 100.0
    verdicts[0].cost_usd = 0.001
    verdicts[1].latency_ms = 300.0
    verdicts[1].cost_usd = 0.002
    summary = cost_latency_summary(verdicts)
    assert summary["total_cost_usd"] == 0.003
    assert summary["n"] == 2
    assert summary["p50_latency_ms"] in (100.0, 300.0, 200.0)
    assert summary["p95_latency_ms"] >= summary["p50_latency_ms"]


def test_cost_latency_summary_handles_missing_cost():
    v = _verdict("C-01", grounded=True)
    v.cost_usd = None
    summary = cost_latency_summary([v])
    assert summary["total_cost_usd"] is None


def _probe(probe, case_id, flagged):
    return ProbeResult(probe=probe, case_id=case_id, flagged=flagged, detail="d",
                        verdict_a=_verdict(case_id, grounded=True),
                        verdict_b=_verdict(case_id, grounded=True))


def test_probe_summary_counts_flags_per_probe_type():
    probes = [
        _probe("consistency", "C-01", False),
        _probe("consistency", "C-02", True),
        _probe("verbosity", "C-01", True),
        _probe("verbosity", "C-02", True),
    ]
    summary = probe_summary(probes)
    assert summary["consistency"]["flagged"] == 1
    assert summary["consistency"]["total"] == 2
    assert summary["verbosity"]["flagged"] == 2


def test_disagreements_lists_only_mismatches_with_judge_reason():
    verdicts = [
        _verdict("C-01", grounded=True, complete=True),
        _verdict("C-02", grounded=False, complete=True),
        _verdict("C-03", grounded=True, complete=False),
    ]
    human = {
        "C-01": {"grounded": True, "complete": True},
        "C-02": {"grounded": False, "complete": True},
        "C-03": {"grounded": False, "complete": False},  # disagreement on grounded only
    }
    rows = disagreements(verdicts, human)
    assert len(rows) == 1
    row = rows[0]
    assert row["case_id"] == "C-03"
    assert row["criterion"] == "grounded"
    assert row["judge"] is True
    assert row["human"] is False
    assert row["judge_reason"] == "r"


def test_disagreements_skips_unlabeled_criteria():
    verdicts = [_verdict("C-01", grounded=True, complete=True)]
    human = {"C-01": {"grounded": False}}  # complete never labeled
    rows = disagreements(verdicts, human)
    assert len(rows) == 1
    assert rows[0]["criterion"] == "grounded"


def test_disagreements_empty_when_fully_agreed():
    verdicts = [_verdict("C-01", grounded=True)]
    human = {"C-01": {"grounded": True}}
    assert disagreements(verdicts, human) == []


def test_summary_md_includes_disagreements_section_when_present():
    verdicts = [_verdict("C-01", grounded=True)]
    human = {"C-01": {"grounded": False}}
    md = summary_md(verdicts, human, [], target="http://x")
    assert "disagreement" in md.lower()
    assert "C-01" in md


def test_results_json_shape():
    verdicts = [_verdict("C-01", grounded=True, complete=True)]
    doc = results_json(verdicts, {}, [], target="http://x")
    assert doc["target"] == "http://x"
    assert "cases" in doc
    assert doc["cases"][0]["id"] == "C-01"


def test_summary_md_mentions_no_labels_when_unlabeled():
    verdicts = [_verdict("C-01", grounded=True, complete=True)]
    md = summary_md(verdicts, {}, [], target="http://x")
    assert "not yet hand-labeled" in md.lower() or "no human labels" in md.lower()


def test_summary_md_shows_agreement_when_labeled():
    verdicts = [_verdict("C-01", grounded=True)]
    human = {"C-01": {"grounded": True}}
    md = summary_md(verdicts, human, [], target="http://x")
    assert "grounded" in md
    assert "100%" in md or "1.0" in md
