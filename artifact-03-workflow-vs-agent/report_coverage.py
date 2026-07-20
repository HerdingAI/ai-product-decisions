#!/usr/bin/env python3
"""Measure the workflow arm's *coverage* on the real query set.

Coverage — the fraction of realistic queries a fixed rule set serves without
falling back — is the one comparison metric computable with no LLM, no tools,
and no human labels: it depends only on the router. We run it over the same
100 queries Artifact 02 collected (same agent, same domain), so the
workflow-vs-agent comparison shares a query distribution.

The agent arm's coverage (measured later on a real model) is expected to be
higher; the gap, priced against the agent's cost/latency, is the artifact's
arithmetic. This script produces the workflow half now.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from workflow.router import route

CALIB = (Path(__file__).resolve().parent.parent
         / "artifact-02-llm-as-judge" / "labels" / "calibration_responses.json")


def main() -> None:
    records = json.loads(CALIB.read_text())
    by_group: Counter = Counter()
    served_by_group: Counter = Counter()
    served = 0
    for r in records:
        g = r.get("group", "?")
        by_group[g] += 1
        if route(r["query"]):
            served += 1
            served_by_group[g] += 1

    n = len(records)
    print(f"Workflow-arm coverage on {n} real queries: "
          f"{served}/{n} = {served / n:.0%}\n")
    print(f"{'group':14} {'served':>8} {'total':>6} {'coverage':>9}")
    for g in sorted(by_group):
        s, t = served_by_group[g], by_group[g]
        print(f"{g:14} {s:>8} {t:>6} {s / t:>8.0%}")
    print(f"\n{n - served} queries fall back (uncovered) — the workflow refuses "
          f"rather than guess. That fallback rate is what the agent's routing "
          f"buys down, at the cost/latency measured in the agent arm.")


if __name__ == "__main__":
    main()
