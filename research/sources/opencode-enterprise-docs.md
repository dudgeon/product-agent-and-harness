---
title: OpenCode Enterprise (docs)
source_url: https://opencode.ai/docs/enterprise/
author: OpenCode (Anomaly)
publisher: opencode.ai
published: 2026-10-23 (page "Last updated")
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [build-vs-buy, harness-portability, cost-control-routing]
relevance: high
---

## Relevance to the project
The enterprise story for the most-starred open harness. Its control model is "central config plus SSO that forces all traffic through your own AI gateway"; it stores no code or context itself. That is attractive for a regulated setting (data stays on the machine and in the org's gateway), but the page has no audit-log feature, share pages must be disabled because self-hosting them is only on the roadmap, and audit would have to come from the org's gateway. Bears on loop-source (fork or adopt an open harness) and governance-control-plane (gateway as the control point).

## Themes
- build-vs-buy: open-source core can be trialled internally before buying seats; "You own all code produced by OpenCode."
- harness-portability: provider-agnostic; config can disable all other providers so requests go only through an internal gateway.
- cost-control-routing: "if you have your own LLM gateway, we do not charge for tokens used"; per-seat pricing by quote.

## Key points
- "OpenCode does not store any of your code or context data"; "All processing happens locally or through direct API calls to your AI provider."
- Central config: "This centralized config can integrate with your SSO provider and ensures all users access only your internal AI gateway."
- Private npm registries (Artifactory, Nexus) via Bun's .npmrc support.
- Share pages: recommended to disable; self-hosted share pages are "on the roadmap".
- Not on the page: audit logs, ZDR as a term, SCIM, admin policy over tools/permissions/MCP beyond config.

## Could not verify
- Price per seat; named enterprise customers; whether central config can lock permissions, MCP servers and plugins (a third-party radar says defaults are permissive; see rubinlake-radar-opencode).
