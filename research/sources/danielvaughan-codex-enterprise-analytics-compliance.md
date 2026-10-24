---
title: "Codex Enterprise Analytics and Compliance APIs: Usage Dashboards, Code Review Metrics, and Audit Integration"
source_url: https://codex.danielvaughan.com/2026/05/11/codex-enterprise-analytics-compliance-apis-governance-dashboards/
author: Daniel Vaughan
publisher: codex.danielvaughan.com
published: 2026-05-11
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, cost-control-routing]
relevance: medium
---

## Relevance to the project
An independent practitioner (already cited in this project for the DIY meta-harness pattern) who writes a running series on Codex enterprise deployment (managed configuration, RBAC, access tokens, compliance). This post (updated 2026-10-24) fills in what OpenAI's own pages defer to API references: Analytics API endpoints, the 30-day Compliance window, and the API-key audit gap. Treat details as secondary until checked against the API reference.

## Themes
- enterprise-admin-controls (proposed): "The Compliance API covers ChatGPT-authenticated Codex usage only"; API-key usage "follows your organisation's separate API data settings", outside this audit trail. "Activity logs are retained for 30 days", "non-negotiable on the platform side", so plan your own archival.
- cost-control-routing: Analytics API usage endpoint "Returns threads, turns, credits, and per-client breakdowns"; code-review endpoints for PR review throughput and engagement; lookback up to 90 days; dashboard can lag up to 12 hours.

## Key points
- Claims the legacy stateful Compliance route was deprecated 2026-03-05 for removal 2026-06-05 (unconfirmed elsewhere).
- Mentions "13 pre-built Compliance API integrations" without naming them; Elastic's integration (v0.2.0, preview) lists a `codex_log` stream with prompts, responses, MCP/tool call arguments and results, plugin metadata, environment (variable names only) and access-token fields (https://www.elastic.co/docs/reference/integrations/openai_chatgpt_enterprise, read in part, not filed separately).

## Could not verify
- Endpoint paths and schemas; the deprecation dates; whether Codex cloud tasks follow Enterprise retention rather than ZDR (asserted in another Vaughan post seen only in search).
