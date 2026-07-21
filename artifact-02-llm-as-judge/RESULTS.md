# RESULTS — is this judge trustworthy enough to gate releases?

**Judge:** `deepseek/deepseek-v4-flash` (OpenRouter, `reasoning_effort=high`), prompt `judge_v1`.
**Reference:** Carlos's hand labels (sole labeler). **Cases:** 95 judged of 100 labeled
(5 unjudged — H-03, H-08, H-12, U-18, U-21 — are empty/parse-failure responses the
fault-tolerant pipeline recorded rather than aborting the run). **Run:** full live pass over
all 100, binary per-criterion verdicts + four bias probes, 8-way parallel, $0.044.

The question this artifact answers is **not** "can an LLM grade responses." It is "do I trust
*this* judge enough to let it gate releases," and the honest answer is **as a cautious review
screen on three of four criteria yes; as an autonomous gate no; and on the fourth criterion —
`appropriately-hedged` — not at all, because it is measurably broken against a human standard.**
That split is the finding.

## 1. Headline agreement

| Criterion | n | Agreement | Cohen's κ | Disagreements | Verdict |
|---|---|---|---|---|---|
| grounded | 95 | 95% | 0.26 | 5 | Screen, run-sensitive — §2 |
| complete | 95 | 86% | **0.49** | 13 | Usable as a screen — §4 |
| appropriately-hedged | 95 | 39% | **0.04** | 58 | **Broken — do not gate** — §3 |
| usable | 95 | 93% | **0.56** | 7 | Usable as a screen — §4 |

Read the κ column, not the agreement column — high agreement with low κ is the kappa paradox
(a criterion where almost everything is one class scores high agreement by luck). `complete`
(0.49) and `usable` (0.56) are the two criteria with real label variance and they land at
moderate, honest κ. `grounded` shows 95% agreement but κ=0.26 — §2. `appropriately-hedged` is
near-chance (0.04).

**One near-uniform direction.** Of 83 total disagreements, **81 are judge=`False` /
human=`True`** — the judge fails things the human passes far more than the reverse. The **2
exceptions** are both `grounded` on empty responses (§2). So the judge is characterically a
**conservative over-flagger**: high recall for problems, lower precision. For a review *screen*
(surface candidates for a human, err toward caution) that is the right error direction; for an
autonomous *gate* it is not, without a precision fix.

## 2. grounded — a screen, but run-sensitive, and the empty-response convention is undefined

95% raw agreement, κ=0.26. The 5 disagreements are almost entirely one underspecified case:
**what does `grounded` mean for an empty / no-claims response?** Carlos rules an empty answer
`grounded=False` (it failed to answer). The judge is *inconsistent with itself* on the same
run: it marked **CQ-10** (empty) "no specific claims, so nothing to be ungrounded" →
`grounded=True`, but **H-21** (also empty) "no claims, therefore cannot be grounded" →
`grounded=False`. Same situation, opposite verdict — a live instance of the 34% consistency
problem (§6). The remaining grounded splits (C-12 sector-mislabel, C-25 ignored-benchmark) are
the judge being *stricter*, and arguably correct.

This is the honest correction to an earlier frozen-verdict pass that showed grounded κ=1.00:
that number rode on one particular run's verdicts happening to match Carlos's four negatives.
A *fresh* run splits on the empty-response convention, and κ falls to 0.26. The finding is not
"the judge got worse" — it's that **grounded agreement is run-sensitive precisely where the
rubric is silent (empty responses)**, and the fix is a rubric line defining that case, after
which grounded should be re-measured over ≥3 samples. Until then, trust grounded as a screen
for the *substantive* negatives (fabrication, sector-mislabel), not as a settled verdict on
empty answers.

## 3. appropriately-hedged — broken, and the failure is diagnosable (κ=0.04)

39% agreement, κ=0.04 — near chance. **58 of the 83 disagreements are here, every one
judge=`False` / human=`True`.** The judge marks the answer "not appropriately hedged"; Carlos
says it hedges fine. This is not noise and not a labeling gap — it is a **criterion-definition
failure**, and Artifact 06's open-coding says exactly what kind.

Carlos labeled `hedged=False` on only the 4 genuinely-broken cases. The dozens the judge flagged,
he ruled `True`. Why the human is right and the judge is wrong: those cases *do* fail — but on a
**different axis**. Open-coding the dominant failure cluster (Artifact 06,
`opencoding_worksheet_coded.md`) names seven themes, and none of them is "overclaimed with false
confidence" (the actual definition of a hedging failure):

- **T1 raw dump, synthesis never performed** · **T2 second half of a compound query silently
  dropped** · **T3 missing comparandum, comparison impossible** · **T4 wrong-scope retrieval
  presented as the answer** · **T5 judgment question answered with facts only** · **T6
  unavailable item, error surfaced raw** · **T7 empty response**.

Every one is a **completeness / synthesis / scope** defect — which Carlos *does* penalize, under
`complete` and `usable`. The judge, seeing the same broken answers, fired the **hedging**
criterion on them instead. It has conflated *"this answer is incomplete / off-scope"* with
*"this answer is unhedged."* So the hedging verdict carries no independent signal — it is a noisy
echo of completeness.

**The fix is a human decision Carlos has now made:** his labels are the ruling that the strict
"flag every unacknowledged gap" reading is *not* his bar. So the correction is **not** "iterate
the judge until it agrees" (that just re-derives completeness under a second name). It is to
**amend the criterion** — bump `RUBRIC.md` to `v1.1`, narrow `appropriately-hedged` to genuine
*overconfidence* (unqualified claims the tool data contradicts or only weakly supports),
explicitly excluding "answer is incomplete" — then re-run under `judge_v1.1`. Until then, **do
not gate on this criterion**, and read its current `False` verdicts as "probably incomplete,"
cross-checked against `complete`.

## 4. complete & usable — usable as screens (κ 0.49 / 0.56)

These are the two criteria with the most human variance, and they land at the highest κ of the
four — 0.49 and 0.56, moderate agreement beyond chance. All disagreements are one-directional
(13 on `complete`, 7 on `usable`, judge stricter), clustering on **format-specific asks**: the
query wanted "one sentence," "a 15-word Slack update," "two articles in priority order," and the
answer delivered the right facts in the wrong shape. The judge fails it; Carlos, seeing the facts
present, sometimes passes it. That is mild criterion bleed (format → completeness), but the
direction is defensible — on a "give me one sentence" ask, an answer that ignores the format
arguably *is* incomplete for the user's purpose. On the axes with genuine variance, the judge
tracks the human closely enough to **triage**.

## 5. The one useful property: a conservative over-flagger

81 of 83 disagreements in one direction is a characterization: **high recall for problems, lower
precision** — the judge rarely waves through a bad answer, but fails some acceptable ones. Right
error direction for a *screen*, wrong for an autonomous *gate* without a precision fix. The 2
counter-examples are both the empty-response "vacuously grounded" call (§2), i.e. an
underspecified-rubric artifact, not the judge being lax on substance.

## 6. Stability, edge cases, and coverage

- **Consistency probe flagged 21 of 92 (23%).** Re-asking the same case flips ≥1 criterion
  roughly a quarter of the time — and §2's CQ-10-vs-H-21 split is a concrete instance. Any gating
  use needs majority-vote over ≥3 samples, not a single call. (Order probe 21/57; verbosity
  13/92; sycophancy 9/92.)
- **Empty-response convention is the open rubric gap.** Both the 2 reverse disagreements and the
  judge's self-inconsistency trace to it. One rubric line ("an empty or no-claims response is
  `grounded=False` and `usable=False`") closes it; the labels already encode that ruling.
- **95 judged of 100.** The 5 unjudged (H-03, H-08, H-12, U-18, U-21) are empty / parse-failure
  responses; the pipeline recorded them as per-case failures rather than aborting the ~$0.044 run.

## 7. Cost and latency

| Metric | Value |
|---|---|
| Judged cases | 95 (+ bias probes) |
| Total run cost | **$0.044** (≈ $0.0005 / case, all-in) |
| p50 latency | 22.9 s / call |
| p95 latency | 39.8 s / call |

Cheap enough to run every release; the latency is a reasoning-model artifact, hence the 8-way
parallelism. A human labeling 95 open-ended cases at ~2 min each is ~3 hours; the judge is ~$0.04
and minutes wall-clock. Worth taking on the three criteria the set can screen — averaged over ≥3
samples to absorb the consistency noise.

## 8. When I would and wouldn't trust this judge

- **Trust as a screen (≥3-sample majority vote):** `complete` (κ=0.49) and `usable` (κ=0.56) to
  triage answers for human review; `grounded` (κ=0.26) for *substantive* groundedness
  (fabrication, sector-mislabel), once the empty-response rubric gap is closed.
- **Do not gate autonomously on anything** — the 23% single-run flip rate and the over-flagging
  precision gap both argue for human-in-the-loop.
- **Do not trust at all:** `appropriately-hedged` (κ=0.04). Over-strict by a measured human
  standard and conflated with completeness (§3). Fix by amending the rubric to `v1.1` and
  re-running, then re-measure.

**Net:** evaluating the evaluator turned a plausible-looking four-criterion judge into a precise
map — two criteria usable as cautious screens, one run-sensitive with a namable rubric gap, one
broken with its cause traced to the open-coding themes in Artifact 06. A judge you've measured,
with its weak spots named and their fixes specified, beats a judge you trusted because it sounded
reasonable.

## 9. Method disclosure

Carlos is the sole human labeler — disclosed, not hidden; a single-labeler reference has no
inter-rater ceiling, itself a limitation. The judge prompt is versioned in
`judge_prompts/judge_v1.md`. This RESULTS reflects a **full live judge pass** over all 100 cases
(`run.py --judge-model deepseek/deepseek-v4-flash --reasoning-effort high --workers 8`); raw
verdicts, per-case reasons, probe outcomes, and cost are in `results/results.json`, the agreement
and disagreement tables in `results/SUMMARY.md`. `regenerate_report.py` re-scores agreement from
frozen verdicts against changed labels *without* re-judging — the tool used before a key was
available, and the way to re-measure after a `RUBRIC.md` edit without paying for a new pass.
