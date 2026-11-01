---
title: "Agent 365 identity (Microsoft Learn)"
source_url: https://learn.microsoft.com/en-us/microsoft-agent-365/developer/identity
author: Microsoft
publisher: Microsoft Learn
published: 2026-08-10
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [identity-delegation, agent-stewardship, enterprise-admin-controls]
relevance: high
---

## Relevance to the project
Microsoft's developer reference for how an Agent 365 agent is represented and which identity a call carries: three execution modes (S2S as its own agent identity, OBO with "the user is the token subject and the agent identity is the actor", and Agentic-User with its own mailbox-holding user account), a mandatory business sponsor, and sign-in and audit logs that separate "the credential source, acting identity, and token subject". This is the most concrete shipped answer to "record who acted, for whom, under what authority", the question a multi-week dependency ask raises when an agent chases and a human answers.

## Themes
- identity-delegation: "OBO (on-behalf-of) ... uses delegated permissions; the user is the token subject and the agent identity is the actor"; S2S "for scheduled tasks, monitoring, and background processing", agent identity as subject; Agentic-User for mailbox, Teams presence, Word and Outlook interactions (Frontier preview only).
- agent-stewardship: "Each agent identity and agent identity blueprint requires at least one sponsor: the business representative accountable for the agent's purpose and lifecycle"; security teams may contact the sponsor during an incident.
- enterprise-admin-controls: blueprint holds credentials and inheritable permissions; "Treat each blueprint as a credential boundary"; one Conditional Access policy or revoke on a blueprint applies to every agent of that kind; declared permissions are not granted until an admin consents; MFA does not apply to agent identities, so Conditional Access governs them.

## Key points
- Agent identity is a Microsoft Entra service principal (`#microsoft.graph.agentIdentity`); single-tenant, while blueprints can be multitenant.
- An agent's user account can be reached "through Teams, Outlook, Word comments, and email", which is the channel an outside owner would answer through.
- Logs: "Sign-in and audit logs differentiate between the blueprint, the agent identity, and the agent's user account."
- Related: [microsoft-entra-agent-owners-sponsors](microsoft-entra-agent-owners-sponsors.md), [microsoft-agent-365-product-page](microsoft-agent-365-product-page.md).

## Could not verify
- Whether OBO chains across several agents (agent A for user, calling agent B) record more than one actor; the page describes one hop. Read via WebFetch (raw page returned).
