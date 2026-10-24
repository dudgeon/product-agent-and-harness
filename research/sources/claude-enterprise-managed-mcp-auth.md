---
title: "Centrally manage authorization for MCP connectors"
source_url: https://claude.com/resources/articles/enterprise-managed-auth
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-06-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [identity-delegation, enterprise-admin-controls, agent-protocol-security, pm-tool-connectivity, agent-control-plane]
relevance: medium
---

## Relevance to the project
Anthropic's enterprise-managed authorization lets admins provision MCP connectors org-wide through the identity provider (Okta first), so users inherit connector access by IdP group and role across Claude chat, Claude Code and Cowork with no per-user OAuth. For a product agent in a regulated company this is the clearest first-party mechanism for making the IdP the control plane for agent tool access: scoped by group, revoked through the IdP, short token lifetimes, and an option to block personal accounts. It is built on an open MCP extension (Cross App Access), which matters for harness portability, but the page is a launch announcement with partner endorsements and no security detail on what the agent can do once connected.

## Themes
- identity-delegation: users' "personal identity passes through" via IdP login while per-connector OAuth grants disappear; access is inherited from existing IdP groups and roles (How it works; customer quote).
- enterprise-admin-controls: provision once, scope by group, revoke via IdP, shorten token lifetimes, and require a connector to connect only through the IdP to keep work and personal accounts separate (How it works).
- agent-protocol-security: implemented as the Enterprise-Managed Authorization extension to the MCP authorization spec, embedding the Cross App Access protocol (intro; Okta-side quote).
- pm-tool-connectivity: launch connectors include Asana, Atlassian (Jira, Confluence, Teamwork Graph via Rovo MCP), Canva, Figma, Granola, Linear, Supabase; GA update adds Datadog, Notion, Slack, with Exa, Miro, Zoom coming (update note, Built with an ecosystem).
- agent-control-plane: identity turned into "a centralized governance plane" for MCP access rather than a separate surface to monitor (How it works; quote).

## Key points
- **Before:** two steps, admin enables a connector, then every user authorises it individually; for Supabase the alternative was being an org owner or handing out Personal Access Tokens (customer quote).
- **After:** admin authorises once; users get connectors on first login, consistent across chat, Claude Code and Cowork. One customer quote reports 2,000 employees provisioned via Okta with zero extra steps (customer claim).
- **Revocation:** because IdP checks are cheap, admins can shorten access-token lifetimes so deprovisioned users lose connector access quickly instead of on stale tokens.
- **Work/personal separation:** an admin can force a connector to IdP-only connection, preventing personal accounts being linked to work tools.
- **Open standard:** any MCP provider or IdP can implement the extension, including custom in-house connectors.
- **Status:** beta for Team and Enterprise at launch (2026-06-18); update of 2026-08-24 says generally available. Okta is the only named IdP; others "coming soon".
- **Named adopters:** HubSpot, Ramp, Webflow rolling out.
- **One customer quote** pairs this with "selective control of individual tools exposed by those MCP hosts", suggesting tool-level scoping exists, but the article does not describe it.
- **Limits / missing:** nothing on what scopes the agent acts with (user's full permissions or narrower), audit logging, agent-specific identity separate from the user, or how write actions are controlled. Partner quotes are endorsements, several with no organisation named beside the speaker.

## Notable quotes
- "Personal identity passes through, but no one gets tripped up on a multitude of OAuth grants." (Andrew Meinert, Director, System Operations & AI)
- "...we turn identity into a centralized governance plane..." (Aaron Parecki, Director of Identity Standards)

## Could not verify
- Which other IdPs are supported as of retrieval; the Help Center page was not read.
- Whether connector access acts with the user's full permissions in the target tool.
