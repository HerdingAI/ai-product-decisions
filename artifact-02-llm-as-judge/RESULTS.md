# RESULTS — is this judge trustworthy enough to gate releases?

**Judge:** `deepseek/deepseek-v4-flash` (OpenRouter, `reasoning_effort=high`), prompt `judge_v1`.
**Reference:** Carlos's hand labels. **Cases:** 85 judged of 87 collected (2 skipped — see §5).
**Run:** binary per-criterion verdicts + four bias probes, 8-way parallel.

The question this artifact answers is **not** "can an LLM grade responses." It is "do I
trust *this* judge enough to let it gate releases," and the honest answer here is
**partially, and only after fixing the calibration set** — for reasons that are more about
the labels than the judge.

## 1. Headline agreement

| Criterion | n | Agreement | Cohen's κ | Human label spread | Verdict |
|---|---|---|---|---|---|
| grounded | 85 | 95% | **0.00** | 87 True / 0 False | **Unvalidated** — see §2 |
| complete | 85 | 86% | 0.29 | 15 True / 72 False | Usable as a screen |
| appropriately-hedged | 85 | 35% | **0.00** | 87 True / 0 False | **Broken / undefined** — §2, §3 |
| usable | 85 | 93% | 0.38 | 8 True / 79 False | Usable as a screen |

Read the κ column, not the agreement column. Two of the four numbers that look strong
(grounded 95%, hedged 35%) sit on top of a **degenerate reference distribution** and cannot
be trusted as validation. That is the single most important finding, and it is a finding
about *my calibration set*, not the model.

## 2. Failure pattern #1 — degenerate reference labels make grounded & hedged unmeasurable

Carlos labeled **every one of the 87 cases `True`** on both `grounded` and
`appropriately-hedged`. When one rater's column is constant, Cohen's κ is structurally 0
regardless of how the other rater behaves — there is no variance for chance-correction to
work against. So:

- **`grounded` 95% / κ=0.00** does not mean "the judge is 95% right." It means the judge
  echoed the human's blanket "grounded" on 81 of 85 cases. It has **never been tested on a
  genuinely ungrounded answer**, because the set contains none that the human marked as such.
- **`appropriately-hedged` 35% / κ=0.00** is the same degeneracy seen from the other side:
  the judge disagreed with the blanket "True" on ~55% of cases (§3), and κ still reports 0
  because the human column is constant.

**Why it matters:** grounding is *the* criterion you'd most want a judge to catch, and this
set cannot show whether it can. **How to fix:** the calibration set needs genuine negatives —
cases a human labels `grounded=False` / `hedged=False` — before either criterion can be
validated. Adding the 13 uncollected cases (C-06–C-18) will not fix this; the fix is
label *variance*, not label *count*.

## 3. Failure pattern #2 — the judge and the human use different definitions of "hedged"

Setting κ aside and reading the verdicts directly, the judge is **internally consistent and
far stricter** than the human on hedging. It marks `appropriately-hedged=False` whenever the
tool evidence is partial and the answer doesn't say so — a coherent rule applied across ~45
cases:

- **Missing jurisdiction unacknowledged:** CQ-01/05/06/18/25, H-11/14, U-14/19 — answer covers
  Colorado, the query asked about NY/IL/EU/UK, and the response never flags the gap.
- **Truncated tool output presented as whole:** C-02, CQ-09/16, U-06 — the answer reproduces a
  summary that ends mid-sentence (`"…(a) the "`, `"…in particular where suc"`) without noting
  it is cut off.
- **Wrong-domain data presented as answer:** C-04, CQ-08, H-24, U-04/12 — an *insurance*
  bulletin returned for a *credit-scoring* question, presented without the mismatch called out.

Every one of these is a defensible "not appropriately hedged" call. The human labeled them
all `True`. This is not noise — it is a **rubric-definition disagreement**: the judge treats
"appropriately hedged" as "explicitly flags every evidentiary gap," the human treats it as
"doesn't wildly overclaim." Until `judge_v1`'s hedging criterion and the labeling guide are
reconciled to one definition, this criterion should not gate anything.

## 4. Failure pattern #3 — "complete" bleeds into synthesis/format (and here it's mostly right)

On `complete`, where the human labels *do* have variance (15T/72F, κ=0.29), the judge's
disagreements cluster on one behavior: it marks a raw data-dump `complete=False` when the
query asked for a **specific synthesized form** the answer didn't produce —
"one sentence" (U-06), "three-bullet checklist" (U-07), "15-word Slack update" (U-22),
"the one thing to know" (U-03), "two articles in priority order" (U-23). The human often
still called these `complete` because the underlying facts were present.

This is criterion bleed — the judge folds a *usability/format* concern into *completeness* —
but note the direction: on these format-specific asks the judge is arguably **more right than
the lenient human label**. It's the reason `complete` and `usable` land at moderate-but-real
κ (0.29 / 0.38) instead of near-zero: on the axis with genuine label variance, the judge
tracks human judgment well enough to screen with.

## 5. Failure pattern #4 — run-to-run instability and the empty-response edge case

- **Consistency probe flagged 27 of 79 cases (34%).** Re-asking the judge the *same* case at
  temperature 0 flips at least one criterion a third of the time. Even where agreement looks
  fine, a single verdict is noisy; a gating use would need majority-vote over several samples,
  not one call. (Order probe: 13/47 ≈ 28% — same instability seen when option order is
  swapped. Verbosity 10/79, sycophancy 6/79 — milder.)
- **Empty responses expose a vacuous-truth gap:** H-03, CQ-10, H-12 returned empty text. The
  judge calls an empty answer `grounded=False` ("no claims, nothing to ground"); the human
  called it `True`. Neither is obviously wrong — it's an undefined case the rubric never
  specified. It should be specified.
- **2 cases (H-08, H-21) never produced a parseable verdict** — provider/parse failures. The
  fault-tolerant pipeline recorded them and finished the other 85 rather than aborting the
  ~$0.04 run. Working as designed, but it means agreement is over 85, not 87.

## 6. Cost and latency

| Metric | Value |
|---|---|
| Judged cases | 85 (+ 4 bias probes each where applicable) |
| Total run cost | **$0.039** (≈ $0.0005 / case, all-in incl. probes) |
| p50 latency | 16.6 s / call |
| p95 latency | 43.4 s / call |

Cheap enough to run on every release; the latency is a reasoning-model artifact and is why
the run is parallelized 8-way. A human labeling 85 open-ended cases at ~2 min each is ~3
hours; the judge is ~$0.04 and a few minutes wall-clock. The trade-off is real — but only
worth taking on the criteria the set can actually validate.

## 7. When I would and wouldn't trust this judge

**Would trust — as a screen, not a gate:** `complete` and `usable`. Real label variance,
moderate κ (0.29 / 0.38), and the disagreements are explainable (format strictness) rather
than random. I'd use them to *rank/triage* open-ended answers for human review, averaged over
≥3 samples to absorb the 34% consistency noise — not as a sole ship/no-ship gate.

**Would not trust — yet:** `grounded` and `appropriately-hedged`. Both are **unvalidated**:
the human labels have zero variance, so κ is undefined-as-zero and the judge has never been
tested against a real negative on the one axis (grounding) you most want it to catch. The
hedging criterion additionally shows the judge and human are running *different definitions*.
Before either gates a release I need (a) a calibration set with genuine `False` cases on both
criteria, (b) a reconciled hedging definition shared by prompt and labeler, and (c) a rubric
ruling on the empty-response case.

**Net:** the machinery is sound and cheap; the *evaluation of the evaluator* surfaced that
half my rubric can't be scored against the labels I have. That is the artifact working as
intended — a judge you've measured, with its blind spots published, beats a judge you trusted
because it sounded reasonable.

## 8. Method disclosure

Carlos is the sole human labeler — disclosed, not hidden; a single-labeler reference has no
inter-rater ceiling to measure against, which is itself a limitation of this pass. The judge
prompt is versioned in `judge_prompts/judge_v1.md`; regenerate these results whenever it
changes. Raw verdicts, per-case reasons, probe outcomes, and cost are in
`results/results.json`; the agreement/disagreement tables are in `results/SUMMARY.md`.
