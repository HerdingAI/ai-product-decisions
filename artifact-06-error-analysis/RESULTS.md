# RESULTS — error analysis & the improvement flywheel

**Question:** a pass rate tells you *that* something is wrong; it never tells you
*what to fix*. The highest-leverage eval skill isn't running the eval — it's
reading the failures: clustering them into categories, and catching the case
where the **criterion itself** has drifted from what anyone actually wants. This
turns the failures the other artifacts already produced into a ranked backlog.

It runs on **real, committed failures** — no new data, no labels invented here:
- Artifact 02's 95 judged cases (judge verdict vs. Carlos's human label per
  criterion).
- Artifact 03's 33 baseline agent crashes.

All three outputs are objective and reproducible: `python report_flywheel.py`.

## 1. Criteria drift — error analysis of the evaluator

For each criterion, how often the judge and the human disagree, and whether the
disagreement is **one-directional** (systematic = drift) or mixed (noise):

| Criterion | Agreement | Disagreements | Direction | Skew | Verdict |
|---|---:|---:|---|---:|---|
| appropriately-hedged | 39% | 58 | judge stricter | 100% | **DRIFT** |
| complete | 86% | 13 | judge stricter | 100% | ok |
| usable | 93% | 7 | judge stricter | 100% | ok |
| grounded | 95% | 5 | judge stricter | 60% | ok (floor) |

(Full live judge pass over all 100 cases; 95 produced verdicts.) The detector flags
**`appropriately-hedged`** and nothing else. That is the same finding Artifact 02
reached by hand — the judge marks answers un-hedged wherever they're confident,
faithfully applying the rubric, while Carlos's labels reserve `hedged=False` for
genuine overconfidence — but here it falls out *mechanically*. The direction
matters: the hedging disagreement is 100% one-way (judge stricter), so this is not
a coin-flip-hard criterion; it's a criterion whose **written standard and human
standard have diverged**. Note `grounded` sits at 95% (above the 80% floor, not
flagged) with a mixed direction — its 5 disagreements are mostly the *empty-response
convention* where the judge is even inconsistent with itself (Artifact 02 §2), not a
systematic drift. The signal is specific, not a blanket "everything disagrees." The
fix for hedging is to revise the **rubric** (the labels are the authoritative human
bar) — **not** to tune the judge to agree, which would only game the metric.

Note the detector's own guardrail: `complete` also disagrees 100% one-way but at
86% agreement, above the 80% floor, so it is *not* flagged. Drift requires both
frequency and direction — otherwise every hard criterion would look like drift.

## 2. Axial coding — which criteria fail together

Collapsing the judged-failing cases by *which criteria they fail* turns a scroll
of individual failures into a few categories (fresh full pass):

| Count | Failure signature | Reading |
|---:|---|---|
| 56 | complete + appropriately-hedged + usable | the bulk: incomplete, "un-hedged," and off-target together |
| 28 | complete + usable | on-target-ish but incomplete/unusable |
| 3 | all four (incl. grounded) | the genuinely broken answers (empty/ungrounded) |
| 3 | other single/pair signatures | lone edge cases |

The dominant cluster is the backlog's top item. Mechanical signature says these
answers are "incomplete + un-hedged + unusable" together — but that's *what* they
fail, not *why*. For that you have to read the traces, which is §2.5.

## 2.5 Open-coding the dominant cluster — the *why*

Mechanical clustering gets you a pile of cases that all trip the same three
criteria; it cannot tell you they fail for **seven different reasons**. Carlos read
all 51 traces of the dominant cluster (`opencoding_worksheet_coded.md`) and named
the failure mode of each. The distribution is the payoff — a single "quality"
number would have hidden it:

| Theme | Count | The failure |
|---|---:|---|
| **T5** Judgment question answered with facts only | **13** | asked to predict/rate/assess → recites statute, takes no stance, bounds no uncertainty |
| **T2** Second half of a compound query silently dropped | **11** | "what does X say **and** which model scores best" → answers half, never flags the omission |
| **T4** Wrong-scope retrieval presented as the answer | **8** | insurance record returned for a credit-scoring ask; Colorado dump for a banking ask |
| **T3** Missing comparandum — comparison impossible | **7** | "compare NY to CO" with NY never retrieved → no comparison, gap unflagged |
| **T6** Unavailable item — error surfaced raw or buried | **5** | "Article 72" not in data → raw error, or buried under an adjacent-article dump |
| **T1** Raw dump, requested synthesis never performed | **4** | right records retrieved, but the one-line/board-deck synthesis never done |
| **T7** Empty response — silent failure | **3** | nothing returned at all, often to a trap question |

**What the themes say that the cluster couldn't.** The 51 "quality failures" are
really **three root causes**, and ranking by them changes the backlog:

- **No synthesis/answer layer over retrieval (T1+T4+T5+T6 = 30 cases, 59%).** The
  data was retrieved (or a gap existed) and the system stopped there — it never
  filtered to scope, took a stance, or wrote the requested form. This is one fix
  (a synthesis step that consumes tool output and answers the *question asked*)
  and it addresses the majority of the cluster. **Highest leverage.**
- **Incomplete retrieval / no query decomposition (T2+T3 = 18 cases, 35%).** The
  system answered from what one lookup returned and never fetched the second
  jurisdiction / benchmark / query-half. Fix is multi-hop: decompose the ask,
  retrieve each part, and *flag* any part still missing.
- **No graceful-gap handling (T6+T7 = 8 cases).** Unavailable items and empty
  results should degrade to an explicit "not in the data," not a raw error or
  silence.

Crucially, **none of the seven themes is "overconfident / poorly hedged."** The
51 cases fail on *synthesis, completeness, and scope* — which is exactly why the
judge's `appropriately-hedged=False` verdict on all of them is a mislabel (§1
drift, and Artifact 02 §3): the judge attached a hedging label to what are really
completeness failures. The open-coding is the independent confirmation that the
drift is real and that the fix is to re-scope the criterion, not the labels.

**Anchor remediation on the themes, not on this run's cluster membership.** Carlos
open-coded the 51 traces the *frozen* judge run put in the dominant cluster. A
*fresh* live pass puts **56** cases there, overlapping the coded set on only 37 —
14 rotated out, 19 in — because judge verdicts are nondeterministic (the 23%
consistency flip, Artifact 02 §6). That churn is not a defect in the coding; it is
the point: **the seven themes are properties of the *responses*** (a raw-dump answer
is a raw dump however the judge scores it that run), so they are stable, while the
mechanical cluster boundary rides on noisy verdicts and is not. This is precisely
the re-run caveat `build_opencoding_worksheet.py` prints, now demonstrated — and the
reason the ranked backlog below is keyed to theme root-causes, not to "the N cases
the judge flagged this pass."

## 3. Root-cause clustering — the agent crashes

The 33 Artifact 03 baseline crashes collapse to **one** signature (a 500 from a
single adapter incompatibility). One root cause, 33 symptoms — already fixed
test-first in `agentic-copilot`. The lesson the flywheel records: cluster before
you count, or you'd triage 33 tickets for one bug.

## Ranked action list (the deliverable)

Two tracks fall out — fix the *evaluator*, then work the *product* backlog the
(now-trusted) evaluator surfaced:

**Evaluator:**
1. **Fix the eval:** `appropriately-hedged` has drifted (39% agreement, judge
   stricter). Re-scope the **rubric** to genuine overconfidence (Carlos's labels
   are now the authoritative bar); do not touch the judge to force agreement.

**Product (the 51-case cluster, open-coded — §2.5):**
2. **Add a synthesis/answer layer over retrieval** — the single highest-leverage
   fix, addressing **30 of 51 cases** (themes T1+T4+T5+T6): filter retrieved
   records to the query's scope, take a stance on judgment questions, and emit the
   requested form instead of a raw dump.
3. **Decompose compound queries and do multi-hop retrieval** — **18 cases**
   (T2+T3): answer every part of the ask, fetch each comparandum, and flag any
   part still missing rather than silently dropping it.
4. **Graceful gap handling** — **8 cases** (T6+T7): unavailable items and empty
   results degrade to an explicit "not in the data," never a raw error or silence.
5. **Agent reliability:** one root cause drove all 33 baseline crashes; fixed,
   keep the regression test.

That is a pass rate turned into a prioritized backlog: a broken criterion at the
top (where a dashboard would never surface it), then three product fixes ranked by
how many real traces each one closes — the flywheel's whole reason to exist.

## Scope & honest limits

- **Two coding layers, clearly split.** Clustering is by objective signature
  (which criteria failed, which exception fired) — reproducible, in code. The
  *open-coding* of the 51-case cluster into seven themes (§2.5) is Carlos's
  qualitative read, the sole-human-analyst pass on top of the mechanical
  skeleton; the counts that rank the backlog come from his labels, not from a
  heuristic pretending to understand *why*.
- **Drift thresholds are explicit** (agreement < 80%, direction skew ≥ 80%) and
  live in `flywheel/drift.py`; they're a defensible default, not a law. Tune
  them to your tolerance — the point is that drift needs *both* frequency and
  direction, not either alone.

## What's built

`flywheel/drift.py` (4 tests) — objective criteria-drift detection.
`flywheel/clustering.py` (4 tests) — axial coding by mechanical signature.
`report_flywheel.py` — the flywheel over Artifacts 02 & 03's real failures.
`build_opencoding_worksheet.py` — assembles the 51-case cluster's full traces
into one file for the human analyst. `opencoding_worksheet_coded.md` — Carlos's
completed open-coding (51 traces → 7 themes; §2.5).
**8 tests, TDD.** Closes the eval thread opened by Artifacts 01 and 02.
