---
title: "Inside the Development Workflow of Claude Code's Creator"
source_url: https://www.infoq.com/news/2026/01/claude-code-creator-workflow/
author: Sergio De Simone
publisher: InfoQ
published: 2026-01-10
retrieved: 2026-10-25
type: article
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [org-learning-loop, compounding-context-repo, rules-vs-judgment-encoding, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
A secondary report of Boris Cherny's own account of how the Claude Code team works. The CLAUDE.md practice is a curated-from-corrections improvement loop: a shared file in git (~2.5k tokens) where teams record Claude's mistakes and conventions, with Cherny tagging Claude on coworkers' PRs to add learnings. It also shows how one expert mixes modes: plan mode first, then auto-accept edits; a deterministic hook for formatting; pre-approved safe commands instead of skipping permissions; verification loops he credits with 2-3x quality.

## Themes
- org-learning-loop: each team keeps a shared CLAUDE.md in git with style conventions, design guidelines and PR templates; mistakes are recorded so Claude improves; Cherny tags Claude on PRs to add learnings.
- compounding-context-repo: the file was about 2.5k tokens at the time.
- rules-vs-judgment-encoding: deterministic where cheap: a PostToolUse hook on Write/Edit runs `bun run format || true`, removing a class of CI failures from model judgment entirely.
- evals-autonomy-trust: starts in plan mode, iterates until he likes the plan ("A good plan is really important!"), then switches to auto-accept; rarely uses `--dangerously-skip-permissions`, instead pre-approves safe commands via `/permissions`; skip flag reserved for sandboxed long runs.

## Key points
- Verification: giving Claude a way to verify its work (tests, bash, browser) improves quality "2-3x" per Cherny (his claim, no method given).
- Slash commands in `.claude/commands/` pre-compute context with inline bash (e.g. git status in `/commit-push-pr`).
- Pairs with traces-boris-cherny-light-cone-summary, where he says CLAUDE.md should be pruned as models improve.

## Could not verify
- The original X thread was not read; InfoQ is a secondary summary.
