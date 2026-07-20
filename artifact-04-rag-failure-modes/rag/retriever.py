"""Pure-Python TF-IDF cosine retriever.

Deliberately offline and dependency-free: the whole point of the failure-mode
study is that retrieval behaviour is *determined by the corpus*, so the modes
we attribute to retrieval reproduce exactly. No embeddings API, no network, no
hidden state. This is a baseline retriever — realistic enough to exhibit the
canonical RAG failure modes (wrong chunk, buried chunk, no relevant chunk),
which is exactly what we want to measure and then fix.
"""
from __future__ import annotations

import math
import re
from collections import Counter

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


class TfidfRetriever:
    def __init__(self, docs: dict[str, str]):
        """docs: chunk_id -> chunk text."""
        self.doc_ids = list(docs)
        self._tokens = {cid: tokenize(text) for cid, text in docs.items()}
        n = len(self.doc_ids) or 1
        # Document frequency, then smoothed idf.
        df: Counter = Counter()
        for toks in self._tokens.values():
            df.update(set(toks))
        self._idf = {t: math.log((1 + n) / (1 + d)) + 1.0 for t, d in df.items()}
        self._vecs = {cid: self._vectorize(toks)
                      for cid, toks in self._tokens.items()}

    def _vectorize(self, tokens: list[str]) -> dict[str, float]:
        if not tokens:
            return {}
        tf = Counter(tokens)
        total = len(tokens)
        vec = {t: (c / total) * self._idf.get(t, 0.0) for t, c in tf.items()}
        return vec

    def retrieve(self, query: str, k: int = 5) -> list[tuple[str, float]]:
        """Return up to k (chunk_id, cosine_score) pairs, highest first."""
        qvec = self._vectorize(tokenize(query))
        scored = [(cid, _cosine(qvec, self._vecs[cid])) for cid in self.doc_ids]
        # Stable order: score desc, then doc_id for determinism on ties.
        scored.sort(key=lambda x: (-x[1], x[0]))
        return scored[:k]


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    # iterate the smaller vector
    if len(a) > len(b):
        a, b = b, a
    dot = sum(w * b.get(t, 0.0) for t, w in a.items())
    if dot == 0.0:
        return 0.0
    na = math.sqrt(sum(w * w for w in a.values()))
    nb = math.sqrt(sum(w * w for w in b.values()))
    return dot / (na * nb) if na and nb else 0.0
