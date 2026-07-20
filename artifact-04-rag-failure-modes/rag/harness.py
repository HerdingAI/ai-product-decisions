"""Run a query set through a retriever and produce the failure-mode
distribution — plus enough per-query detail (gold rank, top hit) to read the
failures, not just count them."""
from __future__ import annotations

from collections import Counter

from rag.failure_modes import classify


def _gold_rank(gold_ids: set[str], ranked: list[tuple[str, float]]) -> int | None:
    """1-based rank of the best-ranked gold chunk, or None if absent."""
    for i, (cid, _) in enumerate(ranked, start=1):
        if cid in gold_ids:
            return i
    return None


def evaluate(retriever, queries: list[dict], k: int = 5,
             abstain_threshold: float = 0.1) -> dict:
    records = []
    for q in queries:
        gold = set(q.get("gold_chunk_ids", []))
        ranked = retriever.retrieve(q["query"], k=max(k, 10))
        mode = classify(gold, ranked, k=k, abstain_threshold=abstain_threshold)
        records.append({
            "id": q["id"],
            "query": q["query"],
            "mode": mode,
            "gold_rank": _gold_rank(gold, ranked),
            "top_hit": ranked[0][0] if ranked else None,
            "top_score": round(ranked[0][1], 4) if ranked else 0.0,
            "note": q.get("note", ""),
        })
    dist = Counter(r["mode"] for r in records)
    return {"records": records, "distribution": dict(dist)}
