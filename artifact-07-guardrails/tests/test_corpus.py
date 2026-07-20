"""Integration check over the real committed corpus: the artifact's headline
story must actually hold on the shipped data, not just on toy fixtures.
"""
from pathlib import Path

from guardrails.attacks import load_cases, ATTACK_TYPES
from guardrails.harness import evaluate

CORPUS = Path(__file__).resolve().parent.parent / "data" / "injection_cases.json"


def test_corpus_is_within_spec_size_and_covers_all_types():
    cases = load_cases(CORPUS)
    assert 25 <= len(cases) <= 40  # spec §4: 25-40 adversarial cases (+ benign controls)
    attack_types = {c.attack_type for c in cases if not c.is_benign}
    assert set(ATTACK_TYPES) == attack_types  # every attack family represented
    assert any(c.is_benign for c in cases)  # benign controls present


def test_defense_lowers_attack_success_and_costs_some_benign():
    cases = load_cases(CORPUS)
    base = evaluate(cases, defended=False)
    deft = evaluate(cases, defended=True)
    # The defense must actually reduce attack success...
    assert deft["attack_success_rate"] < base["attack_success_rate"]
    # ...and it is honest about a residual (some attacks still evade the signatures).
    assert deft["attack_success_rate"] > 0.0
    # ...and it is honest about a benign cost (lookalikes get over-blocked).
    assert deft["benign_pass_rate"] < base["benign_pass_rate"]
