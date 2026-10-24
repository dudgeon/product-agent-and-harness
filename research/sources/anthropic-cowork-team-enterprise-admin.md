---
title: Use Claude Cowork on Team and Enterprise plans (Claude Help Center)
source_url: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
author: Anthropic
publisher: support.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, skills-marketplace, human-review-gates, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
This is the admin's main reference for Cowork, the Anthropic surface closest to a "general agent for knowledge workers" that our PM users would meet. It lists the org-level toggles a regulated admin can set, and where they stop. It also states two facts that matter for an audit-bound setting: local Cowork history sits outside Anthropic's retention policy and can't be deleted centrally, and OpenTelemetry "doesn't replace audit logging for compliance purposes". Bears on governance-control-plane, runtime-location and capability-distribution-trust.

## Themes
- enterprise-admin-controls: org toggle (on by default, off for HIPAA orgs); Enterprise groups and custom roles can enable it per team; separate "Run Cowork in the cloud" toggle (Team on by default; Enterprise off by default, then granted to a group as the "Cowork in the cloud" capability); built-in browser, auto-approve mode, connector "Always allow", network egress and web search toggles (Admin controls section).
- skills-marketplace: no separate Cowork plugin setting; owners distribute plugins through marketplaces with four states (installed by default, available, required, not available), with per-group overrides on Enterprise (Plugins).
- human-review-gates: "Allow 'Always allow' for connector tools" is off by default; when it is off, saved preferences for write tools aren't honoured. Read-only tools are exempt only when the connector annotates them as read-only, so most custom connectors' tools stay gated. Enterprise starts new tasks without auto-approve (Auto mode / Connector tool approvals).
- shared-persistent-sessions: cloud sessions run on Anthropic infrastructure and continue across desktop, web and mobile; scheduled tasks run with no device online. Local sessions run on the user's machine with code in an isolated VM (Where it runs).

## Key points
- Availability (page "updated today", read 2026-10-24): desktop beta on all paid plans; web and mobile on Enterprise only where an owner enables it.
- Network egress setting applies only when a new session starts and "doesn't cover web fetch, web search, or MCPs, including Claude in Chrome". Web search can be switched off separately.
- Projects: no admin controls; owners can't restrict project creation. Local-folder project data stays on the user's machine.
- Compliance API captures Cowork sessions from Claude, Claude Desktop and Claude Mobile, including cloud sessions. Local history "is not subject to Anthropic's standard data retention policies", admins can't manage or delete it centrally, and local-session deletion endpoints aren't available yet. The page says the API covers the last 30 days or a shorter org retention period (this conflicts with the platform docs' 6-year default; see anthropic-compliance-api-session-transcripts; the 30-day figure matches HIPAA-ready orgs).
- HIPAA: after the Primary Owner applies the HIPAA configuration to Claude Code (local mode) and Cowork (local mode), the BAA covers Cowork in Claude Desktop; without it Cowork is "available but not covered under your BAA". The configuration disables cloud sessions and, in local mode, the built-in browser. ZDR not addressed.
- Prompt injection risk called "non-zero"; mitigations are user-side (avoid sensitive files, monitor, limit web access).

## Notable quotes
- "Claude Cowork is on by default, but organization owners can manually disable it."
- OpenTelemetry "doesn't replace audit logging for compliance purposes."

## Could not verify
- Retrieved via WebFetch (model-summarised); wording should be rechecked before quoting. No dated version history; the page has changed over time (an older research-preview version said no per-user or per-role controls existed).
- The 30-day API window vs the platform docs' 6-year retention is unresolved.
