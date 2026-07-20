import json
import os

import httpx
import pytest

from eval_judge.providers import FakeProvider, OpenRouterProvider, ProviderError


def test_openrouter_provider_requires_api_key(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ProviderError, match="OPENROUTER_API_KEY"):
        OpenRouterProvider(model="anthropic/claude-3-haiku")


def test_openrouter_provider_accepts_explicit_key(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    p = OpenRouterProvider(model="anthropic/claude-3-haiku", api_key="sk-test")
    assert p.api_key == "sk-test"


def test_openrouter_provider_reads_env_key(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-env")
    p = OpenRouterProvider(model="anthropic/claude-3-haiku")
    assert p.api_key == "sk-env"


def test_fake_provider_records_calls_and_returns_default():
    p = FakeProvider()
    result = p.complete([{"role": "user", "content": "hello"}])
    assert result.text
    assert len(p.calls) == 1
    assert p.calls[0][0]["content"] == "hello"


def test_fake_provider_scripted_response():
    p = FakeProvider(script={"trigger": '{"ok": true}'})
    result = p.complete([{"role": "user", "content": "trigger"}])
    assert result.text == '{"ok": true}'


def test_fake_provider_unscripted_falls_back_to_default():
    p = FakeProvider(script={"trigger": '{"ok": true}'}, default='{"ok": false}')
    result = p.complete([{"role": "user", "content": "something else"}])
    assert result.text == '{"ok": false}'


class _FakeResponse:
    def __init__(self, status_code, body, headers=None):
        self.status_code = status_code
        self._body = body
        self.text = json.dumps(body)
        self.headers = headers or {}

    def json(self):
        return self._body


_OK_BODY = {
    "choices": [{"message": {"content": '{"grounded": true}'}}],
    "usage": {"cost": 0.0, "prompt_tokens": 10, "completion_tokens": 5},
}


def test_openrouter_provider_retries_on_429_then_succeeds(monkeypatch):
    responses = [
        _FakeResponse(429, {"error": {"message": "rate limited",
                                       "metadata": {"retry_after_seconds": 3}}}),
        _FakeResponse(200, _OK_BODY),
    ]
    sleeps: list[float] = []

    def fake_post(self, url, headers=None, json=None):
        return responses.pop(0)

    monkeypatch.setattr(httpx.Client, "post", fake_post)
    p = OpenRouterProvider(model="fake/model", api_key="sk-test",
                            sleep_fn=sleeps.append)
    result = p.complete([{"role": "user", "content": "hi"}])
    assert result.text == '{"grounded": true}'
    assert sleeps == [3]


def test_openrouter_provider_gives_up_after_max_retries(monkeypatch):
    body = {"error": {"message": "rate limited",
                       "metadata": {"retry_after_seconds": 1}}}

    def fake_post(self, url, headers=None, json=None):
        return _FakeResponse(429, body)

    monkeypatch.setattr(httpx.Client, "post", fake_post)
    sleeps: list[float] = []
    p = OpenRouterProvider(model="fake/model", api_key="sk-test",
                            max_retries=2, sleep_fn=sleeps.append)
    with pytest.raises(ProviderError, match="429"):
        p.complete([{"role": "user", "content": "hi"}])
    assert len(sleeps) == 2  # retried twice, then raised on the 3rd failure


def test_openrouter_provider_includes_reasoning_effort_in_payload(monkeypatch):
    captured: dict = {}

    def fake_post(self, url, headers=None, json=None):
        captured.update(json)
        return _FakeResponse(200, _OK_BODY)

    monkeypatch.setattr(httpx.Client, "post", fake_post)
    p = OpenRouterProvider(model="deepseek/deepseek-v4-flash", api_key="sk-test",
                            reasoning_effort="high")
    p.complete([{"role": "user", "content": "hi"}])
    assert captured["reasoning"] == {"effort": "high"}


def test_openrouter_provider_omits_reasoning_when_not_set(monkeypatch):
    captured: dict = {}

    def fake_post(self, url, headers=None, json=None):
        captured.update(json)
        return _FakeResponse(200, _OK_BODY)

    monkeypatch.setattr(httpx.Client, "post", fake_post)
    p = OpenRouterProvider(model="fake/model", api_key="sk-test")
    p.complete([{"role": "user", "content": "hi"}])
    assert "reasoning" not in captured


def test_openrouter_provider_does_not_retry_non_429_errors(monkeypatch):
    def fake_post(self, url, headers=None, json=None):
        return _FakeResponse(500, {"error": {"message": "server error"}})

    monkeypatch.setattr(httpx.Client, "post", fake_post)
    sleeps: list[float] = []
    p = OpenRouterProvider(model="fake/model", api_key="sk-test",
                            sleep_fn=sleeps.append)
    with pytest.raises(ProviderError, match="500"):
        p.complete([{"role": "user", "content": "hi"}])
    assert sleeps == []
