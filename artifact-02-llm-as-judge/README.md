# Artifact 02 — LLM-as-judge, validated

> Pairs with [Unit 15 — LLM-as-judge](https://www.carlosarivero.com/units/unit-15-llm-as-judge.html) (the Hamel judge method + AIE Ch.3).
> Status: **planned — ships on cadence**, after Artifact 01. The automation step that scales the criteria-first harness.

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

_Planned: runnable judge harness, a human-labeled calibration set, and an
agreement/breakage report. No code committed yet — ships when the cadence
reaches it, ≤2 hrs/wk._

## System under test

Same as Artifact 01: `agentic-copilot` responses, judged against the criteria
the harness already defines — so the two artifacts compose rather than
forking.