---
title: When to use multi-agent systems (and when not to)
source_url: https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
author: Cara Phillips, with Paul Chen, Andy Schumeister, Brad Abrams, Theo Chu (Anthropic)
publisher: Claude blog
published: 2026-01-23
retrieved: 2026-10-31
type: article
evidence: first-party
filed_by: research-agent-handoff-models
themes: [single-agent-many-skills, relay-information-loss, task-context-isolation, cost-control-routing]
relevance: high
---

## Relevance to the project
Anthropic's companion to its coordination-patterns article, and the one that states the cost and the decomposition rule: multi-agent uses "3-10x more tokens", helps in three cases only (context pollution, parallel work, specialisation that improves tool choice), and should be split by context, not by problem type, because problem-type splits create a "telephone game". A role split (planner, implementer, tester, reviewer) spent more tokens on coordination than on work, which bears on any design that gives intent shaping and dependency mapping their own agents.

## Themes
- single-agent-many-skills: outside the three cases "coordination costs usually outweigh the benefits".
- relay-information-loss: splitting by problem type creates a "telephone game" where information degrades at each handoff.
- task-context-isolation: "adopt a context-centric view rather than a problem-centric view"; split only where context can be truly isolated.
- cost-control-routing: 3-10x tokens from duplicated context, coordination messages and handoff summaries.

## Key points
- What crosses: the orchestrator gives a specific task and receives a compressed result; in verification the parent sends the artifact, the success criteria and the tools to check it; research subagents return "distilled findings".
- Precedes [claude-multi-agent-coordination-patterns](claude-multi-agent-coordination-patterns.md) (April 2026) and [claude-fold-subagents-into-main-loop](claude-fold-subagents-into-main-loop.md) (October 2026).

## Could not verify
- The role-split experiment's numbers.
