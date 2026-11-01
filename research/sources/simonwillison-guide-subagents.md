---
title: Subagents (Agentic Engineering Patterns)
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/subagents/
author: Simon Willison
publisher: simonwillison.net
published: 2026-03-17
retrieved: 2026-10-31
type: article
evidence: independent
filed_by: research-agent-handoff-models
themes: [task-context-isolation, single-agent-many-skills, one-job-per-agent]
relevance: medium
---

## Relevance to the project
An independent practitioner's account of subagents in coding agents: the parent writes a prompt, dispatches a fresh copy of itself, waits as for any tool call, and gets back a summary; the value is "preserving that valuable root context and managing token-heavy operations". He cautions that specialist role subagents are often unnecessary because the root agent can review or debug its own output given tokens. Supports model B with subagents as context protection rather than as role owners.

## Themes
- task-context-isolation: Claude Code's Explore subagent returned file locations and details "the parent agent needed" to start editing.
- single-agent-many-skills: "Your root coding agent is perfectly capable of debugging or reviewing its own output provided it has the tokens to spare."
- one-job-per-agent: role subagents (reviewer, test runner, debugger) possible but not the main value.

## Key points
- Context limits "generally top out at around 1,000,000" and quality is better below about 200,000.
- In a 2026-03-16 link post he notes subagents were generally available in Codex and widely supported (OpenCode, VS Code, Cursor).

## Could not verify
- Chapter date taken from his feed (2026-03-17); not shown on the page.
