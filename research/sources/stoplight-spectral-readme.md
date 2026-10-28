---
title: "Spectral: a flexible JSON/YAML linter for creating automated style guides"
source_url: https://github.com/stoplightio/spectral
author: Stoplight (SmartBear)
publisher: GitHub
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, agent-legible-platform]
relevance: medium
---

## Relevance to the project
Spectral is how API governance becomes code: an API platform publishes a ruleset, and any OpenAPI/AsyncAPI/Arazzo document can be linted against it before review. For the dependency agent, a published ruleset is a machine-checkable slice of "what the API platform checks", which the agent can run on a team's spec before submitting it, turning some review rejections into pre-submission fixes.

## Themes
- governance-as-code: rules in JSON/YAML/JS with built-in functions (pattern, length, required keys, ordering) and custom JS/TS functions; extends predefined OpenAPI, AsyncAPI and Arazzo rulesets (README).
- agent-legible-platform: example public rulesets from Adidas, Azure and Zalando show large orgs publishing their API style rules as code.

## Key points
- Lints OpenAPI v2, 3.0, 3.1, 3.2; AsyncAPI; Arazzo v1.
- Apache 2.0; ~3.2k stars.

## Notable quotes
- "Spectral, being a generic YAML/JSON linter, needs a ruleset to lint files."
