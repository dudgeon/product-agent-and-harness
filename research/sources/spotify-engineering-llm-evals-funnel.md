---
title: "Better Experiments with LLM Evals — A funnel, not a fork"
source_url: https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork
author: Matilda Ankargren and Mårten Schultzberg (Spotify)
publisher: Spotify Engineering blog
published: 2026-05-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [evals-autonomy-trust, spec-becomes-prototype-and-evals, metrics-review-agents, org-learning-loop]
relevance: medium
---

## Relevance to the project
Spotify's data scientists place offline LLM evals before online A/B tests in one "evaluation funnel": evals screen candidates and verify quality; experiments validate business outcomes. It also gives baseline experiment numbers (about 12% of tests ship a positive result; about 64% yield learning) that show how much of product work is learning rather than shipping. For an agent harness, it is a model for linking eval scores to measured outcomes.

## Themes
- evals-autonomy-trust: "without offline-online signal calibration, our evals are opinions, not evidence"; run LLM judges on A/B data to check whether judge-preferred variants won with users.
- spec-becomes-prototype-and-evals: evals run early and often to pick treatments; experiments confirm.
- metrics-review-agents: about 42% of launched experiments are rolled back to prevent secondary-metric regressions (Spotify figure, May 2026).
- org-learning-loop: a judge flagging trust-breaking recommendations surfaced patterns that became product fixes, then verified the fixes.

## Key points
- Rigor matched to decision: quick directional tests for iteration, rigorous tests for ship decisions.
- Evals struggle with long-running tasks; cites Opus 4.5 looking flat on one vendor's coding evals while improving on longer tasks.
