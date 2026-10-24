---
title: Cursor Cloud Agents API (v1, public beta)
source_url: https://cursor.com/docs/cloud-agent/api/overview
author: Cursor (Anysphere)
publisher: cursor.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation]
relevance: medium
---

## Relevance to the project
A public API for launching and steering Cursor's background agents from any system (so a primary harness or CI can delegate): durable agents with runs, SSE streaming with Last-Event-ID resume, steering a running turn, artifacts, service-account keys, worker pools. Public beta, webhooks missing in v1.

## Themes
- `remote-agent-invocation`: `POST /v1/agents` creates agent and first run (prompt, repos, model, MCP servers, auto-PR); one active run per agent (409 agent_busy) or `steer`; cancel, per-run token usage, artifacts.

## Key points
- Auth: user API key or service account key; repos from GitHub, GitLab, Bitbucket Cloud, Azure DevOps.
- Agent status ACTIVE/IDLE/ARCHIVED; run state separate.
- Pricing not in the fetched text; page truncated near the end.

## Could not verify
- Pricing and last ~33k characters not read.
