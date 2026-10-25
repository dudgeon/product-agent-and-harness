---
title: Configure permissions (Claude Agent SDK)
source_url: https://code.claude.com/docs/en/agent-sdk/permissions
author: Anthropic
publisher: Claude Code docs (Agent SDK)
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, evals-autonomy-trust, human-review-gates, risk-sloped-review]
relevance: high
---

## Relevance to the project
A concrete, ordered stack of who decides each agent action: code hooks, then declarative deny and ask rules, then a mode, then allow rules, then a runtime callback (usually a human). It shows the three gate types layered in one pipeline, with a model classifier (`auto` mode) as a mode rather than a separate system, and with modes changeable mid-session "as trust builds". Useful as a template for a PM agent's decision-rights layer.

## Themes
- gate-judge-separation: evaluation order is hooks → deny rules → ask rules → permission mode → allow rules → `canUseTool` callback (§How permissions are evaluated).
- evals-autonomy-trust: `setPermissionMode()` mid-session lets you "start restrictive and loosen permissions as trust builds, for example switching to acceptEdits after reviewing Claude's initial approach" (§Set permission mode).
- risk-sloped-review: some actions no mode auto-approves (critical-path `rm`, AskUserQuestion, MCP tools marked `requiresUserInteraction`, org connector tools set to ask) (§Allow and deny rules, warnings).
- human-review-gates: plan mode routes every file edit to the callback "regardless of allow rules", and subagents inherit plan mode "so that handing work to one doesn't get around reviewing the plan first" (§Plan mode; §Subagent inheritance).

## Key points
- Modes: `default` (no auto-approvals; unresolved calls go to callback), `dontAsk` (prompt becomes deny; for "a fixed, explicit tool surface for a headless agent"), `acceptEdits`, `bypassPermissions` (hooks and deny rules still apply), `plan`, `auto` ("A model classifier reviews actions ... allowing or blocking each one it reviews").
- A hook `allow` does not skip deny and ask rules; a hook deny applies even in bypassPermissions. "For checks that must run on every tool call, use a PreToolUse hook."
- Pitfall stated: auto-approved tools never reach `canUseTool`, so checks put there are "silently bypassed".
- My reading: the human is the default fallback at the bottom of the stack; code sits at the top; the model classifier is an optional middle tier that replaces most human prompts.

## Could not verify
- The linked auto-mode decision-order page was not read here (see claude-auto-mode-in-production for the classifier).
