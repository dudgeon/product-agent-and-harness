---
title: "Harbor: Stripe's AI-assisted prototyping tool"
source_url: https://stripe.dev/blog/harbor-stripes-ai-assisted-prototyping-tool
author: Cristian Rivera, Sai Samant (Stripe)
publisher: Stripe Dot Dev Blog
published: 2026-09-14
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [prototyping-agents-limits, spec-becomes-prototype-and-evals, non-engineer-builders, remote-agent-invocation, artifact-standardization, one-job-per-agent, agent-as-service-many-surfaces]
relevance: high
---

## Relevance to the project
Harbor is Stripe's browser-based prototyping agent (designer-first, now company-wide) and the clearest Stripe statement of a **federation of specialised agents connected over MCP** rather than one agent doing everything: Kai does research, Harbor builds the interactive artifact, coding agents on devboxes pull the prototype into a repo. It also shows artifact-level collaboration (publish to URL, anchored comments that survive agent rewrites, remix) that Kai itself lacks. Bears on work-structure/agent-unit, remote-invocation-route, artifact-and-project-structure and the PM "define" step.

## Themes
- prototyping-agents-limits / spec-becomes-prototype-and-evals: designers turn static designs into interactive prototypes with Stripe design systems and mock data; a product page's animated hero shipped "nearly one-for-one from the prototype"; Finance presents monthly actuals as clickable prototypes instead of decks; AEs build pricing proposals, battlecards, ROI calculators.
- non-engineer-builders: since May 2026, 3,000+ Stripes created 12,000 prototypes; 25% of Stripes have made at least one.
- remote-agent-invocation: Harbor's toolset is exposed on Stripe's internal MCP infrastructure so other agents (including coding agents on devboxes) can create, read, update and publish prototypes; Drydock (in-browser renderer: multi-file React/TS tree in, page plus failure report out) is a separate service, used by Kai.
- one-job-per-agent: "it's effective to keep agents specialized (on research, coding, or browser-native tools) while exposing them to capabilities in other systems"; "make Stripe's AI tools work together rather than have each tool solve every part of the workflow".
- artifact-standardization: one published version at a time at a shareable URL; comments anchored by multiple signals and re-resolved as attached / needs review / orphaned after agent rewrites; comments go stale on a new snapshot; remix into one's own copy.

## Key points
- First version built by one engineer in about 40 days.
- The agent writes a multi-file source tree; the page compiles in the viewer's browser (no server); the agent inspects the rendered page, clicks, types, switches viewports, screenshots.
- Example chain: a producer ran a stripe.com viewport analysis in Kai, then used Harbor to make it clickable; engineers mock admin tools in Harbor then hand them to a coding agent.
- Next: prototype-scoped databases and live-data widgets.

## Could not verify
- Adoption numbers Stripe-reported. Whether Harbor sessions share identity/permissions with Kai is not stated.
