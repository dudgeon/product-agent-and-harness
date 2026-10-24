---
title: "Oz Cloud Agents & Orchestration (Warp docs)"
source_url: https://docs.warp.dev/agent-platform/cloud-agents
author: Warp
publisher: Warp docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, remote-agent-invocation, cost-control-routing, meta-harness]
relevance: medium
---
## Relevance to the project
A terminal vendor's cloud agent platform with the team features that matter here: scheduled and event-triggered runs, session-sharing links teammates can attach to and steer, a runs dashboard showing creator and credit usage, centrally configured MCP/secrets, and self-hosted workers. Also states there is no BYO key for cloud runs.

## Themes
- shared-persistent-sessions: cloud run transcripts open in session sharing; a teammate can attach to a running task to monitor or steer it; Runs pages show status, trigger, creator and credit usage
- remote-agent-invocation: triggers from Slack, Linear, schedules, CLI, API/SDK; self-host via managed Docker worker or unmanaged `oz agent run` in CI/Kubernetes
- cost-control-routing: runs incur platform plus compute plus inference charges; personal BYOK not supported for cloud runs; team-managed inference on Business/Enterprise

## Key points
- Identity and run-permission rules live on a separate reference page that was not read; concurrency limits not stated.

## Could not verify
- Permissions reference and independent evidence not found.
