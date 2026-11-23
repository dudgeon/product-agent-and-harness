---
title: "From Demographics to Survey Anchors: Evaluating LLM Agents for Modeling Retirement Attitudes"
source_url: https://arxiv.org/abs/2605.16303
author: arXiv authors (see source)
publisher: arXiv
published: 2026-05-01
retrieved: 2026-11-22
type: paper
evidence: independent
filed_by: research-future-of-product
themes: [synthetic-users-limits]
relevance: medium
---

## Relevance to the project
Tests LLM agents built from real survey respondents on retirement and financial-knowledge items. Adding about 175 of each person's own answers cut distance from the human distribution by about 29% but agents still compressed to the mean, missed tails and were over-accurate on financial knowledge. It shows that useful simulation of financial attitudes needs the firm's own individual-level data, and still understates extremes.

## Themes
- synthetic-users-limits: demographics-only agents collapse to population means; survey-anchored agents better but under-represent tails; risk-tolerance item is where demographics-only agents fail

## Key points
- Qwen3-14B local model, SHARE wave 9 respondents (France, Germany, Spain), 5,461 participants, 15 items; mean total variation distance 0.422 demographics-only vs 0.280 survey-anchored; better on 12 of 15 items.
- Hyper-accuracy: agents answered the compound-interest question correctly almost always, missing human errors and don't-know answers.
- Only survey-anchored agents recovered interaction effects in a replicated regression, with effect sizes still off.

## Could not verify
- Only the first half of the paper was read; one local model family, one run per item per authors.
