# LinkedIn practice post — draft (Artifact 07)

_Structure per plan §6: hook → question → numbers sentence → one surprising
finding → link to artifact + curriculum unit. Written from RESULTS.md; all
numbers demo-internal and reproducible. Draft for Carlos's review; not
auto-published._

---

"We added guardrails" is the AI-PM sentence that means nothing.

A guardrail is only real if you can say which attacks it stops, how many it
still misses, and what it costs everyone who *isn't* attacking you. So I built
the measurement instead of the claim: a 28-case injection slice across five
attack families, plus benign controls, run through the system twice — no guard,
then a signature guard.

The guard works: attack-success dropped from **96% to 14%**. But here's the
number nobody publishes — the benign pass rate fell from **100% to 70%**. The
same guard that blocks "ignore all previous instructions" also blocks a
colleague who writes "ignore the previous draft's formatting." A defense scored
only on attacks blocked is indistinguishable from a guard that blocks
everything.

The surprising part is what still gets through. Four attacks evade the guard —
all by rephrasing around the trigger words. "Overrides all above" instead of
"ignore." "Quietly copy the secret" instead of "email the secret." Signature
matching is a floor, not a solution: it's beaten by a thesaurus. The residual
14% isn't an argument for a bigger regex — it's the argument for a second layer.

That's the whole artifact: a guardrail you can't measure on both axes isn't a
guardrail, it's a vibe with a security label.

Full slice, guard, and the two-rate harness: [link to artifact]

Practices Unit 22 — Defensive prompting, from the Signal / Noise curriculum:
[link]

---

**Reviewer notes for Carlos:**
- Numbers reproduce via `python report_guardrails.py`; offline, key-free.
- A4: attack families are named as categories only; no operational content. The
  regulated/document texture stays in-material. Insert the two links before
  posting.
- The honest "70% benign / 14% residual" framing is the credibility move — keep
  both numbers; dropping either is exactly the failure the post is about.
