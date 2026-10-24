---
title: "Production-grade AI agents for financial compliance: Lessons from Stripe"
source_url: https://aws.amazon.com/blogs/machine-learning/production-grade-ai-agents-for-financial-compliance-lessons-from-stripe/
author: Christopher Phillippi and Chrissie Cui (Stripe), Hasan Tariq and Mohan Musti (AWS)
publisher: AWS Machine Learning Blog
published: 2026-06-26
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [human-review-gates, work-structure-spectrum, one-job-per-agent, cost-control-routing, evals-autonomy-trust, risk-sloped-review]
relevance: high
---

## Relevance to the project
Stripe's other knowledge-worker agent pattern: not a general assistant but agents embedded in compliance analysts' review tooling, answering decomposed sub-questions as pre-fetched research while the human answers every question. It shows a structured (DAG) orchestration in tooling code, a dedicated agent service (100+ agents in under a year), a central LLM Proxy and full audit logs, with a measured 26% cut in median handling time. Co-written with AWS (vendor marketing context), but the architecture claims come from Stripe staff. Bears on work-structure, review-and-autonomy, governance-control-plane and model-provider-coupling.

## Themes
- human-review-gates: agent answers are "supplementary information to the human reviewer, who must ultimately answer each sub-task"; "Humans stay in the driver's seat".
- work-structure-spectrum / one-job-per-agent: a single unconstrained agent "would have focused too much on the wrong things"; the review is split into bite-sized sub-tasks forming a DAG; the review tooling is the orchestrator, piping human-validated answers as context to later questions.
- evals-autonomy-trust: each sub-question is quality-tested against human standards before it may inform reviewers in production; helpfulness rating >96%.
- cost-control-routing: prompt caching cut costs 60%; cost instrumentation per agent invocation.
- cost-control-routing (model proxy): all LLM access goes through an LLM Proxy: noisy-neighbour protection, one API many models, model fallbacks, authenticated usage tracking to check "the appropriate models are being used depending on the privacy of the application"; Bedrock inside the proxy.
- risk-sloped-review: Stripe "isn't willing to accept an increase in risk tolerance", so automation stays assistive.

## Key points
- Problem: analysts spent up to 80% of time navigating fragmented systems to gather documentation.
- ReAct-style compliance agent: tool calls gather signals until confident; every tool output forced back as an observation; explicit traces logged.
- Agent service: ML inference infra was rejected (agents are network-bound, long and stateful, with flexible output schemas). The service started stateless and synchronous, now also runs stateful multi-turn agents, "well over 100 agents in less than a year".
- Audit: the entire agent log retrievable for every historical run.
- Results: 26% reduction in median review handling time; >96% helpfulness; "early progress". Next: questions that need context validated during the review; fine-tuning considered.

## Could not verify
- Vendor-hosted (AWS) post; figures are Stripe-reported. The relationship between this agent service and Kai's execution environment is not stated (Chrissie Cui leads both per her bio).
