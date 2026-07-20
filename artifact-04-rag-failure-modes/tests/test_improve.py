"""The measured dominant failure is no_fallback: the retriever surfaces an
irrelevant chunk for unanswerable queries instead of abstaining, and a naive
score threshold can't fix it (an irrelevant-but-confident chunk can outscore a
relevant-but-terse one). The fix is a distinctive-term coverage gate: abstain
when the top chunk fails to cover the query's high-idf terms. Pinned here.
"""
from rag.improve import covered_fraction, evaluate_with_gate
from rag.retriever import TfidfRetriever


def test_covered_fraction_uses_distinctive_terms_only():
    docs = {"a": "penalty schedule fine amount", "b": "colorado insurers test models"}
    r = TfidfRetriever(docs)
    # "penalty schedule fine" are distinctive and all in doc a -> ~1.0
    assert covered_fraction(r, "penalty schedule fine", "a", min_idf=0.0) == 1.0
    # none of those distinctive terms are in doc b -> 0.0
    assert covered_fraction(r, "penalty schedule fine", "b", min_idf=0.0) == 0.0


def test_gate_converts_confident_irrelevant_hit_to_abstain():
    docs = {
        "test": "colorado insurers must test predictive models for discrimination",
        "gov": "colorado insurers governance senior management oversight review",
    }
    r = TfidfRetriever(docs)
    queries = [
        # answerable: distinctive terms covered -> stays a hit
        {"id": "ok", "query": "test predictive models discrimination", "gold_chunk_ids": ["test"]},
        # unanswerable but shares the common term "colorado" (so baseline is
        # confident, not a zero-overlap abstain); its distinctive terms
        # penalty/fine/schedule are absent -> the gate abstains.
        {"id": "bad", "query": "colorado penalty fine amount schedule", "gold_chunk_ids": []},
    ]
    base = {r_["id"]: r_["mode"] for r_ in
            evaluate_with_gate(r, queries, k=3, gate=0.0)["records"]}   # gate off
    gated = {r_["id"]: r_["mode"] for r_ in
             evaluate_with_gate(r, queries, k=3, gate=0.5)["records"]}  # gate on
    assert base["bad"] == "no_fallback"          # without the gate, confident wrong chunk
    assert gated["bad"] == "correct_abstain"     # with the gate, it abstains
    assert gated["ok"] == "hit"                  # and the real answer is untouched
