---
title: Claude Code MCP docs: MCP tasks, auto-backgrounding, elicitation, OAuth, channels
source_url: https://code.claude.com/docs/en/mcp
author: Anthropic
publisher: code.claude.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, identity-delegation]
relevance: high
---

## Relevance to the project
Shows how the primary harness actually handles remote agents behind MCP today: tool calls over two minutes auto-background, MCP Tasks (public beta, Claude Code v2.1.304+) keep running on the server and survive exit, elicitation dialogs surface in /tasks, OAuth with fixed callback ports and pre-configured credentials, and 'channels' let a server push events into a session. Answers part of the long-running-agent-as-tool question for Claude Code specifically.

## Themes
- `remote-agent-invocation`: MCP call still running after 2 minutes moves to a background task (CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS); MCP Tasks extension jobs run on the remote server and can be followed after resume; non-interactive runs cancel input requests.
- `identity-delegation`: OAuth 2.0 for remote HTTP servers with `claude mcp login`, fixed callback port, pre-registered client id, `headersHelper` for non-OAuth auth.

## Key points
- Subagent calls, IDE servers and non-interactive runs do not auto-background.
- Channels: servers declaring `claude/channel` push CI results, alerts or chat messages into a session via `--channels`.
- Organisation controls on connector tools and `requiresUserInteraction` MCP tools exist (section beyond the read range).

## Could not verify
- Only the first 100k of 150k characters were read; `claude mcp serve` and organisation-controls sections were not read.
