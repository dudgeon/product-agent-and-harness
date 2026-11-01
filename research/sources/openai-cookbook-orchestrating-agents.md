---
title: "Orchestrating Agents: Routines and Handoffs"
source_url: https://developers.openai.com/cookbook/examples/orchestrating_agents
author: OpenAI
publisher: OpenAI Cookbook
published: unknown
retrieved: 2026-10-31
type: article
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks]
relevance: medium
---

## Relevance to the project
The conceptual source of the Swarm handoff: a routine is natural-language steps plus tools, and a handoff is an agent "handing off an active conversation to another agent", likened to a phone transfer in which the new agent has "complete knowledge of your prior conversation". That analogy names the property that matters for the two modules: in a control-transfer handoff the person's conversation follows the transfer.

## Themes
- handoff-context-transfer: handoff defined as passing "an active conversation"; the transfer tool result instructs the model to "Adopt persona immediately".
- agent-frameworks: the recipe is marked archived ("may reference outdated models or APIs"); the sample library "should not be directly used in production".

## Key points
- Routines may "start to struggle" as they grow, which motivates splitting into several agents with handoffs.

## Could not verify
- Author and date not shown on the page (originally published about October 2024, not confirmed).
