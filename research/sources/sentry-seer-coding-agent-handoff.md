---
title: "Seer: hand off to a Cursor Cloud Agent (Sentry docs) and self-healing workflow cookbook"
source_url: https://docs.sentry.io/organization/integrations/coding-agents/cursor/
author: Sentry
publisher: Sentry docs
published: unknown
retrieved: 2026-10-26
type: docs
evidence: first-party
filed_by: research-shared-persistent-agents
themes: [remote-agent-invocation, human-review-gates, agent-factory-sdlc, identity-delegation]
relevance: medium
---
## Relevance to the project
Sentry's Seer is a shipped example of agent-to-agent handoff with the analysis attached (catalogue item 3): Seer does root-cause analysis and a solution plan, then passes "Seer's Autofix output alongside the issue context" to a Cursor Cloud Agent (or, per the cookbook, Claude Code or GitHub Copilot) which writes the fix in the real repo environment and opens a PR. The "stopping point" setting is a dial for how far the first agent goes before a person or second agent takes over. First-party docs; no outcome data. Companion source: https://sentry.io/cookbook/self-healing-workflow-seer/ and launch post https://blog.sentry.io/seer-can-now-trigger-cursor-agents-to-fix-your-bugs.

## Themes
- remote-agent-invocation: handoff is manual (dropdown next to "Find Solution" on the Root Cause Analysis card) or automatic (set Cursor Cloud Agent as the project's "Coding Agent" under Seer Automation) (Cursor Agent docs)
- agent-factory-sdlc: the handed-over object is "the root cause and solution as a structured prompt"; the receiving agent runs type checks, lint and tests in the working environment (cookbook, "Hand off to a coding agent")
- human-review-gates: stopping points are Root Cause, Solution, PR Drafted, or Hand off; "Seer never merges on its own"; teams are advised to start at "Stop after Solution" while they "build trust in Seer's diagnoses" (cookbook)
- identity-delegation: installing needs Sentry Owner/Manager/Admin and a Cursor *user* API key, so the downstream agent runs on one person's Cursor credential; docs do not state the identity explicitly (Cursor Agent docs)

## Key points
- Automatic Issue Fix runs only on issues with 10+ events, seen in the last 14 days, and a sufficient "fixability score" (cookbook FAQ).
- The cookbook names Claude Code, Cursor and GitHub Copilot as handoff targets.
- No data on fix acceptance rates.

## Notable quotes
- "Seer never merges on its own."
- "Treat a Seer-authored PR exactly like a human one: same review, same test run."

## Could not verify
- Neither page is dated. Whether the structured prompt carries a full plan or a summary is not shown.
