---
title: "Features of AgentCore Identity (Amazon Bedrock AgentCore Developer Guide)"
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html
author: Amazon Web Services
publisher: AWS documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [identity-delegation, agent-stewardship]
relevance: medium
---

## Relevance to the project
AWS's agent identity layer: a directory of agent workload identities with ARNs organised hierarchically, a token vault for OAuth tokens and API keys, built-in OAuth providers for Jira, Slack, GitHub, Salesforce, and logged per-request verification. Notably its "on behalf of users" model is described as impersonation using provided credentials, which is weaker for audit than the delegation semantics of RFC 8693.

## Themes
- identity-delegation: supports client-credentials (2LO) and authorization-code (3LO) flows; "impersonation flow where agents can access resources using credentials provided to them" (Agent identity and access controls).
- agent-stewardship: a unified directory "acts as the single source of truth for all agent identities", with ARN paths (`.../directory/default/workload-identity/agent-name`) for policy at different levels (Centralized agent identity management).

## Key points
- Token vault encrypted with KMS; every access validated independently "even from callers within the same trust domain".
- SDK annotations `@requires_access_token`, `@requires_api_key`; automatic consent URL generation.
- All operations logged for monitoring and compliance.
