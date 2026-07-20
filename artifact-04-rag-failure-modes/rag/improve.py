"""The one improvement, chosen from the measured failure distribution.

The dominant failure is no_fallback: for queries whose answer isn't in the
corpus, the retriever still returns a confident chunk. A raw score threshold
can't separate these (an irrelevant-but-confident chunk can outscore a
relevant-but-terse one). The signal that *does* separate them is coverage of the
query's **distinctive** (high-idf) terms: an answerable query's rare terms are
present in the right chunk; an unanswerable query's rare terms ("penalty",
"fine", "stipend") are absent from every chunk. We abstain when the top chunk
fails that coverage gate.
"""
from __future__ import annotations

from collections import Counter

from rag.failure_modes import classify
from rag.retriever import tokenize


def covered_fraction(retriever, query: str, chunk_id: str,
                     min_idf: float = 1.0) -> float:
    """Fraction of the query's distinctive terms that appear in the given chunk.

    Distinctive = high-idf terms present in the corpus, **plus terms absent from
    the corpus entirely** — an absent query term is the strongest unanswerable
    signal, so it must count as uncovered rather than be ignored. 1.0 only when
    the query has no distinctive terms to gate on."""
    idf = retriever._idf
    # Absent-from-corpus terms are treated as maximally distinctive.
    absent_idf = (max(idf.values()) + 1.0) if idf else min_idf
    q_distinctive = {t for t in tokenize(query)
                     if idf.get(t, absent_idf) >= min_idf}
    if not q_distinctive:
        return 1.0
    chunk_tokens = set(retriever._tokens[chunk_id])
    return len(q_distinctive & chunk_tokens) / len(q_distinctive)


def evaluate_with_gate(retriever, queries: list[dict], k: int = 5,
                       abstain_threshold: float = 0.1, gate: float = 0.5,
                       min_idf: float = 1.0) -> dict:
    """Like harness.evaluate, but abstain (drop all results) when the top
    chunk's distinctive-term coverage is below `gate`. gate=0.0 disables it."""
    records = []
    for q in queries:
        gold = set(q.get("gold_chunk_ids", []))
        ranked = retriever.retrieve(q["query"], k=max(k, 10))
        if ranked and gate > 0.0:
            cov = covered_fraction(retriever, q["query"], ranked[0][0], min_idf)
            if cov < gate:
                ranked = []  # force abstention
        mode = classify(gold, ranked, k=k, abstain_threshold=abstain_threshold)
        records.append({"id": q["id"], "query": q["query"], "mode": mode,
                        "note": q.get("note", "")})
    return {"records": records, "distribution": dict(Counter(r["mode"] for r in records))}
