---
title: Practical ways to use Claude Routines at work - a Guide for Product Teams
source_url: https://departmentofproduct.substack.com/p/practical-ways-to-use-claude-routines
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-06-02
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [feedback-triage-agents, status-update-agents, identity-delegation, human-review-gates, skill-standards, memory-architecture, pm-tool-connectivity, non-engineer-builders]
relevance: high
---

## Relevance to the project
The most concrete PM-facing account so far of unattended agent runs: five Claude Code routines for product work (weekly backlog triage, release notes on merge, API deprecation watchdog, competitor changelog tracker, weekly feedback digest), each spelled out as trigger, connectors, skill and output channel. It makes a governance point plainly: an attached connector can be used, writes included, without per-action approval, so the connector list is the run's permission boundary. It also shows the friction a PM meets: routines are built around a code repository, which the PM must have before anything else works. It bears on the scheduled-digests target-user option, the session-persistence dimension and identity/delegation. Product facts are second-hand from Anthropic docs and talks; there is no outcome data.

## Themes
- feedback-triage-agents: the weekly feedback aggregator reads Slack #feedback, Intercom, App Store and Play Store reviews, groups patterns across sources, checks each against open tickets and flags untracked ones as candidates (section 5). Backlog triage groups new tickets by theme, flags duplicates and ranks 5-10 with a rationale, using the team's own priority order (section 1).
- status-update-agents: Monday digests posted to Slack before standup; separate versions per audience (PM vs engineering lead) as separate routines or one prompt (section 1).
- identity-delegation: "Claude can use all tools from attached connectors - including write operations - without asking for permission during each run"; the advice is to attach only what the routine needs and check read-only options in the Permissions tab ("How connectors work"; section 5). Matches the [routines docs](anthropic-claude-code-scheduled-tasks.md) point that a stored prompt can't give live consent.
- human-review-gates: release notes are drafted to Notion and a link posted to Slack "for human review"; the PM can open a run's session, watch it and steer mid-run, then fix the instructions for next time (sections 1, 2).
- skill-standards: process steps live in a SKILL.md and voice rules in a separate brand file, so the voice is reused across any routine that writes customer-facing text and the routine prompt stays one line (section 2). The watchdog keeps its list of monitored APIs in a reference file the skill reads each run (section 3).
- memory-architecture: the competitor tracker keeps state between runs as a snapshot file in the repo and diffs against it; the first run is only a baseline (section 4).
- pm-tool-connectivity: connectors named per routine: Jira/Linear/GitHub Issues, Slack, Notion, Google Drive, Intercom/Zendesk via MCP, optionally Salesforce or billing for revenue weighting (sections 1, 5).
- non-engineer-builders: setup is a desktop form (name, instructions, trigger, repositories, connectors, behaviour, permissions) or /schedule in plain language; but remote runs need repository access, and the tutorial starts by creating a GitHub repo ("Local vs Remote").

## Key points
- What routines are: proactive Claude Code sessions on Anthropic's infrastructure, so they don't depend on the laptop; local runs are also possible.
- Triggers: time-based; GitHub events (PR opened/closed, issue, release); custom events posted to an endpoint the routine exposes, with whatever context the caller includes.
- Backlog triage filter ideas: customer tier, revenue (ARR cross-reference), current strategic theme (for example churn signals in a retention quarter), urgency in the ticket's language.
- Release notes: triggered by a closed PR on a release branch; filters out internal changes; groups New / Improved / Fixed. Describes Anthropic's built-in release-notes prompt (classify, skip internal-only changes, list migration steps for breaking changes, post as a PR comment). Suggests "multiplying" notes per audience and mentions that Uber execs get a product-update podcast (second-hand, unsourced).
- API deprecation watchdog: weekly; checks third-party changelogs, searches the codebase for affected versions, opens a GitHub issue with affected files, assigns and pings the engineer, and posts a "check ran" note when nothing is found.
- Competitor tracker: competitors list file plus snapshot file; open the first sessions to check it reads the right pages.
- Further resources: a talk by an Anthropic speaker at the London Claude Code event, and the routines docs.

## Notable quotes
- "If you give Claude a connector, assume it may use it."

## Could not verify
- The Behaviour and Permissions tabs were "not fully visible" to the author, so what read-only controls exist per connector is unclear from the post.
- Whether a routine can be owned or seen by a team rather than one person isn't addressed; the docs note says routines are personal and act as their creator.
- The Uber exec podcast claim has no link.
- Paywalled; summarised, not reproduced. Prompts in the post are described, not copied.
