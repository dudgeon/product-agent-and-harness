---
title: Build skills (ChatGPT and Codex docs)
source_url: https://learn.chatgpt.com/docs/build-skills
author: OpenAI
publisher: OpenAI (redirected from developers.openai.com/codex/skills)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, harness-portability, skills-marketplace]
relevance: high
---

## Relevance to the project
OpenAI adopts the same SKILL.md format for Codex and ChatGPT and adds its own metadata file and discovery paths, giving a second first-party data point for "portable core plus harness-specific edges". The plugin is OpenAI's distribution unit ("package a skill as a plugin, which can bundle skills and connectors").

## Themes
- skill-standards: "Skills follow the open agent skills standard"; folder with SKILL.md name+description; scripts/references/assets optional.
- harness-portability: Codex-specific `agents/openai.yaml` (UI metadata, `allow_implicit_invocation`, tool dependencies); discovery paths REPO `.agents/skills` (cwd, parents, root), USER `$HOME/.agents/skills`, ADMIN `/etc/codex/skills`, SYSTEM bundled; per-skill disable in `~/.codex/config.toml`; explicit invocation with `$skill`.
- skills-marketplace: sharing beyond one repo = plugin bundling skills and connectors; `$skill-installer` for curated skills.

## Key points
- Initial skill list budget is 2% of context window (or 8,000 chars) -> raising to 10,000 tokens via `skills.max_context_tokens`: a hard limit on how many skills can be advertised.
- Best practice stated by OpenAI: one job per skill; "prefer instructions over scripts unless you need deterministic behavior".
- Built-in `skill-creator`; Record & Replay drafts a skill from a demonstration.

## Could not verify
- Enterprise administration beyond the ADMIN path; plugin packaging format for Codex.

## Added by research-skill-rigidity-spectrum (2026-10-25)
Verified at the current URL https://learn.chatgpt.com/docs/build-skills (the developers.openai.com/codex/skills URL now redirects there; first-party).
- Exact best-practice wording: "Prefer instructions over scripts unless you need deterministic behavior or external tooling." The note's earlier quote omitted "or external tooling".
- `scripts/` is "Optional: executable code"; the skill creator defaults to "Instruction-only". Other practices: "Write imperative steps with explicit inputs and outputs"; one job per skill.
- The page does not define what counts as needing deterministic behaviour, and has no gating section; the nearest controls are `allow_implicit_invocation: false` (explicit `$skill` only) and `enabled = false` in config.
- Themes: work-structure-spectrum, gate-judge-separation.
