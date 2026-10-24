---
title: Create custom subagents (Claude Code)
source_url: https://code.claude.com/docs/en/sub-agents
author: Anthropic
publisher: code.claude.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, skill-standards, one-job-per-agent]
relevance: medium
---

## Relevance to the project
Defines what a Claude Code subagent is (markdown + frontmatter, own context window, tool allowlist, model, scoped MCP servers) so it can be contrasted with a remote agent: subagents run inside the session, share its auth and usage limits, and return a summary. No remote execution of subagents is described.

## Themes
- `one-job-per-agent`: A subagent is a single-purpose definition (name, description, tools, model) selected by description matching.
- `remote-agent-invocation`: In-session only; foreground or background; up to 3 nesting layers and 20 concurrent by default; plugin subagents ignore hooks, mcpServers, permissionMode.

## Key points
- `mcpServers` field gives a subagent servers the main conversation lacks, connected only while it runs.
- Agent teams (coordinated sessions) and background agents (parallel independent sessions) are separate features.
- Cost: subagents consume the same usage limits.

## Could not verify
- Last ~16k characters of the page not read.
