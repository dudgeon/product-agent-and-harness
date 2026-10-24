---
title: Trace agents with OpenTelemetry on the Claude Platform
source_url: https://claude.com/resources/articles/agent-observability-on-the-claude-platform
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-10-14
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-control-plane, evals-autonomy-trust, harness-portability, org-learning-loop, cost-control-routing]
relevance: medium
---

## Relevance to the project
Anthropic now exports OpenTelemetry traces (every agent turn, model call, tool use and MCP call, with latency, tokens and IDs) from Managed Agents, the Messages API and the Claude SDKs, alongside existing Claude Code and Cowork traces, using the vendor-neutral OTel GenAI conventions. For the project this matters in two ways: it frames autonomy as something earned by reviewing traces before widening access, and it makes the audit and improvement loop portable across observability tools rather than locked to Anthropic's console. Public beta; customer quotes (Ramp, Foxglove, Sterling Labs, an accounting-software infrastructure head) are vendor-curated and their numbers unaudited.

## Themes
- agent-control-plane: one destination in the Claude Console sends traces to the organisation's existing tools; Databricks Unity Gateway named for token usage by team and flagging unusual activity ("Works with your observability tools").
- evals-autonomy-trust: "Review its traces, then widen its access as it proves reliable"; eval tools (Arize, Braintrust, Datadog, Langfuse, LangSmith, New Relic, PostHog) turn real traces into evals ("Trace agents with OpenTelemetry").
- harness-portability: traces follow the OpenTelemetry GenAI semantic conventions, so Claude and other providers' data sit in the same dashboards; any OTLP endpoint works ("Works with your observability tools").
- org-learning-loop: Ramp's Reflect scores Langfuse traces, finds recurring failures and proposes fixes; Ramp claims 10-20% fewer tokens and 30% faster sessions on some agents (customer quote).
- cost-control-routing: tokens per call and per team visible in traces for platform and security teams ("Track usage across your organization").

## Key points
- **Coverage.** Claude Managed Agents, Messages API and Claude SDKs; Claude Code and Cowork traces could already be exported, so built agents and first-party tools can land in one place.
- **Setup.** Managed Agents and the Messages API need a destination configured in the Claude Console; SDKs export automatically. Status: public beta.
- **Three uses named:** debugging next to logs and metrics (Grafana Cloud, Honeycomb, Sentry, Splunk); improving agents from production data; tracking org-wide usage.
- **Audit use (customer claim).** An infrastructure head at an accounting-related company says each model call appears in the same trace as the reconciliation or journal-entry workflow, with prompt version, tool calls, latency and token spend, so they can answer an auditor "from one timeline". Relevant to regulated settings, but a single testimonial.
- **Limits:** short launch post; nothing on trace content redaction, PII in prompts sent to third-party tools, retention, or sampling; no Anthropic-side evidence that trace review actually precedes access changes in practice.

## Notable quotes
- "Trusting an agent with more access starts with tracing its model calls, tool use, and MCP server calls." ("Trace agents with OpenTelemetry")
- "When an auditor asks what an agent did and why, we can answer from one timeline." (customer quote, Ankush Sharma, Head of Infrastructure)

## Could not verify
- The company Ankush Sharma represents (not named in the extracted text).
