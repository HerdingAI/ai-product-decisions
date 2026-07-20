"""One-off script: re-run the calibration set against the *fixed*
agentic-copilot server (the /api/chat tool_calls-results bug fix) and
merge the enriched `tool_calls` (now including each tool's actual return
value) back into labels/calibration_responses.json.

Safety rules, since this file holds Carlos's hand labels:
- Never overwrite `human_labels` — copied verbatim from the existing file.
- Only merge in the new `tool_calls` for a case if its `response` text is
  byte-identical to what's already on file. If the agent's response text
  drifted (non-determinism, model change, etc.), that case is left
  untouched and reported so a human can decide whether to re-label it.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from eval_judge.calibration_set import CALIBRATION_SET
from eval_judge.runner import run_all

LABELS_PATH = Path(__file__).resolve().parent / "labels" / "calibration_responses.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8012")
    parser.add_argument("--pace-seconds", type=float, default=0.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    existing = json.loads(LABELS_PATH.read_text())
    existing_by_id = {r["id"]: r for r in existing}

    results = run_all(args.base_url, CALIBRATION_SET, pace_seconds=args.pace_seconds)

    updated, unchanged_text_mismatch, failed = [], [], []
    for case, result in zip(CALIBRATION_SET, results):
        old = existing_by_id[case.id]
        if not result.ok:
            failed.append(case.id)
            continue
        if result.response != old["response"]:
            unchanged_text_mismatch.append(case.id)
            continue
        updated.append(case.id)
        old["tool_calls"] = result.tool_calls
        old["latency_ms"] = result.latency_ms

    print(f"Merged enriched tool_calls for {len(updated)} cases: {updated}")
    if unchanged_text_mismatch:
        print(f"SKIPPED (response text drifted, left untouched): {unchanged_text_mismatch}")
    if failed:
        print(f"SKIPPED (request failed): {failed}")

    if args.dry_run:
        print("--dry-run: not writing file")
        return

    LABELS_PATH.write_text(json.dumps(existing, indent=2))
    print(f"Wrote {LABELS_PATH}")


if __name__ == "__main__":
    main()
