# Attribution

**Own work (D1).** All code in this artifact — the golden set
(`eval_harness/golden_set.py`), the deterministic criteria
(`eval_harness/criteria.py`), the failure taxonomy and two-tier blast-radius
gate (`eval_harness/taxonomy.py`), the runner (`eval_harness/runner.py`), the
report (`eval_harness/report.py`), `run.py`, and the tests — is original work.
No forks, no vendored third-party code, no comparison arms, no outbound links to
anyone else's repository. `promptfoo` is named in the README only to explain
why it was *not* used here; nothing from it is included.

**System under test.** `HerdingAI/agentic-copilot` is Carlos's own build. The
committed run is against its deterministic mock LLM (temperature 0), so the
numbers reproduce exactly with no API key. Point `--target` at a real backend to
regenerate against any model.

**Data.** The 32 golden cases are self-authored. The regulated-document texture
(EU AI Act articles, Colorado insurance regulation) is public-knowledge framing
used as *difficulty*, never a headline (A4); it is not copied from and does not
reproduce any proprietary or employer knowledge base. The labels are the
author's own, as sole labeler, with the rubric (`criteria.md`) written before
the run.

**Scoring is deterministic.** No LLM judge is used in this artifact by design;
scoring is six small rule-based functions. Validated LLM-as-judge scoring is
[Artifact 02](../artifact-02-llm-as-judge/).

**No models, no keys.** The committed results run on a mock backend; nothing
here requires an API key, and no secret appears in the repo or its history.

**No employer or business-outcome data (D15).** Only reproducible, demo-internal
eval numbers. Nothing reflects any employer's data, systems, or results.

**License.** MIT (repo root `LICENSE`).
