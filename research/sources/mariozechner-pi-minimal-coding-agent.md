---
title: What I learned building an opinionated and minimal coding agent
source_url: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
author: Mario Zechner
publisher: mariozechner.at
published: 2025-11-30
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, build-vs-buy, harness-over-model]
relevance: high
---

## Relevance to the project
A practitioner who built his own harness (Pi) because existing ones inject hidden context. Gives the "build" case (full context control, tiny core) with honest costs (maintaining provider abstraction and TUI), and an opposing view on permissions, MCP and sub-agents to Claude Code. Pi is also the base some other projects embed (e.g. OpenClaw).

## Themes
- build-vs-buy: reason to build is control and visibility of context; cost is maintaining unified-LLM API that leaks and a TUI.
- agent-frameworks: four packages (pi-ai, pi-agent-core, pi-tui, pi-coding-agent); under 1,000-token system prompt; four tools.
- harness-over-model: claims a minimal harness is competitive on Terminal-Bench 2.0 with Opus 4.5 (scores only in images).

## Key points
- Omits MCP (token bloat), sub-agents (hidden), plan mode (use PLAN.md), built-in todos, background bash (use tmux), permission prompts (YOLO, argues sandbox is largely theatre once code execution and network are both present).
- Cross-provider context handoff, split tool results for LLM vs UI.
- Notes that benchmarks do not reflect real-world performance; error rates varied with US Pacific hours.

## Notable quotes
- "if I don't need it, it won't be built"

## Could not verify
- Benchmark numbers appear only in images and were not read; claim of beating Claude Code on terminal-bench comes from secondary search summary only.
