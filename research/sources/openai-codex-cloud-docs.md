---
title: Codex cloud (cloud tasks and environments)
source_url: https://learn.chatgpt.com/docs/cloud
author: OpenAI
publisher: learn.chatgpt.com (formerly developers.openai.com/codex/cloud)
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
OpenAI's equivalent of cloud sessions: publish an environment (install script, network preset, secrets, OIDC connections, who may use it), start tasks from web, mobile, desktop, CLI or Slack, parallel tasks keep separate state. Notably environment access can be restricted to oneself or the whole organisation, a ready-made sharing/governance primitive.

## Themes
- `remote-agent-invocation`: Each task has its own workspace and keeps working while the computer sleeps; CLI can start tasks and list recent cloud chats.
- `shared-persistent-sessions`: Environment permissions: only you or everyone in the organisation.

## Key points
- Network access per environment via preset, package-manager access, extra domains; saving a network secret allows its domains.
- Page does not state usage or concurrency limits or describe sandboxing in detail.
- Simon Willison notes 'Codex cloud' was renamed 'Codex web' on 2025-12-31 (cloud tasks vs the web app).

## Could not verify
- Limits, pricing and GitHub/IDE start paths not documented on the fetched page.
