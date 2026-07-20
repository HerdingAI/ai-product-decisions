# Capstone — the eval harness as the system (Unit 13)

_The Unit-13 one-pager, written to the curriculum's capstone spec: the
architecture and why, the eval plan, the production plan, and the data/cost
risks. The "system" here is the **ship-decision harness**, not the agent it
judges — the reusable machinery that turns "it seemed fine" into a defensible
ship / no-ship verdict._

## Architecture pattern & why

A **criteria-first, two-tier blast-radius eval harness** over a hand-labeled
golden set, scoring deterministic rule-based criteria and mapping every failure
to a named class.

- **Golden set** (`eval_harness/golden_set.py`): 32 cases across routing /
  grounding / guardrail / adversarial, each carrying the tool the agent *should*
  call, tools it must *not* call, the criteria that decide the response, and a
  `blast_radius` tag.
- **Criteria in code** (`eval_harness/criteria.py`): six small, independently
  testable functions — deterministic, not an LLM judge. This artifact answers
  "how do I decide it's shippable," so the scoring stays inspectable and
  diffable in the same review as the results.
- **Taxonomy + ship gate** (`eval_harness/taxonomy.py`): each failed criterion
  becomes a named failure class a PM can act on ("fix tool-selection ordering"),
  and two threshold tables — a strict **autonomous** tier (answers that could
  flow into unreviewed action) and a softer **reviewed** tier (a human reads the
  answer first). The gate fails if *either* tier fails.

**Why this shape:** the value is the judgment layer, not the plumbing. Writing
the criteria and thresholds as plain Python keeps the decision visible; the
blast-radius split is the load-bearing idea — it refuses to let a high average
hide a catastrophic failure on the unreviewed path.

## Eval plan

- Binary pass/fail per criterion (never a Likert blur), scored on the same run.
- One-third adversarial floor (12/32): canonical happy-path cases never trigger
  the "no rule matched" fallback that turns out to be the real failure surface.
- Rubric (`criteria.md`) written **before** the run; thresholds fixed before
  scoring. Sole labeler disclosed.
- Verdict is a decision + blockers + deferrable known-issues, not a percentage.
- Scale path: [Artifact 02](../artifact-02-llm-as-judge/) validates an LLM judge
  against these same criteria so the eval automates without losing them.

## Production plan

- The harness is backend-agnostic: `python run.py --target <url>` runs the same
  gate against any OpenAI-compatible endpoint, so the ship decision re-runs for
  free against a real model or a new build.
- Cost and latency become first-class the moment a real backend replaces the
  mock (both are $0 / N/A on the deterministic mock used for the committed run).
- Gate wired into CI as a pre-ship check; the failure vocabulary is stable
  across model swaps even as specific pass rates move.
- Remediation is prescribed per-blocker (reorder tool-selection rules; route
  unmatched queries to an honest "I don't know" instead of grounding in an
  unrelated regulation).

## Data & cost risks

- **Small-N coverage:** 32 cases will not catch a subtle long-tail regression.
  Mitigation: this is a *pre-ship gate*, not the only eval forever; the golden
  set grows and Artifact 02 scales it.
- **Mock-LLM specificity:** the committed pass rates describe the mock's
  heuristics; they will move under a real LLM. The decision process is what
  transfers, and that is stated explicitly rather than hidden.
- **Sole-labeler bias:** one labeler on a small set is a credibility hole if
  undocumented; `criteria.md` amateur-proofs it by fixing the rubric before
  labeling and disclosing the labeler.
- **Cost (real backend):** at 32 sequential rate-limited calls per run the
  inference cost is negligible, but it is non-zero once the mock is replaced —
  metered per-query alongside quality, per Unit 12.
