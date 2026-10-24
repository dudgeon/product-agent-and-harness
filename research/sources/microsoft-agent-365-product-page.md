---
title: Microsoft Agent 365 (product page)
source_url: https://www.microsoft.com/en-us/microsoft-agent-365
author: Microsoft
publisher: microsoft.com
published: unknown
retrieved: 2026-10-24
type: other
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, identity-delegation, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
Microsoft's own description of Agent 365 as "the control plane" for an organisation's agents, with public per-user pricing. It is the clearest example of a governance-only layer (registry, identity, access, audit) sold separately from any agent runtime, which is a different shape from both P4 (meta-harness) and P5 (org-deployed agent workspace). Bears on governance-control-plane and agent-identity-delegation for a regulated Microsoft-estate company.

## Themes
- agent-control-plane: page states "Agent 365 is the control plane to observe, secure, and govern AI agents"; registry covers Microsoft agents, partner agents and customer-registered agents; agents map; lifecycle rules (expire inactive, flag ownerless).
- identity-delegation: each agent protected through Microsoft Entra (Entra Agent ID); agents published through Microsoft 365 channels with an Entra Agent ID appear in inventory automatically; Conditional Access and traffic filtering extended to agents.
- vendor-claims-vs-independent-evidence: only testimonials (Microsoft Digital, Genspark, KPMG); no outcome data.

## Key points
- Components named: registry/inventory, access control (which users, data, tools, MCP servers and agents an agent may reach), agents map, Defender (threat protection), Purview (data security, audit), Entra (identity), analytics.
- Third-party reach: "agents from our ecosystem partners" (Adobe, Cognition, Genspark, Glean, Kasisto, Manus, Nvidia, n8n, ServiceNow, Workday listed as partners), but "Agents built outside these environments will require additional steps." No model vendor (Anthropic, OpenAI) named on the page.
- Pricing (as shown 2026-10-24): Agent 365 $15/user/month annual; included in Microsoft 365 E7 ($99/user/month). Licensing is per human user, not per agent (secondary licensing blogs agree; GA reported as 2026-05-01).
- Banner says "Now generally available"; no date on page.

## Notable quotes
- "Agent 365 is the control plane to observe, secure, and govern AI agents,"
- "Agents built outside these environments will require additional steps."

## Could not verify
- GA date of 2026-05-01 comes from secondary licensing blogs (licensingschool.co.uk) and the FastTrack atlas, not this page. Retrieved via WebFetch (model-summarised view).
