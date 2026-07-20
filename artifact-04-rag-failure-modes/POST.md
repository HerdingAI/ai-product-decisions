# LinkedIn practice post — draft (Artifact 04)

_Structure per plan §6: hook → question → numbers sentence → one surprising finding →
link to artifact + curriculum units. Written from RESULTS.md. Draft for Carlos's review;
all numbers are demo-internal and reproducible (D15). Not auto-published._

---

When a RAG system is wrong, it's usually confident, fluent, and cites a source.
That's what makes it dangerous — and it's why "let's improve our RAG" is a
budget line, not a plan.

The real question isn't "is our RAG working." The demo always retrieves the
right chunk. It's: **which failure mode dominates, and is the fix worth the
sprint?**

So I measured it. 20 chunks, 18 queries with known answers (3 of them
deliberately unanswerable), one deterministic retriever. The result surprised
me: retrieval was *fine* — 14 of 15 answerable queries hit rank 1. The dominant
failure, 3 of 3 cases, was the opposite: for questions whose answer wasn't in
the corpus at all, the system **confidently returned an irrelevant chunk instead
of saying "I don't know."** A reranker or a reindex — the reflexive fixes —
would have addressed exactly **one** case out of eighteen.

The sharp part: you can't fix this with a confidence threshold. My unanswerable
query scored 0.362; a genuine answer scored 0.258. Confidence and correctness
aren't the same axis. The fix that worked was a coverage gate on the query's
*distinctive* terms — it turned all 3 confident-wrong answers into honest
abstentions. It cost one real answer, lost to a stem mismatch
("accountable" vs "accountability") — which is exactly the ticket for the next
fix. That's the flywheel: each fix's failure names the next one.

Measuring first turned "improve our RAG" into "ship the coverage gate, then add
stemming; don't build the reranker this sprint." That's a backlog, not a vibe.

Full study, code, and the ranked fix list: [link to artifact]

Practices Unit 17 — RAG internals — from the Signal / Noise curriculum: [link]

---

**Reviewer notes for Carlos:**
- All numbers reproduce offline via `python report_rag.py` — no key, no network.
- The corpus is constructed (self-authored, public frameworks) — the post says
  "20 chunks, 18 queries," honest about scale; don't imply a production corpus.
- "one case out of eighteen" = the single buried case a reranker fixes. Exact.
- Insert the two links before posting. A4 discipline — no regulated-domain headline.
