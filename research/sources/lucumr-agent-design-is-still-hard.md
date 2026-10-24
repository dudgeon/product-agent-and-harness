---
title: Agent Design Is Still Hard
source_url: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
author: Armin Ronacher
publisher: lucumr.pocoo.org
published: 2025-11-21
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, build-vs-buy, memory-architecture]
relevance: high
---

## Relevance to the project
An experienced independent practitioner reports that using the Vercel AI SDK only for provider abstraction was a mistake, that model differences force your own abstraction, and that evals are the hardest problem. The best independent counter-evidence to "buy a framework".

## Themes
- agent-frameworks: SDK abstractions broke message history with provider tools; would not choose it again.
- build-vs-buy: own agent abstraction likely needed because model differences are large; avoid abstractions for now.
- memory-architecture: explicit cache management; shared virtual filesystem between tools; subagents isolate failure noise.

## Key points
- Reinforcement via tool results (todo, state reminders).
- Testing and evals are the hardest unsolved problem; external eval tools miss agent context.

## Notable quotes
- "At this point we would not make that choice again."
- "We find testing and evals to be the hardest problem here."

## Could not verify
- Ronacher's project/team context not specified in the fetched text.
