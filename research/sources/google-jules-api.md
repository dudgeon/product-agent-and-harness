---
title: Jules REST API reference overview
source_url: https://jules.google/docs/api/reference/overview/
author: Google
publisher: jules.google
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation]
relevance: low
---

## Relevance to the project
Google's background coding agent exposes a v1alpha REST API (sessions, activities, sources) with an API key, so other tools can start and monitor Jules sessions. Alpha status and community-written MCP wrappers (not Google-supported) show immaturity as a callable agent.

## Themes
- `remote-agent-invocation`: Sessions are units of work; activities (plan generated, message, completion) are monitored by polling; auth via x-goog-api-key.

## Key points
- Base URL is `v1alpha`; quotas not stated beyond HTTP 429.
- Search found only unofficial MCP servers wrapping Jules.

## Could not verify
- Plan-approval mechanics not described on the fetched page.
