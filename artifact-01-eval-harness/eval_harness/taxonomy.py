"""
Failure taxonomy and blast-radius thresholds.

The taxonomy turns a failed criterion into a named failure class the PM can
act on ("fix the tool-selection ordering") rather than a bare pass/fail.
Blast-radius thresholds are the ship gate: the minimum quality below which
the failure class is a blocker, not a known-issue.

Thresholds here are deliberately PM-set, not statistically derived — this is
a 30-case golden set, not a powered experiment. They encode a risk posture,
split by who is exposed to a wrong answer:

  - autonomous cases: the agent's answer could flow straight into an
    unreviewed downstream action (a compliance check, a filed answer). Held
    to the strict bar — routing mistakes and hallucinations are blockers.
  - reviewed cases: a human reads the answer before it's acted on (an
    analyst skimming a chat transcript, a memo draft). The bar is real but
    softer — these are cases where the query itself is ambiguous, compound,
    or missing context, so some degradation is expected and a human catching
    it is the actual safety net, not the agent being perfect.

Two ship gates are reported for exactly this reason: a system that's solid
on the autonomous tier but shaky on ambiguous reviewed-tier input is a
different (and lower-severity) problem than one that's shaky on the paths
it's expected to run on its own.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .criteria import CaseVerdict


# Failure class <- criterion that, when failed, produces it.
# Order matters: the first matching class is assigned (a case can fail
# several criteria; we report the most actionable one first).
TAXONOMY: list[tuple[str, list[str]]] = [
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


# Autonomous tier: the strict bar. These are the cases most likely to run
# unreviewed, so the thresholds match the original single-tier gate.
THRESHOLDS_AUTONOMOUS: list[Threshold] = [
    Threshold("tool_correct", 0.90, True,
              "Routing the canonical paths is the core contract. Below 90% "
              "the agent cannot be trusted to reach the right tool on its own."),
    Threshold("no_wrong_tool", 0.95, True,
              "Calling a forbidden tool is worse than missing one — it "
              "produces a confidently wrong answer with no human catching it."),
    Threshold("idk_when_no_tool", 1.0, True,
              "Any hallucination on an out-of-scope query is an absolute "
              "blocker. One invented regulation undoes the whole point of a "
              "compliance agent when nobody reviews the output."),
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

# Reviewed tier: softer bar. These queries are ambiguous, compound, or
# missing context by construction — a human is the safety net, so the gate
# checks for gross failure (fabrication, wrong tool on an unambiguous part
# of the query) rather than perfect handling of an underspecified ask.
THRESHOLDS_REVIEWED: list[Threshold] = [
    Threshold("tool_correct", 0.60, True,
              "Ambiguous or compound queries are expected to strain routing. "
              "Below 60% the agent isn't even a useful first pass for a "
              "human to review."),
    Threshold("no_wrong_tool", 0.80, True,
              "A wrong tool call still costs review time even with a human "
              "in the loop, so this stays a blocker, just at a looser bar "
              "than the autonomous tier."),
    Threshold("idk_when_no_tool", 0.80, True,
              "Some ambiguous queries will tempt a tool call; a human "
              "reviewing the transcript is expected to catch an occasional "
              "miss, but not most of them."),
    Threshold("no_fabrication", 0.80, True,
              "Same logic as idk_when_no_tool from the tool-call side."),
    Threshold("answers_question", 0.60, False,
              "A partial or declined answer on a genuinely ambiguous query "
              "is an acceptable outcome for a human to follow up on — flagged, "
              "not blocking."),
    Threshold("cites_source", 0.60, False,
              "Same as autonomous tier: quality issue, not a trust blocker."),
]

# Kept for callers that don't care about tiering (e.g. a quick all-up read).
THRESHOLDS: list[Threshold] = THRESHOLDS_AUTONOMOUS


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


def _summarize(verdicts: list[CaseVerdict], thresholds: list[Threshold]) -> list[MetricSummary]:
    summaries: list[MetricSummary] = []
    all_criteria = sorted({r.name for v in verdicts for r in v.results})
    by_threshold = {t.criterion: t for t in thresholds}
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


def summarize(verdicts: list[CaseVerdict]) -> list[MetricSummary]:
    """All-up summary against the autonomous (strict) thresholds.

    Kept for callers/tests that want a single flat read; the ship decision
    itself should use summarize_by_tier so blast radius is respected.
    """
    return _summarize(verdicts, THRESHOLDS_AUTONOMOUS)


def summarize_by_tier(verdicts: list[CaseVerdict]) -> dict[str, list[MetricSummary]]:
    """Summaries split by blast_radius, each against its own threshold tier."""
    autonomous = [v for v in verdicts if v.blast_radius == "autonomous"]
    reviewed = [v for v in verdicts if v.blast_radius == "reviewed"]
    return {
        "autonomous": _summarize(autonomous, THRESHOLDS_AUTONOMOUS),
        "reviewed": _summarize(reviewed, THRESHOLDS_REVIEWED),
    }


@dataclass
class ShipDecision:
    ship: bool
    blocker_metrics: list[str]
    known_issues: list[str]
    tier: str = "autonomous"

    def render(self) -> str:
        head = "SHIP" if self.ship else "DO NOT SHIP"
        lines = [f"[{self.tier}] Verdict: {head}"]
        if self.blocker_metrics:
            lines.append("Blockers:")
            lines.extend(f"  - {m}" for m in self.blocker_metrics)
        if self.known_issues:
            lines.append("Known issues (next cycle):")
            lines.extend(f"  - {m}" for m in self.known_issues)
        return "\n".join(lines)


def _gate(summaries: list[MetricSummary], tier: str) -> ShipDecision:
    blockers = [m for m in summaries if m.blocker]
    issues = [m for m in summaries
              if m.against_threshold and not m.meets_threshold and not m.blocker]
    return ShipDecision(
        ship=len(blockers) == 0,
        blocker_metrics=[m.label for m in blockers],
        known_issues=[m.label for m in issues],
        tier=tier,
    )


def ship_gate(summaries: list[MetricSummary]) -> ShipDecision:
    """Single-tier gate (autonomous by convention) — kept for callers that
    only pass one summary list."""
    return _gate(summaries, "autonomous")


def ship_gate_by_tier(summaries_by_tier: dict[str, list[MetricSummary]]) -> dict[str, ShipDecision]:
    return {tier: _gate(summaries, tier) for tier, summaries in summaries_by_tier.items()}
