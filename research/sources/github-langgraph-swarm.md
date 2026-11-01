---
title: langgraph-swarm-py (README)
source_url: https://github.com/langchain-ai/langgraph-swarm-py
author: LangChain
publisher: GitHub
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
The swarm pattern is the purest control-transfer design: agents hand off to each other, one shared `messages` key carries the whole conversation, and the system remembers which agent was last active so the next user turn resumes with it. That needs a checkpointer, which makes the active agent part of persisted session state.

## Themes
- handoff-context-transfer: agents "communicate over a single `messages` key that is shared by all agents"; `create_handoff_tool` "passes full message history" and adds a tool message confirming the transfer.
- shared-persistent-sessions: without a checkpointer the swarm "forget[s]" which agent was last active; compile with `checkpointer=` for multi-turn use; long-term memory via a store.
- agent-frameworks: custom handoff tools can change name, description, arguments and what state is passed.

## Could not verify
- Maintenance status (not marked archived at retrieval).
