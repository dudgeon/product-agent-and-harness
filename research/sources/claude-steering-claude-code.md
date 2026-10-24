---
title: "Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents"
source_url: https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more
author: Michael Segner (Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-06-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [harness-over-model, policy-enforcement-fail-open, task-context-isolation, enterprise-admin-controls, memory-architecture]
relevance: high
---

## Relevance to the project
Anthropic's own map of the seven ways to steer Claude Code (CLAUDE.md, rules, skills, subagents, hooks, output styles, system-prompt append), compared by when each loads, how it survives compaction, its context cost and its authority, is effectively the harness-layering menu the project's options need. Its key design claim is that prompted rules are not guardrails: anything that must never happen belongs in deterministic hooks, permissions or admin-deployed managed settings, the only way to enforce an organisation-wide rule. It also gives concrete governance moves for shared harnesses (owned, code-reviewed CLAUDE.md under 200 lines, per-team subdirectory files, MDM-deployed central CLAUDE.md that users cannot exclude). The framing is coding-centric; translating it to PM, designer and analyst harnesses is the project's job.

## Themes
- harness-over-model: "two separate dials" (model and effort) control capability, while the seven methods control behaviour; each trades context cost against authority (intro; "The seven methods").
- policy-enforcement-fail-open: prompted "never do this" rules fail under pressure, in long sessions, ambiguity or prompt injection; real guardrails are hooks (PreToolUse exit code 2) and permissions, with managed settings for org-wide enforcement ("When to use each method").
- task-context-isolation: subagents run in a fresh context and return only their final message; they can nest up to five levels and dynamic workflows orchestrate tens to hundreds of background agents (Subagents).
- enterprise-admin-controls: centrally managed CLAUDE.md deployed via MDM that individuals cannot exclude; managed settings cannot be overridden locally (CLAUDE.md; "When to use each method").
- memory-architecture: per-method compaction behaviour (root CLAUDE.md re-read after compaction; invoked skills re-injected up to a shared budget, oldest dropped first; hooks bypass compaction) (summary table).

## Key points
- **Comparison table.** Root CLAUDE.md: always loaded, high cost, for build commands, layout, conventions. Subdirectory CLAUDE.md: loaded on touching that directory. Rules (`.claude/rules/`): always-on or path-scoped via a `paths:` field, re-injected on compaction. Skills: name and description at start, body on invocation. Subagents: name, description and tool list at start, body only when called. Hooks: fire on lifecycle events, outside context. Output styles: replace the default system prompt, never compacted, highest instruction-following weight. System-prompt append: per-invocation flag, additive, diminishing adherence as it grows.
- **Shared CLAUDE.md decays like any unowned config.** Every team appends, nothing is deleted, every line costs every engineer tokens and dilutes adherence. Advice: under 200 lines, give it an owner, review changes like code; push team conventions into path-scoped rules and procedures into skills; `claudeMdExcludes` lets developers skip other teams' files.
- **Skill vs subagent.** Use a skill when you want to see and steer each step in the main thread; a subagent when intermediate results would clutter the main context (deep search, log analysis, dependency audit).
- **Hooks.** Types: command, HTTP, mcp_tool (deterministic) and prompt, agent (model judgement). Registered in settings.json, managed policy settings, or skill/agent frontmatter. Most hook output does not return to context unless configured. Skills plus hooks are called the building blocks of agent loops that run until a stop condition.
- **Output styles warning.** A custom style drops Claude Code's default engineering instructions (scope of changes, security, running tests before declaring done) unless `keep-coding-instructions: true`.
- **Anti-patterns:** "every time X, do Y" in CLAUDE.md (use a hook); "never do this" in CLAUDE.md (use hooks or permissions); 30-line procedures in CLAUDE.md (use a skill); unscoped API-only rules; personal preferences in project files (use user-level files).
- **Packaging.** Skills, subagents, hooks and output styles can be bundled as a plugin to share a setup across teammates or projects.
- **Limits:** guidance, not measurement; no adherence numbers for any method; written for software teams in Claude Code.

## Notable quotes
- "The model choosing to run a formatter is different from the formatter running automatically." ("When to use each method")
- "A real guardrail needs to be deterministic, and the enforcement methods are hooks and permissions." ("When to use each method")
