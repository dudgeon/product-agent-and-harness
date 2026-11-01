---
title: "Devin in Slack (Devin docs)"
source_url: https://docs.devin.ai/integrations/slack
author: Cognition
publisher: docs.devin.ai
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [identity-delegation, shared-persistent-sessions, human-relay-removed]
relevance: medium
---

## Relevance to the project
Shows how a deployed agent is invoked from a team channel rather than from the person's harness: @Devin in a thread reads the earlier thread as context, replies and asks questions in-thread, and syncs with the web session. Each person must link their Slack profile to a Devin account with a matching email, so invocations are tied to a named user. For the two modules this is the "not everyone lives in a coding harness" path: a PM or owner can start and steer an agent from Slack.

## Themes
- identity-delegation: "Every user in your organization needs to complete this step once to use Devin from Slack"; Slack email must match the Devin account email; the page does not say which account a session runs under or whose ACUs it uses.
- shared-persistent-sessions: synced session: webapp messages appear in the thread and thread replies reach Devin; controls `mute`, `unmute`, `(aside)`, `sleep`, `unsync`.
- human-relay-removed: tagging Devin inside an existing bug discussion brings the thread's context in without restating it.

## Key points
- Attachments on the tagging message can be included; a code channel created from a message Devin was not part of carries only that message.
- Only explicit approval gate on the page: environment configuration changes show a diff and an Apply button.
- Emoji reactions mark runs completed or failed.

## Could not verify
- Interactive Planning was not documented on the pages read (the "work with Devin" page has no section on it); billing attribution.
