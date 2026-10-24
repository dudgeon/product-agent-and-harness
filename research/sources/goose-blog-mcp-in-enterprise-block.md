---
title: "MCP in the Enterprise: Real World Adoption at Block"
source_url: https://goose-docs.ai/blog/2025/04/21/mcp-in-enterprise/
author: Angie Jones (Head of Developer Relations, Block)
publisher: goose blog
published: 2025-04-21
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [single-agent-many-skills, pm-tool-connectivity, enterprise-admin-controls, harness-portability, non-engineer-builders, enablement-by-product]
relevance: high
---

## Relevance to the project
Block's earliest detailed account of goose as the company-wide agent: pre-installed, auto-configured models, a curated default bundle of internally written MCP servers, OAuth with keychain storage, and per-server LLM allowlists. It names which teams use it for what (design, product, support, risk among them). Self-reported time savings of 50-75% are the origin of later quoted figures.

## Themes
- single-agent-many-skills: one agent (CLI and desktop) with "default access to a curated set of approved MCP servers" (distribution).
- pm-tool-connectivity: named servers: Snowflake, GitHub, Jira, Slack, Google Drive, internal APIs for compliance checks and support triage (servers).
- enterprise-admin-controls: all internal MCP servers written by Block engineers; some servers enforce LLM allowlists or restrict sharing tool output across systems; goose restricted from certain sensitive data categories (governance).
- harness-portability: models hosted on Databricks via enterprise endpoints; Claude and OpenAI models under corporate agreements (governance).
- non-engineer-builders: design, product, support and risk use it for documentation, ticket triage and prototyping; data and ops for querying and reports (teams).
- enablement-by-product: pre-installation, bundled servers and auto-config sped adoption; weekly DevRel sessions, help channels, prompt sharing (education).

## Key points
- "Thousands of Block employees use the tool daily"; "Most employees report saving 50-75% of their time on common tasks" (self-reported, no method).
- Tool annotations (read-only/destructive) can trigger confirmation; more human-in-the-loop controls planned.
- OAuth flows run inside local MCP servers, described as temporary.
