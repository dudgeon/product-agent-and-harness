---
title: "Background Coding Agents: Context Engineering (Honk, Part 2)"
source_url: https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2
author: Max Charas and Marc Bruggmann, Spotify
publisher: Spotify Engineering blog
published: 2025-11-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [agent-ready-intent, harness-over-model, task-context-isolation, one-job-per-agent, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The most concrete public guide we have on writing intent for an unattended agent at scale. Spotify's lessons (describe the end state, state when not to act, give examples, define done as tests, one change per prompt) are a ready-made checklist for "agent-ready intent". It also argues for large, version-controlled static prompts and a deliberately small toolset over many MCP tools, because each tool adds unpredictability. That is a design choice our harness has to make too.

## Themes
- agent-ready-intent: prompt rules: tailor to the agent, state preconditions (when not to act), use concrete examples, define the end state ideally as tests, one change at a time, ask the agent what the prompt lacked (section "The proof is in the prompt").
- harness-over-model: home-built loop (10 turns, 3 retries, user-picked files via git grep) failed on multi-file changes; switching to Claude Code (todo lists, subagents) made it the top agent, used in about 50 migrations and the source of most merged agent PRs (Spotify claim, Nov 2025).
- task-context-isolation: code search and docs tools are intentionally not exposed; context is condensed into the prompt up front or built by workflow agents.
- one-job-per-agent: only three tools: a Verify MCP tool (format, lint, test, with log summarising), a restricted Git tool (never push or change origin), and allowlisted Bash.
- evals-autonomy-trust: "still flying mostly by intuition": no structured way to evaluate prompts or models, and no way to tell whether a merged PR solved the original problem.

## Key points
- Goose and Aider were tried first; they went far on one prompt but did not reliably produce mergeable PRs at migration scale.
- The custom loop failed when context filled: the agent lost track of the task.
- Claude Code works better with end-state prompts; the home-built agent needed strict step lists.
- Two prompt anti-patterns: too generic (agent guesses intent) and too specific (breaks on the unexpected).
- Static prompts can be versioned, tested and evaluated; the more tools, "the more dimensions of unpredictability".
- Spotify recommends encoding guidance in target repos as tests, linters and API docs rather than in agent instruction files, because thousands of repos have different builds.

## Notable quotes
- "Claude Code does better with prompts that describe the end state and leave room for figuring out how to get there."

## Could not verify
- The comparison table of agents (Table 1) was not fully read.
