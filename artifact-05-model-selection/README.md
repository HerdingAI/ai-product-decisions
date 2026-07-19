# Artifact 05 — Model selection under constraints

> Pairs with [Unit 07 — Defining "good"](https://www.carlosarivero.com/units/unit-07-defining-good.html).
> Status: **planned — ships on cadence.**
> Evidence base: [`HerdingAI/document-ai-bench`](https://github.com/HerdingAI/document-ai-bench) — the benchmark this artifact reasons from.

## The problem

"Which model should we use?" gets answered two bad ways: by the leaderboard
(whatever topped the public benchmark this month), or by the demo (whatever
impressed the room). Both ignore the constraints that actually decide a
production selection — cost per call, latency, and the model's behavior on
*your* documents, not the benchmark's. Public benchmarks mislead in a
specific, predictable way: they measure average capability on a curated set,
which is rarely the distribution you ship on, and they hide cost and latency
entirely.

## The decision

Make model selection a **defensible workflow** with cost and latency as
first-class criteria, evidence drawn from a benchmark on documents like
yours, and the public-leaderboard result used only as a prior, not a verdict.

## Options and trade-offs

- **Pick the leaderboard leader** — zero effort, defensible-by-appeal-to-
  authority, and wrong whenever your distribution or your cost/latency budget
  differs from the benchmark's assumptions (usually).
- **Bake-off on your data** — the right evidence, expensive to do well, and
  easy to do badly (a handful of queries, no held-out set, no cost accounting).
- **Structured selection workflow (this artifact)** — the bake-off, but with
  the criteria and the decision rule stated up front, so the selection is
  auditable rather than vibes-with-a-table.

## What I'll measure

- Per candidate model, on the `document-ai-bench` task set: accuracy by
  category, hallucination rate, mean latency, and cost per task — the four
  axes that actually decide a selection.
- The gap between public-benchmark rank and on-distribution rank, made
  explicit: how often does the leaderboard leader stay the leader when cost
  and latency are counted?
- A selection rubric that turns the four axes into a decision under a stated
  budget (e.g., "≤$X/task, ≤Ys p95, accuracy ≥Z"), so the selection changes
  visibly when the budget changes.

## What I'd ship, and why

The selection workflow and the rubric — reusable across every future model
choice — with one worked example drawn from `document-ai-bench` as the
receipts. The artifact is the method; the specific model it picks today is
obsolete in a quarter. The method isn't.

_Planned: a selection runner over the `document-ai-bench` results, the
cost/latency/accuracy rubric, and a worked selection under a stated budget.
No code committed yet — ships when the cadence reaches it, ≤2 hrs/wk._