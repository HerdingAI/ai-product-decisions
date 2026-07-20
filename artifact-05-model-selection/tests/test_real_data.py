"""Locks the headline finding against the real document-ai-bench results, so
RESULTS.md can't drift from the data: the raw-accuracy leader is llama-4-
maverick, but under a production latency SLA the defensible pick flips to
gpt-4o. If the benchmark file is absent (spoke not checked out), skip.
"""
import json
from pathlib import Path

import pytest

from selection.core import Budget, leaderboard_leader, load_models, select

RESULTS = (Path(__file__).resolve().parents[3]
           / "document-ai-bench" / "results" / "results.json")


@pytest.mark.skipif(not RESULTS.exists(), reason="document-ai-bench not present")
def test_latency_sla_flips_leaderboard_leader():
    models = load_models(json.loads(RESULTS.read_text()))
    assert leaderboard_leader(models).name == "meta-llama/llama-4-maverick"

    # A 3s p-latency SLA (interactive product) with a real accuracy floor.
    sel = select(models, Budget(max_latency_ms=3000, min_accuracy=0.75),
                 rank_by="accuracy")
    assert sel.winner.name == "openai/gpt-4o"
    assert sel.flipped_from_leaderboard is True
    assert "meta-llama/llama-4-maverick" in sel.rejected
    assert "latency" in sel.rejected["meta-llama/llama-4-maverick"].lower()
