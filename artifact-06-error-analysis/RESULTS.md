# RESULTS — error analysis & the improvement flywheel

**Question:** a pass rate tells you *that* something is wrong; it never tells you
*what to fix*. The highest-leverage eval skill isn't running the eval — it's
reading the failures: clustering them into categories, and catching the case
where the **criterion itself** has drifted from what anyone actually wants. This
turns the failures the other artifacts already produced into a ranked backlog.

It runs on **real, committed failures** — no new data, no labels invented here:
- Artifact 02's 85 judged cases (judge verdict vs. Carlos's human label per
  criterion).
- Artifact 03's 33 baseline agent crashes.

All three outputs are objective and reproducible: `python report_flywheel.py`.

## 1. Criteria drift — error analysis of the evaluator

For each criterion, how often the judge and the human disagree, and whether the
disagreement is **one-directional** (systematic = drift) or mixed (noise):

| Criterion | Agreement | Disagreements | Direction | Skew | Verdict |
|---|---:|---:|---|---:|---|
| appropriately-hedged | 35% | 55 | judge stricter | 100% | **DRIFT** |
| complete | 86% | 12 | judge stricter | 100% | ok |
| usable | 93% | 6 | judge stricter | 100% | ok |
| grounded | 95% | 4 | judge stricter | 100% | ok |

The detector flags **`appropriately-hedged`** and nothing else. That is the same
finding Artifact 02 reached by hand — the judge marks answers un-hedged wherever
they're confident, faithfully applying the rubric, while the labels were more
lenient — but here it falls out *mechanically* from the verdicts. The direction
matters: because the disagreement is 100% one-way (judge stricter), this is not
a coin-flip-hard criterion; it's a criterion whose **written standard and whose
labels have diverged**. The fix is to revise the rubric/labels — **not** to tune
the judge to agree, which would only game the metric. (This is the discipline
Artifact 02 documents; the flywheel is what surfaces it as an action.)

Note the detector's own guardrail: `complete` also disagrees 100% one-way but at
86% agreement, above the 80% floor, so it is *not* flagged. Drift requires both
frequency and direction — otherwise every hard criterion would look like drift.

## 2. Axial coding — which criteria fail together

Collapsing the 83 judged-failing cases by *which criteria they fail* turns a
scroll of individual failures into four categories:

| Count | Failure signature | Reading |
|---:|---|---|
| 51 | complete + appropriately-hedged + usable | the bulk: verbose, over-confident, and off-target together |
| 27 | complete + usable | on-target-ish but incomplete/unusable |
| 4 | all four (incl. grounded) | the genuinely broken answers (empty/ungrounded) |
| 1 | usable only | a lone edge case |

The 51-case cluster is the backlog's top item — and because it always includes
`appropriately-hedged`, it's entangled with the drift above: fix the hedging
criterion first, and the size and meaning of this cluster change. That ordering
(fix the eval before mining the failures it produces) is the whole point of a
flywheel over a dashboard.

## 3. Root-cause clustering — the agent crashes

The 33 Artifact 03 baseline crashes collapse to **one** signature (a 500 from a
single adapter incompatibility). One root cause, 33 symptoms — already fixed
test-first in `agentic-copilot`. The lesson the flywheel records: cluster before
you count, or you'd triage 33 tickets for one bug.

## Ranked action list (the deliverable)

1. **Fix the eval:** `appropriately-hedged` has drifted (35% agreement, judge
   stricter). Revise the rubric/labels to the real bar; do not touch the judge.
2. **Open-code the dominant failure cluster** (51 cases,
   complete+hedged+usable) — *after* the hedging fix re-scores them.
3. **Agent reliability:** one root cause drove all 33 baseline crashes; fixed,
   keep the regression test.

That is a pass rate turned into a prioritized backlog with the highest-leverage
item — a broken criterion — at the top, where a dashboard would never surface it.

## Scope & honest limits

- **Mechanical coding only.** Clustering here is by objective signature (which
  criteria failed, which exception fired). Subjective *open-coding* of trace
  themes — the qualitative read of *why* the 51 cases fail — is the human
  analyst's pass; this artifact builds the reproducible skeleton and the counts
  that rank it, not the qualitative labels.
- **Drift thresholds are explicit** (agreement < 80%, direction skew ≥ 80%) and
  live in `flywheel/drift.py`; they're a defensible default, not a law. Tune
  them to your tolerance — the point is that drift needs *both* frequency and
  direction, not either alone.

## What's built

`flywheel/drift.py` (4 tests) — objective criteria-drift detection.
`flywheel/clustering.py` (4 tests) — axial coding by mechanical signature.
`report_flywheel.py` — the flywheel over Artifacts 02 & 03's real failures.
**8 tests, TDD.** Closes the eval thread opened by Artifacts 01 and 02.
