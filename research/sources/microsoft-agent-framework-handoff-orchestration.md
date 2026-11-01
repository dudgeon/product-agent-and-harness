---
title: Microsoft Agent Framework Workflows Orchestrations - Handoff
source_url: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff
author: Microsoft (Tao Chen)
publisher: Microsoft Learn
published: 2026-10-15
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, human-review-gates, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
The most explicit first-party contrast between handoff and agent-as-tools on three axes (control flow, task ownership, context management), and a precise account of what is synchronised: agents do not share a session; each broadcasts user and agent messages to all participants, while tool calls (including handoff calls) are filtered out. It also shows durable pause for approvals "hours or days later" via checkpointing, which matters for long-lived dependency asks.

## Themes
- handoff-context-transfer: "the agent receiving the handoff takes full ownership of the task. In agent-as-tools, the primary agent retains overall responsibility"; "the conversation is handed off to another agent entirely. The receiving agent has full context"; "Tool related contents, including handoff tool calls, are not broadcasted to other agents. Only user and agent messages are synchronized" (Context Synchronization).
- agent-frameworks: mesh topology "without an orchestrator"; handoff rules only govern who can take over next; `enable_return_to_previous` controls whether a user reply goes back to the agent that asked or to the start agent.
- human-review-gates: handoff is "inherently interactive": if an agent answers without handing off, the workflow returns to the user; approval-required tools pause with a `RequestInfoEvent`.
- shared-persistent-sessions: `checkpoint_storage` lets a workflow pause for an approval and resume after a process restart; stable agent IDs are needed to rehydrate.

## Key points
- Autonomous mode (experimental in Python) auto-replies "User did not respond. Continue assisting autonomously." up to 50 turns per agent by default.
- Python keeps user text, files and URIs across synchronisation; non-user messages keep text only.
- Orchestration overview page (https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/, dated 2026-02-12) lists sequential, concurrent, handoff, group chat and Magentic; all support human-in-the-loop via tool approval and request-info.

## Could not verify
- Production usage; Go support "coming soon".
