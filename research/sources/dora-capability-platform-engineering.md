---
title: "Capabilities: Platform engineering"
source_url: https://dora.dev/capabilities/platform-engineering/
author: DORA
publisher: DORA / Google Cloud
published: unknown
retrieved: 2026-10-28
type: docs
evidence: independent
filed_by: research-dependency-agent
themes: [platform-as-a-product, cognitive-load-and-platforms, platform-onboarding-friction, coordination-cost-and-waiting]
relevance: high
---

## Relevance to the project
DORA's capability guide for platform engineering, updated to January 2026, folds its 2024 and 2025 findings into advice: treat the platform as a product with a product manager, reduce developers' cognitive load, measure adoption and task success, and avoid named anti-patterns including "ticket-ops" and the "ivory tower" that drives shadow IT. Two findings matter most for a dependency agent: developer independence (finishing tasks without relying on an enabling team) is linked to productivity, and the platform capability most linked to good user experience is clear feedback on the outcome of a task. Both describe what a well-instrumented onboarding flow would give a requesting team.

## Themes
- platform-as-a-product: assign a product manager focused on developer experience; map critical user journeys such as "spinning up a new service" (User-centred section).
- cognitive-load-and-platforms: platform engineers should "shift down" complexity into the platform rather than expecting developers to become experts in it (Cognitive load section).
- platform-onboarding-friction: pitfalls named "Build it and they will come", "Ivory tower" (drives shadow IT), "Ticket-ops", "Big bang" release and "One-size-fits-all" ("golden cage") (Common pitfalls).
- coordination-cost-and-waiting: 2024 finding that developer independence, the ability to complete tasks without relying on an enabling team, was linked to a 5% productivity improvement at team and individual levels (Key findings).

## Key points
- 2025 figures on the page: 90% of organisations use an internal developer platform; 76% have dedicated platform teams (DORA 2025, per page). Evidence: independent survey research run by Google Cloud's DORA team.
- When platform quality is high, AI adoption has a strong positive effect on organisational performance; when low, the effect is negligible. Individual coding gains are often lost to "downstream disorder" in testing, security review and deployment.
- 2025: the platform capability most correlated with positive user experience is clear feedback on the outcome of tasks.
- J-curve: gains, then a dip as complexity grows, then recovery.
- Measurement: DORA delivery metrics, developer satisfaction (CSAT/NPS), adoption and retention via HEART (how many new teams onboard and stay), task success.
- Advice: start with a minimum viable platform on the most common golden path; publish clear APIs and a contribution model so the platform team does not become a bottleneck.

## Could not verify
- Original publication date; the page shows only "last updated January 12, 2026".
