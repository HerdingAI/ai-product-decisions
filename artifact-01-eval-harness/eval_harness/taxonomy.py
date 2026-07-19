"""
Failure taxonomy and blast-radius thresholds.

The taxonomy turns a failed criterion into a named failure class the PM can
act on ("fix the tool-selection ordering") rather than a bare pass/fail.
Blast-radius thresholds are the ship gate: the minimum quality below which
the failure class is a blocker, not a known-issue.

Thresholds here are deliberately PM-set, not statistically derived — this is
a 10-case golden set, not a powered experiment. They encode a risk posture:
routing mistakes on the canonical paths are blockers; a single hallucination
on an out-of-scope query is an absolute blocker (one invented regulation is
the whole ballgame for a compliance agent).
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .criteria import CaseVerdict


# Failure class <- criterion that, when failed, produces it.
# Order matters: the first matching class is assigned (a case can fail
# several criteria; we report the most actionable one first).
TAXONOMY: list[tuple[str, list[str]]] = [
    # blast-radius: blockers
    ("hallucination", ["no_fabrication", "idk_when_no_tool"]),
    ("wrong_tool", ["tool_correct", "no_wrong_tool"]),
    ("no_answer", ["answers_question"]),
    ("missing_citation", ["cites_source"]),
]


def classify(verdict: CaseVerdict) -> list[str]:
    """Map a verdict's failed criteria to failure-class tags."""
    failed = {r.name for r in verdict.results if not r.passed}
    tags: list[str] = []
    for cls, crits in TAXONOMY:
        if failed & set(crits):
            tags.append(cls)
            failed -= set(crits)
    return tags


# ── blast-radius thresholds (the ship gate) ────────────────────────────────

@dataclass(frozen=True)
class Threshold:
    criterion: str
    minimum: float
    blocker: bool  # if True, falling below is a ship blocker
    rationale: str


THRESHOLDS: list[Threshold] = [
    Threshold("tool_correct", 0.90, True,
              "Routing the canonical paths is the core contract. Below 90% "
              "the agent cannot be trusted to reach the right tool."),
    Threshold("no_wrong_tool", 0.95, True,
              "Calling a forbidden tool is worse than missing one — it "
              "produces a confidently wrong answer."),
    Threshold("idk_when_no_tool", 1.0, True,
              "Any hallucination on an out-of-scope query is an absolute "
              "blocker. One invented regulation undoes the whole point of a "
              "compliance agent."),
    Threshold("no_fabrication", 1.0, True,
              "Mirrors idk_when_no_tool from the tool-call side: no tool "
              "should fire on a query no tool can serve."),
    Threshold("answers_question", 0.90, True,
              "Returning 'I don't know' when a tool could answer is a silent "
              "failure — the user thinks the system can't do something it can."),
    Threshold("cites_source", 0.95, False,
              "Ungrounded answers are a quality issue, not a trust blocker — "
              "flagged for the next cycle, not a ship gate."),
]


@dataclass
class MetricSummary:
    criterion: str
    pass_rate: float
    passed: int
    total: int
    against_threshold: Threshold | None = None
    meets_threshold: bool = True
    blocker: bool = False

    @property
    def label(self) -> str:
        if not self.against_threshold:
            return f"{self.criterion}: {self.pass_rate:.0%} ({self.passed}/{self.total})"
        gate = "PASS" if self.meets_threshold else "FAIL"
        return (f"{self.criterion}: {self.pass_rate:.0%} ({self.passed}/{self.total}) "
                f"vs ≥{self.against_threshold.minimum:.0%} [{gate}]")


def summarize(verdicts: list[CaseVerdict]) -> list[MetricSummary]:
    summaries: list[MetricSummary] = []
    all_criteria = sorted({r.name for v in verdicts for r in v.results})
    by_threshold = {t.criterion: t for t in THRESHOLDS}
    for cid in all_criteria:
        relevant = [v for v in verdicts if any(r.name == cid for r in v.results)]
        if not relevant:
            continue
        passed = sum(1 for v in relevant
                     for r in v.results if r.name == cid and r.passed)
        total = len(relevant)
        rate = passed / total if total else 0.0
        t = by_threshold.get(cid)
        meets = (rate >= t.minimum) if t else True
        summaries.append(MetricSummary(
            criterion=cid, pass_rate=rate, passed=passed, total=total,
            against_threshold=t, meets_threshold=meets,
            blocker=bool(t and t.blocker and not meets),
        ))
    return summaries


@dataclass
class ShipDecision:
    ship: bool
    blocker_metrics: list[str]
    known_issues: list[str]

    def render(self) -> str:
        head = "SHIP" if self.ship else "DO NOT SHIP"
        lines = [f"Verdict: {head}"]
        if self.blocker_metrics:
            lines.append("Blockers:")
            lines.extend(f"  - {m}" for m in self.blocker_metrics)
        if self.known_issues:
            lines.append("Known issues (next cycle):")
            lines.extend(f"  - {m}" for m in self.known_issues)
        return "\n".join(lines)


def ship_gate(summaries: list[MetricSummary]) -> ShipDecision:
    blockers = [m for m in summaries if m.blocker]
    issues = [m for m in summaries
              if m.against_threshold and not m.meets_threshold and not m.blocker]
    return ShipDecision(
        ship=len(blockers) == 0,
        blocker_metrics=[m.label for m in blockers],
        known_issues=[m.label for m in issues],
    )