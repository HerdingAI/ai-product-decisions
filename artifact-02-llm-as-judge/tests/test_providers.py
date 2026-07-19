import os

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
