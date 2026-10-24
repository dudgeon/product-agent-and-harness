---
title: PDLC/SDLC across agent ecosystems
status: active
directed_by: director-project-agent-and-harness
model: claude-fable-5-1
done_when: One standalone HTML work product with inline styling that lays the product and software lifecycle tasks against every ecosystem mapped (Stripe, Ramp, Shopify, Anthropic, Atlassian, Intercom), shows where each has agents, artifacts and handoffs (documented / inferred / unknown), names the common seams and gaps (e.g. research → intent → plan across people), links to each ecosystem map and its sources, and ties back to options/DIMENSIONS.md; accepted by Geoff
---

## Request

Geoff (2026-10-24): "then when all those wrap, have a single worker make a PDLC/SDLC across agent frameworks work product (html with inline styling) for all available agent ecosystems -- this is a task, i trust you to document it and cross-link where appropriate"

Inputs: the per-ecosystem maps listed in [[pdlc-maps-per-ecosystem]]; the runtime-patterns synthesis; the options register; the opportunity-to-code-chain theme. Related: [[strategy-story-and-explainer-video]].

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness, waiting for the per-ecosystem maps.
- 2026-10-24 Worker pdlc-cross-ecosystem started via claude --bg on Fable 5.1 with --remote-control.
- 2026-10-24 Worker pdlc-cross-ecosystem: built tasks/pdlc-cross-ecosystem-map/index.html (standalone, no scripts, no web fonts, light and dark, matrix plus by-ecosystem view) from the six maps, with README.md and the generator index.build.py; all 135 relative links and anchors checked; public-check clean; folder staged, not committed.
- 2026-10-24 Worker pdlc-cross-ecosystem: checked in Chrome at desktop and phone widths, light and dark; fixed phone overflow; director asked that two more columns (Airbnb, Spotify) can be added later: the generator is data-driven, noted in README.md.
