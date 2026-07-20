"""Model selection under constraints.

Turns a benchmark's per-model aggregates into a *defensible* pick: cost and
latency are first-class filters, not afterthoughts, and the selected model
changes visibly when the budget changes. The public-leaderboard leader (raw
accuracy max) is reported only as a prior — `select()` says whether the
constrained pick flips away from it, and gives a reason for every rejection.

Pure logic over already-computed benchmark numbers (document-ai-bench); no
model calls here.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ModelStats:
    name: str
    accuracy: float
    hallucination_rate: float
    mean_latency_ms: float
    cost_per_task: float
    category_accuracy: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class Budget:
    """Optional constraints; None means 'no limit on this axis'."""
    max_cost_per_task: float | None = None
    max_latency_ms: float | None = None
    min_accuracy: float | None = None
    max_hallucination: float | None = None


@dataclass
class Selection:
    winner: ModelStats | None
    ranked_feasible: list[ModelStats]
    rejected: dict[str, str]          # model name -> reason
    leaderboard_leader: str | None
    flipped_from_leaderboard: bool


# rank_by -> (stat attribute, ascending?) — how to order the *feasible* set.
_RANK_KEYS = {
    "accuracy": ("accuracy", False),
    "cost": ("cost_per_task", True),
    "latency": ("mean_latency_ms", True),
    "hallucination": ("hallucination_rate", True),
}


def load_models(raw: dict) -> list[ModelStats]:
    """Build ModelStats from a document-ai-bench results dict. cost_per_task is
    derived from total_cost_usd / task_count so per-task cost is comparable
    across runs of different sizes."""
    task_count = raw.get("task_count") or 1
    out: list[ModelStats] = []
    for name in raw["models"]:
        agg = raw["per_model"][name]["aggregate"]
        out.append(ModelStats(
            name=name,
            accuracy=agg["accuracy"],
            hallucination_rate=agg["hallucination_rate"],
            mean_latency_ms=agg["mean_latency_ms"],
            cost_per_task=agg["total_cost_usd"] / task_count,
            category_accuracy=dict(agg.get("category_accuracy", {})),
        ))
    return out


def leaderboard_leader(models: list[ModelStats]) -> ModelStats | None:
    """The pick a naive leaderboard glance gives: highest raw accuracy, ignoring
    cost and latency entirely. This is the prior the constrained selection is
    measured against."""
    return max(models, key=lambda m: m.accuracy, default=None)


def _reject_reason(m: ModelStats, b: Budget) -> str | None:
    if b.max_cost_per_task is not None and m.cost_per_task > b.max_cost_per_task:
        return (f"cost/task ${m.cost_per_task:.4f} > budget "
                f"${b.max_cost_per_task:.4f}")
    if b.max_latency_ms is not None and m.mean_latency_ms > b.max_latency_ms:
        return (f"latency {m.mean_latency_ms:.0f}ms > budget "
                f"{b.max_latency_ms:.0f}ms")
    if b.min_accuracy is not None and m.accuracy < b.min_accuracy:
        return f"accuracy {m.accuracy:.1%} < required {b.min_accuracy:.1%}"
    if b.max_hallucination is not None and m.hallucination_rate > b.max_hallucination:
        return (f"hallucination {m.hallucination_rate:.1%} > allowed "
                f"{b.max_hallucination:.1%}")
    return None


def select(models: list[ModelStats], budget: Budget,
           rank_by: str = "accuracy") -> Selection:
    """Filter by the budget (recording a reason per rejection), rank the
    feasible set by `rank_by`, and report whether the pick flipped away from
    the public-leaderboard leader."""
    if rank_by not in _RANK_KEYS:
        raise ValueError(f"rank_by must be one of {sorted(_RANK_KEYS)}, "
                         f"got {rank_by!r}")
    attr, ascending = _RANK_KEYS[rank_by]

    feasible: list[ModelStats] = []
    rejected: dict[str, str] = {}
    for m in models:
        reason = _reject_reason(m, budget)
        if reason:
            rejected[m.name] = reason
        else:
            feasible.append(m)

    ranked = sorted(feasible, key=lambda m: getattr(m, attr),
                    reverse=not ascending)
    winner = ranked[0] if ranked else None
    leader = leaderboard_leader(models)
    flipped = bool(winner and leader and winner.name != leader.name)
    return Selection(
        winner=winner,
        ranked_feasible=ranked,
        rejected=rejected,
        leaderboard_leader=leader.name if leader else None,
        flipped_from_leaderboard=flipped,
    )
