---
title: How to build an AI Agent
source_url: https://departmentofproduct.substack.com/p/how-to-build-an-ai-agent
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-01-14
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [agent-frameworks, build-vs-buy, evals-autonomy-trust, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
A January 2025 primer for product teams: what an agent is, a perception-cognition-action model, three ways to build one (framework, from scratch, no-code/SaaS) and company examples. Its three-way build choice is an early, simpler version of the project's loop-source dimension; it predates the "use a vendor harness and extend it" option that most filed sources now describe, which shows how fast that menu changed. One example is a clean goal loop: Uber's AutoCover is said to generate, run and fix unit tests until a coverage target is reached. Company facts are second-hand from vendor case studies and press.

## Themes
- agent-frameworks: LangChain (contributors doubled to 4,000, products built quadrupled to 132,000, per LangChain) and Microsoft AutoGen (Magentic-One roles: orchestrator, web surfer, file surfer, coder, terminal). AutoGen was later archived ([archive notice](github-microsoft-autogen-archive-notice.md)).
- build-vs-buy: framework vs from scratch (most control, needs ML and engineering depth) vs no-code/SaaS (quick but "probably isn't your best bet" for production) ("How agents are built").
- evals-autonomy-trust: three autonomy levels: predefined tasks under strict supervision, conditional autonomy with human escalation, and full independence ("What are AI agents?").
- vendor-claims-vs-independent-evidence: OpenTable on Salesforce Agentforce (reservation changes, loyalty questions, inquiry triage) is a vendor case; see [Agentforce adoption](salesforceben-agentforce-adoption.md) for an independent view.

## Key points
- Agent defined as a program acting with some autonomy toward set goals; "bots with LLMs, RAG and ML".
- Cognition includes memory and RAG; action covers tasks, API calls and multi-round interactions.
- eBay: an in-house framework that routes tasks to several LLMs (WSJ interview, second-hand).
- Uber: vision-based agents for end-to-end app testing; AutoCover loops prepare mocks, generate tests, build and run, fix failures, until coverage is met.
- No-code tools listed: Chatbase, Beam, CrewAI, Agentforce, Copilot agents.

## Could not verify
- None of the case studies were opened; the diagrams were images not in the text copy.
- Paywalled; summarised, not reproduced.
