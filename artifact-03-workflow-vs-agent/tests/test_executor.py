"""The executor runs a fixed plan against injected tools, collects results, and
synthesizes a deterministic (template, no-LLM) response. On an empty plan it
must refuse honestly rather than fabricate. Its tool_calls output mirrors
agentic-copilot's transparency records so Artifact 02's judge can score both
arms identically.
"""
from workflow.router import ToolCall
from workflow.executor import execute, WorkflowResult


def _registry():
    return {
        "get_eu_ai_act_article": lambda args: f"Article {args['article_number']} — Status: adopted",
        "query_by_jurisdiction": lambda args: f"{args['jurisdiction']} (CO) — adopted",
    }


def test_executes_plan_and_records_tool_calls_with_results():
    plan = [ToolCall("get_eu_ai_act_article", {"article_number": "9"})]
    res = execute(plan, _registry())
    assert isinstance(res, WorkflowResult)
    assert len(res.tool_calls) == 1
    tc = res.tool_calls[0]
    assert tc["tool"] == "get_eu_ai_act_article"
    assert tc["args"] == {"article_number": "9"}
    assert "adopted" in tc["result"]          # paired result present (for the judge)
    assert "Article 9" in res.response         # result surfaced in the answer


def test_empty_plan_refuses_without_calling_tools():
    res = execute([], _registry())
    assert res.tool_calls == []
    assert "don't have" in res.response.lower() or "cannot" in res.response.lower()


def test_records_latency_and_zero_model_cost():
    # The workflow arm spends no model tokens on routing — cost is zero by
    # construction, which is half the arithmetic vs. the agent.
    res = execute([ToolCall("query_by_jurisdiction", {"jurisdiction": "Colorado"})],
                  _registry())
    assert res.cost_usd == 0.0
    assert res.latency_ms >= 0.0
