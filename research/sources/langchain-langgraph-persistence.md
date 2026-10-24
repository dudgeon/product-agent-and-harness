---
title: "LangGraph persistence (checkpointers, threads, stores)"
source_url: https://docs.langchain.com/oss/python/langgraph/persistence
author: LangChain
publisher: LangChain docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, memory-architecture, shared-persistent-sessions]
relevance: medium
---
## Relevance to the project
Primary doc for framework-level session persistence: thread-scoped checkpoints for resume and human-in-the-loop, and cross-thread stores for shared memory. This is the in-process, library option versus a workflow engine or a platform session log. Notes checkpoint growth as a practical problem.

## Themes
- memory-architecture: checkpointers keep thread-scoped state keyed by thread_id; stores hold cross-thread data (preferences, facts); a parent graph may not see subgraph state immediately because of checkpoint namespaces
- shared-persistent-sessions: InMemory saver is for dev only; production uses Postgres/Sqlite savers; Agent Server handles persistence automatically; checkpoints accumulate over long conversations and need pruning

## Key points
- Pages read did not cover time travel, replay, or encryption in detail.

## Could not verify
- Time-travel/replay and encryption not covered by retrieved text.
