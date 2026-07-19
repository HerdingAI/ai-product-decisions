import httpx
import pytest

from eval_judge.calibration_set import OpenCase
from eval_judge.runner import RawResult, run_all, run_case

CASE = OpenCase("C-01", "grounding", "What does Colorado require?")


def _mock_transport(handler):
    return httpx.Client(transport=httpx.MockTransport(handler))


def test_run_case_success():
    def handler(request):
        assert request.url.path == "/api/chat"
        body = request.read()
        assert b"What does Colorado require?" in body
        return httpx.Response(200, json={
            "response": "Colorado requires X.",
            "tool_calls": [{"tool": "query_by_jurisdiction"}],
        })

    client = _mock_transport(handler)
    result = run_case(client, "http://127.0.0.1:8011", CASE)
    assert isinstance(result, RawResult)
    assert result.ok is True
    assert result.case_id == "C-01"
    assert result.response == "Colorado requires X."
    assert result.tool_calls == [{"tool": "query_by_jurisdiction"}]
    assert result.latency_ms >= 0


def test_run_case_uses_fresh_thread_id_per_call():
    seen_threads = []

    def handler(request):
        import json
        payload = json.loads(request.read())
        seen_threads.append(payload["thread_id"])
        return httpx.Response(200, json={"response": "ok", "tool_calls": []})

    client = _mock_transport(handler)
    run_case(client, "http://127.0.0.1:8011", CASE)
    run_case(client, "http://127.0.0.1:8011", CASE)
    assert len(set(seen_threads)) == 2


def test_run_case_handles_http_error():
    def handler(request):
        return httpx.Response(500, text="boom")

    client = _mock_transport(handler)
    result = run_case(client, "http://127.0.0.1:8011", CASE)
    assert result.ok is False
    assert result.response == ""
    assert result.error


def test_run_all_rejects_bad_base_url():
    with pytest.raises(ValueError, match="base_url"):
        run_all("not-a-url", [CASE])


def test_run_all_returns_one_result_per_case(monkeypatch):
    calls = []

    def fake_run_case(client, base_url, case, timeout=30.0):
        calls.append(case.id)
        return RawResult(case_id=case.id, ok=True, response="r", tool_calls=[], latency_ms=1.0)

    monkeypatch.setattr("eval_judge.runner.run_case", fake_run_case)
    cases = [CASE, OpenCase("C-02", "grounding", "q2")]
    results = run_all("http://127.0.0.1:8011", cases)
    assert [r.case_id for r in results] == ["C-01", "C-02"]
    assert calls == ["C-01", "C-02"]
