"""The workflow arm routes queries to tools with fixed, deterministic rules —
no LLM, no loop. Its whole point (and its measurable weakness vs. the agent)
is that routing is a pinned rule set: fast and free, but it returns an empty
plan on any query shape the rules don't cover. These tests pin that contract.
"""
from workflow.router import route, ToolCall


def test_routes_eu_ai_act_article_query_and_extracts_number():
    plan = route("What does EU AI Act Article 9 require for risk management?")
    assert plan == [ToolCall("get_eu_ai_act_article", {"article_number": "9"})]


def test_routes_jurisdiction_lookup():
    plan = route("What does Colorado require of AI developers?")
    assert ToolCall("query_by_jurisdiction", {"jurisdiction": "Colorado"}) in plan


def test_routes_model_comparison_to_compare_models():
    plan = route("Compare Gemini Pro and OpenAI o3 for compliance work.")
    assert plan[0].tool == "compare_models"


def test_unroutable_query_returns_empty_plan():
    # The coverage gap that is the artifact's central finding: a fixed rule set
    # cannot serve a query shape it was never built for. It must fail closed
    # (empty plan → honest refusal downstream), not guess.
    plan = route("Draft me a haiku about quarterly earnings.")
    assert plan == []


def test_routing_is_deterministic():
    q = "What does EU AI Act Article 9 require?"
    assert route(q) == route(q)
