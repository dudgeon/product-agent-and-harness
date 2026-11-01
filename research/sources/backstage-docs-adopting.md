---
title: Strategies for adopting (Backstage documentation)
source_url: https://backstage.io/docs/overview/adopting
author: Backstage project (Spotify)
publisher: backstage.io
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [two-sided-cold-start, platform-as-a-product, agent-legible-platform]
relevance: high
---

## Relevance to the project

Spotify's own playbook for the two-sided problem in an internal developer portal: Backstage is described as a "platform of platforms", a marketplace between infrastructure and platform teams and end users, and most of the work is done by contributing platform teams, who own their plugins as products. The central team is told to treat those platform teams as its customers and to court them actively (embedding, hack days, usage digests, approaching owners of internal UIs that could be consolidated). This is the closest first-party precedent for co-curating anchor platforms with their owners, and its success proxies (teams contributing, share of contributions from outside the central team) are candidate measures for the dependency agent's context layer. Spotify's figures are its own and unaudited.

## Themes

- **two-sided-cold-start**: Backstage "acts as a marketplace between infrastructure/platform teams and end users"; contributing teams have internal engineers as customers and the central team should treat those teams as customers too (Internal evangelization). First-party.
- **two-sided-cold-start**: evangelisation tactics aimed at the supply side: lunch and learns on building a plugin, embedding a central-team member in a contributing team for a sprint or two, hack days, quarterly show and tell, weekly usage digests to contributing teams, and proactively approaching teams that own internal UIs or platforms (Evangelization tactics). First-party.
- **platform-as-a-product**: a central team runs the deployment as a product with four objectives: operate it, drive developer adoption, encode best practice in Software Templates with senior leaders and architects, and promote Backstage to other platform teams (Organizational setup). First-party.
- **agent-legible-platform**: platform teams expose their tools through plugins they own, so they can change API and UI together and users need not know the underlying tool (CI plugin case) (Internal evangelization). First-party.

## Key points

- Spotify figures quoted as "currently": 135 internal plugins from 63 teams; 85% of contributions from outside the central Backstage team; about 50% of all Spotifiers use it monthly although engineers are under half of staff; most engineers use it daily (Spotify figures). First-party, unaudited, undated.
- Onboarding (time to 10th merged PR) fell 55% two years after deployment (KPIs). First-party.
- Platform-success proxies: number of teams contributing at least one plugin, total plugins, share of contributions from outside the central team, MAU/DAU and page views (Metrics).
- Warning against optimising for time spent in the portal: "time spent in Backstage is time not spent writing code" (Metrics note).
- The page does not say which teams to approach first or name a champion role.

## Notable quotes

- "THE developer portal at your company" (Organizational setup, on where the value comes from)
