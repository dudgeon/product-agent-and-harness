---
title: Entra Agent ID from a Security Perspective
source_url: https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/
author: Christian Feuchter
publisher: Compass Security Blog
published: 2026-06-09
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [identity-delegation, agent-control-plane, agent-failure-modes]
relevance: high
---

## Relevance to the project
The only independent, hands-on security test found of any big-vendor agent identity system. It shows that Entra Agent ID's blueprint model concentrates credentials and that its permission blocks are incomplete (944 of 1,041 Graph permissions tested were allowed, including dangerous ones). For a regulated company, this is concrete evidence that "agents get their own identity" does not by itself mean least privilege; the identity admin roles become highly privileged.

## Themes
- identity-delegation: object model of blueprint (holds credentials), blueprint principal, agent identity (holds permissions), optional agent user; three flows: autonomous app, on-behalf-of (user signs in through an app with `access-agent` permission), agent user account.
- agent-control-plane: identity is the base layer Agent 365 builds on; weaknesses here propagate.
- agent-failure-modes: blueprint owner could add a secret, impersonate a child agent identity and (in the author's test) assign Global Administrator via `RoleAssignmentSchedule.ReadWrite.Directory`; Azure RBAC had no restrictions (agent identities could be Owner); cross-tenant consent phishing via a multitenant blueprint.

## Key points
- Credentials can be set only on the blueprint, so compromising it affects all child agent identities.
- Some directory roles blocked (Global Admin, Group Admin) but others allowed (Exchange Admin, Windows 365 Admin).
- Graph permissions: 97 blocked, 944 allowed of 1,041 tested; `Application.ReadUpdate.All` allowed as a workaround for blocked `Application.ReadWrite.All`.
- Inherited permissions do not appear when enumerating the agent identity directly (audit blind spot).
- `AgentIdentity.CreateAsManager` always present in the blueprint principal token.
- Recommendations: treat Agent ID Administrator, AI Administrator and blueprint-credential permissions as highly privileged; prefer delegated over application permissions; vet foreign blueprints before consent.

## Notable quotes
- "the blueprint holds the authentication credentials, while the agent identity holds the permissions"

## Could not verify
- Whether Microsoft has since changed the permission blocks (test dated June 2026). Retrieved via WebFetch (model-summarised view); figures should be re-checked on the live page before quoting.
