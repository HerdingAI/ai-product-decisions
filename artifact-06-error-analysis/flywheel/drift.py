"""Criteria-drift detection — error analysis of the evaluator itself.

The highest-leverage failure an eval can have is being wrong about what "good"
means: the judge faithfully applies the rubric, the human applies what they
actually want, and the two systematically diverge. That shows up as high,
**one-directional** judge-vs-human disagreement on a criterion. High but
*mixed* disagreement is noise (a hard criterion); high and *skewed* is drift
(the criterion or the labels need revising). This computes it objectively from
per-case verdicts — no new labels.
"""
from __future__ import annotations

# Thresholds: below this agreement AND at least this fraction of disagreements
# in one direction => the disagreement is systematic, i.e. drift.
_AGREEMENT_FLOOR = 0.80
_SKEW_FLOOR = 0.80


def analyze_criterion(cases: list[dict], criterion: str) -> dict:
    pairs = []
    for c in cases:
        judge = c.get("results", {}).get(criterion)
        human = c.get("human_labels", {}).get(criterion)
        if judge is None or human is None:
            continue
        pairs.append((bool(judge), bool(human)))

    n = len(pairs)
    agree = sum(1 for j, h in pairs if j == h)
    judge_stricter = sum(1 for j, h in pairs if j is False and h is True)
    human_stricter = sum(1 for j, h in pairs if j is True and h is False)
    disagreements = judge_stricter + human_stricter
    agreement_rate = agree / n if n else 1.0
    skew = max(judge_stricter, human_stricter) / disagreements if disagreements else 0.0
    direction = ("judge_stricter" if judge_stricter >= human_stricter
                 else "human_stricter")
    drift = (n > 0 and agreement_rate < _AGREEMENT_FLOOR
             and skew >= _SKEW_FLOOR)
    return {
        "criterion": criterion,
        "n": n,
        "agreement_rate": agreement_rate,
        "disagreements": disagreements,
        "judge_stricter": judge_stricter,
        "human_stricter": human_stricter,
        "skew": skew,
        "direction": direction,
        "drift": drift,
    }


def drift_report(cases: list[dict], criteria: list[str]) -> list[dict]:
    """Per-criterion drift analysis, worst agreement first."""
    rows = [analyze_criterion(cases, c) for c in criteria]
    rows.sort(key=lambda r: r["agreement_rate"])
    return rows
