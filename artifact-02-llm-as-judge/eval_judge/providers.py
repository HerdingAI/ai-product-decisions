"""
Providers — thin chat-completion adapter for the judge model.

D6 (repo spec): OpenRouter is the provider standard — one key, many models,
uniform cost/latency reporting. This is the *judge's* model call; it is
separate from `agentic-copilot`'s own LLM, which is the system under test
and is called via `runner.py`, not this module.

No first-party key is ever read from anywhere but the environment, and none
is committed to this repo (D11/D15 discipline carried over from the demo
spec, applied here too: a judge that could silently bill someone else's key
would be a defect, not a feature).
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Callable, Protocol

import httpx

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class ProviderError(RuntimeError):
    pass


@dataclass
class CompletionResult:
    text: str
    latency_ms: float
    cost_usd: float | None
    model: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None


class Provider(Protocol):
    model: str

    def complete(self, messages: list[dict], *, temperature: float = 0.0,
                 max_tokens: int = 1024) -> CompletionResult: ...


class OpenRouterProvider:
    """Calls a model via OpenRouter. Requires OPENROUTER_API_KEY in the env."""

    def __init__(self, model: str, api_key: str | None = None, timeout: float = 60.0,
                 max_retries: int = 5, sleep_fn: Callable[[float], None] = time.sleep,
                 reasoning_effort: str | None = None):
        self.model = model
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
        self.timeout = timeout
        self.max_retries = max_retries
        self._sleep = sleep_fn
        # OpenRouter's unified reasoning control: "low" | "medium" | "high".
        # None omits the field entirely (non-reasoning models / default behavior).
        self.reasoning_effort = reasoning_effort
        if not self.api_key:
            raise ProviderError(
                "OPENROUTER_API_KEY is not set. Get a key at "
                "https://openrouter.ai/keys and export it before running "
                "the judge: export OPENROUTER_API_KEY=... "
                "(no key is ever committed to this repo)."
            )

    @staticmethod
    def _retry_delay(response: httpx.Response, attempt: int) -> float:
        """Prefer the server's own Retry-After signal (header or OpenRouter's
        JSON `error.metadata.retry_after_seconds`); fall back to exponential
        backoff only when the server didn't tell us how long to wait."""
        header = response.headers.get("Retry-After")
        if header is not None:
            try:
                return float(header)
            except ValueError:
                pass
        try:
            meta = response.json().get("error", {}).get("metadata", {})
            if "retry_after_seconds" in meta:
                return float(meta["retry_after_seconds"])
        except Exception:
            pass
        return float(2 ** attempt)

    def complete(self, messages: list[dict], *, temperature: float = 0.0,
                 max_tokens: int = 1024) -> CompletionResult:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "usage": {"include": True},
        }
        if self.reasoning_effort is not None:
            payload["reasoning"] = {"effort": self.reasoning_effort}
        t0 = time.perf_counter()
        r = None
        for attempt in range(self.max_retries + 1):
            with httpx.Client(timeout=self.timeout) as client:
                r = client.post(OPENROUTER_URL, headers=headers, json=payload)
            if r.status_code == 429 and attempt < self.max_retries:
                self._sleep(self._retry_delay(r, attempt))
                continue
            break
        latency_ms = (time.perf_counter() - t0) * 1000
        if r.status_code != 200:
            raise ProviderError(f"OpenRouter {r.status_code}: {r.text[:400]}")
        data = r.json()
        try:
            text = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            raise ProviderError(f"Unexpected OpenRouter response shape: {data}") from e
        usage = data.get("usage") or {}
        return CompletionResult(
            text=text,
            latency_ms=latency_ms,
            cost_usd=usage.get("cost"),
            model=self.model,
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
        )


class FakeProvider:
    """Deterministic stub for tests — no network calls.

    `script` maps the exact user-message content to a canned response text;
    anything unmatched gets `default`. Every call is recorded for assertion.
    """

    def __init__(self, script: dict[str, str] | None = None, default: str | None = None,
                 model: str = "fake/stub"):
        self.script = script or {}
        self.default = default or (
            '{"grounded": true, "grounded_reason": "stub", '
            '"complete": true, "complete_reason": "stub", '
            '"appropriately-hedged": true, "appropriately-hedged_reason": "stub", '
            '"usable": true, "usable_reason": "stub"}'
        )
        self.calls: list[list[dict]] = []
        self.max_tokens_seen: list[int] = []
        self.model = model

    def complete(self, messages: list[dict], *, temperature: float = 0.0,
                 max_tokens: int = 1024) -> CompletionResult:
        self.calls.append(messages)
        self.max_tokens_seen.append(max_tokens)
        key = messages[-1]["content"] if messages else ""
        text = self.script.get(key, self.default)
        return CompletionResult(text=text, latency_ms=0.1, cost_usd=0.0, model=self.model)
