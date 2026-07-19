"""
Report — renders eval output for a PM audience.

Two artifacts:
  - results.json : the machine-readable record (cases, criteria, metrics,
    ship decision per blast-radius tier) for diffing across runs.
  - SUMMARY.md   : the human-readable brief a PM would actually read — what
    passed, what failed, the failure taxonomy, and the ship decision with the
    blocker rationale, reported separately for the autonomous and reviewed
    tiers so a shaky-on-ambiguous-input result doesn't get conflated with a
    shaky-on-canonical-paths result.
"""
from __future__ import annotations

from datetime import datetime, timezone

from .criteria import CaseVerdict
from .runner import RawResult
from .taxonomy import (
    MetricSummary,
    ShipDecision,
    classify,
    ship_gate_by_tier,
    summarize_by_tier,
)


def results_json(verdicts: list[CaseVerdict], raw: list[RawResult],
                 summaries_by_tier: dict[str, list[MetricSummary]],
                 decisions_by_tier: dict[str, ShipDecision],
                 target: str) -> dict:
    return {
        "target": target,
        "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "system_under_test": "HerdingAI/agentic-copilot (mock LLM, temperature 0)",
        "ship": all(d.ship for d in decisions_by_tier.values()),
        "tiers": {
            tier: {
                "ship": decisions_by_tier[tier].ship,
                "case_count": sum(1 for v in verdicts if v.blast_radius == tier),
                "metrics": [
                    {
                        "criterion": m.criterion,
                        "pass_rate": round(m.pass_rate, 4),
                        "passed": m.passed,
                        "total": m.total,
                        "threshold": m.against_threshold.minimum if m.against_threshold else None,
                        "blocker": m.blocker,
                    }
                    for m in summaries
                ],
            }
            for tier, summaries in summaries_by_tier.items()
        },
        "cases": [
            {
                "id": v.case_id,
                "group": v.group,
                "blast_radius": v.blast_radius,
                "query": v.query,
                "tools_called": sorted({tc.get("tool", "") for tc in v.tool_calls if tc.get("tool")}),
                "passed": v.passed,
                "failures": classify(v),
                "criterion_results": [
                    {"name": r.name, "passed": r.passed, "reason": r.reason}
                    for r in v.results
                ],
                "latency_ms": next((r.latency_ms for r in raw if r.case_id == v.case_id), None),
                "response_excerpt": v.response[:160],
            }
            for v in verdicts
        ],
    }


def _tier_section(tier: str, verdicts: list[CaseVerdict],
                  summaries: list[MetricSummary], decision: ShipDecision) -> list[str]:
    lines: list[str] = []
    lines.append(f"## {tier.capitalize()} tier ({len(verdicts)} cases)\n")
    lines.append("```")
    lines.append(decision.render())
    lines.append("```\n")

    lines.append("| Criterion | Pass rate | Threshold | Gate |")
    lines.append("|---|---|---|---|")
    for m in summaries:
        if m.against_threshold:
            gate = "PASS" if m.meets_threshold else ("BLOCKER" if m.blocker else "issue")
            lines.append(
                f"| {m.criterion} | {m.pass_rate:.0%} ({m.passed}/{m.total}) "
                f"| ≥{m.against_threshold.minimum:.0%} | {gate} |"
            )
        else:
            lines.append(f"| {m.criterion} | {m.pass_rate:.0%} ({m.passed}/{m.total}) | — | — |")
    lines.append("")

    failures = [(v, classify(v)) for v in verdicts if not v.passed]
    if failures:
        lines.append(f"### {tier.capitalize()} tier — failures\n")
        for v, tags in failures:
            tools = sorted({tc.get("tool", "") for tc in v.tool_calls if tc.get("tool")})
            lines.append(f"**{v.case_id}** — {', '.join(tags) or 'uncategorized'}")
            lines.append(f"- Query: {v.query!r}")
            lines.append(f"- Tools called: {tools or 'none'}")
            for r in v.results:
                if not r.passed:
                    lines.append(f"- {r.name}: {r.reason}")
            lines.append(f"- Response excerpt: _{v.response[:140]}…_")
            lines.append("")
    return lines


def summary_md(verdicts: list[CaseVerdict], raw: list[RawResult],
               summaries_by_tier: dict[str, list[MetricSummary]],
               decisions_by_tier: dict[str, ShipDecision],
               target: str) -> str:
    lines: list[str] = []
    lines.append("# Eval harness — results summary\n")
    lines.append("**System under test:** `HerdingAI/agentic-copilot` (mock LLM, temperature 0)  ")
    lines.append(f"**Target:** `{target}`  ")
    lines.append(f"**Cases:** {len(verdicts)} "
                 f"({sum(1 for v in verdicts if v.blast_radius == 'autonomous')} autonomous, "
                 f"{sum(1 for v in verdicts if v.blast_radius == 'reviewed')} reviewed)\n")

    overall_ship = all(d.ship for d in decisions_by_tier.values())
    lines.append("## Overall verdict\n")
    lines.append(f"**{'SHIP' if overall_ship else 'DO NOT SHIP'}** — both tiers must clear "
                 "their gate; blast radius is a lens on the same failures, not a way to "
                 "average them away.\n")

    for tier in ("autonomous", "reviewed"):
        verdicts_t = [v for v in verdicts if v.blast_radius == tier]
        lines.extend(_tier_section(tier, verdicts_t, summaries_by_tier[tier], decisions_by_tier[tier]))

    lines.append("## What this is, and what it isn't\n")
    lines.append(
        "These numbers are real, produced by running the harness against a "
        "live `agentic-copilot` backend using its deterministic mock LLM. They "
        "describe **the mock LLM's tool-selection heuristics**, not a "
        "production model. The point of the artifact is the harness and the "
        "decision criteria — the two ship gates, the failure taxonomy, the "
        "blast-radius tiering — not the specific pass rates, which move "
        "the moment a real LLM is swapped in. Regenerate with "
        "`python run.py --target http://127.0.0.1:8011`.\n"
    )
    return "\n".join(lines)


def build(raw: list[RawResult], verdicts: list[CaseVerdict], target: str):
    summaries_by_tier = summarize_by_tier(verdicts)
    decisions_by_tier = ship_gate_by_tier(summaries_by_tier)
    return (
        results_json(verdicts, raw, summaries_by_tier, decisions_by_tier, target),
        summary_md(verdicts, raw, summaries_by_tier, decisions_by_tier, target),
        decisions_by_tier,
    )
