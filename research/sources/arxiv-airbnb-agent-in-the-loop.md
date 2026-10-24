---
title: "Agent-in-the-Loop: A Data Flywheel for Continuous Improvement in LLM-based Customer Support"
source_url: https://arxiv.org/abs/2510.06674
author: Cen Mia Zhao, Tiantian Zhang, Hanchen Su, et al. (Airbnb)
publisher: arXiv; EMNLP 2025 Industry Track
published: 2025-10-08
retrieved: 2026-10-24
type: paper
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [org-learning-loop, human-review-gates, tacit-knowledge-capture, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Airbnb's design for learning from human support agents while they work: a copilot proposes two candidate replies, and the agent's choice, critique, rating of retrieved knowledge and flags for missing policy feed weekly model updates instead of quarterly offline labelling. It is a worked example of capturing tacit expert knowledge inside the workflow, which maps to how a PM harness might capture reviewer judgement as it happens.

## Themes
- org-learning-loop: model update cycle cut from about three months (offline baseline) to weekly (Sec. 4, Table 1).
- human-review-gates: the system is a copilot; humans choose and send replies. Human experts plus an LLM verifier audit annotations; the filter dropped 14.3% of examples before retriever training and 34.5% before generator training (Sec. 3.3, 5.2).
- tacit-knowledge-capture: step 4 lets agents flag missing policies or unrecorded best practices through a knowledge selection interface; immediate annotation helped this step most (Sec. 5.1).
- evals-autonomy-trust: human and LLM scores correlate at r > 0.90 and are averaged into a hybrid metric (App. G).

## Key points
- Pilot: 40 US support agents on an async messaging channel; more than 5,000 cases annotated, about 11 a day each; productivity comparable to non-participants (Sec. 4).
- Results vs baseline (authors' claims): retrieval recall@75 +11.7%, precision@8 +14.8%, helpfulness +8.4%, citation correctness +38.1%, adoption of suggestions +4.5%; humans preferred the new model 60% vs 33% (Sec. 4.2-4.3).
- Models: Mixtral-style 8x7B MoE generator (SFT then ORPO), E5-Mistral 7B retriever, FLAN-T5 ranker; gains repeated on Qwen2.5 and Llama 3 (App. D-E, Sec. 5.5).
- Median annotation times were 1-2 minutes per step.
- Limits: English only, short study, possible annotation fatigue (Sec. 6).

## Could not verify
- Pilot length not stated; some table figures differ from the text (e.g. Table 5 vs Sec. 4.3).
