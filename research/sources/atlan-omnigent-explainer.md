---
title: What is Databricks Omnigent? The meta-harness explained
source_url: https://atlan.com/know/ai-agent/databricks/what-is-databricks-omnigent-meta-harness/
author: Kovid Rathee (Nexifi)
publisher: Atlan
published: 2026-10-06
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-portability]
relevance: medium
---

## Relevance to the project
Secondary write-up that adds maturity and architecture detail (alpha OSS, Beta on Databricks, harness support tiers, Postgres/OIDC server). It is written by a vendor that sells a context layer, so treat the 'lock-in moves to context' framing as positioning, but the maturity advice is useful.

## Themes
- [[meta-harness]]: Omnigent decomposed as YAML agent definition, stateful policies (allow/ask/deny per session, agent, server), shared server with OIDC/SSO and MCP proxy, two execution modes (Direct vs Native TUI).
- [[harness-portability]]: support is tiered: Claude Code, Codex and OpenAI Agents SDK fully supported; others maintained or community-supported.

## Key points
- Recommends a pilot, not a platform standard. On Databricks, models route through Unity Gateway and custom policies use CEL (no custom Python).
- Argues the layer does not supply business context (definitions, lineage, ownership), so lock-in migrates to wherever context lives.
- Contains no Databricks adoption figures. Atlan sells a competing/adjacent context product, so bias is stated by the source itself.

## Could not verify
- Claims about tiers and the Databricks beta were not cross-checked against Databricks docs.
