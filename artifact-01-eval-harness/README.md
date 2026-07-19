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
  answer for a mature product. Wrong for a pre-ship decision on a 10-case
  spine: the setup cost dwarfs the signal, and "what should happen" on the
  canonical paths is not a matter of opinion.
- **Criteria-first on a hand-labeled golden set (this artifact)** — small,
  opinionated, and the criteria are the artifact. The trade-off is coverage:
  ten cases will not find a subtle regression in a long-tail query. That is
  acceptable for the ship decision; it is not acceptable as the only eval
  forever. Artifact #2 (LLM-as-judge, validated) is the automation step that
  scales this without losing the criteria.

One deliberate boundary: the criteria here are **deterministic and
rule-based**. This artifact answers "how do I decide it's shippable," not
"how do I automate judgment." Mixing in an LLM judge here would muddle the
decision being demonstrated.

## What I measured

The golden set is ten cases across three groups — routing (did it pick the
right tool?), grounding (does the answer cite its source?), and guardrail
(does it say "I don't know" when it should?). Each case carries the tool a
correct agent *should* call, any tools it must *not* call, and the criteria
that decide the response.

Run against `agentic-copilot` on its deterministic mock LLM (temperature 0,
so the numbers are reproducible):

| Criterion | Pass rate | Threshold | Gate |
|---|---|---|---|
| answers_question | 100% (7/7) | ≥90% | PASS |
| cites_source | 100% (7/7) | ≥95% | PASS |
| no_wrong_tool | 86% (6/7) | ≥95% | BLOCKER |
| tool_correct | 57% (4/7) | ≥90% | BLOCKER |
| idk_when_no_tool | 67% (2/3) | ≥100% | BLOCKER |
| no_fabrication | 67% (2/3) | ≥100% | BLOCKER |

**Verdict: do not ship.** Four blockers. The failures map cleanly to the
taxonomy:

- **wrong_tool** — the canonical misroute: *"Which model is best for
  assessing compliance with Article 9?"* fired `query_by_model` (keyword
  "model") and `get_eu_ai_act_article` (keyword "article 9") instead of
  `get_best_model_for_article`. The "compare two models" case misroutes the
  same way. These are the keyword-overlap failures a real LLM faces when two
  tools have similar descriptions — documented in `agentic-copilot`'s
  `docs/DECISIONS.md`, and now caught automatically.
- **hallucination** — *"What will the SEC require for AI model governance in
  2031?"* is forward-looking and speculative; no tool has future
  requirements. The agent grounded it in a real but unrelated Colorado
  regulation instead of saying "I don't know." For a compliance agent, one
  invented requirement is the whole ballgame — hence the 100% threshold.

The grounding and answer-presence criteria pass clean. The agent's failure
mode is narrow and specific: **tool selection and the out-of-scope
guardrail.** That is a useful result — it tells the next cycle exactly where
to spend, rather than "make it better."

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
tighten the descriptions so the ranking sticks under a real LLM, and add an
explicit out-of-scope → "I don't know" path that does not call a tool. None
of that is a guess — each item is a blocker the harness named.

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
├── run.py                  # entry point
├── eval_harness/
│   ├── golden_set.py       # 10 hand-labeled cases (routing / grounding / guardrail)
│   ├── criteria.py         # the rubric — deterministic, rule-based
│   ├── taxonomy.py         # failure classes + blast-radius thresholds + ship gate
│   ├── runner.py           # drives /api/chat, fresh thread per case
│   └── report.py           # results.json + SUMMARY.md
└── results/
    ├── results.json
    └── SUMMARY.md
```

## What this is not

Not a benchmark. Not powered to catch regressions in long-tail queries. Not a
substitute for the LLM-as-judge automation in Artifact #2. It is the
pre-ship decision a PM owns — made runnable, with the criteria stated out
loud.