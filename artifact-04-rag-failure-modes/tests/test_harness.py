"""The harness maps a query set through a retriever into a failure-mode
distribution — the one number that tells a PM which fix to fund. Pinned here on
a tiny corpus so the aggregation is verified independently of the real data.
"""
from rag.harness import evaluate
from rag.retriever import TfidfRetriever


def test_evaluate_produces_per_query_modes_and_distribution():
    docs = {
        "g1": "colorado insurers must test predictive models for discrimination",
        "d1": "colorado insurers governance senior management oversight",
        "far": "illinois biometric consent unrelated topic",
    }
    retr = TfidfRetriever(docs)
    queries = [
        {"id": "hit1", "query": "illinois biometric consent", "gold_chunk_ids": ["far"]},
        {"id": "abs1", "query": "what is the fine amount schedule", "gold_chunk_ids": []},
    ]
    out = evaluate(retr, queries, k=3, abstain_threshold=0.1)
    modes = {r["id"]: r["mode"] for r in out["records"]}
    assert modes["hit1"] == "hit"
    assert modes["abs1"] in ("no_fallback", "correct_abstain")
    # distribution sums to number of queries
    assert sum(out["distribution"].values()) == 2
