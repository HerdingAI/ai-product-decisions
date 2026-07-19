"""
Report — renders eval output for a PM audience.

Two artifacts:
  - results.json : the machine-readable record (cases, criteria, metrics,
    ship decision) for diffing across runs.
  - SUMMARY.md   : the human-readable brief a PM would actually read — what
    passed, what failed, the failure taxonomy, and the ship decision with the
    blocker rationale.
"""
from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime

from .criteria import CaseVerdict
from .runner import RawResult
from .taxonomy import MetricSummary, ShipDecision, classify, ship_gate, summarize


def results_json(verdicts: list[CaseVerdict], raw: list[RawResult],
                 summaries: list[MetricSummary], decision: ShipDecision,
                 target: str) -> dict:
    return {
        "target": target,
        "run_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "system_under_test": "HerdingAI/agentic-copilot (mock LLM, temperature 0)",
        "ship": decision.ship,
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
        "cases": [
            {
                "id": v.case_id,
                "group": v.group,
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


def summary_md(verdicts: list[CaseVerdict], raw: list[RawResult],
               summaries: list[MetricSummary], decision: ShipDecision,
               target: str) -> str:
    lines: list[str] = []
    lines.append(f"# Eval harness — results summary\n")
    lines.append(f"**System under test:** `HerdingAI/agentic-copilot` (mock LLM, temperature 0)  ")
    lines.append(f"**Target:** `{target}`  ")
    lines.append(f"**Cases:** {len(verdicts)}\n")

    lines.append("## Ship decision\n")
    lines.append("```")
    lines.append(decision.render())
    lines.append("```\n")

    lines.append("## Metrics vs. blast-radius thresholds\n")
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

    lines.append("## Failures by class (taxonomy)\n")
    failures = [(v, classify(v)) for v in verdicts if not v.passed]
    if not failures:
        lines.append("_No failures._\n")
    else:
        for v, tags in failures:
            tools = sorted({tc.get("tool", "") for tc in v.tool_calls if tc.get("tool")})
            lines.append(f"### {v.case_id} — {', '.join(tags) or 'uncategorized'}")
            lines.append(f"- **Query:** {v.query}")
            lines.append(f"- **Tools called:** {tools or 'none'}")
            for r in v.results:
                if not r.passed:
                    lines.append(f"- **{r.name}:** {r.reason}")
            lines.append(f"- **Response excerpt:** _{v.response[:140]}…_")
            lines.append("")

    lines.append("## What this is, and what it isn't\n")
    lines.append(
        "These numbers are real, produced by running the harness against a "
        "live `agentic-copilot` backend using its deterministic mock LLM. They "
        "describe **the mock LLM's tool-selection heuristics**, not a "
        "production model. The point of the artifact is the harness and the "
        "decision criteria — the ship gate, the failure taxonomy, the "
        "blast-radius thresholds — not the specific pass rates, which move "
        "the moment a real LLM is swapped in. Regenerate with "
        "`python run.py --target http://127.0.0.1:8011`.\n"
    )
    return "\n".join(lines)


def build(raw: list[RawResult], verdicts: list[CaseVerdict], target: str):
    summaries = summarize(verdicts)
    decision = ship_gate(summaries)
    return (
        results_json(verdicts, raw, summaries, decision, target),
        summary_md(verdicts, raw, summaries, decision, target),
        decision,
    )