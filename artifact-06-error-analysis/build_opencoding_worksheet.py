#!/usr/bin/env python3
"""Task-3 prep: assemble the dominant failure cluster's full traces into one
file for Carlos's open-coding pass — objective/mechanical assembly only, no
theme-naming or coding done here (that's the human analyst's read; see
RESULTS.md's "Scope & honest limits").

Pulls, for every case in the target failure signature: the query, the full
response text, and the judge's per-criterion reasons — everything needed to
read and name themes without cross-referencing three files by hand.
"""
from __future__ import annotations

import json
from pathlib import Path

from flywheel.clustering import criterion_failure_signature, cluster_by_signature

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "artifact-02-llm-as-judge" / "results" / "results.json"
CALIB = (HERE.parent / "artifact-02-llm-as-judge" / "labels"
         / "calibration_responses.json")
OUT = HERE / "opencoding_worksheet.md"

TARGET_SIGNATURE = "complete+appropriately-hedged+usable"


def main() -> None:
    judged = json.load(open(RESULTS))["cases"]
    responses = {c["id"]: c for c in json.load(open(CALIB))}

    clusters = cluster_by_signature(judged, criterion_failure_signature)
    target = clusters.get(TARGET_SIGNATURE)
    if target is None:
        raise SystemExit(f"No cluster found for signature {TARGET_SIGNATURE!r}; "
                          f"available: {list(clusters)}")

    ids = [c["id"] for c in judged if criterion_failure_signature(c) == TARGET_SIGNATURE]

    lines = [
        f"# Open-coding worksheet — {TARGET_SIGNATURE} cluster ({len(ids)} cases)",
        "",
        "Mechanical assembly only — no themes named here. For each case: the query, "
        "the full response, and the judge's per-criterion reasons. Read and name "
        "recurring themes (e.g. 'raw tool dump, no synthesis', 'confident despite "
        "partial data') in a new column or a separate notes file.",
        "",
        "**Re-run note:** this cluster is entangled with the `appropriately-hedged` "
        "drift (RESULTS.md §1/§2) — if the hedging labels/rubric get fixed, "
        "membership here will change. Re-run `build_opencoding_worksheet.py` after "
        "that fix before finalizing themes.",
        "",
    ]
    for cid in ids:
        case = next(c for c in judged if c["id"] == cid)
        resp = responses.get(cid, {})
        lines.append(f"## {cid} ({resp.get('group', '?')})")
        lines.append("")
        lines.append(f"**Query:** {resp.get('query', '(missing)')}")
        lines.append("")
        lines.append("**Response:**")
        lines.append("```")
        lines.append(resp.get("response", "(missing)") or "(empty)")
        lines.append("```")
        lines.append("")
        lines.append("**Judge reasons (failed criteria):**")
        for crit, passed in case["results"].items():
            if not passed:
                lines.append(f"- *{crit}*: {case['reasons'].get(crit, '')}")
        lines.append("")
        lines.append("**Theme (Carlos fills in):** _____")
        lines.append("")
        lines.append("---")
        lines.append("")

    OUT.write_text("\n".join(lines))
    print(f"Wrote {len(ids)} cases to {OUT}")


if __name__ == "__main__":
    main()
