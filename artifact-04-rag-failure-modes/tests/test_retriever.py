"""A RAG failure-mode study needs a retriever whose behaviour is fully
determined by the corpus (no network, no embeddings API), so the failure modes
we attribute to retrieval are reproducible. A pure TF-IDF cosine retriever
gives us that: same corpus + query -> same ranking, every time.
"""
import math

from rag.retriever import TfidfRetriever, tokenize


def test_tokenize_lowercases_and_splits_on_nonalpha():
    assert tokenize("SB 21-169: AI risk!") == ["sb", "21", "169", "ai", "risk"]


def test_exact_term_match_ranks_top():
    docs = {
        "a": "Colorado insurance AI governance testing requirements",
        "b": "California privacy consumer data broker rules",
        "c": "generic boilerplate about weather and sports",
    }
    r = TfidfRetriever(docs)
    ranked = r.retrieve("Colorado AI governance testing", k=3)
    assert ranked[0][0] == "a"
    # scores are descending
    scores = [s for _, s in ranked]
    assert scores == sorted(scores, reverse=True)


def test_idf_downweights_ubiquitous_terms():
    # "the" appears everywhere -> near-zero idf -> shouldn't drive ranking.
    docs = {
        "a": "the reranker improves buried chunk recall",
        "b": "the the the the the the the the the the",
    }
    r = TfidfRetriever(docs)
    ranked = r.retrieve("reranker buried chunk", k=2)
    assert ranked[0][0] == "a"


def test_no_overlap_returns_zero_scores():
    docs = {"a": "insurance regulation", "b": "lending compliance"}
    r = TfidfRetriever(docs)
    ranked = r.retrieve("astronomy telescope nebula", k=2)
    assert all(math.isclose(s, 0.0) for _, s in ranked)


def test_k_limits_results_and_covers_all_docs_when_large():
    docs = {str(i): f"term{i} shared" for i in range(5)}
    r = TfidfRetriever(docs)
    assert len(r.retrieve("shared", k=2)) == 2
    assert len(r.retrieve("shared", k=99)) == 5
