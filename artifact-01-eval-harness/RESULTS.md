# Results — Eval harness ship decision

**System under test:** `HerdingAI/agentic-copilot` (deterministic mock LLM,
temperature 0 — the numbers below are exactly reproducible).
**Golden set:** 32 hand-labeled cases (24 autonomous tier, 8 reviewed tier),
12 of them adversarial.
**Scoring:** deterministic, rule-based criteria (no LLM judge in this artifact
by design — see the README's "one deliberate boundary"). Judge-based scoring is
[Artifact 02](../artifact-02-llm-as-judge/). Because the SUT runs on a mock LLM,
inference cost is **$0** and latency is not a meaningful axis here; both become
first-class once a real backend is swapped in.

## Verdict: DO NOT SHIP — on both tiers

The blast-radius lens is applied to the *same* failures rather than averaging
them away. Even the softer reviewed-tier bar fails.

### Autonomous tier (24 cases — answers could flow into unreviewed action)

| Criterion | Pass rate | Threshold | Gate |
|---|---|---|---|
| answers_question | 92% (12/13) | ≥90% | PASS |
| cites_source | 77% (10/13) | ≥95% | issue (next cycle) |
| no_wrong_tool | 92% (12/13) | ≥95% | BLOCKER |
| tool_correct | 62% (8/13) | ≥90% | BLOCKER |
| idk_when_no_tool | 45% (5/11) | ≥100% | BLOCKER |
| no_fabrication | 45% (5/11) | ≥100% | BLOCKER |

### Reviewed tier (8 cases — a human reads the answer before it is acted on)

| Criterion | Pass rate | Threshold | Gate |
|---|---|---|---|
| answers_question | 100% (6/6) | ≥60% | PASS |
| cites_source | 100% (3/3) | ≥60% | PASS |
| no_wrong_tool | 100% (5/5) | ≥80% | PASS |
| tool_correct | 100% (6/6) | ≥60% | PASS |
| idk_when_no_tool | 0% (0/1) | ≥80% | BLOCKER |
| no_fabrication | 50% (1/2) | ≥80% | BLOCKER |

## The finding: the fallback path hallucinates by design

The largest result the 32-case set surfaced is a **grounded hallucination on
the no-rule-matched fallback**. When no keyword rule fires cleanly, the mock
still calls `query_by_jurisdiction` and grounds its answer in a Colorado
insurance regulation — real-looking fields, entirely unrelated to what was
asked. It fired on **five separate adversarial cases** (a weather query, a
flight-booking request, a fictional "Wakanda" jurisdiction, garbled noise, and
the single word "regulations"). A 10-case set saw this once and it looked like
an edge case; at 32 cases with a one-third-adversarial floor, it is a pattern —
the fallback *itself* is the failure surface. For a compliance-adjacent agent,
one invented requirement is the whole ballgame, which is why `no_fabrication`
and `idk_when_no_tool` carry a 100% autonomous-tier bar.

That is the argument for the one-third-adversarial requirement: canonical
happy-path cases never trigger "no rule matched," so they never exercise the
path that actually fails.

## Numbers sentence (spec §2.6, adapted for a deterministic ship-decision)

> On a 32-case golden set the agent **fails the ship gate on both tiers**:
> autonomous-tier `no_fabrication` and `idk_when_no_tool` at 45% (bar: 100%),
> `tool_correct` at 62% (bar: 90%). Scoring is deterministic rule-based (no
> judge); on the mock backend cost is $0/query. The prescribed remediation —
> reorder tool-selection rules and route unmatched queries to "I don't know" —
> is named per-blocker by the taxonomy.

## Scope boundary (honest)

The ADoD "one improvement iteration with re-run and delta" is **prescribed, not
executed** here: this artifact ships the *decision machinery* (harness, criteria,
taxonomy, blast-radius gate) and a per-blocker remediation list, not a patched
agent. The remediation itself belongs to the SUT (`agentic-copilot`) — a related
reliability fix on that repo is applied and measured in
[Artifact 03](../artifact-03-workflow-vs-agent/). The specific pass rates
describe the mock's heuristics and will move the moment a real LLM is swapped in;
the decision process and failure vocabulary do not.

## Reproduce

```bash
# 1. Start the SUT (in the agentic-copilot repo): backend on :8000
# 2. In this artifact:
python run.py --target http://127.0.0.1:8000
# → results/results.json + results/SUMMARY.md, and a ship verdict on stdout
```

The committed `results/` are from a real run against the mock LLM; point
`--target` at a real backend to regenerate against any model.
