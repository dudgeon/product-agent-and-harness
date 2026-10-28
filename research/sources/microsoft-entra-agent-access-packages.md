---
title: "Access packages for agent identities in Microsoft Entra"
source_url: https://learn.microsoft.com/en-us/entra/agent-id/agent-access-packages
author: Microsoft
publisher: Microsoft Learn
published: 2026-05-01
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-originated-requests, identity-delegation, agent-stewardship, onboarding-as-code]
relevance: high
---

## Relevance to the project
The most complete shipped example of an agent requesting access through an enterprise governance process: an Entra agent identity can itself programmatically request an access package (a Graph `accessPackageAssignmentRequest`), the request is routed to the approvers defined in the package policy (up to three stages), access is time-bound, and the agent's human sponsor is notified before expiry and must request an extension or let it lapse. The intake (the access package and its policy) is defined as data and is creatable via Graph, so it is legible to an agent.

## Themes
- agent-originated-requests: three pathways: "The agent identity itself can programmatically request an access package when needed for its operations"; the sponsor can request on its behalf; or an admin assigns directly (Access request and approval process).
- identity-delegation: packages can carry OAuth application permissions, delegated permissions (to assist a user), group memberships, or allowed directory roles; not app roles, SAP roles or SharePoint site roles (Prerequisites, Create).
- agent-stewardship: on expiry the sponsor is notified and may request extension (which can trigger a new approval cycle); with no action access lapses (Access assignment lifecycle).
- onboarding-as-code: policy fields define who can request ("All agents"), approval stages and approvers, expiry and extension; packages can be created via Microsoft Graph and PowerShell.

## Key points
- Adding API permissions or directory roles marks the catalog as privileged and requires Global Administrator; resource-ownership validation runs when API permissions are onboarded or added.
- Doc dated 2026-05-01, updated 2026-10-06; related pages mark request-on-behalf-of-agent as preview (search summaries).

## Could not verify
- Whether approvers can include policy-based auto-approval for agents, and GA status of the agent-request pathway.
