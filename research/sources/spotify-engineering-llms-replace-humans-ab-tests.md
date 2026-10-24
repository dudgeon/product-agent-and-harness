---
title: "When Can LLMs Replace Humans in A/B Tests?"
source_url: https://engineering.atspotify.com/2026/8/when-can-llms-replace-humans-in-a-b-tests
author: Sebastian Ankargren, Joel Persson and Mårten Schultzberg (Spotify)
publisher: Spotify Engineering blog
published: 2026-08-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [synthetic-users-limits, metrics-review-agents, ai-synthesis-hallucination-risk]
relevance: high
---

## Relevance to the project
Spotify's experimentation scientists test whether LLM predictions can stand in for users in A/B tests. Raw LLM predictions recovered only about 39% of the true human effect, and substitution only works under assumptions that are weakest exactly for novel ideas, where it would help most. This is strong first-party evidence for the limits of synthetic users, from the team behind Confidence.

## Themes
- synthetic-users-limits: on the Upworthy headline dataset, raw gpt-4o-mini predictions recovered about 39% of the human treatment effect, biased toward zero; non-linear calibration (random forest, boosted trees) got within sampling error; linear calibration failed by about 3.8 standard errors.
- metrics-review-agents: recommended uses are screening weak ideas before they take an experiment slot and using LLM outputs as covariates for variance reduction, not replacing users.
- ai-synthesis-hallucination-risk: if surrogacy or comparability fails, more LLM predictions measure the effect on the LLM, not on users.

## Key points
- Method borrows surrogate-endpoint theory from biostatistics; paper on arXiv.
- Calibration needs real user data and goes stale as models change.
- Upworthy is a best case (binary outcome, text-only treatment); layout, algorithm or pricing changes are harder.

## Notable quotes
- Human experiments are valid "by design"; LLM substitutes only "by assumption".
