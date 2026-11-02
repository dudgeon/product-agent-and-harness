---
title: "Unlocking Financial Insights with Finch: Uber's Conversational AI Data Agent"
source_url: https://www.uber.com/us/en/blog/unlocking-financial-insights-with-finch/
author: Eddie Huang, Taya Yusuf, Tim Ross (Uber)
publisher: Uber Engineering Blog
published: 2025-07-17
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [metrics-review-agents, agent-as-service-many-surfaces, identity-delegation, certified-metrics-layer, human-review-gates]
relevance: medium
---

## Relevance to the project
Finch is Uber's Slack-native finance data agent: a supervisor routes questions to sub-agents (SQL writer, document reader), which use a semantic layer of natural-language aliases over curated single-table data marts and check the user's permissions before running SQL. It is a pre-Cortana example of a domain assistant bound to a function and a Slack surface, the pattern Cortana later generalised as personas. It also shows Uber's "request validation by an SME" idea for executive answers.

## Themes
- metrics-review-agents: natural-language finance questions to SQL over Presto and planning systems; results as summary, table, executed query and optional Sheets export (Output).
- certified-metrics-layer: curated single-table data marts and an OpenSearch index of column and value aliases to get WHERE clauses right (Semantic layer).
- identity-delegation: RBAC and governed datasets; the SQL writer validates the user's permissions before executing (Access control).
- agent-as-service-many-surfaces: Slack AI Assistant APIs give starter questions, a pinned app and a split pane; live status messages from a LangGraph callback (Slack surface).
- human-review-gates: planned "Request validation" button so an SME checks answers for leaders such as the CEO and CFO; "it's not 100% reliable and is prone to hallucination" (Future).

## Key points
- Models via Uber's Generative AI Gateway, self-hosted and third-party, swappable.
- Evaluation: sub-agent outputs vs golden query outputs; supervisor routing accuracy (intent collisions); end-to-end simulated queries; regression on historical queries before prompt or model changes.
- No adoption or accuracy numbers.

## Notable quotes
- "it's not 100% reliable and is prone to hallucination"

## Could not verify
- User counts, accuracy, latency: not reported. Relation to Cortana not stated.
