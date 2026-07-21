# Open-coding worksheet — complete+appropriately-hedged+usable cluster (51 cases)

Mechanical assembly only — no themes named here. For each case: the query, the full response, and the judge's per-criterion reasons. Read and name recurring themes (e.g. 'raw tool dump, no synthesis', 'confident despite partial data') in a new column or a separate notes file.

**Re-run note:** this cluster is entangled with the `appropriately-hedged` drift (RESULTS.md §1/§2) — if the hedging labels/rubric get fixed, membership here will change. Re-run `build_opencoding_worksheet.py` after that fix before finalizing themes.

## C-01 (grounding)

**Query:** What does Colorado require for AI model risk management?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**California NAIC AI Model Bulletin Adoption** (California)
Status: adopted | Sector: insurance | Effective: 2024-12-15
California adopted the NAIC Model Bulletin on insurers' use of AI, joining the 12-state NAIC AI Systems Evaluation Tool pilot. Requires insurer governance framework, risk management controls, and third-party vendor oversight for AI systems used in insurance practices.

**Maryland NAIC AI Model Bulletin Adoption** (Maryland)
Status: adopted | Sector: insurance | Effective: 2025-03-01
Maryland adopted the NAIC Model Bulletin on insurers' use of AI and participates in the 12-state NAIC AI Systems Evaluation Tool pilot. Requires written governance, testing for bias, and documentation of AI systems used in underwriting and pricing.

**Virginia NAIC AI Model Bulletin Adoption** (Virginia)
Status: adopted | Sector: insurance | Effective: 2024-11-01
Virginia adopted the NAIC Model Bulletin on AI use in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, risk assessment, and oversight of AI systems in insurance underwriting and pricing decisions.

**Connecticut NAIC AI Model Bulletin Adoption** (Connecticut)
Status: adopted | Sector: insurance | Effective: 2025-01-01
Connecticut adopted the NAIC Model Bulletin and participates in the 12-state NAIC AI Systems Evaluation Tool pilot (January–September 2026). Requires insurer AI governance, third-party model oversight, and bias testing.

**Pennsylvania NAIC AI Model Bulletin Adoption** (Pennsylvania)
Status: adopted | Sector: insurance | Effective: 2024-10-01
Pennsylvania adopted the NAIC Model Bulletin on AI use in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance framework and risk management for AI systems used in underwriting, pricing, and claims.

**Louisiana NAIC AI Model Bulletin Adoption** (Louisiana)
Status: adopted | Sector: insurance | Effective: 2024-12-01
Louisiana adopted the NAIC Model Bulletin on insurers' use of AI. Participates in the 12-state NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and bias testing for AI systems in insurance.

**Wisconsin NAIC AI Model Bulletin Adoption** (Wisconsin)
Status: adopted | Sector: insurance | Effective: 2025-02-01
Wisconsin adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires insurer governance framework, risk management, and third-party oversight for AI in insurance.

**Florida NAIC AI Model Bulletin Adoption** (Florida)
Status: adopted | Sector: insurance | Effective: 2024-09-01
Florida adopted the NAIC Model Bulletin on AI in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance and risk management framework for AI systems used by insurers.

**Rhode Island NAIC AI Model Bulletin Adoption** (Rhode Island)
Status: adopted | Sector: insurance | Effective: 2025-01-15
Rhode Island adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and oversight of AI systems in insurance.

**Iowa NAIC AI Model Bulletin Adoption** (Iowa)
Status: adopted | Sector: insurance | Effective: 2025-03-15
Iowa adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance and risk management framework for AI systems used in insurance underwriting and pricing.

**Vermont NAIC AI Model Bulletin Adoption** (Vermont)
Status: adopted | Sector: insurance | Effective: 2025-02-15
Vermont adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and bias testing for AI systems in insurance.

**NAIC AI Systems Evaluation Tool Pilot** (Multi-State)
Status: pending | Sector: insurance | Effective: 2026-01-01
12-state pilot (Colorado, Maryland, Louisiana, Virginia, Connecticut, Pennsylvania, Wisconsin, Florida, Rhode Island, Iowa, Vermont, California) running January–September 2026. Tests a standardized evaluation framework for AI systems used by insurers. Pilot outcomes will inform potential national adoption.

**Texas NAIC AI Model Bulletin Adoption** (Texas)
Status: adopted | Sector: insurance | Effective: 2025-06-01
Texas adopted the NAIC Model Bulletin on insurers' use of AI. Requires governance framework, risk management, and documentation of AI systems in insurance underwriting and pricing. Not part of the 12-state evaluation tool pilot.

**Illinois NAIC AI Model Bulletin Adoption** (Illinois)
Status: adopted | Sector: insurance | Effective: 2025-04-01
Illinois adopted the NAIC Model Bulletin on AI in insurance. Requires governance, documentation, and third-party oversight for AI systems. Not part of the 12-state evaluation tool pilot.

**NAIC Model Bulletin on AI (Base Model)** (Federal)
Status: adopted | Sector: insurance | Effective: 2023-12-04
The NAIC's model bulletin providing guidance to insurers on the use of AI systems. Requires a governance framework, risk management controls, and third-party vendor oversight. Over 20 states have adopted or are in the process of adopting this bulletin. This is the baseline against which state-specific frameworks like NY's Circular Letter 7 and Colorado's insurance regs are measured.

**New Jersey NAIC AI Model Bulletin Adoption** (New Jersey)
Status: adopted | Sector: insurance | Effective: 2025-05-01
New Jersey adopted the NAIC Model Bulletin on AI use in insurance. Requires governance, documentation, and bias testing for AI systems in insurance underwriting and pricing.

**Ohio NAIC AI Model Bulletin Adoption** (Ohio)
Status: adopted | Sector: insurance | Effective: 2025-07-01
Ohio adopted the NAIC Model Bulletin on insurers' use of AI. Requires governance framework and risk management for AI systems in insurance. Not part of the 12-state evaluation tool pilot.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
- California NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Maryland NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Virginia NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Connecticut NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Pennsylvania NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Louisiana NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Wisconsin NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Florida NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Rhode Island NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Iowa NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Vermont NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- NAIC AI Systems Evaluation Tool Pilot: https://content.naic.org/insurance-topics/artificial-intelligence
- Texas NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Illinois NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- NAIC Model Bulletin on AI (Base Model): https://content.naic.org/insurance-topics/artificial-intelligence
- New Jersey NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Ohio NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
```

**Judge reasons (failed criteria):**
- *complete*: The response fails to directly answer the query about Colorado's requirements; it includes many irrelevant entries from other states' NAIC adoptions without focusing on Colorado, leaving the user to extract the relevant information.
- *appropriately-hedged*: The response presents non-Colorado entries (e.g., California, Maryland, etc.) without any indication that they are not Colorado's requirements, which could mislead the user into thinking they apply to Colorado.
- *usable*: A professional would need to ask a follow-up question to clarify which entries are actually Colorado's requirements, as the response is a raw dump of all tool results without synthesis or filtering.

**Theme (Carlos fills in):** _____

---

## C-02 (grounding)

**Query:** What does the EU AI Act require for risk management under Article 9?

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks what Article 9 requires for risk management, but the response merely dumps the truncated Article 9 text alongside many irrelevant articles (penalties, data governance, logging, etc.) without synthesizing or fully answering the question.
- *appropriately-hedged*: The response presents the Article 9 summary as if it were complete, even though the tool output is truncated mid-sentence, and does not flag that the text is partial or that the answer is incomplete.
- *usable*: A professional would need to ask a follow-up question to get a coherent, synthesized explanation of Article 9's risk management requirements; the raw data dump is not actionable without further clarification.

**Theme (Carlos fills in):** _____

---

## C-04 (grounding)

**Query:** What insurance-sector AI regulations exist, and which ones are the strictest?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for insurance-sector AI regulations and which are strictest, but the response only lists two Colorado lending-fintech regulations and never addresses insurance or strictness.
- *appropriately-hedged*: The response presents the Colorado lending-fintech regulations as if they answer the query without acknowledging that the tool results are not about the insurance sector and do not address strictness.
- *usable*: A professional would need to follow up because the response does not provide any insurance-sector regulations or a comparison of strictness, leaving the core question unanswered.

**Theme (Carlos fills in):** _____

---

## CQ-01 (compound)

**Query:** What does New York require for AI in credit scoring, and how does that compare to Colorado's approach?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

{
  "models": [
    {
      "model_id": "gpt-4o",
      "model_name": "GPT-4o (OpenAI)",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    },
    {
      "model_id": "o3",
      "model_name": "OpenAI o3",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    }
  ],
  "categories": {
    "art9_risk_management": {
      "name": "Article 9: Risk Management System",
      "results": [
        {
          "model_id": "gpt-4o",
          "avg_compliance_score": 3.0,
          "avg_plausibility_score": 4.25,
          "accuracy": 0.688,
          "hallucination_rate": 1.062,
          "scenario": "Scenario A"
        },
        {
          "model_id": "o3",
          "avg_compliance_score": 2.375,
          "avg_plausibility_score": 4.0,
          "accuracy": 0.844,
          "hallucination_rate": 1.0,
          "scenario": "Scenario A"
        }
      ]
    },
    "art10_data_governance": {
      "n

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for New York's requirements and a comparison to Colorado, but the response only covers Colorado and includes irrelevant model comparison data, omitting New York entirely.
- *appropriately-hedged*: The response does not acknowledge that no tool result for New York was obtained; it simply ignores that part of the query, failing to hedge about the missing information.
- *usable*: A professional cannot act on this response because it does not answer the question about New York's requirements or provide the requested comparison, leaving the user without the needed information.

**Theme (Carlos fills in):** _____

---

## CQ-03 (compound)

**Query:** What lending and fintech regulations should I know about, and are there any AI-specific rules mentioned?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked broadly about lending and fintech regulations, but the response only covers Colorado; it does not address other jurisdictions or indicate that the search was limited to Colorado, leaving the main question unanswered.
- *appropriately-hedged*: The response presents the Colorado regulations as a definitive answer without acknowledging that the tool only queried one jurisdiction, so it fails to hedge the partial scope of the data.
- *usable*: A professional acting on this response would not know whether other relevant regulations exist elsewhere, requiring a follow-up question to clarify the scope, so the response is not immediately actionable.

**Theme (Carlos fills in):** _____

---

## CQ-04 (compound)

**Query:** What does the EU AI Act say about Article 10, and which models score best on that article in the benchmark?

**Response:**
```
**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks both what Article 10 says and which models score best on that article in a benchmark; the response only provides Article 10 text and unrelated articles, with no mention of any benchmark or model scores.
- *appropriately-hedged*: The tool results contain no benchmark data, but the response does not flag this gap or hedge the missing answer; it simply omits the second part of the query.
- *usable*: A professional asking for benchmark model scores would need to follow up because the response provides no information on that topic, only a dump of unrelated regulatory articles.

**Theme (Carlos fills in):** _____

---

## CQ-05 (compound)

**Query:** Summarize AI regulation requirements across Colorado, New York, and the EU, and flag any that conflict.

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for summaries across Colorado, New York, and the EU, but the response only covers Colorado, omitting New York and the EU entirely.
- *appropriately-hedged*: The response does not indicate that it lacks data for New York and the EU, nor does it hedge about the missing jurisdictions; it simply ignores them.
- *usable*: A professional cannot act on this because it provides no information about New York or EU regulations and does not flag any conflicts as requested.

**Theme (Carlos fills in):** _____

---

## H-02 (hedge)

**Query:** Will the EU AI Act's Article 9 requirements likely change in the next version?

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The response fails to answer the user's question about whether Article 9 requirements will likely change; it merely regurgitates tool data without analysis.
- *appropriately-hedged*: The response does not acknowledge that the tool results contain no information about likely changes to Article 9, leaving the user without any indication of uncertainty or lack of data.
- *usable*: The response does not provide an answer to the user's question, so a professional would need to follow up to get an actual analysis.

**Theme (Carlos fills in):** _____

---

## H-04 (hedge)

**Query:** Does New York's AI credit-scoring rule apply to small lenders, or just large banks?

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The query asks about New York's AI credit-scoring rule for lenders, but the response only describes an insurance underwriting guidance, leaving the question entirely unanswered.
- *appropriately-hedged*: The response does not acknowledge that the tool result pertains to insurance rather than credit scoring, nor does it indicate any uncertainty or lack of relevant data.
- *usable*: A professional cannot act on this response because it does not address the specific question about credit-scoring rules for small lenders versus large banks, necessitating a follow-up.

**Theme (Carlos fills in):** _____

---

## H-05 (hedge)

**Query:** How confident are you that Illinois has no AI-specific insurance law?

**Response:**
```
**Illinois NAIC AI Model Bulletin Adoption** (Illinois)
Status: adopted | Sector: insurance | Effective: 2025-04-01
Illinois adopted the NAIC Model Bulletin on AI in insurance. Requires governance, documentation, and third-party oversight for AI systems. Not part of the 12-state evaluation tool pilot.

**Sources:**
- Illinois NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
```

**Judge reasons (failed criteria):**
- *complete*: The response does not address the user's question about confidence; it merely presents the law found, without stating whether the assistant is confident that there is no AI-specific insurance law.
- *appropriately-hedged*: The response does not hedge or acknowledge that the tool result contradicts the premise of the question; it simply presents the law without addressing the confidence aspect.
- *usable*: A professional would need a follow-up to understand whether the assistant is confident that Illinois has no AI-specific insurance law, as the response does not answer that question.

**Theme (Carlos fills in):** _____

---

## U-02 (usability)

**Query:** My team needs to pick a model for an Article 9 compliance tool by Friday — what do you recommend and why in one paragraph?

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for a model recommendation and reasoning, but the response provides only a summary of Article 9 and no model suggestion.
- *appropriately-hedged*: The response does not address the model selection part of the query at all, so it fails to hedge appropriately (e.g., by stating that the tool data was insufficient or by giving a conditional recommendation).
- *usable*: A professional cannot act on this response because it contains no recommendation or actionable guidance for picking a model.

**Theme (Carlos fills in):** _____

---

## U-04 (usability)

**Query:** Give me a two-sentence summary of what New York requires for AI in credit scoring.

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for AI requirements in credit scoring, but the response only covers an insurance regulation and does not address credit scoring at all.
- *appropriately-hedged*: The response presents the insurance regulation as the answer without noting that the tool result is limited to insurance and does not cover credit scoring.
- *usable*: A professional seeking credit-scoring rules would need to follow up because the response is about a different sector (insurance) and does not answer the question.

**Theme (Carlos fills in):** _____

---

## C-19 (grounding)

**Query:** What does your data show about AI regulation in the banking sector?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks about AI regulation in the banking sector generally, but the response only covers Colorado without acknowledging that the data is limited to a single jurisdiction, leaving the broader question unanswered.
- *appropriately-hedged*: The tool output is limited to Colorado, yet the response presents the information as a complete answer without any qualification or disclaimer about the narrow scope.
- *usable*: A professional seeking AI regulation across the banking sector would need to follow up to obtain data for other jurisdictions, as the response does not indicate its limitation to Colorado.

**Theme (Carlos fills in):** _____

---

## C-24 (grounding)

**Query:** What post-market monitoring does EU AI Act Article 72 require of providers?

**Response:**
```
Error: Article 72 not found. Available: 9, 10, 12, 14, 15.

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The response does not answer the user's question about Article 72; it only lists other articles without addressing post-market monitoring.
- *appropriately-hedged*: The tool returned no data for Article 72, but the response did not acknowledge that it was not answering the question; instead it presented unrelated articles without qualification.
- *usable*: The response does not provide the requested information about Article 72, so a professional cannot act on it without further inquiry.

**Theme (Carlos fills in):** _____

---

## CQ-06 (compound)

**Query:** Compare Colorado and Illinois on AI insurance rules, and tell me which imposes more obligations.

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

{
  "models": [
    {
      "model_id": "gpt-4o",
      "model_name": "GPT-4o (OpenAI)",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    },
    {
      "model_id": "o3",
      "model_name": "OpenAI o3",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    }
  ],
  "categories": {
    "art9_risk_management": {
      "name": "Article 9: Risk Management System",
      "results": [
        {
          "model_id": "gpt-4o",
          "avg_compliance_score": 3.0,
          "avg_plausibility_score": 4.25,
          "accuracy": 0.688,
          "hallucination_rate": 1.062,
          "scenario": "Scenario A"
        },
        {
          "model_id": "o3",
          "avg_compliance_score": 2.375,
          "avg_plausibility_score": 4.0,
          "accuracy": 0.844,
          "hallucination_rate": 1.0,
          "scenario": "Scenario A"
        }
      ]
    },
    "art10_data_governance": {
      "n

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The response does not address Illinois at all, failing to compare the two states as requested.
- *appropriately-hedged*: The response does not acknowledge the absence of Illinois data and presents only Colorado information without qualification.
- *usable*: A professional cannot determine which state imposes more obligations because Illinois is not discussed and the model comparison data is irrelevant.

**Theme (Carlos fills in):** _____

---

## CQ-07 (compound)

**Query:** What does EU AI Act Article 9 require, and how does the top benchmark model score on it?

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks both what Article 9 requires and how the top benchmark model scores on it; the response only covers Article 9 and other articles, completely omitting any mention of a benchmark model or its score.
- *appropriately-hedged*: The response does not acknowledge that it lacks information about the top benchmark model's score; it simply ignores that part of the query instead of hedging or stating the data is unavailable.
- *usable*: A professional cannot act on this response because the second part of the question (benchmark model score) is unanswered, requiring a follow-up query to obtain that information.

**Theme (Carlos fills in):** _____

---

## CQ-08 (compound)

**Query:** List New York's AI credit-scoring obligations and then flag which ones would be hardest for a small fintech to meet.

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for AI credit-scoring obligations and a flag for hardest to meet, but the response only lists one insurance underwriting regulation and does not address credit-scoring obligations or flag difficulty for a small fintech.
- *appropriately-hedged*: The response does not note that the returned regulation is about insurance, not credit-scoring, nor does it acknowledge that the tool may have missed relevant credit-scoring obligations; it presents the insurance guidance as if it answers the query.
- *usable*: A professional seeking AI credit-scoring obligations would not be able to act on this response because it covers the wrong sector and omits the required difficulty analysis, necessitating a follow-up.

**Theme (Carlos fills in):** _____

---

## CQ-09 (compound)

**Query:** Give me the EU AI Act Article 10 data-governance rules and a one-line takeaway for a data team.

**Response:**
```
**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked for Article 10 data-governance rules and a one-line takeaway for a data team; the response merely repeats the truncated Article 10 summary and dumps several unrelated articles, omitting the requested one-line takeaway and failing to extract or synthesize the data-governance rules.
- *appropriately-hedged*: The Article 10 summary from the tool is truncated (ends with '(a) the '), but the assistant presents it as a complete statement without flagging the truncation, and the response does not note that the tool output is partial for that article.
- *usable*: A data team would need a follow-up question to get the one-line takeaway and to understand which parts of the raw article dump constitute the data-governance rules; the response is an unsynthesized list of tool results, not an actionable answer.

**Theme (Carlos fills in):** _____

---

## CQ-12 (compound)

**Query:** What AI rules apply in Colorado, and which of them also have an equivalent at the EU level?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks which Colorado AI rules also have an EU equivalent, but the response does not address EU equivalence at all, leaving the second part of the question unanswered.
- *appropriately-hedged*: The tool output contains no information about EU equivalents, yet the response fails to acknowledge this gap or hedge the missing data; it simply omits the topic.
- *usable*: A professional cannot act on this response because the missing EU-equivalence information would require a follow-up question to complete the analysis.

**Theme (Carlos fills in):** _____

---

## CQ-14 (compound)

**Query:** Tell me the strictest EU AI Act article for high-risk systems and which model handles it best.

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The response does not identify the strictest article nor mention any model, leaving both parts of the query unanswered.
- *appropriately-hedged*: The response fails to indicate that it does not know the strictest article or which model handles it best, instead presenting raw data without qualification.
- *usable*: The response is a raw list of articles with no analysis or conclusion, so a professional cannot act on it without further clarification.

**Theme (Carlos fills in):** _____

---

## CQ-16 (compound)

**Query:** Give me EU AI Act Articles 13 and 14 side by side for a compliance checklist.

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The response omits Article 13 entirely, which was explicitly requested alongside Article 14, and does not address the 'side by side' format.
- *appropriately-hedged*: The response reproduces truncated tool summaries (e.g., Article 14 ends with 'in particular where suc') without indicating that the text is incomplete, and fails to note that Article 13 was not returned by the tool.
- *usable*: A professional cannot act on this response because it lacks Article 13 and presents a disorganized list of unrelated articles instead of a side-by-side checklist for the requested articles.

**Theme (Carlos fills in):** _____

---

## CQ-17 (compound)

**Query:** Which frameworks apply to credit scoring, and which model would you trust for reviewing them?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks both which frameworks apply to credit scoring and which model to trust for reviewing them; the response only lists Colorado frameworks and omits any answer about a model.
- *appropriately-hedged*: The response presents the Colorado frameworks as the full answer without acknowledging that the tool only queried Colorado, and it does not mention that the model data (o3) was available but not used, leaving the second part of the question unaddressed.
- *usable*: A professional cannot act on this response because the model recommendation is missing entirely, requiring a follow-up question to complete the answer.

**Theme (Carlos fills in):** _____

---

## CQ-18 (compound)

**Query:** Compare Colorado, New York, and Illinois on AI enforcement and rank them by how far along each is.

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

{
  "models": [
    {
      "model_id": "gpt-4o",
      "model_name": "GPT-4o (OpenAI)",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    },
    {
      "model_id": "o3",
      "model_name": "OpenAI o3",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    }
  ],
  "categories": {
    "art9_risk_management": {
      "name": "Article 9: Risk Management System",
      "results": [
        {
          "model_id": "gpt-4o",
          "avg_compliance_score": 3.0,
          "avg_plausibility_score": 4.25,
          "accuracy": 0.688,
          "hallucination_rate": 1.062,
          "scenario": "Scenario A"
        },
        {
          "model_id": "o3",
          "avg_compliance_score": 2.375,
          "avg_plausibility_score": 4.0,
          "accuracy": 0.844,
          "hallucination_rate": 1.0,
          "scenario": "Scenario A"
        }
      ]
    },
    "art10_data_governance": {
      "n

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for comparison and ranking of Colorado, New York, and Illinois, but the response only covers Colorado and does not address New York or Illinois at all.
- *appropriately-hedged*: The response does not acknowledge that it lacks information on New York and Illinois, nor does it flag that the comparison and ranking cannot be provided.
- *usable*: A professional cannot act on this response to compare and rank the three states because it only provides data on Colorado and irrelevant model comparison data.

**Theme (Carlos fills in):** _____

---

## CQ-19 (compound)

**Query:** What does EU AI Act Article 52 require, and does any US state have a comparable transparency rule?

**Response:**
```
Error: Article 52 not found. Available: 9, 10, 12, 14, 15.

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for Article 52's requirements and a US state comparison, but the response neither explains Article 52 (the tool call failed) nor addresses US states.
- *appropriately-hedged*: The response does not acknowledge the gap from the missing Article 52 information or the unanswered US state question, instead presenting unrelated data without qualification.
- *usable*: A professional cannot act on this response because it fails to answer either part of the query, requiring a follow-up question.

**Theme (Carlos fills in):** _____

---

## CQ-20 (compound)

**Query:** Summarize benchmark performance across all models and call out the single biggest weakness.

**Response:**
```
Error invoking tool 'list_all_models' with kwargs {} with error:
 input: Field required
 Please fix the error and try again.
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for a summary across all models and identification of the biggest weakness, but the response only outputs an error message and provides none of the requested information.
- *appropriately-hedged*: The response does not acknowledge the partial data (only o3 results were obtained) or the failure to retrieve all models; it simply outputs the raw error without any hedging or explanation.
- *usable*: A professional cannot act on this response because it contains no analysis or summary, only an error message that requires a follow-up to obtain the requested information.

**Theme (Carlos fills in):** _____

---

## CQ-21 (compound)

**Query:** What are the EU AI Act's high-risk obligations, and which one is most often failed according to the benchmark?

**Response:**
```
**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The response lists high-risk obligations but does not address the second part of the query—which obligation is most often failed according to the benchmark—and no benchmark data is present in the tool results.
- *appropriately-hedged*: The response asserts the obligations without any hedge or acknowledgment that the benchmark failure data is unavailable, leaving the second part of the query unanswered.
- *usable*: A professional cannot act on this response because the critical information about which obligation is most often failed is missing, requiring a follow-up question.

**Theme (Carlos fills in):** _____

---

## CQ-22 (compound)

**Query:** List the AI insurance rules by state and note which state a national insurer should worry about first.

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for AI insurance rules 'by state' and which state to worry about first, but the response only covers Colorado and does not list any other states or identify a priority state.
- *appropriately-hedged*: The response presents Colorado's rules as if they are the complete answer without acknowledging that only one state was queried and no information was retrieved for any other state.
- *usable*: A professional acting on this response would have no information about other states' rules and no guidance on which state to prioritize, requiring a follow-up question to obtain the missing data.

**Theme (Carlos fills in):** _____

---

## CQ-23 (compound)

**Query:** Give me Colorado's algorithmic-discrimination rule and the EU AI Act's closest equivalent article.

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for 'the EU AI Act's closest equivalent article' to Colorado's algorithmic-discrimination rule, but the response merely lists multiple EU AI Act articles without identifying which one is the closest equivalent, leaving the second part of the question unanswered.
- *appropriately-hedged*: The tool results do not indicate which EU AI Act article is the closest equivalent to Colorado's rule, yet the response asserts a list of articles without acknowledging that the specific equivalence requested is not directly supported by the data.
- *usable*: A professional would need to ask a follow-up question to determine which EU AI Act article is the closest equivalent to Colorado's algorithmic-discrimination rule, because the response does not provide that identification.

**Theme (Carlos fills in):** _____

---

## CQ-25 (compound)

**Query:** Summarize what New York and the EU each require for AI in financial services and flag the biggest gap between them.

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The response covers only New York and omits the EU requirements and the gap analysis requested.
- *appropriately-hedged*: The response does not acknowledge that no EU data was retrieved, leaving the EU part unaddressed.
- *usable*: A professional would need to follow up for the EU requirements and gap, so the response is not actionable alone.

**Theme (Carlos fills in):** _____

---

## H-06 (hedge)

**Query:** Is my chatbot definitely exempt from the EU AI Act?

**Response:**
```
**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked whether their chatbot is definitely exempt from the EU AI Act, but the response does not address that question at all; it merely lists regulations without answering yes/no or providing analysis.
- *appropriately-hedged*: The response fails to acknowledge that the tool data does not directly answer the exemption question and makes no attempt to hedge or qualify the lack of a definitive answer.
- *usable*: A professional would need to ask a follow-up question to get an actual answer about exemption, as the response provides no actionable conclusion.

**Theme (Carlos fills in):** _____

---

## H-07 (hedge)

**Query:** Will Colorado's AI act survive a court challenge?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked whether Colorado's AI act will survive a court challenge, but the response merely recites the two regulations' details without any analysis or prediction regarding court challenges.
- *appropriately-hedged*: The tool results contain no information about court challenges, yet the response does not acknowledge this gap or hedge its claims; it simply presents the data as if it answers the question.
- *usable*: A professional cannot act on this response because it does not address the core question about court challenge survivability, requiring a follow-up to obtain the needed analysis.

**Theme (Carlos fills in):** _____

---

## H-10 (hedge)

**Query:** Is the NAIC bulletin legally binding on insurers?

**Response:**
```
**California NAIC AI Model Bulletin Adoption** (California)
Status: adopted | Sector: insurance | Effective: 2024-12-15
California adopted the NAIC Model Bulletin on insurers' use of AI, joining the 12-state NAIC AI Systems Evaluation Tool pilot. Requires insurer governance framework, risk management controls, and third-party vendor oversight for AI systems used in insurance practices.

**Maryland NAIC AI Model Bulletin Adoption** (Maryland)
Status: adopted | Sector: insurance | Effective: 2025-03-01
Maryland adopted the NAIC Model Bulletin on insurers' use of AI and participates in the 12-state NAIC AI Systems Evaluation Tool pilot. Requires written governance, testing for bias, and documentation of AI systems used in underwriting and pricing.

**Virginia NAIC AI Model Bulletin Adoption** (Virginia)
Status: adopted | Sector: insurance | Effective: 2024-11-01
Virginia adopted the NAIC Model Bulletin on AI use in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, risk assessment, and oversight of AI systems in insurance underwriting and pricing decisions.

**Connecticut NAIC AI Model Bulletin Adoption** (Connecticut)
Status: adopted | Sector: insurance | Effective: 2025-01-01
Connecticut adopted the NAIC Model Bulletin and participates in the 12-state NAIC AI Systems Evaluation Tool pilot (January–September 2026). Requires insurer AI governance, third-party model oversight, and bias testing.

**Pennsylvania NAIC AI Model Bulletin Adoption** (Pennsylvania)
Status: adopted | Sector: insurance | Effective: 2024-10-01
Pennsylvania adopted the NAIC Model Bulletin on AI use in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance framework and risk management for AI systems used in underwriting, pricing, and claims.

**Louisiana NAIC AI Model Bulletin Adoption** (Louisiana)
Status: adopted | Sector: insurance | Effective: 2024-12-01
Louisiana adopted the NAIC Model Bulletin on insurers' use of AI. Participates in the 12-state NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and bias testing for AI systems in insurance.

**Wisconsin NAIC AI Model Bulletin Adoption** (Wisconsin)
Status: adopted | Sector: insurance | Effective: 2025-02-01
Wisconsin adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires insurer governance framework, risk management, and third-party oversight for AI in insurance.

**Florida NAIC AI Model Bulletin Adoption** (Florida)
Status: adopted | Sector: insurance | Effective: 2024-09-01
Florida adopted the NAIC Model Bulletin on AI in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance and risk management framework for AI systems used by insurers.

**Rhode Island NAIC AI Model Bulletin Adoption** (Rhode Island)
Status: adopted | Sector: insurance | Effective: 2025-01-15
Rhode Island adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and oversight of AI systems in insurance.

**Iowa NAIC AI Model Bulletin Adoption** (Iowa)
Status: adopted | Sector: insurance | Effective: 2025-03-15
Iowa adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance and risk management framework for AI systems used in insurance underwriting and pricing.

**Vermont NAIC AI Model Bulletin Adoption** (Vermont)
Status: adopted | Sector: insurance | Effective: 2025-02-15
Vermont adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and bias testing for AI systems in insurance.

**NAIC AI Systems Evaluation Tool Pilot** (Multi-State)
Status: pending | Sector: insurance | Effective: 2026-01-01
12-state pilot (Colorado, Maryland, Louisiana, Virginia, Connecticut, Pennsylvania, Wisconsin, Florida, Rhode Island, Iowa, Vermont, California) running January–September 2026. Tests a standardized evaluation framework for AI systems used by insurers. Pilot outcomes will inform potential national adoption.

**Texas NAIC AI Model Bulletin Adoption** (Texas)
Status: adopted | Sector: insurance | Effective: 2025-06-01
Texas adopted the NAIC Model Bulletin on insurers' use of AI. Requires governance framework, risk management, and documentation of AI systems in insurance underwriting and pricing. Not part of the 12-state evaluation tool pilot.

**Illinois NAIC AI Model Bulletin Adoption** (Illinois)
Status: adopted | Sector: insurance | Effective: 2025-04-01
Illinois adopted the NAIC Model Bulletin on AI in insurance. Requires governance, documentation, and third-party oversight for AI systems. Not part of the 12-state evaluation tool pilot.

**NAIC Model Bulletin on AI (Base Model)** (Federal)
Status: adopted | Sector: insurance | Effective: 2023-12-04
The NAIC's model bulletin providing guidance to insurers on the use of AI systems. Requires a governance framework, risk management controls, and third-party vendor oversight. Over 20 states have adopted or are in the process of adopting this bulletin. This is the baseline against which state-specific frameworks like NY's Circular Letter 7 and Colorado's insurance regs are measured.

**New Jersey NAIC AI Model Bulletin Adoption** (New Jersey)
Status: adopted | Sector: insurance | Effective: 2025-05-01
New Jersey adopted the NAIC Model Bulletin on AI use in insurance. Requires governance, documentation, and bias testing for AI systems in insurance underwriting and pricing.

**Ohio NAIC AI Model Bulletin Adoption** (Ohio)
Status: adopted | Sector: insurance | Effective: 2025-07-01
Ohio adopted the NAIC Model Bulletin on insurers' use of AI. Requires governance framework and risk management for AI systems in insurance. Not part of the 12-state evaluation tool pilot.

**Sources:**
- California NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Maryland NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Virginia NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Connecticut NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Pennsylvania NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Louisiana NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Wisconsin NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Florida NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Rhode Island NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Iowa NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Vermont NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- NAIC AI Systems Evaluation Tool Pilot: https://content.naic.org/insurance-topics/artificial-intelligence
- Texas NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Illinois NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- NAIC Model Bulletin on AI (Base Model): https://content.naic.org/insurance-topics/artificial-intelligence
- New Jersey NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Ohio NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
```

**Judge reasons (failed criteria):**
- *complete*: The user asked whether the NAIC bulletin is legally binding on insurers, but the response merely lists state adoptions without ever stating that the bulletin itself is a non-binding model that becomes binding only upon state adoption.
- *appropriately-hedged*: The response presents the adoptions as straightforward facts and fails to hedge or note that the NAIC bulletin is not inherently binding and that its legal force depends on each state's legislative or regulatory action.
- *usable*: A professional reading this would still not know whether the NAIC bulletin is legally binding and would need to ask a follow-up question to get a direct answer.

**Theme (Carlos fills in):** _____

---

## H-11 (hedge)

**Query:** Can I assume the EU AI Act rules also apply in the UK?

**Response:**
```
**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked whether the EU AI Act rules also apply in the UK, but the response only lists EU regulations and never addresses UK applicability or the lack thereof.
- *appropriately-hedged*: The tool results contain no information about the UK, yet the response does not acknowledge this gap or hedge the answer; it simply presents EU data as if it were a direct answer to the question.
- *usable*: A professional cannot act on this response because it does not answer the core question about UK applicability, requiring a follow-up to determine whether the EU AI Act applies there.

**Theme (Carlos fills in):** _____

---

## H-12 (hedge)

**Query:** Which single model should every compliance team use, no caveats?

**Response:**
```
(empty)
```

**Judge reasons (failed criteria):**
- *complete*: The response does not answer the user's question at all; it is empty.
- *appropriately-hedged*: The response is empty and does not acknowledge the partial or ambiguous nature of the tool output.
- *usable*: An empty response provides no actionable information for a professional.

**Theme (Carlos fills in):** _____

---

## H-14 (hedge)

**Query:** Is Illinois stricter than New York on AI in insurance?

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The response does not address the Illinois part of the comparative question, providing only New York information.
- *appropriately-hedged*: The response fails to mention that it lacks Illinois data or that the comparison cannot be made based on available information.
- *usable*: A professional would need to follow up with Illinois information to make the intended comparison.

**Theme (Carlos fills in):** _____

---

## H-15 (hedge)

**Query:** Will the EU AI Act penalties actually be enforced against small vendors?

**Response:**
```
**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks whether penalties will actually be enforced against small vendors, but the response merely lists regulations without any analysis or answer to that question.
- *appropriately-hedged*: The response does not address the ambiguity or partiality of the tool data regarding enforcement likelihood; it simply dumps the data without acknowledging that the question remains unanswered.
- *usable*: A professional cannot act on this response because it provides no conclusion or actionable insight about enforcement against small vendors, requiring a follow-up question.

**Theme (Carlos fills in):** _____

---

## H-16 (hedge)

**Query:** Based on your data, is there definitely no federal US AI law yet?

**Response:**
```
**Interagency Model Risk Management Guidance (SR 11-7 Replacement)** (Federal)
Status: adopted | Sector: lending-fintech | Effective: 2026-04-01
The OCC, Federal Reserve, and FDIC jointly replaced the 2011 SR 11-7 model-risk guidance with updated guidance covering AI/ML models. Requires model risk management, validation, and governance for AI systems used in credit decisions. Addresses governance of third-party AI models and adverse-action notice requirements.

**CFPB Adverse-Action / ECOA Guidance for AI** (Federal)
Status: adopted | Sector: lending-fintech | Effective: 2026-04-15
CFPB guidance requiring lenders using AI for credit decisions to provide specific, accurate adverse-action notices. The 'no black-box' rule survived CFPB's April 2026 narrowing of disparate-impact enforcement. Lenders must explain the principal reasons for denial even when AI models produce complex, non-linear decision paths.

**NAIC Model Bulletin on AI (Base Model)** (Federal)
Status: adopted | Sector: insurance | Effective: 2023-12-04
The NAIC's model bulletin providing guidance to insurers on the use of AI systems. Requires a governance framework, risk management controls, and third-party vendor oversight. Over 20 states have adopted or are in the process of adopting this bulletin. This is the baseline against which state-specific frameworks like NY's Circular Letter 7 and Colorado's insurance regs are measured.

**Sources:**
- Interagency Model Risk Management Guidance (SR 11-7 Replacement): https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/
- CFPB Adverse-Action / ECOA Guidance for AI: https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/
- NAIC Model Bulletin on AI (Base Model): https://content.naic.org/insurance-topics/artificial-intelligence
```

**Judge reasons (failed criteria):**
- *complete*: The user asked whether there is definitely no federal US AI law yet, but the response only lists three guidance documents without explicitly answering the yes/no question.
- *appropriately-hedged*: The response does not address the distinction between guidance and law, nor does it hedge about whether these items constitute a 'law'; it presents them as facts without acknowledging the user's implied question.
- *usable*: A professional reading this response would still need to ask whether any of these items count as a federal AI law, so the response is not actionable without a follow-up.

**Theme (Carlos fills in):** _____

---

## H-18 (hedge)

**Query:** Is Article 9 the most important part of the EU AI Act?

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked whether Article 9 is the most important part of the EU AI Act, but the response merely lists tool results without any analysis or answer to that question.
- *appropriately-hedged*: The tool output contains no information about which article is 'most important', yet the response does not acknowledge this limitation or hedge its non-answer; it simply presents data as if it were a direct answer.
- *usable*: A professional cannot act on this response because it does not address the user's question about the importance of Article 9, providing only a raw dump of unrelated article summaries.

**Theme (Carlos fills in):** _____

---

## H-19 (hedge)

**Query:** Does Colorado's law cover generative AI specifically?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The query asks whether Colorado's law covers generative AI specifically, but the response only lists the two laws without addressing whether generative AI falls under their scope.
- *appropriately-hedged*: The tool output is silent on generative AI, yet the response does not acknowledge this uncertainty or qualify its answer; it simply presents the laws without addressing the specific question.
- *usable*: A professional reading this response would still not know whether Colorado's law covers generative AI, so they would need to ask a follow-up question.

**Theme (Carlos fills in):** _____

---

## H-20 (hedge)

**Query:** How sure are you these benchmark scores reflect real-world compliance accuracy?

**Response:**
```
(empty)
```

**Judge reasons (failed criteria):**
- *complete*: The response does not answer the user's question about certainty of benchmark scores reflecting real-world compliance accuracy.
- *appropriately-hedged*: The response does not address the significant uncertainty indicated by the tool results (e.g., hallucination_rate=1.0) and provides no hedging.
- *usable*: The response is empty and provides no actionable information; a professional would need a follow-up.

**Theme (Carlos fills in):** _____

---

## H-22 (hedge)

**Query:** Do all EU member states enforce the AI Act the same way?

**Response:**
```
**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The question asks whether all EU member states enforce the AI Act the same way, but the response only lists EU-level regulations and does not address member-state enforcement or variation.
- *appropriately-hedged*: The response does not acknowledge that the tool results contain no information about member-state enforcement differences, nor does it hedge the lack of an answer to the query.
- *usable*: A professional asking about enforcement uniformity would not receive an answer and would need to ask a follow-up question to get the relevant information.

**Theme (Carlos fills in):** _____

---

## H-23 (hedge)

**Query:** Will following the NAIC bulletin keep me compliant in every state?

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

**California NAIC AI Model Bulletin Adoption** (California)
Status: adopted | Sector: insurance | Effective: 2024-12-15
California adopted the NAIC Model Bulletin on insurers' use of AI, joining the 12-state NAIC AI Systems Evaluation Tool pilot. Requires insurer governance framework, risk management controls, and third-party vendor oversight for AI systems used in insurance practices.

**Maryland NAIC AI Model Bulletin Adoption** (Maryland)
Status: adopted | Sector: insurance | Effective: 2025-03-01
Maryland adopted the NAIC Model Bulletin on insurers' use of AI and participates in the 12-state NAIC AI Systems Evaluation Tool pilot. Requires written governance, testing for bias, and documentation of AI systems used in underwriting and pricing.

**Virginia NAIC AI Model Bulletin Adoption** (Virginia)
Status: adopted | Sector: insurance | Effective: 2024-11-01
Virginia adopted the NAIC Model Bulletin on AI use in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, risk assessment, and oversight of AI systems in insurance underwriting and pricing decisions.

**Connecticut NAIC AI Model Bulletin Adoption** (Connecticut)
Status: adopted | Sector: insurance | Effective: 2025-01-01
Connecticut adopted the NAIC Model Bulletin and participates in the 12-state NAIC AI Systems Evaluation Tool pilot (January–September 2026). Requires insurer AI governance, third-party model oversight, and bias testing.

**Pennsylvania NAIC AI Model Bulletin Adoption** (Pennsylvania)
Status: adopted | Sector: insurance | Effective: 2024-10-01
Pennsylvania adopted the NAIC Model Bulletin on AI use in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance framework and risk management for AI systems used in underwriting, pricing, and claims.

**Louisiana NAIC AI Model Bulletin Adoption** (Louisiana)
Status: adopted | Sector: insurance | Effective: 2024-12-01
Louisiana adopted the NAIC Model Bulletin on insurers' use of AI. Participates in the 12-state NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and bias testing for AI systems in insurance.

**Wisconsin NAIC AI Model Bulletin Adoption** (Wisconsin)
Status: adopted | Sector: insurance | Effective: 2025-02-01
Wisconsin adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires insurer governance framework, risk management, and third-party oversight for AI in insurance.

**Florida NAIC AI Model Bulletin Adoption** (Florida)
Status: adopted | Sector: insurance | Effective: 2024-09-01
Florida adopted the NAIC Model Bulletin on AI in insurance. Participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance and risk management framework for AI systems used by insurers.

**Rhode Island NAIC AI Model Bulletin Adoption** (Rhode Island)
Status: adopted | Sector: insurance | Effective: 2025-01-15
Rhode Island adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and oversight of AI systems in insurance.

**Iowa NAIC AI Model Bulletin Adoption** (Iowa)
Status: adopted | Sector: insurance | Effective: 2025-03-15
Iowa adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance and risk management framework for AI systems used in insurance underwriting and pricing.

**Vermont NAIC AI Model Bulletin Adoption** (Vermont)
Status: adopted | Sector: insurance | Effective: 2025-02-15
Vermont adopted the NAIC Model Bulletin and participates in the NAIC AI Systems Evaluation Tool pilot. Requires governance, documentation, and bias testing for AI systems in insurance.

**NAIC AI Systems Evaluation Tool Pilot** (Multi-State)
Status: pending | Sector: insurance | Effective: 2026-01-01
12-state pilot (Colorado, Maryland, Louisiana, Virginia, Connecticut, Pennsylvania, Wisconsin, Florida, Rhode Island, Iowa, Vermont, California) running January–September 2026. Tests a standardized evaluation framework for AI systems used by insurers. Pilot outcomes will inform potential national adoption.

**Texas NAIC AI Model Bulletin Adoption** (Texas)
Status: adopted | Sector: insurance | Effective: 2025-06-01
Texas adopted the NAIC Model Bulletin on insurers' use of AI. Requires governance framework, risk management, and documentation of AI systems in insurance underwriting and pricing. Not part of the 12-state evaluation tool pilot.

**Illinois NAIC AI Model Bulletin Adoption** (Illinois)
Status: adopted | Sector: insurance | Effective: 2025-04-01
Illinois adopted the NAIC Model Bulletin on AI in insurance. Requires governance, documentation, and third-party oversight for AI systems. Not part of the 12-state evaluation tool pilot.

**NAIC Model Bulletin on AI (Base Model)** (Federal)
Status: adopted | Sector: insurance | Effective: 2023-12-04
The NAIC's model bulletin providing guidance to insurers on the use of AI systems. Requires a governance framework, risk management controls, and third-party vendor oversight. Over 20 states have adopted or are in the process of adopting this bulletin. This is the baseline against which state-specific frameworks like NY's Circular Letter 7 and Colorado's insurance regs are measured.

**New Jersey NAIC AI Model Bulletin Adoption** (New Jersey)
Status: adopted | Sector: insurance | Effective: 2025-05-01
New Jersey adopted the NAIC Model Bulletin on AI use in insurance. Requires governance, documentation, and bias testing for AI systems in insurance underwriting and pricing.

**Ohio NAIC AI Model Bulletin Adoption** (Ohio)
Status: adopted | Sector: insurance | Effective: 2025-07-01
Ohio adopted the NAIC Model Bulletin on insurers' use of AI. Requires governance framework and risk management for AI systems in insurance. Not part of the 12-state evaluation tool pilot.

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
- California NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Maryland NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Virginia NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Connecticut NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Pennsylvania NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Louisiana NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Wisconsin NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Florida NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Rhode Island NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Iowa NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Vermont NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- NAIC AI Systems Evaluation Tool Pilot: https://content.naic.org/insurance-topics/artificial-intelligence
- Texas NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Illinois NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- NAIC Model Bulletin on AI (Base Model): https://content.naic.org/insurance-topics/artificial-intelligence
- New Jersey NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
- Ohio NAIC AI Model Bulletin Adoption: https://content.naic.org/sites/default/files/cmte-h-big-data-artificial-intelligence-wg-map-ai-model-bulletin.pdf
```

**Judge reasons (failed criteria):**
- *complete*: The response does not answer the user's question about whether following the NAIC bulletin ensures compliance in every state; it merely lists regulations without analysis or conclusion.
- *appropriately-hedged*: The response does not hedge that the tool results are incomplete for the query (e.g., Colorado's non-insurance AI law is not covered by the NAIC bulletin) and presents the information as if it were the answer.
- *usable*: A professional cannot act on this response without a follow-up question because it fails to answer the yes/no query and provides no actionable guidance.

**Theme (Carlos fills in):** _____

---

## H-24 (hedge)

**Query:** Is New York's credit-scoring rule the toughest in the country?

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The query asks whether New York's credit-scoring rule is the toughest in the country, but the response only describes an AI/insurance regulation and does not address credit scoring or compare it to other states.
- *appropriately-hedged*: The tool result does not mention credit scoring, yet the response presents the regulation without acknowledging that it does not answer the question about credit-scoring rules.
- *usable*: A professional cannot act on this response because it fails to answer the core question about credit-scoring toughness, requiring a follow-up query.

**Theme (Carlos fills in):** _____

---

## U-06 (usability)

**Query:** Draft one sentence I can put in a board deck about our EU AI Act Article 9 exposure.

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked for a single sentence about Article 9 exposure, but the response provided a full dump of multiple articles and no synthesized sentence, failing to address the request.
- *appropriately-hedged*: The response copies the truncated Article 9 summary ending with 'to ' without indicating it is incomplete, and while the Digital Omnibus proposal is hedged as 'proposed' and 'not yet law', the overall presentation of raw data without qualification on the truncation is not appropriately hedged.
- *usable*: A professional would need to ask for the requested single sentence because the response only provides raw data and no synthesized board-deck sentence.

**Theme (Carlos fills in):** _____

---

## U-09 (usability)

**Query:** Which model should we pick for an Article 10 review? Just give me the name and one reason.

**Response:**
```
**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**Sources:**
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked for a model name and one reason for an Article 10 review, but the response only provides Article 10 information and does not recommend any model.
- *appropriately-hedged*: The response does not address the model selection at all, so it fails to hedge or acknowledge the partiality of the tool output regarding which model to pick.
- *usable*: A professional cannot act on this response to select a model for an Article 10 review because no model recommendation is given.

**Theme (Carlos fills in):** _____

---

## U-11 (usability)

**Query:** Give me the EU AI Act Article 13 obligations as a numbered list I can paste into a ticket.

**Response:**
```
Error: Article 13 not found. Available: 9, 10, 12, 14, 15.

**EU AI Act Annex III (High-Risk AI Systems)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
EU AI Act Annex III classifies AI systems used for credit scoring and life/health insurance risk-pricing as high-risk. Obligations include risk management, data governance, technical documentation, human oversight, and conformity assessment. Enforcement date is August 2, 2026, but a pending Digital Omnibus proposal (agreed May 7, 2026, not yet law) could defer this to December 2, 2027.

**EU AI Act Article 99 (Penalties)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
Three penalty tiers: Tier 1 (prohibited practices) up to €35M or 7% of global annual turnover; Tier 2 (provider/deployer obligations) up to €15M or 3% of turnover; Tier 3 (misleading information) up to €7.5M or 1% of turnover. SMEs/startups pay the lower of percentage or fixed amount. Compliance costs estimated at €50,000–€500,000 for SMEs depending on use-case complexity.

**Digital Omnibus Deferral Proposal** (EU)
Status: proposed | Sector: both | Effective: 2027-12-02
Proposed deferral of the EU AI Act Annex III enforcement date from August 2, 2026 to December 2, 2027. Agreed in principle on May 7, 2026 but not yet enacted into law as of June 2026. If passed, gives covered entities additional time to comply with high-risk AI system obligations for credit scoring and insurance risk-pricing.

**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**EU AI Act Article 10** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used. 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the 

**EU AI Act Article 12 (1-2)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system. 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modificat

**EU AI Act Article 14 (1-4)** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where suc

**EU AI Act Article 15** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. 2. To address the technical aspects of how to measure the appropriate levels of accuracy and robustness set out in paragraph 1 and any other relevant performance metrics, the Commission shall, in cooperation with relevant stakeholders and organisations such as metro

**Sources:**
- EU AI Act Annex III (High-Risk AI Systems): https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 99 (Penalties): https://artificialintelligenceact.eu/article/99/
- Digital Omnibus Deferral Proposal: https://artificialintelligenceact.eu/annex/3/
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
- EU AI Act Article 10: https://artificialintelligenceact.eu/article/10/
- EU AI Act Article 12 (1-2): https://artificialintelligenceact.eu/article/12/
- EU AI Act Article 14 (1-4): https://artificialintelligenceact.eu/article/14/
- EU AI Act Article 15: https://artificialintelligenceact.eu/article/15/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked for a numbered list of Article 13 obligations, but the response only reports that Article 13 was not found and then dumps unrelated articles without addressing the request.
- *appropriately-hedged*: The response does not hedge or clarify that it is not providing the requested Article 13 obligations; it simply shows an error and then unrelated content, which could mislead the user.
- *usable*: A professional cannot act on this response because it does not contain the requested numbered list of Article 13 obligations, requiring a follow-up question.

**Theme (Carlos fills in):** _____

---

## U-12 (usability)

**Query:** What's the fastest compliant path to ship an AI credit tool in New York? One paragraph.

**Response:**
```
**NYDFS Circular Letter No. 7 (2024)** (New York)
Status: adopted | Sector: insurance | Effective: 2024-07-11
NYDFS guidance on use of AI and external data in underwriting and pricing of insurance. Requires insurer governance, risk management, and disclosure of AI use. Mandates that external data and AI models not result in unfair discrimination. Insurers must maintain documentation of data sources, models, and testing for bias.

**Sources:**
- NYDFS Circular Letter No. 7 (2024): https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
```

**Judge reasons (failed criteria):**
- *complete*: The query asks for the fastest compliant path to ship an AI credit tool, but the response only describes an insurance underwriting regulation and does not address credit tools or provide any path.
- *appropriately-hedged*: The response presents the insurance regulation as the answer without acknowledging that the tool result is about insurance, not credit, and does not hedge about the mismatch or the lack of a direct answer.
- *usable*: A professional cannot act on this response to ship an AI credit tool because it provides no actionable path, only an irrelevant regulation summary.

**Theme (Carlos fills in):** _____

---

## U-13 (usability)

**Query:** Give me a yes/no with one caveat: can we use GPT-4o for Article 9 work?

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
```

**Judge reasons (failed criteria):**
- *complete*: The user asked for a yes/no with one caveat about using GPT-4o for Article 9 work, but the response only recites the article text and never addresses whether GPT-4o can be used, leaving the core question unanswered.
- *appropriately-hedged*: The response makes no attempt to hedge or qualify any answer because it does not provide any answer to the user's question; it simply states the article content without acknowledging the missing judgment.
- *usable*: A professional cannot act on this response because it fails to give the requested yes/no and caveat, requiring a follow-up question to obtain the actual answer.

**Theme (Carlos fills in):** _____

---

## U-14 (usability)

**Query:** Summarize Colorado vs. New York AI rules in a two-row table I can screenshot.

**Response:**
```
**Colorado SB 26-189 (Automated Decision-Making Technology)** (Colorado)
Status: adopted | Sector: lending-fintech | Effective: 2027-01-01
Colorado's rewritten AI law replaces the broader SB 24-205 with a narrowed scope focused on automated decision-making in consequential decisions including credit scoring. Enforced via the state Consumer Protection Act as a deceptive trade practice, with AG enforcement and a 60-day cure notice before Jan 1, 2030. Requires disclosure of AI use and risk assessments for high-risk automated decisions.

**Colorado SB 24-205 (Original AI Act, repealed)** (Colorado)
Status: repealed-and-replaced | Sector: lending-fintech | Effective: 2025-02-01
Colorado's original comprehensive AI Act, effective February 2025. Replaced by SB 26-189 in May 2026 with substantially narrowed scope. Many secondary sources still reference this version. Required algorithmic impact assessments and anti-discrimination provisions for high-risk AI systems.

{
  "models": [
    {
      "model_id": "gpt-4o",
      "model_name": "GPT-4o (OpenAI)",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    },
    {
      "model_id": "o3",
      "model_name": "OpenAI o3",
      "provider": "OpenAI",
      "context_window": "unknown",
      "release_date": "unknown"
    }
  ],
  "categories": {
    "art9_risk_management": {
      "name": "Article 9: Risk Management System",
      "results": [
        {
          "model_id": "gpt-4o",
          "avg_compliance_score": 3.0,
          "avg_plausibility_score": 4.25,
          "accuracy": 0.688,
          "hallucination_rate": 1.062,
          "scenario": "Scenario A"
        },
        {
          "model_id": "o3",
          "avg_compliance_score": 2.375,
          "avg_plausibility_score": 4.0,
          "accuracy": 0.844,
          "hallucination_rate": 1.0,
          "scenario": "Scenario A"
        }
      ]
    },
    "art10_data_governance": {
      "n

**Sources:**
- Colorado SB 26-189 (Automated Decision-Making Technology): https://www.consumerfinancialserviceslawmonitor.com/2026/05/colorado-rewrites-its-ai-law/
- Colorado SB 24-205 (Original AI Act, repealed): https://finsights.cooley.com/the-new-colorado-ai-act-what-financial-institutions-need-to-know/
```

**Judge reasons (failed criteria):**
- *complete*: The response does not address New York AI rules at all, nor does it provide the requested two-row table for comparison.
- *appropriately-hedged*: The response fails to acknowledge that no New York data was retrieved and presents irrelevant model comparison data without any qualification about the missing jurisdiction.
- *usable*: A professional cannot screenshot a two-row table from this response, and the missing New York information makes it unusable for the requested comparison.

**Theme (Carlos fills in):** _____

---

## U-21 (usability)

**Query:** What's the headline number I should quote about our top model's compliance performance?

**Response:**
```
(empty)
```

**Judge reasons (failed criteria):**
- *complete*: The user asked for a headline number about compliance performance, but the response provided no number or information.
- *appropriately-hedged*: The response does not address the data at all, failing to hedge or acknowledge any ambiguity in the tool output.
- *usable*: An empty response cannot be acted upon by a professional; it provides no actionable information.

**Theme (Carlos fills in):** _____

---

## U-24 (usability)

**Query:** Give me a one-line risk rating (low/medium/high) for using the lowest-scoring model on Article 9.

**Response:**
```
**EU AI Act Article 9** (EU)
Status: adopted | Sector: both | Effective: 2026-08-02
1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems. 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to 

**Sources:**
- EU AI Act Article 9: https://artificialintelligenceact.eu/article/9/
```

**Judge reasons (failed criteria):**
- *complete*: The query asked for a risk rating for the lowest-scoring model on Article 9, but the response does not provide any rating or mention the model data.
- *appropriately-hedged*: The response does not address the query, so it fails to hedge any uncertainty about the model's performance or the risk rating.
- *usable*: A professional would need to follow up because the response does not contain the requested risk rating.

**Theme (Carlos fills in):** _____

---
