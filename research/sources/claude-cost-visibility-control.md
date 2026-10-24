---
title: "A guide to cost visibility and control in Claude"
source_url: https://claude.com/resources/articles/a-guide-to-cost-visibility-and-control-in-claude
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-08-04
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [cost-control-routing, enterprise-admin-controls, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
Anthropic's inventory of cost levers for Claude Enterprise admins (access gating, model entitlements and defaults, hard spend caps, usage analytics, Analytics API, analytics chat) and for API builders (workspaces, caching, batch, effort, the advisor strategy). It recommends a sequence (gate access, watch a month, then cap) and frames value as cost per outcome, while admitting "no vendor can measure it for you". Useful as the default control set a company agent's governance layer would sit on. First-party product description, no customer data.

## Themes
- cost-control-routing: match model to whether work is "hard" or merely "large"; Fable/Opus/Sonnet/Haiku tiers; effort control; advisor tool lets smaller models consult a frontier model (section "Useful ways to think about cost").
- enterprise-admin-controls: access gating by group/custom role, model entitlements and defaults, hard caps per org/user/group, automated review of limit-increase requests (section "Cost controls for Claude Enterprise").
- outcome-measurement-gap: cost-per-outcome recommended, but what work would have cost without AI is business-specific and vendor-unmeasurable (opening section).

## Key points
- Suggested order: access gating (start with one team, expand by department), model controls (entitle hard-work teams to top models, default others to Sonnet), then hard caps once a baseline exists; caps "bind right away".
- Observability: usage by person, team, model; exports said to closely match invoices; Analytics API to BI/finance tools; natural-language analytics chat ("Who are our top spenders this month?").
- API levers: workspaces as separate cost lines; prompt caching (cache hits ~10% of input rate); batch at half price, stacking with caching; effort parameter per call; advisor strategy.
- Notes cheaper models on hard reasoning can cost more overall through retries and human correction.
- Limits: no figures on typical savings ("substantially"); no guidance on per-agent or per-automation attribution.

## Could not verify
- Which controls are Enterprise-only versus Team; the invoice-match claim.
