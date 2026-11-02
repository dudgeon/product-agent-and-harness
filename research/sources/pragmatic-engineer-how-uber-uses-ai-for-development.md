---
title: "How Uber uses AI for development: inside look"
source_url: https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development
author: Gergely Orosz
publisher: The Pragmatic Engineer
published: 2026-03-10
retrieved: 2026-11-02
type: article
evidence: independent
filed_by: competitive-teardown-uber-cortana
themes: [agent-factory-sdlc, harness-portability, agent-control-plane, non-engineer-builders, cost-control-routing, vendor-claims-vs-independent-evidence, leadership-permission-mandate]
relevance: medium
---

## Relevance to the project
An independent write-up of Uber's Pragmatic Summit session (principal engineer Ty Smith and engineering director Anshu Chada), useful as the March 2026 snapshot of the stack Cortana later sat on: four layers (internal AI platform on Michelangelo, internal context as agent "memory", industry agents such as Claude Code and Codex, and specialised agents), plus an MCP gateway, a no-code Uber Agent Builder with Agent Studio and an agent registry, and the AIFX CLI. Cortana is not named in the readable part, which fits the podcast's account that it started as one engineer's assistant in December 2025 and grew later. It also gives dated adoption figures that sit before the August 2026 talk. Bears on harness-layering, capability-packaging and adoption.

## Themes
- agent-factory-sdlc: four layers: internal AI platform, internal Uber context (code, docs, Slack, Jira as memory), industry agents, specialised agents (background agents, test generation, code review), plus engineering enablement (section 1).
- harness-portability: the AIFX CLI provisions clients (Claude Code, Codex, Cursor and others), finds MCP servers, runs background agent tasks and updates clients (section 2).
- agent-control-plane: MCP gateway proxies internal Thrift, Protobuf or HTTP endpoints as MCP servers by configuration, fronts third-party MCPs, and centralises authorisation, telemetry and logging, with a registry and sandbox (section 2).
- non-engineer-builders: Uber Agent Builder is "a no-code solution to build agents" over MCP servers and Uber datasets that can hand off to other agents; Agent Studio visualises, debugs, traces, versions and evaluates multi-agent workflows; built agents are discoverable, usable and copyable in a registry (section 2).
- cost-control-routing: AI-related costs "up 6x since 2024"; token cost optimisation a growing priority (contents summary).
- vendor-claims-vs-independent-evidence: March 2026 numbers from Uber: 84% of devs agentic coding users; 65-72% of code AI-generated inside IDE tools; Claude Code usage from 32% (Dec) to 63% (Feb); 92% use agents monthly; 11% of PRs opened by agents (update note and contents summary).
- leadership-permission-mandate: "Top-down mandates are less efficient than engineers sharing their wins with peers"; adoption "slower than expected" (contents summary).

## Key points
- Company strategy explicitly includes becoming "GenAI-powered"; dev platform focus is toil (upgrades, migrations, trivial fixes) so engineers do creative work (intro).
- Workflows moved from single-threaded IDE coding to orchestrating several parallel background agents, which creates resource and cost pressure (section 3).
- Paywalled sections (not read): Minion at scale, Code Inbox, uReview, Autocover (5,000+ unit tests a month), Shepherd for migrations, challenges, impact numbers.

## Could not verify
- Sections 4 onward are behind the paid tier and were not read; figures above come from the free header and contents summary.
- Cortana is not mentioned in the free part; whether Agent Builder agents and Cortana personas share infrastructure is unknown.
