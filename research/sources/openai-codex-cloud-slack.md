---
title: "Codex cloud and the Slack integration (OpenAI docs)"
source_url: https://learn.chatgpt.com/docs/third-party/slack
author: OpenAI
publisher: OpenAI docs (learn.chatgpt.com)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, remote-agent-invocation, harness-portability]
relevance: medium
---
## Relevance to the project
OpenAI's counterpart to Claude Tag and Cursor Slack agents, with a third answer to identity: the task runs under the requester's account, follow-ups continue only if the same account sends them, and results posted to a channel are readable by the whole channel. Together with the cloud docs, it shows cloud tasks with environments, parallel tasks and mobile/web continuation.

## Themes
- shared-persistent-sessions: repository work 'runs as a separate task under the requester's account'; a different account may start a new task instead of continuing; sharing an environment does not grant repo access or share credential values
- shared-persistent-sessions: approval requests go to the requester as a private card, but the response 'can be read by people with access to that channel'; following the channel reply does not give access to the task
- remote-agent-invocation: Codex cloud tasks run in published environments, in parallel, 'while your computer is asleep'; internet access and secrets configured per environment (cloud docs, learn.chatgpt.com/docs/cloud.md)

## Key points
- Requirements: admin sets up Slack deployment; Cloud delegation enabled; a published environment shared with the workspace. Slack Connect channels unsupported; personal environments do not appear.
- Cloud docs page did not describe container implementation, sharing, usage limits or handoff to local.

## Could not verify
- Cloud docs page: sharing, limits and local handoff not covered in what was retrieved.
