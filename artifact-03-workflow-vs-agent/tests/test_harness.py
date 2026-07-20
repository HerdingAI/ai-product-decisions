"""The harness runs a query set through the workflow arm and computes the
arithmetic the artifact turns on: coverage (fraction the fixed rules serve vs.
fall back on), tool-call volume, and latency. No labels needed — this is the
mechanical half of the comparison; quality judging comes later via Artifact 02.
"""
from workflow.harness import run_workflow


def _registry():
    return {
        "get_eu_ai_act_article": lambda a: f"Article {a['article_number']} — adopted",
        "query_by_jurisdiction": lambda a: f"{a['jurisdiction']} — adopted",
    }


def test_reports_per_query_records_and_coverage_summary():
    queries = [
        "What does EU AI Act Article 9 require?",   # routed
        "What does Colorado require of AI developers?",  # routed
        "Write me a poem about compliance.",        # uncovered -> refusal
    ]
    out = run_workflow(queries, _registry())

    assert len(out["records"]) == 3
    # 2 of 3 served by the fixed rules.
    assert out["summary"]["coverage_rate"] == 2 / 3
    assert out["summary"]["refused"] == 1
    assert out["summary"]["n"] == 3


def test_summary_has_latency_and_tool_call_stats():
    out = run_workflow(["What does EU AI Act Article 9 require?"], _registry())
    s = out["summary"]
    assert s["p50_latency_ms"] >= 0.0
    assert s["p95_latency_ms"] >= 0.0
    assert s["mean_tool_calls"] == 1.0
    assert s["total_cost_usd"] == 0.0
