# Artifact 02 — LLM-as-judge, validated

> Pairs with [Unit 15 — LLM-as-judge](https://www.carlosarivero.com/units/unit-15-llm-as-judge.html) (the Hamel judge method + AIE Ch.3).
> Status: **judge measured against human labels — two criteria usable as screens, one run-sensitive, one broken.** Judge, bias probes, and report are implemented and unit-tested; 100 real calibration responses collected from `agentic-copilot` and hand-labeled by me (genuine `False` variance on every criterion), judged in a full live pass by `deepseek/deepseek-v4-flash`.
>
> **Numbers (95 judged of 100 labeled):** Judge–human agreement per criterion: `usable` 93% (κ=**0.56**), `complete` 86% (κ=**0.49**), `grounded` 95% (κ=0.26, run-sensitive on the empty-response edge case), `appropriately-hedged` **39% (κ=0.04, broken)**. 81 of 83 disagreements run one direction — judge=`False` / human=`True` — so the judge is a **conservative over-flagger** (high recall, lower precision): a review *screen*, not an autonomous *gate*, and needs ≥3-sample majority vote (23% single-run flip rate). The hedging criterion fires on incomplete/off-scope answers (a completeness defect — see Artifact 06's open-coding), carrying no independent signal; fix is a rubric `v1.1` narrowing it to genuine overconfidence. Cost: **$0.044** for the 95-case run (~$0.0005/case), p95 39.8 s/call. See [`RESULTS.md`](RESULTS.md).

## The problem

Artifact 01's harness decides ship/no-ship on ten hand-labeled cases with
deterministic criteria. That works for the canonical paths and fails the
moment you need to score a hundred open-ended answers, or judge whether a
response *really* answered the question instead of merely being non-empty and
grounded. The deterministic criteria can't see nuance; a human can, but a
human can't score a thousand responses a week.

## The decision

Use an LLM as the judge — but **validated against human labels first**, so
the judge's score is a calibrated proxy for a human's judgment, not an impression. The
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
compound-query, hedge, and usability groups. **All 100 are collected and
hand-labeled by me, with genuine `False` variance on every criterion**
(grounded 4 F, complete 79 F, appropriately-hedged 4 F, usable 88 F). A **full
live judge pass** ran with `deepseek/deepseek-v4-flash` (`--reasoning-effort high
--workers 8`) over all 100; 95 produced verdicts (5 are empty/parse-failure
responses), writing `results/results.json` + `results/SUMMARY.md`. The
failure-pattern analysis and trust verdict are in [`RESULTS.md`](RESULTS.md).

**What's outstanding (all optional — the artifact is at Definition of Done):**
- **Amend the hedging criterion to `v1.1`.** RESULTS.md §3: the judge over-fires
  `appropriately-hedged` on incomplete/off-scope answers (κ=0.04). Narrow the
  rubric to genuine overconfidence, then re-run under `judge_v1.1` and re-measure.
- **Define the empty-response case in the rubric.** RESULTS.md §2: `grounded` is
  run-sensitive only because the rubric is silent on no-claims responses; one line
  closes it (the labels already encode the ruling).

To re-run the full judge pass: `export OPENROUTER_API_KEY=…` then
`python run.py --judge-model deepseek/deepseek-v4-flash --reasoning-effort high
--workers 8`. To re-score agreement after a label change without re-judging:
`python regenerate_report.py`.