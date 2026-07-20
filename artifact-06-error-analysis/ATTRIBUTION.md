# Attribution

**Own work (D1).** All code in this artifact — the criteria-drift detector
(`flywheel/drift.py`), the axial-coding harness (`flywheel/clustering.py`), the
report (`report_flywheel.py`), and the tests — is original work. No forks, no
vendored third-party code, no outbound links to anyone else's repository.

**Inputs are this repo's own prior outputs.** The flywheel runs over failures
already produced and committed by:
- Artifact 02 (`artifact-02-llm-as-judge/results/results.json`) — per-case judge
  verdicts vs. Carlos's human labels.
- Artifact 03 (`artifact-03-workflow-vs-agent/results/agent_arm_baseline_prefix.json`)
  — the baseline agent crashes.
No new data is generated here and no new labels are invented; the drift check and
clustering are objective computations over those committed verdicts.

**Human vs. machine boundary.** The *drift detection* and *mechanical clustering*
are objective and reproducible. The *subjective open-coding* of trace themes —
the qualitative read of why a failure cluster fails — is Carlos's analyst pass;
this artifact builds the reproducible skeleton and counts, not those qualitative
labels. The human labels it consumes are Carlos's own, as sole labeler.

**No models, no keys.** Fully offline and deterministic;
`python report_flywheel.py` regenerates every number from committed files.

**No employer or business-outcome data (D15).** Only reproducible, demo-internal
eval numbers. Nothing reflects any employer's data, systems, or results;
regulated-domain texture stays in-material and never a headline (A4).

**License.** MIT (repo root `LICENSE`).
