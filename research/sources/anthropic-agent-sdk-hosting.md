---
title: Hosting the Agent SDK (Claude Code docs)
source_url: https://code.claude.com/docs/en/agent-sdk/hosting.md
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, shared-persistent-sessions, cost-control-routing]
relevance: high
---

## Relevance to the project
The best primary account of what it costs operationally to run a vendor-SDK harness as a deployed service: every session is a long-lived CLI subprocess with local disk state. It shows what is left to the builder (session storage, isolation, scaling, observability) even when the loop is bought.

## Themes
- shared-persistent-sessions: names four session patterns (ephemeral, long-running, hybrid with SessionStore, multi-agent container); transcripts live on local disk unless a SessionStore adapter is configured.
- agent-frameworks: lists what the builder must still provide: sandbox, multi-tenant isolation, egress proxy, auth gateway, durable storage, OTel collector.
- cost-control-routing: states token cost typically dominates container cost by an order of magnitude; a minimal container is roughly $0.05/hour.

## Key points
- SDK spawns and supervises a claude CLI subprocess owning shell, cwd and session files; hosting is not like a stateless API wrapper.
- Guidance: about 1 GiB RAM, 5 GiB disk, 1 CPU per agent as a floor; pin sessions to containers by consistent hashing.
- SessionStore mirrors transcripts only, not CLAUDE.md memory or working-directory artifacts; mirror writes are best-effort (mirror_error messages).
- Multi-tenant leak risk: default behaviour reads settings and CLAUDE.md from the filesystem; must set settingSources, disable auto memory, per-tenant config dir and cwd.
- Known limitations: no top-level session timeout, memory growth in long sessions, parallel subagent fanouts can hit rate limits, no per-subagent wall-clock deadline.
- Points to Managed Agents if you do not want to run the loop yourself.
