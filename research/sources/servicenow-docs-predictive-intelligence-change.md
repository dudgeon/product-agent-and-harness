---
title: "Predictive Intelligence for Change Management"
source_url: https://www.servicenow.com/docs/r/MlbQAgTiiiMOLOw9T36wJg/Daxg1JRkSso6RiKaaEyoAg
author: ServiceNow
publisher: ServiceNow product documentation (Zurich release)
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [risk-review-as-classification, risk-sloped-review, human-review-gates]
relevance: medium
---
## Relevance to the project
The documented basis of "AI change auto-approval" in ServiceNow: a similarity-and-categorisation model ("Risk for proposed change") predicts change risk, and customers can then configure Change Approval Policies to auto-approve when risk is low. Auto-approval is a customer policy on top of a prediction, not a built-in AI decision; the page makes no accuracy claims and does not state training-data requirements.

## Themes
- risk-review-as-classification: two ML solution definitions: "Risk for proposed change" (similarity and categorisation) and "Standard change candidates" (clustering to propose standard templates).
- risk-sloped-review: "when risk = low, you can use Change Approval Policies to automatically approve this low risk activity."
- human-review-gates: predictions shown to itil or sn_change_write users; admins configure and must train the solutions.

## Key points
- Plugins: Change Management - Risk Intelligence (com.snc.change_management.ml.risk) and Standard Change Template Intelligence (com.snc.change_management.ml.sctp), requested via Now Support.
- No precision/recall figures; compare the ING study (arxiv-kapel-ing-change-incident-prediction) where the ITSM tool's rule-based baseline had AUC about 0.55.
