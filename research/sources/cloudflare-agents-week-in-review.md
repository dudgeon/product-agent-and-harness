---
title: Building the agentic cloud: everything we launched during Agents Week 2026
source_url: https://blog.cloudflare.com/agents-week-in-review/
author: Cloudflare
publisher: Cloudflare Blog
published: 2026-04-20
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, shared-persistent-sessions, agent-frameworks, cost-control-routing]
relevance: high
---

## Relevance to the project
Index of Cloudflare's 'agentic cloud' components: Sandboxes, Artifacts (Git for agents), Workflows, Mesh, Managed OAuth for Access, Agent Memory, Project Think. Shows the infrastructure-vendor route: provide primitives and let any harness or framework run on them.

## Themes
- [[shared-persistent-sessions]]: Sandboxes GA (persistent isolated environments), Durable Object Facets (per-app SQLite), Agent Memory (managed persistent memory), Workflows control plane for 50,000 concurrent runs.
- [[remote-agent-invocation]]: Managed OAuth for Access (RFC 9728) lets agents authenticate on a user's behalf without service accounts; Mesh gives scoped private-network access to agents.
- [[agent-frameworks]]: Project Think previews the next Agents SDK.
- [[cost-control-routing]]: AI inference layer with 14+ providers; MCP reference architecture using Access, AI Gateway and MCP server portals.

## Key points
- Groups: Compute (Artifacts, Sandboxes GA, Outbound Workers for Sandboxes that inject credentials, Facets, Workflows), Security (Mesh, Managed OAuth, non-human identity, MCP governance), Agent Toolbox (Think, voice, Email Service, inference, Agent Memory, AI Search, Browser Run), Prototype to Production (cf CLI, Agent Lee, Flagship, PlanetScale, Registrar API), Agentic Web.
- Framing: 'Cloud 2.0, the agentic cloud', infrastructure for agents as a primary workload. The kickoff post (2026-04-12) argues the cloud was built one-to-many and agents are one-to-one, hence V8 isolates over containers.
- Media call this Cloudflare's 'agent cloud'; the blog's own term is 'agentic cloud'.
- The recap does not mention Claude Code or Codex. The Sandbox docs separately have a 'coding agents' guide for running Claude Code, Codex or Devin in a per-task sandbox.

## Could not verify
- Per-product GA status beyond the recap list not checked; Sandbox SDK docs page does not state overall GA vs beta (labels one scheduling policy 'public beta').
