---
title: Microsoft Agent Framework overview
source_url: https://learn.microsoft.com/en-us/agent-framework/overview/
author: Microsoft
publisher: Microsoft Learn
published: 2026-07-29
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-over-model, work-structure-spectrum]
relevance: high
---

## Relevance to the project
Microsoft's consolidated successor to AutoGen and Semantic Kernel. Notably it now ships an opinionated "Harness Agent" (planning, compaction, memory, approvals), showing frameworks absorbing the harness layer. Includes an explicit "if you can write a function, do that" rule.

## Themes
- agent-frameworks: four areas (agents, harness agent, workflows, integrations) plus session state, context providers, middleware, MCP clients.
- harness-over-model: framework vendors shipping a batteries-included harness agent.
- work-structure-spectrum: agent vs workflow decision table.

## Key points
- Combines AutoGen agent abstractions with Semantic Kernel enterprise features and adds graph workflows.
- .NET, Python and Go (Go in public preview at time of docs).
- Docs page dated 2026-07-29 (updated 2026-08-25). Model providers include Foundry, Anthropic, Azure OpenAI, OpenAI, Ollama.
- Decision table: use an agent for open-ended tasks, a workflow for well-defined steps; "If you can write a function to handle the task, do that".
- Disclaimer puts responsibility for third-party systems, data flows and responsible-AI mitigations on the builder.

## Could not verify
- GA date (a third-party source says 1.0 GA on 2026-04-02/03) not confirmed from Microsoft text in this fetch.
