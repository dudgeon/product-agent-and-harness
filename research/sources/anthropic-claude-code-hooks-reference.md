---
title: Hooks reference (Claude Code)
source_url: https://code.claude.com/docs/en/hooks
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, policy-enforcement-fail-open, enterprise-admin-controls]
relevance: high
---

## Relevance to the project
The reference spells out the decision vocabulary a deterministic gate can return (allow, deny, ask, defer; block) and, importantly, that hooks fail open by default. For a PM-skills harness this means a "hard gate" is only hard if it is written to exit 2 or set `onFailure: block`; otherwise a crashing check silently passes. It also shows the ask decision: a code gate whose output is "send this to a human".

## Themes
- gate-judge-separation: five handler types; command/http/mcp_tool are code, prompt/agent are model judgment ("send a prompt to a Claude model for single-turn evaluation") (§Hook types).
- policy-enforcement-fail-open: "a timed-out command, http, or mcp_tool hook doesn't block the tool call"; "The hook can deny the call, but staying silent doesn't approve it"; fail-closed is opt-in via `"onFailure": "block"` (v2.1.295+) (§Fail-open behaviour).
- policy-enforcement-fail-open: "Exit code 1 ... is a non-blocking error"; "If your hook is meant to enforce a policy, use `exit 2`" (§Exit codes).
- enterprise-admin-controls: managed hooks merge with and cannot be removed by user or project settings; `disableAllHooks` cannot disable them (§Scoping).

## Key points
- PreToolUse decisions go in `hookSpecificOutput.permissionDecision`: `allow`, `deny`, `ask`, `defer`, with a reason. Other events use top-level `decision: "block"`. PermissionRequest uses `decision.behavior` (allow/deny).
- Exit codes: 0 success (JSON applied); 2 blocking error (action stopped on blockable events); other codes non-blocking.
- The `if` filter is best-effort: "use the permission system rather than a hook to enforce a hard allow or deny."
- "For instructions that never change, prefer CLAUDE.md": the docs themselves place static conventions in advisory context and dynamic checks in hooks.
- Events cover tool gates (PreToolUse, PostToolUse, PermissionRequest, PermissionDenied), turn gates (UserPromptSubmit, Stop), subagent and compaction events.

## Could not verify
- Only the first ~100k of ~280k characters were read; event-by-event detail after SessionStart and the full prompt/agent-hook reference sections were not read here (the guide's version of those sections was read; see anthropic-claude-code-hooks-guide).
