---
title: "Extend Claude Code (features overview: when to use CLAUDE.md, skills, subagents, hooks, MCP and plugins)"
source_url: https://code.claude.com/docs/en/features-overview
author: Anthropic
publisher: Claude Code docs (code.claude.com)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [capability-packaging-layers, single-agent-many-skills, task-context-isolation, policy-enforcement-fail-open, delegation-return-contract]
relevance: high
---

## Relevance to the project
This is Anthropic's current layering guidance for its own harness: which capability goes in CLAUDE.md, a skill, a subagent, a dynamic workflow, cross-session messaging, MCP, a hook or a plugin, with a context-cost table. It is the vendor's answer to "how should an intent-refinement or dependency-identification capability reach the person's harness under model B (through line)": method as a skill, enterprise systems as MCP, isolation as a subagent, enforcement as a hook, distribution as a plugin. It also states plainly that instructions in CLAUDE.md or a skill are requests, not guarantees.

## Themes
- capability-packaging-layers: "Match features to your goal" table (CLAUDE.md, output style, skill, subagent, dynamic workflow, cross-session messaging, code intelligence, MCP, hook, artifact) and "Plugins are the packaging layer" that bundles skills, hooks, subagents and MCP servers.
- single-agent-many-skills: "Skills are the most flexible extension"; skills "can run in your current conversation or in an isolated context via subagents"; a skill + MCP pattern ("MCP provides the connection; a skill teaches Claude how to use it well").
- task-context-isolation: Skill vs Subagent tab: a subagent has "its own context" and runs in isolation; "Work happens separately, only summary returns".
- policy-enforcement-fail-open: Hook vs Skill tab: "An instruction like 'never edit .env' in CLAUDE.md or a skill is a request, not a guarantee. A PreToolUse hook that blocks the edit is enforcement."
- delegation-return-contract: subagents load "Fresh, isolated context" containing their own system prompt, listed skills, CLAUDE.md and git status, and "Whatever context the lead agent passes in the prompt"; a fork instead loads the parent's conversation.

## Key points
- Build-over-time triggers: a convention wrong twice goes into CLAUDE.md; a playbook pasted a third time becomes a skill; data copied from a browser tab becomes an MCP server; a side task that floods the conversation goes to a subagent; something that must always happen becomes a hook; a second repository needing the same setup becomes a plugin.
- Context cost by feature: CLAUDE.md every request; skills low (descriptions each request, body on use); MCP low until used (tool search on by default); subagents isolated from main session; hooks zero unless they return output.
- Layering precedence: CLAUDE.md files are additive; skills and subagents override by name (managed > user > project for skills; managed > CLI flag > project > user > plugin for subagents); MCP servers override by name (local > project > user); hooks merge.
- Subagent vs dynamic workflow: "With subagents, Claude decides turn by turn what runs next. In a workflow, the script decides."
- "To pass a finding from one of your sessions to another, ask the first session's Claude to send it" (cross-session messaging).
- Keep CLAUDE.md under 200 lines; move reference content to skills.

## Notable quotes
- "Skills are reusable content you can load into any context." Subagents are described as running "separately from your main conversation."
- "If a rule must hold every time, make it a hook rather than a prompt instruction."

## Could not verify
- The page has no publication date; it is a living doc and was read on 2026-10-31.
- Nothing on the page addresses remote deployed agents beyond "connect that system as an MCP server".
