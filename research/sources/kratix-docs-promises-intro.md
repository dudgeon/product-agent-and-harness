---
title: "Promises (Kratix reference)"
source_url: https://docs.kratix.io/main/reference/promises/intro
author: Syntasso (Kratix maintainers)
publisher: docs.kratix.io
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, agent-legible-platform]
relevance: high
---

## Relevance to the project
A Kratix Promise is the closest open-source construct to "a platform publishes its intake as a machine-readable contract and fulfils requests against it": the platform team ships a Promise, Kratix creates a Kubernetes API (CRD) for it, and a consumer requests a resource by submitting an object against that API, which triggers ordered workflows. The API schema is discoverable like any CRD, so an agent could read and submit it; approvals are not part of the model and would have to be a workflow step.

## Themes
- onboarding-as-code: a Promise bundles dependencies, an API for requesting it, workflows (Promise and Resource lifecycles, each with `configure`/`delete`) and destination rules (Definition, Workflows).
- agent-legible-platform: the request API is a namespace-scoped CRD; `requiredPromises` declares dependencies between platform offerings (API, Requirements).

## Key points
- A request is "customised with the options the Promise exposes"; one request can fan out into several resources (e.g. database + Jenkins + update script).
- Governance on the page is limited to `destinationSelectors` (where resources land); no approval or compliance step is described.

## Notable quotes
- A Promise is "a set of instructions written in YAML".

## Could not verify
- Whether teams commonly add approval/compliance containers to workflows (not on this page).
