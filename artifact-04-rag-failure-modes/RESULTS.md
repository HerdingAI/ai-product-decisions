# RESULTS — RAG failure modes, ranked by fix effort

**Question:** RAG fails quietly — the model is fluent, a citation is present,
and the retrieval was wrong. The PM question isn't "is our RAG working" (the
demo always retrieves the right chunk); it's **which failure mode dominates, and
is the fix worth the effort.** This measures the failure-mode distribution on a
fixed corpus, ranks the fixes by the mode that actually occurs, applies the one
the data points to, and measures its cost.

Fully offline and deterministic: a pure TF-IDF retriever (no embeddings API, no
network) over a **20-chunk** regulated-document corpus and **18** queries with
gold chunk labels — including 3 whose answer is deliberately **not in the
corpus**. Same corpus + query → same ranking, every run. Reproduce:
`python report_rag.py`.

## Baseline failure-mode distribution (k=3)

| Mode | Count | What it means | Fix it implies |
|---|---:|---|---|
| hit | 14 | gold chunk at rank 1 | — |
| **no_fallback** | **3** | answer absent, retriever returns a confident wrong chunk | abstention / coverage gate |
| buried | 1 | gold chunk retrieved but outranked | reranker |
| wrong_chunk | 0 | gold chunk missed entirely | better chunking / query rewriting |

**The reflexive fixes would have addressed nothing.** The instinct on "improve
our RAG" is bigger index, better chunking, or a reranker. On this data the
retriever is already good at *retrieval* — 14/15 answerable queries hit rank 1,
one is buried. The dominant failure (3 cases) is the opposite problem: for
queries whose answer isn't in the corpus at all, the retriever **confidently
surfaces an irrelevant chunk** instead of abstaining. A reranker or a reindex
fixes zero of those. This is exactly why you measure the distribution before
funding a fix.

## Why a score threshold can't fix it

The obvious patch — "abstain when the top score is low" — fails here. The
unanswerable query q16 ("penalty schedule / fine amount") scores **0.362**,
while the *genuine* answer to q02 (Colorado governance) scores only **0.258**. A
threshold that catches the false positive kills a true one. Confidence and
correctness aren't the same axis, so you can't gate on confidence.

## The fix the data points to: a distinctive-term coverage gate

The signal that *does* separate them is coverage of the query's **distinctive**
(high-idf) terms — including terms absent from the corpus entirely. An
answerable query's rare terms appear in the right chunk; an unanswerable query's
rare terms ("penalty", "fine", "stipend") appear in no chunk. Abstain when the
top chunk fails that coverage bar (`min_idf=1.5, gate=0.4`):

| | baseline | with coverage gate |
|---|---|---|
| hit | 14 | 13 |
| no_fallback (confident wrong) | **3** | **0** |
| correct_abstain | 0 | 3 |
| buried | 1 | 1 |
| false abstain (real answer lost) | 0 | **1** |

**Every confident-wrong answer became an honest "I don't know" (q16/q17/q18).**
The fix is not free: it cost **one** false abstention (q02), where the real
answer was lost — and the cause is precise. The query says "**accountable**" and
"**insurance**"; the gold chunk says "**accountability**" and "**insurers**".
The lexical gate can't match across those stems, so it wrongly judged the chunk
uncovered. That single regression **names the next fix** — stemming/lemmatization
before the gate — which is the whole point of an effort-ranked flywheel: each
fix's failure is the next fix's ticket.

## The decision this produces

A PM walking into the eng conversation with this doesn't say "let's improve our
RAG." They say: **"Our retrieval is fine; our problem is we answer questions we
shouldn't. Ship the coverage gate — it converts 3 confident-wrong answers to
abstentions — then add stemming to recover the one real answer it costs us. Do
not spend the sprint on a reranker; it addresses one case out of eighteen."**
That is retrieval quality turned into a prioritized backlog, not a reindex.

## Scope & honest limits

- **Retrieval modes only.** The fourth canonical mode — "chunk retrieved but the
  answer isn't grounded in it" — is a *generation* failure, not retrieval. A
  lexical grounding proxy is included (`rag.failure_modes.lexical_grounding` /
  `is_grounded`, unit-tested), but the model-quality version of that judgment is
  Artifact 02's `grounded` criterion; this artifact doesn't re-do it.
- **Constructed corpus.** The 20 chunks and 18 queries are self-authored to
  exhibit the modes on realistic regulated-document vocabulary. The *method*
  (measure distribution → rank fixes → apply one → measure its cost) transfers;
  the specific counts are only valid for this corpus. Swapping in a real corpus
  and its gold labels is the intended use.
- **TF-IDF, not embeddings.** A dense retriever would move some counts (fewer
  buried, different coverage behaviour), but the *no_fallback / no-abstention*
  failure is retriever-agnostic — dense retrievers hallucinate confident
  neighbours for out-of-corpus queries too.

## What's built

`rag/retriever.py` (5 tests), `rag/failure_modes.py` (6 tests),
`rag/harness.py` (1 test), `rag/improve.py` (2 tests) — **14 tests, TDD**.
`report_rag.py` runs the whole study; `data/corpus.json` + `data/queries.json`
are the fixed evidence set with gold labels.
