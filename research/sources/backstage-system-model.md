---
title: "System Model (Backstage Software Catalog)"
source_url: https://backstage.io/docs/features/software-catalog/system-model
author: Backstage (CNCF; originated at Spotify)
publisher: backstage.io
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [dependency-types-and-practices, legible-org-for-agents, stale-records-mislead-agents]
relevance: medium
---

## Relevance to the project
Backstage's system model is the most widely copied vocabulary for recording system dependencies and ownership: components, APIs, resources, systems, domains, groups and users, with components providing and consuming APIs and depending on resources. It is a ready-made schema for the "system/service" dependency type a dependency agent would read, but it covers only software entities: intake processes, approvals, funding and release trains, which dominate regulated-enterprise dependencies, have no place in it.

## Themes
- dependency-types-and-practices: "APIs are the boundaries between different components"; components "implement APIs for other components to consume", "consume APIs implemented by other components", and may "directly depend on components or resources that are attached to it at runtime" (§Core entities).
- legible-org-for-agents: "A system, in this sense, is a collection of resources and components that exposes one or several public APIs"; domains group systems by business purpose and may nest; groups describe "an organizational entity, such as for example a team, a business unit".
- stale-records-mislead-agents: all of these relations are declared by hand in descriptor files; nothing on the page reconciles them with runtime reality (this filer's observation; see thereliabilityengineering-service-catalog-already-wrong).

## Key points
- Kinds: Component, API (public, restricted or private visibility), Resource, System, Domain, Group, User, plus Location and Template.
- The page does not state that ownership is mandatory; the separate descriptor-format page makes `spec.owner` required (see backstage-descriptor-format).
- No entity kind for a process, an intake queue, a release calendar or an approval body.
