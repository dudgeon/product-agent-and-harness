---
title: Record for AI agents (Loom)
source_url: https://support.atlassian.com/loom/docs/record-for-agent/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [opportunity-to-code-chain, agent-ready-intent, tacit-knowledge-capture, feedback-triage-agents, harness-portability]
relevance: high
---

## Relevance to the project
This is the first-party documentation of the Loom-to-work-item handoff the Atlassian CPO described in her talk: a screen recording with narration becomes a structured "agent prompt" and, for Atlassian-managed accounts, Jira work items "for agents to act on". It lists exactly what is captured (transcript, keyframes, clicks, URLs, console and network logs) and what the prompt contains. Two related Loom/Jira pages cover bug reports from video and meeting-driven work item updates.

## Themes
- `opportunity-to-code-chain`: "generates a prompt for you to review and share with an agent or automatically create work items in Jira for agents to act on." (intro)
- `agent-ready-intent`: each task in the agent prompt has "A concise title and bulleted instructions", "A transcript quote", "Visual references or keyframes", "Timestamps" (Agent prompt).
- `tacit-knowledge-capture`: captures transcript, keyframes (with Selection tool and Magic pen marks), "Interaction events", "Visited links", and on Chrome "console.log, warn, error, navigation messages, and network request/response metadata" (Data capture).
- `harness-portability`: "Send to agent" opens the preferred agent with the prompt pre-filled, or copies it for CLI tools; example agents "Rovo or Claude".

## Key points
- **Documented:** open beta; Business + AI and Enterprise plans; "the Jira work item creation flow is exclusively available to users with Atlassian-managed accounts with an active Jira subscription"; Chrome extension and desktop app 2.0+; 5-minute limit; camera off.
- **Documented flow:** Generate tab > Record for agent > narrate > Stop > view "Action Plan" > "Create in Jira" (turns "specific actions into work items for agents to act on") or "Open in Jira" from Send to agent.
- **Related page, documented** ([Use AI workflows](https://support.atlassian.com/loom/docs/use-ai-workflows/)): after any recording, Loom AI generates a bug report ("a short description, steps to reproduce, and a link to your video") to "Create in Jira" (first-party: Atlassian-linked account, Business + AI or Enterprise; full custom field support) or Linear; document templates include SOP, Step-by-step guide, PR description, QA steps, Code docs.
- **Related page, documented** ([Get AI-suggested work item updates from Loom meetings in Jira](https://support.atlassian.com/jira-software-cloud/docs/get-ai-suggested-work-item-updates-from-loom-meetings-in-jira/)): connect a Loom meeting to a Jira space before or after recording; "Rovo analyzes the meeting transcript and recommends updates such as reassigning work items, changing priority or status, or adding a comment" (also updating the description); the meeting owner sees a nudge on the board and Accepts or Discards each.
- **Not documented:** creating new stories, epics or JPD ideas from meeting recordings (a public feature request, LOOM-251, asks for it; status not checked). Not documented: the work item's fields when created from Record for agent (whether the action plan goes into the description).

## Could not verify
- Whether the CPO-described flow (Loom recording to work item to In Progress triggering a coding agent) is a configured automation or a product default.
