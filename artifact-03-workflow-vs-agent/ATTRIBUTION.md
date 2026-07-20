# Attribution

**Own work (D1).** All code in this artifact — the deterministic workflow arm
(`workflow/`), the agent-arm analysis (`agent_arm/`), the live runners
(`run_agent_arm.py`, `retry_failed.py`), the coverage report, and the tests —
is original work. No forks, no vendored third-party code, no outbound links to
anyone else's repository.

**Systems compared.** Both arms operate over the same task and tools as
`agentic-copilot`, a companion build (own work, MIT).
- The **workflow arm** is an original deterministic re-implementation of that
  task's tool-selection (fixed rules, fails closed).
- The **agent arm** is `agentic-copilot` itself, run live on a real model.

**Modification to the base app (disclosed).** The live agent run surfaced a real
bug: under `deepseek/deepseek-v4-flash` the model emits a spurious `input`
argument on zero-parameter tools, and the MCP adapter forwarded it into the
function, hard-500-ing 33/100 queries. The fix — `_filter_kwargs_for_fn` in
`agentic-copilot/agent/mcp_adapter.py`, added test-first — passes only kwargs the
target function declares. It is committed in the `agentic-copilot` repo (own
work, MIT), not vendored here. The pre-fix baseline is preserved
(`results/agent_arm_baseline_prefix.json`) and reported as the reliability
finding.

**Models.** All model calls go through **OpenRouter** (D6), the single
model-provider standard for this repo. The agent arm used
`deepseek/deepseek-v4-flash`. No first-party inference keys are used or
committed; a reader reproduces the numbers with their own OpenRouter key.

**Data.** Queries are the same self-authored 100-case calibration set as
Artifact 02. Agent-arm outputs (`results/agent_arm.json`) are generated live and
collected verbatim; only response previews are stored. Answer-quality judging
(the one open step) will use Carlos's own labels as sole labeler.

**Cost figure.** Per-query cost is an *estimate* (the chat API returns no token
usage); latency and tool-call counts are measured exactly. Stated as such in
RESULTS.md.

**No employer or business-outcome data (D15).** Only reproducible, demo-internal
numbers (coverage, latency, estimated cost, crash rate). Nothing reflects any
employer's data, systems, or results.

**License.** MIT (repo root `LICENSE`).
