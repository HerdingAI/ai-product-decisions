# LinkedIn practice post — draft (Artifact 02)

_Structure per plan §6: hook → question → numbers sentence → one surprising finding →
link to artifact + curriculum units. Written from RESULTS.md. Draft for Carlos's review;
all numbers are demo-internal and reproducible (D15). Not auto-published._

---

Everyone is wiring up an LLM to grade their AI's outputs at scale. It's the only way to
evaluate a thousand open-ended answers a week without a room full of humans.

But here's the question nobody wants to sit with: **how do you know the judge is right?**

So I measured mine. I hand-labeled a 100-case set, ran an LLM judge over it, and checked
agreement per criterion. On the two criteria where my labels had the most variance, the
judge tracked me reasonably: `usable` 93% agreement (κ=0.56), `complete` 86% (κ=0.49) — good
enough to *screen* answers for human review, not good enough to *gate* releases alone. Cost:
$0.04 for the whole run, ~$0.0005 a case.

The surprising part wasn't a number — it was what one disagreement exposed. On "appropriately
hedged," the judge disagreed with me **61% of the time**, almost always calling an answer
"not hedged" where I'd passed it. So I read the failing answers. None of them was
*overconfident* — the actual meaning of a hedging failure. They were **incomplete**: raw data
dumps, dropped halves of a two-part question, the wrong jurisdiction returned. The judge had
quietly attached its "hedging" label to what were really *completeness* failures. The
criterion wasn't measuring what it claimed to.

That's a broken metric — and I'd never have seen it from the agreement score alone (86% and
93% on the other criteria look fine). It only showed up because I coded *why* the answers
failed, not just *that* they did. The fix isn't to chase agreement by tuning the judge; it's
to re-scope the criterion so "incomplete" and "unhedged" stop bleeding into each other.

Measuring the evaluator didn't just grade the model. It caught a criterion that was lying to
me. The judge you've measured — blind spots named — beats the judge you trusted because it
sounded reasonable.

Full write-up, code, and the failure-pattern analysis: [link to artifact]

Practices Units 06 (the evals game) and 15 (LLM-as-judge) from the Signal / Noise
curriculum: [link]

---

**Reviewer notes for Carlos:**
- "61% disagreement" = 39% agreement on `appropriately-hedged` (RESULTS.md §1/§3); κ=0.04.
- Headline is now the *mis-scoped criterion* (hedging conflated with completeness), confirmed
  by the Artifact 06 open-coding — a cleaner, more defensible finding than "my labels drifted."
- Insert the two links before posting. Keep A4 discipline — no regulated-domain headline.
