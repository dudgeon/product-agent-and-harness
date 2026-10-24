---
title: "Automation Platform v2: Improving Conversational AI at Airbnb"
source_url: https://medium.com/airbnb-engineering/automation-platform-v2-improving-conversational-ai-at-airbnb-d86c9386e0cb
author: Chutian Wang and 13 co-authors (Airbnb)
publisher: The Airbnb Tech Blog (Medium)
published: 2024-10-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [agent-frameworks, org-context-grounding, policy-enforcement-fail-open, human-review-gates]
relevance: medium
---

## Relevance to the project
Shows the internal platform under Airbnb's LLM customer-support work in late 2024: a shared runtime where product teams build LLM apps with a tool manager, a context loader, a guardrails framework, a prompt playground and LLM observability. It is a useful early pattern for "one platform, many agent apps", and it records Airbnb's stated stance then: mix LLM reasoning with fixed workflows, and keep sensitive flows (claims) on deterministic workflows. Read via the Wayback Machine because Medium blocked direct fetch.

## Themes
- agent-frameworks: v1 modelled chatbots as predefined step workflows; v2 adds a "Chain of Thought" workflow where the LLM picks tools in a loop; existing actions and workflows become tools.
- org-context-grounding: a Context Loader and Runtime Context Manager supply chat history, user role, trip data and help articles; developers declare static context or name dynamic retrievers; point-in-time retrieval supports offline evaluation.
- policy-enforcement-fail-open: a Guardrails Framework where teams write reusable guardrails run in parallel, e.g. an LLM content-moderation guardrail and rule-based tool guardrails that block bad writes such as invalid listing updates.
- human-review-gates: the stated aim is to help human support agents work faster; LLM apps sit next to, not instead of, traditional workflows.

## Key points
- Problem with v1: rigid flows and manual workflow building per scenario did not scale.
- Stance (Oct 2024): LLMs not yet reliable enough on latency and hallucination to fully run support for millions; combine them with workflows. Claims processing with sensitive numbers stays a workflow.
- Example flow: "where is my next reservation?" gathers context, LLM requests a tool call, platform executes and adds result to context, LLM answers, conversation is logged.
- Components: CoT IO handler, Tool Manager (payloads, retries, rate limits), LLM Adapter (plug in different models), playground for prompt writers, observability (latency, tokens), tool registration and publishing.
- Next steps named: other agent frameworks, more tools, LLM application simulation.

## Could not verify
- No adoption or quality numbers in the post.
