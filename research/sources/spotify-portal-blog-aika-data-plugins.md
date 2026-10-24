---
title: "AI knowledge assistant and data plugins coming to Spotify Portal"
source_url: https://portal.spotify.com/blog/aika-data-plugins-coming-to-portal
author: Tom Barkan-Benkler (Product Director, Developer Experience and Backstage, Spotify)
publisher: Spotify Portal blog
published: 2025-04-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [status-update-agents, org-context-grounding, legible-org-for-agents, org-learning-loop]
relevance: medium
---

## Relevance to the project
The fullest public account of AiKA, Spotify's internal "ask the org" assistant on Backstage, with adoption numbers. It shows a pattern we should expect: once an assistant answers from docs, teams start fixing their docs so it answers better. It also puts datasets into the software catalog as owned entities, which is the base that the later Vedder data assistant (`spotify-engineering-vedder-context-layer`) builds on.

## Themes
- status-update-agents: AiKA answers questions on internal systems, reference code, policies and acronyms; first production version Dec 2023 after a Hack Week.
- org-context-grounding: RAG with cited sources; internal version uses several sources and LLMs; external alpha only TechDocs and OpenAI.
- org-learning-loop: teams improved their documentation so AiKA could learn from it; fewer repeat questions in Slack.
- legible-org-for-agents: Data Experience plugin makes datasets catalog entities with owner, tags, schema, and Soundcheck health checks.

## Key points
- Internal use (Spotify claim, Apr 2025): 1,000+ employees daily; 25% of employees weekly; 70% have tried it; 86% of weekly active GitHub users are weekly AiKA users.
- Used by developers and non-developers; helps new hires and people switching teams.
- Scale cited: 1.6 trillion events a day, 42,500+ active data pipelines.
- Announced at KubeCon EU 2025 as alpha for Portal customers. (KubeCon talk "Leveraging Internal Knowledge: Building AiKA at Spotify", 2 Apr 2025, adds a flexible ingestion API for teams' own knowledge.)

## Could not verify
- Lineage features are not mentioned here (Honk part 4 shows lineage in Backstage).
