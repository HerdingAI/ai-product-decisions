#!/usr/bin/env python3
"""Unblind Carlos's quality judgments and tally workflow-vs-agent wins on the
shared-served set.

`results/quality_pairs.json` stores each pair in blind left/right order (Carlos
judged without seeing which arm was which); `left_arm`/`right_arm` reveal the
mapping only after judging. This maps each `winner` (left|right|tie) back to the
arm it names and reports overall + per-group win counts. Pure aggregation over
the judged file — no judgment happens here.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

PAIRS = Path(__file__).resolve().parent / "results" / "quality_pairs.json"


def winning_arm(pair: dict) -> str:
    w = pair["human_quality_labels"]["winner"]
    return "tie" if w == "tie" else pair[f"{w}_arm"]


def tally(pairs: list[dict]) -> tuple[Counter, dict[str, Counter]]:
    overall: Counter = Counter()
    by_group: dict[str, Counter] = defaultdict(Counter)
    for p in pairs:
        arm = winning_arm(p)
        overall[arm] += 1
        by_group[p["group"]][arm] += 1
    return overall, by_group


def main() -> None:
    pairs = json.loads(PAIRS.read_text())
    overall, by_group = tally(pairs)
    n = len(pairs)
    print(f"Shared-served quality judgments (n={n}):")
    print(f"  workflow {overall['workflow']}  |  agent {overall['agent']}  "
          f"|  tie {overall['tie']}")
    print("\nPer group:")
    for g in sorted(by_group):
        c = by_group[g]
        print(f"  {g:10} workflow {c['workflow']:>2}  agent {c['agent']:>2}  tie {c['tie']:>2}")


if __name__ == "__main__":
    main()
