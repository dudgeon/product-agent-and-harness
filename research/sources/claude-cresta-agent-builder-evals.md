---
title: How Cresta turned CX expertise into an agent builder on the Claude Agent SDK
source_url: https://claude.com/resources/articles/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-10-05
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [meta-harness, evals-autonomy-trust, build-vs-buy, org-learning-loop, harness-over-model]
relevance: medium
---

## Relevance to the project
Cresta's Conductor is an agent that builds, tests, changes and root-causes other customer-service agents, layered as a domain "control plane" on top of the Claude Agent SDK as the general execution harness: a clean example of the harness-layering split (buy the loop, build the domain layer). Its four-part evaluation of the builder itself (outcome, execution path, quality against a curated reference, resource use), rerun on every model or framework change, is a reusable template for evaluating a PM agent. It also turns what a build teaches into a shareable memory artifact and skill. Bears on harness-layering, pm-agent-evaluation, harness-upkeep and model-provider-coupling. Cresta's claims (e.g. deployment time roughly halved) are unaudited.

## Themes
- meta-harness: Conductor is "a self-improving meta-agent" that helps developers build and improve other agents (§A meta-agent that helps build the next agent).
- evals-autonomy-trust: build tasks (new agent, write a test case, change an existing agent, root-cause analysis) scored on outcome, execution path, quality vs curated reference, and resource use; rerun on each new Claude model or framework update before committing (§How Cresta evaluates Conductor).
- build-vs-buy: Cresta "drew a hard line" between its own conversation data and CX expertise and what it took from the Agent SDK, "and refused to build anything on the wrong side of it" (best-practices box).
- org-learning-loop: builders turn lessons from a build into a reusable memory artifact (patterns, business rules, evaluation approaches) and share it as a skill (§A meta-agent...).
- harness-over-model: SDK chosen as "the same agentic development harness" as Claude Code, used programmatically (§intro quote, Renjie Li).

## Key points
- **What Conductor does.** Users describe the agent they want; Conductor goes from a "grounded blueprint" to implementation, evaluation and optimisation, drawing on historical conversations to decide where humans stay in the loop and where the model can adapt.
- **Deterministic vs flexible.** Its main design judgement: harden "enterprise-critical workflows" (especially for regulated, low-risk-tolerance industries) and leave the rest flexible to avoid a giant decision tree; deterministic pieces need tests revised as business rules change.
- **Evals as product feature.** Requirements and edge cases captured during the build become tests in Conductor's evaluation module, so customers can monitor must-work workflows as policies and systems change.
- **Layering.** Agent SDK handles context gathering, tool calls and running code; Conductor adds CX workflows, tools, domain context and governs runs "through policy, observability, verification, and feedback-driven improvement". SDK review covered data privacy, tenant architecture, org-level key distribution, controls and observability.
- **Path to product.** Began as an internal tool for Cresta's forward-deployed team; productised only once output matched what an expert engineer would build.
- **Claimed result.** Initial deployment time "roughly in half" in early use cases across Cresta and partners. Company context: $270M+ raised, $100M+ ARR (Cresta figures).
- **Limits.** One headline metric with no baseline or sample; no eval scores; the "20% build / 80% iteration" split is an assertion.

## Notable quotes
- "The initial build is only about 20% of the effort, the other 80% is the testing, optimization, and continuous improvement that follows." (best-practices box)

## Could not verify
- Who wrote the article (no byline); size and composition of the evaluation set.
