# Eval harness — results summary

**System under test:** `HerdingAI/agentic-copilot` (mock LLM, temperature 0)  
**Target:** `http://127.0.0.1:8011`  
**Cases:** 10

## Ship decision

```
Verdict: DO NOT SHIP
Blockers:
  - idk_when_no_tool: 67% (2/3) vs ≥100% [FAIL]
  - no_fabrication: 67% (2/3) vs ≥100% [FAIL]
  - no_wrong_tool: 86% (6/7) vs ≥95% [FAIL]
  - tool_correct: 57% (4/7) vs ≥90% [FAIL]
```

## Metrics vs. blast-radius thresholds

| Criterion | Pass rate | Threshold | Gate |
|---|---|---|---|
| answers_question | 100% (7/7) | ≥90% | PASS |
| cites_source | 100% (7/7) | ≥95% | PASS |
| idk_when_no_tool | 67% (2/3) | ≥100% | BLOCKER |
| no_fabrication | 67% (2/3) | ≥100% | BLOCKER |
| no_wrong_tool | 86% (6/7) | ≥95% | BLOCKER |
| tool_correct | 57% (4/7) | ≥90% | BLOCKER |

## Failures by class (taxonomy)

### R-03 — wrong_tool
- **Query:** Which model is best for assessing compliance with Article 9?
- **Tools called:** ['get_eu_ai_act_article', 'query_by_model']
- **tool_correct:** expected ['get_best_model_for_article'], called ['get_eu_ai_act_article', 'query_by_model']; missing ['get_best_model_for_article']
- **no_wrong_tool:** called a forbidden tool: ['query_by_model']
- **Response excerpt:** _**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implem…_

### R-04 — wrong_tool
- **Query:** Compare GPT-4o and o3 on overall compliance assessment.
- **Tools called:** ['query_by_article', 'query_by_model']
- **tool_correct:** expected ['compare_models'], called ['query_by_article', 'query_by_model']; missing ['compare_models']
- **Response excerpt:** _**Gemini Pro (Google)** — Accuracy: 0.917 | Hallucination rate: 1.223

**OpenAI o3** — Accuracy: 0.9 | Hallucination rate: 1.0

**Kimi K2 (M…_

### R-05 — wrong_tool
- **Query:** What insurance-sector regulations exist?
- **Tools called:** ['query_by_jurisdiction']
- **tool_correct:** expected ['query_by_sector'], called ['query_by_jurisdiction']; missing ['query_by_sector']
- **Response excerpt:** _**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
C…_

### G-03 — hallucination
- **Query:** What will the SEC require for AI model governance in 2031?
- **Tools called:** ['query_by_jurisdiction', 'query_by_model']
- **idk_when_no_tool:** did not fall back to 'I don't know' on an out-of-scope query
- **no_fabrication:** called ['query_by_jurisdiction', 'query_by_model'] on an out-of-scope query — likely fabricated grounding
- **Response excerpt:** _**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
C…_

## What this is, and what it isn't

These numbers are real, produced by running the harness against a live `agentic-copilot` backend using its deterministic mock LLM. They describe **the mock LLM's tool-selection heuristics**, not a production model. The point of the artifact is the harness and the decision criteria — the ship gate, the failure taxonomy, the blast-radius thresholds — not the specific pass rates, which move the moment a real LLM is swapped in. Regenerate with `python run.py --target http://127.0.0.1:8011`.
