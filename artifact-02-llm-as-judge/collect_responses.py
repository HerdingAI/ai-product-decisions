"""One-off script: run the calibration set against a live agentic-copilot
server and dump raw responses to labels/calibration_responses.json for
Carlos to hand-label (grounded/complete/appropriately-hedged/usable per
case). Not part of the pytest suite — this hits a real running server.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from eval_judge.calibration_set import CALIBRATION_SET
from eval_judge.runner import run_all

OUT_PATH = Path(__file__).resolve().parent / "labels" / "calibration_responses.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8011")
    parser.add_argument("--pace-seconds", type=float, default=0.0)
    args = parser.parse_args()

    results = run_all(args.base_url, CALIBRATION_SET, pace_seconds=args.pace_seconds)

    failed = [r for r in results if not r.ok]
    if failed:
        for r in failed:
            print(f"FAILED {r.case_id}: {r.error}")

    records = []
    for case, result in zip(CALIBRATION_SET, results):
        records.append({
            "id": case.id,
            "group": case.group,
            "query": case.query,
            "note": case.note,
            "ok": result.ok,
            "response": result.response,
            "tool_calls": result.tool_calls,
            "latency_ms": result.latency_ms,
            "error": result.error,
            # Carlos fills these in by hand; left null until labeled.
            "human_labels": {
                "grounded": None,
                "complete": None,
                "appropriately-hedged": None,
                "usable": None,
            },
        })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(records, indent=2))
    ok_count = sum(1 for r in results if r.ok)
    print(f"Wrote {len(records)} cases ({ok_count} ok, {len(failed)} failed) to {OUT_PATH}")


if __name__ == "__main__":
    main()
