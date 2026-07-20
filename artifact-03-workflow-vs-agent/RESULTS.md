# RESULTS — workflow vs. agent (in progress)

**Status:** the labels-independent half is measured; the quality + agent-arm-cost
half is pending (see "Still open"). Numbers here are reproducible from the code with
no keys and no labels.

## Coverage — the metric a fixed workflow can't hide

Coverage is the fraction of a realistic query distribution the workflow arm serves
without falling back. It depends only on the router (no LLM, no tools, no labels), so
it's the first honest number in the comparison. Measured over the **same 100 queries
Artifact 02 collected** (same agent, same domain):

| Query group | Served | Total | Coverage |
|---|---|---|---|
| compound | 19 | 25 | 76% |
| grounding | 19 | 25 | 76% |
| hedge | 14 | 25 | 56% |
| usability | 12 | 25 | 48% |
| **All** | **64** | **100** | **64%** |

Reproduce: `python report_coverage.py`.

**Reading it.** A deterministic rule set serves ~two-thirds of the distribution and
**fails closed on the other third** — it refuses rather than guess. The weakness is
concentrated exactly where you'd predict: `usability` queries ("draft me one sentence
for the board deck," "give me a 15-word Slack update") map to no lookup tool at all, so
the workflow can only refuse them (48%). `grounding`/`compound` lookups, which *are*
tool-shaped, route cleanly (76%).

That 36% fallback rate is the number the agent's LLM routing is supposed to buy down —
and the whole artifact is whether buying it down is worth the agent's per-query cost,
latency, and misroute risk. This establishes the workflow side of that trade.

## Still open (the other half of the comparison)

- **Agent-arm cost/latency/coverage** — run `agentic-copilot` on a real OpenRouter model
  over the same 100 queries; record $/query, p50/p95 latency, tool-call-count
  distribution, and how much of the 36% fallback it recovers. Spends an API key ($).
- **Quality judging** — for the queries *both* arms serve, judge answer quality with
  Artifact 02's method (needs Carlos's labels on the shared set). Coverage without a
  quality check would reward a workflow that answers confidently and wrongly.
- **Decision table + memo** — task class → cost/latency/reliability/coverage → the rule
  each shape implies (§4 #3 deliverable), once the above two land.

## What's built

`workflow/` (16 tests, TDD): `router.py` (full agent task-set coverage, fails closed),
`executor.py` (templated synthesis, honest refusal, judge-compatible tool_calls),
`harness.py` (coverage/latency/cost arithmetic). Agent arm = `agentic-copilot` as-is.
