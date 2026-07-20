"""Objective RAG failure-mode classification.

Each mode implies a different fix, so naming the dominant mode — not "improve
RAG" — is the whole deliverable. Given a query's gold chunk ids and the
retriever's ranking, we classify the *retrieval* outcome deterministically. The
generation-side mode (chunk retrieved, answer not grounded in it) is measured
separately with a lexical grounding proxy; the model-quality version of that is
Artifact 02's grounding criterion.
"""
from __future__ import annotations

from rag.retriever import tokenize

# Content-bearing stopwords excluded from the grounding overlap so function
# words don't inflate it.
_STOP = frozenset(
    "the a an of to for and or in on at by is are be must under this that with "
    "as it its their they shall may can".split()
)


def classify(gold_ids: set[str], ranked: list[tuple[str, float]], k: int = 5,
             abstain_threshold: float = 0.1) -> str:
    """Return one of: hit, buried, wrong_chunk, no_fallback, correct_abstain.

    - answer not in corpus (gold empty): confident top hit -> no_fallback;
      else correct_abstain.
    - answer in corpus: gold at rank 1 -> hit; gold in top-k but outranked ->
      buried; gold absent from top-k -> wrong_chunk.
    """
    top_k = ranked[:k]
    top_ids = [cid for cid, _ in top_k]

    if not gold_ids:
        top_score = ranked[0][1] if ranked else 0.0
        return "no_fallback" if top_score >= abstain_threshold else "correct_abstain"

    if not any(cid in gold_ids for cid in top_ids):
        return "wrong_chunk"
    if top_ids and top_ids[0] in gold_ids:
        return "hit"
    return "buried"


def lexical_grounding(answer: str, chunk: str) -> float:
    """Fraction of the answer's content tokens that appear in the chunk. A cheap
    offline proxy for 'is the answer supported by the retrieved text'."""
    a = [t for t in tokenize(answer) if t not in _STOP]
    if not a:
        return 0.0
    c = set(tokenize(chunk))
    return sum(1 for t in a if t in c) / len(a)


def is_grounded(answer: str, chunk: str, threshold: float = 0.5) -> bool:
    return lexical_grounding(answer, chunk) >= threshold
