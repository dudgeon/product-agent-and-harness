---
title: "Building agents that reach production systems with MCP"
source_url: https://claude.com/resources/articles/building-agents-that-reach-production-systems-with-mcp
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-04-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [pm-tool-connectivity, harness-portability, skill-standards, identity-delegation, task-context-isolation]
relevance: medium
---

## Relevance to the project
Anthropic's case for MCP over direct API calls and CLIs once agents run in the cloud, with concrete design rules for the connectors a PM/analyst agent would need: remote servers, tools grouped by intent, code orchestration for large surfaces, elicitation, CIMD OAuth and Managed Agents vaults for token custody. It also sets out how skills pair with MCP (bundled as plugins, or served from the MCP server) and context-saving client patterns (tool search, programmatic tool calling). First-party advocacy for its own protocol; the efficiency numbers are Anthropic's internal testing.

## Themes
- pm-tool-connectivity: three connection paths (direct API, CLI, MCP) and why cloud agents reaching auth'd systems land on MCP (section "Connecting agents to external systems").
- harness-portability: one remote server reaches Claude, ChatGPT, Cursor, VS Code; skills-from-server extension aims to make skill pairing portable across clients (sections "Build remote servers", "Distribute skills from an MCP server").
- skill-standards: skills teach procedure, MCP gives access; data plugin for Cowork = 10 skills + 8 MCP servers (section "Pairing MCP servers with skills").
- identity-delegation: CIMD client registration; vaults hold users' OAuth tokens and inject them per MCP connection (section "Lean on standardized auth").
- task-context-isolation: tool search cuts tool-definition tokens 85%+; programmatic tool calling about 37% fewer tokens on complex workflows (section "Making MCP clients more context-efficient").

## Key points
- **M x N problem**: direct API calls make each agent-service pair bespoke; CLIs are a thin common layer limited to filesystem/shell environments with on-disk credentials; MCP standardizes auth, discovery and semantics.
- **Private networks**: MCP tunnels in Claude Managed Agents connect over outbound-only connections, no exposed ports.
- **Adoption claims (Anthropic)**: MCP SDKs >300M downloads/month (from 100M at start of year); 200+ servers in Anthropic's directory; MCP underpins Cowork, Managed Agents and Claude Code channels.
- **Server design**: group tools by intent (create_issue_from_thread vs four primitives); for huge APIs expose search/execute over code (Cloudflare: two tools, ~2,500 endpoints, ~1K tokens); MCP Apps for inline UI (said to raise adoption, unquantified); elicitation form mode for missing params or confirming destructive actions, URL mode for OAuth/payments so credentials never transit the client.
- **Mature integrations ship all three**: API foundation, CLI for local, MCP for cloud agents.
- Limits: no failure modes or security risks of MCP discussed (prompt injection, server trust); numbers are internal tests.

## Notable quotes
- "Group tools around intent, not endpoints."

## Could not verify
- Download and token-saving figures; the "meaningfully higher adoption" claim for MCP Apps.
