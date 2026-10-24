---
title: "Risk-Aware Product Decisions in A/B Tests with Multiple Metrics"
source_url: https://engineering.atspotify.com/2024/3/risk-aware-product-decisions-in-a-b-tests-with-multiple-metrics
author: Mårten Schultzberg, Sebastian Ankargren, Mattias Frånberg (Spotify)
publisher: Spotify Engineering
published: 2024-03-05
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [experiment-decision-rules, risk-review-as-classification, artifact-standardization, metrics-review-agents]
relevance: high
---

## Relevance to the project
Describes Spotify's default product-shipping decision rule, encoded in its experimentation platform (Confidence) since early 2020: ship only if at least one success metric improves, all guardrails are non-inferior, nothing deteriorates and no quality test fails. The platform then gives every treatment an automatic "shipping recommendation". For the project this is a clear case of a written-down, pre-agreed decision rule that turns measurement into a standard, explainable recommendation anyone can read, a model for how an agent could report "ship / don't ship" with reasons.

## Themes
- experiment-decision-rules (proposed): four metric types (success, guardrail, deterioration, quality) and an explicit ship rule ("Aspects that should go into a decision rule").
- risk-review-as-classification: every possible outcome maps to a decision, so the platform can give "constructive guidance on the product implication" without anyone reading individual metrics ("Decision rules help standardize and democratize").
- artifact-standardization: the rule standardises decisions so different teams don't "hold themselves to different standards"; analysis became fully automated after the 2019 platform rebuild.
- metrics-review-agents: Confidence shows a recommendation per treatment and how each part of the rule contributes ("Get access to Spotify's decision engine").

## Key points
- Decision engine first built early 2020 from studying how experimenters actually used metrics.
- Statistical findings: no false-positive correction for guardrails; but power (beta) must be corrected for the number of guardrails, or with 10 guardrails simultaneous power falls to ~11%.
- Certain critical business metrics are tested for deterioration in all experiments.
- Rule is not for every case (e.g. decisions driven by outside factors), but covers "the bulk of experiments".
- Paper: Schultzberg, Ankargren, Frånberg (2024), arXiv 2402.11609.

## Could not verify
- Full post read; formulas rendered as images were not captured.
