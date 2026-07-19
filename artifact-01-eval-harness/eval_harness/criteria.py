"""
Criteria — the rubric a PM uses to decide an agent is good enough to ship.

Criteria are deterministic and rule-based on purpose. This artifact answers
"how do I decide it's shippable," not "how do I automate judgment" — that is
Artifact #2 (LLM-as-judge, validated). Mixing the two would muddle the
decision being demonstrated.

Each criterion is a function: (case, response, tool_calls) -> CriterionResult.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable

from .golden_set import GoldenCase


# The mock's "I don't know" fallback phrasing. A real deployment would
# canonicalize this from the system prompt; keyed here so the harness stays
# honest about what it is measuring.
_IDK_PATTERNS = [
    r"i don'?t have (?:enough )?information",
    r"i don'?t have (?:anything |any )?on that",
    r"i'?m not able to (?:help|answer)",
    r"no (?:relevant )?(?:tool|information) (?:has|available)",
    r"i can'?t (?:find|provide)",
]

# Source-grounding proxy: the agent's tool-backed answers consistently carry
# one of these — a jurisdiction tag, a status/effective line, or a numeric
# metric. Their presence is a reasonable deterministic stand-in for "the
# answer is grounded in tool output, not invented."
_GROUNDING_PATTERNS = [
    r"\((?:Colorado|EU|Federal|California|New York|Maryland|Virginia|"
    r"Connecticut|Pennsylvania|Louisiana|Wisconsin|Florida|Texas|Illinois|"
    r"New Jersey|Ohio|Rhode Island|Iowa|Vermont)\)",
    r"Status:\s",
    r"Effective:\s",
    r"Accuracy:\s*0\.\d+",
    r"Article \d+",
    r"Source:?",
]


@dataclass
class CriterionResult:
    name: str
    passed: bool
    reason: str = ""


@dataclass
class CaseVerdict:
    case_id: str
    query: str
    group: str
    tool_calls: list[dict] = field(default_factory=list)
    response: str = ""
    results: list[CriterionResult] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)  # taxonomy tags

    @property
    def passed(self) -> bool:
        return all(r.passed for r in self.results)


def _tools_called(tool_calls: list[dict]) -> set[str]:
    return {tc.get("tool", "") for tc in tool_calls if tc.get("tool")}


def _is_idk(response: str) -> bool:
    low = response.lower()
    return any(re.search(p, low) for p in _IDK_PATTERNS)


def _is_grounded(response: str) -> bool:
    return any(re.search(p, response, re.IGNORECASE) for p in _GROUNDING_PATTERNS)


# ── individual criteria ────────────────────────────────────────────────────

def crit_tool_correct(case: GoldenCase, response: str, tool_calls: list[dict]) -> CriterionResult:
    if not case.expected_tools:
        return CriterionResult("tool_correct", True, "no tools expected")
    called = _tools_called(tool_calls)
    missing = [t for t in case.expected_tools if t not in called]
    if missing:
        return CriterionResult(
            "tool_correct", False,
            f"expected {case.expected_tools}, called {sorted(called)}; "
            f"missing {missing}",
        )
    return CriterionResult("tool_correct", True, f"called {sorted(called)}")


def crit_no_wrong_tool(case: GoldenCase, response: str, tool_calls: list[dict]) -> CriterionResult:
    called = _tools_called(tool_calls)
    wrong = sorted(called & set(case.must_not_tools))
    if wrong:
        return CriterionResult(
            "no_wrong_tool", False,
            f"called a forbidden tool: {wrong}",
        )
    return CriterionResult("no_wrong_tool", True, "no forbidden tools called")


def crit_answers_question(case: GoldenCase, response: str, tool_calls: list[dict]) -> CriterionResult:
    # Only applies when a tool was expected to answer.
    if not case.expected_tools:
        return CriterionResult("answers_question", True, "n/a (no tool expected)")
    if not response.strip():
        return CriterionResult("answers_question", False, "empty response")
    if _is_idk(response):
        return CriterionResult(
            "answers_question", False,
            "returned the IDK fallback when a tool could have answered",
        )
    return CriterionResult("answers_question", True, "non-empty, non-IDK answer")


def crit_cites_source(case: GoldenCase, response: str, tool_calls: list[dict]) -> CriterionResult:
    # Only applies when a tool was expected to answer.
    if not case.expected_tools:
        return CriterionResult("cites_source", True, "n/a (no tool expected)")
    if _is_grounded(response):
        return CriterionResult("cites_source", True, "response carries a source grounding marker")
    return CriterionResult(
        "cites_source", False,
        "no grounding marker in a tool-backed answer",
    )


def crit_idk_when_no_tool(case: GoldenCase, response: str, tool_calls: list[dict]) -> CriterionResult:
    # Only applies when NO tool was expected.
    if case.expected_tools:
        return CriterionResult("idk_when_no_tool", True, "n/a (tool expected)")
    if _is_idk(response):
        return CriterionResult("idk_when_no_tool", True, "said 'I don't know'")
    return CriterionResult(
        "idk_when_no_tool", False,
        "did not fall back to 'I don't know' on an out-of-scope query",
    )


def crit_no_fabrication(case: GoldenCase, response: str, tool_calls: list[dict]) -> CriterionResult:
    # Out-of-scope query that nonetheless called a tool = fabrication risk.
    if case.expected_tools:
        return CriterionResult("no_fabrication", True, "n/a (tool expected)")
    called = _tools_called(tool_calls)
    if called:
        return CriterionResult(
            "no_fabrication", False,
            f"called {sorted(called)} on an out-of-scope query — "
            f"likely fabricated grounding",
        )
    return CriterionResult("no_fabrication", True, "no tool called on out-of-scope query")


CRITERIA: dict[str, Callable[[GoldenCase, str, list[dict]], CriterionResult]] = {
    "tool_correct": crit_tool_correct,
    "no_wrong_tool": crit_no_wrong_tool,
    "answers_question": crit_answers_question,
    "cites_source": crit_cites_source,
    "idk_when_no_tool": crit_idk_when_no_tool,
    "no_fabrication": crit_no_fabrication,
}


def evaluate(case: GoldenCase, response: str, tool_calls: list[dict]) -> CaseVerdict:
    verdict = CaseVerdict(
        case_id=case.id, query=case.query, group=case.group,
        tool_calls=tool_calls, response=response,
    )
    for cid in case.criteria:
        verdict.results.append(CRITERIA[cid](case, response, tool_calls))
    return verdict