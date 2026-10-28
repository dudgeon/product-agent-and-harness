---
title: "Score: developer-centric workload specification"
source_url: https://score.dev/
author: Score project (CNCF Sandbox)
publisher: score.dev
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, agent-legible-platform]
relevance: medium
---

## Relevance to the project
Score is the cleanest form of the consumer side of an intake contract: a developer (or an agent) declares what a workload needs (containers, ports, a database) in `score.yaml`, and the platform decides how to satisfy it per environment. It shows the split the dependency agent needs, "what I need" written by the consumer versus "how it is provided" owned by the platform, but it carries no approval, policy or lead-time information.

## Themes
- onboarding-as-code: "a developer-centric and platform-agnostic workload specification"; resource dependencies declared, resolved by the platform (home page).
- agent-legible-platform: same file works across local and remote environments, so an agent could write one declaration and let each platform resolve it.

## Key points
- CNCF Sandbox project; reference implementations score-compose (Docker Compose) and score-k8s (Kubernetes); other targets suggested (Cloud Run, ECS, Nomad).
- Originated at Humanitec (platform orchestrator vendor); Humanitec's role is not stated on the page.

## Could not verify
- How resource provisioners encode approvals or policy; the overview docs page did not render.
