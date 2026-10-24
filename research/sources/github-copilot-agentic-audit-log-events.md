---
title: Audit log events for agents (GitHub Copilot docs) and Reviewing audit logs for Copilot
source_url: https://docs.github.com/en/copilot/reference/agentic-audit-log-events
author: GitHub
publisher: GitHub Docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, identity-delegation, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
Defines what a regulated org can evidence about agent actions on GitHub: each agent event carries `actor_is_agent`, the initiating `user` and an `agent_session_id`, retained 180 days and streamable to a SIEM. The companion page (https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs) states the main gap: local client prompts are not in the audit log. This is the best documented agent-attribution schema among the three vendors and a template for our own audit design.

## Themes
- identity-delegation: fields `action` (e.g. `pull_request.create`), `actor_is_agent` ("always `true` for agentic audit log events"), `agent_session_id` ("only appears when the event is the result of an agent session"), `user` (the person who initiated the agentic event).
- enterprise-admin-controls (proposed): filter `actor:Copilot` for 180 days of agentic activity; enterprise owners only; streaming to a SIEM recommended for longer retention.
- shared-persistent-sessions: the session id links code changes to the session log, supporting the "audit trail that links code to the session that wrote it" key question.

## Key points
- Streamed Copilot API usage records (public preview; EMU or GHE Cloud with data residency) carry request/response `body` (truncated at 1 MB), `user_id`, `enterprise_id`, `endpoint` and timestamps: prompt-level content capture exists only in that preview stream.
- Review-audit-logs page: "The audit log retains events for the last 180 days." "The audit log does not include client session data, such as the prompts a user sends to Copilot locally." Suggested workaround: custom hooks sending Copilot CLI events to your own logging.
- Search snippets (not in the fetched text) mention an `agent_session.task` event for session start/finish/fail; not confirmed.

## Could not verify
- A full list of agentic event types; whether partner-agent (Claude, Codex) actions carry the same fields (the third-party agents page says only that partner app actions are recorded in the audit log). Model-summarised fetch; pages undated.
