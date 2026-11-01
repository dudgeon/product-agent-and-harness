---
title: "Ralph Wiggum as a \"software engineer\""
source_url: https://ghuntley.com/ralph/
author: Geoffrey Huntley
publisher: ghuntley.com
published: 2025-07-14
retrieved: 2026-10-31
type: article
evidence: anecdote
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, relay-information-loss, deterministic-scaffold-model-nodes]
relevance: medium
---

## Relevance to the project
The origin of the "Ralph loop": a bash loop that pipes the same PROMPT.md into a fresh agent session forever, with specs, a fix plan and AGENT.md in the repo as the only memory. It is the purest file-driven relay of an agent with itself: each iteration is a new session that re-reads the files, picks one task and commits. The author states the loss directly: later loops "will not have the reasoning in their context window", so reasons must be written into code and docs.

## Themes
- process-artifacts-as-coordination: `while :; do cat PROMPT.md | claude-code ; done`; specs one per file in specs/; fix_plan.md as the task list; "The @AGENT.md is the heart of the loop".
- relay-information-loss: fresh context each iteration; reasons for tests must be recorded in code and docs because the next loop will not have them.
- deterministic-scaffold-model-nodes: the loop is deterministic; task choice is the model's ("trust Ralph to decide what's the most important thing to implement"); back pressure from type checks, static analysis and tests.

## Key points
- One task per loop, single repository, single process.
- Human role: watch the stream for "patterns of bad behaviour", tune prompts ("like a guitar"), reset the repo or write rescue prompts.
- Failure modes reported: false "not implemented" conclusions from code search; placeholder implementations; duplicate implementations (the "Achilles' heel"); broken builds fixed by `git reset --hard`.
- Anthropic later packaged a Ralph loop as a Claude Code plugin (secondary sources; not verified here).

## Could not verify
- Single practitioner's report; outcomes (e.g. the CURSED language built over months) not independently checked. Model-summarised fetch.
