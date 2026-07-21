# ai-product-decisions

**Seven product decisions an AI PM actually faces — each one as runnable code, a
real eval, and the trade-off math behind the call.**

Most AI-PM portfolios are screenshots and confidence. This one is a repo you can
clone and run, where the answer changes when you change the inputs — and where
the eval sometimes tells me *no* and I listen. Code second, judgment first.

Each artifact is one folder: the decision in plain language, the code that makes
it, and the numbers it produced. Read the write-up, or run it yourself.

---

## The decisions

| # | The question | What the numbers said |
|---|---|---|
| [01](artifact-01-eval-harness/) | Is this agent good enough to ship? | **No — and here's the receipt.** The harness returns a no-ship verdict with the blocking cases named, not a single accuracy number to argue with. |
| [02](artifact-02-llm-as-judge/) | Can I trust an LLM to grade my agent? | Two criteria yes (κ 0.49 / 0.56), one flat broken (κ 0.04) — measured against 100 hand labels. A judge you don't validate is just a second opinion with no résumé. |
| [03](artifact-03-workflow-vs-agent/) | Workflow or agent? | The agent covers more (81 vs 64). The workflow wins on quality (28–13, 21 ties) at a fraction of the cost. Flexibility isn't free — do the arithmetic. |
| [04](artifact-04-rag-failure-modes/) | Which RAG fix is worth the effort? | Retrieval was never the problem (14/15 hit rank 1). The fix is a coverage gate, not a fancier embedder. Read the failures before you rebuild. |
| [05](artifact-05-model-selection/) | Which model? | The leaderboard leader wins **1 of 4** realistic budgets. "Best" is undefined until you name the constraint — then the pick is mechanical. |
| [06](artifact-06-error-analysis/) | A pass rate dropped — now what? | Turn it into a backlog: 51 traces → 7 themes → 3 root causes, and one *broken criterion* the dashboard was quietly hiding. |
| [07](artifact-07-guardrails/) | Does the guardrail actually work? | Attack success 96% → 14%. But benign traffic paid for it: 100% → 70%. Report both halves, or it isn't a measurement. |

Every row links to the folder with the code and the full write-up. Start
anywhere — they stand alone.

---

## Why these seven (the demand math, not taste)

The list isn't a wishlist. It's reverse-engineered from what AI-PM roles actually
hire on:

- **The vocabulary** the postings use — *agentic*, *LLM*, *RAG*, *evals*. The
  artifacts live in that language instead of talking around it.
- **The highest-leverage skill** is evals, so the eval thread is the spine:
  three of seven artifacts are evals (01, 02, 06), and a fourth (07) measures a
  defense the same way.
- **The case-round topics** — eval design, workflow-vs-agent, model selection,
  metric definition. Together the seven cover all four.

---

## One body of work, three surfaces

These artifacts don't invent demo systems to grade. They evaluate the repos
already on the profile:

- **01** and **03** put [`agentic-copilot`](https://github.com/HerdingAI/agentic-copilot)
  — a stateful, tool-using agent — under test, once as a ship decision and once
  against a fixed workflow doing the same job.
- **05** reasons from [`document-ai-bench`](https://github.com/HerdingAI/document-ai-bench).

The [course](https://www.carlosarivero.com/course.html) is the theory. The
[essays](https://www.carlosarivero.com/thoughts.html) are the argument. This repo
is the same decisions as working code. Every artifact names its course unit; the
course links back. **One connected system, three surfaces.**

---

## License

MIT — see [LICENSE](LICENSE).
