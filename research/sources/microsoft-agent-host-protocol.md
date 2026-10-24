---
title: Agent Host Protocol (microsoft/agent-host-protocol README)
source_url: https://github.com/microsoft/agent-host-protocol
author: Microsoft (VS Code team)
publisher: GitHub
published: 2026-03-12
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [shared-persistent-sessions, harness-portability, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
What VS Code (and so GitHub Copilot's editor surface) is building on instead of A2A: a protocol for a standalone sessions server that several clients connect to with a synchronised view of agent sessions. A VS Code team member said on HN (2026-06-18) that they are "rebuilding our agent infrastructure on top of" it. It is a session/host protocol (closer to Track 5's shared sessions and Zed's Agent Client Protocol) rather than agent-to-agent delegation, so it is evidence that the IDE side is standardising on host protocols, not A2A.

## Themes
- `shared-persistent-sessions`: "A synchronized, multi-client state protocol for AI agent sessions": immutable state, pure reducers, write-ahead reconciliation; multiple clients see the same sessions.
- `harness-portability`: Hosts include the VS Code agent host (reference server), pi-ahp (pi coding agent), hydra-ahp and an AHP-ACP gateway that runs ACP agents; clients include VS Code's Agent Sessions view, CLIs and a WeChat bridge. SDKs in Rust, TypeScript, Kotlin, Go, Swift, .NET with a `MultiHostClient`.
- `remote-agent-invocation`: No A2A in the repo (code search returned one incidental hit); the route from VS Code to remote agents is hosts speaking AHP, not A2A.

## Key points
- Repo created 2026-03-12; 413 stars; active (pushed 2026-10-23).

## Could not verify
- The AHP documentation site was not read; whether GitHub Copilot cloud agent or Copilot CLI use AHP. A separate GitHub issue (github/copilot-sdk #2270, 2026-08-05, open) requests "Support for A2A communication with Foundry Agents", which suggests the Copilot SDK has no A2A client yet.
