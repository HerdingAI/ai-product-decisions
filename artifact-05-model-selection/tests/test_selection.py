"""Model selection is a *defensible workflow*, not a leaderboard glance: cost
and latency are first-class constraints, and the right pick changes when the
budget changes. These pin that logic — loading benchmark aggregates, filtering
by an explicit budget with a reason per rejection, ranking the feasible set,
and making the leaderboard-vs-constrained gap explicit.
"""
import math

from selection.core import (
    Budget,
    ModelStats,
    leaderboard_leader,
    load_models,
    select,
)

# A small fixture mirroring document-ai-bench's aggregate shape.
RAW = {
    "task_count": 10,
    "models": ["fast_ok", "slow_best", "cheap_weak"],
    "per_model": {
        "fast_ok": {"aggregate": {
            "accuracy": 0.80, "hallucination_rate": 0.20,
            "mean_latency_ms": 1000.0, "total_cost_usd": 0.50,
            "category_accuracy": {"extraction": 0.9}}},
        "slow_best": {"aggregate": {
            "accuracy": 0.90, "hallucination_rate": 0.10,
            "mean_latency_ms": 8000.0, "total_cost_usd": 1.00,
            "category_accuracy": {"extraction": 0.95}}},
        "cheap_weak": {"aggregate": {
            "accuracy": 0.60, "hallucination_rate": 0.40,
            "mean_latency_ms": 500.0, "total_cost_usd": 0.02,
            "category_accuracy": {"extraction": 0.7}}},
    },
}


def test_load_computes_cost_per_task():
    models = load_models(RAW)
    by = {m.name: m for m in models}
    assert len(models) == 3
    assert math.isclose(by["fast_ok"].cost_per_task, 0.05)      # 0.50 / 10
    assert math.isclose(by["cheap_weak"].cost_per_task, 0.002)  # 0.02 / 10
    assert by["slow_best"].accuracy == 0.90


def test_leaderboard_leader_is_raw_accuracy_max():
    models = load_models(RAW)
    assert leaderboard_leader(models).name == "slow_best"


def test_budget_flips_the_pick_vs_leaderboard():
    # Under a 2s p-latency ceiling, the raw accuracy leader (slow_best, 8s) is
    # infeasible; the pick must flip to the best *feasible* model.
    models = load_models(RAW)
    sel = select(models, Budget(max_latency_ms=2000), rank_by="accuracy")
    assert leaderboard_leader(models).name == "slow_best"
    assert sel.winner.name == "fast_ok"
    assert sel.flipped_from_leaderboard is True
    assert "slow_best" in sel.rejected
    assert "latency" in sel.rejected["slow_best"].lower()


def test_no_budget_keeps_leaderboard_leader():
    models = load_models(RAW)
    sel = select(models, Budget(), rank_by="accuracy")
    assert sel.winner.name == "slow_best"
    assert sel.flipped_from_leaderboard is False
    assert sel.rejected == {}


def test_min_accuracy_and_max_hallucination_reject_with_reasons():
    models = load_models(RAW)
    sel = select(models, Budget(min_accuracy=0.75, max_hallucination=0.25),
                 rank_by="cost")
    # cheap_weak fails both accuracy and hallucination; only fast_ok & slow_best feasible.
    assert "cheap_weak" in sel.rejected
    # ranked by cost ascending among feasible → fast_ok ($0.05) beats slow_best ($0.10)
    assert sel.winner.name == "fast_ok"


def test_infeasible_budget_yields_no_winner():
    models = load_models(RAW)
    sel = select(models, Budget(max_cost_per_task=0.0), rank_by="accuracy")
    assert sel.winner is None
    assert len(sel.rejected) == 3
