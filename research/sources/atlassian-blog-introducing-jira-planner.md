---
title: Introducing Jira Planner
source_url: https://www.atlassian.com/blog/jira/introducing-jira-planner
author: Aditi Venkatesh, Brian Morton (Atlassian)
publisher: Atlassian blog
published: 2026-08-19
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: user-story-mapping
themes: [agent-ready-intent, prd-agents, agent-led-intent-shaping, spec-edge-case-review, opportunity-to-code-chain]
relevance: high
---

## Relevance to the project
Jira Planner is Atlassian's "shape the intent / plan the change" agent: from a rough idea it asks clarifying questions, grounds a spec in code and Teamwork Graph, publishes it as a Confluence Live Doc, checks readiness, and splits it into sequenced Jira work items with acceptance criteria. It is the closest vendor match to a PM intent-shaping agent and names PMs in its audience. Only a launch blog exists; there is no support doc yet (Early Access).

## Themes
- `agent-led-intent-shaping`: "Start with an idea of goal, even a rough one. ... Jira Planner asks the right follow-up questions to help you clarify scope, constraints, and what success looks like." (step 1)
- `agent-ready-intent`: "turns rough ideas into structured, agent-ready specs grounded in a semantic understanding of your codebase, standards, and decisions."
- `spec-edge-case-review`: "surfaces ambiguity upfront and tells you whether your spec is detailed enough for execution, with specific suggestions for what's missing." (step 5)
- `opportunity-to-code-chain`: "breaks the finalized plan into Jira work items, sequenced with dependencies and milestones, with each one carrying its own acceptance criteria and the context of the full plan. From there, agent orchestration takes over." (step 6)
- `prd-agents`: output is "editable Confluence Live Docs ... connected back to Jira"; co-editing and inline comments by engineers, PMs, designers (steps 3-4).

## Key points
- **Claimed:** reads "your code across multi-repo setups, and pulls in context from Teamwork Graph."
- **Claimed:** audience is "tech leads, senior engineers, engineering managers, and PMs" for multi-sprint features and architectural decisions.
- **Documented availability (in the blog):** Early Access, Jira Cloud with Rovo enabled and Teamwork Graph connected, plus Confluence (plans publish as Live Docs); rolling out in waves.
- **Vendor survey claim:** 60% of engineering leaders say teams are shifting toward spec-driven development, "fewer than 15%" have a structured framework (no method).
- **Not stated:** whether Planner reads JPD ideas or Atlassian Goals as input (the July launch post says Teamwork Graph includes JPD customer insights, but does not say Planner uses them).

## Could not verify
- Any support documentation, spec template, or readiness criteria.
