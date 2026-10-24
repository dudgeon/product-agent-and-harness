---
title: AI agent sandboxes: survey of 23 tools
source_url: https://rywalker.com/research/ai-agent-sandboxes
author: Ry Walker (CEO, Tembo; disclosed)
publisher: rywalker.com
published: 2026-09-15
retrieved: 2026-10-24
type: report
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, remote-agent-invocation, build-vs-buy]
relevance: medium
---

## Relevance to the project
The session-runtime layer (E2B, Modal, Daytona, Vercel Sandbox, Cloudflare and others) as a comparison, with a disclosed conflict. Key for the runtime-location axis: what persists (files vs memory vs processes), isolation tech and open-egress risks.

## Themes
- [[shared-persistent-sessions]]: persistence differs: E2B pause/resume can keep memory; Daytona keeps memory only in VM classes; Cloudflare keeps sandbox identity, not a stopped container's files; restoring a checkpoint does not undo external effects.
- [[remote-agent-invocation]]: Firecracker microVMs (E2B, Vercel, Blaxel, Sprites), gVisor (Modal), containers (Daytona tier); egress often open by default; injected env-var credentials are readable by guest code.
- [[build-vs-buy]]: ownership churn: Baseten announced acquiring Blaxel 2026-09-10; Daytona reportedly moved its open core private (June 2026, search-result claim).

## Key points
- Many products beta/preview (Modal VM Sandboxes, Cloudflare 1.0, Microsandbox, OpenShell alpha). No hands-on benchmark or audit in the report.
- A separate 'AI Code Sandbox Benchmark 2026' (superagent.sh, Jan 2026) was read but has no documented methodology, so it is not filed.

## Could not verify
- Author's company (Tembo) is a competitor in the 'team coding-agent delivery' category.
