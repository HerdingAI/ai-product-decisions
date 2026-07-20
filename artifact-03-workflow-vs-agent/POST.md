# LinkedIn practice post — draft (Artifact 03)

_Structure per plan §6: hook → question → numbers sentence → one surprising finding →
link to artifact + curriculum units. Written from RESULTS.md. Draft for Carlos's review;
all numbers are demo-internal and reproducible (D15). Not auto-published._

---

"Should this be an agent?" is the most expensive question in AI product work,
because the honest answer is usually "for part of it."

So I stopped arguing and measured it. I took one bounded task — regulatory
lookups — and built it twice: a deterministic **workflow** (fixed rule → tool,
fails closed) and an **agent** (an LLM picks tools and loops). Same 100 queries,
same tools, head to head.

The numbers: the workflow served **64/100** in under a millisecond for $0. The
agent served **81/100** — but at **p50 17.6 s, p95 44.9 s**, ~$0.0005 a query,
and a mean of 3.8 tool calls with a tail that hit **20 tool calls on a single
query**. And nearly all of the agent's extra coverage was in one place:
open-ended asks ("draft one sentence for the board deck") that map to no tool at
all. On pure lookups, the two **tied** — the LLM's routing bought nothing.

The surprising part was a reliability cliff. The agent's *first* run hard-crashed
on **33 of 100 queries** — the model emitted a tool argument the adapter didn't
expect, and there's no fail-closed on a generated tool call, so a third of
traffic 500'd. One test-first adapter fix took it to zero. A workflow can't have
that failure mode: its tool calls are written by a human, not generated per
request.

The takeaway isn't "agents win" or "workflows win." It's **route by task
shape**: workflow for tool-shaped lookups, agent for open-ended synthesis, and
workflow-first-with-agent-fallback for the hybrid — which recovered 30 of the 36
gaps while paying agent latency on only a third of traffic.

Full comparison, code, and the decision memo: [link to artifact]

Practices Units 07 (workflows vs. agents) and 12 (cost/latency/reliability
trade-offs) from the Signal / Noise curriculum: [link]

---

**Reviewer notes for Carlos:**
- All numbers from RESULTS.md; agent = deepseek-v4-flash live via OpenRouter.
- Cost is an *estimate* (no token usage from the chat API) — post says "~$0.0005"
  not a billed figure; keep that hedge in.
- The 33% crash → 0 story reflects well (found live, fixed test-first) but it's a
  bug in the companion app — fine to state, just confirm you're comfortable.
- Quality-judging (are the served answers actually *good*) is still open, gated on
  your labels. Don't imply the quality comparison is done.
- Insert the two links before posting. A4 discipline — no regulated-domain headline.
