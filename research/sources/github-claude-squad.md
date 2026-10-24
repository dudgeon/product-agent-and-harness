---
title: smtg-ai/claude-squad (README)
source_url: https://github.com/smtg-ai/claude-squad
author: smtg-ai
publisher: GitHub
published: 2026-10-24
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-portability]
relevance: low
---

## Relevance to the project
The minimal end of the wrapper spectrum: tmux plus git worktrees to run several agents in parallel from one terminal. Shows how little 'meta' is needed for the parallel-session use case.

## Themes
- [[meta-harness]]: terminal app (`cs`) running Claude Code (default), Codex, Gemini, Aider, OpenCode, Amp in tmux sessions with worktrees; AGPL-3.0; ~8.7k stars.
- [[harness-portability]]: agent-agnostic by running any CLI; no policy, sharing or persistence beyond the local machine.

## Key points
- Known failure: 'timed out waiting for tmux session', fixed by updating the agent; `--autoyes` experimental.
