# Artifact 02 — LLM-as-judge, validated

> Pairs with [Unit 15 — LLM-as-judge](https://www.carlosarivero.com/units/unit-15-llm-as-judge.html) (the Hamel judge method + AIE Ch.3).
> Status: **judge validated against human labels.** Judge, bias probes, and report are implemented and unit-tested; 87 real calibration responses collected from `agentic-copilot` and hand-labeled by Carlos, then judged by `deepseek/deepseek-v4-flash`.
>
> **Numbers:** Judge–human agreement, per criterion: `complete` 86% (κ=0.29), `usable` 93% (κ=0.38); `grounded` 95% and `appropriately-hedged` 35% are **unvalidated** — the human labels have zero variance on both, so κ=0.00 by construction (see [`RESULTS.md`](RESULTS.md)). Cost: **$0.039** for the 85-case run (~$0.0005/case), p95 latency 43.4 s/call. The headline result is a *finding about the calibration set*, not a green light — half the rubric can't yet be scored against the labels on hand.

## The problem

Artifact 01's harness decides ship/no-ship on ten hand-labeled cases with
deterministic criteria. That works for the canonical paths and fails the
moment you need to score a hundred open-ended answers, or judge whether a
response *really* answered the question instead of merely being non-empty and
grounded. The deterministic criteria can't see nuance; a human can, but a
human can't score a thousand responses a week.

## The decision

Use an LLM as the judge — but **validated against human labels first**, so
the judge's score is a calibrated proxy for a human's, not a vibe. The
decision is not "can an LLM grade responses" (yes, sometimes). It is "do I
trust this judge enough to let it gate releases," and that is an empirical
question with a measurable answer: agreement rate with humans, on the cases
humans labeled.

## Options and trade-offs

- **Likert-scale judge (1–5 quality)** — common, and noisy. Two graders
  rarely agree on a 5-point scale; a judge that agrees with humans 60% of the
  time on a Likert score is barely better than chance and hides
  disagreement in the middle of the scale.
- **Binary judge (pass/fail against a rubric criterion)** — less
  expressive, but agreement is a real number you can act on. Chosen for the
  primary signal; Likert kept only as a secondary, reported-with-caveats
  signal.
- **No judge, only humans** — gold standard, does not scale, and humans
  drift over time too. Rejected as the only signal; kept as the calibration
  anchor.

## What I'll measure

- Judge-vs-human agreement rate, per criterion, on a labeled set (the same
  golden set extended with open-ended cases).
- Where the judge breaks: the specific failure modes — sycophancy (agrees
  with a hinted "correct" answer), position bias, verbosity preference
  (longer = higher score), and rubric-blind spots.
- The cost of a judged run vs. a human-judged run, so the trade-off is
  explicit.
- Inter-rater agreement between humans as the ceiling the judge is measured
  against — a judge that agrees with humans more than humans agree with each
  other is a red flag, not a win.

## What I'd ship, and why

A judge I have measured, with the agreement rate and the known breakage
published alongside it — not a judge I trust because it sounded reasonable.
The ship gate from Artifact 01 gets a second tier: deterministic criteria for
the canonical paths, validated judge for the open-ended tail. Neither tier is
trusted blindly; both carry their measured error rate.

## System under test

Same as Artifact 01: `agentic-copilot` responses, judged against the criteria
the harness already defines — so the two artifacts compose rather than
forking.

## Current status

Built and unit-tested (`pytest -q` → 60 passed): `eval_judge/providers.py`
(OpenRouter + a fake for tests, with 429 retry/backoff), `eval_judge/judge.py`
(prompt assembly, strict-JSON parsing, reasoning-model token budget),
`eval_judge/bias_probes.py` (consistency, verbosity, sycophancy, order probes),
`eval_judge/pipeline.py` (fault-tolerant, parallel evaluation — one bad verdict
can't abort the run), `eval_judge/runner.py` (drives `agentic-copilot`),
`eval_judge/report.py` (agreement rate, Cohen's κ, probe summary, cost/latency).

`eval_judge/calibration_set.py` defines 100 open-ended cases across grounding,
compound-query, hedge, and usability groups. **87 are collected and hand-labeled
by Carlos**; the judge pass ran over them with `deepseek/deepseek-v4-flash`
(`--reasoning-effort high --workers 8`), writing `results/results.json` +
`results/SUMMARY.md`. The failure-pattern analysis and trust verdict are in
[`RESULTS.md`](RESULTS.md).

**What's outstanding:**
- **Collect + label the remaining 13 cases** (C-06–C-18) to reach N=100 —
  `python collect_new_cases.py --pace-seconds 4` (idempotent), then Carlos labels.
- **Add genuine negatives to the reference set.** The pass surfaced that Carlos
  labeled `grounded` and `appropriately-hedged` `True` on *all* 87 cases, which
  forces κ=0.00 and leaves both criteria unvalidated (RESULTS.md §2). Fixing this
  needs label *variance* — real `False` cases — not just more cases.

To re-run: `export OPENROUTER_API_KEY=…` then
`python run.py --judge-model deepseek/deepseek-v4-flash --reasoning-effort high
--workers 8` (D6: OpenRouter is the sole model-provider standard here too).