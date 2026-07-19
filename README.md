# ai-product-decisions

**PM judgment, made runnable.** Each artifact is one product decision AI PMs
actually face — with working code, an eval, and the trade-off math.

The [course](https://www.carlosarivero.com/course.html) is the theory; the
[essays](https://www.carlosarivero.com/thoughts.html) are the argument. This
repo is the same decisions as **working code** — not a tutorial, not a demo,
a system you can run the decision through and see the answer change.

---

## Why these artifacts (the demand math, not taste)

The artifact list is derived from three measured findings, so it maps to the
work the role actually demands:

1. **Vocabulary demand** — the lexicon AI-PM roles hire on: *agentic* (16.7%
   of postings), *LLM* (12.2%), *GenAI* (3.4× enriched), *RAG / embeddings*.
   The artifacts live in that vocabulary.
2. **Skill leverage** — evals are the highest-leverage AI-PM interview skill.
   The eval thread is the priority spine; **three of six artifacts are eval
   artifacts** (01, 02, 06).
3. **Case-round topics** — eval design, workflow-vs-agent, model selection,
   metric definition. Every artifact rehearses at least one; together they
   cover all four.

---

## The artifacts

Each artifact is one folder: README (the decision, in PM voice) + runnable
code + data/results. Code second, judgment first.

| # | Artifact | Decision it makes | Course unit | Status |
|---|---|---|---|---|
| 01 | [Eval harness — "is this agent good enough to ship"](artifact-01-eval-harness/) | Ship / no-ship on a criteria-first golden set, with a failure taxonomy and blast-radius thresholds | [Unit 13](https://www.carlosarivero.com/units/unit-13-capstone.html) · Essay 12 | **Shipped** |
| 02 | [LLM-as-judge, validated](artifact-02-llm-as-judge/) | Whether to trust a judge to gate releases — measured against human labels, binary over Likert, where it breaks | [Unit 15](https://www.carlosarivero.com/units/unit-15-llm-as-judge.html) | Planned |
| 03 | [Workflow vs. agent — the arithmetic](artifact-03-workflow-vs-agent/) | When the agent's flexibility is worth its cost, latency, and compounding-failure penalty | [Units 04](https://www.carlosarivero.com/units/unit-04-workflows-vs-agents.html) / [12](https://www.carlosarivero.com/units/unit-12.html) · Essay 2 | Planned |
| 04 | [RAG failure modes, ranked by fix effort](artifact-04-rag-failure-modes/) | Which RAG fix is worth the effort — measured by failure-mode distribution | [Unit 17](https://www.carlosarivero.com/units/unit-17-rag.html) | Planned |
| 05 | [Model selection under constraints](artifact-05-model-selection/) | A defensible selection workflow with cost/latency as first-class criteria | [Unit 07](https://www.carlosarivero.com/units/unit-07-model-selection.html) | Planned |
| 06 | [Error analysis & the improvement flywheel](artifact-06-error-analysis/) | Turning a pass rate into a backlog — open/axial coding, criteria drift | [Unit 14](https://www.carlosarivero.com/units/unit-14-error-analysis.html) | Planned |

Artifact 01 anchors the repo and ships first; 02–06 follow on cadence
(≤2 hrs/wk; cadence beats volume).

---

## One body of work — the artifacts evaluate the repos already on the profile

The flagship artifacts don't invent demo systems to evaluate. They evaluate
the repos that are already here:

- **Artifact 01 (eval harness)** uses
  [`agentic-copilot`](https://github.com/HerdingAI/agentic-copilot) as its
  system under test — a conversational, tool-using agent evaluated end to end.
- **Artifact 03 (workflow vs. agent)** rebuilds the same task
  `agentic-copilot` performs as a fixed workflow, then publishes the
  cost / latency / failure table.
- **Artifact 05 (model selection)** uses
  [`document-ai-bench`](https://github.com/HerdingAI/document-ai-bench) as its
  evidence base.

Every artifact README names its course unit; the
[course page](https://www.carlosarivero.com/course.html) links back. **Repo ↔
course ↔ essays: one connected system, three surfaces.**

---

## The standalone-repo rule

No new standalone repos for artifacts, examples, or exercises — those live
as folders *here*. A new repo is justified only for a shipped product (the
[site](https://github.com/HerdingAI/carlosarivero), a live tool), never for
an artifact. This keeps one funnel, one anti-clutter boundary, and the hours
cap all aligned.

---

## License

MIT — see [LICENSE](LICENSE).