---
title: LangGraph overview
source_url: https://docs.langchain.com/oss/python/langgraph/overview
author: LangChain Inc.
publisher: LangChain docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks]
relevance: medium
---

## Relevance to the project
LangGraph is the low-level durable-execution runtime of the LangChain family; it deliberately does not abstract prompts or agent architecture. Useful for the option "workflow engine with embedded agents" and for deterministic parts of a hybrid.

## Themes
- agent-frameworks: durable execution, human-in-the-loop, memory, streaming; deployment and tracing are via paid LangSmith.

## Key points
- Durable execution, resume after failure, inspect/modify state, short- and long-term memory.
- Mixed deterministic and LLM steps in one graph.
- Does not abstract prompts or architecture; does not require LangChain.
- Names Klarna, Uber, J.P. Morgan as users (vendor claim).

## Could not verify
- No version on page.
