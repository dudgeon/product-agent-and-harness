---
title: Plugin controls (ChatGPT / Codex enterprise docs)
source_url: https://learn.chatgpt.com/docs/enterprise/apps-and-connectors
author: OpenAI
publisher: learn.chatgpt.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, skills-marketplace, skill-supply-chain-security, pm-tool-connectivity]
relevance: high
---

## Relevance to the project
How OpenAI governs plugins (skills plus optional connectors/MCP servers) across ChatGPT Work and Codex: per-role availability, a public catalog with CSV export for review, workspace-created plugins imported from GitHub, and per-connector read/write action controls. It is the OpenAI counterpart to Claude org plugin sync and Copilot's custom agents in `.github-private`, and it is the most explicit vendor statement that a plugin is a "capability chain" with several separately governed links, which matters for the capability-distribution-trust dimension.

## Themes
- skills-marketplace: a plugin bundles skills and optional connectors; help-center companion says admins mark a plugin "Available" or "Installed" per eligible role (Workspace settings > Plugins); ChatGPT Business uses workspace-wide availability instead of roles.
- skill-supply-chain-security: the public-catalog CSV export "does not include plugins created for that workspace", snapshot up to 48 hours old, not available in FedRAMP; no internal publishing/approval workflow is described, only "complete any required review before enabling it".
- pm-tool-connectivity: Action control lets admins allow read-only actions or an approved custom set and decide how newly added actions are handled; "Whatever the initial set, start with read actions."
- enterprise-admin-controls (proposed): company-domain app restriction blocks new connections from personal or unauthorised workspaces once activated; existing connections are not disconnected automatically.

## Key points
- Capability chain: skills governed by the plugin package and Skill controls; connector access by Workspace apps and Permissions & roles; connector actions by Action control and app permissions; external data by the connected service's own IdP. "Installing a plugin for everyone doesn't, by itself, provide a shared account."
- Surfaces: Chat and Work on web, desktop, mobile; Codex in the desktop app and CLI plugin browser; not the IDE extension. Help-center wording on mobile coverage conflicts with this page.
- Role changes take up to five minutes; Lockdown Mode restrictions can override ordinary role grants.
- Under cloud orchestration, command hooks and plugin hooks do not run even when the plugin is allowed; admin-defined MCP hooks may; "MCP hooks don't provide a complete Compliance API audit trail."
- Chat conversations using connections remain available through the Compliance API; non-synced connector data processed transiently, synced data indexed.

## Could not verify
- The Skill controls and Plugin management pages were not read; who may publish workspace plugins and whether there is an approval queue is unknown.
- No date on the page; model-summarised fetch.
