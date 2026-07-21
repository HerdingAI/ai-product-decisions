# RESULTS — is this judge trustworthy enough to gate releases?

**Judge:** `deepseek/deepseek-v4-flash` (OpenRouter, `reasoning_effort=high`), prompt `judge_v1`.
**Reference:** Carlos's hand labels (sole labeler). **Cases:** 85 judged of 100 labeled
(15 collected + labeled *after* this judge run — see §6).
**Run:** binary per-criterion verdicts + four bias probes, 8-way parallel.
**Provenance:** the judge verdicts are the frozen committed run; the gold standard was
refreshed 2026-07-20 and the agreement below **re-scored against the new labels without
re-invoking the judge** (`regenerate_report.py`) — the judge never sees the labels, so its
verdicts are a fixed artifact and holding them constant is the correct, reproducible thing to
do. §7.

The question this artifact answers is **not** "can an LLM grade responses." It is "do I trust
*this* judge enough to let it gate releases," and the honest answer is **on three of four
criteria yes as a screen, and on the fourth — `appropriately-hedged` — no, because the judge
is measurably over-strict against a human standard.** That split is the finding.

## 1. Headline agreement

| Criterion | n | Agreement | Cohen's κ | Human spread | Verdict |
|---|---|---|---|---|---|
| grounded | 85 | **100%** | **1.00** | 81 T / 4 F | **Validated** — §2 |
| complete | 85 | 86% | 0.29 | 21 T / 64 F¹ | Usable as a screen — §4 |
| appropriately-hedged | 85 | 40% | **0.05** | 81 T / 4 F | **Broken — do not gate** — §3 |
| usable | 85 | 93% | 0.38 | 12 T / 73 F¹ | Usable as a screen — §4 |

¹ spreads over the 85 judged rows; over all 100 labeled cases the split is complete 21/79,
usable 12/88.

Read the κ column. The story is no longer "degenerate all-True labels" (the prior pass) —
Carlos added genuine `False` variance, so every criterion now has a real reference
distribution. What the variance reveals is a judge that is **uniformly stricter than the
human**: of 69 judge-vs-human disagreements, **all 69 are judge=`False` / human=`True`.** The
judge never once passed something the human failed. That single directional fact drives every
verdict below.

## 2. grounded — validated (κ=1.00)

Carlos marked exactly four cases `grounded=False`: **C-23, CQ-10, H-03, U-19** — the four
empty / structurally-broken responses (no claims, or claims with no tool support). The judge,
independently, marked those **same four and only those four** `grounded=False`. 81 True + 4
False, agreed on all 85 → **100% agreement, κ=1.00.**

This is the criterion you most want a grader to get right, and on this set it is now
*validated against real negatives* rather than sitting on a constant column (the prior pass
had 0 human negatives and a structurally-meaningless κ=0). The caveat is honest: 4 negatives
is a thin positive-class test, and all four are the "empty response" shape — the judge has
proven it catches *that* negative perfectly, not that it catches subtle mid-answer
fabrication. But within what the set can show, grounded is the one criterion I would trust.

## 3. appropriately-hedged — broken, and the failure is diagnosable (κ=0.05)

40% agreement, κ=0.05 — near chance. **51 of 85 rows disagree, every one judge=`False` /
human=`True`.** The judge marks the answer "not appropriately hedged"; Carlos says it hedges
fine. This is not noise and not a labeling gap — it is a **criterion-definition failure**, and
Artifact 06's open-coding says exactly what kind.

Carlos labeled `hedged=False` on only the same 4 broken cases as grounded. The other 51 the
judge flagged, he ruled `True`. Why the human is right and the judge is wrong here: those 51
cases *do* fail — but they fail on a **different axis**. Open-coding them (Artifact 06,
`opencoding_worksheet_coded.md`) names seven failure themes, and none of them is "overclaimed
with false confidence" (the actual definition of a hedging failure):

- **T1 raw dump, synthesis never performed** · **T2 second half of a compound query silently
  dropped** · **T3 missing comparandum, comparison impossible** · **T4 wrong-scope retrieval
  presented as the answer** · **T5 judgment question answered with facts only** · **T6
  unavailable item, error surfaced raw** · **T7** (residual).

Every one of those is a **completeness / synthesis / scope** defect — which Carlos *does*
penalize, under `complete` (64 F) and `usable` (73 F). The judge, seeing the same broken
answers, fired the **hedging** criterion on them instead. It has conflated *"this answer is
incomplete / off-scope"* with *"this answer is unhedged."* The two co-occur (an answer that
dumps the wrong jurisdiction is both incomplete and, arguably, silently overconfident), so the
judge's mistake is understandable — but it means the hedging verdict carries no independent
signal: it is mostly a noisy echo of completeness.

**The fix is a human decision Carlos has now effectively made:** his labels are the ruling
that the strict "flag every unacknowledged gap" reading is *not* his bar — those gaps belong
to completeness. So the correction is **not** "iterate the judge until it agrees" (that would
just re-derive completeness under a second name). It is to **amend the hedging criterion** —
bump `RUBRIC.md` to `v1.1` with a changelog line narrowing `appropriately-hedged` to genuine
*overconfidence* (unqualified claims the tool data contradicts or only weakly supports),
explicitly excluding "answer is incomplete" (that's `complete`) — then re-run the judge under
`judge_v1.1`. Until then, **do not gate on this criterion**, and read its current `False`
verdicts as "the answer is probably incomplete," cross-checked against `complete`.

## 4. complete & usable — usable as screens (κ 0.29 / 0.38)

These are the two criteria with the most human variance (21T/64F and 12T/73F over the judged
set), and they land at moderate-but-real κ. All disagreements are again one-directional —
12 on `complete`, 6 on `usable`, every one judge=`False` / human=`True`. The judge's extra
strictness clusters on **format-specific asks**: the query wanted "one sentence," "a
three-bullet checklist," "a 15-word Slack update," "the one thing to know," and the answer
delivered the right facts in the wrong shape. The judge fails it; Carlos, seeing the facts
present, sometimes passes it.

That's mild criterion bleed (format → completeness), but the direction is defensible: on a
"give me one sentence" ask, an answer that ignores the format arguably *is* incomplete for the
user's purpose. This is why `complete`/`usable` screen usefully — on the axis with genuine
label variance the judge tracks the human closely enough to **triage**, over-flagging rather
than under-flagging.

## 5. The one useful property: the judge is a conservative over-flagger

69/69 disagreements in one direction is not a coincidence, it's a characterization: **this
judge has high recall for problems and lower precision** — it will rarely wave through a bad
answer, but it will fail some acceptable ones. For a *release screen* (surface candidates for
human review, fail-safe toward caution) that is the error direction you want. For an
*autonomous gate* it is not, without a precision fix. That is the difference between "screen"
and "gate" in the verdicts above, and it falls straight out of the directional data.

## 6. Stability, edge cases, and coverage honesty

- **Consistency probe flagged 27 of 79 (34%).** Re-asking the same case at temperature 0
  flips ≥1 criterion a third of the time. Any gating use needs majority-vote over ≥3 samples,
  not a single call. (Order probe 13/47 ≈ 28%; verbosity 10/79; sycophancy 6/79.)
- **Empty-response edge case — now resolved.** The prior pass flagged empty answers (H-03,
  CQ-10, and the broken C-23/U-19) as an undefined rubric case. Carlos's labels rule them
  `grounded=False` + `hedged=False`, and the judge agrees — the case is now specified by
  example and both raters concur.
- **85 judged, 100 labeled.** 13 cases (C-06–C-18) were collected and hand-labeled *after*
  this judge run; 2 more (H-08, H-21) never produced a parseable verdict (provider/parse
  failures the fault-tolerant pipeline recorded rather than aborting the ~$0.04 run). Agreement
  is therefore over the 85 with verdicts. Closing the gap is one command —
  `python run.py --judge-model deepseek/deepseek-v4-flash --reasoning-effort high --workers 8`
  with `OPENROUTER_API_KEY` set — and the labels for all 100 are already in place waiting for it.

## 7. Cost and latency

| Metric | Value |
|---|---|
| Judged cases | 85 (+ bias probes) |
| Total run cost | **$0.039** (≈ $0.0005 / case, all-in) |
| p50 latency | 16.6 s / call |
| p95 latency | 43.4 s / call |

Cheap enough to run every release; the latency is a reasoning-model artifact, hence the 8-way
parallelism. A human labeling 85 open-ended cases at ~2 min each is ~3 hours; the judge is
~$0.04 and minutes wall-clock. Worth taking on the three criteria the set validates.

## 8. When I would and wouldn't trust this judge

- **Trust as a screen:** `grounded` (κ=1.00, validated on real negatives), `complete`
  (κ=0.29), `usable` (κ=0.38) — averaged over ≥3 samples to absorb the 34% consistency noise,
  used to triage answers for human review, not as a sole autonomous gate.
- **Do not trust / do not gate:** `appropriately-hedged` (κ=0.05). The judge is over-strict by
  a measured human standard and the criterion is conflated with completeness (§3). Fix by
  amending the rubric to `v1.1` (narrow it to genuine overconfidence) and re-running, then
  re-measure.

**Net:** evaluating the evaluator turned a plausible-looking four-criterion judge into a
precise map — one criterion validated, two usable as cautious screens, one broken and *why* it
is broken (traced to the open-coding themes in Artifact 06). A judge you've measured, with its
one broken criterion named and its fix specified, beats a judge you trusted because it sounded
reasonable.

## 9. Method disclosure

Carlos is the sole human labeler — disclosed, not hidden; a single-labeler reference has no
inter-rater ceiling, itself a limitation. The judge prompt is versioned in
`judge_prompts/judge_v1.md`. Agreement is **re-scored from the frozen judge verdicts against
the current labels** by `regenerate_report.py` — re-running the LLM was deliberately avoided so
the judge side stays constant while the labels evolve; a full fresh pass over all 100 (`run.py`)
is a one-command refresh when a key is available. Raw verdicts, per-case reasons, probe
outcomes, and cost are in `results/results.json`; the agreement/disagreement tables in
`results/SUMMARY.md`.
