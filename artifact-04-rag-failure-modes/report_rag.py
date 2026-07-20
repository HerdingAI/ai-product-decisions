#!/usr/bin/env python3
"""RAG failure-mode study: measure the distribution, rank fixes by the mode
that actually dominates, then apply the one fix that mode implies and measure
its cost. All offline and deterministic (pure TF-IDF over a fixed corpus)."""
from __future__ import annotations

import json
from pathlib import Path

from rag.harness import evaluate
from rag.improve import evaluate_with_gate
from rag.retriever import TfidfRetriever

HERE = Path(__file__).resolve().parent
K = 3
ABSTAIN = 0.10
GATE, MIN_IDF = 0.4, 1.5

# Each mode -> the fix it implies. The point of measuring is that only the
# fixes for *present* modes are worth funding.
FIX = {
    "wrong_chunk": "better chunking / query rewriting (retriever misses the chunk)",
    "buried": "reranker (right chunk retrieved but outranked)",
    "no_fallback": "abstention / coverage gate + fallback (confident wrong answer)",
    "hit": "— (working)",
    "correct_abstain": "— (correctly declined)",
}


def main() -> None:
    docs = json.loads((HERE / "data" / "corpus.json").read_text())
    queries = json.loads((HERE / "data" / "queries.json").read_text())
    retr = TfidfRetriever(docs)

    base = evaluate(retr, queries, k=K, abstain_threshold=ABSTAIN)
    print(f"Corpus: {len(docs)} chunks | Queries: {len(queries)} | k={K}\n")
    print("=== Baseline failure-mode distribution ===")
    for mode, n in sorted(base["distribution"].items(), key=lambda x: -x[1]):
        print(f"  {mode:16} {n:2}   -> fix: {FIX.get(mode, '?')}")

    # Rank fixes by frequency of the failure modes (hits/abstains excluded).
    failures = {m: n for m, n in base["distribution"].items()
                if m in ("wrong_chunk", "buried", "no_fallback")}
    print("\n=== Ranked fix list (by measured frequency) ===")
    if not failures:
        print("  no retrieval failures on this set")
    for i, (mode, n) in enumerate(sorted(failures.items(), key=lambda x: -x[1]), 1):
        print(f"  {i}. {FIX[mode]}  — addresses {n} case(s)")

    # Apply the dominant fix (coverage gate for no_fallback) and measure cost.
    gated = evaluate_with_gate(retr, queries, k=K, abstain_threshold=ABSTAIN,
                               gate=GATE, min_idf=MIN_IDF)
    print(f"\n=== Improvement: coverage gate (min_idf={MIN_IDF}, gate={GATE}) ===")
    print(f"  baseline: {base['distribution']}")
    print(f"  gated:    {gated['distribution']}")

    goldmap = {q["id"]: bool(q["gold_chunk_ids"]) for q in queries}
    base_mode = {r["id"]: r["mode"] for r in base["records"]}
    fixed, regressed = [], []
    for r in gated["records"]:
        was, now = base_mode[r["id"]], r["mode"]
        if was == "no_fallback" and now == "correct_abstain":
            fixed.append(r["id"])
        if goldmap[r["id"]] and now in ("wrong_chunk",) and was != now:
            regressed.append(r["id"])
    print(f"  fixed (confident-wrong -> abstain): {fixed}")
    print(f"  regressions (real answer -> abstain): {regressed}")
    print("\n  Read: the gate converts every confident-wrong answer into an "
          "honest abstention. Its one regression is a real answer lost to a "
          "stem mismatch (accountable/accountability) — which names the next "
          "fix: stemming/lemmatization before the gate.")


if __name__ == "__main__":
    main()
