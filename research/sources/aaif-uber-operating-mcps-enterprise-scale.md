---
title: "Keynote: Operating MCPs at Enterprise Scale: Uber's Journey (How Uber Runs 60,000 AI Agent Tasks Per Week With MCP)"
source_url: https://www.youtube.com/watch?v=yVqMxBahjfA
author: Meghana Somasundara (Agentic AI Lead) and Rush Tehrani (Head of Engineering, Agentic AI Platform), Uber
publisher: Agentic AI Foundation (YouTube; MCP Dev Summit North America 2026)
published: 2026-05-07
retrieved: 2026-11-02
type: video
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [agent-control-plane, pm-tool-connectivity, agent-legible-platform, non-engineer-builders, skills-marketplace, skill-improvement-loops, evals-autonomy-trust, agent-protocol-security]
relevance: high
---

## Relevance to the project
Uber's own account of the MCP layer under Cortana and of its no-code Uber Agent Builder, which already had "thousands" of monthly active internal agents in April 2026, before Cortana personas were announced. It shows how tool exposure is owned (service owners curate LLM-generated tool descriptions through a reviewed diff), how a no-code agent is scoped to specific tools with fixed parameters, and that skill evals and A/B tests were still roadmap. Bears on whether a PM-facing agent should build on a tool gateway with owner-curated tools, and on the overlap between Agent Builder agents and Cortana personas.

## Themes
- agent-control-plane: MCP Gateway and Registry is "the control plane for all MCP interactions at Uber"; central authorization, PII Redactor, diff-time and periodic code scanning, blocking of mutable endpoints that could bring down critical services (03:30-05:30).
- agent-legible-platform: an orchestrator crawls 10,000+ proto/thrift IDLs, has an LLM write tool descriptions from message names and comments, stores them in object storage; owners choose which tools are exposed and edit descriptions via a scanned diff (05:30-07:10).
- non-engineer-builders: thousands of non-engineers trying agentic workflows; Uber Agent Builder is a no-code tool for internal productivity and team workflow agents, "thousands" active monthly (00:30, 07:20-07:50).
- pm-tool-connectivity: three consumption surfaces for the same MCPs: Agent Builder (no-code), Uber Agent SDK (code-first, with managed memory, chat history and orchestration), coding agents via the AIFX CLI `mcp add` (07:20-11:10).
- skills-marketplace: skills are "recipes for using these MCPs"; aim to share them across teams (13:00).
- skill-improvement-loops: roadmap to evaluate skill output quality, invocation correctness, and A/B test skill versions (13:20-14:00).
- evals-autonomy-trust: plan to show eval results and service SLAs in the registry to tier MCPs; a tool-search tool to cut context bloat (11:50-12:50).
- agent-protocol-security: third-party MCPs get more gating and scanning than internal ones; one-off playground environments were deprecated in favour of code-managed config (03:50-04:20).

## Key points
- Scale (00:30-01:20): 5,000+ engineers, 90%+ using AI monthly for agentic workflows; 10,000+ services; 1,500+ monthly active internal agents; 60,000+ executions per week.
- Problems: no standard way to develop and deploy MCP servers, duplicated bespoke integrations, need to see "who was accessing what data", agent blast radius larger than human, third-party data handling, discovery and quality.
- Agent Builder specifics (09:10-10:40): an MCP is scoped by @-mentioning the server inside the agent's system instructions; builders can pick specific tools so the model does not choose; parameter overrides fix values so the model does not supply them. The SDK does the same through a YAML config.
- SDK use cases in production: grocery assistant, care coordination agent, customer support agent.
- Minion: background agent "built on" the Claude harness, ~1,800 code changes a week; coding agents used by 95% of engineers (08:40-09:05).

## Notable quotes
- "Service owners, which are basically the experts, still stay in control of which tools actually get exposed." (Somasundara, 03:50)
- "You can think of them as recipes for using these MCPs." (Tehrani on skills, 13:05)

## Could not verify
- Cortana is not mentioned; nor is a context graph. Whether Cortana personas are built on Agent Builder (both bind a prompt and selected tools/skills to a team use) is not stated in any source found.
- Keynote was delivered 2026-04-02; the video upload date is 2026-05-07. Auto-captions ("cloud" for Claude, "AIFXC" for AIFX CLI).
