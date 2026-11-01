---
title: Subagents (LangChain multi-agent docs)
source_url: https://docs.langchain.com/oss/python/langchain/multi-agent/subagents
author: LangChain
publisher: LangChain docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, task-context-isolation, remote-agent-invocation]
relevance: high
---

## Relevance to the project
Names the three input options for a called sub-agent (isolated task string, forked full history, custom slice of parent state) and the default output (final message only), plus an async start/check/get pattern for long work. The async pattern is the in-runtime shape of a long-lived dependency ask that the main agent checks on later.

## Themes
- handoff-context-transfer: "Passing only the task description (`query`) keeps the subagent isolated"; a forked subagent "receives the parent's full message history (including tool calls) and system prompt" (Deep Agents); "the supervisor only sees the final output", so subagents must put results in the final message.
- task-context-isolation: isolated by default; forked or custom only when prior work must carry over.
- remote-agent-invocation: async mode uses three tools (start job, check status, get result) so "users should be able to keep chatting" while independent work runs.

## Key points
- Sync is the default: "the main agent waits for each subagent to complete before continuing".
- A `Command` can return extra state alongside the text.

## Could not verify
- No data on isolated versus forked quality.
