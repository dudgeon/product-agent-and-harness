---
title: Omnigent on Databricks (AWS docs)
source_url: https://docs.databricks.com/aws/en/omnigent/
author: Databricks
publisher: Databricks documentation
published: 2026-09-28
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, build-vs-buy, cost-control-routing]
relevance: high
---

## Relevance to the project
Confirms Databricks ships Omnigent as a product: a Databricks-operated Omnigent server, in Beta, tied to workspace identity, Unity Gateway model access and Databricks Sandboxes. For a regulated buyer this is the "managed" variant of the meta-harness option, with narrower policy expressiveness (built-in plus CEL, no custom Python) and model access only through Databricks. The page is last updated 2026-09-28.

## Themes
- [[meta-harness]]: "Omnigent is in Beta"; "A Databricks-operated Omnigent server that integrates with your workspace's identity provider"; described as a common layer over "Claude Code, Codex, Cursor, Pi, and the agents you write yourself".
- [[build-vs-buy]]: managed server and sandboxes remove ops but bind model access to Foundation Model APIs and Unity Gateway; "You cannot bring your own model API keys for a Databricks Sandbox host."
- [[cost-control-routing]]: policies are "built-in contextual policies" and "custom policies" in CEL; "Custom Python policies are not supported."

## Key points
- Requires a workspace region that supports Unity Gateway; Databricks Sandbox only in "select regions on AWS"; Sandbox preview must be enabled; "Do not use Databricks Sandbox in a workspace with serverless egress control (SEG) enabled."
- The Omnigent preview must be enabled per workspace.
- No mention on this page of audit logs, system tables, MLflow tracing, SCIM, pricing, or Claude/ChatGPT subscriptions. (Search summaries of the Agent Bricks product page say contextual policies are enforced through Unity AI Gateway and sessions traced in MLflow; not verified on a fetched page.)
- Native Windows not supported (per search summary of the same docs).

## Could not verify
- Whether managed Omnigent is formally part of Agent Bricks; no fetched Databricks page says so.
- Pricing and GA timeline.
- Azure/GCP availability.
