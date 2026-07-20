"""The value of a RAG failure study is naming *which* mode dominates, because
each mode implies a different fix. These pin the objective classifier: given a
query's gold chunks and the retriever's ranking, decide wrong-chunk vs. buried
vs. hit vs. no-fallback — plus a lexical grounding proxy for the generation-side
mode (retrieved the chunk, answer didn't use it).
"""
from rag.failure_modes import classify, is_grounded, lexical_grounding


def _ranked(*pairs):
    return list(pairs)


def test_hit_when_gold_is_rank_one():
    m = classify(gold_ids={"g"}, ranked=_ranked(("g", 0.9), ("x", 0.2)), k=5)
    assert m == "hit"


def test_buried_when_gold_present_but_outranked():
    m = classify(gold_ids={"g"}, ranked=_ranked(("x", 0.8), ("g", 0.3)), k=5)
    assert m == "buried"


def test_wrong_chunk_when_no_gold_in_top_k():
    m = classify(gold_ids={"g"}, ranked=_ranked(("x", 0.8), ("y", 0.3), ("g", 0.1)), k=2)
    assert m == "wrong_chunk"


def test_no_fallback_when_answer_absent_but_retriever_confident():
    # gold empty = answer isn't in the corpus; a confident top hit means the
    # retriever surfaced an irrelevant chunk instead of abstaining.
    m = classify(gold_ids=set(), ranked=_ranked(("x", 0.6)), k=5,
                 abstain_threshold=0.1)
    assert m == "no_fallback"


def test_correct_abstain_when_answer_absent_and_scores_low():
    m = classify(gold_ids=set(), ranked=_ranked(("x", 0.02)), k=5,
                 abstain_threshold=0.1)
    assert m == "correct_abstain"


def test_lexical_grounding_fraction_and_flag():
    chunk = "Colorado SB 21-169 requires insurers to test AI models for bias"
    grounded_answer = "Insurers must test AI models for bias under SB 21-169"
    hallucinated = "The statute mandates quarterly board audits and fines"
    assert lexical_grounding(grounded_answer, chunk) > 0.6
    assert lexical_grounding(hallucinated, chunk) < 0.3
    assert is_grounded(grounded_answer, chunk, threshold=0.5) is True
    assert is_grounded(hallucinated, chunk, threshold=0.5) is False
