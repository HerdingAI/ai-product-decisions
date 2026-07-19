"""
Runner — drives the system under test.

Each golden case is sent to the agent's /api/chat endpoint with a fresh
thread_id, so cases don't contaminate each other through the agent's
persisted memory. A real eval would also run each case N times to measure
variance; the mock LLM is deterministic (temperature 0), so a single run is
faithful. Against a real LLM, bump --repeat and report the variance.
"""
from __future__ import annotations

import time
import urllib.parse
from dataclasses import dataclass

import httpx

from .golden_set import GoldenCase


@dataclass
class RawResult:
    case_id: str
    ok: bool
    response: str
    tool_calls: list[dict]
    latency_ms: float
    error: str = ""


def _fresh_thread(case_id: str) -> str:
    # Unique per case so memory doesn't leak across cases.
    return f"eval-{case_id}-{int(time.time()*1000)}"


def run_case(client: httpx.Client, base_url: str, case: GoldenCase,
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


def run_all(base_url: str, cases: list[GoldenCase]) -> list[RawResult]:
    # URL-encode nothing here; base_url is a host. Validate reachability first.
    parsed = urllib.parse.urlparse(base_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(f"base_url must be an http(s) URL, got {base_url!r}")
    results: list[RawResult] = []
    with httpx.Client() as client:
        for case in cases:
            results.append(run_case(client, base_url, case))
    return results