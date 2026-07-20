#!/usr/bin/env python3
"""Drive the *agent arm* — agentic-copilot on a real LLM — over the same 100
calibration queries the workflow arm was measured on, and record the
comparison numbers.

This is the thin HTTP shell; all classification/arithmetic lives in
`agent_arm/analysis.py` (unit-tested). We hit a running agentic-copilot
instance (default :8020) with a fresh thread_id per query so cases don't
contaminate each other through the agent's persisted memory, then measure
served/refused, tool-call count, latency, and an estimated per-query cost.

Latency and tool-call counts are measured exactly. Cost is an *estimate*:
`/api/chat` returns no token usage, so we approximate tokens as chars/4 over
the system prompt + query + tool results (input) and the answer + tool args
(output), priced at the model's per-1M-token rates (--price-in/--price-out).

Usage:
    python run_agent_arm.py --base-url http://127.0.0.1:8020 \
        --price-in 0.10 --price-out 0.30 --pace-seconds 0.5
"""
from __future__ import annotations

import argparse
import json
import time
import uuid
from pathlib import Path

import httpx

from agent_arm.analysis import (
    AgentRecord,
    estimate_cost_usd,
    fallback_recovery,
    is_refusal,
    summarize,
)
from workflow.router import route

HERE = Path(__file__).resolve().parent
CALIB = (HERE.parent / "artifact-02-llm-as-judge" / "labels"
         / "calibration_responses.json")
SYS_PROMPT = (HERE.parent.parent / "agentic-copilot" / "agent" / "system_prompt.py")
OUT = HERE / "results" / "agent_arm.json"


def _sys_prompt_chars() -> int:
    """Approximate the fixed system-prompt overhead the model processes on
    every call (best-effort; 0 if the file can't be read)."""
    try:
        return len(SYS_PROMPT.read_text())
    except OSError:
        return 0


def _drive_one(client, base_url, case, sys_chars, price_in, price_out):
    query = case["query"]
    thread = f"agentarm-{case['id']}-{uuid.uuid4().hex[:8]}"
    t0 = time.perf_counter()
    try:
        r = client.post(base_url.rstrip("/") + "/api/chat",
                        json={"message": query, "thread_id": thread}, timeout=120.0)
        r.raise_for_status()
        data = r.json()
        latency = (time.perf_counter() - t0) * 1000
        response = data.get("response", "") or ""
        tool_calls = data.get("tool_calls", []) or []
        # Input the model saw ~ system prompt + query + tool results fed back.
        tool_result_chars = sum(len(str(t.get("result", ""))) for t in tool_calls)
        tool_arg_chars = sum(len(str(t.get("args", ""))) for t in tool_calls)
        est_cost = estimate_cost_usd(
            prompt_chars=sys_chars + len(query) + tool_result_chars,
            completion_chars=len(response) + tool_arg_chars,
            price_in=price_in, price_out=price_out,
        )
        served = not is_refusal(response)
        return AgentRecord(
            case_id=case["id"], group=case.get("group", "?"),
            served=served, refused=not served,
            n_tool_calls=len(tool_calls), latency_ms=latency,
            est_cost_usd=est_cost, ok=True, error="",
        ), {"tool_calls": [t.get("tool") for t in tool_calls],
            "response_preview": response[:200]}
    except Exception as e:  # network / HTTP / parse
        latency = (time.perf_counter() - t0) * 1000
        return AgentRecord(
            case_id=case["id"], group=case.get("group", "?"),
            served=False, refused=True, n_tool_calls=0, latency_ms=latency,
            est_cost_usd=0.0, ok=False, error=f"{type(e).__name__}: {e}",
        ), {"tool_calls": [], "response_preview": ""}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="http://127.0.0.1:8020")
    ap.add_argument("--price-in", type=float, default=0.10,
                    help="assumed input $/1M tokens (estimate only)")
    ap.add_argument("--price-out", type=float, default=0.30,
                    help="assumed output $/1M tokens (estimate only)")
    ap.add_argument("--pace-seconds", type=float, default=0.5)
    ap.add_argument("--model", default="deepseek/deepseek-v4-flash")
    args = ap.parse_args()

    cases = json.loads(CALIB.read_text())
    sys_chars = _sys_prompt_chars()
    records: list[AgentRecord] = []
    details: dict[str, dict] = {}
    queries = {c["id"]: c["query"] for c in cases}

    print(f"Driving {len(cases)} queries against {args.base_url} "
          f"(model {args.model})...")
    with httpx.Client() as client:
        for i, case in enumerate(cases):
            if i and args.pace_seconds:
                time.sleep(args.pace_seconds)
            rec, det = _drive_one(client, args.base_url, case, sys_chars,
                                  args.price_in, args.price_out)
            records.append(rec)
            details[rec.case_id] = det
            flag = "ok " if rec.ok else "ERR"
            print(f"  [{i+1:3}/{len(cases)}] {rec.case_id:6} {flag} "
                  f"served={int(rec.served)} tools={rec.n_tool_calls} "
                  f"{rec.latency_ms:7.0f}ms")

    summary = summarize(records)
    recovery = fallback_recovery(records, queries, route)
    # per-group coverage, to compare against the workflow's group table.
    groups: dict[str, dict] = {}
    for r in records:
        g = groups.setdefault(r.group, {"served": 0, "total": 0})
        g["total"] += 1
        g["served"] += int(r.served)

    out = {
        "model": args.model,
        "base_url": args.base_url,
        "price_assumptions": {"in_per_1m": args.price_in,
                              "out_per_1m": args.price_out,
                              "note": "cost is an estimate; latency/tools measured"},
        "summary": summary,
        "fallback_recovery": recovery,
        "by_group": groups,
        "records": [r.__dict__ for r in records],
        "details": details,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))

    print(f"\nAgent arm: {summary['served']}/{summary['n']} served "
          f"({summary['coverage_rate']:.0%}), "
          f"{summary['errors']} errors")
    print(f"Recovered {recovery['agent_recovered']}/{recovery['workflow_gaps']} "
          f"workflow fallbacks ({recovery['recovery_rate']:.0%})")
    print(f"Latency p50 {summary['p50_latency_ms']:.0f}ms / "
          f"p95 {summary['p95_latency_ms']:.0f}ms; "
          f"mean tools {summary['mean_tool_calls']:.2f}; "
          f"est total ${summary['total_cost_usd']:.4f}")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
