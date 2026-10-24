---
title: "When AI Becomes Your New Team Member: The Story of Goose Janitor"
source_url: https://goose-docs.ai/blog/2025/08/28/ai-teammate
author: Angie Jones (Head of Developer Relations, Block)
publisher: goose blog
published: 2025-08-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [one-job-per-agent, tacit-knowledge-capture, agent-factory-sdlc]
relevance: low
---

## Relevance to the project
A Block iOS engineer packaged feature-flag removal as a parameterised goose recipe ("Goose Janitor") run from the CLI, after weeks of capturing the team's know-how in context files. A small example of the path from tacit team knowledge to a reusable task agent.

## Themes
- tacit-knowledge-capture: phase 1 documented safe flag removal in `.mdc`, `.goosehints` and symlinked docs; phase 2 validated it across three generations of flag implementations.
- one-job-per-agent: `goose run` recipe with flag key, variant to keep, and whether to open a PR; uses Xcode Index MCP; plans, implements, builds and tests locally.
- agent-factory-sdlc: opens draft PRs via GitHub CLI during "Feature Flag Removal Month".

## Could not verify
- No results reported; human review not described.
