# RESULTS — workflow vs. agent

**Question:** for a bounded regulatory-lookup task, when is a deterministic
*workflow* (fixed rule → tool) the right call, and when do you need an *agent*
(LLM picks tools, loops, recovers)? This measures both arms on the **same 100
calibration queries** Artifact 02 collected (same domain, same tools), so the
comparison shares a query distribution.

Two numbers are reproducible with no key and no labels (coverage, workflow
latency/cost). The agent-arm numbers come from a live run of `agentic-copilot`
on `deepseek/deepseek-v4-flash` over OpenRouter. Latency and tool-call counts
are measured exactly; **cost is an estimate** (the chat API returns no token
usage — see "Cost" below).

## Head-to-head

| Metric | Workflow arm | Agent arm (deepseek-v4-flash) |
|---|---|---|
| Coverage (served / 100) | **64** | **81** |
| Fallback recovery¹ | — | **30 / 36 (83%)** |
| Mean tool calls / query | 1.0 | **3.82** |
| Tool-call tail (max on one query) | 1 | **20** |
| p50 latency | <1 ms | **17.6 s** |
| p95 latency | <1 ms | **44.9 s** |
| Cost / query | $0 | ~$0.00055 (est.) |
| Hard failures (crash) | **0** (fails closed) | 0 post-fix — **33/100 pre-fix** (see below) |

¹ Of the 36 queries the workflow fails closed on, how many the agent serves.

Per-group coverage (25 queries each):

| Query group | Workflow | Agent |
|---|---|---|
| grounding | 19 | 19 |
| compound | 19 | 23 |
| hedge | 14 | 15 |
| usability | 12 | **24** |
| **All** | **64** | **81** |

Reproduce: workflow `python report_coverage.py`; agent `python run_agent_arm.py
--base-url http://127.0.0.1:8020` (needs a running real-LLM `agentic-copilot`).

## Reading it

**The agent buys coverage — almost entirely in one place.** It lifts 64 → 81,
and 12 of those 17 extra served queries are `usability` ("draft one sentence for
the board deck," "give me a 15-word Slack update"). Those map to **no lookup
tool**, so the workflow can only refuse them (12/25); the agent composes an
answer from tool output it *does* have, so it serves 24/25. The `grounding`
group, which is purely tool-shaped, is a **tie at 19/25** — the LLM's routing
adds nothing a fixed rule didn't already get. So the agent's value here is not
"better routing," it's "handles the open-ended asks a rule set structurally
can't express."

**That coverage is not free — and the tail is the story.** Mean latency is p50
17.6 s / p95 44.9 s versus the workflow's sub-millisecond deterministic route.
Mean tool calls is 3.82, but the *distribution* is what matters: a heavy tail
runs to **18 and 20 tool calls on single queries** — the agent looping,
re-querying, and re-deciding. That is the compounding-cost failure mode a
deterministic workflow cannot have by construction: the workflow makes exactly
one tool call or none. Every 20-tool-call query is latency and dollars spent
with no guarantee of a better answer.

## The reliability finding: 33% hard-crash before a one-line adapter fix

The first full agent run **500-errored on 33 of 100 queries.** Root cause: under
a real LLM (deepseek), the model emits a spurious `input` argument even for
zero-parameter tools like `list_all_articles`; `agentic-copilot`'s MCP adapter
forwarded every kwarg into the function, so `list_all_articles(input=...)`
raised `TypeError: unexpected keyword argument 'input'`, which the API turned
into a 500. Raw baseline: **57/100 served, 33 crashes** (`results/agent_arm_baseline_prefix.json`).

This is the agent-arm risk in miniature: a fixed workflow's tool calls are
written by a human and can't be malformed; an agent's are generated per-request,
so a single adapter/model incompatibility takes down a third of traffic with no
fail-closed. The fix (`agentic-copilot/agent/mcp_adapter.py`,
`_filter_kwargs_for_fn`, TDD'd) passes only kwargs the target function declares,
unless it accepts `**kwargs`. Re-running the 33 failed cases against the fixed
server: **0 crashes, 81/100 served.** The post-fix numbers are the fair ones for
the comparison above; the baseline is kept as the reliability finding.

## Cost

Estimated, not billed: `/api/chat` returns no token usage, so per-query cost is
approximated as (system prompt + query + tool results) input tokens and (answer
+ tool args) output tokens at chars/4, priced at assumed
`$0.10 / $0.30` per-1M in/out. Total over 100 queries ≈ **$0.055** (~$0.00055
each). Treat as an order-of-magnitude figure; the workflow's $0 is exact. Even
if the real price were 3× the estimate, the decision below does not change — the
latency gap (4–5 orders of magnitude) dominates.

## Decision memo — which arm per task shape

The comparison does not crown a winner; it says **route by task shape**:

- **Tool-shaped lookups** (`grounding`, most `compound`): **workflow.** Coverage
  ties (19/25 vs 19/25 on grounding), and the workflow returns in <1 ms for $0
  with zero crash surface. Paying 17 s and an LLM call to match a rule you
  already have is strictly worse. Route these deterministically; fail closed.
- **Open-ended / synthesis asks** (`usability`, drafting): **agent.** The
  workflow serves 12/25 because these map to no tool; the agent serves 24/25 by
  composing. This is the only group where the agent earns its cost — there is no
  fixed rule that writes a board-deck sentence.
- **Hybrid, latency-sensitive path:** workflow-first with agent fallback. Try
  the rule set (free, instant); on fail-closed, hand the 36 uncovered queries to
  the agent. That recovers 30 of them (83%) while paying agent latency/cost on
  only ~⅓ of traffic instead of all of it — and caps the compounding tail to the
  queries that actually need it.

**Guardrail the tail regardless.** Whichever arm serves, cap agent tool-call
depth (the 18–20-call runs are almost all wasted) and keep the workflow's
fail-closed behavior as the default so a malformed generation degrades to "I
don't know," not a 500.

## The quality half — and it flips the easy reading of the coverage numbers

Coverage counts *whether* an arm answered, not whether the answer is *good*. So
on the **62 queries both arms serve**, Carlos judged the two answers blind (left/
right order randomized per pair, same discipline as Artifact 02's order probe;
`assemble_quality_pairs.py` captured full response text from the workflow run
offline against the real `reg_atlas`/`regfin_bench` tools and the agent live
against `agentic-copilot`). Unblinding his verdicts (`analyze_quality_pairs.py`):

| Quality winner (shared-served, n=62) | Count |
|---|---|
| **Workflow better** | **28** |
| Tie | 21 |
| **Agent better** | **13** |

Per group:

| Group | Workflow | Agent | Tie |
|---|---|---|---|
| grounding | **15** | 2 | 2 |
| compound | 7 | 4 | 8 |
| hedge | 2 | 3 | 7 |
| usability | 4 | 4 | 4 |

**This inverts the naïve coverage takeaway.** Coverage alone (81 vs 64) reads
"the agent is better." But where both arms actually answer, the **workflow wins
more than 2:1 (28 vs 13)** — and on `grounding`, the purely tool-shaped group, it
is a rout (**15 vs 2**). The two findings are consistent, not contradictory: the
agent answers *more* questions, but its answers on the overlap are *worse*.

**Why the workflow wins the overlap** (from Carlos's reasons): on a tool-shaped
lookup the workflow returns the **single on-target record, or a clean gap-flag**
("Article 43 unavailable; available: 9, 10, 12, 14, 15"). The agent, on the same
query, **buries the right record under an 8-record dump** or leads with irrelevant
Colorado rows — the exact "raw dump, no synthesis" / "wrong-scope retrieval" /
"unavailable-item buried" behaviors Carlos independently open-coded as themes
**T1 / T4 / T6** in Artifact 06. The agent's extra tool calls (mean 3.82, tail to
20) don't just cost latency and dollars — on the overlap they frequently *degrade*
the answer by adding noise around it.

**Why the agent wins the 13 it wins:** almost never on grounding. It wins when the
workflow's fixed route **missed a comparandum** (returned one jurisdiction of a
requested two) or answered the **wrong sector**, and when a `usability` ask wanted
prose the agent's synthesis produced drop-in memo text where the workflow emitted
raw JSON. Those are the open-ended shapes a rule set structurally can't express —
the same place the coverage numbers already said the agent earns its cost.

**What this does to the decision.** It *strengthens* the workflow-first-with-agent-
fallback rule. The workflow isn't merely cheaper and faster on tool-shaped
lookups — on the answers both arms produce, **its answers are also better**. So
route deterministically wherever the workflow serves (better *and* free *and*
instant), and reach for the agent only on the open-ended tail it structurally
owns — where, notably, the shared-served quality is a wash (usability 4/4/4), so
the agent's real value there is coverage, not superior quality. Raw per-arm output
for all 100 cases (including the 38 not shared-served) is in
`results/quality_pairs_raw_arms.json`.

**Side finding while building this:** the router sent `query_by_article` the
wrong keyword argument (`article_category` vs. the real tool's
`article_category_id`) — would have raised `TypeError` had that branch ever
executed against a real registry. Caught via TDD
(`test_task_category_lookup_uses_real_tool_arg_name`) while wiring the real
tools for the workflow arm above; fixed. It never affected the shipped
coverage numbers (`query_by_article` never fires on this 100-query set — see
the routing distribution: `query_by_jurisdiction` 26, `get_eu_ai_act_article`
19, `query_by_framework` 10, `query_by_sector` 4, `query_by_model` 3,
`compare_models` 1, `list_all_models` 1, uncovered 36), but it's a latent bug
now closed.

## What's built

`workflow/` (16 tests, +1 for the arg-name fix = 17) — `router.py`,
`executor.py`, `harness.py` (deterministic arm). `agent_arm/analysis.py` (7
tests) — served/refused, cost estimate, latency percentiles,
fallback-recovery. `run_agent_arm.py` / `retry_failed.py` — live HTTP drivers.
`assemble_quality_pairs.py` — Task-2 prep: shared-served-set answer pairs for
quality judging. Agent-arm robustness fix + test live in the `agentic-copilot`
spoke (`_filter_kwargs_for_fn`). 24 tests green in this artifact.
