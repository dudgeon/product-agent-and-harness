---
title: Agent Control Planes Still Need A Robust Standards Stack
source_url: https://www.forrester.com/blogs/agent-control-planes-still-need-a-robust-standards-stack/
author: Leslie Joseph (Forrester)
publisher: Forrester blog
published: 2026-03-20
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, identity-delegation, skill-standards, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The clearest public analyst definition of the term "agent control plane": the third plane (with build and orchestration), which must sit outside both. It names the standards gaps that make cross-vendor governance hand-built today (no portable agent identity, experimental OpenTelemetry genAI conventions, no cross-plane policy schemas) and warns that merging build, runtime and governance into one "agent management" function may force costly refactoring. Directly informs terminology and the governance-control-plane dimension.

## Themes
- agent-control-plane: term introduced by Forrester in December 2025; vendor poll (Feb 2026, 47 vendors): 79% see it as a distinct category, 92% have a named PM or team, 40% report active RFPs.
- identity-delegation: no portable agent identity standard across planes; Microsoft Entra Agent Registry listed as proprietary.
- skill-standards: no capability-manifest schema across planes; MCP (2.1 added server identity), A2A agent cards, IBM ACP manifests each cover part.
- vendor-claims-vs-independent-evidence: the poll is of vendors, not buyers.

## Key points
- Control plane needs: observability, portable identity (model bindings, tool access, permissions, cost ceilings, behavioural constraints), policy propagation to build and orchestration layers, interventions (suspend, reroute, throttle, escalate).
- NIST AI Agent Standards Initiative (Feb 2026) and W3C AI Agent Protocol Community Group working on gaps.
- Until standards mature, control planes are limited to platform-specific implementations; standards decisions in 12-18 months could lock enterprises into one vendor's identity model.
- Forrester later published "The Agentic Control Plane Solutions Landscape, Q2 2026" with 33 vendors (per vendor press releases; report not read).

## Notable quotes
- "We are in the "dial-up internet" phase of the agentic era."
- "A control plane can't govern what it can't observe."
- "No such standard exists at the level of maturity that enterprises require."

## Could not verify
- The Q2 2026 landscape report itself (paywalled); vendor list known only from Airia and WSO2 releases. Retrieved via WebFetch (model-summarised view).
