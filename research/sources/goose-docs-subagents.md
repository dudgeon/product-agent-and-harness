---
title: Subagents (goose docs)
source_url: https://goose-docs.ai/docs/guides/context-engineering/subagents
author: goose maintainers (AAIF)
publisher: goose-docs.ai
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-block-product-practices
themes: [single-agent-many-skills, one-job-per-agent, task-context-isolation, cost-control-routing]
relevance: medium
---

## Relevance to the project
Shows how goose turns its single general agent into task agents on demand: temporary subagents configured by prompt or by a recipe, with restricted extensions, their own model, and no ability to recurse or touch the scheduler. It is the mechanism by which "recipes as task agents" works inside one harness.

## Themes
- single-agent-many-skills / one-job-per-agent: subagents are "temporary, independent instances" for specific tasks; configured by direct prompt or a recipe YAML (found via `GOOSE_RECIPE_PATH` or the working directory).
- task-context-isolation: subagents inherit the parent's extensions unless limited; they cannot spawn subagents, enable or modify extensions, or create, modify or delete scheduled tasks (security restrictions).
- cost-control-routing: `GOOSE_SUBAGENT_MODEL` / `GOOSE_SUBAGENT_PROVIDER` set a cheaper model for subagents; recipes override.

## Key points
- Defaults: 5 concurrent subagents per parent, 1000 max turns, 5-minute timeout, full-detail return.
- Autonomous spawning only in Autonomous mode; disabled in manual, smart and chat modes.
- External subagents: e.g. OpenAI Codex CLI run as an MCP server.
- Failed or timed-out subagents return nothing.
