---
title: cloudflare/cloudflare-os (README)
source_url: https://github.com/cloudflare/cloudflare-os
author: Cloudflare
publisher: GitHub
published: 2026-10-24
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, build-vs-buy, harness-portability]
relevance: high
---

## Relevance to the project
The code-level truth of Cloudflare OS: what is open, what is tied to Cloudflare's platform, and its maturity. Shows the 'agent' is a built-in general Code Mode agent on Pi, not a wrapper over Claude Code or Codex.

## Themes
- [[harness-portability]]: built-in agent is a Code Mode agent that writes and runs code; provider abstraction through Pi (`pi-agent-core`). No Claude Code/Codex wrapping.
- [[build-vs-buy]]: designed to be forked into '<Your Company> OS'; self-hosting on workerd marked COMING SOON, so today it depends on Cloudflare's platform.
- [[shared-persistent-sessions]]: each workspace is a Durable Object; gadgets (apps) are per-user sandboxes; blueprints copy code only.

## Key points
- Apache-2.0; version 2 'early access' with 'many rough edges'; about 11.6k stars, 1.4k forks, 86 open issues, 994 commits at retrieval.
- Packages: workshop-backend ('kernel'), workshop-frontend ('shell'), gatekeeper-* ('drivers'). Gatekeepers for GitHub, Google, Cloudflare, Supabase, Notion, Confluence, Email, Slack and others; each needs per-service OAuth configuration.
- External contributions are discouraged (only tiny verified fixes). Repo holds `.agents/skills` and AGENTS.md, i.e. it is itself developed with agents.

## Could not verify
- Which models/providers work out of the box is not listed.
