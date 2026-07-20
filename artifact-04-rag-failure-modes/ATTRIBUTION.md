# Attribution

**Own work (D1).** All code in this artifact — the TF-IDF retriever
(`rag/retriever.py`), the failure-mode classifier (`rag/failure_modes.py`), the
harness (`rag/harness.py`), the coverage-gate improvement (`rag/improve.py`),
the report (`report_rag.py`), and the tests — is original work. No forks, no
vendored third-party code, no embeddings/model APIs, no network calls, no
outbound links to anyone else's repository.

**Data.** The 20-chunk corpus (`data/corpus.json`) and 18 gold-labeled queries
(`data/queries.json`) are **self-authored** to exhibit the canonical RAG
retrieval failure modes on realistic regulated-document vocabulary. They
paraphrase publicly-known regulatory frameworks (Colorado SB 21-169, the NAIC AI
model bulletin, EU AI Act articles, ECOA/Reg B, SR 11-7, CPRA, BIPA, Utah AI
Policy Act); they are not copied from, and do not reproduce, any proprietary or
employer knowledge base. The gold chunk labels are the author's own, and — because
retrieval correctness against a known corpus is **objective** — no subjective
human-labeling pass is required to validate them.

**No models, no keys.** This artifact is fully offline and deterministic (pure
TF-IDF). There is nothing to reproduce with an API key; `python report_rag.py`
regenerates every number.

**No employer or business-outcome data (D15).** The corpus is constructed from
public regulatory texture kept in-material and never a headline (A4). Nothing
here reflects any employer's data, systems, corpus, or results.

**License.** MIT (repo root `LICENSE`).
