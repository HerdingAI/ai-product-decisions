# LLM-as-judge — calibration results

**Target:** `deepseek/deepseek-v4-flash`  
**Cases judged:** 95

## Judge-vs-human agreement

| Criterion | n | Agreement | Cohen's κ |
|---|---|---|---|
| grounded | 95 | 95% | 0.26 |
| complete | 95 | 86% | 0.49 |
| appropriately-hedged | 95 | 39% | 0.04 |
| usable | 95 | 93% | 0.56 |

## Disagreements (judge vs. human)

Raw rows below; see `RESULTS.md` for the coded failure-pattern analysis (verbosity bias, position bias, criterion misreading, etc. — spec §4 Artifact #2 acceptance criteria).

| Case | Criterion | Judge | Human | Judge's reason |
|---|---|---|---|---|
| C-01 | complete | False | True | The response lists all tool results but does not synthesize or directly answer what Colorado requires for AI model risk management; it includes many irrelevant entries and fails to provide a focused answer. |
| C-01 | usable | False | True | A professional would need to extract the Colorado-specific requirements from a long list of non-Colorado entries, making the response impractical without follow-up. |
| C-02 | complete | False | True | The response fails to answer the query about Article 9's risk management requirements; it merely lists truncated tool outputs and includes irrelevant articles, leaving the user without a coherent explanation. |
| C-02 | appropriately-hedged | False | True | The response presents the truncated Article 9 summary (ending mid-sentence) as if complete, and does not indicate that the tool output was partial or that other articles are not directly responsive. |
| C-02 | usable | False | True | A professional would need to ask for a proper synthesis because the response is a raw data dump with no analysis or actionable summary. |
| C-04 | appropriately-hedged | False | True | The response does not acknowledge that the tool results are for lending-fintech, not insurance, and presents them as if they answer the query without qualification. |
| C-05 | appropriately-hedged | False | True | The response makes no attempt to address the model comparison part of the query, and does not hedge or acknowledge the gap. |
| CQ-01 | appropriately-hedged | False | True | The response fails to hedge or flag that no New York information was retrieved, leaving the user with an incomplete answer. |
| CQ-02 | appropriately-hedged | False | True | The tool results contain no information about GPT-4o or o3, yet the response does not acknowledge this gap or hedge its inability to answer the comparison; it simply ignores the query. |
| CQ-03 | appropriately-hedged | False | True | The response does not indicate that it is limited to Colorado regulations, despite the query asking broadly about regulations. |
| CQ-04 | appropriately-hedged | False | True | The tool call results contain no benchmark data, yet the response does not hedge or acknowledge the missing information; it simply ignores the second part of the question. |
| CQ-05 | appropriately-hedged | False | True | The response does not acknowledge that tool results were only available for Colorado, leaving the user unaware that New York and EU information is missing. |
| H-01 | appropriately-hedged | False | True | The tool output is silent on the relative strictness of the two frameworks, yet the response does not acknowledge this gap or hedge its non-answer; it presents the data as if it were sufficient, failing to flag the missing comparison. |
| H-02 | appropriately-hedged | False | True | The response does not acknowledge that the tool results contain no information about future changes to Article 9, and it presents the data without any qualification about the lack of answer. |
| H-04 | appropriately-hedged | False | True | The response presents the insurance guidance as if it were the answer to the credit-scoring question without acknowledging that the tool result is from a different sector (insurance) and does not address lenders or credit scoring. |
| H-05 | appropriately-hedged | False | True | The response asserts the regulation as fact without acknowledging that the user's premise (no AI-specific law) is contradicted by the tool data, and does not hedge about the confidence level. |
| H-05 | usable | False | True | A professional would need to ask a follow-up to understand whether the existence of the NAIC Model Bulletin means there is an AI-specific insurance law, which the response does not clarify. |
| U-03 | complete | False | True | The user asked for 'the one thing I need to know' but the response lists all 16 entries without identifying a single key takeaway or prioritizing the information. |
| U-04 | appropriately-hedged | False | True | The tool result clearly indicates the regulation applies to insurance, not credit scoring, yet the response presents it without any qualification or acknowledgment that the query's specific topic is not addressed by the returned data. |
| U-05 | complete | False | True | The query asks for advice on what to tell a client about legality in the EU, but the response merely lists regulations without addressing the client's question or providing any guidance. |
| U-05 | appropriately-hedged | False | True | The response does not hedge or address the ambiguity of the client's undefined 'this' and instead presents a raw list of regulations, failing to qualify the answer appropriately. |
| C-07 | appropriately-hedged | False | True | The response fails to indicate that the information provided is not about Article 13 and does not acknowledge the gap; it presents unrelated articles without qualification. |
| C-08 | complete | False | True | The response only provides a truncated summary of Article 14 (ending mid-sentence with 'in particular where suc') and does not fully enumerate or explain the human-oversight requirements, while also including irrelevant articles not asked about. |
| C-08 | appropriately-hedged | False | True | The response does not flag that the Article 14 summary is incomplete or that the tool result was cut off, and it presents multiple unrelated articles without clarifying their relevance to the specific question. |
| C-08 | usable | False | True | A professional would need to extract the human-oversight requirements from a raw, truncated dump of tool outputs and would have to ask a follow-up question to get a clear, synthesized answer. |
| C-10 | appropriately-hedged | False | True | The tool output is limited to Colorado and does not provide a comparison, yet the response does not hedge or acknowledge the uncertainty about whether Colorado was the first state. |
| C-11 | appropriately-hedged | False | True | The tool results contain no accuracy data, yet the response does not acknowledge this gap or hedge; it simply ignores the query. |
| C-12 | grounded | False | True | The response includes Colorado SB 26-189 and SB 24-205 as applicable to insurance, but the tool data labels their sector as 'lending-fintech', not insurance. |
| C-12 | appropriately-hedged | False | True | The response asserts Colorado SB 26-189 and SB 24-205 as applicable to insurance without acknowledging that the tool data classifies them under 'lending-fintech', not insurance. |
| C-14 | appropriately-hedged | False | True | The response does not hedge or acknowledge that it is not answering the question about Article 6, and presents other articles without clarifying their relevance to the query. |
| C-15 | appropriately-hedged | False | True | The tool output for Article 12 is truncated (ends with 'substantial modificat'), but the response presents it without noting the truncation or that the summary is incomplete. |
| C-16 | usable | False | True | The response is a verbatim dump of all tool results, including many irrelevant articles, requiring the user to extract the penalty information themselves, so a professional would need a follow-up for a concise answer. |
| C-17 | appropriately-hedged | False | True | The response presents both the current and repealed regulations side by side without flagging that the current law's summary does not explicitly mention algorithmic discrimination, nor does it note that the repealed act's anti-discrimination provisions are no longer in effect. |
| C-18 | appropriately-hedged | False | True | The response asserts regulatory details without acknowledging that it is not addressing the user's query about model compliance scores, and the tool results for model o3 contain compliance scores that could have been used. |
| C-19 | appropriately-hedged | False | True | The response does not hedge about the limited scope of the data (only Colorado) and presents the information as a complete answer to the query. |
| C-21 | appropriately-hedged | False | True | The response does not hedge or indicate that the information provided does not answer the query; it simply dumps unrelated data. |
| C-24 | appropriately-hedged | False | True | The response does not acknowledge that it lacks information on Article 72 or that the listed articles are not the one asked about; it presents the error and then unrelated content without any hedging about the missing answer. |
| C-25 | grounded | False | True | The response does not use any of the benchmark results returned by query_by_model, which contained the scores for GPT-4o; instead it only summarizes regulation data from query_by_jurisdiction, which does not answer the question about benchmark scores. |
| C-25 | appropriately-hedged | False | True | The response does not hedge at all; it fails to acknowledge that it is not addressing the question and does not indicate that the benchmark data was available but not used. |
| CQ-06 | appropriately-hedged | False | True | The response does not acknowledge that Illinois information is absent from the tool results; it presents only Colorado data without any qualification about the missing comparison. |
| CQ-07 | appropriately-hedged | False | True | The tool results contain no information about benchmark model scores, yet the response does not indicate this gap or hedge on that part of the query. |
| CQ-08 | appropriately-hedged | False | True | The response presents the insurance regulation as if it answers the credit-scoring question without noting that the tool result is about insurance, not credit scoring, and does not acknowledge the gap. |
| CQ-09 | appropriately-hedged | False | True | The Article 10 summary is truncated mid-sentence without any indication that the text is incomplete, which could mislead the user. |
| CQ-10 | grounded | True | False | The response makes no specific claims, so there is nothing to be ungrounded. |
| CQ-12 | appropriately-hedged | False | True | The response does not hedge or flag that the EU-equivalence part of the query is unanswered; it simply omits that sub-question entirely. |
| CQ-14 | appropriately-hedged | False | True | The tool output is silent on which article is strictest and which model handles it best, but the response does not acknowledge this gap and instead presents the data without qualification. |
| CQ-15 | complete | False | True | The response lists many insurance regulations but does not explicitly answer whether there is anything similar in the insurance sector generally; it fails to synthesize or directly address the second part of the query. |
| CQ-15 | usable | False | True | A professional would need to extract the answer from a lengthy data dump; the response does not provide a concise, actionable answer to the query. |
| CQ-16 | appropriately-hedged | False | True | The response fails to acknowledge that Article 13 was not retrieved from the tool and instead presents unrelated articles without any hedging about the missing requested content. |
| CQ-18 | appropriately-hedged | False | True | The response does not acknowledge that it lacks data for New York and Illinois, nor does it indicate that the model comparison data is unrelated to state enforcement. |
| CQ-19 | appropriately-hedged | False | True | The tool results contain no information about US state transparency rules, but the response does not acknowledge this gap or hedge its inability to answer that part of the query. |
| CQ-21 | appropriately-hedged | False | True | The tool results contain no information about benchmark failure rates, yet the response does not flag that it lacks this information; it simply ignores the second part of the query. |
| CQ-22 | appropriately-hedged | False | True | The response presents Colorado rules as if they are the complete answer without acknowledging that only one state was queried and that other states' rules are missing, failing to hedge the partial coverage. |
| CQ-24 | appropriately-hedged | False | True | The tool output is silent on the question of model comparison, but the response does not acknowledge this gap; it presents unrelated data as if it were an answer. |
| CQ-25 | appropriately-hedged | False | True | The response does not acknowledge that no EU data was retrieved, presenting an incomplete answer without qualification. |
| H-06 | appropriately-hedged | False | True | The tool results do not contain any information about exemptions for chatbots, yet the response presents the data without acknowledging that the question of exemption is unanswered or that the tool output is silent on that point. |
| H-07 | appropriately-hedged | False | True | The tool results are silent on court challenges, but the response does not acknowledge this limitation or hedge; it simply ignores the question. |
| H-11 | appropriately-hedged | False | True | The tool results are silent on UK applicability, yet the response does not flag this gap or hedge the answer; it presents EU data as if it were a direct answer to the question. |
| H-14 | appropriately-hedged | False | True | The response does not acknowledge that no tool result for Illinois was available, nor does it qualify the comparison; it presents only New York's data as if it fully answers the question. |
| H-16 | appropriately-hedged | False | True | The response does not acknowledge that the listed items are guidance and model bulletins, not laws, and fails to hedge the answer to the user's question about 'law'. |
| H-16 | usable | False | True | A professional cannot act on this response because it does not directly answer the yes/no question, requiring a follow-up to clarify the status of the listed items as law. |
| H-17 | appropriately-hedged | False | True | The tool results contain no information about an 'EU AI Act certified' label or any certification scheme, yet the response does not acknowledge this gap or hedge the lack of support for such a claim. |
| H-18 | appropriately-hedged | False | True | The response does not acknowledge that the tool results are silent on the question of importance, nor does it hedge the lack of an answer; it presents data as if it were responsive. |
| H-19 | appropriately-hedged | False | True | The response does not acknowledge that the tool results contain no mention of generative AI; it presents the summaries as if they answer the question, without any hedge about the missing information. |
| H-21 | grounded | False | True | The response contains no claims and therefore cannot be grounded in the tool-call results. |
| H-21 | appropriately-hedged | False | True | The response is empty and makes no attempt to hedge or qualify the uncertainty present in the tool results. |
| H-22 | appropriately-hedged | False | True | The tool results contain no information about member state enforcement, yet the response does not acknowledge this gap or hedge its non-answer. |
| H-23 | appropriately-hedged | False | True | The response does not hedge or acknowledge that the tool results only show adoption in some states and do not directly answer the user's question about compliance in every state, so it is not appropriately hedged. |
| H-24 | appropriately-hedged | False | True | The tool result does not mention credit scoring or toughness comparisons, yet the response presents the regulation without flagging that it does not answer the question, failing to hedge the gap. |
| U-06 | complete | False | True | The user asked for a single sentence for a board deck, but the assistant provided a multi-paragraph list of summaries without condensing into one sentence or addressing the specific request. |
| U-07 | complete | False | True | The user asked for a three-bullet checklist, but the response provides summaries of two regulations without any checklist format or actionable steps. |
| U-10 | complete | False | True | The user asked for a plain-English summary of the NAIC bulletin, but the response merely lists all returned regulations verbatim without synthesizing or explaining the bulletin's implications for a non-lawyer PM. |
| U-11 | appropriately-hedged | False | True | The response does not clearly communicate that it cannot fulfill the request for Article 13 obligations; it presents other articles without qualification, potentially misleading the user. |
| U-12 | appropriately-hedged | False | True | The response does not acknowledge that the regulation is specific to insurance and may not apply to credit tools, nor does it note the lack of information on credit tools. |
| U-14 | appropriately-hedged | False | True | The response fails to acknowledge that no New York data was retrieved and presents irrelevant EU AI Act compliance data without flagging the gap. |
| U-16 | complete | False | True | The user requested a concise compliance line for a product page, but the response merely lists raw regulation entries without synthesizing a product-ready statement, leaving the request unaddressed. |
| U-17 | appropriately-hedged | False | True | The response does not hedge or acknowledge that it failed to answer the question; it presents information without addressing the user's request for a prioritization. |
| U-19 | grounded | True | False | The response's claims about Colorado regulations are directly supported by the tool call results. |
| U-20 | appropriately-hedged | False | True | The response makes no claim about the model's sufficiency and fails to acknowledge or hedge regarding the model performance data that is partial and ambiguous, thus not appropriately hedged. |
| U-22 | complete | False | True | The user requested a 15-word Slack update, but the assistant provided a multi-paragraph detailed response, not a concise update. |
| U-23 | complete | False | True | The user asked to name two EU AI Act articles in priority order, but the response lists nine items without prioritizing or answering the question. |
| U-25 | complete | False | True | The query asks for a single follow-up question to ask legal, but the response provides a list of all regulations with no follow-up question, thus failing to address the query at all. |
| U-25 | appropriately-hedged | False | True | The response does not hedge because it does not attempt to answer the query; it simply dumps data without acknowledging that it is not providing the requested follow-up question. |

## Bias probes

| Probe | Flagged | Total |
|---|---|---|
| consistency | 21 | 92 |
| verbosity | 13 | 92 |
| sycophancy | 9 | 92 |
| order | 21 | 57 |

## Cost / latency

- Cases: 95
- Total cost: $0.043637
- p50 latency: 22864.7 ms
- p95 latency: 39812.4 ms

## What this is, and what it isn't

Carlos is the sole labeler for the human-label side of this comparison; that's disclosed here, not hidden. The judge prompt is versioned in `judge_prompts/`; results should be regenerated whenever the prompt changes.
