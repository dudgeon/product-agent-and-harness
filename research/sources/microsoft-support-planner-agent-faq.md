---
title: "Frequently asked questions about Planner Agent"
source_url: https://support.microsoft.com/en-us/planner/copilot/frequently-asked-questions-about-planner-agent
author: Microsoft
publisher: Microsoft Support
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [status-update-agents, human-review-gates, product-artifact-primitives]
relevance: medium
---
## Relevance to the project
Microsoft's Planner Agent (renamed from Project Manager agent in March 2026) generates tasks from a goal (premium plans), can be assigned a task and returns its output in a Loop component, and writes status reports covering completed, ongoing, upcoming, overdue items and notable changes. The FAQ does not mention dependencies between tasks at all: Microsoft's mass-market planning agent is a task executor and reporter, not a dependency manager.

## Themes
- status-update-agents: configurable status reports (date range, sections, length), "created as a Loop component".
- human-review-gates: feedback in the Loop component or comments, then Regenerate; thumbs up/down; it "may not always be able to successfully complete the task" and then gives instructions for a human.
- product-artifact-primitives: the agent is an assignee on Planner tasks; output lives in Loop components inside the plan.

## Key points
- Requires a Microsoft 365 Copilot licence; task generation needs premium Planner; Hebrew and Arabic not supported.
- No dependency, sequencing or cross-plan behaviour described.
