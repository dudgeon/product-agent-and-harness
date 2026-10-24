---
title: How Shopify built an AI stack that doesn't care which models survive
source_url: https://venturebeat.com/orchestration/how-shopify-built-an-ai-stack-that-doesnt-care-which-models-survive
author: Taryn Plumb
publisher: VentureBeat
published: 2026-06-24
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: competitive-teardown-shopify-river
themes: [cost-control-routing, harness-portability, meta-harness]
relevance: low
---

## Relevance to the project
A trade-press write-up of the Beyond the Pilot episode with Farhan Thawar (see [venturebeat-beyond-the-pilot-farhan-thawar](venturebeat-beyond-the-pilot-farhan-thawar.md)). It adds a concrete failover anecdote and the "circuit breaker" framing, but mentions River only in passing ("creates a 'substrate of information' across the company"). It is journalism resting entirely on Shopify's own claims.

## Themes
- `cost-control-routing`: an LLM proxy with bulk token purchasing, reporting and automatic failover. "Circuit breakers" ping a user when a model has been running a long time ("say, 10 hours") and consuming many tokens.
- `harness-portability`: engineers use Claude Code, Codex, Cursor and GitHub Copilot for VS Code on the same proxy. A usage dashboard tracks spend, use of the most expensive models, and time spent reasoning.
- `meta-harness`: the proxy is the shared layer under many harnesses.

## Key points
- Failover anecdote: "When Claude Fable 5 shut down", the proxy "shifted them to Claude Opus or GPT 5.5 automatically, without interrupting their workflows" (quoted via fetch tool).
- Distillation: an engineer supplies a teacher model, training data, evals and a target. The pipeline runs about a day, reports speed, cost and accuracy, and deployment needs no separate approval. Gains are "2x" and up to "30x" cheaper/faster. Sidekick is cited as an example. The long-term goal is a pipeline that proposes its own target model.
- Thawar frames the shift as from "AI reflexivity" to "AI leverage": infrastructure before features.
- River appears only in a teaser line.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- The exact wording around the "Claude Fable 5 shut down" event. A MindStudio post (2026-06-15) separately refers to a "Claude Fable 5 shutdown" and "government model bans", but this was not checked.
- The Port software-factories page cites a "$250-a-day" alert threshold (from Bessemer) and "10-hour mark" (from here). These are two framings of the same alerting.
