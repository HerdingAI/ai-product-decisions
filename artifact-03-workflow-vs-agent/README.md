# Artifact 03 — Workflow vs. agent: the arithmetic

> Pairs with [Unit 04](https://www.carlosarivero.com/units/unit-04-workflows-vs-agents.html) / [Unit 12](https://www.carlosarivero.com/units/unit-12-cost-and-latency.html) and ["Workflow or agent? Do the arithmetic first"](https://www.carlosarivero.com/thoughts/workflow-or-agent-do-the-arithmetic-first.html).
> Status: **both arms measured — coverage/cost/latency/reliability done; quality-judging gated on human labels.** See [RESULTS.md](RESULTS.md).
> System under test: [`HerdingAI/agentic-copilot`](https://github.com/HerdingAI/agentic-copilot) — the agent side of the comparison.
>
> **Numbers (100 shared queries; agent = `deepseek/deepseek-v4-flash` live via OpenRouter):** coverage — workflow **64/100**, agent **81/100** (agent recovers **30/36** of the workflow's fail-closed queries, almost all open-ended `usability` asks). Cost/latency — workflow **$0 at <1 ms**; agent **~$0.00055/query (est.), p50 17.6 s / p95 44.9 s**, mean 3.82 tool calls with a tail to 20. Reliability — the agent hard-500'd on **33/100** queries until a one-line adapter fix (spurious `input` kwarg on zero-arg tools); the workflow's fail-closed design has zero crash surface. Rule: **workflow for tool-shaped lookups, agent for open-ended synthesis, workflow-first-with-agent-fallback for the hybrid path.**

## The problem

"Should we build this with an agent or a workflow?" is asked in every AI
product review, and usually answered with a vibe. Agents are flexible and
demo beautifully; workflows are predictable and boring. The decision is
rarely "agent" or "workflow" on aesthetics — it is arithmetic: for a specific
task, what does the agent's flexibility cost in latency, spend, and
compounding failure, and is that cost worth what the workflow cannot do?

## The decision

Build the same task both ways — once as the existing `agentic-copilot` agent
(tool-selecting, multi-turn), once as a fixed workflow (pinned tool sequence,
no routing decisions) — and publish the cost, latency, and failure
arithmetic side by side. The output is a table and a defensible rule for when
each shape wins, not a slogan.

## Options and trade-offs

- **Agent only** — handles the long tail of query shapes, at the cost of a
  routing decision every turn (latency, a token spend on reasoning, and a
  misroute risk that compounds across turns).
- **Workflow only** — fast, cheap, deterministic, and dead on any query the
  pinned sequence wasn't built for.
- **Both, measured (this artifact)** — the work is in the comparison. The
  trade-off is build cost: you pay to implement the task twice. That cost is
  bounded and one-time; the lesson is reusable across every future
  agent-vs-workflow call.

## What I'll measure

- **Cost per query** — tokens and dollars, agent vs. workflow, on the same
  task set.
- **Latency** — end-to-end, p50 and p95. The agent's routing step is the
  likely gap; quantify it.
- **Compounding failure** — the case for the workflow. If each tool step is
  95% reliable, an 8-step workflow is `0.95⁸ ≈ 66%` end-to-end; the agent can
  recover a bad step by re-routing, but at the cost of more calls. Publish
  the actual reliability numbers, not the illustrative `0.95⁸`.
- **Coverage** — the case for the agent. What fraction of a realistic query
  distribution does the workflow serve without a fallback, vs. the agent?

## What I'd ship, and why

A one-page decision table — task class, cost, latency, reliability, coverage
— and the rule it implies: *use a workflow when the task is bounded and the
step-reliability arithmetic compounds badly; use an agent when the query
distribution is wide and the recovery is worth the spend.* The rule is the
artifact; the numbers are the receipts.

_Shipped: the fixed-workflow implementation of the agentic-copilot task set, a
live agent-arm runner on a real model, and the comparison table + decision memo
in [RESULTS.md](RESULTS.md). The shared-served-set answer pairs for
quality-judging are assembled (62/100 pairs, full response text both arms,
blind order) — Carlos's labeling pass against Artifact 02's rubric is the one
remaining step (sole-labeler discipline)._