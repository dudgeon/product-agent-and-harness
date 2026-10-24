---
title: "Auto-complete your backlog: Unleash your favorite AI models with deep context, from plan to code, with Rovo Dev in Jira"
source_url: https://www.atlassian.com/blog/announcements/rovo-dev-in-jira
author: Gareth Wham (Atlassian)
publisher: Atlassian blog
published: 2026-04-02
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: user-story-mapping
themes: [agent-factory-sdlc, opportunity-to-code-chain, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
The launch of Rovo Dev in Jira (later documented as the Jira Coding Agent) plus an Atlassian engineer's first-person account of using it. Together they show the internal usage pattern: Slack request to work item to cloud session to draft PR, with plan review before execution and Jira Automation codifying proven patterns. They also show the gaps the engineer hit (review comments and CI failures not yet fed back to the agent).

## Themes
- `agent-factory-sdlc`: "Rovo Dev gathers the right context, proposes a concrete plan you can review and refine, then executes code changes, runs tests, and creates merge-ready PRs in a safe, configurable sandbox."
- `opportunity-to-code-chain`: feature-flag cleanup work items include "details about the flag, its intended state, and where it still appears in code"; Rovo Dev "pulls in context from the ticket, the relevant code across repositories, and repo-specific cleanup commands stored alongside the code"; PRs "linked back to the Jira work items that kicked everything off."
- `human-review-gates`: "Developers stay in the driver's seat, choosing what to delegate versus tackle themselves, reviewing plans and progress, and approving changes before anything ships."
- `vendor-claims-vs-independent-evidence`: "cleaned up 12 feature flags in two days, boosting cleanup velocity by around 85%, and ... created 29 of 31 cleanup PRs that required no manual code changes."

## Key points
- **Claimed:** "Because this work is tied back to Jira work items, PMs, designers, and other collaborators can stay close to the outcomes through the same issues, comments, and reviews."
- **Claimed:** automation by label triggers Rovo Dev with a repo-specific command; a "Jira-driven queue" paces work.
- **Anecdote, related post** ([Delivering 120 PRs in two weeks with Rovo Dev in Jira](https://www.atlassian.com/blog/developer/120-prs-two-weeks-rovo-dev-in-jira), Viktor Adam, 2026-03-30): "probably 95% or more of my dev work in it nowadays"; captures a Slack request into a work item "to commit against", starts a session, gets in-app and Slack notifications when ready, reviews the draft PR in Bitbucket. Gaps: to request changes he goes back to the Jira session; "eventually we should be able to just leave review comments on the draft PR"; CI failures not yet fed back automatically. Also asked the agent to analyse a parent work item and "capture some plans and options on subtasks", i.e. the agent writing work items for itself and others.

## Could not verify
- Baseline for the 85% velocity figure; whether plan-review step still exists in the current Jira Coding Agent UI (the support doc does not mention a plan step).
