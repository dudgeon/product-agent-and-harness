---
title: Cline repository
source_url: https://github.com/cline/cline
author: Cline Bot Inc.
publisher: GitHub
published: unknown
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability]
relevance: low
---

## Relevance to the project
Apache-2.0 coding agent now offered as an SDK (@cline/sdk), CLI, IDE extensions and desktop app, with plugin hooks for policy and audit, cron-scheduled agents and Slack/Telegram connections. A usable base for an org-governed harness, with plan/act approval gating by default.

## Themes
- agent-frameworks: shared SDK powering CLI, desktop, VS Code and JetBrains; custom tools and hooks for logging, auditing, policy.

## Key points
- About 70.8k stars; Plan mode then Act mode with per-action approval unless auto-approve.
- Headless CLI with JSON output for CI; multi-agent teams, scheduled agents.
- Wide provider support including Bedrock, Vertex, Ollama, any OpenAI-compatible API.

## Could not verify
- JetBrains plugin is not open source; enterprise feature set not described on the page. Fork lineage claims (Roo Code archived May 2026; Kilo Code) come from Kilo's own comparison page and were not filed.

## Follow-up (2026-10-24)
Filed by research-runtime-patterns-follow-up-round.
- Enterprise detail now filed in [cline-docs-enterprise-remote-configuration](cline-docs-enterprise-remote-configuration.md) (SSO via WorkOS, hosted remote config, prompt storage to own S3/R2, OTel; enforcement mostly limited to VS Code and JetBrains).
- **Supplier signal (search summaries, not read first-hand):** in January 2026 The Information reported that OpenAI hired at least seven Cline staff for Codex; an OpenAI spokesperson confirmed the hires and said it was not an acquisition (via techleap.nl and texxr.com summaries). CB Insights lists a 2026-01-29 "reverse acqui-hire" with OpenAI participating; unconfirmed elsewhere. Earlier funding: about $32M over three rounds, Series A July 2025 (CB Insights summary).
- **Roo Code (Cline fork):** Roo Code sunset its VS Code extension, Cloud and Router on 2026-05-15, pointing users to Cline and to Roomote (its cloud-agent successor) (Distill Intelligence directory entry; codepick.dev and standardcompute.com summaries). Community fork "Zoo Code" reportedly maintains the extension. Kilo Code (another Cline-lineage fork) continues. Roo was hit by the Anthropic subscription block in January 2026 ([falcao](falcao-anthropic-claude-access-crackdown.md)).
- Independent rating: Thoughtworks Trial, April 2025, no longer on the current radar ([note](thoughtworks-radar-cline.md)).
