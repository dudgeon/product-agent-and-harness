---
title: How Notion ships and scales agents with Claude Managed Agents
source_url: https://claude.com/customers/notion-qa
author: Anthropic (Q&A with Eric Liu, Product Manager, Notion)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [shared-persistent-sessions, human-review-gates, org-learning-loop, scoped-governance-containers, one-job-per-agent]
relevance: medium
---

## Relevance to the project
Notion's PM describes a task board as the agent orchestrator: moving a card to "ready to start" opens a Claude Managed Agents session that reads linked pages, the design system, API docs and PRDs, with results routed to named people for approval, which is a concrete multiplayer pattern for PM work rather than one-person-one-agent chat. It also shows per-stage agents (investigate, plan, build) each with its own permissions, private-by-default sharing with chat/trigger/edit roles, and skills that the agent updates itself from merged PRs and thumbs-up feedback. That bears on the session-persistence-sharing, agent-interface, governance-control-plane and harness-upkeep dimensions. All numbers are Notion's claims on an Anthropic page, unaudited.

## Themes
- shared-persistent-sessions: "you create a task, move it to 'ready to start,' and it invokes a Claude session"; teammates are tagged into the same output and "jammed on the same output together right in Notion" (Q&A, "How would you explain..." and "You've been using this yourself").
- human-review-gates: platform "routes them to the right person for approvals"; users give thumbs up/down on agent work in the task; Liu's forecast is humans as "reviewers of agentic work rather than directly the doers" (Q&A, last answer).
- one-job-per-agent: "a Claude agent for each stage: one that investigates, one that plans, and one that builds", each with own permissions, context and automations (Q&A, "army of agents").
- scoped-governance-containers: every agent starts private and must be shared explicitly, with chat-only, trigger and edit permission levels; the review agent is managed by a few people, the investigator by many (same answer).
- org-learning-loop: skills are "basically auto-maintained": after a merged PR or completed task Claude extracts lessons into the skills database; positive feedback also feeds skills (Q&A, skills answer; case study "The outcome").

## Key points
- **Usage claims (Q&A header and first answer).** About 18,000 Claude agents created in the first three weeks of "External Agents", about 140,000 steps; 90% of turns triggered by automations (a Notion page, a Slack message, a schedule), not chat. Top workspaces run three or four agents with dozens of threads a day.
- **Integration choice.** Managed Agents offered three modes per the interviewer: Claude-branded in product, unbranded engine, or internal agents. Notion chose Claude-branded because users trust the model; the session streams from Managed Agents into Notion's client.
- **What Managed Agents supplied.** Long-running tasks, memory management, preinstalled skills and packages, a sandbox, and a GitHub endpoint so users can pull repos and run code. Liu: Notion's own agent "is not the best at coding"; Claude covers code and the "long tail of artifacts" (slides, PDFs, websites).
- **Concurrency.** 30-40 jobs launched at once from the board; Liu's anecdote of dragging about 30 prototype tasks to start and returning to finished prototypes; "12 hours of prototyping work collapse into about 20 minutes" (single anecdote).
- **PM-shaped flow (case study).** A PM's meeting note is transcribed into action items and Claude writes the code; for non-technical teams, client decks and sample sites.
- **Skills.** Public Anthropic skills (PowerPoint, PDF, docs) are preloaded; Notion runs its own skills marketplace and lets users bring their own; skills encode "our flavor of PowerPoint" rather than capability.
- **Collaboration thesis.** Scaling agents is a collaboration problem; suggested edits, version history and shared knowledge bases carry over from human collaboration; next six months: more version control and human-in-the-loop on the page/database primitives.
- **Older Claude claims (case study).** Prompt caching cut cost 90% and latency up to 85%; Osaka Gas 35% less search time; Remote about 10 minutes saved per search; dbt Labs over $35k a year saved. These are earlier Notion AI search figures, not agent results.
- **Limits.** No quality, error or rollback data for agent output; the self-updating skills loop is described without any review step, so there is no account of how bad lessons are caught; "very little marketing" adoption claim is unverified.

## Companion pages
- https://claude.com/customers/notion (case study "Notion builds agent orchestration where teams and Claude collaborate on real work"): adds the 30+ concurrent tasks and prompt-caching figures, model selection quotes from Simon Last (co-founder) and Sarah Sachs (AI Lead Engineer), and the meeting-note-to-code flow.

## Notable quotes
- "The interface is becoming more about human beings reviewing the work of agents." (Eric Liu, Q&A)
- "Every agent that you create is locked down from a permission standpoint by default." (Eric Liu, Q&A)

## Could not verify
- Publication dates of both pages (not shown).
- How the 18,000 agents and 90% automation share are counted (created vs active).
