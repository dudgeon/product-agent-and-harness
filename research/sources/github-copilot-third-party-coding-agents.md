---
title: About third-party coding agents (GitHub Copilot docs)
source_url: https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents
author: GitHub
publisher: GitHub Docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, identity-delegation, enterprise-admin-controls, meta-harness]
relevance: high
---

## Relevance to the project
Claude (on the Claude Agent SDK) and Codex (on the Codex SDK) run as asynchronous agents on GitHub under GitHub's policies, security mitigations and billing. This makes GitHub a de facto multi-vendor host for coding agents: one place to enable, audit and pay for several vendors' loops, which is one realistic shape of a "layer above harnesses" for the engineering handoff at the end of the intent-shaping workflow. It also shows what the host does not say: data handling by Anthropic/OpenAI is not described.

## Themes
- harness-portability / meta-harness: "Coding agents are subject to the same security protections, mitigations, and limitations as Copilot cloud agent"; CodeQL, secret scanning and dependency checks run without GitHub Advanced Security.
- identity-delegation: partner agents run as GitHub Apps (`anthropic code agent`, `openai code agent`); their actions appear in the audit log but the apps do not appear in the account's list of installations.
- enterprise-admin-controls (proposed): Business/Enterprise use org or enterprise policy; policies "don't apply to local agents in VS Code".

## Key points
- Public preview. Entry points: Agents tab, issue assignment, `@AGENT_NAME` in PR comments, GitHub Mobile, VS Code.
- Billing: consumes GitHub Actions minutes and AI credits; "you can use agents without incurring additional costs" within included minutes and credits.
- Models listed: Claude (Auto, Sonnet 4.6, Sonnet 5, Opus 4.8, Opus 5, Fable 5.1) and Codex (Auto, GPT-5.3-Codex, GPT-5.4 nano); partner Auto does not use Copilot's auto selection.
- Search-snippet context (changelog, not fetched): enabling for Business/Enterprise needs enterprise AI Controls > Agents > Partner Agents plus org-level enablement; Claude and Codex became available to Business and Pro on 2026-02-26.

## Could not verify
- Data retention or terms applying to prompts sent to Anthropic/OpenAI via GitHub; commit attribution for partner agents; MCP and custom-instruction support. Undated page; model-summarised fetch.
