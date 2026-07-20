"""Execute a fixed tool plan and synthesize a deterministic response.

No LLM anywhere: tools are called in the plan's pinned order, results are
templated into the answer, and an empty plan yields an honest refusal. Tool
calls are recorded with their paired results in the same shape
agentic-copilot emits, so Artifact 02's judge can score the workflow arm and
the agent arm with one rubric.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable

from .router import ToolCall

# A tool registry maps a tool name to a callable taking its args dict and
# returning the tool's result string. Injected so the executor is testable
# without the real MCP servers; the runner binds the real tools.
Registry = dict[str, Callable[[dict], str]]

_REFUSAL = ("I don't have information on that in my sources. "
            "This query falls outside the workflow's fixed set of lookups.")


@dataclass
class WorkflowResult:
    response: str
    tool_calls: list[dict] = field(default_factory=list)
    latency_ms: float = 0.0
    cost_usd: float = 0.0  # zero by construction — no model tokens spent


def execute(plan: list[ToolCall], registry: Registry) -> WorkflowResult:
    start = time.perf_counter()

    if not plan:
        # Fail closed: an uncovered query gets an honest refusal, never a guess.
        return WorkflowResult(response=_REFUSAL, tool_calls=[],
                              latency_ms=(time.perf_counter() - start) * 1000.0)

    tool_calls: list[dict] = []
    for call in plan:
        fn = registry.get(call.tool)
        if fn is None:
            result = f"(no tool '{call.tool}' available)"
        else:
            result = fn(call.args)
        tool_calls.append({"tool": call.tool, "args": dict(call.args),
                           "result": result})

    response = _synthesize(tool_calls)
    return WorkflowResult(response=response, tool_calls=tool_calls,
                          latency_ms=(time.perf_counter() - start) * 1000.0)


def _synthesize(tool_calls: list[dict]) -> str:
    """Template the tool results into an answer — deterministic, no model.
    Boring by design; that predictability is the workflow arm's whole pitch."""
    return "\n\n".join(tc["result"] for tc in tool_calls)
