---
title: "Claude Code /insights: Your Personalized AI Usage Report"
source_url: https://blog.vincentqiao.com/en/posts/claude-code-insights/
author: Vincent Qiao
publisher: blog.vincentqiao.com
published: 2026-04-08
retrieved: 2026-10-25
type: article
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops]
relevance: low
---

## Relevance to the project
A third-party description of Claude Code's `/insights` command, which turns a user's local session transcripts into a report with a Friction Analysis (categories such as `misunderstood_request` and `wrong_approach`, each with examples from real sessions) and a Suggestions section that proposes CLAUDE.md lines for instructions the user kept repeating. That is a shipped "curate corrections into the instruction file" loop with the human still choosing what to paste. Filed as anecdote: the author shows a sample header, not real report sections, and cites no Anthropic documentation; an official docs page could not be found.

## Themes
- skill-improvement-loops: scans sessions under `~/.claude/projects/` (up to 200, most recent first), analyses them with Claude Opus, writes an HTML report; seven sections including Friction Analysis and Suggestions that propose CLAUDE.md rules from repeated instructions (post).

## Key points
- Friction categories named: `misunderstood_request`, `wrong_approach`; three categories shown, each with two examples.
- Author states nothing is uploaded to the cloud; not verified.

## Could not verify
- No official Anthropic page for `/insights` was found (code.claude.com/docs/en/insights returned 404; site search found only third-party posts). Report structure and privacy claims are the author's.
