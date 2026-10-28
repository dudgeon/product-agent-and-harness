---
title: "Moving Faster and Reducing Risk: Using LLMs in Release Deployment"
source_url: https://arxiv.org/abs/2410.06351
author: Rui Abreu, Vijayaraghavan Murali, Peter C. Rigby, Chandra Maddila, Weiyan Sun, Jun Ge, Kaavya Chinniah, Audris Mockus, Megh Mehta, Nachiappan Nagappan (Meta)
publisher: arXiv / ICSE-SEIP 2025
published: 2024-10-08
retrieved: 2026-10-28
type: paper
evidence: first-party
filed_by: research-dependency-agent
themes: [risk-review-as-classification, risk-sloped-review, human-review-gates]
relevance: medium
---
## Relevance to the project
Meta's Diff Risk Score predicts how likely a code change is to cause a severe incident and gates risky changes during code freezes. Gating the riskiest 5%, 10% and 50% of diffs, the production logistic regression captured 18.7%, 27.9% and 84.6% of incident-causing diffs; a risk-aligned fine-tuned LLM (iDiffLlama-13B) captured 26.2%, 42.3% and 88.5%. It shows how much (and how little) risk prediction catches at a given gating cost, and the human escape hatches that make gating tolerable.

## Themes
- risk-review-as-classification: LLM beats regression by 1.40x, 1.52x, 1.05x at weekend, yellow and red gating levels; on another organisation's diffs, 21.9/39.4/88.8% vs 11.9/26.3/84.4%.
- risk-sloped-review: four gating levels (none, weekend, yellow, red); "Diffs that are beyond a particular threshold of risk can then be gated."
- human-review-gates: developers see the score, reasons and suggested actions in the review tool; blocked diffs can wait, be revised, or be escalated to managers via standard reasons.

## Key points
- Regression model in production for more than nine months at time of writing; productivity cost of gating not measured; single company; models need retraining as data drifts; risk alignment took 2-4 hours on 64 A100s.
