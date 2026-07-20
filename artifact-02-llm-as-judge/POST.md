# LinkedIn practice post — draft (Artifact 02)

_Structure per plan §6: hook → question → numbers sentence → one surprising finding →
link to artifact + curriculum units. Written from RESULTS.md. Draft for Carlos's review;
all numbers are demo-internal and reproducible (D15). Not auto-published._

---

Everyone is wiring up an LLM to grade their AI's outputs at scale. It's the only way to
evaluate a thousand open-ended answers a week without a room full of humans.

But here's the question nobody wants to sit with: **how do you know the judge is right?**

So I measured mine. I hand-labeled a 100-case set, ran an LLM judge over it, and checked
agreement per criterion. On the two criteria where my labels had real variance, the judge
tracked me reasonably: `usable` 93% agreement (κ=0.38), `complete` 86% (κ=0.29) — good
enough to *screen* answers for review, not good enough to *gate* releases alone. Cost:
$0.04 for the whole run, ~$0.0005 a case.

The surprising part wasn't a number — it was what the disagreement exposed. On
"appropriately hedged," the judge disagreed with me on 65% of cases. My first instinct was
"the judge is too strict." Then I checked its calls against my own written rubric — and the
judge was following the rubric. **My labels weren't.** I'd been quietly more lenient than
the standard I wrote down before labeling started.

The eval didn't just validate the model. It caught *me*. That's the whole point of
measuring the evaluator instead of trusting it: the judge you've measured — blind spots
published — beats the judge you trusted because it sounded reasonable.

Full write-up, code, and the failure-pattern analysis (including the κ=0 trap that hides
in any criterion where your labels don't vary): [link to artifact]

Practices Units 06 (the evals game) and 15 (LLM-as-judge) from the Signal / Noise
curriculum: [link]

---

**Reviewer notes for Carlos:**
- "65% disagreement" = 35% agreement on `appropriately-hedged` (RESULTS.md §1/§3).
- The rubric-vs-labels finding is the honest headline; it reflects well (you built the
  discipline that caught it) but double-check you're comfortable stating it publicly.
- Insert the two links before posting. Keep A4 discipline — no regulated-domain headline.
