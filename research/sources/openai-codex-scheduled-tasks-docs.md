---
title: "Scheduled tasks (Codex automations docs)"
source_url: https://learn.chatgpt.com/docs/automations?surface=app
author: OpenAI
publisher: OpenAI docs (redirected from developers.openai.com/codex/app/automations)
published: unknown
retrieved: 2026-10-26
type: docs
evidence: first-party
filed_by: research-shared-persistent-agents
themes: [remote-agent-invocation, shared-persistent-sessions, identity-delegation, human-review-gates]
relevance: high
---
## Relevance to the project
OpenAI's current docs for Codex scheduled tasks (formerly "automations") show the overnight-run-and-morning-report pattern (catalogue item 4) as shipped: runs on an RRULE schedule or on Gmail/Slack/GitHub events, results land in a "Scheduled" view that "acts as your inbox", and thread-scoped tasks return to the same chat with its context. Two details matter for the project: desktop tasks need the computer on and the app running (so they are not truly persistent), while "Team Tasks run in the cloud through a team service account", which is the identity model for a task that outlives one person (item 9).

## Themes
- remote-agent-invocation: time schedules (custom cadence or RFC 5545 RRULE) or event triggers from Gmail, Slack or GitHub on web/mobile; the two cannot be combined (Scheduling)
- shared-persistent-sessions: standalone tasks start a new chat each run and report into Scheduled; tasks scheduled inside a chat return to it and keep its context, suited to "check-in loops and ongoing triage" (Thread vs standalone)
- identity-delegation: "Team Tasks run in the cloud through a team service account", in contrast to local tasks running as the user on their machine (Where it runs)
- human-review-gates: "Scheduled tasks run unattended and use your default sandbox settings"; full access can change files, run commands and use the network without asking; docs advise testing prompts in a normal chat and reviewing the first few runs (Sandbox; Warnings)

## Key points
- Desktop: "Keep the computer on and the app running when a scheduled task needs local files." Worktree mode isolates scheduled changes from unfinished local work.
- Frequent schedules create many worktrees; archive runs you don't need.
- Unread indicator flags runs that need attention; event-triggered runs may batch close events.
- The docs say nothing about what a run should do when it has nothing to report.

## Notable quotes
- "The Scheduled view acts as your inbox."
- "Scheduled tasks run unattended and use your default sandbox settings."

## Could not verify
- Page is undated; Team Tasks plan eligibility and the service account's permissions are not detailed.
