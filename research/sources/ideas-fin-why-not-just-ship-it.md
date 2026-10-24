---
title: "Why not just ship it?"
source_url: https://ideas.fin.ai/p/why-not-just-ship-it
author: Pedro Tabacof (Principal ML Scientist, Fin / Intercom)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-08-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [evals-autonomy-trust, human-review-gates, org-learning-loop, spec-becomes-prototype-and-evals]
relevance: high
---

## Relevance to the project
How Intercom's AI group decides which Fin changes ship: every change (a one-line prompt edit to a model swap) passes backtests on a few thousand replayed real conversations graded by LLM-judge ensembles, then a pre-registered A/B test on resolution rate with a wider scorecard, then a 0% dark launch and ramp with health checks, then judges scoring live samples. It evidences the release and operate-and-learn rows for the AI product, and the loop back: new failure modes become backtest cases. Release authority is not named.

## Themes
- evals-autonomy-trust: backtests replay "a few thousand" past conversations through production and candidate; LLM judges (ensembles across model families, calibrated against human labels) score grounding, guidance adherence and escalation; a full backtest graded in under an hour; one calibration found guidance judges too harsh and blocking good changes.
- human-review-gates: decision is "not a binary readout"; standing rules "never knowingly ship a resolution rate regression" and never knowingly increase hallucinations; some resolution winners held back over worse handoffs to humans (Stage 3).
- org-learning-loop: post-release judges score live samples, humans keep reading, and new failure modes become cases in the next backtest (Stage 4).
- spec-becomes-prototype-and-evals: manual reading of sampled conversations in a spreadsheet comes first and "surfaces unanticipated failure modes" that become automated checks ("Look at the data!").

## Key points
- Fin deploys about 200 times a day; thousands of experiments over three years.
- A/B practice: power analysis upfront, one pre-declared primary metric (resolution rate), whole-week runs, a stricter-than-5% significance bar. Scorecard: hard resolutions, negative feedback, CSAT, internal CX score, latency, cost, hallucination rate, guidance following, length/format.
- 2024 incident: moving from conversation summaries to full chat history raised hallucinations; release blocked; about two months of prompt changes and backtests to fix.
- Reported trajectory: resolution about 30% at launch (early 2023) to 76%; CSAT 57% to 75%.
- Same approach sold to customers as "eval-driven delivery".

## Could not verify
- Judge models, rubrics, thresholds, sample sizes; who holds release authority; monitoring detail (deferred to a future post).
