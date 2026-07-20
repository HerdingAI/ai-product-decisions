# LinkedIn practice post — draft (Artifact 01)

_Structure per plan §6: hook → question → numbers sentence → one surprising
finding → link to artifact + curriculum units. Written from RESULTS.md; all
numbers are demo-internal and reproducible. Draft for Carlos's review; not
auto-published._

---

Every agent demo works. That's the problem.

You type the question the demo was built around, it calls the right tool, it
answers with a citation, everyone nods. But the question a PM actually has to
answer is the opposite of the demo: **is this good enough to put in front of
users — and how would I know?** "I tried it a few times and it seemed fine" is
not a ship decision.

So I built the decision instead of the demo: a 32-case golden set, criteria
written down *before* the run, every failure mapped to a named class, and two
threshold tiers — a strict bar for answers that flow into unreviewed action, a
softer one for answers a human reads first. The verdict isn't "92% accurate."
It's **DO NOT SHIP**, with the blockers named.

Here's the surprising part. The failure that mattered most only showed up
because one-third of the cases were adversarial. When no rule matched cleanly,
the agent didn't stop — it fell back to grounding its answer in an unrelated
regulation, with real-looking fields, on a *weather question*. It did this on
five separate cases a happy-path test set would never trigger. At 10 cases it
looked like a fluke; at 32 it's a pattern: the fallback path itself hallucinates
by design. For a compliance-adjacent agent, one invented requirement is the
whole ballgame — which is exactly why "say I don't know" carries a 100% bar.

The harness ships; the agent doesn't. The specific pass rates will move the
moment you swap in a real model — but the decision process, and the failure
vocabulary, don't.

Full harness, criteria, and the ship gate: [link to artifact]

Practices Unit 13 (Capstone) and Unit 14 (Error analysis) from the Signal /
Noise curriculum: [link]

---

**Reviewer notes for Carlos:**
- Numbers reproduce via `python run.py --target <backend>` over the committed
  golden set; the mock backend makes them exact and key-free.
- A4: the regulated texture stays in-material (a failure example), never the
  headline. Insert the two links before posting.
- The "harness ships, agent doesn't" framing is the honest scope line — keep it;
  it's the credibility move, not a hedge.
