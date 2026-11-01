---
title: "What are Custom Agents? (Notion Help Center)"
source_url: https://www.notion.com/help/custom-agents
author: Notion
publisher: Notion Help Center
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [event-triggered-agents, process-artifacts-as-coordination, scoped-governance-containers, human-review-gates]
relevance: high
---

## Relevance to the project
Notion's reference for Custom Agents lists the triggers that let an agent wake on a change to a shared record: a page added to, updated in or removed from a database, a comment on a page, an AI meeting note finishing, a Slack message, reaction or mention, or a schedule. That makes a Notion database a working event bus for agents that coordinate only through records (a dependency register whose status change wakes an agent), but the page documents no approval gate and does not say whose identity a run acts under.

## Themes
- event-triggered-agents: Notion triggers: "comment added to a page, page added to a database, property updated in a database, page removed from a database", AI Meeting Note finished; some accept filters (property values, a database view). Slack triggers: message posted to a channel, emoji reaction added, agent mentioned; schedule triggers daily to yearly with timezone.
- process-artifacts-as-coordination: "A Custom Agent can pass part of a job to other Custom Agents during a run", limited to sub-agents it has been given access to; whether one agent's write can trigger another agent is not stated.
- scoped-governance-containers: "Agents act only on the pages, databases, and external apps you explicitly grant access to"; "They never have full workspace access by default"; linking a page in instructions does not grant access; "Embedding an agent in a page doesn't give anyone new access to the agent."
- human-review-gates: no documented approval gate or pre-run confirmation; oversight is an Activity tab per run (trigger, actions, errors, step detail), version history of the agent's configuration, thumbs-down feedback, and advice to keep "runs reviewable and reversible".

## Key points
- Enterprise audit log records "Key configuration and access changes to Custom Agents" (instructions, permissions, integrations), not each action; chat insights export capped at 300 chats per period.
- Slack account must use the same email as the Notion account; "Saved or 'Later' messages in Slack are not supported."
- Business or Enterprise plan; runs consume Notion credits; admins can restrict who creates agents and which models they use.
- External control: the Notion MCP server exposes tools to spawn, wait on, message and stop Custom Agent sessions ([notion-mcp-supported-tools](notion-mcp-supported-tools.md)); secondary reporting says the public-beta agent API moved to "sessions and events" with the private-alpha endpoints retired on 2026-10-01 (not verified first-hand).

## Could not verify
- Identity under which a triggered run writes (owner, triggering user or agent account). Page undated (footer 2026). Read via WebFetch (model-summarised view).
