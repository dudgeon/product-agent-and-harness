---
title: API keys (Cursor docs)
source_url: https://cursor.com/docs/settings/api-keys
author: Cursor (Anysphere)
publisher: cursor.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, cost-control-routing]
relevance: medium
---

## Relevance to the project
Defines Cursor's BYOK limits: own keys cover chat models only, Tab stays on Cursor's models, Cursor's ZDR does not apply to own-key traffic, and Teams/Enterprise pay a Cursor token fee even on own keys. So Cursor is model-agnostic but not provider-independent: Cursor stays in the data path and the billing path.

## Themes
- harness-portability: providers for own keys: OpenAI, Anthropic, Google, Azure OpenAI, AWS Bedrock (IAM roles configurable in the dashboard).
- cost-control-routing: Teams/Enterprise "Eligible third-party model requests carry the Cursor Token Rate of $0.25 per million tokens", including own-key requests.

## Key points
- "Custom API keys only work with chat models. Tab completion continues using Cursor's built-in models."
- "Cursor's Zero Data Retention policy does not apply when you use your own API keys."
- Cloud agents not mentioned on this page.
