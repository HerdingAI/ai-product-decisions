"""Axial coding: collapse individual failures into counted categories.

Kept to *mechanical* signatures (which criteria failed, which exception fired)
so the coding is objective and reproducible. Subjective open-coding of trace
themes is the human analyst's pass; this provides the reproducible skeleton it
hangs on and the counts that rank it.
"""
from __future__ import annotations

import re
from collections import OrderedDict


def criterion_failure_signature(case: dict) -> str:
    """The failure pattern of a judged case = the criteria it failed, in order.
    '(none)' when everything passed. This is the axis eval failures cluster on:
    cases that fail the same criteria share a root cause."""
    failed = [k for k, v in case.get("results", {}).items() if v is False]
    return "+".join(failed) if failed else "(none)"


_URL_RE = re.compile(r"for url '[^']*'")
_QUOTED_RE = re.compile(r"'[^']*'")


def exception_signature(err: str) -> str:
    """Normalize an exception string to its stable shape by stripping variable
    parts (URLs, quoted specifics) so identical root causes cluster together."""
    s = _URL_RE.sub("", err).strip()
    # collapse remaining quoted specifics except a leading status-ish token
    s = _QUOTED_RE.sub("'…'", s)
    return re.sub(r"\s+", " ", s).strip()


def cluster_by_signature(items: list[dict], signature_fn, id_key: str = "id") -> dict:
    """Group items by signature_fn(item); return signature -> {count, examples}
    with insertion order preserved for stable reporting."""
    clusters: "OrderedDict[str, dict]" = OrderedDict()
    for it in items:
        sig = signature_fn(it)
        bucket = clusters.setdefault(sig, {"count": 0, "examples": []})
        bucket["count"] += 1
        bucket["examples"].append(it.get(id_key))
    return clusters
