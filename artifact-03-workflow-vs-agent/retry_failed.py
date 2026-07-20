#!/usr/bin/env python3
"""Re-drive only the cases that errored in a prior agent-arm run and merge the
fresh records back in. Used after the adapter kwarg-tolerance fix: the 67
cases that already succeeded are unaffected by that fix, so only the failed
ones need re-running. Idempotent — re-running with no remaining failures is a
no-op. Recomputes summary / recovery / by_group from the merged records."""
from __future__ import annotations

import json
import time
from pathlib import Path

import httpx

from agent_arm.analysis import fallback_recovery, summarize, AgentRecord
from run_agent_arm import _drive_one, _sys_prompt_chars, CALIB, OUT
from workflow.router import route

BASE_URL = "http://127.0.0.1:8020"
PRICE_IN, PRICE_OUT = 0.10, 0.30
PACE = 3.5


def main() -> None:
    data = json.loads(OUT.read_text())
    cases = {c["id"]: c for c in json.loads(CALIB.read_text())}
    sys_chars = _sys_prompt_chars()

    failed = [r["case_id"] for r in data["records"] if not r["ok"]]
    print(f"Retrying {len(failed)} previously-failed cases: {failed}")
    if not failed:
        print("Nothing to retry.")
        return

    rec_by_id = {r["case_id"]: r for r in data["records"]}
    det = data.get("details", {})
    with httpx.Client() as client:
        for i, cid in enumerate(failed):
            if i and PACE:
                time.sleep(PACE)
            rec, d = _drive_one(client, BASE_URL, cases[cid], sys_chars,
                                PRICE_IN, PRICE_OUT)
            rec_by_id[cid] = rec.__dict__
            det[cid] = d
            flag = "ok " if rec.ok else "ERR"
            print(f"  [{i+1:2}/{len(failed)}] {cid:6} {flag} "
                  f"served={int(rec.served)} tools={rec.n_tool_calls} "
                  f"{rec.latency_ms:7.0f}ms")

    # Rebuild ordered records in original case order.
    order = [c["id"] for c in json.loads(CALIB.read_text())]
    merged = [rec_by_id[cid] for cid in order]
    records = [AgentRecord(**r) for r in merged]
    queries = {cid: cases[cid]["query"] for cid in order}

    groups: dict[str, dict] = {}
    for r in records:
        g = groups.setdefault(r.group, {"served": 0, "total": 0})
        g["total"] += 1
        g["served"] += int(r.served)

    data["records"] = merged
    data["details"] = det
    data["summary"] = summarize(records)
    data["fallback_recovery"] = fallback_recovery(records, queries, route)
    data["by_group"] = groups
    OUT.write_text(json.dumps(data, indent=2))

    s, rc = data["summary"], data["fallback_recovery"]
    print(f"\nMerged. Served {s['served']}/{s['n']} ({s['coverage_rate']:.0%}), "
          f"errors {s['errors']}. Recovery {rc['agent_recovered']}/"
          f"{rc['workflow_gaps']} ({rc['recovery_rate']:.0%}).")
    print(f"p50 {s['p50_latency_ms']:.0f}ms p95 {s['p95_latency_ms']:.0f}ms "
          f"mean_tools {s['mean_tool_calls']:.2f} est ${s['total_cost_usd']:.4f}")


if __name__ == "__main__":
    main()
