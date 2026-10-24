---
title: Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents
source_url: https://claude.com/customers/rakuten-qa
author: Anthropic (Q&A with Yusuke Kaji, General Manager of AI for Business, Rakuten)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [opportunity-to-code-chain, pm-persona-role-expansion, feedback-triage-agents, org-learning-loop, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
Rakuten describes a company-wide agent setup on Claude Managed Agents in which users assign tasks to agents on a Kanban-style board (plus Slack and Teams), and one product's loop runs from an agent that interviews users and files tickets, through agent or human triage, to agent-assisted PRD, wireframe and prototype. It is one of the clearest customer descriptions of an end-to-end opportunity-to-prototype chain for PMs, and of a PM ("Galileo") running FinOps pipelines and ambient anomaly agents herself. Outcome figures (major releases every two weeks instead of quarterly; 97% fewer initial critical errors and 30%+ lower cost and latency from agent memory in a pilot) are the customer's unaudited claims, with no method given.

## Themes
- opportunity-to-code-chain: feedback agent chats with users and creates tickets; another agent or humans triage; if accepted, agents help finalise the PRD, wireframe or prototype, iterating to success criteria (task system answer).
- pm-persona-role-expansion: PM Shoko Sakamoto builds multi-cloud FinOps pipelines and stakeholder dashboards and sets up ambient observability agents "all by herself" (Galileo answer).
- feedback-triage-agents: user-interviewing agent that creates tickets for agent or human triage (task system answer).
- org-learning-loop: agents with memory avoid repeating past mistakes; Kaji claims individual learning "becomes organizational learning instantly" (memory answer).
- shared-persistent-sessions: tasks assigned to agents on a Kanban-style system; "the workspace and artifacts are shared with colleagues"; separate environments per use case (deployment answer).

## Key points
- **Build vs buy.** Rakuten first built its own persistent compute, memory and storage for agents; it now says managing the execution layer is not core and redirects engineers to the agent experience and governed integration with corporate systems.
- **Deployment.** Each specialist agent deployed "within a week", running long tasks across engineering, product, sales, marketing and finance, producing apps, decks and spreadsheets in sandboxes. Channels: Slack, Microsoft Teams, internal Kanban; mobile voice input for richer task descriptions.
- **Delegating goals, not tasks.** With agents working for hours, users share the end state and the agent decides the tasks; framed as cheaper hypothesis validation.
- **Engineer-built, non-engineer-deployed agents.** Tanapat Ratana (leads the Applied AI Group) built a production-exception investigator that posts root-cause analysis to Slack and "self-improves from feedback", distributed so non-engineers can set it up on their own products.
- **Orchestrating agents.** One colleague runs parallel agents (market research, data analysis), reviews overnight outputs and assembles a deck; framed as leadership skill.
- **Customer-claimed numbers:** major releases every two weeks vs once a quarter (for the PM's products); in a memory pilot, 97% fewer initial critical errors and over 30% lower cost and latency "without any loss in output quality". A linked older case study claims 7 hours of autonomous coding and feature delivery from 24 days to 5.
- **Limits:** no description of governance, permissions or review gates despite "safe, governed integration" being named as the focus; no definition of "critical error"; pilot size unknown; strategic rhetoric ("AI-nization", "Galileo") outweighs mechanism.

## Notable quotes
- "We delegate goals, not tasks." (long-running agents answer)
- "Managing the agent execution layer is not our core objective." (first answer)

## Could not verify
- Publication date (page undated).
- Method behind the 97% error reduction and release-cadence claims.
