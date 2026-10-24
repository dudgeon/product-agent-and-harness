---
title: "How Ramp built a full-context background coding agent on Modal"
source_url: https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal
author: Greta Workman (Modal)
publisher: Modal blog
published: 2026-02-19
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, cost-control-routing, non-engineer-builders, agent-factory-sdlc]
relevance: high
---
## Relevance to the project
Infrastructure-level account of Ramp Inspect (Modal sandbox per session, snapshots every 30 minutes, queues routing prompts from many clients into one session). Complements the existing Pragmatic Summit note by naming the coordination primitives behind 'multiplayer'. Written by the infrastructure vendor about a customer, so promotional.

## Themes
- shared-persistent-sessions: each session gets its own Modal sandbox; Modal Dicts hold session locks, Modal Queues route prompts from any client into the right session so several clients feed one session without conflict
- cost-control-routing: sessions start in seconds from a filesystem snapshot refreshed by a cron every 30 minutes (repos cloned, dependencies installed, build run); startup speed framed as the adoption driver
- non-engineer-builders: clients are Slack, a web UI with hosted VS Code and VNC, and a Chrome extension for non-engineers to select UI elements; roughly half of merged PRs started by Inspect within months

## Key points
- Sandbox bundles Postgres, Redis, Temporal, RabbitMQ, OpenCode, VS Code server, VNC/Chromium; integrates GitHub, Slack, Buildkite, Sentry, Datadog.
- Hundreds of concurrent sessions reported; agents can spawn child sessions across repos; over 80% of Inspect's own code written by Inspect (Modal's account of Ramp's claim).
- Not covered by the post (per retrieval): cost, authentication, and how session state is stored. Other summaries cite 30%/40%/over half merged-PR figures that differ by date.

## Could not verify
- Cost, auth model and session persistence mechanism not described.
