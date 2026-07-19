# SAMPLING — how the calibration set was built

## Current status: 20 cases, not the target N≈100

The playbook's Stage 5 DoD calls for "N≈100 outputs generated + fully
labeled" with agreement reported on a held-out slice. `calibration_set.py`
currently has **20 hand-written cases** — enough to build and unit-test the
full judge/probe/report pipeline against, and enough for a first honest
agreement read once Carlos labels them, but not yet the full N the DoD
calls for. Scaling to ~100 (more cases per group, plus new groups covering
failure modes the first 20 don't stress) is the next increment on this
artifact, done after the first labeling pass shows which groups are
under-covered — writing 80 more cases *before* seeing where the judge
actually struggles would be guessing at coverage instead of targeting it.

## Composition (v1, 20 cases)

| Group | Cases | Targets |
|---|---|---|
| `grounding` (C-01..C-05) | 5 | claims that should/shouldn't trace to a tool result |
| `compound` (CQ-01..CQ-05) | 5 | multi-part questions where partial answers should be caught by `complete` |
| `hedge` (H-01..H-05) | 5 | partial/ambiguous tool data that should trigger hedging, or shouldn't |
| `usability` (U-01..U-05) | 5 | responses that could be correct but too vague/generic to act on |

Each group maps to one of the four rubric criteria in
[RUBRIC.md](RUBRIC.md) (`grounded`, `complete`, `appropriately-hedged`,
`usable`) — not a strict partition (a `hedge` case can also reveal a
`grounded` failure), but each group is *written* to stress its named
criterion specifically, and every case carries a `note` field explaining
the failure mode it targets (see `calibration_set.py`).

All 20 queries target real tools in `agentic-copilot`'s regulation-atlas
and benchmark-comparison surface (`query_by_jurisdiction`,
`query_by_framework`, `compare_models`, `get_eu_ai_act_article`, etc.) —
they are not generic questions; each was written against what that specific
tool can and can't answer, so a grounding or hedging failure is real and
checkable against the tool's actual output, not a matter of interpretation.

## Selection process

Cases were written by hand, not sampled from real user traffic (there is no
real user traffic for a demo agent) — this is a **deliberately constructed
stress set**, not a representative sample of "typical" queries. That's
disclosed here, not hidden: the calibration set is built to find where the
judge (and the agent) break, which is a different design goal than
estimating typical-case accuracy.

## Held-out protocol

Per [RUBRIC.md](RUBRIC.md)'s calibration protocol:

1. All 20 cases are run once against `agentic-copilot`
   (`collect_responses.py` → `labels/calibration_responses.json`).
2. Carlos hand-labels every case against the four rubric criteria, before
   the judge sees any of them. Carlos is the sole labeler; that's disclosed
   here, not hidden.
3. The judge prompt (`judge_prompts/judge_v1.md`) is iterated, if needed,
   against a subset of the labeled cases.
4. A held-out slice — cases never shown to the judge-prompt author during
   iteration — is scored last, so the reported agreement number isn't
   inflated by prompt-tuning-to-the-test. With only 20 cases, this slice is
   necessarily small (a handful of cases); this gets more statistically
   meaningful once the set grows toward N≈100.

## What this sampling doesn't cover yet

- No cases stress the `order` bias probe's actual target (a case with 3+
  tool calls where reordering plausibly changes a human's read) — the
  current cases mostly have 1-2 tool calls.
- No adversarial/injection-flavored cases (that's Artifact #4's
  guardrails slice, spec §7, not this artifact's scope).
- Group sizes are uniform (5/5/5/5) by construction, not by evidence that
  each criterion needs equal stress — that's a starting assumption to
  revisit once the first labeling pass shows where the judge actually
  disagrees with Carlos.
