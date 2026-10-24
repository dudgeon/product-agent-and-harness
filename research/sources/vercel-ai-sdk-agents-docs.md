---
title: AI SDK: Agents overview
source_url: https://ai-sdk.dev/docs/agents/overview
author: Vercel
publisher: AI SDK docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability, meta-harness]
relevance: medium
---

## Relevance to the project
The Vercel AI SDK now has a ToolLoopAgent plus a HarnessAgent that runs preconfigured harnesses (Claude Code, Codex, Pi) and streams them into AI SDK UI primitives, i.e. a framework acting as a thin meta-harness adapter. Contrast with Ronacher's report that using it only for provider abstraction was a mistake.

## Themes
- harness-portability: HarnessAgent wraps Claude Code, Codex or Pi behind one interface.
- agent-frameworks: ToolLoopAgent handles loop, context management and stop conditions (stopWhen, prepareStep).

## Key points
- ToolLoopAgent is the recommended class; loop control via stopWhen and prepareStep.
- Workflow patterns by using generateText/streamText with explicit control flow.
- @ai-sdk/tui for a terminal UI with approval prompts.
- Example model string anthropic/claude-sonnet-5.5.

## Could not verify
- No version number on page; web-UI streaming detail not in this page.
