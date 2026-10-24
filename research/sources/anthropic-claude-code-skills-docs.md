---
title: Extend Claude with skills (Claude Code docs)
source_url: https://code.claude.com/docs/en/skills
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, skill-standards, single-agent-many-skills]
relevance: high
---

## Relevance to the project
The clearest first-party statement of what is portable and what is Claude Code-specific in skills. It shows that a "standard" skill and a "Claude Code skill" differ materially, and that even Anthropic's own surfaces (claude.ai uploads, Skills API) accept only the six-field subset. This is the main evidence for "quietly harness-specific".

## Themes
- harness-portability: Claude Code adds 13 extension fields beyond the six spec fields (`when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`). "Claude.ai uploads, the Skills API, and package_skill.py accept only the six spec fields and fail with a hard error on any other key."
- skill-standards: skills and custom commands have been merged (`.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`).
- single-agent-many-skills: `context: fork` runs a skill as a subagent (SKILL.md becomes the subagent's prompt, no conversation history); a subagent definition's `skills` field injects full skill content at startup. So a skill can encode a delegated sub-task without new infrastructure.

## Key points
- Skill locations and precedence: enterprise (managed settings dir) > personal `~/.claude/skills` > project `.claude/skills`; plugin skills namespaced `/plugin:skill`; claude.ai account skills sync to `~/.claude/skills/synced/` for Cowork, cloud and terminal sessions.
- Skill-level `hooks` and `allowed-tools`/`disallowed-tools` let a skill carry its own guardrails, but they only bind in harnesses that implement them.
- Doc also describes a skill-creator eval flow (`evals/evals.json`); not read in detail.

## Could not verify
- Last ~18k characters of the page not read.
