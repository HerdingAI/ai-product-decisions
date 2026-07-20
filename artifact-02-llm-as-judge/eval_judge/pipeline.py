"""Drive the judge over a list of collected response records, tolerating
per-case failures.

A calibration pass over ~100 cases with bias probes is hundreds of paid
model calls; a single unparseable verdict (e.g. a reasoning model that
truncates its JSON) must not abort the whole run. `evaluate` records such
failures and continues, so the run still produces agreement numbers over
every case that *did* parse.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from .bias_probes import run_all_probes
from .calibration_set import OpenCase
from .judge import Judge, JudgeParseError, JudgeVerdict
from .providers import ProviderError

# Errors that should down-grade a single case to a recorded failure rather
# than crashing the whole pass.
_RECOVERABLE = (JudgeParseError, ProviderError)


def _eval_one(judge: Judge, rec: dict, run_probes: bool) -> dict:
    """Judge one record (and optionally probe it). Never raises for a
    recoverable model/parse error — reports it in `failures` instead.
    Returns a dict of partial results to be merged in input order."""
    out = {"verdict": None, "probes": [], "human_label": None, "failures": []}
    case = OpenCase(id=rec["id"], group=rec["group"],
                    query=rec["query"], note=rec.get("note", ""))
    try:
        out["verdict"] = judge.judge(case, rec["tool_calls"], rec["response"])
    except _RECOVERABLE as e:
        out["failures"].append((rec["id"], str(e)))
        return out

    # `human_labels` may be absent, None (unlabeled record), or a partial
    # dict; keep only concrete True/False labels for the agreement stats.
    labeled = {k: v for k, v in (rec.get("human_labels") or {}).items()
               if v is not None}
    if labeled:
        out["human_label"] = (rec["id"], labeled)

    if run_probes:
        try:
            out["probes"] = run_all_probes(judge, case, rec["tool_calls"], rec["response"])
        except _RECOVERABLE as e:
            out["failures"].append((f"{rec['id']} (probe)", str(e)))
    return out


def evaluate(judge: Judge, records: list[dict], run_probes: bool = True,
             max_workers: int = 1):
    """Judge each ok record; optionally run bias probes.

    With `max_workers > 1`, cases are judged concurrently (each case is
    independent) — necessary because a reasoning judge can take tens of
    seconds per call, making a sequential ~100-case × probes pass hours long.
    Results are merged in input order regardless of completion order.

    Returns (verdicts, probes, human_labels, failures) where `failures` is a
    list of (case_id, error_message) for cases that raised.
    """
    ok_records = [r for r in records if r.get("ok")]

    if max_workers <= 1:
        outs = [_eval_one(judge, r, run_probes) for r in ok_records]
    else:
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            # ex.map preserves input order in its result iterator.
            outs = list(ex.map(lambda r: _eval_one(judge, r, run_probes), ok_records))

    verdicts: list[JudgeVerdict] = []
    probes: list = []
    human_labels: dict[str, dict[str, bool]] = {}
    failures: list[tuple[str, str]] = []
    for out in outs:
        if out["verdict"] is not None:
            verdicts.append(out["verdict"])
        probes.extend(out["probes"])
        if out["human_label"] is not None:
            cid, labeled = out["human_label"]
            human_labels[cid] = labeled
        failures.extend(out["failures"])

    return verdicts, probes, human_labels, failures
