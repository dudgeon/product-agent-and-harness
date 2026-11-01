---
title: "MCP Tasks and Events, Explained: Long-Running Tools and Agents That Wake Up"
source_url: https://upstash.com/blog/mcp-tasks-and-events
author: Cahid Arda Oz (Upstash)
publisher: Upstash blog
published: 2026-10-09
retrieved: 2026-10-31
type: article
evidence: vendor-claim
filed_by: research-agent-handoff-models
themes: [remote-agent-invocation, coordination-cost-and-waiting, harness-portability]
relevance: high
---

## Relevance to the project
A dated client-support table for the MCP Tasks extension and the proposed MCP Events, which are the two protocol pieces a long-lived dependency ask needs (start work that outlives a call; wake the agent when an owner responds). As of 2026-10-07 it reports that Claude Code, Codex, Cursor and OpenCode do not support Tasks, and only ChatGPT handles Events (via webhooks). That conflicts with Anthropic's Claude Code MCP docs, which describe MCP Tasks as a public beta from v2.1.304 ([Claude Code MCP](anthropic-claude-code-mcp-tasks-oauth.md), retrieved 2026-10-24); the gap is probably timing (support shipped after the table) but is unresolved. The fallback it offers, tasks as ordinary MCP tools with a task ID and status tool, works in every client today.

## Themes
- remote-agent-invocation: Tasks (`io.modelcontextprotocol/tasks`, shipped in the 2026-07-28 spec): server returns a task handle, client polls `tasks/get`; states working, input_required, completed, failed, cancelled.
- coordination-cost-and-waiting: Events are a working-group sketch with no SEP: `events/subscribe` with a callback URL, signed webhook deliveries with retries, subscriptions that expire unless refreshed; an event "wakes" the host so the agent can act when it is not running.
- harness-portability: client support uneven: ChatGPT no Tasks but Events via webhooks in Work chats; Codex no Tasks, Events only for OpenAI connectors; Claude Code neither (feature requests filed); Cursor and OpenCode neither; SDKs: C# and Rust support Tasks, TypeScript and Python not yet.

## Key points
- Fallback: `@upstash/mcp-toolkit/tasks` exposes a task tool returning a task ID plus `task_status` and `task_cancel` tools, with records in Redis and work on QStash or Upstash Workflow.
- Demo only (Report Desk, Deploy Watch on ChatGPT); an event notification arrived about three minutes after delivery; no production metrics or named customers.
- Each ChatGPT monitor gets its own callback URL, so the server does not learn which ChatGPT user it is (an identity gap for audit).

## Could not verify
- The table is the vendor's own test; the Claude Code docs disagree on Tasks support. Retention periods and session lifetimes not given.
