---
title: Simon Willison: async-coding-agents posts (2025-2026)
source_url: https://simonwillison.net/tags/async-coding-agents/
author: Simon Willison
publisher: simonwillison.net
published: 2026-02-16
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, agent-failure-modes, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
A running independent log of using cloud coding agents (Codex cloud, Claude Code for web, Jules, Copilot coding agent). Gives real-use texture (Codex task ~4 min, PRs 'cover most requirements' but failing tests from Jules), a PR-count adoption comparison (PRarena, 2025-10-01) and recurring security cautions (prompt injection, lethal trifecta, internet-access allowlists). This tag page was read as excerpts, not each post.

## Themes
- `remote-agent-invocation`: Defines the category 'asynchronous coding agents'; heavy user of Claude Code on the web via native apps; container managed by Anthropic lowers risk to his machine.
- `agent-failure-modes`: Jules PR (2025-05-19) covered most requirements but tests failed; Codex internet access off by default with a 71-domain default allowlist, recommends GET/HEAD/OPTIONS only; prompt-injection reports (Rehberger's Summer of Johann).
- `evals-autonomy-trust`: Agents must demonstrate work, not only pass tests (Showboat/Rodney, 2026-02-10).

## Key points
- PRarena snapshot 2025-10-01: Codex ~1.9M PRs (84.2% merged), Copilot ~247K (61.5%), Claude Code ~146K (84.2%, undercounted), Jules ~35.4K (78.5%).
- 2025-12-31: 'Codex cloud is now called Codex web'.

## Could not verify
- Individual posts and the PRarena methodology were not opened; figures come from the tag-page excerpts.
