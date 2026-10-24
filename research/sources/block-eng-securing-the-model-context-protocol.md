---
title: Securing the Model Context Protocol
source_url: https://engineering.block.xyz/blog/securing-the-model-context-protocol
author: Alex Rosenzweig with Block InfoSec contributors
publisher: Block Engineering Blog
published: 2025-03-31
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-protocol-security, skill-supply-chain-security, enterprise-admin-controls, human-review-gates]
relevance: medium
---

## Relevance to the project
Block InfoSec's threat model for MCP, written as goose spread internally. It frames the agent as a non-deterministic client that may call any exposed tool and the MCP server as a client library, and recommends allowlists of pre-validated servers for enterprise agents. It is the rationale behind Block's internal MCP allowlist; it does not describe the review process itself.

## Themes
- agent-protocol-security: four areas: agent-to-MCP communication, MCP-to-tool connectivity, identity (user, agent, device), host and supply chain (threat model).
- skill-supply-chain-security: most MCP servers install via docker, uvx, pipx or npx, i.e. arbitrary code execution; install only from trusted sources, verify integrity, use allowlists (supply chain).
- enterprise-admin-controls: MCP implementations may declare which LLM providers they can be used with; enterprise agents should allowlist pre-validated MCPs (governance).
- human-review-gates: human approval for higher-risk actions; welcomes `readOnly`/`destructive` tool annotations.

## Key points
- Agents, not individual MCP servers, should orchestrate browser OAuth; the server exchanges third-party tokens for its own.
- No numbers; no description of Block's server registry or review board.
