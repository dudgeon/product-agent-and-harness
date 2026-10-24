---
title: "Encoding Your Domain Expert: The Context Layer Behind Spotify's Data Assistant"
source_url: https://engineering.atspotify.com/2026/6/encoding-your-domain-expert-the-context-layer-behind-spotifys-data-assistant
author: Pavlina Mitsou and Jonathan Warburton (Senior Engineers, Spotify)
publisher: Spotify Engineering blog
published: 2026-06-10
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, org-context-grounding, metrics-review-agents, agent-as-service-many-surfaces, org-learning-loop, ai-synthesis-hallucination-risk]
relevance: high
---

## Relevance to the project
The clearest first-party test of mining versus curation that we have. Spotify's data assistant, Vedder, grounds on **clusters** of context owned by named domain experts: datasets with profiling, vetted question-and-SQL pairs, and business docs. When Spotify tried the obvious shortcut, turning experts' query history into examples automatically, curators **rejected 87.5% as noise**. Each cluster carries a continuously computed **health score** (pair validity after schema changes, coverage of real questions, SQL reproducibility), and every conversation is fed back to cluster owners. This is direct evidence for Geoff's context-creation hypothesis in its "owner-curated, verified" form, and against pure passive mining. It parallels Stripe's Hubble/"ask data" tiering and Trailhead verification.

## Themes
- tacit-knowledge-capture: "A layer that captures what actually matters about a slice of the warehouse, owned by people who own and understand the domain"; schemas don't say that INT64 values under 100 are legacy test data, or what "active user" means.
- ai-synthesis-hallucination-risk: auto-generating pairs from query history: "The other 87.5% were ad-hoc exploration, debugging sessions, one-off answers ... queries that used the wrong table, or queries that were technically correct but taught the wrong pattern. Query history is rich. Most of it is noise."
- org-learning-loop: every conversation's questions, answers, SQL and feedback are shown to cluster owners; the experts' role shifts to "shaping the knowledge layer that answers thousands".
- org-context-grounding: when no cluster covers a topic, the agent says so; answers come with the query and sources.
- agent-as-service-many-surfaces: Slack bot, an MCP server for IDEs and AI tools, and a web UI.
- metrics-review-agents: since August 2025, 2,100+ users, 13,000+ conversations, 60,000+ messages, 177 clusters; more than a quarter of users had never written SQL.

## Key points
- Scale: 70,000+ datasets; 1.4 trillion data points a day. "Provide the same number of tables to a model, and it will be confident in selecting the wrong one."
- A cluster = datasets (schema, cardinality, common values, partitions) + pairs (expert-written or expert-approved few-shot examples) + docs (terminology, gotchas, which columns to avoid).
- Health score signals: underlying data health, how many pairs are still valid after schema changes, coverage of the questions people actually ask, SQL reproducibility, and others. Degraded scores suggest actions.
- Next: knowledge "outside the schema" (process documentation and definitions).

## Notable quotes
- "The model reasons over context. It doesn't decide what's true about the data, the experts do."

## Could not verify
- Usage figures are Spotify's own; there is no accuracy metric. "87.5%" is the share rejected in the curation trial; the trial's size is not given.
