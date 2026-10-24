---
title: Superset homepage, pricing and enterprise pages
source_url: https://superset.sh/pricing
author: Superset Inc.
publisher: superset.sh
published: unknown
retrieved: 2026-10-24
type: other
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
Shows a local parallel-session manager growing into a hosted product with cloud workspaces and an Enterprise tier (SAML SSO, SCIM, audit logs, SOC 2 Type II). That moves it partly from "single user, own machine" toward the hosted-control-plane shape, but the governance on offer is account-level (identity, audit of the app), not policy over what the agents do. Also read: homepage https://superset.sh/ and https://superset.sh/enterprise.

## Themes
- meta-harness: tagline "One workspace for Claude Code, Codex, and any coding agent"; "Superset never proxies model calls or locks your workflow to one provider."
- shared-persistent-sessions: remote hosts where "Workspaces keep running when your laptop sleeps"; Team plan adds cloud workspaces (beta).

## Key points
- Plans (pricing page): Free ($0, 1 user, local workspaces, desktop app, CLI); Pro ($20/user/mo; remote access, automations, Linear and Slack integrations, mobile); Team ($60/user/mo; cloud workspaces beta, 1,200 GB-hours per seat pooled, 5 cloud environments); Ultra ($200/user/mo); Enterprise (custom, annual: SAML SSO, SCIM provisioning, audit logs, SOC 2 Type II report, uptime SLA).
- Homepage: "Repos, worktrees, terminal output, and agent sessions stay on your machine"; source public under ELv2, "not OSI-approved open source"; SOC 2 Type II claimed with a trust portal.
- Logo strip "Trusted by builders from" Microsoft, OpenAI, Google, Salesforce, Vercel, Cloudflare, Amazon: individuals, not stated as customers.
- Enterprise page is a contact form; no detail on admin policy, self-hosting or data handling.
- "Superset is getting a new name soon" (homepage, 2026).

## Could not verify
- What the audit logs cover; whether the control plane can be self-hosted; any named enterprise customer.
