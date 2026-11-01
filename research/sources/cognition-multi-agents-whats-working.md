---
title: "Multi-Agents: What's Actually Working"
source_url: https://cognition.com/blog/multi-agents-working
author: Walden Yan (Cognition)
publisher: Cognition blog
published: 2026-04-22
retrieved: 2026-10-31
type: article
evidence: first-party
filed_by: research-agent-handoff-models
themes: [single-agent-many-skills, one-job-per-agent, handoff-context-transfer, human-review-gates]
relevance: high
---

## Relevance to the project
Cognition's follow-up, ten months after "Don't Build Multi-Agents" ([cognition-dont-build-multi-agents](cognition-dont-build-multi-agents.md)). The refined rule is that multi-agent works when "writes stay single-threaded and the additional agents contribute intelligence rather than actions": a clean-context reviewer, a stronger "smart friend" model consulted with a fork of the full context, and a manager Devin that splits work across children. For the modules it suggests intent-shaping and dependency agents that advise or check, while one agent owns the writes to the feature record.

## Themes
- single-agent-many-skills: parallel-writer swarms see little adoption; unstructured swarms are "mostly a distraction".
- one-job-per-agent: most multi-agent setups are read-only subagents (search) that resemble tool calls.
- handoff-context-transfer: reviewer gets the diff, not the coder's history ("work best when the coding and review agents do not share any context beforehand"); smart friend gets "a fork of the full context"; manager-to-child payload not specified.
- human-review-gates: Devin and Devin Review iterate before a human opens the PR; review catches about 2 bugs per Devin PR, about 58% severe (vendor claim).

## Key points
- Failures still open: weaker primary models don't know when to escalate; over-prescriptive managers with little codebase context; children's discoveries that should change siblings' work; agents assume shared state with children; children don't message the manager by default.
- Largest enterprise segment usage up about 8x in six months (vendor claim).

## Could not verify
- Who the manager reports to (user or caller) is not stated.
