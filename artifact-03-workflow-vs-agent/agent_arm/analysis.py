"""Pure analysis for the agent arm.

The agent arm is `agentic-copilot` run on a *real* LLM: unlike the workflow's
fixed router, the agent decides its own tool calls and can recover on queries
the workflow fails closed on — at a per-query cost and latency the workflow
doesn't pay. These functions turn a run's raw per-query records into the
comparison numbers, and are kept free of any I/O so they're unit-testable.
"""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass


@dataclass
class AgentRecord:
    case_id: str
    group: str
    served: bool
    refused: bool
    n_tool_calls: int
    latency_ms: float
    est_cost_usd: float
    ok: bool
    error: str = ""


# Phrases a real LLM uses when it declines / can't ground an answer. Kept
# conservative: we'd rather count a hedged-but-substantive answer as *served*
# (the quality judge, not this heuristic, decides if it's any good) than
# inflate the refusal rate.
_REFUSAL_RE = re.compile(
    r"\b(i (?:do not|don't) have|i cannot|i can't|i'm unable|i am unable|"
    r"unable to (?:find|help|answer)|no information (?:on|about)|"
    r"i'm sorry,? (?:but )?i)\b",
    re.IGNORECASE,
)


def is_refusal(response: str) -> bool:
    """True if the agent produced no usable answer — empty, or an explicit
    decline. Mirrors the workflow arm's 'fails closed' so coverage is
    comparable across arms."""
    if not response or not response.strip():
        return True
    return bool(_REFUSAL_RE.search(response))


def estimate_cost_usd(prompt_chars: int, completion_chars: int,
                      price_in: float, price_out: float) -> float:
    """Estimate one query's cost. `/api/chat` returns no token usage, so we
    approximate tokens as chars/4 (the usual English rule of thumb) and price
    at the model's per-1M-token input/output rates. This is an *estimate*, and
    labelled as such wherever it surfaces — the latency and tool-call numbers
    are measured exactly; only cost is derived."""
    in_tokens = prompt_chars / 4
    out_tokens = completion_chars / 4
    return (in_tokens * price_in + out_tokens * price_out) / 1e6


def _percentile(values: list[float], pct: float) -> float:
    """Nearest-rank percentile — matches workflow/harness.py so both arms'
    latency percentiles are computed identically."""
    if not values:
        return 0.0
    ordered = sorted(values)
    k = max(1, math.ceil(pct / 100 * len(ordered)))
    return ordered[k - 1]


def summarize(records: list[AgentRecord]) -> dict:
    n = len(records)
    served = sum(1 for r in records if r.served)
    latencies = [r.latency_ms for r in records]
    return {
        "n": n,
        "served": served,
        "refused": sum(1 for r in records if r.refused),
        "coverage_rate": served / n if n else 0.0,
        "mean_tool_calls": (sum(r.n_tool_calls for r in records) / n) if n else 0.0,
        "tool_call_distribution": dict(Counter(r.n_tool_calls for r in records)),
        "p50_latency_ms": _percentile(latencies, 50),
        "p95_latency_ms": _percentile(latencies, 95),
        "total_cost_usd": sum(r.est_cost_usd for r in records),
        "mean_cost_usd": (sum(r.est_cost_usd for r in records) / n) if n else 0.0,
        "errors": sum(1 for r in records if not r.ok),
    }



def fallback_recovery(records: list[AgentRecord], queries: dict[str, str],
                      workflow_route) -> dict:
    """Of the queries the *workflow* fails closed on, how many does the agent
    serve? This is the core of the trade: the fallback the agent's LLM routing
    buys down, which the decision memo prices against its cost/latency.

    `queries` maps case_id -> query text; `workflow_route` is the workflow
    arm's `route` (returns an empty plan when it fails closed)."""
    gaps = 0
    recovered = 0
    for r in records:
        q = queries.get(r.case_id, "")
        workflow_served = bool(workflow_route(q))
        if not workflow_served:
            gaps += 1
            if r.served:
                recovered += 1
    return {
        "workflow_gaps": gaps,
        "agent_recovered": recovered,
        "recovery_rate": (recovered / gaps) if gaps else 0.0,
    }

