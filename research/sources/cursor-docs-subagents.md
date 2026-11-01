---
title: "Subagents (Cursor docs)"
source_url: https://cursor.com/docs/context/subagents
author: Cursor (Anysphere)
publisher: cursor.com
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [harness-portability, task-context-isolation, delegation-return-contract, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
Cursor's subagents run in the editor, the CLI and Cloud Agents, and Cursor reads subagent definitions from `.claude/agents/` and `.codex/agents/` as well as `.cursor/agents/`. That is the first concrete sign that subagent definitions are becoming de facto portable across three harnesses, even with no spec, which lowers the cost of shipping an intent-refinement or dependency-identification subagent into whatever harness a person uses. The same page shows the limit: cloud subagents use the team's MCP servers configured at cursor.com/agents, not the person's local ones, so enterprise context reachable locally may not be reachable in the cloud.

## Themes
- harness-portability: project locations `.cursor/agents/`, `.claude/agents/`, `.codex/agents/`; `.cursor/` wins on name conflicts; frontmatter `name`, `description`, `model` (default `inherit`), `readonly`, `is_background`.
- task-context-isolation: "Subagents start with a clean context and can't see prior conversation. The parent must include the relevant details in the prompt."
- delegation-return-contract: the subagent "returns a final message"; background subagents write output to `~/.cursor/subagents/` where the parent checks progress; each run returns an agent ID that resumes it with context preserved.
- remote-agent-invocation: "Cloud subagents use the MCP servers configured for your team at cursor.com/agents, not your local ones."

## Key points
- Built-ins: Explore (faster model, parallel search) and Browser (filters noisy DOM and screenshots).
- Parallel when the parent issues several Task calls; edit-heavy parallel work can get its own worktree or cloud VM and branch, merged only when the parent integrates.
- Subagents inherit all parent tools including MCP; `readonly: true` blocks writes; child subagents one level deep (since Cursor 2.5); hooks and tool policies can block spawning.

## Could not verify
- No page date. Whether Cursor honours Claude-specific frontmatter fields (hooks, memory, permissionMode) when reading `.claude/agents/` is not stated.
