"""The agent arm's comparison numbers come from a handful of pure functions
(served/refused classification, cost estimation, latency percentiles, and
fallback-recovery vs. the workflow). We pin those here so the HTTP driver
stays a thin, untested shell over tested logic — the same discipline the
workflow arm follows.
"""
import math

from agent_arm.analysis import (
    AgentRecord,
    estimate_cost_usd,
    fallback_recovery,
    is_refusal,
    summarize,
)


# ── served vs. refused ───────────────────────────────────────────────────────

def test_empty_response_is_refusal():
    assert is_refusal("") is True
    assert is_refusal("   ") is True


def test_explicit_refusal_phrases_detected():
    assert is_refusal("I'm sorry, I don't have information on that.") is True
    assert is_refusal("I cannot help with that request.") is True
    assert is_refusal("Unable to find anything matching your query.") is True


def test_substantive_answer_is_not_refusal():
    assert is_refusal(
        "Colorado's SB 21-169 requires insurers to test AI models for "
        "unfair discrimination and document governance."
    ) is False


# ── cost estimation ──────────────────────────────────────────────────────────

def test_cost_scales_with_text_and_is_nonnegative():
    cheap = estimate_cost_usd(prompt_chars=100, completion_chars=100,
                              price_in=0.10, price_out=0.30)
    dear = estimate_cost_usd(prompt_chars=100, completion_chars=10_000,
                             price_in=0.10, price_out=0.30)
    assert dear > cheap > 0.0
    # 10k completion chars ~= 2500 tokens; 2500/1e6 * $0.30 = $0.00075 (+ input)
    assert math.isclose(dear, (100 / 4 * 0.10 + 10_000 / 4 * 0.30) / 1e6,
                        rel_tol=1e-9)


# ── summary ──────────────────────────────────────────────────────────────────

def _rec(cid, served, n_tools, latency, cost, ok=True):
    return AgentRecord(case_id=cid, group="g", served=served, refused=not served,
                       n_tool_calls=n_tools, latency_ms=latency,
                       est_cost_usd=cost, ok=ok, error="")


def test_summarize_core_metrics():
    recs = [
        _rec("a", True, 1, 100.0, 0.001),
        _rec("b", True, 2, 300.0, 0.002),
        _rec("c", False, 0, 200.0, 0.0005),
    ]
    s = summarize(recs)
    assert s["n"] == 3
    assert s["served"] == 2
    assert math.isclose(s["coverage_rate"], 2 / 3)
    assert s["refused"] == 1
    assert math.isclose(s["mean_tool_calls"], (1 + 2 + 0) / 3)
    assert math.isclose(s["total_cost_usd"], 0.0035)
    assert s["p50_latency_ms"] == 200.0          # median of 100,200,300
    assert s["tool_call_distribution"] == {0: 1, 1: 1, 2: 1}


def test_summarize_p95_uses_nearest_rank_upper_tail():
    recs = [_rec(str(i), True, 1, float(i), 0.0) for i in range(1, 101)]
    s = summarize(recs)
    # 100 values 1..100; p95 nearest-rank -> the 95th value = 95.
    assert s["p95_latency_ms"] == 95.0


# ── fallback recovery vs. the workflow ───────────────────────────────────────

def test_fallback_recovery_counts_only_workflow_gaps():
    # workflow serves q1, fails closed on q2 & q3. Agent serves q1 & q2.
    def wf_route(q):
        return [1] if q == "q1" else []
    agent = [
        _rec("1", True, 1, 10, 0.0),   # q1 - both serve (not a gap)
        _rec("2", True, 1, 10, 0.0),   # q2 - workflow gap, agent recovers
        _rec("3", False, 0, 10, 0.0),  # q3 - workflow gap, agent also refuses
    ]
    queries = {"1": "q1", "2": "q2", "3": "q3"}
    rec = fallback_recovery(agent, queries, wf_route)
    assert rec["workflow_gaps"] == 2
    assert rec["agent_recovered"] == 1
    assert math.isclose(rec["recovery_rate"], 0.5)
