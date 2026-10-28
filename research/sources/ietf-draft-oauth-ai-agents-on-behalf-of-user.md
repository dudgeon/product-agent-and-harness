---
title: "OAuth 2.0 Extension: On-Behalf-Of User Authorization for AI Agents (draft-oauth-ai-agents-on-behalf-of-user-02)"
source_url: https://datatracker.ietf.org/doc/html/draft-oauth-ai-agents-on-behalf-of-user-02
author: T. S. Senarath, A. Dissanayaka (WSO2)
publisher: IETF Datatracker (individual Internet-Draft)
published: 2025-08-26
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [identity-delegation, decision-rights-for-agents]
relevance: medium
---

## Relevance to the project
One of the concrete IETF proposals for making "agent acting for a user" a first-class OAuth flow: the user consents to a named agent at the authorisation endpoint, and the resulting token records user, client and agent separately (`act.sub`), giving an auditable delegation chain. It matters for the dependency agent because a platform that records "requested by agent X for person Y" needs exactly this token shape; it is an individual draft, not a standard.

## Themes
- identity-delegation: `requested_actor` at the authorisation endpoint binds the code to user, client and agent; the agent presents an `actor_token` at the token endpoint; the access token has the user in `sub`, the client in `azp`/`client_id`, the agent in `act.sub` (Mechanism).
- decision-rights-for-agents: a resource server can trigger the flow with 401/403 and `WWW-Authenticate`, prompting fresh consent for the agent.

## Key points
- Argues RFC 8693 is mainly for server-side exchange/impersonation and does not natively support front-channel user consent for a specific agent, nor specify how the subject token is obtained.
- Revision -00 (May 2025) used a `requested_agent` parameter and a dedicated grant type; -02 dated 26 Aug 2025, expiry 27 Feb 2026; not adopted by the OAuth WG as of April 2026 (secondary).

## Could not verify
- Whether a later revision exists or the draft has expired.
