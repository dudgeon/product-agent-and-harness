---
title: "Ramp Inspect Architecture 2026: How Background Coding Agents Scale Safely"
source_url: https://wavect.io/blog/ramp-inspect-background-coding-agent-infrastructure-2026/
author: Kevin Riedl (Wavect)
publisher: Wavect blog
published: 2026-09-09
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, build-vs-buy, human-review-gates, cost-control-routing]
relevance: medium
---
## Relevance to the project
Third-party secondary analysis of the Inspect pattern from a consultancy that sells related services (says it is unaffiliated with Ramp or Modal). Its value is the argument that the sandbox is a container for policy, not the policy, and a pilot design. It is commentary, not evidence of a deployment.

## Themes
- shared-persistent-sessions: blast radius is set by credentials, network egress, data, GitHub permissions, internal system access and auditability, not by the sandbox; scaling sandboxes without those controls yields 'hundreds of isolated ways to make a bad decision faster'
- build-vs-buy: buy commodity sandbox infrastructure; build or heavily customise base images, harness, context, permissions and evals
- cost-control-routing: measure accepted changes per unit of review effort and incident risk, not PRs per day; review capacity and CI become the bottleneck

## Key points
- Recommends a 30-day pilot on one repo with ~30 tasks including failure injection (killing a sandbox, rotating a credential, stale snapshot).
- Risks named but not evidenced: repository drift after snapshot restore, stale-environment failures.
