# LinkedIn practice post — draft (Artifact 06)

_Structure per plan §6: hook → question → numbers sentence → one surprising finding →
link to artifact + curriculum units. Written from RESULTS.md. Draft for Carlos's review;
all numbers are demo-internal and reproducible (D15). Not auto-published._

---

A pass rate tells you *that* something is wrong. It never tells you *what to
fix*. That gap is where most eval programs quietly stall — a dashboard number
goes down, and nobody knows which lever to pull.

So the question that matters isn't "what's our pass rate." It's: **when I read
the failures, what categories fall out — and is the criterion itself one of
them?**

I built the flywheel and ran it over failures my earlier artifacts already
produced. It did three things automatically: clustered 83 judged failures into
**4 categories**, collapsed 33 agent crashes into **1** root cause, and — the
one that matters — flagged a **drifted criterion**: "appropriately hedged" had
just **35% agreement** between the judge and the human, and 100% of the
disagreement ran one direction. The other three criteria were fine (86–95%).

Here's the surprising part: a dashboard would have shown "hedging pass rate:
low" and sent someone to fix the *system*. But the system was fine — the
*criterion* had drifted from what anyone actually wanted. The judge was
faithfully applying a rubric the labels no longer matched. The highest-leverage
fix wasn't in the product; it was in the eval. No pass-rate chart surfaces that.
Only reading the failures does.

That's the difference between an eval and a flywheel: an eval gives you a
verdict; a flywheel turns the verdict into a ranked backlog — with "fix your
broken criterion" sitting at the top.

Full harness, the drift detector, and the ranked action list: [link to artifact]

Practices Unit 14 — Error analysis (the Hamel field guide) from the Signal /
Noise curriculum: [link]

---

**Reviewer notes for Carlos:**
- All numbers reproduce via `python report_flywheel.py` over committed files.
- The drift finding is the same one Artifact 02 documents — here it's detected
  mechanically. Post is consistent with that; don't imply a *new* finding.
- The subjective open-coding is still yours to do; the post says the flywheel
  "clustered" (mechanical), which is accurate — don't overclaim qualitative themes.
- Insert the two links before posting. A4 discipline — no regulated-domain headline.
