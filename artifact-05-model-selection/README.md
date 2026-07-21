# Artifact 05 — Model selection under constraints

> Pairs with [Unit 07 — Defining "good"](https://www.carlosarivero.com/units/unit-07-defining-good.html).
> Status: **shipped — selection workflow + worked example over real benchmark data.** See [RESULTS.md](RESULTS.md).
> Evidence base: [`HerdingAI/document-ai-bench`](https://github.com/HerdingAI/document-ai-bench) — the benchmark this artifact reasons from.
>
> **Numbers (document-ai-bench, 45 tasks × 5 models, live OpenRouter):** the raw-accuracy leaderboard leader is **llama-4-maverick (83.7%)** — but it wins only **1 of 4** realistic budgets. Under a 3 s interactive latency SLA the pick **flips to gpt-4o** (1123 ms vs 7920 ms, −0.8 pt accuracy); a cost-first batch budget flips to **llama-3.3-70b** (25× cheaper/task). Across five models within ~5 accuracy points sit a **25× cost range and a 7× latency range** — the axes a leaderboard hides. Rule: **"best" is undefined until you state the budget; then selection is mechanical, auditable, and re-runs for free.**

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
  auditable rather than a bake-off with unstated criteria.

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
choice — with one worked example drawn from `document-ai-bench`. The artifact is the method; the specific model it picks today is
obsolete in a quarter. The method isn't.

_Shipped: a selection runner over the `document-ai-bench` results
(`selection/core.py`, 7 tests, TDD), the cost/latency/accuracy/hallucination
rubric, and four worked selections under stated budgets (`report_selection.py`,
`RESULTS.md`). Method transfers to any task set; the specific 2026 picks don't._