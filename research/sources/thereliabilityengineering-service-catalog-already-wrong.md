---
title: "Your service catalog is already wrong"
source_url: https://thereliabilityengineering.substack.com/p/your-service-catalog-is-already-wrong
author: Spiros Economakis
publisher: Reliability Engineering (Substack)
published: 2026-07-13
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [stale-records-mislead-agents, legible-org-for-agents, dependency-types-and-practices]
relevance: medium
---

## Relevance to the project
A reliability engineer argues that hand-declared service catalogs (Backstage, Cortex, Compass, Roadie) drift from reality "within weeks", that the real dependency graph is usually discovered during an incident, and that this now matters more because agents read the catalog and act on it. His remedy, deriving ownership and dependencies from runtime evidence and labelling each fact's provenance and confidence, is a direct design pattern for a dependency agent's context layer. Opinion without data, so use it for the argument, not the numbers.

## Themes
- stale-records-mislead-agents: "Every service catalog is declared by hand and drifts from reality within weeks"; "In practice the gap opens within about two weeks, and it compounds" (author's experience, no data).
- legible-org-for-agents: "An agent needs the catalog to tell it, explicitly, how much to trust each fact before it acts"; proposes labelling facts runtime-observed, synthesized or declared, with confidence.
- dependency-types-and-practices: proposes dependencies from the observed call graph, ownership from deploy history and contributor activity, readiness from SLOs, alerts and incidents, blast radius from live topology.

## Key points
- Keeping YAML current is "invisible, unfinished work" that reorgs, new deployments and shifting dependencies outpace.
- "The catalog nobody maintains has quietly become the context layer every agent that touches production depends on."
- Recommends keeping existing portals but changing how they stay accurate (continuous reconciliation on every change).
- Limit for this project: runtime evidence covers system dependencies only; process, approval and funding dependencies leave no call graph.
