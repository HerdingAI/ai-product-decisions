#!/usr/bin/env python3
"""Task-2 prep: assemble the shared-served-set answer pairs Carlos needs to
quality-judge the workflow vs. agent comparison.

Objective/scriptable half only — this produces (query, workflow_response,
agent_response) triples for every case *both* arms served, with a randomized
left/right label so blind judging isn't order-biased (same discipline as the
Artifact 02 order bias probe). No quality judgment happens here; the labels
list is emitted empty for Carlos to fill in.

Workflow arm: run offline against the real reg_atlas / regfin_bench tool
functions (deterministic, no network, no LLM).
Agent arm: hit a live agentic-copilot instance and capture full response text
(the existing results/agent_arm.json only stored a 200-char preview).
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
import uuid
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
CALIB = (HERE.parent / "artifact-02-llm-as-judge" / "labels"
         / "calibration_responses.json")
AGENTIC_COPILOT = Path(
    "/tmp/claude-1000/-home-buntu/1d7995a9-5210-493c-98b8-0fb76f5b6752"
    "/scratchpad/agentic-copilot-fresh")
OUT = HERE / "results" / "quality_pairs.json"


def _build_workflow_registry():
    sys.path.insert(0, str(AGENTIC_COPILOT))
    from mcp_servers.reg_atlas import server as reg_atlas
    from mcp_servers.regfin_bench import server as regfin_bench

    return {
        "query_by_jurisdiction": lambda a: reg_atlas.query_by_jurisdiction(**a),
        "query_by_sector": lambda a: reg_atlas.query_by_sector(**a),
        "query_by_framework": lambda a: reg_atlas.query_by_framework(**a),
        "list_all_jurisdictions": lambda a: reg_atlas.list_all_jurisdictions(**a),
        "get_regulation_by_id": lambda a: reg_atlas.get_regulation_by_id(**a),
        "get_eu_ai_act_article": lambda a: reg_atlas.get_eu_ai_act_article(**a),
        "query_by_model": lambda a: regfin_bench.query_by_model(**a),
        "query_by_article": lambda a: regfin_bench.query_by_article(**a),
        "compare_models": lambda a: regfin_bench.compare_models(**a),
        "get_best_model_for_article": lambda a: regfin_bench.get_best_model_for_article(**a),
        "list_all_models": lambda a: regfin_bench.list_all_models(**a),
        "list_all_articles": lambda a: regfin_bench.list_all_articles(**a),
    }


def _run_workflow_arm(cases: list[dict]) -> dict[str, dict]:
    sys.path.insert(0, str(HERE))
    from workflow.harness import run_workflow

    registry = _build_workflow_registry()
    queries = [c["query"] for c in cases]
    out = run_workflow(queries, registry)
    by_id = {}
    for case, rec in zip(cases, out["records"]):
        by_id[case["id"]] = {"served": rec["routed"], "response": rec["response"]}
    return by_id


def _drive_one_full(client, base_url, case, retries=3):
    refusal_markers = ("I don't have", "I do not have", "outside")
    last_err = None
    for attempt in range(retries):
        thread = f"qualitypairs-{case['id']}-{uuid.uuid4().hex[:8]}"
        try:
            r = client.post(base_url.rstrip("/") + "/api/chat",
                             json={"message": case["query"], "thread_id": thread},
                             timeout=120.0)
            r.raise_for_status()
            data = r.json()
            response = (data.get("response", "") or "").strip()
            served = bool(response) and not any(
                response.startswith(m) for m in refusal_markers)
            if served or attempt == retries - 1:
                return {"served": served, "response": response}
            last_err = "empty/refused response, retrying"
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
        time.sleep(2.0 * (attempt + 1))  # backoff before retry
    return {"served": False, "response": f"(error after {retries} attempts: {last_err})"}


def _run_agent_arm(cases: list[dict], base_url: str, pace: float) -> dict[str, dict]:
    by_id = {}
    with httpx.Client() as client:
        for i, case in enumerate(cases):
            if i and pace:
                time.sleep(pace)
            by_id[case["id"]] = _drive_one_full(client, base_url, case)
            print(f"  [{i+1:3}/{len(cases)}] {case['id']:6} "
                  f"served={int(by_id[case['id']]['served'])}")
    return by_id


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="http://127.0.0.1:8012")
    ap.add_argument("--pace-seconds", type=float, default=0.3)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    cases = json.loads(CALIB.read_text())
    print(f"Running workflow arm over {len(cases)} cases (offline, real tools)...")
    workflow = _run_workflow_arm(cases)

    print(f"Running agent arm over {len(cases)} cases against {args.base_url}...")
    agent = _run_agent_arm(cases, args.base_url, args.pace_seconds)

    rng = random.Random(args.seed)
    pairs = []
    for case in cases:
        cid = case["id"]
        w, a = workflow.get(cid), agent.get(cid)
        if not w or not a or not w["served"] or not a["served"]:
            continue
        order = ["workflow", "agent"]
        rng.shuffle(order)
        left, right = order
        responses = {"workflow": w["response"], "agent": a["response"]}
        pairs.append({
            "case_id": cid,
            "group": case.get("group", "?"),
            "query": case["query"],
            "left_arm": left,
            "right_arm": right,
            "left_response": responses[left],
            "right_response": responses[right],
            "human_quality_labels": None,
        })

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(pairs, indent=2))
    raw_out = OUT.with_name("quality_pairs_raw_arms.json")
    raw_out.write_text(json.dumps({"workflow": workflow, "agent": agent}, indent=2))
    print(f"\n{len(pairs)}/{len(cases)} cases served by both arms — "
          f"shared quality-judging set written to {OUT} "
          f"(raw per-arm output in {raw_out})")


if __name__ == "__main__":
    main()
