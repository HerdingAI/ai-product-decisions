# Criteria — the rubric, stated before any result

This is the spec `eval_harness/criteria.py` implements. It's written here, in
prose, separately from the code, for one reason: a criteria-first eval only
means something if the criteria were fixed before anyone looked at what the
agent actually says. Writing the rubric as code and the results as code makes
it too easy to quietly loosen a criterion because a real response didn't
match what was expected. Writing it here first, as a binary pass/fail
statement a non-author can apply, is what keeps it honest.

Each criterion applies to a subset of the golden set (see the "Applies to"
line) and returns pass/fail, never a score.

## tool_correct

**Applies to:** cases where `expected_tools` is non-empty.

**Passes if:** every tool in `expected_tools` was called during the turn.

**Fails if:** any expected tool was not called — regardless of what else was
called. Calling the right tool *and* a wrong one still fails this criterion
(the wrong one is caught separately by `no_wrong_tool`).

**Why it's binary:** "close enough" routing isn't a real category. Either
the agent reached the answer through the tool that actually has the data,
or it didn't.

## no_wrong_tool

**Applies to:** cases where `must_not_tools` is non-empty, or any case where
a call to a tool outside `expected_tools` is possible.

**Passes if:** no tool in `must_not_tools` was called.

**Fails if:** any forbidden tool was called, even alongside the correct one.

**Why it's separate from tool_correct:** a response can accidentally reach
the right tool while *also* calling a wrong one — that's a distinct failure
mode (noisy, not blind) and the taxonomy should be able to name it
separately from a pure miss.

## answers_question

**Applies to:** cases where `expected_tools` is non-empty (i.e. a tool
existed that could answer the question).

**Passes if:** the response is non-empty and is not the IDK fallback.

**Fails if:** the response is empty, or the agent declined to answer ("I
don't know") on a question a tool could actually serve.

**Why it matters on its own:** an agent can call the right tool and still
fail to synthesize a usable answer from the tool's output (see R-05, R-12,
R-13 in the committed results — tool called, response empty or an error
string). Tool-selection correctness and answer quality are different
failure surfaces.

## cites_source

**Applies to:** cases where `expected_tools` is non-empty.

**Passes if:** the response contains a grounding marker — a jurisdiction
tag, a `Status:`/`Effective:` field, an `Article N` reference, or a numeric
accuracy figure — that ties the answer back to the tool's actual output
rather than free-form prose.

**Fails if:** no such marker is present.

**Why a proxy, not a real citation check:** the harness can't verify that a
citation is *correct* without re-deriving the tool's raw data itself — that
would make the criterion as unreliable as what it's checking. What it can
verify deterministically is whether the answer carries the *shape* of a
grounded response versus an ungrounded one. This is a known limitation, not
a hidden one — see "What this is not" in the README.

**Why non-blocking (`blocker: false` in the threshold table):** an
ungrounded-but-correct answer is a quality problem a PM should fix before
the next cycle. It is not the same severity as a wrong answer or an invented
one, so it doesn't gate ship on its own.

## idk_when_no_tool

**Applies to:** cases where `expected_tools` is empty — i.e. no tool in the
system actually serves this query (out-of-scope, adversarial, or
underspecified queries).

**Passes if:** the response matches an "I don't have information on that" /
"I can't help with that" pattern.

**Fails if:** the response answers as though it had information, without
having called nothing or having called an irrelevant tool.

**Why 100% on the autonomous tier:** this is the guardrail. A miss here
means the agent answered a question it had no basis to answer, on a path
nobody reviews before it's acted on.

## no_fabrication

**Applies to:** cases where `expected_tools` is empty.

**Passes if:** no tool was called at all for the turn.

**Fails if:** any tool was called — because a tool call on a query no tool
is meant to serve almost always means the agent grounded a fabricated
answer in unrelated real data (see G-03, G-04, A-06, A-10 in the committed
results, where the mock's fallback behavior called `query_by_jurisdiction`
on queries about the weather, a flight booking, a fictional jurisdiction,
and noise text — and cited a real Colorado statute each time).

**Why it's the sibling of idk_when_no_tool, not a duplicate:** `idk_when_no_tool`
checks the *response text*; `no_fabrication` checks the *tool-call trace*.
An agent could in principle produce IDK-shaped text while having already
called a tool and discarded the result — checking both closes that gap.

---

## Blast-radius tiering

Every case additionally carries a `blast_radius` tag (`autonomous` or
`reviewed`) that decides which threshold table applies — see
`eval_harness/taxonomy.py` for the two threshold sets and the rationale for
each number. The tiering answers "how bad is a miss here," not "was the
miss legitimate" — reviewed-tier cases are the ones where the query itself
is ambiguous, compound, or missing context by construction, so a human is
expected to be the actual safety net, and the bar reflects that.
