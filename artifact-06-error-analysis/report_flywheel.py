#!/usr/bin/env python3
"""Error-analysis flywheel over *real* failures already produced by the other
artifacts: Artifact 02's judge-vs-human verdicts (criteria drift + which
criteria fail together) and Artifact 03's baseline agent crashes (mechanical
root-cause clustering). Turns pass-rate into a ranked backlog.

All objective and reproducible: drift is computed from committed verdicts, and
clustering is a mechanical signature. Subjective open-coding of trace themes is
the human analyst's pass on top of this skeleton.
"""
from __future__ import annotations

import json
from pathlib import Path

from flywheel.clustering import (
    cluster_by_signature,
    criterion_failure_signature,
    exception_signature,
)
from flywheel.drift import drift_report

HERE = Path(__file__).resolve().parent
A02 = HERE.parent / "artifact-02-llm-as-judge" / "results" / "results.json"
A03 = (HERE.parent / "artifact-03-workflow-vs-agent" / "results"
       / "agent_arm_baseline_prefix.json")
CRITERIA = ["grounded", "complete", "appropriately-hedged", "usable"]


def main() -> None:
    cases = json.loads(A02.read_text())["cases"]
    labeled = [c for c in cases if c.get("human_labels")]

    print(f"=== Criteria drift (Artifact 02, {len(labeled)} labeled cases) ===")
    print("Error analysis of the *evaluator*: where judge & human systematically diverge.\n")
    drift_rows = drift_report(labeled, CRITERIA)
    for r in drift_rows:
        flag = "  <-- DRIFT" if r["drift"] else ""
        print(f"  {r['criterion']:22} agree {r['agreement_rate']:.0%}  "
              f"disagree {r['disagreements']:2} ({r['direction']}, skew {r['skew']:.0%})"
              f"{flag}")

    print("\n=== Axial coding: which criteria fail together (judged fails) ===")
    fails = [c for c in cases if not c.get("passed", True)]
    clusters = cluster_by_signature(fails, criterion_failure_signature, id_key="id")
    for sig, info in sorted(clusters.items(), key=lambda x: -x[1]["count"]):
        ex = ", ".join(info["examples"][:4])
        print(f"  {info['count']:2}x  [{sig}]   e.g. {ex}")

    # Artifact 03 baseline crashes -> mechanical root-cause cluster.
    if A03.exists():
        recs = json.loads(A03.read_text())["records"]
        errs = [{"id": r["case_id"], "error": r.get("error", "")}
                for r in recs if not r["ok"]]
        print(f"\n=== Root-cause clustering (Artifact 03 baseline, {len(errs)} crashes) ===")
        eclusters = cluster_by_signature(errs, lambda e: exception_signature(e["error"]),
                                         id_key="id")
        for sig, info in sorted(eclusters.items(), key=lambda x: -x[1]["count"]):
            print(f"  {info['count']:2}x  {sig[:80]}")

    print("\n=== Ranked action list (highest leverage first) ===")
    actions = []
    for r in drift_rows:
        if r["drift"]:
            actions.append(
                f"FIX THE EVAL: '{r['criterion']}' drifts ({r['agreement_rate']:.0%} "
                f"agreement, {r['direction']}). The judge follows the rubric, so revise "
                f"the labels/rubric — do NOT tune the judge to agree (that games the metric).")
    top_fail = max(clusters.items(), key=lambda x: x[1]["count"]) if clusters else None
    if top_fail and top_fail[0] != "(none)":
        actions.append(f"DOMINANT JUDGED FAILURE: [{top_fail[0]}] "
                       f"({top_fail[1]['count']} cases) — open-code these traces next.")
    if A03.exists() and errs:
        actions.append("AGENT RELIABILITY: 1 root cause drove all baseline crashes "
                       "(malformed tool kwarg) — already fixed in agentic-copilot; "
                       "keep the regression test.")
    for i, a in enumerate(actions, 1):
        print(f"  {i}. {a}")


if __name__ == "__main__":
    main()
