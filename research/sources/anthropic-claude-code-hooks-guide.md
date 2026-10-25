---
title: Automate actions with hooks (Claude Code hooks guide)
source_url: https://code.claude.com/docs/en/hooks-guide
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, work-structure-spectrum, method-as-harness, human-review-gates]
relevance: high
---

## Relevance to the project
The clearest first-party statement that a hook is the deterministic counterpart to an advisory instruction ("certain actions always happen rather than relying on the LLM to choose to run them"), and, in the same page, that a hook can hand the decision to a model (prompt and agent hooks). It separates *where* a gate fires (a fixed lifecycle event the harness enforces) from *who judges* (script, single model call, tool-using subagent). That separation bears directly on the rigidity-spectrum question: a PM skill's completeness gate can be a fixed checkpoint even when the check itself needs judgment.

## Themes
- gate-judge-separation: command hooks give "deterministic control"; "for decisions that require judgment rather than deterministic rules" use `type: "prompt"` (single-turn model call returning `{"ok": ..., "reason": ...}`) or `type: "agent"` (subagent with Read/Grep/Glob, up to 50 tool turns) (intro; §Prompt-based hooks; §Agent-based hooks).
- work-structure-spectrum: the Stop-hook example asks a model "Check if all tasks are complete"; on `ok: false` Claude keeps working with the reason as its next instruction, turning a gate into a loop (§Prompt-based hooks).
- method-as-harness: agent-hook example "Verify that all unit tests pass" before Claude may stop (§Agent-based hooks).
- human-review-gates: the walkthrough's first hook is a Notification hook so the human is alerted when Claude waits for input (§Set up your first hook).

## Key points
- Hooks are shell commands (also HTTP, MCP tool, prompt, agent types) that run at fixed lifecycle points; framed as "deterministic control" versus relying on the model to choose (intro).
- Prompt hooks: "Claude Code sends your prompt and the hook's input data to a Claude model to make the decision"; `model` field lets you choose a more capable model. Outcomes on `ok: false` differ by event: Stop/SubagentStop feed the reason back so Claude continues (unless `impossible: true`); PreToolUse denies the tool call and by default ends the turn (`continueOnBlock: true` returns the reason to Claude so it can adjust); UserPromptSubmit ends the turn.
- Agent hooks are experimental: "For production workflows, prefer command hooks." Rule of thumb given: "Use prompt hooks when the hook input data alone is enough to make a decision. Use agent hooks when you need to verify something against the actual state of the codebase."
- Safety valve: Claude Code overrides a Stop hook after it blocks eight times in a row with no tool call between; scripts should check `stop_hook_active` (§Troubleshooting).
- My reading (judgment, not the source's): the doc implies three gate types at one enforcement point; the fixed part is *that* the check runs, not *how* it decides.

## Notable quotes
- "certain actions always happen rather than relying on the LLM to choose to run them" (intro)
- "For decisions that require judgment rather than deterministic rules, use `type: \"prompt\"` hooks." (§Prompt-based hooks)

## Could not verify
- No adherence, error-rate or cost data for any hook type; page undated.
