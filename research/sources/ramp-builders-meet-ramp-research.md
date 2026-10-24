---
title: Meet Ramp Research: Our Agentic Data Analyst
source_url: https://builders.ramp.com/post/meet-ramp-research
author: Faiz Hilaly, Cesar Duran, Jay Sobel
publisher: Ramp Builders (builders.ramp.com)
published: 2025-09-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [research-synthesis-agents, org-context-grounding, legible-org-for-agents, evals-autonomy-trust]
relevance: high
---

## Relevance to the project

Ramp's data-research agent: the "research the problem, read the data" step of its lifecycle, run in Slack threads. It shows how Ramp made analytics context legible to an agent (indexed dbt, Looker and Snowflake metadata plus domain-owner docs) and how it evaluates the context layer rather than each answer. Later absorbed into Glass as a connected tool (Goddijn, April 2026). Bears on where research output lives and whether it reaches intent and planning.

## Themes

- **research-synthesis-agents**: answers data questions in Slack in minutes; 1,800+ questions from 300 users in its first weeks; 1,476 answered in four weeks versus 66 in the human #help-data channel (Building, Scaling sections).
- **org-context-grounding**: domain owners wrote technical docs organised as a file system the agent reads; metadata from dbt, Looker and Snowflake indexed (Defining the search space).
- **legible-org-for-agents**: the context layer is "an incredibly valuable technical asset" (Looking forward).
- **evals-autonomy-trust**: per-question human review didn't scale; Ramp moved to tests of the context layer that assert on intermediate steps, tool calls, tables and query shape (Evaluations).

## Key points

- Stateful Slack threads let users clarify intent and collaborate; in-thread CSV previews for verification.
- Teams add it to alert channels (diagnose failed transactions) and project channels "to scope out new features": the documented link from research into scoping.
- Plans: a headless API; automate maintenance of the context layer.
- No PII access.

## Could not verify

All figures self-reported, from its first weeks (Aug–Sept 2025). How its answers are carried into specs or plans is not described beyond "project channels to scope out new features".
