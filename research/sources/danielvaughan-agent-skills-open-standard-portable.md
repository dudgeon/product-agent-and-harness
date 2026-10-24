---
title: "The Agent Skills Open Standard: Writing Portable SKILL.md Files That Work Across Codex CLI, Claude Code, and 30+ Tools"
source_url: https://codex.danielvaughan.com/2026/05/05/agent-skills-open-standard-portable-skills-codex-cli-cross-agent/
author: Daniel Vaughan
publisher: codex.danielvaughan.com (personal blog)
published: 2026-05-05
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, harness-portability]
relevance: medium
---

## Relevance to the project
Independent practitioner synthesis (updated 2026-10-24) of portable vs harness-specific skill features. Useful as a cross-check on the first-party docs, but a secondary source with its own unverified claims.

## Themes
- harness-portability: core spec portable across "32+" tools; extras (`agents/openai.yaml` for Codex; `context: fork`, `when_to_use`, `user-invocable`, `disable-model-invocation` for Claude Code) are ignored by other tools, so including them does not break but relying on them reduces portability; advice: "verify in at least two agents before calling a skill portable".
- skill-standards: "the standard lacks backward-compatibility guarantees"; no formal versioning; community registries vary in quality.

## Key points
- Claims Microsoft and OpenAI integrated skills within 48 hours of the December 2025 publication (unverified).

## Could not verify
- The 32+ tools list, 48-hour claim, AAIF governance of SKILL.md (no primary source found).
