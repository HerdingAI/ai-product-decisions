"""Run a query set through the workflow arm and compute the comparison
arithmetic: coverage (fraction the fixed rules serve without falling back),
tool-call volume, latency percentiles, and cost (zero for this arm).

This is the labels-independent half of Artifact 03. The quality half — is a
*served* answer actually good — is judged later with Artifact 02's method on
the same query set, so agent and workflow are scored identically.
"""
from __future__ import annotations

from .executor import Registry, execute
from .router import route


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * pct
    lo, hi = int(k), min(int(k) + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def run_workflow(queries: list[str], registry: Registry) -> dict:
    """Route + execute each query; return per-query records and a summary."""
    records = []
    for q in queries:
        plan = route(q)
        res = execute(plan, registry)
        records.append({
            "query": q,
            "routed": bool(plan),
            "refused": not plan,
            "n_tool_calls": len(res.tool_calls),
            "response": res.response,
            "tool_calls": res.tool_calls,
            "latency_ms": res.latency_ms,
            "cost_usd": res.cost_usd,
        })

    n = len(records)
    served = [r for r in records if r["routed"]]
    latencies = [r["latency_ms"] for r in records]
    summary = {
        "n": n,
        "coverage_rate": (len(served) / n) if n else 0.0,
        "refused": sum(1 for r in records if r["refused"]),
        # mean tool calls over *served* queries (refusals make no calls).
        "mean_tool_calls": (sum(r["n_tool_calls"] for r in served) / len(served))
                           if served else 0.0,
        "p50_latency_ms": _percentile(latencies, 0.50),
        "p95_latency_ms": _percentile(latencies, 0.95),
        "total_cost_usd": sum(r["cost_usd"] for r in records),
    }
    return {"records": records, "summary": summary}
