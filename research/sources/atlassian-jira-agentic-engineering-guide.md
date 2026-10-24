---
title: Using Jira for agentic engineering
source_url: https://www.atlassian.com/software/jira/guides/agentic-engineering/overview
author: Finch Grace (Atlassian)
publisher: atlassian.com Jira guide
published: 2026-08-06
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: user-story-mapping
themes: [agent-factory-sdlc, opportunity-to-code-chain, human-review-gates, agent-control-plane, agent-ready-intent, human-judgment-pm-jobs]
relevance: high
---

## Relevance to the project
Atlassian's own lifecycle model for agent work: plan, orchestrate, review, scale. It is explicit about which step stays human ("Set the goal (people decide what and why; Jira turns it into a plan)"), and it names the handoff mechanisms: assignment, workflow transition, board column, automation rule, and a review status that blocks "done". This is the vendor's view of the map the project is building, so it is the baseline to compare against.

## Themes
- `agent-factory-sdlc`: "Jira supports agent work across four stages: plan, orchestrate, review, and scale." (Where Jira fits)
- `opportunity-to-code-chain`: "Requests arrive from everywhere: a Slack thread, a Confluence page, a Loom recording, a meeting. Mention @Jira or use Rovo to turn them into work items in place." (Plan)
- `agent-ready-intent`: "the spec is the anchor input: the agent works on the work item from the spec, not from a one-off prompt"; Jira Planner drafts the spec and you "add acceptance criteria, so the spec becomes what the agent builds from and is reviewed against." (Plan)
- `agent-control-plane`: "Trigger an agent from an automation rule or a workflow transition (or add an agent to a board column) so it picks up work automatically as status changes." (Orchestrate)
- `human-review-gates`: output "can't transition to done until someone approves it"; CI status "surfaces on the work item so a review step can hold the transition to done." (Review)
- `human-judgment-pm-jobs`: table row "Planning ... What Jira does not do: Set the goal (people decide what and why; Jira turns it into a plan)."

## Key points
- **Claimed (FAQ):** "Agents draw context from the work item itself (requirements and acceptance criteria) and from the Teamwork Graph, which connects related work, docs, and code."
- **Claimed:** "Assign a work item to Claude, Cursor, Codex, GitHub Copilot, or the native Jira Coding Agent, then see the actions it took and the decisions it made across web, IDE, and terminal sessions."
- **Claimed:** "As an agent works, its activity and the pull request it opens stays linked to the work item."
- **Claimed:** "Iterate. ... results feed back into the next spec, and work re-enters the lifecycle." No mechanism is described.
- **Claimed:** Getting started: pick a routine task, capture it as a work item, assign to Jira Coding Agent from the Agents panel, review the PR, then automate.
- **Corroborates the CPO talk:** the "workflow transition" trigger matches the Lenny-talk description of moving a work item to In Progress to start a cloud coding agent ([transcript](lenny-podcast-tamar-yehoshua-roles-expanding.transcript.md)).
- Linked sub-guides (spec-driven development, context engineering, human-in-the-loop, guardrails) did not return content when fetched.

## Could not verify
- Sub-guide pages; "16% of their time writing code" figure source.
