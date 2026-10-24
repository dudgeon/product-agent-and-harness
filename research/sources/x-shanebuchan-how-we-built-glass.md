---
title: How We Built Glass: Vibe Coding a Product Used by 700 People
source_url: https://x.com/shanebuchan/status/2044524727679566156
author: Shane Buchan (Ramp, Glass core team)
publisher: X (Article, plus summary post)
published: 2026-04-15
retrieved: 2026-10-24
type: x-post
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [memory-architecture, skills-marketplace, agent-factory-sdlc, build-vs-buy]
relevance: high
---

## Relevance to the project

The most technical Glass source: how a small team built it by vibe coding, the codebase-health tooling that kept it coherent, and concrete designs for connections, Dojo, and memory. Directly informs harness design concepts and prototypes.

## Themes

- **memory-architecture**: 24-hour pipeline mines sessions plus Slack/Notion/Calendar and writes memory files; agent reads them at session start and never edits memory mid-chat; inspectable files.
- **skills-marketplace**: Dojo = Git repo of markdown skills; Glass hides branch/PR/review behind 'publish'; 350+ skills.
- **agent-factory-sdlc**: Glass builds Glass: Defrag skill, design system, doc validation in PRs, pre-commit gates; idea-to-production in hours; humans review diffs.
- **build-vs-buy**: Origin: Jay Sobel's weekend project; Goddijn took it over; 3-person core team; users before a team.

## Key points

- Shared MCP proxy: connect once at launch, startup from ~45s to ~2s with 13+ integrations.
- Pre-bundled CLIs; Okta SSO; self-healing integrations with plain-language re-auth.
- Distribution/auth across a managed fleet called one of the hardest problems (Cameron Leavenworth).
- Direction: every feature a conversation; the UI is a reference, not a requirement.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify

Full article text not saved; replies not retrieved.
Context (audit 2026-10-24): this is the April 2026 architecture (desktop app, local MCP proxy, laptop-side scheduling). Ramp's October Laminar post moves Glass sessions to cloud workers and says the codebase there is agent-written but not 'vibe coded' ([source](ramp-builders-building-laminar.md)).
