"""Axial coding = collapse individual failures into a small set of categories
with counts, so "read the failures" becomes a ranked backlog instead of an
unbounded scroll. When the signature is mechanical (which criteria failed, which
exception fired), the coding is objective and reproducible. Pinned here.
"""
from flywheel.clustering import (
    cluster_by_signature,
    criterion_failure_signature,
    exception_signature,
)


def test_criterion_failure_signature_lists_failed_criteria():
    case = {"results": {"grounded": True, "complete": False,
                        "appropriately-hedged": False, "usable": True}}
    assert criterion_failure_signature(case) == "complete+appropriately-hedged"


def test_criterion_failure_signature_none_when_all_pass():
    case = {"results": {"grounded": True, "usable": True}}
    assert criterion_failure_signature(case) == "(none)"


def test_exception_signature_normalizes_variable_parts():
    e1 = "HTTPStatusError: Server error '500 Internal Server Error' for url 'http://x/a'"
    e2 = "HTTPStatusError: Server error '500 Internal Server Error' for url 'http://y/b'"
    assert exception_signature(e1) == exception_signature(e2)
    assert "HTTPStatusError" in exception_signature(e1)


def test_cluster_by_signature_counts_and_keeps_examples():
    items = [
        {"id": "a", "sig": "x"}, {"id": "b", "sig": "x"}, {"id": "c", "sig": "y"},
    ]
    clusters = cluster_by_signature(items, lambda it: it["sig"], id_key="id")
    assert clusters["x"]["count"] == 2
    assert clusters["x"]["examples"] == ["a", "b"]
    assert clusters["y"]["count"] == 1
