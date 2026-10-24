---
title: Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents - A Source-Code Study of Eleven Systems
source_url: https://arxiv.org/abs/2609.00006
author: Paul Barbaste, Tristan Darrigol, Germain Vu, Tom Wiltberger
publisher: arXiv (cs.SE)
published: 2026-07-15
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability, meta-harness, build-vs-buy, skill-standards]
relevance: high
---

## Relevance to the project
The only independent systematic study found: source-level audit of 11 coding harnesses (Claude Code, Codex CLI, Gemini CLI, Mistral Vibe, OpenHands, Aider, Mini-SWE-Agent, Hermes, Pi, OpenCode, OpenClaw) plus Omnigent as a meta-harness. Provides the seven-subsystem definition of a harness used in our track report, the finding that none of them uses a general agentic framework, and 18 design recommendations. Scope is coding harnesses; applicability to knowledge-work or durable multi-user agents is untested.

## Themes
- agent-frameworks: 0 of 11 production harnesses import LangChain, LangGraph, AutoGen, CrewAI, ADK, Pydantic AI, Semantic Kernel etc.; recommendation 15 says do not use them for the agent runtime; the harness SDKs are now the framework layer.
- build-vs-buy: Mini-SWE-Agent 50-line linear loop self-reports 74%+ SWE-Bench Verified; "begin with just a bash tool"; Codex is a 126-crate million-line Rust workspace (cost range).
- skill-standards: SKILL.md adopted by 9 of 11 vs MCP 8 of 11; ACP in six systems as harness hosting.
- meta-harness: Omnigent analysed as the first meta-harness; harnesses became importable SDKs while framework vendors shipped harnesses ("platform turn").
- harness-portability: provider coupling vs agnosticism trade-off; per-provider conditioning layer is the cost of portability.

## Key points
- Seven subsystems: agent loop, LLM integration, tools and actions, memory and context, safety and permissions, orchestration, extensibility; plus interface layer and session substrate as cross-cutting surfaces.
- 13 cross-cutting observations, 29 recurring patterns; about four million lines audited; longitudinal re-audit after one quarter suggests convergence is becoming imitation.
- Loop sophistication does not predict benchmark performance; production systems invest in scaffolding for safety, reliability and workflow integration rather than task completion.
- Thesis: in H1 2026 the coding harness moved from tool to platform; the competitive unit is the ecosystem surface (marketplaces, governance), not the loop.
- Anti-patterns: no vector retrieval for code (0/11), no 1-to-1 API-wrapping tools, do not over-engineer stuck detection; provides a 90-line minimum viable harness.

## Could not verify
- Read from arXiv HTML text extracted locally; PDF not machine-read. Benchmark figures in the paper are self-reported by projects. Authors are not identified with an institution in the text read. Paper says it neither benchmarks nor ranks.
