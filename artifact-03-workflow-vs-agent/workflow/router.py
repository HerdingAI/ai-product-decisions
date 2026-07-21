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


_TASK_CATEGORY_TERMS = ("hallucination resistance", "reasoning chain",
                        "multi-jurisdiction", "category performance",
                        "task category", "task type")
_FRAMEWORK_TERMS = ("naic", "ecoa", "sr 11", "model risk", "circular letter",
                    "sb 24", "sb 26", "digital omnibus", "annex iii",
                    "model bulletin")
_SECTORS = ("insurance", "lending", "fintech", "credit scoring", "banking")


def route(query: str) -> list[ToolCall]:
    """Map a query to an ordered, fixed tool plan — mirroring the full
    agentic-copilot task set so the coverage comparison is fair. Rules run
    most-specific first; empty list = uncovered (fails closed)."""
    q = query.lower()

    # 1 — list intents (must beat single-item lookups that share keywords).
    if any(k in q for k in ("which states", "what states", "list states",
                            "list all jurisdiction", "all jurisdictions")):
        return [ToolCall("list_all_jurisdictions", {})]
    if any(k in q for k in ("what models", "list models", "all models",
                            "available models")):
        return [ToolCall("list_all_models", {})]
    if any(k in q for k in ("what categories", "list categories",
                            "all categories", "task categories")):
        return [ToolCall("list_all_articles", {})]

    # 2 — EU AI Act article lookup.
    m = _ARTICLE_RE.search(query)
    if m and ("eu ai act" in q or "ai act" in q or ("article" in q and "eu" in q)):
        return [ToolCall("get_eu_ai_act_article", {"article_number": m.group(1)})]

    # 3 — model comparison.
    if any(k in q for k in ("compare", " vs ", "versus")) and (
            "model" in q or _mentions_model(query)):
        return [ToolCall("compare_models", {"model_ids": _extract_models(query)})]

    # 4 — best-model-for recommendation (explicit phrasing only).
    if any(k in q for k in ("best model for", "top model for", "recommend model",
                            "recommend a model")):
        m2 = _ARTICLE_RE.search(query)
        return [ToolCall("get_best_model_for_article",
                         {"article_category_id": f"art{m2.group(1)}" if m2 else ""})]

    # 5 — benchmark task-category lookup.
    if any(t in q for t in _TASK_CATEGORY_TERMS):
        return [ToolCall("query_by_article", {"article_category_id": _first_hit(q, _TASK_CATEGORY_TERMS)})]

    # 6 — named regulatory framework (beats model/jurisdiction: shares keywords).
    if any(t in q for t in _FRAMEWORK_TERMS):
        return [ToolCall("query_by_framework", {"framework_name": _first_hit(q, _FRAMEWORK_TERMS)})]

    # 7 — sector lookup.
    if "sector" in q and any(s in q for s in _SECTORS):
        return [ToolCall("query_by_sector", {"sector": _first_hit(q, _SECTORS)})]

    # 8 — single model performance lookup.
    if _mentions_model(query) and any(k in q for k in ("perform", "score",
                                      "benchmark", "accuracy", "how does", "how good")):
        return [ToolCall("query_by_model", {"model_id": _extract_models(query)})]

    # 9 — jurisdiction regulation lookup.
    juris = _extract_jurisdiction(query)
    if juris and any(k in q for k in ("require", "regulation", "regulat", "rule",
                                      "law", "obligation", "comply", "compliance")):
        return [ToolCall("query_by_jurisdiction", {"jurisdiction": juris})]

    # Fail closed: no rule matched. Downstream turns this into an honest refusal.
    return []


def _first_hit(q: str, terms) -> str:
    for t in terms:
        if t in q:
            return t
    return ""


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
