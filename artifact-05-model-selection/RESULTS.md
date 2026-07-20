# RESULTS — model selection under constraints

**Question:** "which model should we use?" is usually answered by leaderboard
(whatever topped a public benchmark this month) or by demo (whatever impressed
the room). Both ignore the constraints that actually decide a production pick —
cost per call, latency, and behavior on *your* documents. This makes selection a
**defensible workflow**: cost and latency are first-class filters, the benchmark
is evidence not verdict, and the pick changes visibly when the budget changes.

Evidence base: [`document-ai-bench`](https://github.com/HerdingAI/document-ai-bench)
— 45 regulated-document tasks (flagging, extraction, grounded QA, planted-error)
across 5 models, run live on OpenRouter. All numbers below are the benchmark's
already-computed aggregates; this artifact adds no model calls, only the
selection logic on top.

## The four axes that actually decide

| Model | Accuracy | Hallucination | Mean latency | Cost/task |
|---|---:|---:|---:|---:|
| meta-llama/llama-4-maverick | **83.7%** | 16.3% | 7920 ms | $0.00019 |
| openai/gpt-4o | 82.9% | 17.1% | **1123 ms** | $0.00125 |
| anthropic/claude-sonnet-5 | 80.7% | 19.3% | 6310 ms | $0.00278 |
| meta-llama/llama-3.3-70b-instruct | 78.3% | 21.7% | 8142 ms | **$0.00005** |
| google/gemini-2.5-pro | 69.4% | 30.6% | 7959 ms | $0.00090 |

Leaderboard leader (raw accuracy): **llama-4-maverick, 83.7%.** That is the only
number a leaderboard glance gives you — and on three of the four realistic
budgets below, it is the wrong pick.

## The pick changes with the budget

Reproduce: `python report_selection.py`. Four stated budgets, four selection
runs:

| Budget (product scenario) | Rank by | Winner | vs. leaderboard |
|---|---|---|---|
| No constraints | accuracy | llama-4-maverick | (same) |
| Interactive SLA: latency ≤ 3 s, acc ≥ 75% | accuracy | **gpt-4o** | **flips** |
| High-stakes: hallucination ≤ 17%, acc ≥ 80% | accuracy | llama-4-maverick | (same) |
| Cost-first batch: acc ≥ 75%, cheapest | cost | **llama-3.3-70b** | **flips** |

- **Interactive SLA flips to gpt-4o.** The leaderboard leader is 7920 ms — a
  7× miss on a 3 s interactive budget. *Every* model except gpt-4o (1123 ms) is
  rejected on latency, so the defensible pick is gpt-4o at a 0.8-point accuracy
  cost. A leaderboard glance would have shipped a model that blows the SLA.
- **High-stakes stays with maverick** — but for a real reason now, not
  authority: gpt-4o is rejected because its 17.1% hallucination just exceeds the
  17% ceiling, and maverick is the accuracy leader among the survivors. Same pick
  as the leaderboard, but arrived at defensibly.
- **Cost-first flips to llama-3.3-70b** — 25× cheaper per task than gpt-4o
  ($0.00005 vs $0.00125) while clearing a 75% accuracy floor. For a bulk
  back-office job with no latency pressure, paying for maverick or gpt-4o is
  waste.

## Reading it

The leaderboard leader won **1 of 4** realistic budgets outright. The point is
not that any one model is best — it's that **"best" is undefined until you state
the budget**, and once you do, the selection is mechanical and defensible. The
same rubric re-runs for free the next time constraints change or a new model
lands; the specific 2026 picks go obsolete, the workflow does not.

The gap this closes: a leaderboard optimizes average capability on a curated set
and hides cost and latency entirely. Three of these five models top the accuracy
chart within ~5 points of each other, but span a **25× cost range and a 7×
latency range** — precisely the axes a leaderboard omits and a production
decision lives or dies on.

## Honest limits

- **On-distribution ≠ your distribution.** These are `document-ai-bench`'s 45
  regulated-document tasks. The method (state a budget, filter, rank, show the
  flip) transfers; the specific accuracy numbers are only valid for documents
  like the benchmark's. Swapping in your own task set is the intended use.
- **Accuracy/hallucination come from the benchmark's scorer** (see
  `document-ai-bench/RUBRIC.md`), including a control-task-aware planted-error
  heuristic — not a human re-label. Selection quality is bounded by the
  benchmark's scoring quality, which is documented in that spoke.
- **Latency is the benchmark's measured mean**, not a p95, and OpenRouter
  routing adds variance; treat the latency column as relative ordering, not an
  SLA guarantee.

## What's built

`selection/core.py` (7 tests, TDD): `load_models` (derives cost/task),
`Budget`, `select` (filter-with-reasons → rank → leaderboard-flip flag),
`leaderboard_leader`. `report_selection.py` — the worked example over the real
benchmark. `tests/test_real_data.py` locks the headline flip against the
committed benchmark results so this write-up can't drift from the data.
