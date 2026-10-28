---
title: "Platform as a Product in a 300-Year-Old Bank"
source_url: https://speakerdeck.com/syntasso/platform-as-a-product-in-a-300-year-old-bank
author: Joel King (NatWest Group) and Abby Bangser (Syntasso)
publisher: Speaker Deck (Syntasso)
published: 2026-06-19
retrieved: 2026-10-28
type: other
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [platform-as-a-product, cognitive-load-and-platforms, platform-onboarding-friction, process-governance-load]
relevance: medium
---

## Relevance to the project
Slides from a talk co-presented by a NatWest principal engineer and the vendor of Kratix, the platform framework NatWest uses. Before the platform, tens of departments and hundreds of teams were containerising at once and solving the same infrastructure problems in parallel, with "135+ patterns in production", high cognitive load, configuration drift and slow manual change under a model the slides call "Safety through tickets". The response is a marketplace in which providers (security, data, vendor and finance capabilities among them) publish self-service products that consumers request through a portal, GitOps or API. Relevant as a big-UK-bank example of turning platform intake into published, requestable products; outcomes are claimed without figures.

## Themes
- platform-as-a-product: marketplace model separating providers from consumers, with eight interface factors; component principles "product-scoped, self-serve, operationally owned".
- cognitive-load-and-platforms: high cognitive load on developers and duplicated effort across teams named as the starting problem.
- platform-onboarding-friction: the older central model described as "Safety through tickets".
- process-governance-load: principles include reviewed and traceable changes, Git as source of truth, reconciliation to prevent drift, "governable".

## Key points
- NatWest scale on slides: over 20 million customers, about 59,000 staff.
- Request flow: developer portal / GitOps / API, then a Kratix control plane (Promise and configure pipeline), GitLab desired state, Flux reconciliation, Terraform Enterprise and AWS controllers, out to a multi-cluster fleet.
- Outcomes listed without figures: faster time to value, higher autonomy, improved security and compliance, standardisation at scale, clear ownership boundaries.
- Framed using the CNCF Platforms White Paper and Maturity Model.

## Could not verify
- An "over 97%" time-to-market reduction appears only in a talk description, not on the slides; the event is not named on the strategy page. Kratix itself is covered in kratix-docs-promises-intro.
