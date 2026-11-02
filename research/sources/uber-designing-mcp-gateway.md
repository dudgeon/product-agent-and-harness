---
title: "Designing MCP Gateway: Uber's MCP Management Platform"
source_url: https://www.uber.com/us/en/blog/designing-mcp-gateway/
author: Alok Srivastava, Deepanshu Mehndiratta, Gaurav Gill (Uber)
publisher: Uber Engineering Blog
published: 2026-10-01
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [legible-org-for-agents, agent-legible-platform, agent-control-plane, identity-delegation, enterprise-admin-controls, governance-as-code]
relevance: high
---

## Relevance to the project
Uber's design write-up of the MCP Gateway shows how one platform turns thousands of existing internal APIs into agent tools while keeping owners in control: a registry (control plane) and proxy (data plane), an AutoCrawler that generates tools from the IDL registry, and a rule that every generated tool starts disabled until its owning team reviews and enables it. It is the tool layer under Cortana and Minion, and the clearest evidence for "existing APIs are the fastest way to give agents tools". It bears on the agent-legible platform and admin-control questions: who owns a tool, who can call it, and how description changes are reviewed.

## Themes
- agent-legible-platform: AutoCrawler (a Cadence workflow) scans Uber's IDL registry on a schedule and creates virtual MCP servers and tools over HTTP, gRPC and TChannel APIs; native servers are built with MCPFx (Architecture).
- governance-as-code: "Every MCP server and tool starts in a disabled state and must be explicitly reviewed and enabled by the owning team"; every tool-description change is a config diff the owner approves, with rollback (Authoring).
- identity-delegation: for third-party servers (Jira, Google) the gateway relays the caller's user token downstream for exchange; authorization via Uber's access control system with charter policies per server and optional per-tool overrides, applying to humans, services and agents (Security).
- enterprise-admin-controls: tool-level authorization, rate limiting and sensitive-data redaction at the gateway (Security).
- legible-org-for-agents: Omni MCP exposes just four tools (discover_server, discover_tools, get_tool_schema, invoke_tool); response projection lets the model ask for nested field paths only; `aifx mcp list|search|call` CLI, with code mode now the default for coding agents (Consumption).

## Key points
- Scale: over 800 MCP servers and over 5,000 tools; "thousands" of internal services; "hundreds of teams" exploring agentic workflows. (The August cost post says 1,000+ servers; the talk said 1,000+ tools; counts drift by source and date.)
- Proxy Gateway executes requests through Muttley (service-mesh sidecar), so it inherits existing routing; config refreshes without restarts.
- Registry is the source of truth for discovery, ownership and enablement.
- Contributors listed in bios include Uday Kiran Medisetty; one bio mentions a "Skills Marketplace".

## Notable quotes
- "It's a foundational microservice that powers all MCP interactions at Uber" (Introduction)
- "existing APIs are the fastest way to provide tools to an agent" (Conclusion)

## Could not verify
- Spire / SPIFFE and on-behalf-of chains are not named here; see the agent-identity post for the actor-chain design.
- No mention of Cortana, Minion, personas, DevPods or the context graph.
- The "40% token savings" from the talk is not restated in this post.
