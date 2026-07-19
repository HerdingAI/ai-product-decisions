"""
Judge — assembles the prompt from a versioned template, calls the provider,
and parses the response into a binary per-criterion verdict.

Judge prompts are versioned like code (spec §2.3): the prompt text lives in
`judge_prompts/judge_vN.md`, never inline here, so a prompt change is a
diffable, changelogged artifact of its own.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from .calibration_set import OpenCase
from .providers import CompletionResult

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "judge_prompts"

CRITERIA = ("grounded", "complete", "appropriately-hedged", "usable")


class JudgeParseError(ValueError):
    pass


@dataclass
class JudgeVerdict:
    case_id: str
    prompt_version: str
    results: dict[str, bool] = field(default_factory=dict)
    reasons: dict[str, str] = field(default_factory=dict)
    latency_ms: float = 0.0
    cost_usd: float | None = None
    raw_text: str = ""

    @property
    def passed(self) -> bool:
        return all(self.results.get(c, False) for c in CRITERIA)


def load_prompt(version: str) -> str:
    path = PROMPTS_DIR / f"judge_{version}.md"
    if not path.exists():
        raise FileNotFoundError(f"No judge prompt at {path}")
    return path.read_text()


def _format_tool_calls(tool_calls: list[dict]) -> str:
    if not tool_calls:
        return "(no tool was called this turn)"
    lines = []
    for tc in tool_calls:
        lines.append(f"- {tc.get('tool', '?')}({tc.get('args', {})})"
                     f" -> {tc.get('result', tc.get('output', '(no result field)'))}")
    return "\n".join(lines)


def build_user_prompt(case: OpenCase, tool_calls: list[dict], response: str) -> str:
    return (
        f"## Query\n{case.query}\n\n"
        f"## Tool calls this turn\n{_format_tool_calls(tool_calls)}\n\n"
        f"## Assistant response\n{response}\n"
    )


def _strip_fences(text: str) -> str:
    text = text.strip()
    m = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.DOTALL)
    return m.group(1) if m else text


def parse_verdict(case_id: str, prompt_version: str, result: CompletionResult) -> JudgeVerdict:
    raw = _strip_fences(result.text)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise JudgeParseError(f"{case_id}: judge output was not valid JSON: {result.text[:300]}") from e

    missing = [c for c in CRITERIA if c not in data]
    if missing:
        raise JudgeParseError(f"{case_id}: judge output missing criteria {missing}: {data}")

    results = {c: bool(data[c]) for c in CRITERIA}
    reasons = {c: str(data.get(f"{c}_reason", "")) for c in CRITERIA}
    return JudgeVerdict(
        case_id=case_id, prompt_version=prompt_version,
        results=results, reasons=reasons,
        latency_ms=result.latency_ms, cost_usd=result.cost_usd,
        raw_text=result.text,
    )


class Judge:
    def __init__(self, provider, prompt_version: str = "v1"):
        self.provider = provider
        self.prompt_version = prompt_version
        self.system_prompt = load_prompt(prompt_version)

    def judge(self, case: OpenCase, tool_calls: list[dict], response: str) -> JudgeVerdict:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": build_user_prompt(case, tool_calls, response)},
        ]
        result = self.provider.complete(messages, temperature=0.0)
        return parse_verdict(case.id, self.prompt_version, result)
