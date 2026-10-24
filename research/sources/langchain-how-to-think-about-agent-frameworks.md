---
title: How to think about agent frameworks
source_url: https://www.langchain.com/blog/how-to-think-about-agent-frameworks
author: Harrison Chase (LangChain)
publisher: LangChain blog
published: 2025-04-20
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, agent-frameworks, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Reframes workflow-vs-agent as a *spectrum* ("how agentic") because nearly all production systems mix both. This undercuts a clean two-class split of user activity and supports a hybrid runtime pattern. A framework vendor with a stake (LangGraph).

## Themes
- work-structure-spectrum: moving toward agency lowers predictability, which matters for trust and regulation; reliability depends on giving the LLM the right context at each step, which workflows make controllable.
- agent-frameworks: workflow frameworks have a high floor/high ceiling; agent frameworks low floor/low ceiling; LangGraph pitches both low floor and high ceiling.

## Key points
- Agents in the simplest form are "a model called in a loop with tools". Even agent systems benefit from memory, human-in-the-loop, streaming, fault tolerance, observability.
- Multi-agent systems often work best when workflows govern how agents communicate.
- Main target of the post is OpenAI's guide (called misguided); Anthropic's is praised as more precise.

## Could not verify
- No data supports the reliability claims; they are argument.
