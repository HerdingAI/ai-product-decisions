# Artifact 02 — LLM-as-judge, validated

> Pairs with [Unit 15 — LLM-as-judge](https://www.carlosarivero.com/units/unit-15-llm-as-judge.html) (the Hamel judge method + AIE Ch.3).
> Status: **built, pending a live judge pass.** Judge, bias probes, and report are implemented and unit-tested; 20 real calibration responses are collected from `agentic-copilot`. What's outstanding: hand-labeling the calibration set (Carlos) and an `OPENROUTER_API_KEY` to run the judge for real (D6: OpenRouter-only) — see "Current status" below.

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

Built and unit-tested (`pytest -q` → 42 passed): `eval_judge/providers.py`
(OpenRouter + a fake for tests), `eval_judge/judge.py` (prompt assembly,
strict-JSON parsing), `eval_judge/bias_probes.py` (consistency, verbosity,
sycophancy, order probes), `eval_judge/runner.py` (drives `agentic-copilot`),
`eval_judge/report.py` (agreement rate, Cohen's κ, probe summary, cost/latency).

`eval_judge/calibration_set.py` has 20 open-ended cases across grounding,
compound-query, hedge, and usability groups. `collect_responses.py` has
already been run once against a local `agentic-copilot` instance — real
responses are in `labels/calibration_responses.json`, with a `human_labels`
field per case left `null` pending hand-labeling.

**What's outstanding, and whose it is:**
- **Hand-labeling** `labels/calibration_responses.json` — Carlos's task, not
  automatable; the judge's validity rests on this being a real human
  judgment, not a fabricated one.
- **A live judge pass** — needs `OPENROUTER_API_KEY` (D6: OpenRouter is the
  sole model-provider standard here too). Once set:
  `python run.py --judge-model <openrouter-slug>` judges every collected
  response, runs the bias probes, and writes `results/results.json` +
  `results/SUMMARY.md`. Without labels, the summary still reports judge
  verdicts, bias-probe flags, and cost/latency — it just says "not yet
  hand-labeled" instead of an agreement number, rather than showing a
  fake 0% or 100%.

One finding already visible from the raw (unjudged) responses: case C-03
asks about the NAIC model bulletin and gets back Colorado SB 26-189 content
instead — a candidate grounding miss worth checking once judged.