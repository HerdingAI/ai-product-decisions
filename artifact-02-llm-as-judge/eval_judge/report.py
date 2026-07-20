"""
Report — judge-vs-human agreement, bias-probe summary, cost/latency, and a
PM-readable brief. Mirrors artifact-01's report.py split (results.json for
diffing, SUMMARY.md for reading), but the central question here is
different: not "did the system pass," but "does the judge track a human."

Agreement numbers are only as good as the human labels behind them. When
`human_labels` is empty (not yet hand-labeled), every agreement/kappa field
comes back None/0 and the summary says so plainly instead of pretending 0%
disagreement is a real number.
"""
from __future__ import annotations

from datetime import datetime, timezone

from .bias_probes import ProbeResult
from .judge import CRITERIA, JudgeVerdict


def cohen_kappa(a: list[bool], b: list[bool]) -> float:
    n = len(a)
    if n == 0:
        return 0.0
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    p_a_true = sum(a) / n
    p_b_true = sum(b) / n
    pe = p_a_true * p_b_true + (1 - p_a_true) * (1 - p_b_true)
    if pe == 1.0:
        return 1.0 if po == 1.0 else 0.0
    return (po - pe) / (1 - pe)


def per_criterion_agreement(verdicts: list[JudgeVerdict],
                            human_labels: dict[str, dict[str, bool]]) -> dict:
    out = {}
    for c in CRITERIA:
        judge_vals, human_vals = [], []
        for v in verdicts:
            labels = human_labels.get(v.case_id)
            if labels is None or labels.get(c) is None:
                continue
            if c not in v.results:
                continue
            judge_vals.append(v.results[c])
            human_vals.append(labels[c])
        n = len(judge_vals)
        if n == 0:
            out[c] = {"n": 0, "agreement_rate": None, "kappa": None}
        else:
            agree = sum(1 for j, h in zip(judge_vals, human_vals) if j == h) / n
            out[c] = {"n": n, "agreement_rate": agree, "kappa": cohen_kappa(judge_vals, human_vals)}
    return out


def disagreements(verdicts: list[JudgeVerdict],
                  human_labels: dict[str, dict[str, bool]]) -> list[dict]:
    """Every case/criterion where the judge and Carlos's label disagree.

    This is the raw material for the acceptance-criteria confusion
    breakdown (spec §4 Artifact #2: "judge-vs-human disagreements coded
    by why") — the *coding* into named failure patterns (verbosity bias,
    position bias, criterion misreading, ...) is a qualitative read over
    these rows, done once real disagreements exist, not fabricated ahead
    of the data.
    """
    rows = []
    for v in verdicts:
        labels = human_labels.get(v.case_id)
        if not labels:
            continue
        for c in CRITERIA:
            human_val = labels.get(c)
            if human_val is None or c not in v.results:
                continue
            judge_val = v.results[c]
            if judge_val != human_val:
                rows.append({
                    "case_id": v.case_id,
                    "criterion": c,
                    "judge": judge_val,
                    "human": human_val,
                    "judge_reason": v.reasons.get(c, ""),
                })
    return rows


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    idx = min(len(s) - 1, max(0, round(pct / 100 * (len(s) - 1))))
    return s[idx]


def cost_latency_summary(verdicts: list[JudgeVerdict]) -> dict:
    costs = [v.cost_usd for v in verdicts if v.cost_usd is not None]
    latencies = [v.latency_ms for v in verdicts]
    return {
        "n": len(verdicts),
        "total_cost_usd": round(sum(costs), 6) if costs else None,
        "p50_latency_ms": round(_percentile(latencies, 50), 1) if latencies else None,
        "p95_latency_ms": round(_percentile(latencies, 95), 1) if latencies else None,
    }


def probe_summary(probes: list[ProbeResult]) -> dict:
    out: dict[str, dict[str, int]] = {}
    for p in probes:
        bucket = out.setdefault(p.probe, {"flagged": 0, "total": 0})
        bucket["total"] += 1
        if p.flagged:
            bucket["flagged"] += 1
    return out


def results_json(verdicts: list[JudgeVerdict], human_labels: dict[str, dict[str, bool]],
                 probes: list[ProbeResult], target: str) -> dict:
    return {
        "target": target,
        "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "agreement": per_criterion_agreement(verdicts, human_labels),
        "disagreements": disagreements(verdicts, human_labels),
        "probes": probe_summary(probes),
        "cost_latency": cost_latency_summary(verdicts),
        "cases": [
            {
                "id": v.case_id,
                "prompt_version": v.prompt_version,
                "passed": v.passed,
                "results": v.results,
                "reasons": v.reasons,
                "human_labels": human_labels.get(v.case_id),
            }
            for v in verdicts
        ],
    }


def summary_md(verdicts: list[JudgeVerdict], human_labels: dict[str, dict[str, bool]],
              probes: list[ProbeResult], target: str) -> str:
    agreement = per_criterion_agreement(verdicts, human_labels)
    costs = cost_latency_summary(verdicts)
    probe_stats = probe_summary(probes)

    lines: list[str] = []
    lines.append("# LLM-as-judge — calibration results\n")
    lines.append(f"**Target:** `{target}`  ")
    lines.append(f"**Cases judged:** {len(verdicts)}\n")

    lines.append("## Judge-vs-human agreement\n")
    any_labeled = any(a["n"] > 0 for a in agreement.values())
    if not any_labeled:
        lines.append(
            "No human labels yet — cases have not been hand-labeled. "
            "Agreement and Cohen's kappa are not yet computable; the "
            "numbers below will be N/A until Carlos hand-labels "
            "`labels/calibration_responses.json`.\n"
        )
    else:
        lines.append("| Criterion | n | Agreement | Cohen's κ |")
        lines.append("|---|---|---|---|")
        for c in CRITERIA:
            a = agreement[c]
            if a["n"] == 0:
                lines.append(f"| {c} | 0 | N/A | N/A |")
            else:
                lines.append(f"| {c} | {a['n']} | {a['agreement_rate']:.0%} | {a['kappa']:.2f} |")
        lines.append("")

    dis = disagreements(verdicts, human_labels)
    lines.append("## Disagreements (judge vs. human)\n")
    if not dis:
        lines.append(
            "No disagreements — either no human labels yet, or the judge "
            "matched Carlos on every labeled criterion.\n"
        )
    else:
        lines.append(
            "Raw rows below; see `RESULTS.md` for the coded failure-pattern "
            "analysis (verbosity bias, position bias, criterion misreading, "
            "etc. — spec §4 Artifact #2 acceptance criteria).\n"
        )
        lines.append("| Case | Criterion | Judge | Human | Judge's reason |")
        lines.append("|---|---|---|---|---|")
        for row in dis:
            lines.append(
                f"| {row['case_id']} | {row['criterion']} | {row['judge']} "
                f"| {row['human']} | {row['judge_reason']} |"
            )
        lines.append("")

    lines.append("## Bias probes\n")
    if not probe_stats:
        lines.append("No probe runs recorded.\n")
    else:
        lines.append("| Probe | Flagged | Total |")
        lines.append("|---|---|---|")
        for name, stats in probe_stats.items():
            lines.append(f"| {name} | {stats['flagged']} | {stats['total']} |")
        lines.append("")

    lines.append("## Cost / latency\n")
    lines.append(f"- Cases: {costs['n']}")
    lines.append(f"- Total cost: {'$' + str(costs['total_cost_usd']) if costs['total_cost_usd'] is not None else 'N/A'}")
    lines.append(f"- p50 latency: {costs['p50_latency_ms']} ms")
    lines.append(f"- p95 latency: {costs['p95_latency_ms']} ms\n")

    lines.append("## What this is, and what it isn't\n")
    lines.append(
        "Carlos is the sole labeler for the human-label side of this "
        "comparison; that's disclosed here, not hidden. The judge prompt "
        "is versioned in `judge_prompts/`; results should be regenerated "
        "whenever the prompt changes.\n"
    )
    return "\n".join(lines)


def build(verdicts: list[JudgeVerdict], human_labels: dict[str, dict[str, bool]],
         probes: list[ProbeResult], target: str):
    return (
        results_json(verdicts, human_labels, probes, target),
        summary_md(verdicts, human_labels, probes, target),
    )
