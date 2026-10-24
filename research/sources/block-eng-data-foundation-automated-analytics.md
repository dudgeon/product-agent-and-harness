---
title: Building the Data Foundation for Automated Analytics
source_url: https://engineering.block.xyz/blog/building-the-data-foundation-for-automated-analytics
author: Alyssa Ransbury, Andrew Kuttig, Phil Azar, Zach Stanford (Block)
publisher: Block Engineering Blog
published: 2026-04-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [metrics-review-agents, org-context-grounding, pm-tool-connectivity, evals-autonomy-trust, ai-synthesis-hallucination-risk]
relevance: high
---

## Relevance to the project
How Block made agent analytics trustworthy: split data access into two MCP servers, Block Data MCP (1,100+ governed metrics, pre-approved SQL the LLM cannot see or edit) and Query Expert MCP (RAG-backed exploratory SQL for technical users). Either can be used from the same agent session. This is the strongest first-party evidence on how a metrics-review capability for PMs and business users should be packaged: governed semantic layer first, agent second, with evals to 100% on priority questions.

## Themes
- metrics-review-agents: 100% accuracy on Finance Copilot questions where a governed metric existed; 87% less analyst time in blind tests (40 Finance questions, 7.6 h to under 1 h) (results).
- org-context-grounding: metric definitions as code in GitHub with business and technical owners and CODEOWNERS review; governance tiers Certified / Verified / Preliminary; eight data-mesh domains incl. Product (governance).
- pm-tool-connectivity: tools for metric search, details, filtered fetch, dashboard discovery, permission checks, feedback; both servers share Snowflake RBAC (architecture).
- evals-autonomy-trust: eval tests per priority question iterated to 100%; controlled manual vs AI experiments; an MCP evaluation framework (evaluation).
- ai-synthesis-hallucination-risk: the opening problem was "plausible but untrustworthy numbers" from inconsistent metric definitions.

## Key points
- Query Expert grew from 700 to 2.1K monthly users (Sept 2025 to Mar 2026), over a third of the company; Q1 2026 quarterly uniques: Block Data MCP 1,812, Query Expert 1,899.
- Query Expert indexes ~10K highly used tables (of 100K+) and vetted queries; 400M+ queries run monthly at Block.
- Built by a seven-person tiger team in six weeks; an eight-step Data Domain AI Playbook scales it per domain.
- The agent is unnamed ("the AI agent", an internal AI platform); also mentions a Glean MCP and the Snowflake MCP.

## Could not verify
- Which agent(s) host these servers (goose implied but not stated); whether PMs are a named user group.
