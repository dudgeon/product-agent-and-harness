---
title: "Administrative relationships in Microsoft Entra Agent ID (Owners, sponsors, and managers)"
source_url: https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers
author: Microsoft
publisher: Microsoft Learn
published: 2026-04-16
retrieved: 2026-10-26
type: docs
evidence: first-party
filed_by: research-shared-persistent-agents
themes: [agent-stewardship, identity-delegation, enterprise-admin-controls]
relevance: high
---
## Relevance to the project
Microsoft's identity layer makes a business "sponsor" mandatory for every agent identity, separate from the technical owner, precisely so an agent always has a human accountable for whether it should still exist and what it can access. This is the most concrete enterprise answer found to "a session outlives its creator" (catalogue item 9): sponsorship can be a group (so it survives one person leaving), and "Sponsorship should be maintained to ensure succession when an employee who's a sponsor moves or leaves." First-party docs (ms.date 2026-04-16, updated 2026-09-03).

## Themes
- agent-stewardship: "At least one sponsor is required for each agent identity and agent identity blueprint"; sponsors decide renewal, extension or removal, request access with business justification, and during incidents decide whether behaviour is expected (Sponsors section)
- identity-delegation: three relationships: owners (technical admin, may be service principals), sponsors (business accountability, least privilege: disable, soft-delete, change sponsors only), managers (org-hierarchy, can request access packages) (overview)
- enterprise-admin-controls: in delegated creation the calling user becomes sponsor by default; Agent ID admins are not auto-made sponsors "to avoid unintentionally overburdening admins"; app-only creation must name a sponsor (Assignment policies)

## Key points
- (research-dependency-agent, 2026-10-28) The sponsor role is exercised in access packages: an agent identity can request a package itself via Graph, approvals follow the package policy, and the sponsor is notified to extend or let access lapse (`microsoft-entra-agent-access-packages`).
- Groups (dynamic membership or Microsoft 365) can be sponsors, so accountability can sit with a team; max 100 sponsors with no more than 5 groups.
- Sponsors cannot re-enable or restore what they disable; owners or admins must.
- For unpublished agents creators are often sponsors; for published agents sponsors usually come from the teams using it.
- Succession mechanics: Microsoft Zero Trust workshop guidance says sponsorship silently transfers to the departing sponsor's manager, while a Microsoft Learn training knowledge check says it stays with the departed sponsor until a Lifecycle Workflow or admin reassigns it. The two Microsoft sources conflict (search summaries).

## Notable quotes
- "Sponsorship should be maintained to ensure succession when an employee who's a sponsor moves or leaves."

## Could not verify
- Which succession behaviour is the actual default (see conflict above); the Lifecycle Workflows page was not opened.
