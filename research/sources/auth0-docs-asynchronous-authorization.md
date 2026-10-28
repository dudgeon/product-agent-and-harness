---
title: "Asynchronous Authorization (Auth0 for AI Agents)"
source_url: https://auth0.com/ai/docs/intro/asynchronous-authorization
author: Auth0 (Okta)
publisher: Auth0 docs
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [identity-delegation, human-review-gates, agent-originated-requests]
relevance: medium
---

## Relevance to the project
A standards-based pattern for an agent to ask a specific human to approve a specific action out of band: the agent's backend starts a CIBA request carrying a Rich Authorization Request payload that describes the exact transaction, the user approves on a trusted device, and only then does the agent receive a token. This is the mechanism a dependency agent would use when a platform requires the accountable PM or owner to sign off a submission personally.

## Themes
- identity-delegation: OpenID CIBA, optionally with OAuth RAR, so the approver sees the structured details (e.g. amount, payee) rather than a generic prompt.
- human-review-gates: steps: POST `/bc-authorize` with user id and RAR payload, receive `auth_req_id`, poll `/token`, user approves or denies, tokens issued on approval.
- agent-originated-requests: listed use cases include a DevOps agent needing approval to deploy to production and reading protected health records.

## Key points
- Guardian push is the default channel; email is a paid add-on.
- Part of "Auth0 for AI Agents" (User Authentication, Token Vault, Asynchronous Authorization, FGA for RAG), GA per Auth0 blog.

## Notable quotes
- RAR lets the agent "send a detailed, structured payload describing the exact transaction."
