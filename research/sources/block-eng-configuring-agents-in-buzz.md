---
title: "Player 2 Has Entered the Game: Configuring Agents in Buzz 🐝"
source_url: https://engineering.block.xyz/blog/configuring-agents-in-buzz
author: Will Pfleger (Applied AI, Block)
publisher: Block Engineering Blog
published: 2026-08-10
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [one-job-per-agent, harness-portability, memory-architecture, cost-control-routing, human-review-gates]
relevance: medium
---

## Relevance to the project
A Block practitioner's team of five role-agents in Buzz: orchestrator, two executors, a reviewer from a different model family, and a quick-task agent, each defined by harness, model, effort and an instructions field. It shows Block's agent packaging moving from recipes inside goose to persistent named agents across harnesses, with the harness itself a per-agent setting.

## Themes
- one-job-per-agent: roles differ mainly by model, system prompt and effort; the executor is told to report out-of-scope issues rather than expand scope.
- harness-portability: harness choices `goose`, `claude` (Claude Code), `codex`, or the default `buzz-agent`; any ACP harness works.
- human-review-gates: reviewer agent deliberately from another model family for independent review; "respond-to" setting (Only me default, Selected people, Anyone).
- memory-architecture: agents read `~/AGENTS.md` and SKILL.md from `.agents/skills/`; encrypted memory on the relay, "core" memory injected each session, "cold" memory read on demand.
- cost-control-routing: app-wide defaults for harness, provider, model, effort, shared API keys; per-agent overrides.

## Key points
- Example models: orchestrator on Claude Fable 5 (xhigh effort), executors on Claude Sonnet 4.6, reviewer on GPT-5.6 Sol, quick tasks on GPT-5.6 Luna.

## Could not verify
- Internal adoption; whether this setup is typical at Block or one engineer's.
