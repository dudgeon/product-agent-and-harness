---
title: "Port MCP server: overview and installation"
source_url: https://docs.port.io/ai-interfaces/port-mcp-server/overview-and-installation
author: Port
publisher: Port documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-originated-requests, agent-legible-platform, onboarding-as-code]
relevance: high
---

## Relevance to the project
Port's remote MCP server lets an agent read the software catalog (blueprints, entities, scorecards) and run self-service actions, the portal's "request a resource" forms, as the authenticated user. Combined with Port's per-action approval settings (see `port-docs-self-service-action-rbac`), it is an internal developer portal where an agent can submit a platform request that then waits for human approval.

## Themes
- agent-originated-requests: a `run_action` tool; by default "all actions you have permission to run will be available".
- agent-legible-platform: blueprint, entity and scorecard tools expose the catalog and its standards to agents.
- onboarding-as-code: controls: `x-read-only-mode` hides write tools; `x-allowed-actions-to-run` allowlists actions (empty blocks all).

## Key points
- OAuth sessions up to 30 days, ending after 15 days idle; tied to the org selected at consent.
- Older local (Docker/uvx) server deprecated; it had no action-run tools.

## Could not verify
- Whether approval workflows apply to actions run through MCP (not stated on this page).
