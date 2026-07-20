# LinkedIn practice post — draft (Artifact 05)

_Structure per plan §6: hook → question → numbers sentence → one surprising finding →
link to artifact + curriculum units. Written from RESULTS.md. Draft for Carlos's review;
all numbers are demo-internal and reproducible (D15). Not auto-published._

---

Someone in your org has already said it this quarter: "let's use the model at
the top of the leaderboard." It's the most confident wrong answer in AI product
work.

Here's the question the leaderboard can't answer: **best at what, under whose
budget?**

I took a 45-task benchmark across 5 models and made selection a workflow instead
of a glance — cost per task, latency, and hallucination as first-class filters,
accuracy as one axis among four. The raw-accuracy leader (llama-4-maverick,
83.7%) won exactly **1 of 4** realistic budgets. Under a 3-second interactive
SLA it's disqualified — it runs at 7.9 seconds — and the defensible pick flips to
GPT-4o for a 0.8-point accuracy cost. For a cost-first batch job it flips again,
to a model **25× cheaper per task**.

The surprising part was the spread the leaderboard hides. Five models sit within
~5 accuracy points of each other — and across a **25× cost range and a 7×
latency range**. The chart that ranks them shows one of those three numbers.

So "which model should we use?" has no answer until you write down the budget.
Once you do, the selection is mechanical, auditable, and — the part that matters
for a two-year horizon — it re-runs for free when constraints change or a new
model lands. The specific 2026 picks are already going stale. The workflow isn't.

Full rubric, code, and the four worked selections: [link to artifact]

Practices Unit 07 — Defining "good" — from the Signal / Noise curriculum: [link]

---

**Reviewer notes for Carlos:**
- All numbers from RESULTS.md / document-ai-bench results.json; a test
  (`test_real_data.py`) locks the maverick→gpt-4o flip so the post can't drift.
- Latency is the benchmark's measured mean, not a p95 — the post says "runs at
  7.9 seconds," which is fair for relative ordering; keep it directional.
- "25× cheaper" = llama-3.3-70b $0.00005 vs gpt-4o $0.00125 per task. Exact.
- Insert the two links before posting. A4 discipline — no regulated-domain headline.
