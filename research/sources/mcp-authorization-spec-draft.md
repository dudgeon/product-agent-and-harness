---
title: MCP Authorization specification (draft)
source_url: https://modelcontextprotocol.io/specification/draft/basic/authorization
author: Model Context Protocol project
publisher: modelcontextprotocol.io
published: 2026
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, identity-delegation]
relevance: high
---

## Relevance to the project
Defines how a harness authenticates to a remote MCP server (including one that fronts an agent): OAuth 2.1, protected-resource metadata, resource indicators, token audience binding, step-up scopes. Crucially servers must not accept or pass through tokens issued for other resources, so 'agent acting on the user's behalf downstream' needs token exchange or a vault, not forwarding the user's token.

## Themes
- `identity-delegation`: MCP servers MUST validate tokens are issued for them (RFC 8707 audience) and MUST NOT accept or transit any other tokens; Enterprise-Managed Authorization extension exists but its content was not read.

## Key points
- MCP server is an OAuth 2.1 resource server; client discovers the authorization server via RFC 9728 protected-resource metadata; PKCE and `resource` parameter mandatory.
- Client registration order: Client ID Metadata Documents (preferred), pre-registration, Dynamic Client Registration (deprecated).
- Step-up authorization: 403 `insufficient_scope` with required scopes; clients retry a few times then treat as permanent failure.
- Authorization is optional in the spec; stdio servers should take credentials from the environment.

## Could not verify
- The Enterprise-Managed Authorization extension (ext-auth) was only listed as Stable; its mechanism (cross-app access / identity assertion) was not read.
