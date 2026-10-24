---
title: Introducing Omnigent: A Meta-Harness to Combine, Control and Share Your Agents
source_url: https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents
author: Matei Zaharia, Kasey Uhlenhuth, Corey Zumar
publisher: Databricks Blog
published: 2026-06-13
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-portability, shared-persistent-sessions, cost-control-routing]
relevance: high
---

## Relevance to the project
The canonical statement of the 'meta-harness' idea and the main reference product for pattern class C. It names the three things a layer above harnesses adds: composition, control, collaboration. Directly relevant to making work less dependent on Claude Code and to moving sessions from private/ephemeral to shared.

## Themes
- [[meta-harness]]: defines it as a layer 'above the agents you already use' giving Claude Code, Codex, Pi and SDK agents one session API (section 'How Omnigent works').
- [[harness-portability]]: a custom agent is defined in YAML and ported across harnesses with a one-line change; sub-agents from different harnesses can be combined.
- [[shared-persistent-sessions]]: live sessions shared by URL, files commented, agents steered in real time; web, mobile, macOS app and API clients.
- [[cost-control-routing]]: stateful cost policies pause an agent at thresholds (e.g. every $100); policies live in the meta-harness, not in prompts.

## Key points
- Published 2026-06-13 (the plan listed the date as unknown). Apache 2.0, alpha. Authors include Databricks' Matei Zaharia.
- Problem statement: the authors run four or five agents at once and copy text between them; each harness hides its LLM logic behind a different interface, so swapping or combining is hard.
- Interface insight: whatever an agent does inside, the outside is the same: messages and files in, text streams and tool calls out. A common API wraps terminal agents (Claude Code, Codex, Pi) and SDKs (OpenAI Agents, Claude Agents SDK).
- Features: real-time collaboration, multiple interfaces, local or hosted sandbox execution (Modal, Daytona), contextual security policies (e.g. human approval for git push after an npm download), cost policies, an OS sandbox from Databricks' security team with credential injection at an egress proxy, multi-harness authoring.
- Roadmap: GEPA-based automatic meta-harness optimisation, an Omnigent Server MCP so agents can work across sessions, more harness integrations.
- Analogy to Kubernetes/Terraform: each harness today is a silo with its own context, controls and run model; nothing carries across tools.
- All claims are the vendor's. No adoption numbers in the post.

## Notable quotes
- "a meta-harness that sits above the agents you already use" (intro)

## Could not verify
- The full text could only be read through a summarising fetch, not verbatim.
