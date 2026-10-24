---
title: Link an idea to a Jira work item (Jira Product Discovery)
source_url: https://support.atlassian.com/jira-product-discovery/docs/link-an-idea-to-a-jira-issue/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [opportunity-to-code-chain, product-artifact-primitives, agent-ready-intent]
relevance: high
---

## Relevance to the project
This is the documented handoff from "spot the opportunity / shape the intent" (a JPD idea) to "plan the change" (Jira epics or tasks). One option, "Embed the idea description and fields into the work item", is the only documented way idea content lands inside the work item that a coding agent then reads. Without it, the idea stays a link, and whether an agent follows that link is undocumented.

## Themes
- `opportunity-to-code-chain`: "When an idea is prioritized in Jira Product Discovery, you can seamlessly link it to delivery work planned and executed in Jira. ... creating or linking Epics or Tasks directly from the idea's delivery tab."
- `agent-ready-intent`: "(Optional) Check Embed the idea description and fields into the work item." (Create a work item)
- `product-artifact-primitives`: linked work items show a Delivery progress bar on the idea; "see the linked ideas inside the Jira work items."

## Key points
- **Documented:** needs JPD creator or admin plus Jira permissions; works across Cloud sites; Premium can link to Jira Data Center via application links.
- **Documented:** the linked delivery table can show up to 10 fields (Type, Key, Status, Story points, Assignee, Due date, Sprint, Fix version, Team, Time tracking).
- **Inference, not documented:** a Jira Coding Agent or Claude Agent for Jira working on that work item would see embedded idea content because it reads the description; nothing documents agents traversing the idea link itself. The July 2026 launch post says the Teamwork Graph includes "customer insights from Jira Product Discovery" ([note](atlassian-blog-jira-ai-native-software-development.md)).
- See the existing [JPD ideas note](atlassian-jira-product-discovery-ideas.md) for the idea object.

## Could not verify
- Whether embedding is a one-time copy or stays in sync.
