---
title: Building verification loops in Claude Code with skills
source_url: https://claude.com/resources/articles/building-verification-loops-in-claude-code-with-skills
author: Delba de Oliveira (Claude Code team, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-07-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [tacit-knowledge-capture, org-learning-loop, human-review-gates, agent-ready-intent, skill-standards]
relevance: medium
---

## Relevance to the project
Anthropic's how-to for turning the manual checks a person repeats after every agent change into skills, so the agent verifies its own work, and then promoting those checks from personal use to chained workflows to team-wide PR gates. For a product harness this is a concrete path from one person's tacit review habits to shared, enforced standards, and it names a "spec validation" skill that checks each change against a markdown spec in the repo. No outcome data; it is guidance, not evidence of effect.

## Themes
- tacit-knowledge-capture: "write down everything that you find yourself doing every time", then encode it as a skill; skill-creator can interview the user to draft it ("Writing verification loops"; "Make it a skill").
- org-learning-loop: progression standalone, embedded, chained, on every PR, where "verification stops being personal infrastructure and becomes team infrastructure" ("On every PR").
- human-review-gates: in a chained loop "you only step in when something escalates back to you"; hold off on PR-wide gates while the chain is in flux ("Chained"; "On every PR").
- agent-ready-intent: built-in "spec validation" skill verifies each change against a markdown spec in the repo and fixes violations ("Built-in verification loops").
- skill-standards: example SKILL.md with `name`, `description` (stating when to use) and `allowed-tools` frontmatter; embedding only works on skills you control, so plugin-managed skills are wrapped by chaining instead ("Embedded").

## Key points
- **Built-in loops:** `/verify` (build, run, observe the change); toolchain errors (list build and test commands in CLAUDE.md); Code Review, a managed multi-agent PR review service (research preview); GitHub Actions running a verification skill on each push; spec validation; rubrics in Managed Agents (beta) with a separate grader agent whose failures loop back for rework.
- **Four placements:** standalone (cross-cutting checks such as accessibility audits, invoked deliberately); embedded (one line appended to the producing skill); chained (one skill calls the next; the Claude Code team runs `/code-review`, `/simplify`, `/verify` and a `/design` check against DESIGN.md); on every PR (same skills applied regardless of author diligence).
- **Deterministic project rules count too:** e.g. reject any migration that drops a column without a backfill step.
- **Costs:** chained loops increase token spend; test before deploying broadly.
- **Limits:** no data on defect rates or time saved; examples are code-centric (no product-artifact checks such as PRD completeness), though the pattern transfers.

## Notable quotes
- "What started as a habit ... becomes a contract." ("Chained")
