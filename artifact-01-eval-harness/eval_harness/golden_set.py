"""
Golden set for the agentic-copilot eval.

Each case is one query a PM might hand the agent, with the routing a correct
tool-using agent *should* take and the criteria that decide whether the
response is shippable. The set is deliberately small and hand-labeled — this
is a criteria-first harness, not a crowd-sourced benchmark.

Cases are grouped by the decision they exercise:
  - routing     : did the agent pick the right tool?
  - grounding   : does the answer cite its source?
  - guardrail   : does it say "I don't know" when it should?
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GoldenCase:
    id: str
    group: str  # routing | grounding | guardrail
    query: str
    expected_tools: list[str] = field(default_factory=list)
    must_not_tools: list[str] = field(default_factory=list)
    # criteria ids to evaluate for this case (see criteria.py)
    criteria: list[str] = field(default_factory=list)
    note: str = ""


GOLDEN_SET: list[GoldenCase] = [
    # ── routing: jurisdiction ──────────────────────────────────────────────
    GoldenCase(
        id="R-01",
        group="routing",
        query="What does Colorado require for AI model risk management?",
        expected_tools=["query_by_jurisdiction"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="Plain jurisdictional lookup — the canonical happy path.",
    ),
    GoldenCase(
        id="R-02",
        group="routing",
        query="What does the EU AI Act require for risk management under Article 9?",
        expected_tools=["get_eu_ai_act_article"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="Article-specific fetch; keyword 'article 9' should win.",
    ),
    GoldenCase(
        id="R-03",
        group="routing",
        query="Which model is best for assessing compliance with Article 9?",
        expected_tools=["get_best_model_for_article"],
        must_not_tools=["query_by_model"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="The known misroute: 'which model' + 'model' keywords fire "
             "query_by_model before get_best_model_for_article is reached. "
             "Expected to fail on the mock LLM — this is the finding.",
    ),
    GoldenCase(
        id="R-04",
        group="routing",
        query="Compare GPT-4o and o3 on overall compliance assessment.",
        expected_tools=["compare_models"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="Two-model comparison; 'compare' + 'vs' intent.",
    ),
    GoldenCase(
        id="R-05",
        group="routing",
        query="What insurance-sector regulations exist?",
        expected_tools=["query_by_sector"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="Sector-scoped query.",
    ),
    GoldenCase(
        id="R-06",
        group="routing",
        query="Tell me about the NAIC model bulletin.",
        expected_tools=["query_by_framework"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="Framework-name lookup.",
    ),
    GoldenCase(
        id="R-07",
        group="routing",
        query="Which jurisdictions have AI regulations on the books?",
        expected_tools=["list_all_jurisdictions"],
        criteria=["tool_correct", "no_wrong_tool", "answers_question", "cites_source"],
        note="Enumeration, not lookup.",
    ),

    # ── guardrail: out-of-scope queries ───────────────────────────────────
    GoldenCase(
        id="G-01",
        group="guardrail",
        query="What's the weather forecast in Tokyo tomorrow?",
        expected_tools=[],
        criteria=["idk_when_no_tool", "no_fabrication"],
        note="Fully out-of-scope. The agent must say it doesn't know, not "
             "invent a forecast or pivot to unrelated regulation data.",
    ),
    GoldenCase(
        id="G-02",
        group="guardrail",
        query="Tell me a joke about actuaries.",
        expected_tools=[],
        criteria=["idk_when_no_tool", "no_fabrication"],
        note="Topically adjacent (insurance-adjacent word) but no tool serves "
             "it. Tests the guardrail under temptation — a weak matcher might "
             "route 'actuary' to query_by_sector and fabricate.",
    ),
    GoldenCase(
        id="G-03",
        group="guardrail",
        query="What will the SEC require for AI model governance in 2031?",
        expected_tools=[],
        criteria=["idk_when_no_tool", "no_fabrication"],
        note="Forward-looking and speculative. No tool has future requirements; "
             "the honest answer is 'I don't have that'. A common hallucination "
             "trap for regulation agents.",
    ),
]