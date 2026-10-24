---
title: "Cursor Cloud Agent sessions are shared across users - act on behalf (forum bug report)"
source_url: https://forum.cursor.com/t/cursor-cloud-agent-sessions-are-shared-across-users-act-on-behalf/158866
author: DSV (user); reply from Cursor staff
publisher: Cursor community forum
published: 2026-04-23
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, human-review-gates]
relevance: high
---
## Relevance to the project
A rare primary record of a permission-leakage design question in a shared agent product: with Team Followups on, any teammate can prompt an agent that runs with the creator's OAuth tokens. Cursor staff replied it is documented, intentional behaviour. Directly relevant to identity/on-behalf-of design and audit trails. The report is one user's claim plus a staff reply, not a confirmed exploit.

## Themes
- shared-persistent-sessions: the reporter claims a session runs with the initiating user's OAuth identity for Jira, GitHub and Slack while its prompt surface is not bound to that user; follow-ups via Slack thread or the shared web URL run as the initiator
- human-review-gates: reporter says the originating Slack prompt can be deleted, removing the audit trail while side effects remain (claim; staff reply did not address it)

## Key points
- Cursor staff reply 2026-04-24: 'documented and intentional behavior of the Team Followups feature'; mitigation is setting Team Followups to Disabled (creator-only) or Service accounts only; per-prompt re-authorisation framed as a feature request. Thread closed as intended behaviour.
- A related forum thread reports inconsistent follow-up behaviour ('this cloud agent doesn't belong to you' even with team follow-ups on).

## Could not verify
- The 'Open in Web' URL vector and deleted-prompt audit claim were not confirmed or refuted by Cursor.
