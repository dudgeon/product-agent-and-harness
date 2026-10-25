---
title: Hooks (Kiro docs)
source_url: https://kiro.dev/docs/hooks/
author: Kiro (AWS)
publisher: kiro.dev
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [human-review-gates, process-artifacts-as-coordination]
relevance: medium
---

## Relevance to the project
Kiro's hooks are event-triggered actions of two kinds: a shell command (deterministic) or an injected agent prompt (judgment). The same event can carry either, which makes the gate-type dimension concrete inside one product, and shows how spec-driven tools pair advisory spec files with enforced checks.

## Themes
- human-review-gates: a Stop command hook can ask for confirmation before the agent finishes; PreToolUse can block risky tool calls until preconditions are met (body).
- process-artifacts-as-coordination: hooks are JSON files in .kiro/hooks/ (or ~/.kiro/hooks/), so the checks are versioned with the repo (body).

## Key points
- Triggers named on the page: PostFileSave, PreToolUse, PostToolUse, Stop; a matcher filters by file path regex or tool ID, category, MCP server or wildcard. Full list is on a separate page.
- Command action runs in project root with session context as JSON on STDIN; agent action injects a prompt "for steering the agent's behavior".
- Examples: ESLint --fix after .ts edits; generate tests or docs on new files; quality check before the agent finalises.
- Fields: name, trigger, matcher, action, timeout (default 60 s), enabled.
- My judgment: Kiro thereby offers both an enforced and an advisory control on the same hook point; only the command type is deterministic.

## Could not verify
- The Hook types page with the full trigger list was not opened. Retrieved via WebFetch, a model-summarised view.
