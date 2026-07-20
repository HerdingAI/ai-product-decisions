"""Collect agent responses for calibration cases that aren't yet in
labels/calibration_responses.json, and append them as *unlabeled* records
(human_labels: null).

Why unlabeled: Carlos is the sole human labeler (RUBRIC.md / SAMPLING.md).
This script may add the agent-side data (query, response, tool_calls with
results, latency) so the cases are label-ready — it must never invent the
human labels. Existing labeled records are preserved byte-for-byte; only
brand-new case ids are appended. Output is ordered to match CALIBRATION_SET.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from eval_judge.calibration_set import CALIBRATION_SET
from eval_judge.runner import run_all

LABELS_PATH = Path(__file__).resolve().parent / "labels" / "calibration_responses.json"
CRITERIA = ["grounded", "complete", "appropriately-hedged", "usable"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8012")
    parser.add_argument("--pace-seconds", type=float, default=0.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    existing = json.loads(LABELS_PATH.read_text())
    existing_by_id = {r["id"]: r for r in existing}

    new_cases = [c for c in CALIBRATION_SET if c.id not in existing_by_id]
    print(f"{len(existing)} existing records; {len(new_cases)} new cases to collect.")
    if not new_cases:
        print("Nothing to collect.")
        return

    results = run_all(args.base_url, new_cases, pace_seconds=args.pace_seconds)
    by_case = {r.case_id: r for r in results}

    added, failed = [], []
    for case in new_cases:
        r = by_case[case.id]
        if not r.ok:
            failed.append(case.id)
            continue
        existing_by_id[case.id] = {
            "id": case.id,
            "group": case.group,
            "query": case.query,
            "note": case.note,
            "ok": True,
            "response": r.response,
            "tool_calls": r.tool_calls,
            "latency_ms": r.latency_ms,
            "error": "",
            # Sole-labeler discipline: left null for Carlos to fill in.
            "human_labels": None,
        }
        added.append(case.id)

    # Re-order to match CALIBRATION_SET; keep any existing records not in the set.
    ordered = [existing_by_id[c.id] for c in CALIBRATION_SET if c.id in existing_by_id]

    print(f"Collected {len(added)} new records: {added}")
    if failed:
        print(f"FAILED (left out, will retry): {failed}")

    labeled = sum(1 for r in ordered if r.get("human_labels"))
    print(f"Total records now: {len(ordered)} ({labeled} labeled, "
          f"{len(ordered) - labeled} awaiting Carlos's labels)")

    if args.dry_run:
        print("--dry-run: not writing file")
        return

    LABELS_PATH.write_text(json.dumps(ordered, indent=2))
    print(f"Wrote {LABELS_PATH}")


if __name__ == "__main__":
    main()
