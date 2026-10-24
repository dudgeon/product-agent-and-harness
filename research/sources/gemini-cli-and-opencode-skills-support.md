---
title: Gemini CLI and OpenCode skills support (docs via search)
source_url: https://opencode.ai/docs/skills
author: OpenCode project; Google Gemini CLI (via third-party mirrors)
publisher: opencode.ai; mintlify mirror of google-gemini/gemini-cli docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, skill-standards]
relevance: low
---

## Relevance to the project
Confirms that open-source harnesses read the same SKILL.md format and honour `.claude/skills/` / `.agents/skills/`, so skills are the layer that already lets a user move between Claude Code, Gemini CLI and OpenCode. Details were gathered from search summaries, not the official English pages.

## Themes
- harness-portability: OpenCode reads `.opencode/skills/`, project `.claude/skills/` and `.agents/skills/`, walking up to the git root; only name, description, license, compatibility and metadata are read, "unknown frontmatter fields are ignored". Gemini CLI auto-discovers `.gemini/skills/` or `.agents/skills/`, injects names/descriptions into the prompt and uses an `activate_skill` tool that asks the user's permission before loading.
- skill-standards: a community compatibility table (add-skill project) says basic skills and `allowed-tools` work across agents but `context: fork` and hooks are Claude Code-only.

## Could not verify
- Official Gemini CLI doc page was not fetched; OpenCode path sources conflict (`skill/` vs `skills/`); read the official OpenCode page directly before relying on paths.
