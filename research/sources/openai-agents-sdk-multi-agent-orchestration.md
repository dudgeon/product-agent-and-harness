---
title: Agent orchestration (OpenAI Agents SDK, multi-agent page)
source_url: https://openai.github.io/openai-agents-python/multi_agent/
author: OpenAI
publisher: OpenAI Agents SDK docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [work-structure-spectrum, deterministic-scaffold-model-nodes, agent-frameworks]
relevance: high
---

## Relevance to the project
OpenAI's own framing of the control-flow dimension: "orchestrating via LLM" versus "orchestrating via code", with named code patterns (route on a structured-output category, chain, evaluator loop, parallel). The chain example is a writing pipeline (research, outline, draft, critique, revise), close to a PRD workflow. It also distinguishes two model-chosen handover styles (agents as tools, handoffs) that differ in who owns the user conversation.

## Themes
- work-structure-spectrum: LLM orchestration when "given an open-ended task, the LLM can autonomously plan"; code orchestration "makes tasks more deterministic and predictable, in terms of speed, cost and performance".
- deterministic-scaffold-model-nodes: code patterns: structured output then code picks the next agent; chaining research → outline → draft → critique → revise; "while loop with evaluator" that stops when criteria pass; `asyncio.gather` for parallel agents.

## Key points
- Agents as tools: a manager keeps the conversation; the specialist "should help with a bounded subtask but should not take over the user-facing conversation."
- Handoffs: a triage agent routes and "that specialist becomes the active agent for the rest of the turn." The two can be combined.
- The page treats the two orchestration modes as mixable, not exclusive.

## Could not verify
- Page undated; no measurement of when code orchestration outperforms LLM orchestration.
