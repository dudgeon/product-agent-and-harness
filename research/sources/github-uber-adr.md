---
title: "ADR: Agentic AI Detection and Response (uber/ADR)"
source_url: https://github.com/uber/ADR
author: Uber (paper: Chenning Li, Pan Hu, et al.)
publisher: GitHub (uber); paper on arXiv 2605.17380, MLSys 2026
published: 2026-04-19
retrieved: 2026-11-02
type: docs
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [agent-protocol-security, enterprise-admin-controls, agent-control-plane, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
Uber open-sourced ADR, the security layer that watches the commercial coding agents its engineers run (Claude Code, Cursor, Codex, Copilot CLI and others): endpoint discovery of AI tools and MCP servers, a sensor that normalises agent session telemetry, a two-tier detector, and a 300-task benchmark. It is the "AI Detection and Response" piece of Uber's agent stack and the only relevant Uber open-source release found. It bears on how a company governs harnesses it does not own, alongside the gateways it does.

## Themes
- agent-protocol-security: ADR-Bench, 302-304 tasks, 133-134 MCP servers, all 17 agent attack techniques; detector reports zero false positives and 67% attack detection on ADR-Bench (README, arXiv abstract).
- enterprise-admin-controls: ADR Discovery inventories installed AI apps, CLI agents, IDE extensions, local model runtimes and MCP servers, flagging unknown ones (README).
- agent-control-plane: ADR Sensor captures agent intent, tool use and execution traces across 7+ coding tools on macOS, Linux and Windows, plus internal automation and support agents (README).
- policy-enforcement-fail-open: prevention ("stop unsafe actions") is not in the open-source release; detection is two-tier, cheap triage then agentic reasoning on suspicious sessions (README).

## Key points
- Uber deployment (arXiv abstract, May 2026): 10+ months in production, 7,200+ hosts, 10,000+ agent sessions a day, hundreds of credential exposures found across 26 categories; shift-left prevention at 97.2% precision with 206 credentials detected.
- Apache-2.0; repo created 2026-04-19; ~2,100 stars at retrieval. Offline red-teaming engine (ADR Explorer) not released.
- Other github.com/uber items touching this stack: go-vertex-ai (GenAI Gateway's Vertex client); no MCP gateway, skills or Cortana code released.

## Could not verify
- Whether ADR telemetry covers Cortana or Minion sessions, or only third-party harnesses on endpoints; not stated.
