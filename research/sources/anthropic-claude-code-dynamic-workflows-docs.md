---
title: "Orchestrate subagents at scale with dynamic workflows (Claude Code docs)"
source_url: https://code.claude.com/docs/en/workflows
author: Anthropic
publisher: Claude Code docs (code.claude.com)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [deterministic-scaffold-model-nodes, work-structure-spectrum, human-review-gates, delegation-return-contract]
relevance: high
---

## Relevance to the project
The docs counterpart to the launch article ([dynamic workflows](claude-code-dynamic-workflows.md)). It adds a comparison table that answers "who holds the plan" for subagents, skills, agent teams and workflows, and it states the human-gate limit: a workflow takes no mid-run user input, so sign-off between stages means one workflow per stage. A saved workflow is a JavaScript file in `.claude/workflows/` or a plugin, with schema-typed agent returns, so a multi-stage intent-shaping method could ship as a repeatable script inside the person's harness rather than as a separate agent.

## Themes
- deterministic-scaffold-model-nodes: "A workflow moves the plan into code ... A workflow script holds the loop, the branching, and the intermediate results itself, so Claude's context holds only the final answer"; `agent()`, `pipeline()`, `parallel()`, `phase()`; `Date.now()` and `Math.random()` throw so relaunches replay deterministically.
- work-structure-spectrum: table rows "Who decides what runs next" (Claude turn by turn; Claude following the prompt; the lead agent; the script) and "Where intermediate results live" (context window; context window; a shared task list; script variables).
- human-review-gates: "No mid-run user input ... For sign-off between stages, run each stage as its own workflow"; per-run approval of the planned phases in manual mode, first launch only in auto mode, none in bypass, `-p` or SDK.
- delegation-return-contract: an `agent()` call with a `schema` returns JSON matching the shape, validated with up to five retries; the agent detail view shows each agent's prompt, tool calls and result; `/deep-research` lists claims it could not verify as unverified rather than refuted.

## Key points
- Scale: up to 16 concurrent agents by default (configurable 1 to 256), 4,096 items per call, 1,000 agents per run; "Large workflow" warning above 25 agents or 1.5M projected tokens.
- Resume: within the same session only; completed agents return saved results; a failure reruns every later agent; leaving the session stops the run; cloud sessions keep results with the conversation history.
- Saved to `.claude/workflows/` (shared via repo) or `~/.claude/workflows/`; distributable in plugins; accepts `args`.
- Subagents in a workflow use the person's permission rules; in auto mode the prompt a script passes to `agent()` "doesn't count as a request from you" for the classifier.
- Org admins can disable workflows in managed settings.

## Could not verify
- No data on quality or cost versus a single-agent run; examples remain code-centred, with research (`/deep-research`) the main non-code case.
