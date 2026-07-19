#!/usr/bin/env python3
"""
Run the eval harness against a live agentic-copilot backend.

    # 1. Start the system under test (in the agentic-copilot repo)
    #    ./run.sh                       # backend on :8000, frontend on :3000
    #    or: python -m uvicorn agent.api:app --port 8000

    # 2. Run the harness
    python run.py --target http://127.0.0.1:8000

Writes results/results.json (machine-readable) and results/SUMMARY.md
(human-readable PM brief). Prints the ship decision to stdout.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from eval_harness.criteria import evaluate
from eval_harness.golden_set import GOLDEN_SET
from eval_harness.report import build
from eval_harness.runner import run_all


def main() -> int:
    ap = argparse.ArgumentParser(description="agentic-copilot eval harness")
    ap.add_argument("--target", default="http://127.0.0.1:8000",
                    help="base URL of the agentic-copilot backend (default :8000)")
    ap.add_argument("--out", default=str(Path(__file__).parent / "results"),
                    help="directory to write results.json and SUMMARY.md")
    args = ap.parse_args()

    print(f"Running {len(GOLDEN_SET)} cases against {args.target} …")
    raw = run_all(args.target, GOLDEN_SET)

    errored = [r for r in raw if not r.ok]
    if errored:
        print(f"\n{len(errored)} case(s) failed to reach the agent:", file=sys.stderr)
        for r in errored:
            print(f"  {r.case_id}: {r.error}", file=sys.stderr)
        return 1

    verdicts = [evaluate(c, r.response, r.tool_calls) for c, r in zip(GOLDEN_SET, raw)]
    results, summary, decision = build(raw, verdicts, args.target)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (out / "SUMMARY.md").write_text(summary)

    print()
    print(decision.render())
    print(f"\nWrote {out/'results.json'} and {out/'SUMMARY.md'}")
    return 0 if decision.ship else 2


if __name__ == "__main__":
    raise SystemExit(main())