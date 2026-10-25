---
title: Agentic Workflows Explained - an in-depth but simple guide for Product Teams
source_url: https://departmentofproduct.substack.com/p/agentic-workflows-explained-an-in
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-09-15
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [agent-frameworks, work-structure-spectrum, agent-failure-modes, agent-project-failure-rates, memory-architecture, human-review-gates]
relevance: medium
---

## Relevance to the project
A PM primer on the anatomy of an agentic workflow in seven numbered parts (input, planning and orchestration, tools and tool registry, memory, controls and guardrails, execution, output), using LangChain/LangGraph as the reference framework and Replit Agent 3 as the worked example. It adds little new evidence, but its plain deterministic-vs-non-deterministic framing and seven-part anatomy are a ready vocabulary for the strategy and the explainer film. Its one evidential claim is a cited benchmark where agents failed about half of 34 general tasks, with failures sorted into planning, execution and formatting errors. Triage guessed high; it is medium because it is an introductory explainer and the company facts are second-hand.

## Themes
- work-structure-spectrum: an automated workflow is deterministic (same outcome each run); an agentic one is non-deterministic, varying with input, tools, decisions and error handling; the author calls this the best first mental model ("basic anatomy").
- agent-frameworks: LangChain as the dominant orchestration framework by GitHub stars; LangGraph models workflows as directed graphs with checkpoints, memory, moderation and human-in-the-loop controls; a tools list (Vellum, PromptFlow, Kore.ai, AutoGen, CrewAI, Databricks Unity Catalog, Bedrock Guardrails). See [LangGraph overview](langchain-docs-langgraph-overview.md).
- agent-project-failure-rates: cites a "Cibench" study where agents failed about 50% of 34 programmable tasks (data analysis, web crawling, file operations) ("How reliable are agentic workflows?").
- agent-failure-modes: the study's three failure classes: planning errors (illogical decomposition, not adapting to feedback), execution mistakes (faulty code, tool misuse, environment setup), and response formatting (lost context, wrong format, exceeding allowed rounds).
- memory-architecture: short-term (current conversation, files, retrieved docs, generated artifacts) vs long-term (across conversations and workflows), per LangChain's documentation.
- human-review-gates: guardrails listed as content moderation, policy restrictions, human-in-the-loop for sensitive or ambiguous actions, and sandboxed, tool-only access; evals check the guardrails hold.

## Key points
- **Seven parts:** (1) input (user query or API call); (2) planning and orchestration, decomposing a goal into sequenced sub-tasks; (3) tools from a registry the engineer defines, with fallback to another registered tool on error; (4) memory; (5) controls and guardrails; (6) execution layer that checks inputs, logs every action for audit, and loops on outcomes; (7) output, sometimes offered to the user to accept or reject.
- **Replit Agent 3:** about 200-minute runtime (ten times its predecessor); tests itself by driving a browser preview the user can watch, then fixes issues (second-hand from Replit).
- **Other examples:** Cursor 2.0 and its Composer model; Cursor acquiring Graphite (code review); AWS AgentCore monitoring features and three domain agents, including Kiro Autonomous Agent that takes a backlog item and returns a reviewable PR.
- **Reliability:** SWE-bench top scores around 74-75% for coding; general agentic tasks far worse.

## Notable quotes
- "The tools registry is essentially like a catalog of all of the available tools" (section 3)

## Could not verify
- The post is dated 2025-09-15 but mentions Cursor 2.0, the Graphite acquisition and AWS re:Invent announcements from later in 2025, so it was updated after publication; the date shown is the original.
- The "Cibench" study was not identified or checked; the name may be misreported.
- LangChain's valuation and LinkedIn's use of LangSmith are relayed press claims.
- Paywalled text summarised, not reproduced.
