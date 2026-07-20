# LLM-as-judge — calibration results

**Target:** `deepseek/deepseek-v4-flash`  
**Cases judged:** 85

## Judge-vs-human agreement

| Criterion | n | Agreement | Cohen's κ |
|---|---|---|---|
| grounded | 85 | 95% | 0.00 |
| complete | 85 | 86% | 0.29 |
| appropriately-hedged | 85 | 35% | 0.00 |
| usable | 85 | 93% | 0.38 |

## Disagreements (judge vs. human)

Raw rows below; see `RESULTS.md` for the coded failure-pattern analysis (verbosity bias, position bias, criterion misreading, etc. — spec §4 Artifact #2 acceptance criteria).

| Case | Criterion | Judge | Human | Judge's reason |
|---|---|---|---|---|
| C-01 | complete | False | True | The response fails to directly answer the query about Colorado's requirements; it includes many irrelevant entries from other states' NAIC adoptions without focusing on Colorado, leaving the user to extract the relevant information. |
| C-01 | appropriately-hedged | False | True | The response presents non-Colorado entries (e.g., California, Maryland, etc.) without any indication that they are not Colorado's requirements, which could mislead the user into thinking they apply to Colorado. |
| C-01 | usable | False | True | A professional would need to ask a follow-up question to clarify which entries are actually Colorado's requirements, as the response is a raw dump of all tool results without synthesis or filtering. |
| C-02 | complete | False | True | The query asks what Article 9 requires for risk management, but the response merely dumps the truncated Article 9 text alongside many irrelevant articles (penalties, data governance, logging, etc.) without synthesizing or fully answering the question. |
| C-02 | appropriately-hedged | False | True | The response presents the Article 9 summary as if it were complete, even though the tool output is truncated mid-sentence, and does not flag that the text is partial or that the answer is incomplete. |
| C-02 | usable | False | True | A professional would need to ask a follow-up question to get a coherent, synthesized explanation of Article 9's risk management requirements; the raw data dump is not actionable without further clarification. |
| C-04 | appropriately-hedged | False | True | The response presents the Colorado lending-fintech regulations as if they answer the query without acknowledging that the tool results are not about the insurance sector and do not address strictness. |
| CQ-01 | appropriately-hedged | False | True | The response does not acknowledge that no tool result for New York was obtained; it simply ignores that part of the query, failing to hedge about the missing information. |
| CQ-03 | appropriately-hedged | False | True | The response presents the Colorado regulations as a definitive answer without acknowledging that the tool only queried one jurisdiction, so it fails to hedge the partial scope of the data. |
| CQ-04 | appropriately-hedged | False | True | The tool results contain no benchmark data, but the response does not flag this gap or hedge the missing answer; it simply omits the second part of the query. |
| CQ-05 | appropriately-hedged | False | True | The response does not indicate that it lacks data for New York and the EU, nor does it hedge about the missing jurisdictions; it simply ignores them. |
| H-02 | appropriately-hedged | False | True | The response does not acknowledge that the tool results contain no information about likely changes to Article 9, leaving the user without any indication of uncertainty or lack of data. |
| H-03 | grounded | False | True | The response is empty, so it contains no claims that can be grounded in the tool results. |
| H-03 | appropriately-hedged | False | True | The response is empty and does not hedge or acknowledge any uncertainty in the tool output. |
| H-04 | appropriately-hedged | False | True | The response does not acknowledge that the tool result pertains to insurance rather than credit scoring, nor does it indicate any uncertainty or lack of relevant data. |
| H-05 | appropriately-hedged | False | True | The response does not hedge or acknowledge that the tool result contradicts the premise of the question; it simply presents the law without addressing the confidence aspect. |
| H-05 | usable | False | True | A professional would need a follow-up to understand whether the assistant is confident that Illinois has no AI-specific insurance law, as the response does not answer that question. |
| U-02 | appropriately-hedged | False | True | The response does not address the model selection part of the query at all, so it fails to hedge appropriately (e.g., by stating that the tool data was insufficient or by giving a conditional recommendation). |
| U-03 | complete | False | True | The user asked for 'the one thing' to know before a client call, but the response provides an exhaustive list of all 15+ states with no prioritization or summary of the single most important takeaway. |
| U-04 | appropriately-hedged | False | True | The response presents the insurance regulation as the answer without noting that the tool result is limited to insurance and does not cover credit scoring. |
| U-05 | complete | False | True | The response fails to answer the user's question about what to tell a client regarding legality in the EU, instead merely listing regulations without synthesis or guidance. |
| C-19 | appropriately-hedged | False | True | The tool output is limited to Colorado, yet the response presents the information as a complete answer without any qualification or disclaimer about the narrow scope. |
| C-20 | usable | False | True | A professional asking for 'the stated effective date of Colorado's AI act' would need to infer which act is current; the response lacks a clear synthesis or direct answer, requiring a follow-up to clarify. |
| C-23 | grounded | False | True | The tool call results for Colorado frameworks contain no mention of 'foundation models' or 'general-purpose AI', yet the assistant lists them as if they answer the query, providing no evidence that they meet the condition. |
| C-23 | appropriately-hedged | False | True | The assistant asserts the frameworks as the answer without any hedge or acknowledgment that the tool data does not support the condition, despite the absence of the requested terms. |
| C-24 | appropriately-hedged | False | True | The tool returned no data for Article 72, but the response did not acknowledge that it was not answering the question; instead it presented unrelated articles without qualification. |
| CQ-06 | appropriately-hedged | False | True | The response does not acknowledge the absence of Illinois data and presents only Colorado information without qualification. |
| CQ-07 | appropriately-hedged | False | True | The response does not acknowledge that it lacks information about the top benchmark model's score; it simply ignores that part of the query instead of hedging or stating the data is unavailable. |
| CQ-08 | appropriately-hedged | False | True | The response does not note that the returned regulation is about insurance, not credit-scoring, nor does it acknowledge that the tool may have missed relevant credit-scoring obligations; it presents the insurance guidance as if it answers the query. |
| CQ-09 | appropriately-hedged | False | True | The Article 10 summary from the tool is truncated (ends with '(a) the '), but the assistant presents it as a complete statement without flagging the truncation, and the response does not note that the tool output is partial for that article. |
| CQ-10 | grounded | False | True | The response is empty and contains no claims, so it cannot be grounded in the tool results. |
| CQ-10 | appropriately-hedged | False | True | The response is empty and does not hedge or acknowledge any partiality in the tool output. |
| CQ-12 | appropriately-hedged | False | True | The tool output contains no information about EU equivalents, yet the response fails to acknowledge this gap or hedge the missing data; it simply omits the topic. |
| CQ-14 | appropriately-hedged | False | True | The response fails to indicate that it does not know the strictest article or which model handles it best, instead presenting raw data without qualification. |
| CQ-15 | complete | False | True | The response lists many regulations but does not explicitly answer whether similar requirements exist in the insurance sector generally; it lacks a synthesis or direct answer to the second part of the query. |
| CQ-15 | usable | False | True | The response is a raw data dump without synthesis; a professional would need to ask a follow-up to get a concise answer to the query. |
| CQ-16 | appropriately-hedged | False | True | The response reproduces truncated tool summaries (e.g., Article 14 ends with 'in particular where suc') without indicating that the text is incomplete, and fails to note that Article 13 was not returned by the tool. |
| CQ-17 | appropriately-hedged | False | True | The response presents the Colorado frameworks as the full answer without acknowledging that the tool only queried Colorado, and it does not mention that the model data (o3) was available but not used, leaving the second part of the question unaddressed. |
| CQ-18 | appropriately-hedged | False | True | The response does not acknowledge that it lacks information on New York and Illinois, nor does it flag that the comparison and ranking cannot be provided. |
| CQ-19 | appropriately-hedged | False | True | The response does not acknowledge the gap from the missing Article 52 information or the unanswered US state question, instead presenting unrelated data without qualification. |
| CQ-20 | appropriately-hedged | False | True | The response does not acknowledge the partial data (only o3 results were obtained) or the failure to retrieve all models; it simply outputs the raw error without any hedging or explanation. |
| CQ-21 | appropriately-hedged | False | True | The response asserts the obligations without any hedge or acknowledgment that the benchmark failure data is unavailable, leaving the second part of the query unanswered. |
| CQ-22 | appropriately-hedged | False | True | The response presents Colorado's rules as if they are the complete answer without acknowledging that only one state was queried and no information was retrieved for any other state. |
| CQ-23 | appropriately-hedged | False | True | The tool results do not indicate which EU AI Act article is the closest equivalent to Colorado's rule, yet the response asserts a list of articles without acknowledging that the specific equivalence requested is not directly supported by the data. |
| CQ-25 | appropriately-hedged | False | True | The response does not acknowledge that no EU data was retrieved, leaving the EU part unaddressed. |
| H-06 | appropriately-hedged | False | True | The response fails to acknowledge that the tool data does not directly answer the exemption question and makes no attempt to hedge or qualify the lack of a definitive answer. |
| H-07 | appropriately-hedged | False | True | The tool results contain no information about court challenges, yet the response does not acknowledge this gap or hedge its claims; it simply presents the data as if it answers the question. |
| H-10 | appropriately-hedged | False | True | The response presents the adoptions as straightforward facts and fails to hedge or note that the NAIC bulletin is not inherently binding and that its legal force depends on each state's legislative or regulatory action. |
| H-11 | appropriately-hedged | False | True | The tool results contain no information about the UK, yet the response does not acknowledge this gap or hedge the answer; it simply presents EU data as if it were a direct answer to the question. |
| H-12 | appropriately-hedged | False | True | The response is empty and does not acknowledge the partial or ambiguous nature of the tool output. |
| H-14 | appropriately-hedged | False | True | The response fails to mention that it lacks Illinois data or that the comparison cannot be made based on available information. |
| H-15 | appropriately-hedged | False | True | The response does not address the ambiguity or partiality of the tool data regarding enforcement likelihood; it simply dumps the data without acknowledging that the question remains unanswered. |
| H-16 | appropriately-hedged | False | True | The response does not address the distinction between guidance and law, nor does it hedge about whether these items constitute a 'law'; it presents them as facts without acknowledging the user's implied question. |
| H-16 | usable | False | True | A professional reading this response would still need to ask whether any of these items count as a federal AI law, so the response is not actionable without a follow-up. |
| H-18 | appropriately-hedged | False | True | The tool output contains no information about which article is 'most important', yet the response does not acknowledge this limitation or hedge its non-answer; it simply presents data as if it were a direct answer. |
| H-19 | appropriately-hedged | False | True | The tool output is silent on generative AI, yet the response does not acknowledge this uncertainty or qualify its answer; it simply presents the laws without addressing the specific question. |
| H-20 | appropriately-hedged | False | True | The response does not address the significant uncertainty indicated by the tool results (e.g., hallucination_rate=1.0) and provides no hedging. |
| H-22 | appropriately-hedged | False | True | The response does not acknowledge that the tool results contain no information about member-state enforcement differences, nor does it hedge the lack of an answer to the query. |
| H-23 | appropriately-hedged | False | True | The response does not hedge that the tool results are incomplete for the query (e.g., Colorado's non-insurance AI law is not covered by the NAIC bulletin) and presents the information as if it were the answer. |
| H-24 | appropriately-hedged | False | True | The tool result does not mention credit scoring, yet the response presents the regulation without acknowledging that it does not answer the question about credit-scoring rules. |
| U-06 | complete | False | True | The user asked for a single sentence about Article 9 exposure, but the response provided a full dump of multiple articles and no synthesized sentence, failing to address the request. |
| U-06 | appropriately-hedged | False | True | The response copies the truncated Article 9 summary ending with 'to ' without indicating it is incomplete, and while the Digital Omnibus proposal is hedged as 'proposed' and 'not yet law', the overall presentation of raw data without qualification on the truncation is not appropriately hedged. |
| U-07 | complete | False | True | The user asked for a three-bullet checklist, but the response provides regulation summaries without any checklist structure. |
| U-09 | appropriately-hedged | False | True | The response does not address the model selection at all, so it fails to hedge or acknowledge the partiality of the tool output regarding which model to pick. |
| U-10 | complete | False | True | The user asked for a plain-English summary of the NAIC bulletin, but the response is a raw list of all tool results without synthesis or actionable guidance, failing to address the request. |
| U-11 | appropriately-hedged | False | True | The response does not hedge or clarify that it is not providing the requested Article 13 obligations; it simply shows an error and then unrelated content, which could mislead the user. |
| U-12 | appropriately-hedged | False | True | The response presents the insurance regulation as the answer without acknowledging that the tool result is about insurance, not credit, and does not hedge about the mismatch or the lack of a direct answer. |
| U-13 | appropriately-hedged | False | True | The response makes no attempt to hedge or qualify any answer because it does not provide any answer to the user's question; it simply states the article content without acknowledging the missing judgment. |
| U-14 | appropriately-hedged | False | True | The response fails to acknowledge that no New York data was retrieved and presents irrelevant model comparison data without any qualification about the missing jurisdiction. |
| U-16 | complete | False | True | The user asked for a compliance line for a product page, but the response is a raw dump of all regulation data without any synthesis or a concise compliance statement. |
| U-19 | grounded | False | True | The response only lists Colorado regulations from the tool call but makes no mention of Illinois, so any claim about what Illinois requires is absent and unsupported. |
| U-19 | appropriately-hedged | False | True | The response does not acknowledge that it lacks data on Illinois or that the question cannot be answered with the available tool results. |
| U-21 | appropriately-hedged | False | True | The response does not address the data at all, failing to hedge or acknowledge any ambiguity in the tool output. |
| U-22 | complete | False | True | The user explicitly requested a 15-word Slack update, but the response is a lengthy multi-paragraph answer that does not provide the requested concise summary. |
| U-23 | complete | False | True | The query asked for two articles in priority order, but the response lists eight articles without identifying any two or providing a priority order. |
| U-24 | appropriately-hedged | False | True | The response does not address the query, so it fails to hedge any uncertainty about the model's performance or the risk rating. |
| U-25 | complete | False | True | The response fails to provide the requested single follow-up question to ask legal; instead it lists all regulations without addressing the query. |

## Bias probes

| Probe | Flagged | Total |
|---|---|---|
| consistency | 27 | 79 |
| verbosity | 10 | 79 |
| sycophancy | 6 | 79 |
| order | 13 | 47 |

## Cost / latency

- Cases: 85
- Total cost: $0.039272
- p50 latency: 16649.9 ms
- p95 latency: 43409.2 ms

## What this is, and what it isn't

Carlos is the sole labeler for the human-label side of this comparison; that's disclosed here, not hidden. The judge prompt is versioned in `judge_prompts/`; results should be regenerated whenever the prompt changes.
