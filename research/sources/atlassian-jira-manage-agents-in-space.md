---
title: View and manage agents in your Jira space
source_url: https://support.atlassian.com/jira-software-cloud/docs/view-and-manage-agents-in-your-jira-space/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [agent-control-plane, identity-delegation, scoped-governance-containers, org-context-grounding, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
A Jira space now holds agents as members, with a role, space-level instructions, triggers and linked "sources" (Confluence pages, Loom recordings). This is the documented way context is attached to an agent per team container, which is the pattern a PM harness needs for per-project agent configuration. It also documents two identity modes (agent's own account vs the triggering user's) and the first field-level autonomy control.

## Themes
- `agent-control-plane`: one Agents page lists "out-of-the-box agents created by Atlassian, custom Rovo agents created in Studio, and third-party agents"; an agent appears "when it can be assigned in Jira or is configured in an automation."
- `identity-delegation`: "Agent's account" (needs a space role in private or limited spaces) vs "User's account" ("will inherit the same permissions as the user") (Agent access).
- `scoped-governance-containers`: agents are added with a Space role; "In private spaces, agents will only have access when they've been added with a role."
- `org-context-grounding`: per-space Prompt (instructions) and Sources ("such as Confluence pages or Loom recordings, so the agent has the right information when it works") (Update agent settings).
- `evals-autonomy-trust`: field-level autonomy (priority, assignee, labels, status, components) "only available for the Jira Triage Agent" so far (Set agent autonomy).

## Key points
- **Documented:** the side panel shows description and access level, triggers (workflows, Jira automations, Studio automations), space-level instructions, and linked context. Only Jira admins or space admins can add agents or edit them.
- **Documented:** "App settings" tab exists "for supported third-party agents" (space-level config provided by the app).
- **Related page** ([Use the agentic engineering template](https://support.atlassian.com/jira-software-cloud/docs/use-the-agentic-engineering-template-to-integrate-coding-agents-in-your-workflow/)): a space template "complete with a workflow optimized for agents like Jira Coding Agent, Claude Code, and GitHub Copilot for Jira", with sample data and onboarding tasks; needs Rovo enabled. Example: "bug fixes and improvements are automatically assigned to a coding agent." Statuses and workflow steps are not listed on the page.
- **Not stated:** whether the "Sources" attached here are passed to third-party coding agents, or only to Rovo agents.

## Could not verify
- Page date; which third-party agents support App settings.
