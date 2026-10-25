---
title: "How Sentry built end-to-end bug fixing with Claude Managed Agents"
source_url: https://claude.com/customers/sentry
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [build-vs-buy, opportunity-to-code-chain, human-review-gates, agent-factory-sdlc]
relevance: medium
---

## Relevance to the project
Sentry's Seer hands its root-cause analysis to a coding agent on Claude Managed Agents, which plans, implements and opens a pull request, closing the maintain-stage loop from detected bug to reviewable code. For the strategy it is a clean build-versus-buy data point (one engineer shipped the integration in weeks because sandboxing, lifecycle and runtime were bought, not built) and an example of model-provider coupling chosen for data residency (Claude via Vertex AI). Anthropic customer story; volume and speed figures are the customer's claims, and no fix-acceptance or merge rate is given.

## Themes
- build-vs-buy: building a coding agent meant sandboxing, lifecycle management and a runtime, "a significant detour"; Managed Agents let a single engineer ship the initial integration "in weeks instead of months" and removed ongoing infra upkeep (sections "The challenge", "The solution").
- opportunity-to-code-chain: covers the tail of the chain for bugs: telemetry to root cause to plan to code to PR, with the handoff between diagnosis and coding agent as Sentry's differentiating design work (section "How the Seer-to-PR workflow runs").
- human-review-gates: "The developer's job shifts from writing the fix to reviewing it"; target state is developers reviewing proposed changes rather than writing them (sections "Seer-to-PR workflow", "Looking ahead").
- agent-factory-sdlc: same Managed Agents infrastructure runs background fixing of the most actionable bugs and real-time developer help; claimed reviews on over 600k PRs a month (summary list; workflow section).

## Key points
- Seer already used Claude to analyse stack traces, profiling, traces, logs, spans and metrics; the gap was the developer's context switch from diagnosis to implementation.
- Provider route: Claude through Google Vertex AI to preserve customer data residency and avoid adding a new subprocessor.
- Customer demand: many Sentry customers already used Claude Code and wanted debugging and coding bridged.
- Claimed scale: over 1 million RCAs a year; "near immediate reviews" on over 600k pull requests a month.
- Junior developers get guidance; seniors move to validating analysis rather than combing events.
- Limits: no accuracy, PR-acceptance or regression data; "most actionable bugs" is undefined; nothing on what permissions the coding agent has in customer repos.

## Notable quotes
- "Turns out telling developers what's wrong with their code isn't enough: they want you to fix it too." (Indragie Karunaratne, Senior Director of Engineering, AI/ML, Sentry)

## Could not verify
- Publication date; how "over 1 million RCAs" and "600k pull requests a month" are counted.
