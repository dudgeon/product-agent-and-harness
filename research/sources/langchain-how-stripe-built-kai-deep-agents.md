---
title: How Stripe Built Kai, its Company-Wide AI Agent, on Deep Agents
source_url: https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents
author: Sofia Sulikowski (LangChain), with quotes from Sharadh Krishnamurthy, Anupam Upadhyay, Chrissie Cui (Stripe)
publisher: LangChain blog (customer story)
published: 2026-08-03
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [agent-frameworks, single-agent-many-skills, skills-marketplace, build-vs-buy, memory-architecture, cost-control-routing, shared-persistent-sessions, enablement-by-product, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The most technical account of Kai's harness, written by the framework vendor with Stripe quotes. It gives the layering (Deep Agents base, Stripe harness, configuration layer, UI), the middleware choices (S3-backed virtual filesystem with sync-in/sync-out, sandbox as a tool not the agent's environment, summarization), and the skill-gates-tools pattern with a measured ceiling (~150 skills before frontier models degrade). Bears on loop-source (framework harness vs vendor CLI harness), capability-format-portability, context-and-memory and governance.

## Themes
- agent-frameworks: Kai is built on Deep Agents (LangChain's open-source harness) over LangGraph; "The Deep Agents layer solves all the non-Stripey problems, so that we can focus on solving the Stripey agent problems" (Krishnamurthy).
- single-agent-many-skills: base agent ships foundational skills; tiered skills load by user profile and Kai-agent config (sales ops vs finance), plus a user-level profile layer; foundational skills are pinned.
- skills-marketplace: federated ownership, 1,000+ skills from 100+ teams; 500+ internal MCP tools.
- skill-standards (via allowedTools): Agent Skills `allowedTools` drive dynamic tool loading: two-pass, skill selection gates tool context. 1,024-char frontmatter limit; "quality degradation of frontier models with more than 150 skills when combined with their system prompt". Planned hybrid: RAG/classifier prefilter then LLM choice.
- memory-architecture: virtual filesystem backed by S3; every sandbox execute call wrapped in "sync in / sync out" so the agent sees a coherent, persistent file environment across the session.
- cost-control-routing: summarization thresholds, summarizer model and output size tuned for cost; intermittent sessions make large-context cache misses costly.
- build-vs-buy: Stripe had to build Python service scaffolding beside its Ruby/Java stack; "1 engineer, 1 week" to v1 justified it (vendor framing).
- enablement-by-product: adoption driven by removing knobs: users who found the previous tool "unapproachable. I had to tune a bunch of knobs" found Kai needed none.
- shared-persistent-sessions: "The current model is single-user sessions"; roadmap to shared skills, shared artifacts, collaborative sessions.

## Key points
- Origin: after Claude Code (the post says late 2024) "every Stripe employee wanted to build agents", but terminal, data access and security were barriers for non-engineers; the team chose the "inverse approach": meet them with "an always-on, production-ready assistant".
- Kai: session-based chat; artifacts (reports, dashboards, documents) live alongside the conversation and evolve; "operates like a coding agent for non-engineers"; connects to data warehouse, Slack, Google Suite.
- Four layers: Deep Agents base; Stripe-specific harness (security posture, infra, internal services); configuration layer (custom Kai agents with different skills, behaviours, personas, no harness changes); Kai UI.
- Sandbox exposed as a tool; the agent runs outside it and calls in ("keeping execution boundaries clean").
- Adoption: quarterly target hit in one week of open preview; 296 to 5,000+ users in ~4 weeks; 83% weekly, ">60k sessions" (period unstated); Marketing 95%, GTM 87% (higher than engineering).
- Next: scaling skill selection; governance and guardrails "so that Kai's reach doesn't outpace the oversight structures"; behavioural personalisation by ML classifiers ("you don't need to tune knobs"); cross-session collaboration.

## Notable quotes
- "My Stripe career is divided into before and after Kai." (unnamed user)
- "Kai is absolutely unbelievable for salespeople. Tens of thousands of hours will be saved." (unnamed user)

## Could not verify
- Vendor customer story: "built in one week" is the framework vendor's headline; the How I AI interview says "one and a half people over two weeks" for v0. ">60k sessions" has no period; Krishnamurthy's LinkedIn says 20,000 sessions a day.
- The post dates Claude Code's launch to late 2024 (its public launch was Feb 2025); treat the timeline loosely.
