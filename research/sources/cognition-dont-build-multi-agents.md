---
title: Don't Build Multi-Agents
source_url: https://cognition.com/blog/dont-build-multi-agents
author: Walden Yan (Cognition)
publisher: Cognition blog
published: 2025-06-12
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [single-agent-many-skills, one-job-per-agent, agent-failure-modes]
relevance: high
---

## Relevance to the project
The strongest published argument for a single-threaded agent over many cooperating agents. It bears on reconciling `one-job-per-agent` and `single-agent-many-skills`: the failure it describes is *context fragmentation inside one piece of interdependent work*, which is different from many independent jobs each with their own agent.

## Themes
- single-agent-many-skills: default to a single-threaded linear agent; share full traces, not just messages.
- agent-failure-modes: parallel subagents hold conflicting implicit assumptions (Flappy Bird example: mismatched background and bird).
- one-job-per-agent: Claude Code subagents are used for narrow, well-defined questions, not for writing code; they don't run in parallel with the main agent.

## Key points
- Principle 1: share context (full agent traces). Principle 2: actions carry implicit decisions, and conflicting decisions yield bad results.
- Long tasks: add a context-compression model rather than splitting into agents.
- Author expects multi-agent communication to improve later; the advice is explicitly "in 2025" and for coding-style interdependent work.

## Could not verify
- Whether Cognition changed this position after mid-2025 (not checked).
