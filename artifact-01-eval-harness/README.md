# Artifact 01 — Eval harness: how I decide an agent is good enough to ship

> Pairs with [Unit 13 — Capstone](https://www.carlosarivero.com/units/unit-13-capstone.html) and ["How I decide an agent is good enough to ship"](https://www.carlosarivero.com/thoughts/how-i-decide-an-agent-is-good-enough-to-ship.html).
> System under test: [`HerdingAI/agentic-copilot`](https://github.com/HerdingAI/agentic-copilot) — a stateful, tool-using LangGraph agent.

## The problem

You have a tool-using agent. It demos well — type a question, it calls a tool,
it answers with citations. The demo always works because you typed the
question the demo was built around. The question a PM actually faces is the
opposite of the demo: **is this good enough to put in front of users, and how
do I know?**

"I tried it a few times and it seemed fine" is not an answer. Neither is a
single accuracy number. The decision is whether the agent meets a bar across
the failures that actually matter — routing, grounding, and the guardrail —
and whether the failures it *does* have are tolerable or ship-blocking.

## The decision

Decide ship / no-ship on a small, hand-labeled golden set, scored against
explicit criteria, with each failure mapped to a named class and checked
against a blast-radius threshold. The output is not "92% accurate." It is a
verdict, the blockers behind it, and the known issues that can wait.

## Options and trade-offs

- **Vibes-based testing** — cheapest, and exactly what produces the demo
  that always works. Rejected: it has no memory of what was tried and can't
  tell you what changed between builds.
- **Crowd-sourced eval (a big labeled set, agreement scores)** — the right
  answer for a mature product. Wrong for a pre-ship decision on a 32-case
  spine: the setup cost dwarfs the signal, and "what should happen" on the
  canonical paths is not a matter of opinion.
- **Criteria-first on a hand-labeled golden set (this artifact)** — small,
  opinionated, and the criteria are the artifact. The trade-off is coverage:
  thirty-odd cases will not find a subtle regression in a long-tail query.
  That is acceptable for the ship decision; it is not acceptable as the only
  eval forever. Artifact #2 (LLM-as-judge, validated) is the automation step
  that scales this without losing the criteria.

One deliberate boundary: the criteria here are **deterministic and
rule-based**. This artifact answers "how do I decide it's shippable," not
"how do I automate judgment." Mixing in an LLM judge here would muddle the
decision being demonstrated.

## What I measured

The golden set is 32 cases across four groups — routing (did it pick the
right tool?), grounding (does the answer cite its source?), guardrail (does
it say "I don't know" when it should?), and adversarial (ambiguous asks,
missing context, out-of-scope, injection attempts — 12 of the 32 cases,
comfortably over a third of the set). Each case carries the tool a correct
agent *should* call, any tools it must *not* call, the criteria that decide
the response, and a `blast_radius` tag (`autonomous` or `reviewed`) that
decides which threshold tier it's judged against — see
[`criteria.md`](criteria.md) for the rubric itself, written before this run,
and `eval_harness/taxonomy.py` for the two threshold tables and why they
differ.

Run against `agentic-copilot` on its deterministic mock LLM (temperature 0,
so the numbers are reproducible):

**Autonomous tier (24 cases — answers that could flow straight into an
unreviewed action):**

| Criterion | Pass rate | Threshold | Gate |
|---|---|---|---|
| answers_question | 92% (12/13) | ≥90% | PASS |
| cites_source | 77% (10/13) | ≥95% | issue |
| no_wrong_tool | 92% (12/13) | ≥95% | BLOCKER |
| tool_correct | 62% (8/13) | ≥90% | BLOCKER |
| idk_when_no_tool | 45% (5/11) | ≥100% | BLOCKER |
| no_fabrication | 45% (5/11) | ≥100% | BLOCKER |

**Reviewed tier (8 cases — ambiguous/compound queries where a human reads
the answer before it's acted on, so the bar is real but softer):**

| Criterion | Pass rate | Threshold | Gate |
|---|---|---|---|
| answers_question | 100% (6/6) | ≥60% | PASS |
| cites_source | 100% (3/3) | ≥60% | PASS |
| no_wrong_tool | 100% (5/5) | ≥80% | PASS |
| tool_correct | 100% (6/6) | ≥60% | PASS |
| idk_when_no_tool | 0% (0/1) | ≥80% | BLOCKER |
| no_fabrication | 50% (1/2) | ≥80% | BLOCKER |

**Verdict: do not ship — on both tiers.** Blast radius is a lens on the same
failures, not a way to average them away: even the softer reviewed bar
still fails. The failures map cleanly to the taxonomy:

- **wrong_tool** — the canonical misroute persists at scale: *"Which model
  is best for assessing compliance with Article 9?"* fires `query_by_model`
  and `get_eu_ai_act_article` instead of `get_best_model_for_article`; the
  "compare two models" case misroutes the same way. These are the
  keyword-overlap failures a real LLM faces when two tools have similar
  descriptions — documented in `agentic-copilot`'s `docs/DECISIONS.md`, and
  caught automatically here.
- **no_answer / missing_citation** — two enumeration cases
  ("what models are available," "what task categories exist") call the
  right tool *and* an extra wrong one, and the extra call's error message
  (`Field required`) leaks into the response instead of the actual tool
  result. Tool selection can be correct and answer synthesis can still fail
  — a distinct failure surface the criteria catch separately on purpose.
- **hallucination — the largest and most important finding at 32 cases.**
  The mock LLM has a default-fallback behavior: when no keyword rule fires
  cleanly, it still calls `query_by_jurisdiction` and grounds the answer in
  Colorado's SB 26-189 — a real regulation, cited with real fields, entirely
  unrelated to the question asked. This fired on *five separate adversarial
  cases* the smaller 10-case set never exercised: a weather query, a flight-
  booking request, a fictional jurisdiction ("Wakanda"), garbled noise text,
  and the single-word query "regulations." At 10 cases this looked like an
  edge case (one SEC-2031 miss); at 32 cases it's a pattern — the fallback
  path itself hallucinates by design, not by accident. For a compliance
  agent, one invented requirement is disqualifying on its own — hence the 100%
  threshold on the tier where nobody reviews the output.

The larger set didn't just confirm the original finding — it found a worse
one underneath it. That's the argument for the ⅓-adversarial requirement:
the canonical happy-path cases would never have surfaced the fallback
behavior, because a real user asking a real question rarely triggers "no
rule matched."

## What I'd ship, and why

The harness ships now. The agent it evaluates does not.

The artifact is the harness, the criteria, the taxonomy, and the
blast-radius thresholds — the reusable decision machinery. The specific pass
rates describe the mock LLM's heuristics and will move the moment a real LLM
is swapped in; the decision process does not. Run the harness against a real
model and the same gate tells you whether *that* model is shippable, with the
same failure vocabulary.

The remediation the harness prescribes for `agentic-copilot` is concrete:
reorder the mock's selection rules so `get_best_model_for_article` and
`compare_models` are matched before the broader `query_by_model` keyword,
tighten the descriptions so the ranking sticks under a real LLM, fix the
`list_all_models` / `list_all_articles` argument-schema bug leaking `Field
required` errors into responses, and — the highest-priority item at 32
cases — remove the default-fallback tool call entirely so an unmatched
query falls through to "I don't know" instead of grounding itself in
Colorado's SB 26-189 by default. None of that is a guess — each item is a
blocker the harness named.

## Tools used

- **Hand-rolled harness, not [promptfoo](https://www.promptfoo.dev/).**
  Promptfoo is a strong general fit for exactly this kind of eval — YAML
  test cases, assertion-based scoring, CI integration — and would be the
  right call for a team standardizing evals across many agents. It was
  passed over here for one reason specific to this artifact: the point of
  Artifact 01 is to *show the judgment layer*, not just run it — the golden
  set, the criteria, the taxonomy, and the two-tier blast-radius thresholds
  are the product, and writing them as plain Python keeps that judgment
  visible and diffable in the same review as the results, rather than split
  across a YAML config and a plugin's internal scoring logic. A future
  artifact that just needs to *run* an eval at scale, rather than demonstrate
  how one is built, should default to promptfoo instead of re-deriving this.
- **`httpx`** — synchronous HTTP client for the runner; no async story is
  needed for 32 sequential, rate-limited calls.
- **Standard library (`dataclasses`, `re`, `json`)** for everything else —
  no need for a scoring framework when the scoring logic is six small,
  independently testable functions.

## Run it

```bash
# 1. Start the system under test (in the agentic-copilot repo)
git clone https://github.com/HerdingAI/agentic-copilot.git
cd agentic-copilot
pip install -r requirements.txt
./run.sh                       # backend on http://127.0.0.1:8000

# 2. Run the harness (in this artifact)
cd artifact-01-eval-harness
pip install -r requirements.txt
python run.py --target http://127.0.0.1:8000
# → results/results.json + results/SUMMARY.md, and a ship verdict on stdout
```

The committed `results/` are from a real run against the mock LLM. Regenerate
them against any target — including a real LLM backend — with the same
command.

## Layout

```
artifact-01-eval-harness/
├── criteria.md              # the rubric, in prose, written before results
├── run.py                   # entry point
├── eval_harness/
│   ├── golden_set.py        # 32 hand-labeled cases (routing / grounding / guardrail / adversarial)
│   ├── criteria.py          # the rubric, in code — deterministic, rule-based
│   ├── taxonomy.py          # failure classes + two-tier blast-radius thresholds + ship gate
│   ├── runner.py            # drives /api/chat, fresh thread per case, rate-limit-paced
│   └── report.py            # results.json + SUMMARY.md, split by tier
└── results/
    ├── results.json
    └── SUMMARY.md
```

## What this is not

Not a benchmark. Not powered to catch regressions in long-tail queries. Not a
substitute for the LLM-as-judge automation in Artifact #2. It is the
pre-ship decision a PM owns — made runnable, with the criteria stated out
loud.