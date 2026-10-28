---
title: "Learning from Change: Predictive Models for Incident Prevention in a Regulated IT Environment"
source_url: https://arxiv.org/abs/2604.13462
author: Eileen Kapel, Jan Lennartz (ING Bank); Luis Cruz, Diomidis Spinellis, Arie van Deursen (TU Delft)
publisher: arXiv / ICSE-SEIP 2026
published: 2026-04-15
retrieved: 2026-10-28
type: paper
evidence: first-party
filed_by: research-dependency-agent
themes: [risk-review-as-classification, vendor-claims-vs-independent-evidence, stale-records-mislead-agents, human-review-gates]
relevance: high
---
## Relevance to the project
The best regulated-bank evidence on AI change-risk prediction: at ING, about 175,000 production changes over a year (2.4% incident-inducing) were scored by the ITSM tool's rule-based risk calculator and by gradient-boosted models. The built-in calculator barely beat chance (AUC about 0.55) and caught 56% of risky changes; LightGBM with team metrics caught 93% (weighted recall) but precision stayed at 2-5%, so the authors say outputs must be read as a risk ranking, not a gate, or they cause alert fatigue. It is a sober benchmark for any vendor claim of "AI change auto-approval" and for any agent that flags dependency risk.

## Themes
- risk-review-as-classification: test-set results: rule-based baseline precision 0.04, weighted recall 0.56, AUC 0.55; XGBoost precision 0.05, wR 0.89, AUC 0.71; LightGBM with team metrics precision 0.04, wR 0.93, wF2 0.93, AUC 0.60 (results table).
- vendor-claims-vs-independent-evidence: "The baseline risk assessment fails to effectively identify high-risk changes" (Finding 1), the out-of-the-box ITSM calculator.
- stale-records-mislead-agents: labels depend on manual linking of incidents to changes; the IT Product field is only about 50% populated and release data covers 23.1% of changes; the most influential features are free-text change descriptions, CI name, assignment group and support offering (SHAP).
- human-review-gates: designed for DORA (EU) and AI Act auditability, four-eye approval and CAB; SHAP explanations are for audit and reviewers; "Predictions should therefore not be interpreted as binary signals but as a risk-ranking mechanism" (Section 8.1).

## Key points
- Train 8 months (~120k), validate 2 months (~26k), test 2 months (~30k); sliding-window evaluation with daily retraining planned; production deployment not clearly stated.
- Single company; feature data confidential. ING staff are co-authors and the work was ING-funded, so labelled first-party.
