---
title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
source_url: https://arxiv.org/abs/2406.12045
author: Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan (Sierra, Princeton)
publisher: arXiv
published: 2024-06-17
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [evals-autonomy-trust, agent-failure-modes, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
Introduces pass^k (all k repeated trials succeed), the metric that matters for standardised, repeatable work: an agent that is right 60% of the time per attempt is far less reliable when the same job must be done every time. It supports the claim that repeatable, rule-following jobs need constraint, evals and consistency measurement. Results are from 2024 models and customer-service domains.

## Themes
- evals-autonomy-trust: state-of-the-art function-calling agents succeeded on under 50% of tasks; pass^8 below 25% in retail.
- agent-failure-modes: inconsistency across trials and failure to follow domain policy rules.
- work-structure-spectrum: policy-following tasks (rules + tools + user) are where open-ended agents were weakest.

## Key points
- Simulated user + domain tools + policy; evaluates final database state.

## Could not verify
- Formal pass^k definition is from search results (all k i.i.d. trials succeed). Current-model numbers not checked; the gap has likely narrowed.
