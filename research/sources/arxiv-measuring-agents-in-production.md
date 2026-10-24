---
title: Measuring Agents in Production
source_url: https://arxiv.org/abs/2512.04123
author: Melissa Z. Pan et al. (UC Berkeley, Stanford, IBM and others; includes Ion Stoica, Matei Zaharia, Dawn Song)
publisher: arXiv (ICML 2026 oral)
published: 2025-12-02
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [evals-autonomy-trust, human-review-gates, work-structure-spectrum, one-job-per-agent]
relevance: high
---

## Relevance to the project
The best independent evidence on how deployed agents are actually built: constrained, short-horizon, human-evaluated. It is evidence *against* the picture of production agents as free-roaming general agents, and for constrained task-specific designs wherever reliability matters. Sample is practitioners who volunteered; task types were not extractable from the abstract page.

## Themes
- work-structure-spectrum: production agents use "simple, controllable approaches".
- human-review-gates: 68% execute at most 10 steps before human intervention.
- evals-autonomy-trust: 74% depend primarily on human evaluation; 70% prompt off-the-shelf models rather than tune.
- one-job-per-agent: reliability is the top development challenge, addressed through systems-level design.

## Key points
- 20 in-depth case studies plus a survey of 86 deployed systems across 26 domains (earlier versions cited 306 raw respondents, filtered to 86 in production or pilot). v1 2025-12-02, v4 2026-06-04.

## Could not verify
- Which task types and which sectors dominate; whether "steps" means model calls or tool calls. Full paper not read.
