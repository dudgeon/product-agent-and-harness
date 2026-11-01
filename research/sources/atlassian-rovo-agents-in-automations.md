---
title: "Automating Rovo agents (Atlassian support)"
source_url: https://support.atlassian.com/rovo/docs/agents-in-automations
author: Atlassian
publisher: Atlassian Support
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [event-triggered-agents, prd-agents, human-review-gates, spec-edge-case-review]
relevance: high
---

## Relevance to the project
The one documented example found of a document reviewer agent that wakes on a spec-type artifact: a Confluence automation fires when a page with "DACI" in the title is published, a Rovo agent reviews it, and a second rule step posts the agent's output as a page comment. It shows the shape of a reviewer for intent artifacts (trigger on publish, comment, no block) and its limits: the agent cannot itself act, its output has to be piped into a later action, and blocking is something admins apply to the agent, not something the agent applies to the document.

## Themes
- event-triggered-agents: agents start from a trigger in their own configuration or from an automation flow; examples are Confluence "Page published", Jira "Work item created" and "Scheduled"; "Anyone with Studio access can create an automation flow."
- prd-agents / spec-edge-case-review: "The automation flow is triggered when new Confluence pages are published with "DACI" in the title"; the Decision director agent should "review the page and leave a comment suggesting improvements" (prompt: "Review the content on this page and give recommendations").
- human-review-gates: out-of-the-box agents "don't take actions"; output flows through `{{agentResponse}}` into "Add comment to page", "Add comment to work item" or "Send Slack message"; "Admins and users can prevent agents from acting in automations", in which case write tools fail.

## Key points
- Identity: an example caption says "The agent is set up with a users permissions"; the rule-actor model is in a separate page not read.
- A community answer (anecdote) says Studio automation supports Jira, JSM, Focus, Loom and Assets triggers but not Confluence page events, so Confluence-triggered agents go through Confluence automation; another reports an empty payload when a custom-action agent is triggered from automation (https://community.developer.atlassian.com/t/use-a-custom-rovo-agent-triggered-from-confluence-automation/98354).
- Pairs with [atlassian-rovo-dev-acceptance-criteria-code-review](atlassian-rovo-dev-acceptance-criteria-code-review.md) (code reviewed against Jira acceptance criteria) and [atlassian-jira-manage-agents-in-space](atlassian-jira-manage-agents-in-space.md) (agent's account vs user's account).

## Could not verify
- Full list of Jira and Confluence triggers (e.g. work item transitioned); audit logging of agent runs. Page undated; read via WebFetch (model-summarised view).
