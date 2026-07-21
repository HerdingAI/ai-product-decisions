"""For the coverage comparison to be fair, the workflow arm must re-implement
the *full* agentic-copilot task set — every tool the agent can route to — not
a toy subset. These pin the remaining tool categories (mirroring the agent's
routing map) with the precedence a fixed rule set needs to disambiguate them.
"""
from workflow.router import route


def _tool(query):
    plan = route(query)
    return plan[0].tool if plan else None


def test_list_queries_beat_single_lookups():
    # "which states" is a list intent, not a single-jurisdiction lookup.
    assert _tool("Which states have AI regulations?") == "list_all_jurisdictions"
    assert _tool("What models are available in the benchmark?") == "list_all_models"
    assert _tool("List all task categories.") == "list_all_articles"


def test_sector_lookup():
    assert _tool("What are the AI rules for the insurance sector?") == "query_by_sector"


def test_named_framework_lookup():
    assert _tool("What does the NAIC model bulletin cover?") == "query_by_framework"


def test_model_performance_lookup():
    assert _tool("How does GPT-4o perform on the benchmark?") == "query_by_model"


def test_task_category_lookup():
    assert _tool("Which model is best at hallucination resistance?") in (
        "query_by_article", "get_best_model_for_article")


def test_still_fails_closed_on_uncovered():
    assert route("Tell me a joke.") == []


def test_task_category_lookup_uses_real_tool_arg_name():
    # regfin_bench.query_by_article(article_category_id: str) — the router
    # must emit the same kwarg name, or a real registry raises TypeError.
    plan = route("Which model is best at hallucination resistance?")
    if plan[0].tool == "query_by_article":
        assert "article_category_id" in plan[0].args
