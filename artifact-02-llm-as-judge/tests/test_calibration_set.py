"""Invariants for the calibration set.

Scaling from the original N=20 pilot to N=100 so that per-criterion Cohen's
κ is estimated on a slice large enough to be stable (the N=20 run showed the
κ base-rate paradox: 95% agreement on `grounded` but κ=0 because almost every
case shared the majority label). A bigger, still-balanced set is the fix.
"""
from collections import Counter

from eval_judge.calibration_set import CALIBRATION_SET

GROUPS = {"grounding", "compound", "hedge", "usability"}


def test_calibration_set_has_100_cases():
    assert len(CALIBRATION_SET) == 100


def test_calibration_ids_unique():
    ids = [c.id for c in CALIBRATION_SET]
    assert len(ids) == len(set(ids)), "duplicate case ids"


def test_calibration_balanced_across_groups():
    counts = Counter(c.group for c in CALIBRATION_SET)
    assert set(counts) == GROUPS
    assert all(n == 25 for n in counts.values()), counts


def test_calibration_all_have_nonempty_query_and_valid_group():
    for c in CALIBRATION_SET:
        assert c.query.strip(), f"{c.id} has empty query"
        assert c.group in GROUPS, f"{c.id} has bad group {c.group!r}"
