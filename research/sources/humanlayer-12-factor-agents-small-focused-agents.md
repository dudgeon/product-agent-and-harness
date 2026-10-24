---
title: 12-Factor Agents, factor 10 "Small, Focused Agents"
source_url: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md
author: Dex Horthy (HumanLayer)
publisher: GitHub (humanlayer/12-factor-agents)
published: 2025-04-03
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [one-job-per-agent, human-review-gates, agent-failure-modes]
relevance: high
---

## Relevance to the project
The clearest practitioner statement of "one job per agent" as a *context-length reliability argument* rather than an org-design one: keep agent loops to roughly 3-10 steps (maybe 20) inside a mostly deterministic system, and grow scope only as quality holds. This is the technical rationale to set against Ramp's "single agent with a thousand skills": both can hold if "job" means a bounded loop and skills/subagents are invoked inside one conversational surface.

## Themes
- one-job-per-agent: small agents give manageable context, clear responsibilities, better reliability, easier testing and debugging; "As context grows, LLMs are more likely to get lost or lose focus."
- human-review-gates: the wider guide treats human contact as a tool call; agents are one component in a deterministic system (from search summaries, not re-read here).
- agent-failure-modes: long loops degrade as context fills.

## Key points
- Counterargument addressed: even if models handle 100+ step workflows later, small scope delivers now and can be expanded deliberately.
- Origin essay date 2025-04-03 (from search summary).

## Could not verify
- Only factor 10 was read; the rest of the guide is from secondary summaries. The "3-10 steps" figure is an assertion, not measured.
