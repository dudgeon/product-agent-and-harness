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

## Follow-up (2026-10-24)
Filed by research-runtime-patterns-follow-up-round (codex-copilot-admin comparison). Read the remainder of the page (from character 100,000) for the managed-MCP sections only; the separate managed-mcp page was not read.
- Central control: the page points to "Managed MCP configuration" for deploying a fixed server set with `managed-mcp.json`, providing servers to every user with `managedMcpServers`, and restricting servers with `allowedMcpServers` and `deniedMcpServers`. Entries match by `serverName` or `serverUrl` pattern (e.g. a `serverName` of "claude.ai Slack" blocks that connector).
- Coverage by surface: terminal, VS Code, JetBrains and Agent SDK sessions honour these settings and managed MCP; cloud sessions honour allow/deny entries that reach the session (e.g. via server-managed settings), but "The session's proxy rewrites each connector's URL, so a `serverUrl` pattern written for the connector's own URL doesn't match it"; a `managed-mcp.json` on a self-hosted runner host drops delivered claude.ai connectors.
- Gap: in Desktop app local and SSH sessions, connectors are registered as in-process `type: "sdk"` servers "and no MCP setting or `managed-mcp.json` reaches them"; the org can only block a connector's tools or turn off Claude Code in the desktop app.
- `headersHelper` runs as an arbitrary shell command; since v2.1.238 it runs for project-scoped servers only after the folder trust dialog is accepted (earlier, `claude -p` and SDK sessions ran helpers without the trust check).
- Comparison: Codex `requirements.toml` and Copilot `managed-settings.json` offer equivalent MCP allowlists, with Codex matching on command+args or URL and Copilot on URL, command or name (name called "not a security control"); see [Codex managed configuration](openai-codex-managed-configuration.md) and [Copilot managed settings](github-copilot-enterprise-managed-settings.md).
- Model-summarised fetch; wording should be rechecked before quoting.
