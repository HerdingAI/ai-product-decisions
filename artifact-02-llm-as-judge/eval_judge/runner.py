"""
Runner — drives the system under test (agentic-copilot) for the
open-ended calibration set. Mirrors artifact-01's runner.py pattern:
each case gets a fresh thread_id so cases don't contaminate each other
through the agent's persisted conversation memory.
"""
from __future__ import annotations

import time
import urllib.parse
import uuid
from dataclasses import dataclass

import httpx

from .calibration_set import OpenCase


@dataclass
class RawResult:
    case_id: str
    ok: bool
    response: str
    tool_calls: list[dict]
    latency_ms: float
    error: str = ""


def _fresh_thread(case_id: str) -> str:
    return f"judge-{case_id}-{uuid.uuid4().hex[:8]}"


def run_case(client: httpx.Client, base_url: str, case: OpenCase,
             timeout: float = 30.0) -> RawResult:
    url = base_url.rstrip("/") + "/api/chat"
    payload = {"message": case.query, "thread_id": _fresh_thread(case.id)}
    t0 = time.perf_counter()
    try:
        r = client.post(url, json=payload, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        return RawResult(
            case_id=case.id,
            ok=True,
            response=data.get("response", ""),
            tool_calls=data.get("tool_calls", []),
            latency_ms=(time.perf_counter() - t0) * 1000,
        )
    except Exception as e:  # network / HTTP / parse errors
        return RawResult(
            case_id=case.id, ok=False, response="", tool_calls=[],
            latency_ms=(time.perf_counter() - t0) * 1000,
            error=f"{type(e).__name__}: {e}",
        )


def run_all(base_url: str, cases: list[OpenCase], pace_seconds: float = 0.0) -> list[RawResult]:
    parsed = urllib.parse.urlparse(base_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(f"base_url must be an http(s) URL, got {base_url!r}")
    results: list[RawResult] = []
    with httpx.Client() as client:
        for i, case in enumerate(cases):
            if i and pace_seconds:
                time.sleep(pace_seconds)
            results.append(run_case(client, base_url, case))
    return results
