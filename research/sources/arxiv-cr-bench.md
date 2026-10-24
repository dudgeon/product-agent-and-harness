---
title: "CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents"
source_url: https://arxiv.org/abs/2603.11078
author: Kristen Pereira, Neelabh Sinha, Rajat Ghosh, Debojyoti Dutta
publisher: arXiv (listed at ICLR 2026)
published: 2026-03-10
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [evals-autonomy-trust, agent-failure-modes, human-review-gates]
relevance: medium
---

## Relevance to the project
Review is the textbook "standardise it" task, and this paper shows agents tuned to find all issues have low signal-to-noise, with a measurable trade-off between recall and spurious findings. It supports scoping review agents narrowly and measuring noise, not only catches. Preliminary study.

## Themes
- evals-autonomy-trust: resolution rate alone can mislead; frontier trading issue resolution against spurious findings.
- agent-failure-modes: noisy exhaustive review; compared single-shot and Reflexion-based agents on two unnamed frontier models.

## Could not verify
- Abstract only: models, quantitative results and merge-rate or signal-type findings not read. A separate claimed MSR study of 13 review agents (human-only PR merge rate 68.37% vs 45.20% agent-only) appeared only in a blog summary and is not filed.
