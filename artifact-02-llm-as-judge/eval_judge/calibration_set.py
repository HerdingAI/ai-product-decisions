"""
Calibration set for the LLM-as-judge study.

These are open-ended queries against `agentic-copilot` — deliberately
different from Artifact 01's golden set, which tests tool-routing
correctness with a mechanical pass/fail. Here the interesting question is
whether the *response text* is a good answer, which is exactly the judgment
a regex can't make and a human/LLM judge is being validated on.

Groups map to the four criteria in RUBRIC.md:
  - grounding   : stresses whether every claim traces to a tool result
  - compound    : multi-part asks where partial coverage is the failure mode
  - hedge       : cases where the tool data is thin/partial and a confident
                  answer would overclaim
  - usability   : cases where a technically-correct answer can still be too
                  vague to act on
Every case is expected to produce a tool call — cases with no tool data to
reason about aren't useful for this judge (that's Artifact 01's guardrail
territory, not this artifact's).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OpenCase:
    id: str
    group: str  # grounding | compound | hedge | usability
    query: str
    note: str = ""


CALIBRATION_SET: list[OpenCase] = [
    # ── grounding ────────────────────────────────────────────────────────
    OpenCase("C-01", "grounding",
             "What does Colorado require for AI model risk management?",
             "Canonical single-jurisdiction lookup — baseline for whether "
             "the response stays inside what query_by_jurisdiction returned."),
    OpenCase("C-02", "grounding",
             "What does the EU AI Act require for risk management under "
             "Article 9?",
             "Article-specific fetch; checks the response doesn't pad the "
             "article text with outside EU AI Act knowledge."),
    OpenCase("C-03", "grounding",
             "Tell me about the NAIC model bulletin and how it compares to "
             "similar state-level guidance.",
             "The 'compares to similar guidance' half invites the model to "
             "generalize past what one framework lookup actually returned."),
    OpenCase("C-04", "grounding",
             "What insurance-sector AI regulations exist, and which ones "
             "are the strictest?",
             "'Strictest' requires a judgment call the sector-query tool "
             "doesn't make for the model — does the response invent a "
             "ranking or stay descriptive?"),
    OpenCase("C-05", "grounding",
             "Which model performs best on Article 9 compliance, and why?",
             "'Why' invites explanation beyond the benchmark's numeric "
             "accuracy field — checks whether the reasoning is grounded in "
             "actual returned fields or invented."),

    # ── compound ─────────────────────────────────────────────────────────
    OpenCase("CQ-01", "compound",
             "What does New York require for AI in credit scoring, and how "
             "does that compare to Colorado's approach?",
             "Two-jurisdiction ask; each needs its own tool call and its "
             "own answer, not just the first one."),
    OpenCase("CQ-02", "compound",
             "Compare GPT-4o and o3 on overall compliance, and tell me "
             "which one I should use for an EU AI Act Article 9 review "
             "specifically.",
             "Compound: overall comparison + article-specific "
             "recommendation. A response that only does the overall "
             "comparison silently drops the second half."),
    OpenCase("CQ-03", "compound",
             "What lending and fintech regulations should I know about, "
             "and are there any AI-specific rules mentioned?",
             "Second clause asks the model to filter/characterize the first "
             "clause's results, not just repeat them."),
    OpenCase("CQ-04", "compound",
             "What does the EU AI Act say about Article 10, and which "
             "models score best on that article in the benchmark?",
             "Two different tools (reg-atlas + benchmark) needed for one "
             "coherent answer."),
    OpenCase("CQ-05", "compound",
             "Summarize AI regulation requirements across Colorado, New "
             "York, and the EU, and flag any that conflict.",
             "Three jurisdictions plus a synthesis ask ('flag conflicts') "
             "that the raw tool data doesn't do for the model."),

    # ── hedge ────────────────────────────────────────────────────────────
    OpenCase("H-01", "hedge",
             "Is Colorado's AI risk-management requirement stricter than "
             "the EU AI Act's?",
             "No single tool call returns a cross-framework strictness "
             "comparison — a good answer hedges or explicitly declines to "
             "rank; a bad one asserts a winner the data doesn't support."),
    OpenCase("H-02", "hedge",
             "Will the EU AI Act's Article 9 requirements likely change in "
             "the next version?",
             "Forward-looking; the tool has no version-history field. "
             "Overclaiming here looks like an authoritative prediction."),
    OpenCase("H-03", "hedge",
             "Based on the benchmark, is GPT-4o compliant enough to use for "
             "real regulatory filings?",
             "'Compliant enough' is a threshold judgment the benchmark's "
             "accuracy number doesn't itself make — checks whether the "
             "response distinguishes 'high score' from 'certified "
             "compliant'."),
    OpenCase("H-04", "hedge",
             "Does New York's AI credit-scoring rule apply to small "
             "lenders, or just large banks?",
             "The tool's summary field may or may not resolve an "
             "applicability-threshold question — good answer says which; "
             "bad answer guesses."),
    OpenCase("H-05", "hedge",
             "How confident are you that Illinois has no AI-specific "
             "insurance law?",
             "Absence claims are the classic overclaim trap — the honest "
             "answer distinguishes 'not in this dataset' from 'does not "
             "exist'."),

    # ── usability ────────────────────────────────────────────────────────
    OpenCase("U-01", "usability",
             "I'm writing a client memo about Colorado AI rules — give me "
             "something I can drop straight into the memo.",
             "Tests whether the response is copy-paste usable (names the "
             "requirement, cites it) vs. a generic restatement of the "
             "question."),
    OpenCase("U-02", "usability",
             "My team needs to pick a model for an Article 9 compliance "
             "tool by Friday — what do you recommend and why in one "
             "paragraph?",
             "Forces a specific, actionable recommendation rather than a "
             "neutral listing of options with no stance."),
    OpenCase("U-03", "usability",
             "What's the one thing I need to know about the NAIC bulletin "
             "before a client call in 10 minutes?",
             "Tests whether the response can prioritize — a correct but "
             "unranked wall of facts fails this criterion even if grounded."),
    OpenCase("U-04", "usability",
             "Give me a two-sentence summary of what New York requires for "
             "AI in credit scoring.",
             "Explicit length constraint — checks whether the response "
             "respects it or pads out a longer answer regardless."),
    OpenCase("U-05", "usability",
             "What should I tell a client who asks 'is this even legal in "
             "the EU'?",
             "Vague framing that a usable response has to translate into a "
             "specific, citable answer rather than restating the vagueness "
             "back."),
]
