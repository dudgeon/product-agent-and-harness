---
title: "Block's Playbook for Designing MCP Servers"
source_url: https://engineering.block.xyz/blog/blocks-playbook-for-designing-mcp-servers
author: Salman Mohammed and Kalvin Chau (Block)
publisher: Block Engineering Blog
published: 2025-06-16
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [pm-tool-connectivity, single-agent-many-skills, human-review-gates, cost-control-routing, identity-delegation]
relevance: high
---

## Relevance to the project
Block's own design rules for the 60+ internal MCP servers that give goose its capabilities. It shows how Block packages capability for one general agent: few workflow-shaped tools per system, each with a single risk level so approval can be automated, with OAuth handled at first use. It bears on how a PM-facing harness should expose tools like Linear or calendars (query languages over synced data rather than endpoint mirrors).

## Themes
- pm-tool-connectivity: Linear MCP went from 30+ tools mirroring GraphQL queries (4-6 calls per simple question) to two tools, `execute_readonly_query` and `execute_mutation_query` (Linear MCP example section).
- single-agent-many-skills: capability arrives as MCP servers into one agent; "more than 60 MCP servers" developed at Block (intro).
- human-review-gates: goose permission levels Always Allow / Allow Once / Denied; each tool should carry one risk level (read-only or write) so users can judge risk; `readOnlyHint` annotations drive goose's smart approval (permissions section).
- cost-control-routing: keep instructions static so prompt prefix caching works; watch `cache_read_input_tokens` (prefix caching section).
- identity-delegation: OAuth authorization-code flow, triggered on first use, minimum scopes, tokens in the OS keychain, revoked when the extension is removed (auth section).

## Key points
- "Design top-down from workflows, not bottom-up from API endpoints" (best practices).
- Google Calendar MCP v2 syncs events into DuckDB and exposes one `query_database` SQL tool plus macros such as `free_slots`; v1 was a thin API wrapper that could not answer analytic questions.
- LLM strengths to lean on: SQL over tidy tables, Markdown/Mermaid; weaknesses: long tool chains, strict JSON, long generated names.
- goose uses MCP server instructions to build its system prompt; its file reader rejects files over 400KB with an actionable error.
- Errors should be actionable so the agent can recover.

## Could not verify
- No list of Block's 60+ servers beyond Calendar and Linear; no adoption numbers.
