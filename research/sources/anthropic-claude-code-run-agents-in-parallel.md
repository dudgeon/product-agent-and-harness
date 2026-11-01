---
title: "Run agents in parallel (Claude Code docs)"
source_url: https://code.claude.com/docs/en/agents
author: Anthropic
publisher: Claude Code docs (code.claude.com)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [work-structure-spectrum, task-context-isolation, shared-persistent-sessions, remote-agent-invocation]
relevance: high
---

## Relevance to the project
Anthropic's own comparison of the five ways one person's Claude Code runs several agents (subagents, agent view, agent teams, projects, dynamic workflows), sorted by who coordinates and whether the agents talk to each other. It is the clearest vendor map of model B (through line) inside one harness. One line matters directly for the two modules: every agent in these approaches is a Claude session, and "To involve a different tool, expose it to Claude as an MCP server." So a deployed intent-shaping or dependency agent reaches this harness as an MCP server, not as a peer.

## Themes
- work-structure-spectrum: "Who coordinates the work?" section: Claude turn by turn (subagents); you (agent view); a lead agent (agent teams); a script (dynamic workflows); a coordinator conversation over days or weeks (projects).
- task-context-isolation: "Subagents report results back to the conversation that spawned them, and agent view sessions report results only to you. Teammates in an agent team message each other directly and ... share a task list."
- shared-persistent-sessions: projects are for work that "spans many tasks over days or weeks, should keep running when your machine is off".
- remote-agent-invocation: "To involve a different tool, expose it to Claude as an MCP server."

## Key points
- Table: subagents (side task, summary back); agent view (dispatch and monitor background sessions, research preview); agent teams (shared task list, inter-agent messaging, experimental, off by default); projects (one ongoing conversation that starts cloud threads, public beta on Pro, Max, Ultra); dynamic workflows (script runs many subagents and cross-checks).
- Supporting tools: worktrees, cross-session messaging (your sessions on this machine, another machine or the cloud), `/batch` (5 to 30 worktree-isolated subagents).
- Forked subagent inherits the full conversation (`/subtask`); `/fork` copies the session into a new background session.
- "Running several sessions or subagents at once multiplies token usage."
- Agent teams do not isolate teammates in worktrees; partition files instead.

## Could not verify
- No date on the page; feature status labels (research preview, experimental, public beta) are as of 2026-10-31.
