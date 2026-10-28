---
title: "A decade of cloud native at ING: lessons learned and what comes next"
source_url: https://www.techzine.eu/experts/infrastructure/139326/a-decade-of-cloud-native-at-ing-lessons-learned-and-what-comes-next
author: Jacopo Nardiello (ING, Global Infrastructure Transformation Lead)
publisher: Techzine
published: 2026-03-06
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [platform-as-a-product, platform-onboarding-friction, process-governance-load, cognitive-load-and-platforms]
relevance: high
---

## Relevance to the project
An ING infrastructure lead on ten years of the bank's private cloud: early Kubernetes as namespace-as-a-service and full API self-service, then "layered legacy" in which "thirty solid interfaces feel like thirty different products". The fix is product discipline: every capability gets an owner, a clear contract, semantic versioning, a lifecycle, a reliability target and a cost per unit, with policy validation, identity and tenancy checks automated before anything runs, aligned to compliance, risk, security and the ECB. This is a regulated bank describing, from the inside, what makes platform capabilities legible and consumable, the same properties a dependency agent would need to read.

## Themes
- platform-as-a-product: each capability needs "an owner, a clear contract, semantic versioning, a lifecycle, a reliability target, and a cost-per-unit metric".
- cognitive-load-and-platforms: "Suddenly, thirty solid interfaces feel like thirty different products."
- platform-onboarding-friction: self-service without product discipline becomes "a YAML vending machine (or worse)"; the goal is that "the recommended way is also the easiest way".
- process-governance-load: policy validation, identity and tenancy controls run automatically before scheduling; open standards support upgrade control, auditability of production changes and reduced concentration risk, with the ECB named among external requirements.

## Key points
- The platform runs "thousands of applications and services".
- 2030 vision: a team picks a template, links its repository and provisions a test environment in "minutes, not weeks", with golden paths handling promotion to production; the IDP combines pipelines with agentic workflows. This is a target, not a measured result.
- Portfolio to double without headcount doubling (vision).
