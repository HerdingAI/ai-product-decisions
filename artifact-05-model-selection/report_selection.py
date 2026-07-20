#!/usr/bin/env python3
"""Worked model-selection example over the real document-ai-bench results.

Runs the selection workflow under several stated budgets and prints the
decision — showing the pick change as constraints change, and where it
diverges from the public-leaderboard leader. All numbers come from the
benchmark's already-computed aggregates; this script adds no model calls.
"""
from __future__ import annotations

import json
from pathlib import Path

from selection.core import Budget, leaderboard_leader, load_models, select

RESULTS = (Path(__file__).resolve().parents[2]
           / "document-ai-bench" / "results" / "results.json")

# Named budgets = concrete product scenarios. Each is a real trade-off a PM
# would actually state, not an abstract knob.
SCENARIOS = [
    ("No constraints (leaderboard glance)", Budget(), "accuracy"),
    ("Interactive SLA: p-latency <= 3s, accuracy >= 75%",
     Budget(max_latency_ms=3000, min_accuracy=0.75), "accuracy"),
    ("High-stakes: hallucination <= 17%, accuracy >= 80%",
     Budget(max_hallucination=0.17, min_accuracy=0.80), "accuracy"),
    ("Cost-first batch job: accuracy >= 75%, cheapest wins",
     Budget(min_accuracy=0.75), "cost"),
]


def _fmt(m):
    return (f"{m.name}  (acc {m.accuracy:.1%}, halluc {m.hallucination_rate:.1%}, "
            f"{m.mean_latency_ms:.0f}ms, ${m.cost_per_task:.5f}/task)")


def main() -> None:
    if not RESULTS.exists():
        raise SystemExit(f"benchmark results not found at {RESULTS}")
    models = load_models(json.loads(RESULTS.read_text()))
    leader = leaderboard_leader(models)
    print(f"Public-leaderboard leader (raw accuracy): {_fmt(leader)}\n")

    for label, budget, rank_by in SCENARIOS:
        sel = select(models, budget, rank_by=rank_by)
        print(f"### {label}  (rank by {rank_by})")
        if sel.winner is None:
            print("  -> no model satisfies this budget")
        else:
            flip = " [FLIPS from leaderboard]" if sel.flipped_from_leaderboard else ""
            print(f"  -> pick: {_fmt(sel.winner)}{flip}")
        for name, reason in sel.rejected.items():
            print(f"       rejected {name}: {reason}")
        print()


if __name__ == "__main__":
    main()
