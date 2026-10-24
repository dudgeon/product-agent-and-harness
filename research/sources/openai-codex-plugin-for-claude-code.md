---
title: openai/codex-plugin-cc: Use Codex from Claude Code to review code or delegate tasks
source_url: https://github.com/openai/codex-plugin-cc
author: OpenAI
publisher: GitHub
published: 2026-03-31
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, harness-portability, skill-standards]
relevance: high
---

## Relevance to the project
A concrete cross-vendor primary-harness-calls-another-agent integration: an official OpenAI plugin that lets Claude Code delegate review (`/codex:review`, adversarial review) and tasks (`/codex:rescue`, background, resume) to Codex via the Codex app server. Runs on the same machine with local Codex auth, so it is a cross-harness delegation but not a deployed remote agent. Release date 2026-03-31 comes from secondary coverage.

## Themes
- `harness-portability`: Plugin distributed through the Claude Code plugin marketplace mechanism by a competitor; delegates through a `codex:codex-rescue` subagent; jobs backgrounded with status/result/cancel.
- `remote-agent-invocation`: Optional Stop-hook review gate runs Codex on Claude's output; README warns it can create a long loop that drains usage limits.

## Key points
- Requires Node 18.18+, Codex CLI, ChatGPT subscription (incl. free) or API key; usage counts against Codex limits.
- `/codex:transfer` creates a persistent Codex thread from the Claude session (`codex resume`).
- Repo showed ~34.5k stars at capture, though secondary sources gave other counts on release day.
- No dedicated security section in the README.

## Could not verify
- Release date relies on secondary sources (OpenAI community post and blogs).
