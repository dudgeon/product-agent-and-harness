---
title: Context Engineering for AI Agents: Lessons from Building Manus
source_url: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
author: Yichao "Peak" Ji (Manus)
publisher: Manus blog
published: 2025-07-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, memory-architecture, cost-control-routing, build-vs-buy]
relevance: high
---

## Relevance to the project
A production team that built its own agent framework reports rebuilding it four times and names KV-cache hit rate as the top production metric. Evidence that an own harness is a continuing research cost, and that cost control lives inside harness design (stable prefixes, tool masking).

## Themes
- harness-over-model: framework rebuilt four times ("Stochastic Graduate Descent").
- cost-control-routing: keep prompt prefix stable and context append-only to preserve KV-cache.
- memory-architecture: filesystem as external context; todo recitation to keep goals in recent attention.

## Key points
- Mask tool logits rather than add/remove tools mid-task.
- Keep failed actions in context so the model adapts.

## Notable quotes
- "the KV-cache hit rate is the single most important metric for a production-stage AI agent"
