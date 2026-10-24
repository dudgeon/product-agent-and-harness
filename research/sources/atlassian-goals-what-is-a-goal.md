---
title: What is a goal? (Atlassian Goals)
source_url: https://support.atlassian.com/platform-experiences/docs/what-is-a-goal/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [product-artifact-primitives, opportunity-to-code-chain, status-update-agents, legible-org-for-agents]
relevance: medium
---

## Relevance to the project
Defines the "set the goal" object in Atlassian: a Goal with owner, target date, status, monthly update, sub-goals, and links to projects and Jira epics (and, per related pages, to any Jira work item). This is the top of the Teamwork Graph chain an agent could traverse (goal to epic to work item to PR), and Teamwork Graph has a relationship type for it. The goal is a communication object updated by a human monthly, not an agent-set target.

## Themes
- `product-artifact-primitives`: "Goals in Atlassian represents the outcomes that multiple projects or streams of work contribute to"; minimum fields: name, owner, date or period; frameworks OKRs, KPIs, SMART.
- `opportunity-to-code-chain`: goal page lists "Linked items, such as sub-goals, projects, and Jira epics"; "Goals can be linked to issues in the list view of your Jira project."
- `status-update-agents`: owners get a reminder on the first of each month; updates are released to followers on the 8th.
- `legible-org-for-agents`: Teamwork Graph relationship type [JiraWorkItemContributesToAtlassianGoal](https://developer.atlassian.com/platform/teamwork-graph/api-reference/relationship-types/jira-work-item-contributes-to-atlassian-goal) (Early Access per search snippet; page not read).

## Key points
- **Documented:** status values include On track, Off track, At risk; OKR scoring 0.0 to 1.0 with 0.7 as target.
- **Documented, related page** ([Understand how goals and projects work with Jira](https://support.atlassian.com/platform-experiences/docs/understand-how-goals-and-projects-work-with-jira/)): Atlassian projects (in Home) are "a separate concept from a Jira space"; a project syncs title, target dates and tags with a parent-level work item (epic by default); goals and projects are for communicating "between teams", Jira for work inside a team.
- **Search snippet (not fetched):** [Link work to goals on a work item](https://support.atlassian.com/jira-software-cloud/docs/link-issues-to-goals-in-the-issue-view/) says a Goals field on the work item lets you create, search or paste a goal; goals can connect to any work type.
- **Not documented here:** linking goals to JPD ideas (the JPD quick-start guide reportedly offers a "Goals" field on ideas; not verified whether it is the Atlassian Goals object). Rovo MCP exposes goals and projects as readable (existing note [Rovo MCP supported tools](atlassian-rovo-mcp-server-supported-tools.md)).

## Could not verify
- Whether any agent writes goal updates (Home has "Rovo in Home Dashboards", not read); JPD-to-Goal link.
