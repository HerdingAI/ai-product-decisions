# Artifact 04 — RAG failure modes, ranked by fix effort

> Pairs with [Unit 17 — RAG internals](https://www.carlosarivero.com/units/unit-17-rag-internals.html) and a knowledge-assistant build (anonymized).
> Status: **planned — ships on cadence.**

## The problem

RAG is the default answer to "how do we let the model use our documents," and
the default failure is "we shipped it, the answers look plausible, and they're
wrong in ways no one notices until a customer does." RAG fails quietly — the
model is fluent, the citation is present, and the retrieval was bad. The PM
problem is not "is our RAG working" (the demo always retrieves the right
chunk); it is "where does it break, and which fix is worth the effort."

## The decision

Run a retrieval-quality case study that names the failure modes — wrong chunk
retrieved, right chunk but buried, chunk retrieved but answer not grounded in
it, no relevant chunk and no fallback — and ranks the fixes by effort vs.
lift. The output is a prioritized list, not a reindex.

## Options and trade-offs

- **Bigger index / more chunks** — the reflex fix. Often the least
  cost-effective: it raises recall marginally and hurts precision.
- **Better chunking** — cheap, sometimes decisive, sometimes irrelevant to
  the actual failure mode.
- **Reranker** — a real lift on the "right chunk buried" failure, at a
  latency and cost price.
- **Query rewriting / HyDE** — helps the "wrong query, wrong chunk" failure,
  adds a model call.
- **Grounding check / citation enforcement** — the only fix for "retrieved
  it, didn't use it"; structural, not retrieval.

The trade-off is that the right fix depends on *which* failure mode dominates
in your data, which you don't know until you measure. Measuring first is the
artifact.

## What I'll measure

- Per-query: was the right chunk retrieved? (rank, score) Did the answer use
  it? (grounding check) If not, which failure mode?
- Failure-mode distribution across a labeled query set — so the fix budget
  goes where the failures actually are.
- Fix-effort ranking: for each candidate fix, the implementation cost and the
  measured lift on the failure mode it targets.

## What I'd ship, and why

The failure-mode distribution and the effort-ranked fix list — the artifact a
PM brings to the eng conversation that turns "let's improve our RAG" into
"spend two days on a reranker, it addresses 40% of the failures; don't
reindex, that addresses none of the ones we measured." Anonymized around the
source knowledge base; the method, not the corpus, is what's shared.

_Planned: a retrieval-quality harness, a labeled failure-mode set, and the
ranked fix analysis. No code committed yet — ships when the cadence reaches
it, ≤2 hrs/wk._