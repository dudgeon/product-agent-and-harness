---
title: "Meet the A2A CLI: discover, message, and manage agents from your terminal"
source_url: https://a2a-protocol.org/latest/blog/2026/10/01/introducing-a2a-cli/
author: A2A project
publisher: a2a-protocol.org blog
published: 2026-10-01
retrieved: 2026-10-31
type: article
evidence: first-party
filed_by: research-agent-handoff-models
themes: [remote-agent-invocation, single-agent-many-skills, harness-portability]
relevance: medium
---

## Relevance to the project
The A2A project's answer to coding harnesses lacking a native A2A client: an official `a2a` command-line client plus an Agent Skill that "teaches coding harnesses such as Claude Code, Cursor, and Codex" to call it. So a person's harness can reach a deployed A2A agent today through a skill wrapping a CLI, not through the harness itself. It updates the earlier finding that only Gemini CLI has a native client ([A2A follow-up](../../tasks/research-agent-runtime-patterns-taxonomy/followup-1-a2a-production.md)): still true for native clients, but the skill route now exists.

## Themes
- remote-agent-invocation: `a2a card get` to fetch an agent card; synchronous or asynchronous messages; follow a task through its lifecycle; `--stream`; JSON-RPC, REST or gRPC; JSON output and exit codes for scripts.
- single-agent-many-skills: install with `npx skills add https://github.com/a2aproject/a2a-cli --skill a2a-cli`; the CLI must be installed first.
- harness-portability: one skill for Claude Code, Cursor and Codex, because the harness only needs a shell.

## Key points
- `a2a server --echo` and `--exec` wrap a stdin/stdout program as an A2A server, for learning and testing, "not production".
- A2A v1.0, built on the A2A Go SDK.

## Could not verify
- Authentication options and input-required handling are not described; no adopters named.
