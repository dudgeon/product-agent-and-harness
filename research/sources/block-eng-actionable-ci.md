---
title: Actionable CI
source_url: https://engineering.block.xyz/blog/actionable-ci
author: Angie Jones (AI Enablement for Engineering, Block)
publisher: Block Engineering Blog
published: 2026-02-23
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-factory-sdlc, human-review-gates, harness-portability, risk-sloped-review]
relevance: low
---

## Relevance to the project
A three-layer pattern (deterministic rules, LLM explanation, agentic autofix by headless goose) with an eligibility gate before any agent runs. Capability is exposed both as a button in CI and as an MCP server plus agent skills so any coding agent can use it, i.e. Block packages capability harness-neutrally even when goose is the default executor.

## Themes
- risk-sloped-review: autofix only when every detected issue is a supported type and the count is under a threshold.
- human-review-gates: goose opens a draft PR, CI validates, retries to a limit; promoted to ready-for-review only if it passes and the branch is unchanged; developer notified.
- harness-portability: MCP server and skills expose CI analysis to "AI coding agents"; "Agent Experience" becomes part of Developer Experience; developers can launch a fix prompt in their preferred AI tool.
- agent-factory-sdlc: supported categories: compile errors, dependency violations, lint, some unit test regressions.

## Could not verify
- No fix rates or volumes reported.
