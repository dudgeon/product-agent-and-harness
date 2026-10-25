---
title: Why Do Multi-Agent LLM Systems Fail?
source_url: https://arxiv.org/abs/2503.13657
author: Mert Cemri, Melissa Z. Pan, Shuyi Yang, ... Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
publisher: arXiv (cs.AI)
published: 2025-03-17
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [verification-capacity-gap, process-artifacts-as-coordination, decision-rights-for-agents]
relevance: high
---

## Relevance to the project
The MAST taxonomy is the best empirical map of how multi-agent systems fail: about 44% of failure-mode labels are system design (spec, role, termination), 32% inter-agent misalignment and 24% verification. Its two intervention results (clearer roles +9.4%, a high-level verification step +15.6%) give the closest thing to evidence that process structure, not model quality, drives quality in multi-agent sessions.

## Themes
- verification-capacity-gap: task verification failures (premature termination 6.2%, no or incomplete verification 8.2%, incorrect verification 9.1%); authors argue "Multi-Level Verification is Needed" because verifiers often only check that code compiles (results, discussion).
- process-artifacts-as-coordination: failure to ask for clarification 6.8%, task derailment 7.4%, unaware of termination conditions 12.4%, step repetition 15.7% (taxonomy table).
- decision-rights-for-agents: the ChatDev role-spec intervention also gave the CEO agent the final say (introduction); authors draw on high-reliability organisation research (Roberts 1989; Rochlin 1996) to argue failures are organisational.

## Key points
- Data: 1,642 annotated traces from 7 multi-agent frameworks (MAST-Data); taxonomy built from 150 traces; human inter-annotator kappa 0.88; LLM annotator kappa 0.77 vs humans.
- 14 failure modes in 3 categories: system design issues; inter-agent misalignment; task verification. Category sums (mine, from per-mode shares): about 44.2%, 32.4%, 23.5%.
- Interventions (ChatDev, GPT-4o): clearer role specifications +9.4% task success; task-objective verification step +15.6%. Gains were inconsistent and completion stayed low.
- Conclusion: model improvements alone will not fix these failures.
- Latest version v3, 2025-10-26.
