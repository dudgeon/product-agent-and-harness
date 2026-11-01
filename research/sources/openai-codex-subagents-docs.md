---
title: "Subagents (Codex docs, ChatGPT Learn)"
source_url: https://learn.chatgpt.com/docs/agent-configuration/subagents
author: OpenAI
publisher: learn.chatgpt.com (formerly developers.openai.com/codex/subagents)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [task-context-isolation, harness-portability, identity-delegation, delegation-return-contract]
relevance: high
---

## Relevance to the project
OpenAI's primary docs for Codex subagents, previously known only from a blog ([Vaughan](danielvaughan-codex-vs-claude-code-multi-agent.md)). Codex and ChatGPT Work both spawn parallel subagents that return summaries to the main thread. Two points matter for model B (through line): a subagent inherits the parent's sandbox, approvals, MCP servers and skills and a custom agent cannot override them (so the subagent acts with exactly the person's reach); and in ChatGPT Work, the non-engineer surface, subagents run in OpenAI's hosted environment "without local sandbox or approval controls".

## Themes
- task-context-isolation: subagents keep "noisy intermediate output (logs, exploration notes, stack traces)" off the main thread and return summaries.
- delegation-return-contract: "Its summary and results go back to the main thread, which collects them into the final response"; a good request says how to divide work, whether to wait for all agents, and what summary to return.
- identity-delegation: subagents inherit the parent turn's sandbox and approval settings, provider, MCP servers and skills; custom instructions asking an agent not to edit "don't create a separate read-only sandbox"; if an approval cannot be surfaced the action fails back to the parent.
- harness-portability: custom agents are TOML files in `~/.codex/agents/` or `.codex/agents/` with `name`, `description`, `developer_instructions`; Cursor reads these files too ([Cursor subagents](cursor-docs-subagents.md)).

## Key points
- Spawning is mostly explicit ("spawn two agents", "use one agent per point"); Ultra in ChatGPT Work can delegate proactively; current releases also delegate when AGENTS.md or a skill asks.
- `[agents]` config: `enabled` (default true), `max_concurrent_threads_per_session` (unset, Codex chooses), `default_subagent_model`, `default_subagent_reasoning_effort`, `interrupt_message`.
- Guidance: parallel agents for read-heavy work (exploration, tests, triage, summarisation); caution on parallel writes; more tokens than single-agent runs.
- Visible in Codex CLI, IDE extension and the ChatGPT desktop app.

## Could not verify
- No date or version on the page; no mention of Codex Cloud or a maximum nesting depth (the blog's `max_depth` 1 default is not confirmed here).
