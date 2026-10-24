---
title: Using Skills (goose docs)
source_url: https://goose-docs.ai/docs/guides/context-engineering/using-skills
author: goose maintainers (AAIF)
publisher: goose-docs.ai
published: unknown (page copyright 2026)
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [skill-standards, harness-portability]
relevance: medium
---

## Relevance to the project
Confirms goose reads the Agent Skills format (SKILL.md) from the cross-harness .agents/skills/ path and also from Claude Code's .claude/skills/ locations, so a skill written for Claude Code would load in goose or a goose fork. This lowers the switching cost of the "fork goose" option for capability assets, though not for behaviour.

## Themes
- skill-standards: skills are subdirectories with SKILL.md (name, description frontmatter) plus scripts and templates; progressive loading (names and descriptions at start, full instructions on match or by name).
- harness-portability: discovers .agents/skills/, ~/.agents/skills/, .goose/skills/, .claude/skills/, ~/.claude/skills/; "goose skills work with Claude Desktop and other agents that support Agent Skills".

## Key points
- Plugins can ship skills, namespaced as plugin:skill.
- Recipes are distinct: shareable configurations bundling instructions, prompts, settings (and, per CUSTOM_DISTROS.md, sub-recipes and subagent settings).
- Goosehints carry general preferences and project context; the page does not mention AGENTS.md (the repo itself has an AGENTS.md file).
- The sidebar lists Security and an Extension Allowlist page (not read).

## Could not verify
- Whether goose reads AGENTS.md as context; extension allowlist semantics and whether an admin can enforce it.
