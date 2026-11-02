---
title: "Navigating the LLM Landscape: Uber's Innovation with GenAI Gateway"
source_url: https://www.uber.com/us/en/blog/genai-gateway/
author: Tse-Chi Wang, Roopansh Bansal (Uber)
publisher: Uber Engineering Blog
published: 2024-07-11
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [cost-control-routing, agent-control-plane, enterprise-admin-controls, harness-portability]
relevance: medium
---

## Relevance to the project
This is the origin of the "model gateway" building block under Cortana: a Michelangelo-built Go service that mirrors the OpenAI API, fronts third-party and self-hosted models, redacts PII before vendor calls, and logs every call for cost attribution and audit. In mid-2024 it served ~30 teams and 16M queries a month; the 2026 talk puts it at 800+ projects and 100M requests a day. It shows Uber chose to own the model access layer two years before the agent harness work.

## Themes
- cost-control-routing: audit logs for cost attribution, security audits and quality evaluation; metrics and alerting (Architecture).
- enterprise-admin-controls: engineering security reviews each use case against Uber's data handling standard before granting access (Access review).
- harness-portability: OpenAI-compatible HTTP/JSON interface so teams use standard clients (LangChain, LlamaIndex) across vendors (Design).
- agent-control-plane: PII redactor swaps sensitive values for numbered placeholders and restores them in the response (PII redactor).

## Key points
- Vendors at the time: OpenAI, Vertex AI (PaLM 2; Uber open-sourced its Go Vertex client, github.com/uber/go-vertex-ai); self-hosted Llama 2.
- Numbers (Jul 2024): 60+ LLM use cases, close to 30 customer teams, 16M queries/month, 25 QPS peak.
- Caching and guardrails not covered in this post (the May 2024 Michelangelo post lists cost and safety guardrails).

## Notable quotes
- "A pivotal design decision was to mirror the HTTP/JSON interface of the OpenAI API."

## Could not verify
- "Spire identity" and "AI Guard" are not in this post; they appear in the 2026 identity post and the talk.
