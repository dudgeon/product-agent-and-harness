---
title: Best practices for Claude Code
source_url: https://code.claude.com/docs/en/best-practices
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, human-review-gates, evals-autonomy-trust, single-agent-many-skills]
relevance: high
---

## Relevance to the project
Anthropic's own guidance already encodes a structure ladder inside one general harness: vague prompts for exploration, plan mode for uncertain multi-file work, precise specs plus verification for delegation, skills/hooks for repeatable workflows, subagents for isolated review, non-interactive `claude -p` for CI and fan-out. That is direct evidence that the general harness spans both classes in the working hypothesis, with structure added by the user on demand rather than by switching tools.

## Themes
- work-structure-spectrum: "Vague prompts can be useful when you're exploring"; "Sometimes you should skip planning ... because the task is exploratory"; if you could describe the diff in one sentence, skip the plan.
- evals-autonomy-trust: give Claude a check it can run; "the difference between a session you watch and one you walk away from"; hooks are deterministic where CLAUDE.md is advisory.
- human-review-gates: adversarial review in a fresh subagent; a Writer/Reviewer two-session pattern; auto-mode classifier replaces per-action prompts.
- single-agent-many-skills: skills for repeatable workflows (e.g. a fix-issue skill with `disable-model-invocation: true` for side effects); CLAUDE.md only for broadly applicable rules.

## Key points
- Context is the fundamental constraint; subagents keep investigation out of the main context.
- Fan-out: loop `claude -p` over a task list or `/batch` across worktrees for migrations (highly structured, repetitive work).

## Could not verify
- Publication date (living docs page). Guidance is Anthropic's own; no outcome data.
