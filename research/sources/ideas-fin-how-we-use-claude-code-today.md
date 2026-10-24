---
title: "How we use Claude Code today at Intercom"
source_url: https://ideas.fin.ai/p/how-we-use-claude-code-today-at-intercom
author: Brian Scanlan (Intercom / Fin)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-03-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [skills-marketplace, org-learning-loop, human-review-gates, agent-factory-sdlc, non-engineer-builders, compounding-context-repo]
relevance: high
---

## Relevance to the project
The most mechanism-dense first-party account of Intercom's engineering harness: 13 internal plugins, 100+ skills, hooks that force a PR skill, a background CI-watching agent, a read-only production console over MCP, OpenTelemetry on every Claude Code event, and a SessionEnd hook that mines transcripts for missing skills and opens GitHub issues. It evidences the write-the-code, review, operate and learn rows of the Intercom map, and the handoff from "session" back into "harness improvement". It says nothing about discovery, specs or PM shaping work.

## Themes
- skills-marketplace: 13 plugins, 100+ skills, distributed to Macs by JAMF; most-used skills have quality evals and are reviewed regularly ("Keeping it all running").
- org-learning-loop: SessionEnd hook sends the transcript to Claude Haiku, classifies gaps (missing_skill, missing_tool, repeated_failure, wrong_info) and posts to Slack with a pre-filled GitHub issue; loop is sessions → gaps → issues → new skills ("Full lifecycle observability with OpenTelemetry").
- human-review-gates: PreToolUse hook blocks raw `gh pr create` unless the create-pr skill was loaded; another hook blocks push/commit/rebase/edit on merged PR branches ("PR workflow enforcement at the shell level").
- agent-factory-sdlc: after a PR is created a background agent monitors CI checks; code-review agents post only important feedback; incident skill works with Honeycomb traces, Datadog metrics and production logs in Snowflake ("And there's more").
- non-engineer-builders: design managers, customer support engineers and product management leaders were among the top five users of the read-only production console; Claude4Data (30+ analytics skills) used by sales reps, PMs and data scientists.
- compounding-context-repo: a weekly GitHub Action fact-checks and updates CLAUDE.md files ("And there's more").

## Key points
- Write the code: plugins and skills carry conventions; the create-pr skill asks *why* the change exists to capture business intent in the PR description (PR enforcement section). That PR description is the artifact that carries intent into review.
- Review: code review agents tuned to post only important feedback (no detail on rules here; see intercom-ai-approving-pull-requests).
- Operate: read-only Rails production console via MCP (read replica, critical tables blocked, Okta auth, DynamoDB audit trail; a skill-level gate forces safety docs to load first). Goal stated: all runbooks followable by Claude within six weeks.
- QA: a video-transcript skill turns Google Meet recordings into markdown with screenshots; a QA follow-up skill runs QA session docs through a 7-stage pipeline ending in GitHub issues (QA and video analysis). This is a concrete hand-off from a human QA session to tracked work.
- Flaky tests: 9-step forensic workflow, 20-category taxonomy; never skip a spec, never guess without CI data.
- Permissions: after five prompts a hook suggests a permissions analyzer that reads 14 days of transcripts and classes commands GREEN/YELLOW/RED.
- Telemetry: 14 hook event types to Honeycomb; prompts, messages and tool input not captured; transcripts to S3 with hashed usernames.

## Could not verify
- No outcome metrics (time saved, defects). "No issues so far" on the production console is self-reported.
- Does not cover product discovery, specs, PRDs, planning, deploy pipeline or on-call paging.
