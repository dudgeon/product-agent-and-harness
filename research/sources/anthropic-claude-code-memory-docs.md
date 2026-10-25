---
title: "How Claude remembers your project (Claude Code docs)"
source_url: https://code.claude.com/docs/en/memory
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [memory-architecture, compounding-context-repo, harness-portability]
relevance: high
---

## Relevance to the project

The first-party definition of project structure for Claude Code: scoped CLAUDE.md files, path-scoped .claude/rules, @imports, AGENTS.md fallback, and a separate model-written auto memory. This is the de facto 'project structure' convention a Claude-based meta-harness inherits.

## Themes

- memory-architecture: CLAUDE.md (human-written instructions) vs auto memory (Claude-written learnings; first 200 lines or 25KB loaded each session).
- compounding-context-repo: the hierarchy managed policy > user > project > local lets org, team and personal context layer.
- harness-portability: Claude reads AGENTS.md when no CLAUDE.md exists in or above the working directory (v2.1.277+); otherwise CLAUDE.md wins, and a CLAUDE.md can @import AGENTS.md.

## Key points

- Locations: managed policy (e.g. /Library/Application Support/ClaudeCode/CLAUDE.md), user, project (./CLAUDE.md or ./.claude/CLAUDE.md), local (CLAUDE.local.md).
- Guidance: keep each CLAUDE.md under about 200 lines; @path imports up to four hops; .claude/rules/*.md are modular and may be scoped by path; symlinks allowed with approval for external targets.
- 'Claude treats them as context, not enforced configuration'; to block an action use a PreToolUse hook.
- claudeMdExcludes can exclude files at any settings layer.

## Could not verify

I read only part of this long page (via a saved fetch); auto-memory storage location and subagent memory details not captured.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
