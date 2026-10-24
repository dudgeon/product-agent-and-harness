---
title: Custom subagents in Claude Code (docs)
source_url: https://code.claude.com/docs/en/sub-agents
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, single-agent-many-skills, skills-marketplace]
relevance: high
---

## Relevance to the project
Subagent definitions are the less-standardised sibling of skills: there is no cross-vendor spec, and this page is explicit that nothing in the format is marked portable. Relevant to the question "how far can a packaged subagent carry complexity": model, tool allowlist, permission mode, memory, worktree isolation, hooks and MCP servers can all be declared, but all bind to Claude Code features.

## Themes
- harness-portability: the docs note that fields (model values, tool names, permissionMode, memory, isolation, hooks) "depend on Claude Code features" and "documentation does not label any field as portable". Format = Markdown + YAML frontmatter, body = system prompt.
- skills-marketplace: precedence managed settings > `--agents` > project > user > plugin; plugin-shipped subagents have `hooks`, `mcpServers`, `permissionMode` ignored "for security", so a plugin cannot ship a fully privileged agent definition.
- single-agent-many-skills: subagents can spawn subagents up to three layers by default; 20 concurrent default; the `skills` field preloads up to 32 skills.

## Key points
- Required: name, description. Optional: tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory (user/project/local), isolation: worktree, background, effort.
- Delegation is description-matched by default in Claude Code.

## Could not verify
- Final ~16k characters of the page not read.
