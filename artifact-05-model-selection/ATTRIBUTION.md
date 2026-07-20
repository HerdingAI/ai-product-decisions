# Attribution

**Own work (D1).** All code in this artifact — the selection core
(`selection/core.py`), the worked-example report (`report_selection.py`), and
the tests — is original work. No forks, no vendored third-party code, no
outbound links to anyone else's repository.

**Evidence base.** The per-model numbers come from `document-ai-bench`, a
companion benchmark build (own work, Apache-2.0). This artifact reads that
benchmark's already-computed aggregates and adds the selection workflow on top;
it does not modify the benchmark and makes no model calls of its own.

**Models.** The underlying benchmark run used **OpenRouter** (D6) across
`openai/gpt-4o`, `anthropic/claude-sonnet-5`, `google/gemini-2.5-pro`,
`meta-llama/llama-4-maverick`, and `meta-llama/llama-3.3-70b-instruct`. No
first-party inference keys are used or committed; a reader reproduces the
benchmark with their own OpenRouter key and re-runs the selection with none.

**Data & scoring.** Accuracy, hallucination rate, latency, and cost are the
benchmark's own metrics (`document-ai-bench/RUBRIC.md`), including a
control-task-aware planted-error scorer — not a human re-label. Selection
quality is bounded by the benchmark's scoring quality, disclosed in that spoke.
No new subjective human labeling is required: a budget constraint is objective
arithmetic, so this artifact is fully reproducible without a human-labeling pass.

**No employer or business-outcome data (D15).** Only reproducible,
demo-internal benchmark numbers a stranger can regenerate. Nothing reflects any
employer's data, systems, or results. The regulated-document texture is the
benchmark's public task set, kept in-material and never a headline (A4).

**License.** MIT (repo root `LICENSE`).
