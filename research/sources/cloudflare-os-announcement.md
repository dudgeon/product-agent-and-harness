---
title: Cloudflare OS: an open platform for agents, apps, and work
source_url: https://blog.cloudflare.com/cloudflare-os
author: Cloudflare (page lists Phillip Jones, Dan Carter)
publisher: Cloudflare Blog
published: 2026-08-05
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, remote-agent-invocation, cost-control-routing, build-vs-buy, harness-portability]
relevance: high
---

## Relevance to the project
This is the Cloudflare offering the research plan meant. It is not a meta-harness over Claude Code/Codex: it is an org-deployable, per-employee agent workspace on Cloudflare's own primitives, with a capability-based security model. It is the strongest example found of the 'deployed, shared, persistent' end of the runtime-location axis, and of governance by observation logging.

## Themes
- [[shared-persistent-sessions]]: browser workspace with persistent sessions/state; apps are private by default, shareable live (shared state) or as 'blueprints' (code only, no data).
- [[cost-control-routing]]: all inference through AI Gateway; requests attributed to person/team/workspace; budgets, rate limits, behaviour at limit set by admins.
- [[build-vs-buy]]: Cloudflare built it internally first (v1 in May 2026), rebuilt as v2 and open-sourced; partners Presidio and Happy Cog help customise.
- [[harness-portability]]: works with any model, but the post names no external harness (no Claude Code/Codex); portability is at the model layer, not harness layer.
- [[remote-agent-invocation]]: agents call the same server methods as the UI over Cap'n Web; 'agents can use your tool to do the job when you're not there'.

## Key points
- Three parts: agent workspace (sessions, files, isolated runtime to write/run code), security and governance framework, platform for personal modifiable apps.
- Security: Cloudflare Access gates entry; agents start with zero access; resources granted as typed bindings, credentials never exposed to agent code; server code in Dynamic Workers with global outbound disabled; client code in sandboxed frames.
- Gatekeepers: per-service Workers that handle OAuth, hold credentials, enforce policy, log reads, mediate side effects (example: limit to one GitHub repo, allow issue reads but not code, require approval before merge).
- Observation-based policy: every resource an agent has observed is logged; when another person opens the workspace, Gatekeepers re-check that person's access to those resources; the log can block risky actions after a sensitive read (writes, invites, hand-offs to another agent, outbound requests).
- Apps: Dynamic Worker + Durable Object Facet with its own SQLite; no dedicated server/container. Workflows can run on demand, on schedule, or on events; predictable steps run as code and the model only where judgement is needed.
- Open source (core repo + cloudflare-os-starter). Planned: fully managed version in the dashboard, containers for dev workflows, workspaces in Slack and chat tools. Early access, with a rewrite described as having rough edges (see repo note).
- Origin: v1 launched to all employees in May 2026; limits found: static apps, token cost re-running routine jobs, MCP access not showing which data an agent had seen, which became a security problem once sharing arrived.

## Notable quotes
- "So if you can build a tool to do a job yourself, agents can use your tool to do the job when you're not there."

## Could not verify
- License named only in the repo (Apache-2.0), not in the post. Authorship shown only via sidebar.
