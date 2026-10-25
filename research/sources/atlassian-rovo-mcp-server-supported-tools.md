---
title: "Atlassian Rovo MCP server: supported tools"
source_url: https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [legible-org-for-agents, human-review-gates]
relevance: high
---

## Relevance to the project

The most concrete first-party list of what an agent can read and write in Jira, Confluence, Goals and Projects. It shows which artifact operations are default-on and which (delete, project admin) are admin-gated, a useful pattern for a meta-harness permission model.

## Themes

- legible-org-for-agents: agents can read work items, projects, boards, sprints, pages, whiteboards, databases, goals and projects.
- human-review-gates: delete and project-management tools are disabled by default and need an admin to enable.

## Key points

- Jira read: work items, projects, boards, sprints, filters, dashboards, comments, changelogs, worklogs, statuses, versions, components. Write: create/edit/transition work items, comments, links, versions, sprints, boards. Search by JQL.
- Jira delete and manage (create/update projects, read workflows, edit screens) are off by default; admin must enable.
- Confluence read: pages, blogs, whiteboards, databases, spaces, comments, versions, attachments, tasks, templates, permissions. Write: create/update/copy/move/archive/restore, comments, labels, permissions, public links; full-body replace or granular edit. Search by CQL. Generated infographics cost 15-30 Rovo credits.
- Goals and Projects (Atlassian Home objects): search/get goals, goal updates, goal types, projects, project updates; create goals/projects and updates; add connections to them.
- JSM: alerts, on-call, requests, resolver plans.

## Could not verify

Compass was not covered on the page. No statement about rate limits per tool.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.

## Verification (user-story-mapping re-check, 2026-10-24)

Re-read verbatim from a curl download of the page (tags stripped), not via summarising fetch.

- Scope of page: "The tools listed on this page are only available with Atlassian MCP v2." Tools are grouped into permission groups ("read, write, or search"); "Organization admins grant or revoke access at the permission-group level". Only "Primary" tools are shown to agents up front; others are found with `discover` and run through `executeRead`, `executeWrite`, `executeDestructive` ("Utilization of each execute type is used to apply agent-level confirmation"). Full flat list at `https://mcp.atlassian.com/v2/mcp?tools=all`.
- Confirmed off by default: "delete_jira is disabled by default. An admin must enable it before you can be utilized." (deleteJiraIssue, deleteJiraComment, deleteJiraIssueAttachment; scope `delete:jira:agent-interface`). "manage_jira is disabled by default. An admin must enable it before you can utilize it." (createJiraProject, updateJiraProject, workflow read/edit-link, getJiraScreen, updateJiraScreen with plan-then-commit). No Confluence delete group exists on the page; Confluence write includes archive/unarchive, move, restore version, but no delete tool.
- Jira write tools (verbatim names): createJiraIssue, editJiraIssue, transitionJiraIssue, addOrEditJiraIssueComment, addOrEditJiraIssueWorklog, createJiraIssueLink, manageJiraProjectVersion, manageJiraProjectVersionRelatedWork, manageJiraSprint, createJiraBoard, watchJiraIssue, uploadAttachmentToJiraIssue, editJiraEntityProperty, createJiraIssueRemoteIssueLink ("a web link on a work item for a Confluence page or external URL"), convertJiraIssueHierarchy.
- Confluence read tools include getConfluenceContent ("page, blog, live doc, comment, whiteboard, embed, database, or folder"), getConfluenceSpace ("configured space instructions"), getConfluenceSpaceInstructions, version diff (diffConfluenceContentVersions), getConfluenceContentPermissions, getConfluenceContentRestrictionState ("OPEN, EDIT_RESTRICTED, or fully restricted"), getConfluencePublicLinkStatus, listConfluenceTemplates/getConfluenceTemplate, getConfluenceMauiApp. Write tools include createConfluenceContent ("page, blog post, live doc, whiteboard, database, embed, smart link, or folder"), updateConfluenceContent, createConfluenceSpace, setConfluenceSpaceInstructions, copy/move/archive/unarchive, restoreConfluenceContentVersion, convertConfluenceContentMode, setConfluenceContentStatus, comments, attachments, labels, add/remove/replaceConfluenceContentPermissions, setConfluenceContentRestrictionState, enable/disableConfluencePublicLink, tasks, stars, watch. (Earlier note's "generated infographics cost 15-30 Rovo credits" was not found in this read; treat as unverified.)
- Atlassian Home: read_goals (searchGoals, getGoal, getGoalUpdate, getGoalTypes), write_goals (createGoal, createGoalUpdate, addConnectionsToGoals), read_projects (searchProjects, getProject, getProjectUpdate), write_projects (createProject "Create an Atlassian project", createProjectUpdate, addConnectionsToProjects), plus read/write_focus (focus areas), read/write_teams, read/write_talent, capacity planning.
- Teamwork Graph group `read_teamwork_graph` (scope `read:all:twg`): getTeamworkGraphContext ("all relationships and linked objects in one traversal"; entry points Jira, Confluence, "Goals, Projects, Focus Areas, tags and updates", People, DevOps, Loom, Compass, incidents/conversations/calendar events/external documents, Assets), getTeamworkGraphObject, getPeopleInfo, getWorkPortfolio ("native and inferred projects, owned goals, and focus areas"), getWorkActivity, getPullRequests. "The vast majority of enriched TWG API and tool calls are 1-10 Rovo credits per call." Third-party data follows Jira permissions under "Limited access" connectors.
- Jira Product Discovery: zero occurrences of "Product Discovery", "JPD" or "idea" on the page. A July 2026 Atlassian blog claims JPD support (see atlassian-blog-mcp-enhancements-jpd.md); the likely path is the generic work-item tools, since JPD ideas are Jira issues. Unconfirmed.
- Closing disclaimer: "MCP clients can perform actions across Atlassian apps with your existing permissions. Use least privilege, review high-impact changes before confirming, and monitor audit logs".
