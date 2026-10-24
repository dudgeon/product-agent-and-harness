---
title: Improving Deep Agents with harness engineering
source_url: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
author: Vivek Trivedy (LangChain)
publisher: LangChain blog
published: 2026-02-17
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, evals-autonomy-trust, agent-frameworks]
relevance: high
---

## Relevance to the project
Quantified evidence that harness changes alone (prompt, tools, middleware) moved the same model from 52.8% to 66.5% on Terminal Bench 2.0. Supports harness-over-model, and also shows that harness tuning is ongoing engineering work a builder inherits. Single-vendor result, not independently reproduced.

## Themes
- harness-over-model: +13.7 points with the model fixed at gpt-5.2-codex.
- evals-autonomy-trust: verify-before-exit middleware, loop detection, trace analysis as a skill; warns of overfitting to tasks.

## Key points
- Terminal Bench 2.0 (89 tasks), Harbor on Daytona sandboxes, LangSmith traces.
- Middleware: PreCompletionChecklist, LocalContext, LoopDetection, time-budget warnings.
- Reasoning-budget "sandwich" (xhigh-high-xhigh) 66.5% vs xhigh-only 53.9% due to timeouts.

## Notable quotes
- "Models are biased towards their first plausible solution."

## Could not verify
- No independent replication found.
