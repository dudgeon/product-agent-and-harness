---
title: Contextual Policies in Omnigent: Using session state to better govern AI agents
source_url: https://www.databricks.com/blog/contextual-policies-omnigent-using-session-state-better-govern-ai-agents
author: Matei Zaharia, David Nasi, Xiangrui Meng, Kecheng Cao, Tomu Hirata
publisher: Databricks Blog
published: 2026-07-07
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, cost-control-routing]
relevance: high
---

## Relevance to the project
Describes what governance 'above the harness' concretely means: stateful policies that see every tool call and LLM event across any wrapped agent. The clearest published example of a cross-harness control plane, relevant to the governance dimension.

## Themes
- [[meta-harness]]: because Omnigent launches the agents and intercepts their tool calls, one policy set applies to Claude Code, Codex, Antigravity, Pi, OpenCode, Hermes and SDK agents.
- [[cost-control-routing]]: cost policy with a soft threshold (prompt to continue) and a hard cap that blocks the expensive model until the agent switches to a cheaper one; optional per-user daily caps.

## Key points
- A policy receives events (tool calls/responses, LLM inputs/outputs) and can allow, deny, transform or ask; it keeps per-policy per-session state stored by the server.
- Built-in examples: Google Drive write limits with a Bell-LaPadula-style 'no write-down' after reading confidential files; running risk score that escalates to ASK; cost policy; intent-based authorisation that blocks tool calls unrelated to the user's initial request.
- Argument: static allow-lists are too rigid and per-action prompts cause fatigue; safety depends on prior context (e.g. has the agent read untrusted content).
- No limitations section; alpha. Enforcement relies on launching agents through Omnigent.

## Could not verify
- No data on effectiveness or false-positive rates.
