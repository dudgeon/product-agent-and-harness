---
title: "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud"
source_url: https://claude.com/resources/articles/introducing-the-claude-apps-gateway
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-06-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-control-plane, enterprise-admin-controls, cost-control-routing, identity-delegation]
relevance: medium
---

## Relevance to the project
A self-hosted control plane for Claude Code on Bedrock or Google Cloud: corporate SSO via OIDC, server-defined managed settings enforced per request, per-user spend caps and OTLP telemetry to the customer's own collector, with routing and failover across Claude API, Bedrock and Google Cloud. For a regulated company this is the pattern of keeping identity, policy and usage data inside its own network while still using the vendor harness. First-party launch post; Anthropic says it will publish the gateway protocol for other implementers.

## Themes
- agent-control-plane: single stateless container plus PostgreSQL holding the upstream credential, auth, policy, telemetry and routing (sections "Deploying the gateway", "How the gateway works").
- enterprise-admin-controls: managed settings defined once and enforced on every request; allowed models and defaults set centrally; onboarding/offboarding via the IdP.
- cost-control-routing: daily, weekly, monthly caps per org, group or user; optional provider failover.
- identity-delegation: OIDC relying party (Google Workspace, Entra ID, Okta); short-lived sessions, no long-lived secrets on laptops.

## Key points
- Replaces per-developer cloud credentials and manual settings pushes.
- Ships inside the same claude binary; /login is gateway-aware; clients apply managed settings at sign-in.
- No inference or usage data goes to Anthropic unless routed to the Claude API.
- Rollout via forceLoginMethod and forceLoginGatewayUrl in managed-settings.json.
- Limits: the post describes it for Claude Code only (other surfaces not mentioned); no audit-log detail beyond usage metrics.

## Could not verify
- Whether the protocol has been published or implemented by others.
