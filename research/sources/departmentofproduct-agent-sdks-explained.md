---
title: AI Agent SDKs Explained
source_url: https://departmentofproduct.substack.com/p/ai-agent-sdks-explained-a-guide-for
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-04-27
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [agent-frameworks, identity-delegation, evals-autonomy-trust]
relevance: low
---

## Relevance to the project
A non-engineer's primer (April 2025) on agent SDKs: model-vendor frameworks (OpenAI Agents SDK, Google ADK) versus domain toolkits from SaaS companies (Stripe's agent toolkit, 1Password's agentic SDK). It predates the harness-as-SDK products (Claude Agent SDK, Codex SDK) the project's loop-source dimension turns on, so it is mostly background. Two points carry over: domain SDKs ship credential and spending controls for agents (restricted keys, single-use virtual cards, vault-fetched secrets), and Stripe's docs tell builders to run agents in a sandbox with evals because behaviour is non-deterministic. All company facts are second-hand from vendor docs.

## Themes
- agent-frameworks: defines the common parts (agents, loops, handoffs, tools including agents-as-tools, protocol support for MCP and A2A); notes OpenAI's SDK and ADK are model-agnostic; ADK's base, LLM, workflow and custom agent types; a YouTube Shorts demo with three sub-agents under a loop agent. See [OpenAI Agents SDK](openai-agents-sdk-docs.md), [ADK](google-adk-docs.md).
- identity-delegation: 1Password's SDK lets agents read, write, share and rotate vault secrets instead of hard-coded credentials; Stripe's toolkit uses restricted API keys and single-use cards with spend limits.
- evals-autonomy-trust: relays Stripe's doc warning to use a sandbox and run evaluations before money moves.

## Key points
- SDK refresher: libraries/APIs, docs, code samples, dev tools ("recipe kits").
- Stripe's toolkit works with OpenAI Agents SDK, Vercel AI SDK, LangChain and CrewAI; demos (via Steve Kaliski) include payment links, multi-agent receipt-to-invoice and usage-based billing for a research agent.
- Cites a WSJ survey that 6% of execs had deployed agents (second-hand).

## Could not verify
- The WSJ 6% figure (not linked).
