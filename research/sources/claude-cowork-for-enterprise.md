---
title: "Making Claude Cowork ready for enterprise"
source_url: https://claude.com/resources/articles/cowork-for-enterprise
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-04-09
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [enterprise-admin-controls, agent-control-plane, cost-control-routing, org-learning-loop, pm-tool-connectivity]
relevance: medium
---

## Relevance to the project
Cowork's general-availability post lists the admin controls a company needs to roll a desktop agent out beyond one team: RBAC via SCIM groups, per-group spend limits, usage analytics (including skill and connector invocations per user), expanded OpenTelemetry, and per-tool connector controls (e.g. read but not write). Anthropic also states that most Cowork usage comes from outside engineering, on the work around core tasks (updates, decks, research sprints), which matches the PM-adjacent target user. Bears on the governance-control-plane and adoption-model dimensions; the customer quotes are short and unaudited.

## Themes
- enterprise-admin-controls: RBAC with custom roles per group (manual or SCIM), group spend limits, per-tool connector controls applied org-wide (section "Controls for organization-wide deployment").
- agent-control-plane: OTel events for tool and connector calls, files read or modified, skills used, and whether each AI action was approved manually or automatically; SIEM-compatible (Splunk, Cribl); a shared user identifier correlates OTel with Compliance API records.
- cost-control-routing: per-team budgets "adjustable as you learn what each team needs".
- org-learning-loop: Airtree partner: skills built by one person used by everyone, so Cowork "became shared firm infrastructure".
- pm-tool-connectivity: Zapier connected Cowork to its org database, Slack and Jira to surface engineering bottlenecks; Product and Design Ops copied the result; Zoom MCP connector launched.

## Key points
- GA on all paid plans (macOS and Windows), alongside Claude Code on Desktop.
- Usage pattern claim (Anthropic): "the vast majority" of Cowork usage is outside engineering; functions hand Claude "the work that surrounds their most critical tasks", not the core work.
- Analytics API: per-user Cowork activity, skill and connector invocations, DAU/WAU/MAU next to Chat and Claude Code.
- OTel available on Team and Enterprise.
- Customer examples (claims): Jamf turned a seven-facet performance review into a 45-minute guided self-evaluation; Airtree built board prep from portfolio Drive, Slack and competitor news compared against the previous prep.
- Quoted customers say bespoke dashboards replace BI-tool or engineer requests, and that the human role becomes "validation, refinement, and decision-making".
- Limits: launch post; no adoption numbers; quotes appear without company names in the extract (carousel).

## Could not verify
- Which company each carousel quote belongs to (names and titles only in the text extract; Joel Hron is CTO, company not shown).
- This post predates the CISO guide's (2026-07-17) statement that Cowork was not yet in the Compliance API; the OTel/Compliance API correlation line here implies Compliance API records exist for the same user, not that Cowork sessions are in it.
