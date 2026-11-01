---
title: openai/swarm (README)
source_url: https://github.com/openai/swarm
author: OpenAI
publisher: GitHub
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks]
relevance: medium
---

## Relevance to the project
Swarm is the origin of the "handoff" idea now in the OpenAI Agents SDK and copied by LangGraph and Microsoft: a function returns an Agent and execution moves to it, with the chat history unchanged and only the system prompt swapped. It shows that the original handoff was designed as a single shared transcript with a changing persona, not as a relay of artifacts.

## Themes
- handoff-context-transfer: "If a function returns an `Agent`, execution will be transferred to that `Agent`"; at a handoff "the `system` prompt will change, but the chat history will not".
- agent-frameworks: "Swarm is now replaced by the OpenAI Agents SDK"; experimental and educational.

## Key points
- An Agent is "a set of `instructions` with a set of `functions`".
- `context_variables` is a dict available to functions and instructions; a function can return a `Result` updating them along with the next agent and a value. If several handoff functions are called, only the last applies.
- Stateless between calls (no persistence built in); the caller holds the message list.

## Could not verify
- README undated; repository creation date (October 2024) from memory, not confirmed on the page.
