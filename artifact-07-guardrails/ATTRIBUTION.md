# Attribution

**Own work (D1).** All code in this artifact — the attack taxonomy and loader
(`guardrails/attacks.py`), the baseline/defended guard (`guardrails/guard.py`),
the two-rate harness (`guardrails/harness.py`), the report
(`report_guardrails.py`), and the tests — is original work. No forks, no
vendored third-party code, no model or network calls, no outbound links to
anyone else's repository.

**Data.** The 28 attack cases and 10 benign controls
(`data/injection_cases.json`) are **self-authored**. The attack payloads are
generic, widely-documented prompt-injection patterns (fake role turns, control
tokens, "ignore previous instructions," system-prompt and data exfiltration,
off-policy requests); they are not drawn from, and do not reproduce, any
proprietary employer red-team corpus. Case labels (attack type, benign/attack)
are the author's own — and are **objective**: whether the guard blocked a case
is a mechanical fact, so no subjective human-labeling pass is required to score
this artifact.

**Off-policy phrasing.** The off-policy cases name harmful *categories* (phishing,
malware, laundering) only as short refusal-trigger strings to test the guard;
they contain no operational content.

**No models, no keys.** The guard is deterministic pattern matching; the whole
artifact is offline. `python report_guardrails.py` regenerates every number with
no API key.

**No employer or business-outcome data (D15).** Only reproducible, demo-internal
eval numbers. The regulated/document texture is difficulty, kept in-material,
never a headline (A4). Nothing reflects any employer's data, systems, or results.

**License.** MIT (repo root `LICENSE`).
