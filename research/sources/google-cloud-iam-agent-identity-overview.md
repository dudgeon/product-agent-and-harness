---
title: "Agent Identity overview (Google Cloud IAM)"
source_url: https://docs.cloud.google.com/iam/docs/agent-identity-overview
author: Google Cloud
publisher: Google Cloud documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [identity-delegation, agent-stewardship, stale-records-mislead-agents]
relevance: medium
---

## Relevance to the project
Google gives each deployed agent a SPIFFE-based, attested identity that is a first-class IAM principal, and records both agent and user identities in audit logs when the agent acts for a user. It is the clearest workload-identity (SPIFFE) answer to "which agent made this request", which a platform's decision record needs; its lifecycle caveat (bindings outlive the agent) is a concrete staleness risk.

## Themes
- identity-delegation: acting for a user uses 3-legged OAuth via the Agent Identity auth manager; acting on its own authority uses its own identity or OIDC ID tokens; "logs show both the agent's and the user's identities" (Auth, Audit).
- agent-stewardship: SPIFFE ID `spiffe://agents.global.org-ORG_ID.system.id.goog/resources/...` mapped to the hosting resource; X.509 certs valid 24h, auto-renewed; mTLS default, DPoP across Agent Gateway.
- stale-records-mislead-agents: "Deleting an agent doesn't remove the IAM bindings that reference its principal"; a redeployed agent gets a new principal needing new grants (Lifecycle).

## Notable quotes
- "Agent Identity provides a strongly attested, cryptographic identity for each agent."

## Could not verify
- Preview vs GA status (not stated).
