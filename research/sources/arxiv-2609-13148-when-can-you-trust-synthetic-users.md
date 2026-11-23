---
title: "When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels"
source_url: https://arxiv.org/abs/2609.13148
author: Robson Tigre and Hugo Gobato Souto
publisher: arXiv
published: 2026-06-03
retrieved: 2026-11-22
type: paper
evidence: independent
filed_by: research-future-of-product
themes: [synthetic-users-limits]
relevance: high
---

## Relevance to the project
Gives a statistical framework for when a synthetic panel can be trusted, corrected or abandoned. Its conditions (a complete invitation frame, human outcomes for respondents, missing-at-random) mean synthetic respondents are an auxiliary to a real sample, not a replacement. This defines the bar for using simulation on desirability, and why it is weaker than simulation of system behaviour.

## Themes
- synthetic-users-limits: agreement on aggregates can hide subgroup error; correction fails when nonresponse depends on unobserved human outcomes (coverage near zero)

## Key points
- Separates population mismatch (covariate shift) from conditional response differences (concept shift).
- AIPW estimator treating LLM output as auxiliary information; needs real human outcomes for respondents.
- Nominal 95% intervals covered 88-94% in some regimes; evaluation on ANES and Twin-2K-500 paired human and LLM responses.
- Validation must target the intended population and task.

## Could not verify
- Abstract-level read; v2 dated 2026-10-25. Not specific to financial products.
