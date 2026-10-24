---
title: Stateless MCP has recaptured my interest
source_url: https://simonwillison.net/2026/Jul/31/stateless-mcp/
author: Simon Willison
publisher: simonwillison.net
published: 2026-07-31
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability]
relevance: medium
---

## Relevance to the project
An influential independent practitioner reverses his 2025 skepticism: stateless MCP is simple to host, and named tools are easier to audit than giving an agent shell plus internet. Relevant to the argument that exposing a bounded capability over MCP is a safer boundary than letting a general harness do everything. It says nothing about tasks, auth or agent-as-tool.

## Themes
- `remote-agent-invocation`: 'MCP tools are easier to audit and control' than shell plus open internet; one HTTP request per call; hosted Datasette MCP endpoint usable from Claude and ChatGPT.

## Key points
- MCP lost mindshare in 2025 to Skills because a terminal and curl did much of the same job.
- He built mcp-explorer, datasette-mcp (list_databases, get_database_schema, execute_sql read-only) and llm-mcp-client in a week.
- Security view shifted: end-user mixing of tools pushed exfiltration risk to users; bounded server-side capabilities are easier to reason about.

## Notable quotes
- "MCP tools are easier to audit and control" (Willison, 2026-07-31)
