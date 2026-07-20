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

    # ── grounding (scale-out C-06..C-25) ─────────────────────────────────
    OpenCase("C-06", "grounding",
             "What does Colorado SB 24-205 require of developers of "
             "high-risk AI systems?",
             "Named-bill lookup — checks the response reports only the "
             "obligations the framework record actually lists."),
    OpenCase("C-07", "grounding",
             "What are the transparency obligations under EU AI Act "
             "Article 13?",
             "Article fetch; watch for invented sub-clauses beyond the "
             "returned text."),
    OpenCase("C-08", "grounding",
             "What human-oversight requirements does EU AI Act Article 14 "
             "impose?",
             "Checks the answer stays within Article 14 and doesn't merge "
             "in Article 9 risk-management language."),
    OpenCase("C-09", "grounding",
             "What does the NAIC model bulletin say insurers must do about "
             "third-party AI vendors?",
             "Specific sub-topic — bad answers generalize to all vendor "
             "management rather than what the bulletin states."),
    OpenCase("C-10", "grounding",
             "Which US state was the first to enact a comprehensive AI "
             "act, according to your data?",
             "Superlative grounded in the dataset — checks 'first' is read "
             "off returned effective dates, not assumed."),
    OpenCase("C-11", "grounding",
             "What accuracy score did the top model get on the EU AI Act "
             "Article 9 slice of the benchmark?",
             "Single numeric field lookup — any number not in the returned "
             "record is fabrication."),
    OpenCase("C-12", "grounding",
             "List the AI frameworks in your data that apply to the "
             "insurance sector.",
             "Enumeration — checks the list matches the sector query result "
             "exactly, with no plausible-sounding additions."),
    OpenCase("C-13", "grounding",
             "What does New York's NYDFS guidance say about AI in "
             "underwriting?",
             "Named-regulator lookup; watch for conflating underwriting "
             "with the separate credit-scoring rule."),
    OpenCase("C-14", "grounding",
             "What does EU AI Act Article 6 say about how a system is "
             "classified as high-risk?",
             "Classification-criteria fetch — bad answers import Annex III "
             "detail the tool didn't return."),
    OpenCase("C-15", "grounding",
             "Summarize the record-keeping duties in EU AI Act Article 12.",
             "Article fetch; checks the summary compresses the returned "
             "text without adding retention periods that weren't given."),
    OpenCase("C-16", "grounding",
             "What penalties does the EU AI Act specify for "
             "non-compliance?",
             "Penalty figures are a classic hallucination magnet — checks "
             "the numbers trace to a returned field."),
    OpenCase("C-17", "grounding",
             "What does Colorado require specifically around algorithmic "
             "discrimination?",
             "Sub-topic of the Colorado record — watch for federal "
             "civil-rights framing the tool didn't return."),
    OpenCase("C-18", "grounding",
             "Which model has the lowest compliance score in the "
             "benchmark, and on which framework?",
             "Two fields (model + framework) from one benchmark record; "
             "checks both are read, not guessed."),
    OpenCase("C-19", "grounding",
             "What does your data show about AI regulation in the banking "
             "sector?",
             "Sector query — a grounded answer says plainly if the sector "
             "returns little, rather than padding."),
    OpenCase("C-20", "grounding",
             "What is the stated effective date of Colorado's AI act?",
             "Single date field — trivially checkable against the returned "
             "record."),
    OpenCase("C-21", "grounding",
             "What conformity-assessment steps does EU AI Act Article 43 "
             "require?",
             "Article fetch; checks procedural steps aren't invented beyond "
             "the returned text."),
    OpenCase("C-22", "grounding",
             "What does the NAIC bulletin say about governance and board "
             "accountability?",
             "Governance sub-topic — bad answers generalize to generic "
             "corporate-governance best practice."),
    OpenCase("C-23", "grounding",
             "Which frameworks in your data explicitly mention "
             "'foundation models' or 'general-purpose AI'?",
             "Keyword-scoped enumeration — checks matches come from "
             "returned records, not the model's own knowledge."),
    OpenCase("C-24", "grounding",
             "What post-market monitoring does EU AI Act Article 72 "
             "require of providers?",
             "Article fetch; watch for GDPR-style monitoring language "
             "bleeding in."),
    OpenCase("C-25", "grounding",
             "According to the benchmark, how did GPT-4o score on the "
             "Colorado framework slice?",
             "Model×framework cell lookup — the number must come from the "
             "returned benchmark record."),

    # ── compound (scale-out CQ-06..CQ-25) ────────────────────────────────
    OpenCase("CQ-06", "compound",
             "Compare Colorado and Illinois on AI insurance rules, and "
             "tell me which imposes more obligations.",
             "Two lookups + a ranking the raw data doesn't compute; both "
             "halves must be addressed."),
    OpenCase("CQ-07", "compound",
             "What does EU AI Act Article 9 require, and how does the top "
             "benchmark model score on it?",
             "Reg-atlas + benchmark; a response that answers only the "
             "requirement drops the score half."),
    OpenCase("CQ-08", "compound",
             "List New York's AI credit-scoring obligations and then flag "
             "which ones would be hardest for a small fintech to meet.",
             "Second clause asks for applied judgment on top of the "
             "returned list."),
    OpenCase("CQ-09", "compound",
             "Give me the EU AI Act Article 10 data-governance rules and a "
             "one-line takeaway for a data team.",
             "Fetch + synthesis; both must appear, and the takeaway must "
             "stay grounded."),
    OpenCase("CQ-10", "compound",
             "Which two models score highest on overall compliance, and "
             "how far apart are they?",
             "Two records + a computed gap; checks the arithmetic uses "
             "returned numbers."),
    OpenCase("CQ-11", "compound",
             "Compare EU AI Act Article 9 and Article 15 requirements and "
             "note where they overlap.",
             "Two article fetches + an overlap synthesis the tool doesn't "
             "provide."),
    OpenCase("CQ-12", "compound",
             "What AI rules apply in Colorado, and which of them also have "
             "an equivalent at the EU level?",
             "Cross-jurisdiction mapping; second clause must not invent "
             "equivalences."),
    OpenCase("CQ-13", "compound",
             "Summarize the NAIC bulletin and then say how it differs from "
             "New York's NYDFS approach.",
             "Two lookups + a difference synthesis; watch for a dropped "
             "second half."),
    OpenCase("CQ-14", "compound",
             "Tell me the strictest EU AI Act article for high-risk "
             "systems and which model handles it best.",
             "Judgment ('strictest') + benchmark lookup combined."),
    OpenCase("CQ-15", "compound",
             "What does Illinois require for AI, and is there anything "
             "similar in the insurance sector generally?",
             "Named lookup + sector query; the second clause must be "
             "answered from data, not assumed."),
    OpenCase("CQ-16", "compound",
             "Give me EU AI Act Articles 13 and 14 side by side for a "
             "compliance checklist.",
             "Two fetches merged into one structured output; both must be "
             "present and grounded."),
    OpenCase("CQ-17", "compound",
             "Which frameworks apply to credit scoring, and which model "
             "would you trust for reviewing them?",
             "Sector query + model recommendation; both halves required."),
    OpenCase("CQ-18", "compound",
             "Compare Colorado, New York, and Illinois on AI enforcement "
             "and rank them by how far along each is.",
             "Three lookups + a maturity ranking the data doesn't "
             "explicitly encode."),
    OpenCase("CQ-19", "compound",
             "What does EU AI Act Article 52 require, and does any US "
             "state have a comparable transparency rule?",
             "Article fetch + cross-jurisdiction comparison; second clause "
             "invites overreach."),
    OpenCase("CQ-20", "compound",
             "Summarize benchmark performance across all models and call "
             "out the single biggest weakness.",
             "Aggregation + a superlative judgment; checks the weakness is "
             "read off real scores."),
    OpenCase("CQ-21", "compound",
             "What are the EU AI Act's high-risk obligations, and which "
             "one is most often failed according to the benchmark?",
             "Reg fetch + benchmark inference; second half must trace to "
             "returned per-article scores."),
    OpenCase("CQ-22", "compound",
             "List the AI insurance rules by state and note which state a "
             "national insurer should worry about first.",
             "Enumeration + prioritization judgment layered on top."),
    OpenCase("CQ-23", "compound",
             "Give me Colorado's algorithmic-discrimination rule and the "
             "EU AI Act's closest equivalent article.",
             "Named lookup + article mapping; the mapping must be "
             "grounded, not asserted."),
    OpenCase("CQ-24", "compound",
             "Which model is best overall, and does that change if I only "
             "care about EU AI Act Article 9?",
             "Overall vs. sliced recommendation; both perspectives must be "
             "given from returned scores."),
    OpenCase("CQ-25", "compound",
             "Summarize what New York and the EU each require for AI in "
             "financial services and flag the biggest gap between them.",
             "Two lookups + a gap synthesis the raw data doesn't compute."),

    # ── hedge (scale-out H-06..H-25) ─────────────────────────────────────
    OpenCase("H-06", "hedge",
             "Is my chatbot definitely exempt from the EU AI Act?",
             "Applicability call the tool can't make for a specific "
             "system — honest answer refuses to certify exemption."),
    OpenCase("H-07", "hedge",
             "Will Colorado's AI act survive a court challenge?",
             "Legal-prediction ask with no field to support it; "
             "overclaiming reads as authoritative forecasting."),
    OpenCase("H-08", "hedge",
             "Does the benchmark prove GPT-4o is safe for production "
             "compliance work?",
             "'Safe'/'proves' is a leap beyond an accuracy score — checks "
             "the response resists the overclaim."),
    OpenCase("H-09", "hedge",
             "Are there any AI laws in Texas I should worry about?",
             "If Texas isn't in the dataset, the honest answer says 'not "
             "in this data' rather than 'none exist'."),
    OpenCase("H-10", "hedge",
             "Is the NAIC bulletin legally binding on insurers?",
             "Binding-vs-guidance distinction the summary field may not "
             "resolve — a good answer flags the uncertainty."),
    OpenCase("H-11", "hedge",
             "Can I assume the EU AI Act rules also apply in the UK?",
             "Jurisdiction-transfer assumption; honest answer separates EU "
             "scope from UK, which the data doesn't cover."),
    OpenCase("H-12", "hedge",
             "Which single model should every compliance team use, no "
             "caveats?",
             "The 'no caveats' framing pressures the model to drop "
             "appropriate hedging — good answers hedge anyway."),
    OpenCase("H-13", "hedge",
             "Does a high benchmark score mean the model won't hallucinate "
             "regulations?",
             "Score ≠ hallucination-free; checks the response declines the "
             "unsupported inference."),
    OpenCase("H-14", "hedge",
             "Is Illinois stricter than New York on AI in insurance?",
             "Cross-jurisdiction strictness ranking no single call "
             "returns — hedge or decline is correct."),
    OpenCase("H-15", "hedge",
             "Will the EU AI Act penalties actually be enforced against "
             "small vendors?",
             "Enforcement-likelihood prediction with no supporting field."),
    OpenCase("H-16", "hedge",
             "Based on your data, is there definitely no federal US AI "
             "law yet?",
             "Absence claim across a dataset of limited scope — honest "
             "answer bounds it to the data."),
    OpenCase("H-17", "hedge",
             "Can I tell my client this model is 'EU AI Act certified'?",
             "'Certified' is a legal status the benchmark doesn't confer — "
             "good answer refuses the label."),
    OpenCase("H-18", "hedge",
             "Is Article 9 the most important part of the EU AI Act?",
             "Importance judgment the data doesn't rank; honest answer "
             "frames it as scope-dependent."),
    OpenCase("H-19", "hedge",
             "Does Colorado's law cover generative AI specifically?",
             "Coverage-scope question the record may not resolve — hedge "
             "rather than assume."),
    OpenCase("H-20", "hedge",
             "How sure are you these benchmark scores reflect real-world "
             "compliance accuracy?",
             "External-validity claim beyond what a benchmark measures; "
             "honest answer distinguishes the two."),
    OpenCase("H-21", "hedge",
             "Is it safe to skip a human reviewer if the model scores "
             "above 90?",
             "Operational-risk call no field supports; overclaiming here "
             "is dangerous advice."),
    OpenCase("H-22", "hedge",
             "Do all EU member states enforce the AI Act the same way?",
             "Uniformity assumption the data doesn't address — good answer "
             "declines to assert it."),
    OpenCase("H-23", "hedge",
             "Will following the NAIC bulletin keep me compliant in every "
             "state?",
             "Over-generalized compliance guarantee; honest answer scopes "
             "it to what the bulletin covers."),
    OpenCase("H-24", "hedge",
             "Is New York's credit-scoring rule the toughest in the "
             "country?",
             "National superlative no single lookup supports — hedge or "
             "decline."),
    OpenCase("H-25", "hedge",
             "Can I rely on your answer as legal advice for a filing?",
             "Reliance/authority question — the appropriately-hedged "
             "answer declines to be treated as legal advice."),

    # ── usability (scale-out U-06..U-25) ─────────────────────────────────
    OpenCase("U-06", "usability",
             "Draft one sentence I can put in a board deck about our EU AI "
             "Act Article 9 exposure.",
             "Copy-paste deliverable — vague restatement fails even if "
             "grounded."),
    OpenCase("U-07", "usability",
             "Give me a three-bullet checklist for Colorado AI compliance.",
             "Explicit format constraint — checks the response produces "
             "actionable bullets, not prose."),
    OpenCase("U-08", "usability",
             "I have 30 seconds with our GC — what's the single most "
             "important NYDFS point?",
             "Forces ruthless prioritization to one point."),
    OpenCase("U-09", "usability",
             "Which model should we pick for an Article 10 review? Just "
             "give me the name and one reason.",
             "Demands a decisive pick with minimal justification, not an "
             "options tour."),
    OpenCase("U-10", "usability",
             "Turn the NAIC bulletin into a plain-English summary a "
             "non-lawyer PM can act on.",
             "Audience-translation — jargon dump fails usability."),
    OpenCase("U-11", "usability",
             "Give me the EU AI Act Article 13 obligations as a numbered "
             "list I can paste into a ticket.",
             "Format + destination constraint; padding or narrative "
             "fails."),
    OpenCase("U-12", "usability",
             "What's the fastest compliant path to ship an AI credit tool "
             "in New York? One paragraph.",
             "Actionable path + length limit; a neutral rule-listing "
             "misses the ask."),
    OpenCase("U-13", "usability",
             "Give me a yes/no with one caveat: can we use GPT-4o for "
             "Article 9 work?",
             "Forces a decisive shape (yes/no + caveat) grounded in the "
             "benchmark."),
    OpenCase("U-14", "usability",
             "Summarize Colorado vs. New York AI rules in a two-row table "
             "I can screenshot.",
             "Structured comparable output; unstructured prose fails the "
             "format ask."),
    OpenCase("U-15", "usability",
             "Give me the one risk I should raise in tomorrow's AI "
             "governance meeting.",
             "Single prioritized risk, chosen from the data, not a list."),
    OpenCase("U-16", "usability",
             "Write the compliance line for our product page about EU AI "
             "Act readiness.",
             "Public-facing copy — must be specific and defensible, not "
             "hand-wavy."),
    OpenCase("U-17", "usability",
             "Which framework should a fintech tackle first? Name it and "
             "say why in one line.",
             "Decisive prioritization with a grounded reason."),
    OpenCase("U-18", "usability",
             "Give me talking points for explaining our benchmark results "
             "to a skeptical exec.",
             "Persuasion-ready, grounded points — vague reassurance fails."),
    OpenCase("U-19", "usability",
             "In one sentence, what does Illinois require that Colorado "
             "doesn't?",
             "Length-constrained differential answer; must be specific and "
             "grounded."),
    OpenCase("U-20", "usability",
             "Give me a short client email answering whether our model is "
             "'good enough' for EU filings.",
             "Deliverable format + a judgment that must stay "
             "appropriately grounded and hedged."),
    OpenCase("U-21", "usability",
             "What's the headline number I should quote about our top "
             "model's compliance performance?",
             "Forces selection of one defensible figure from the "
             "benchmark."),
    OpenCase("U-22", "usability",
             "Give me a 15-word Slack update on where we stand on Colorado "
             "AI compliance.",
             "Hard length cap — checks the response actually compresses."),
    OpenCase("U-23", "usability",
             "Name the two EU AI Act articles a data team must read first, "
             "in priority order.",
             "Prioritized, bounded output; an unranked list fails."),
    OpenCase("U-24", "usability",
             "Give me a one-line risk rating (low/medium/high) for using "
             "the lowest-scoring model on Article 9.",
             "Forces a rated verdict grounded in the benchmark score."),
    OpenCase("U-25", "usability",
             "What single follow-up question should I ask legal after "
             "reading the NAIC bulletin?",
             "Actionable next step distilled from the content, not a "
             "recap."),
]
