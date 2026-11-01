---
title: "Advanced capabilities: Managed Devins, session analysis, skills, Devin MCP (Devin docs)"
source_url: https://docs.devin.ai/work-with-devin/advanced-capabilities
author: Cognition
publisher: docs.devin.ai
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [remote-agent-invocation, human-review-gates, skill-improvement-loops, identity-delegation]
relevance: high
---

## Relevance to the project
Cognition, the author of "Don't build multi-agents" ([Cognition](cognition-dont-build-multi-agents.md)), now ships a coordinator Devin that launches child Devins in isolated VMs, messages them, sleeps and wakes when they finish, and a Devin MCP server that "any Devin session or MCP-compatible agent" can call to create, message, wait on and terminate sessions. So a person's general harness (Claude Code, Codex) can drive Devin sessions as remote agents over MCP: model B with a deployed agent behind a tool. The coordinator's wake-on-child-event and scheduled self-messages are the mechanics a long-lived dependency ask needs.

## Themes
- remote-agent-invocation: Devin MCP tools cover session management (create, search, inspect events, message, terminate, archive, wait for several sessions in one call), skills, knowledge, schedules, integrations and repository docs.
- human-review-gates: "Child sessions start without confirmation by default. To review each batch before launch, turn off Auto-approve child sessions."
- skill-improvement-loops: Devin turns successful sessions into a reusable `SKILL.md` (saved to org skills or opened as a PR) and refines skills from sessions where they fell short; session analysis suggests revised prompts.
- identity-delegation: permissions are org roles: Use Devin Sessions, Manage Playbooks, Manage Knowledge, Manage Schedules; default `org_member` and `org_admin` include all four.

## Key points
- A child receives a prompt, optional skills, optional tags and an ACU limit; children can open their own PRs and report when finished or needing input; the coordinator compiles results.
- Coordinator can track ACU use, put children to sleep, terminate them, and schedule messages to itself for check-ins; it is woken automatically, no polling.
- For wide fan-outs or dependent stages, the page recommends a dynamic workflow "which runs as a recorded, resumable script".
- Scheduling: cron or one-time sessions, including "weekly knowledge upkeep".

## Could not verify
- No dates on the page; whether children inherit Knowledge entries; maximum concurrent children. Whether a Devin MCP call made from another harness acts as the calling person's Devin user or a service identity is not stated.
