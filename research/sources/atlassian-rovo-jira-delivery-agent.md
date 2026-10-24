---
title: Work with Jira Delivery agent
source_url: https://support.atlassian.com/rovo/docs/work-with-jira-delivery-agent/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [status-update-agents, legible-org-for-agents, opportunity-to-code-chain, one-job-per-agent]
relevance: medium
---

## Relevance to the project
The Jira Delivery Agent is Atlassian's out-of-the-box status-update and delivery-risk agent. Its documented tool list is the clearest first-party evidence of what a Teamwork Graph traversal returns for a work item (PRs, commits, branches, pages, hierarchy) and for a person (work items, pages, PRs, Loom videos, projects and goals). That is the context-flow evidence the lifecycle map needs between "write the code" and "set the goal".

## Themes
- `status-update-agents`: "produces tailored delivery artefacts for different audiences, including team stand ups and executive summaries"; daily digests; "detects work items that haven't moved for a specified period and automatically follows up with assignees."
- `legible-org-for-agents`: tool "get work-item context in twg": "Retrieve comprehensive context for a Jira work item, including related pull requests, commits, branches, pages, and hierarchy from the teamwork graph." Tool "get work summary for given user in twg": "assigned work items, Confluence pages, pull requests, Loom videos, and Atlas projects or goals." (tools table)
- `opportunity-to-code-chain`: a tool fetches "the projects linked to a team, including goals and epics, within a specific date range" and "Atlassian project, epic, or goal context".
- `one-job-per-agent`: a narrowly scoped out-of-the-box agent with its own tools and conversation starters.

## Key points
- **Documented:** chat use, plus automation use by starting the prompt with "Automation Mode" so the response can be used in the rule.
- **Documented tools:** fetch work item, JQL search, TWG work-item context, team projects/goals/epics, Confluence page, work item changelog, TWG user summary, project/epic/goal context, similar-summary search.
- **Claimed:** "continuously learns from your project's transitions and comment activity" (mechanism not described).
- The page's conversation-starters section is headed "Service Triage", which looks like a copy error.

## Could not verify
- Whether the TWG work-item context tool is the same as the Rovo MCP `getTeamworkGraphContext` tool (existing [MCP tools note](atlassian-rovo-mcp-server-supported-tools.md)).
