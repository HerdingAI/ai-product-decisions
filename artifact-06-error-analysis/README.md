# Artifact 06 — Error analysis & the improvement flywheel

> Pairs with [Unit 14 — Error analysis](https://www.carlosarivero.com/units/unit-14-error-analysis.html) (the Hamel field guide — the highest-ROI unit in the series).
> Status: **shipped — drift detector + axial coding over real failures.** See [RESULTS.md](RESULTS.md). Closes the eval thread opened by Artifacts 01 and 02.
>
> **Numbers (over Artifacts 02 & 03's real, committed failures):** an objective criteria-drift detector re-derives the hand-found result — **`appropriately-hedged` drifts (35% judge–human agreement, 100% one-directional, judge stricter)** while the other three criteria hold (86–95%) — and correctly does *not* flag `complete` (86%, above the floor). Axial coding collapses 83 judged failures into **4 categories** (top: 51 cases co-failing complete+hedged+usable) and 33 agent crashes into **1** root cause. Rule: **fix the drifted criterion before mining the failures it produced; a dashboard would never surface a broken criterion as the top action.**

## The problem

A pass rate tells you *that* something is wrong. It does not tell you *what*
to fix. The highest-leverage AI-PM skill is not running evals — it is reading
the failures: open-coding the traces, finding the categories, and watching
for criteria drift (the rubric that stopped matching what users actually
care about). Eval without error analysis is a dashboard no one acts on; error
analysis is the flywheel that turns a pass rate into a backlog.

## The decision

Take the failures the harness produces and run them through a real
error-analysis pass — open coding, then axial coding into categories, then a
drift check on the criteria themselves. The output is a small, named set of
failure categories with counts and a recommended next action each, plus a
note on whether the criteria need revising.

## Options and trade-offs

- **Aggregate metrics only** — what dashboards give you. Tells you the
  number is down; does not tell you why. Fine for monitoring, useless for
  fixing.
- **Ad-hoc "let me read some failures"** — better than nothing, unbounded in
  effort, and produces no reusable categories. The next person re-does it
  from scratch.
- **Structured open/axial coding (this artifact)** — bounded effort, reusable
  category set, and it surfaces criteria drift — the failure mode where the
  eval itself is wrong rather than the system.

## What I'll measure

- Open-coded failure categories from a real batch of traces (drawn from
  `agentic-copilot` runs through the Artifact 01 harness).
- Axial coding: the merge into a small category set with counts.
- Criteria drift: cases where the harness's pass/fail disagrees with a human
  read — i.e., the criterion itself is miscalibrated, not the system.
- The action each category implies, ranked by expected lift per effort.

## What I'd ship, and why

The category set and the drift check — the artifacts that close the loop
between eval and improvement. This is the unit that makes the rest of the
eval thread pay off: Artifacts 01 and 02 produce the failures, this artifact
turns them into the next thing to build. Without it, the eval is a verdict;
with it, the eval is a flywheel.

_Shipped: an objective criteria-drift detector and axial-coding harness
(`flywheel/`, 8 tests, TDD) run over Artifacts 02 & 03's real committed failures,
plus the ranked action list (`report_flywheel.py`, `RESULTS.md`). The subjective
open-coding of trace themes is the human analyst's pass on top of this skeleton._