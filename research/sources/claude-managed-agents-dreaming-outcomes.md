---
title: "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration"
source_url: https://claude.com/resources/articles/new-in-claude-managed-agents
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [memory-architecture, evals-autonomy-trust, org-learning-loop, single-agent-many-skills]
relevance: medium
---

## Relevance to the project
Anthropic's launch of three Managed Agents features that map onto harness concerns the project tracks: "dreaming", a scheduled job that reviews past sessions and memory stores to curate shared memory (with optional human review before changes land); "outcomes", a rubric graded by a separate grader in its own context window that sends the agent back for another pass; and lead-agent orchestration of specialist subagents on a shared filesystem, traced in the Console. Outcomes is the nearest vendor primitive to encoding a PM's definition of "good" for agent output. Bears on context-and-memory, pm-agent-evaluation and harness-upkeep. Dreaming is research preview, the rest public beta; benchmark gains are Anthropic's, customer results are customers' claims.

## Themes
- memory-architecture: memory captures learnings per agent; dreaming "refines that memory between sessions, pulling shared learnings across agents"; can update automatically or have changes reviewed first (§Build self-improving agents with dreaming).
- evals-autonomy-trust: outcomes: write a rubric, a separate grader evaluates "in its own context window, so it isn't influenced by the agent's reasoning", and the agent iterates; up to 10 points better task success than a standard prompting loop; +8.4% docx and +10.1% pptx task success in internal benchmarks (§Outcomes).
- org-learning-loop: dreaming surfaces "recurring mistakes, workflows that agents converge on, and preferences shared across a team" (§dreaming).
- single-agent-many-skills: counterpoint: multiagent orchestration delegates to specialists with their own model, prompt and tools when there is "too much work for a single agent to do well" (§Multiagent orchestration).

## Key points
- **Dreaming.** Scheduled; reads sessions and memory stores; extracts patterns, restructures memory to stay high-signal; human review optional. Research preview, by request.
- **Outcomes.** Rubric can be structural (a framework, a presentation standard, requirements) or subjective (brand voice, visual guidelines); a webhook notifies when the outcome is met.
- **Orchestration.** Lead agent splits work; specialists run in parallel on a shared filesystem; persistent events let the lead check back mid-workflow; every step traceable in the Claude Console (which agent did what, in what order, why).
- **Customer claims.** Harvey: completion rates up about 6x in their tests with dreaming. Netflix: build-log analysis agent processes batches in parallel and surfaces only recurring patterns. Spiral by Every: Haiku lead agent, Opus drafting subagents, drafts scored against editorial principles and the user's voice from memory; only passing drafts returned. Wisedocs: document QA agent 50% faster with outcomes grading against internal guidelines.
- **Limits.** Benchmarks are internal and unspecified; Harvey's "6x" lacks a baseline; no account of grader error or of bad memories being consolidated by dreaming.

## Notable quotes
- "Agents do their best work when they know what 'good' looks like." (§Outcomes)

## Could not verify
- Benchmark sets behind the 10-point and docx/pptx figures.
