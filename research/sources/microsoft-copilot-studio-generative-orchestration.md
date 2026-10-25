---
title: Orchestrate agent behavior with generative AI (Microsoft Copilot Studio)
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions
author: Microsoft (Gary Pretty)
publisher: Microsoft Learn
published: 2026-08-26
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [work-structure-spectrum, agent-frameworks, agent-failure-modes]
relevance: high
---

## Relevance to the project
The cleanest shipping example of the control-flow dimension as a product setting: one toggle switches an agent between classic orchestration (author-written dialog trees triggered by phrases, author-written question and message nodes) and generative orchestration (model picks topics, tools, knowledge and other agents by description, generates its own questions and answers). Generative is now the default for new agents, and admins can turn it off per environment, which makes control flow an admin-governed decision right.

## Themes
- work-structure-spectrum: comparison table (topics chosen by trigger phrase vs by description; tools callable only from inside a topic vs chosen by the agent; author must write question nodes vs agent generates questions for missing inputs) (§comparison table).
- agent-failure-modes: overlapping topic descriptions make selection "unpredictable"; disambiguation system topic not called under generative orchestration; limited conversation history means the agent may re-ask (§Best practices; §Known limitations).

## Key points
- "By default, new agents use generative orchestration"; an admin can disable it in an environment, forcing classic.
- Selection depends mainly on descriptions; authoring guidance is about writing distinguishable descriptions (say what a topic cannot do).
- Controls kept for the author inside generative mode: an End all topics node cancels the planner's remaining steps; triggers on "AI response generated" and "Plan complete"; clearing planner conversation history.
- Behaviour "depend[s] on the model your agent is configured to use"; test with that model.

## Could not verify
- No data on accuracy or user outcomes for either mode.
