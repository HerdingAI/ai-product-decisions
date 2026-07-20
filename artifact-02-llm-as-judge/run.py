#!/usr/bin/env python3
"""
Run the LLM-as-judge over the collected calibration responses.

    # 1. Collect responses (only needed once, or after agentic-copilot changes)
    python collect_responses.py --base-url http://127.0.0.1:8011

    # 2. Hand-label labels/calibration_responses.json (Carlos, not this script)

    # 3. Run the judge + bias probes + agreement report
    export OPENROUTER_API_KEY=sk-...
    python run.py --judge-model anthropic/claude-3-haiku

Writes results/results.json (machine-readable) and results/SUMMARY.md
(human-readable). Requires OPENROUTER_API_KEY (D6/D11: OpenRouter is the
sole model-provider standard; no first-party key is used here).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from eval_judge.judge import Judge
from eval_judge.pipeline import evaluate
from eval_judge.providers import OpenRouterProvider, ProviderError
from eval_judge.report import build

RESPONSES_PATH = Path(__file__).parent / "labels" / "calibration_responses.json"


def main() -> int:
    ap = argparse.ArgumentParser(description="LLM-as-judge calibration run")
    ap.add_argument("--judge-model", default="anthropic/claude-3-haiku",
                    help="OpenRouter model slug to use as judge (default: claude-3-haiku)")
    ap.add_argument("--prompt-version", default="v1")
    ap.add_argument("--responses", default=str(RESPONSES_PATH))
    ap.add_argument("--out", default=str(Path(__file__).parent / "results"))
    ap.add_argument("--skip-probes", action="store_true",
                    help="skip bias probes (they re-call the judge 2-3x per case)")
    ap.add_argument("--reasoning-effort", default=None,
                    choices=["low", "medium", "high"],
                    help="OpenRouter reasoning effort for the judge model "
                         "(omit for non-reasoning models / provider default)")
    ap.add_argument("--workers", type=int, default=1,
                    help="concurrent judge calls (reasoning models are slow; "
                         ">1 parallelizes across cases)")
    args = ap.parse_args()

    responses_path = Path(args.responses)
    if not responses_path.exists():
        print(f"No responses file at {responses_path}. Run collect_responses.py first.",
              file=sys.stderr)
        return 1
    records = json.loads(responses_path.read_text())

    try:
        provider = OpenRouterProvider(model=args.judge_model,
                                      reasoning_effort=args.reasoning_effort)
    except ProviderError as e:
        print(f"Provider error: {e}", file=sys.stderr)
        print("Set OPENROUTER_API_KEY to run a real judge pass (D6: OpenRouter-only).",
              file=sys.stderr)
        return 1

    judge = Judge(provider, prompt_version=args.prompt_version)

    print(f"Judging {len(records)} cases with {args.judge_model} (prompt {args.prompt_version}) …")
    verdicts, probes, human_labels, failures = evaluate(
        judge, records, run_probes=not args.skip_probes, max_workers=args.workers)

    for cid, err in failures:
        print(f"  case {cid} failed and was skipped: {err[:200]}", file=sys.stderr)
    if failures:
        print(f"{len(failures)} case(s) failed to judge; agreement computed over "
              f"the {len(verdicts)} that parsed.", file=sys.stderr)

    results, summary = build(verdicts, human_labels, probes, target=args.judge_model)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (out / "SUMMARY.md").write_text(summary)

    print()
    print(summary)
    print(f"Wrote {out/'results.json'} and {out/'SUMMARY.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
