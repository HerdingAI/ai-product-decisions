"""Deterministic query router — the workflow arm's tool selection.

Contrast with the agent arm: the agent hands the query to an LLM that decides
which tool(s) to call and can loop/recover. This router is a fixed rule set —
one pass, no LLM, no recovery. It is fast and free, and it fails closed (empty
plan) on any query shape the rules don't cover. That coverage gap, measured
against the agent, is the artifact's central arithmetic.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ToolCall:
    tool: str
    args: dict

    def __eq__(self, other):  # dataclass eq, but dict order-insensitive
        return (isinstance(other, ToolCall)
                and self.tool == other.tool and self.args == other.args)

    def __hash__(self):
        return hash((self.tool, tuple(sorted(self.args.items()))))


# Jurisdictions the reg_atlas dataset knows about. A fixed workflow can only
# recognise names it was compiled with — extend this list, and you've changed
# the pinned rules (that's the point: coverage is manual, not learned).
_JURISDICTIONS = (
    "Colorado", "California", "Illinois", "New York", "Texas", "Utah",
    "Connecticut", "Virginia", "Maryland", "Washington", "New Jersey",
    "European Union", "EU", "United Kingdom", "UK", "Federal",
)

_ARTICLE_RE = re.compile(r"\barticle\s+(\d+)\b", re.IGNORECASE)


def route(query: str) -> list[ToolCall]:
    """Map a query to an ordered, fixed tool plan. Empty list = uncovered."""
    q = query.lower()

    # Rule 1 — EU AI Act article lookup (most specific; checked first).
    m = _ARTICLE_RE.search(query)
    if m and ("eu ai act" in q or "ai act" in q or "article" in q and "eu" in q):
        return [ToolCall("get_eu_ai_act_article", {"article_number": m.group(1)})]

    # Rule 2 — model comparison.
    if any(k in q for k in ("compare", " vs ", "versus")) and (
            "model" in q or _mentions_model(query)):
        return [ToolCall("compare_models", {"model_ids": _extract_models(query)})]

    # Rule 3 — best-model-for recommendation.
    if any(k in q for k in ("best model for", "top model for", "recommend model",
                            "which model")):
        m2 = _ARTICLE_RE.search(query)
        cat = f"art{m2.group(1)}" if m2 else ""
        return [ToolCall("get_best_model_for_article", {"article_category_id": cat})]

    # Rule 4 — jurisdiction regulation lookup.
    juris = _extract_jurisdiction(query)
    if juris and any(k in q for k in ("require", "regulation", "regulat", "rule",
                                      "law", "obligation", "comply", "compliance")):
        return [ToolCall("query_by_jurisdiction", {"jurisdiction": juris})]

    # Fail closed: no rule matched. Downstream turns this into an honest refusal.
    return []


def _extract_jurisdiction(query: str) -> str | None:
    for j in _JURISDICTIONS:
        if re.search(rf"\b{re.escape(j)}\b", query, re.IGNORECASE):
            return j
    return None


_KNOWN_MODELS = ("Gemini Pro", "OpenAI o3", "o3", "Kimi K2", "GPT-4o",
                 "Claude", "Gemini", "Llama")


def _mentions_model(query: str) -> bool:
    return any(re.search(rf"\b{re.escape(m)}\b", query, re.IGNORECASE)
               for m in _KNOWN_MODELS)


def _extract_models(query: str) -> str:
    found = [m for m in _KNOWN_MODELS
             if re.search(rf"\b{re.escape(m)}\b", query, re.IGNORECASE)]
    return ",".join(found)
