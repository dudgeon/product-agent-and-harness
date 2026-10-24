---
title: How to develop an MCP Product Strategy
source_url: https://departmentofproduct.substack.com/p/how-to-develop-an-mcp-product-strategy
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-08-04
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [pm-tool-connectivity, agent-protocol-security, agent-as-service-many-surfaces]
relevance: low
---

## Relevance to the project
Written for PMs deciding whether their own product should ship an MCP server, so it bears on the project only indirectly: it describes what PM tools (Linear, Notion, Asana) exposed to agents in mid-2025 and frames the choice between being an MCP server inside someone else's agent and being the agent (MCP client) yourself, which is the same choice a company PM agent faces. Its most reusable point is Notion's (second-hand) decision to design "AI-first tools" with its own agent team rather than wrap existing API endpoints. Dated (August 2025) for tool counts and pricing.

## Themes
- pm-tool-connectivity: Linear's remote MCP had five tools (create/update/search issues, get user issues, add comment); Notion's had thirteen including cross-tool search (Notion, Slack, Drive, Jira). Compare [Notion MCP docs](notion-mcp-developer-docs.md). Cites Stripe's Jeff Weinstein that one-click Connectors raised installs 3.5x (second-hand).
- agent-as-service-many-surfaces: Intercom chose to make Fin an MCP client that reaches other tools, rather than let Claude-style clients abstract Fin away; Stripe is happy to be invisible behind agents (section 1).
- agent-protocol-security: cites the Asana and GitHub MCP incidents; broad read/write scopes are hard to avoid; points to the [MCP authorization spec](mcp-authorization-spec-draft.md) (OAuth, reject tokens with excessive or irrelevant scopes) (section 4).

## Key points
- Five questions: do users want it (unofficial community servers are a demand signal); what will it do (agent-friendly tools, not one tool per endpoint, citing Docker's guidance and Notion); monetisation (mostly free; Intercom priced per outcome at $0.99; Stripe added paid MCP access); security; how it differs from an API strategy (the user is the agent), with API PMs likely owning MCP.
- Shift to remote, centrally hosted servers attributed to an Anthropic talk.

## Could not verify
- The 3.5x install figure, the Asana/GitHub incident details and Intercom's per-outcome MCP pricing (not linked to primaries in the text).
