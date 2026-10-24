---
title: What is parallel AI agent coding? An in-depth guide for product teams
source_url: https://departmentofproduct.substack.com/p/what-is-parallel-ai-agent-coding
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-11-04
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [meta-harness, pm-persona-role-expansion, human-review-gates, agent-failure-modes, harness-over-model, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
An explainer for product teams on running several coding agents at once (Cursor 2.0's up-to-eight agents, GitHub Agent HQ, Claude Code on the web), each in its own git worktree, with a human or orchestrator comparing and merging results. Its PM angle is a claim, not evidence: that PMs, as "mini orchestrators", may be well suited to judging agents' output and could run several versions of a feature as experiments. It adds little beyond what is filed on local parallel-session managers ([Claude Squad](github-claude-squad.md), [Conductor](conductor-build-homepage.md)) and on async coding agents ([Simon Willison](simonwillison-async-coding-agents-tag.md)). Company facts are second-hand from vendor launch posts and press.

## Themes
- meta-harness: GitHub Agent HQ described as a command centre for agents from several vendors in the GitHub workflow; Osmani's caution that normalising many agents behind one platform can become lowest-common-denominator ("GitHub Agent HQ"; "Google Chrome's engineering leader").
- pm-persona-role-expansion: PMs and designers could take on the orchestration and evaluation role for lower-risk features if they have enough technical grounding; engineers would need breadth across the stack more than depth ("Why should product teams care?").
- human-review-gates: each agent's work lands as a separate branch; the engineer reviews, picks between models' solutions and merges (stages 5-6).
- agent-failure-modes: parallelism brings merge conflicts, interdependencies and harder debugging; a startup CTO's split says parallel agents do well on small, well-defined and backend tasks and poorly on architecture and UI that needs visual feedback ("Real world examples").
- harness-over-model: teams may need to invest first in CI, technical docs and staging environments for parallel agents to pay off ("Why should product teams care?").
- vendor-claims-vs-independent-evidence: repeats an 80% headcount cut at one small company (WSJ) and "90% of code AI generated" at Anthropic without checking.

## Key points
- Six stages: prompt (optionally several models), agent creation with isolated worktrees, per-agent planning, execution (with Cursor's in-IDE browser for checking), aggregation and review, merge.
- Parallel vs sequential agent workflows defined; Cursor's Composer model credited with parallel tool calls.
- Best-of-N by model: the same task given to different models, with a human choosing the winner.
- Practitioner uses: Osmani (UI bug fixes, small features, migrations, dependency upgrades; orchestrators such as Claude Squad and Conductor); Willison (research proofs of concept, codebase explanations, small maintenance, tightly specified work).

## Notable quotes
- "PMs are essentially mini orchestrators themselves"

## Could not verify
- Cursor, GitHub and WSJ claims were not opened. Several examples were embedded tweets or videos not visible in the text copy.
- Paywalled; summarised, not reproduced.
