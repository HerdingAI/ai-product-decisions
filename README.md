# AI Product Decisions

Each folder here is one decision AI product managers actually face — should this
agent ship, workflow or agent, which model, is the guardrail working — worked
through as running code, an eval, and the numbers that settled it.

Some of the verdicts came back no. Those stayed in. A harness that only ever
says yes isn't measuring anything, and the no-ship write-ups turned out to be
the most useful ones.

Read the write-ups, or clone and run them — the answers change when you change
the inputs.

---

## The decisions

| # | The question | What the numbers said |
|---|---|---|
| [01](artifact-01-eval-harness/) | Is this agent good enough to ship? | No. The harness returns a no-ship verdict with the blocking cases named — not a single accuracy number to argue about. |
| [02](artifact-02-llm-as-judge/) | Can an LLM grade my agent? | Partly. Two criteria agreed with human labels well enough to use (κ 0.49, 0.56); one didn't (κ 0.04). Validated against 100 hand labels first. |
| [03](artifact-03-workflow-vs-agent/) | Workflow or agent? | The agent covered more cases (81 vs 64). The workflow produced better output on the shared ones (28–13, with 21 ties) at a fraction of the cost. |
| [04](artifact-04-rag-failure-modes/) | Which RAG fix is worth the effort? | Retrieval was fine — 14 of 15 failures had the right document at rank 1. The failures were coverage gaps, so the fix is a gate, not a better embedder. |
| [05](artifact-05-model-selection/) | Which model? | The leaderboard leader won 1 of 4 realistic budget scenarios. Once the constraint is named, the pick is mechanical. |
| [06](artifact-06-error-analysis/) | A pass rate dropped — now what? | 51 failing traces → 7 themes → 3 root causes. One of them was a broken criterion, not a broken model. |
| [07](artifact-07-guardrails/) | Does the guardrail work? | Attack success fell from 96% to 14%. Benign traffic paid for it: 100% → 70% pass. Both halves reported, because one without the other isn't a measurement. |

Each artifact stands alone; start anywhere.

---

## Why these seven

They're the decisions that kept recurring across the AI systems I've shipped —
the places where a team is about to spend a quarter and the answer is checkable
in a week. Three of the seven are evaluation artifacts (01, 02, 06) and a fourth
measures a defense the same way (07), because in practice that's where shipping
decisions actually get made.

Artifacts 01 and 03 use [`agentic-copilot`](https://github.com/HerdingAI/agentic-copilot),
a stateful tool-using agent elsewhere on this profile, as their system under
test. Artifact 05 draws on [`document-ai-bench`](https://github.com/HerdingAI/document-ai-bench).
Each write-up links the unit of
[How to make AI products](https://www.carlosarivero.com/course.html) — my free
24-unit curriculum — that covers its theory; longer arguments live in the
[essays](https://www.carlosarivero.com/thoughts.html).

Built on good open-source tools where they exist; each artifact's write-up says
which and why. The cases, criteria, and thresholds are my own.

---

## License

MIT — see [LICENSE](LICENSE).
