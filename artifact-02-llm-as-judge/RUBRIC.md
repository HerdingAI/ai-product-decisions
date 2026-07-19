# RUBRIC — the judge's rubric, stated before any labeling

This is the spec `eval_judge/judge.py` implements, written here in prose
before any calibration response is read — same discipline as Artifact 01's
`criteria.md`, for the same reason: a rubric written after looking at the
outputs quietly bends to match them. See [SAMPLING.md](SAMPLING.md) for how
the calibration set was built and how held-out scoring works.

Artifact 01 already answers "did the agent call the right tool and say
something non-empty" with deterministic pattern-matching — that's a routing
question with a mechanically checkable answer. This artifact exists because
routing-correct is not the same as *answer-good*: a response can call the
right tool and still be an answer a PM wouldn't ship — overconfident on a
partial dataset, unclear, or asserting something the tool result doesn't
actually support. That's a subjective-quality judgment, which is why it
needs a judge instead of a regex.

Each criterion is binary pass/fail against one `(query, tool_calls,
response)` triple — never a 1–5 score. The judge sees the same
tool-call trace a human labeler sees; neither is asked to re-derive the
underlying regulation/benchmark data from scratch.

## grounded

**Passes if:** every specific claim in the response (a number, a
jurisdiction, a status, a citation) traces to something present in the
tool-call output for that turn.

**Fails if:** the response asserts a fact that doesn't appear in any tool
result from that turn — including plausible-sounding filler ("this is a
common requirement across jurisdictions") that reads as fact but isn't
backed by a call.

**Why binary, not partial credit:** a response is either traceable to its
own tool output or it isn't. "Mostly grounded" is exactly the failure mode
this criterion exists to catch — it doesn't get partial credit for being
plausible.

## complete

**Passes if:** the response addresses every part of what was actually asked
— including compound questions, where each sub-question gets a real answer
or an explicit "the tool data doesn't cover X."

**Fails if:** the response answers part of a compound question and is
silent on the rest, without flagging the gap.

**Why it's separate from grounded:** a response can be perfectly grounded
in the tool output and still silently drop half a two-part question — a
different failure surface than fabrication.

## appropriately-hedged

**Passes if:** where the tool output is partial, ambiguous, or silent on a
sub-claim, the response says so, rather than presenting a confident,
unqualified answer.

**Fails if:** the response states something with unqualified confidence
that the tool data only partially supports (e.g. citing one jurisdiction's
number as if it were a general rule).

**Why this is the hardest criterion for the judge to get right:** a
verbose, hedge-everywhere response can game this criterion by looking
careful without actually distinguishing supported claims from unsupported
ones — see the verbosity bias probe (`bias_probes.py`), which is designed
specifically to catch a judge that rewards hedging-as-volume over
hedging-as-precision.

## usable

**Passes if:** a PM could act on the response without a follow-up question
— it's specific (names the jurisdiction/article/model it's about), not
generic boilerplate, and doesn't require the reader to already know the
answer to parse it.

**Fails if:** the response is vague enough that a PM would need to re-ask
the question, or is generic enough it could have been the answer to a
different query.

**Why it's the PM-facing criterion:** the other three check correctness;
this one checks that a correct-but-useless answer still fails — a shipped
system's answers have to be usable, not just true.

---

## What the judge does not check

The judge is not re-run on the deterministic routing criteria from
Artifact 01 (`tool_correct`, `no_wrong_tool`, `idk_when_no_tool`,
`no_fabrication`) — those already have a mechanical answer and re-scoring
them with an LLM would only add judge noise to a question that doesn't need
one. The judge is scoped to the four criteria above, on the subset of
calibration-set cases where a tool actually returned data to reason about.
