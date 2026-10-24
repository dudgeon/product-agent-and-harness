---
title: "Agent view in Claude Code"
source_url: https://claude.com/resources/articles/agent-view-in-claude-code
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-11
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-control-plane, shared-persistent-sessions, human-review-gates]
relevance: medium
---

## Relevance to the project
Agent view is a Claude Code CLI screen listing all of a user's sessions with their status (needs input, working, done), last response and last interaction, so one person can dispatch many background agents and step in only when one needs a decision. For the project it is a first-party example of the personal "inbox of agents" interface pattern and of a human-in-the-loop model where the human answers blocked sessions inline. It is a single-user research preview: no sharing, no team view, no governance, and no data on how many concurrent sessions people manage well.

## Themes
- agent-control-plane: one list of sessions with status, last response and last-interaction time; opened by left arrow or `claude agents` ("See everything at once").
- shared-persistent-sessions: sessions can be backgrounded with `/bg` or launched straight to background with `claude --bg [task]`; long-running looping jobs show their next run time ("Background anything"; usage patterns).
- human-review-gates: peek at the last turn and answer a waiting decision inline so the session resumes; dispatch several ideas and return to "a list of pull requests ready for review" ("Peek and reply"; usage patterns).

## Key points
- **Problem named:** parallel agents previously meant terminal tabs, tmux grids and a mental ledger of what needs attention.
- **Row contents:** session, whether it needs input, last response content, last interaction time; status indicators show which produced a PR.
- **Early-user patterns (Anthropic's account):** scale concurrent sessions each optionally paired with a skill; manage long-running jobs (PR babysitters, dashboard updaters); jump to a side task and back; scan what shipped.
- **Availability:** research preview on Pro, Max, Team, Enterprise and Claude API plans; opt in via `claude agents`; normal rate limits apply.
- **Limits:** developer-only CLI surface; nothing on multi-user visibility, cost controls, or failure handling for abandoned sessions.

## Could not verify
- The linked docs page was not read; whether sessions here include cloud/remote sessions is not stated.
