---
title: Agent 365 Lifecycle Atlas (Microsoft FastTrack copilot-agent-strategy)
source_url: https://microsoft.github.io/FastTrack/copilot-agent-strategy/agent-365-lifecycle-atlas/index.html
author: Microsoft FastTrack
publisher: microsoft.github.io
published: 2026-09-16
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, identity-delegation, harness-portability, meta-harness]
relevance: high
---

## Relevance to the project
Microsoft's own deployment guidance says plainly what the "control plane" does and does not do: it governs but does not host or run agents, and telemetry is visibility, not enforcement. It documents how a Claude Agent SDK agent would be onboarded (SDK + CLI creates an Entra blueprint and agent identity while the runtime stays where it is) and that Anthropic Claude Managed Agents is a preview registry-sync connector. This is the most precise evidence found that a big-vendor "agent control plane" can wrap a Claude-based agent we build, but only as governance metadata plus identity, not as a harness layer.

## Themes
- agent-control-plane: "Agent 365 governs; it does not host or run agents"; registration creates metadata and identity references, does not grant permissions or host code.
- identity-delegation: each agent gets a tenant-local Entra identity; a blueprint is the shared credential boundary for child identities; blueprint permissions need admin consent; Azure RBAC per agent identity; disabling identity blocks sign-in but does not delete compute or registry record.
- harness-portability: custom agents on Claude Agent SDK, LangChain, CrewAI etc. onboard via the Agent 365 SDK and `a365` CLI; the runtime stays put.
- meta-harness: explicitly not one; it does not launch or wrap harnesses.

## Key points
- Six-stage lifecycle: build/acquire, connect, identity, capabilities and package, deploy and runtime (hosted by you, Azure or the platform), govern and operate. Stages are largely independent operations.
- Connected-platform registry sync (preview, "status contested across public docs"): Amazon Bedrock, Google Vertex AI, Anthropic Claude Managed Agents listed; imports metadata only, no identity or telemetry wiring.
- Local coding agents (e.g. OpenClaw, Ollama) are not registered; Defender "Shadow AI" (preview) detects unmanaged agents on managed devices.
- Defender: activity views, hunting. Purview: DLP, audit, retention, eDiscovery for governed agents. Runs without a valid root `invoke_agent` span are invisible in Defender and Purview views (i.e. audit depends on instrumentation).
- GA: Agent 365 (2026-05-01), core identity/telemetry, package and catalog governance. Preview/beta: registry sync, Shadow AI, Agent Registration API, MCP Management, agent user accounts.

## Notable quotes
- "Agent 365 governs; it does not host or run agents, and no single action cascades across the others."
- "Telemetry is visibility, not enforcement."

## Could not verify
- Page shows "accuracy reviewed 2026-09-16" (used as published date). A vendor blog (egroup-us, vantaige) claims Agent 365 offers "local agent governance" for Claude Code and Copilot CLI; this atlas does not say so (only Shadow AI detection). Treat that claim as unverified.
