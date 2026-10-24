---
title: Service accounts and Codex access tokens (ChatGPT enterprise docs)
source_url: https://learn.chatgpt.com/docs/enterprise/service-accounts
author: OpenAI
publisher: learn.chatgpt.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [identity-delegation, enterprise-admin-controls]
relevance: high
---

## Relevance to the project
OpenAI now offers two non-interactive identities for headless Codex (CI, scheduled jobs, app-server automation): personal access tokens that act as the creating member, and SCIM-provisionable service accounts whose tokens "represent the service account, not the person who creates it." This is the clearest vendor option found for running a shared or unattended agent under an auditable non-human identity with its own roles, groups, plugins and connections, which feeds the agent-identity-delegation dimension. Companion page read: https://learn.chatgpt.com/docs/enterprise/access-tokens.

## Themes
- identity-delegation: service account tokens represent the account; personal tokens represent the member who created them. Service accounts get their own roles, groups, plugins and connections and "don't inherit the creator's" (service accounts page).
- identity-delegation: SCIM with `userType` = `ServiceAccount`; the IdP manages name, groups and lifecycle; SCIM-managed accounts cannot be renamed or deleted in ChatGPT.
- enterprise-admin-controls (proposed): owners set an "Access token expiration limit" (example 90 days); scoped tokens must expire (7/30/60/90 days suggested); owners and admins can revoke any workspace token; disabling a member's local Codex permission suspends their tokens (access tokens page).

## Key points
- Service accounts: pay-as-you-go plans only; created by owners/admins in UI or Admin API; delegated roles User / Configure / Manager for people who manage the account; a service-account token cannot authenticate Admin API requests; requires Codex CLI 0.142.0+; `CODEX_ACCESS_TOKEN` with `codex exec`; avoid saved logins on shared runners; disabling/deleting revokes all tokens; finite TTL must be under one year.
- Access tokens: Business and Enterprise only; scopes "Codex" or "Workspace Agents"; a Codex-only token cannot trigger workspace agents; general API calls need a Platform API key; supported in CLI and `codex app-server`, not desktop or IDE.
- Audit: runs are attributed to the service account; token-backed personal runs "appear in workspace governance data"; event coverage deferred to Admin API / Compliance docs.
- Neither page mentions Codex cloud tasks.

## Could not verify
- Whether service accounts can own cloud tasks, Slack-triggered tasks or environments. Ship date (5 May 2026 for access tokens) is from a third-party blog only.
- Model-summarised fetch; no dates on pages (UI mockups show Jul 2026 sample data).
