---
title: omnigent-ai/omnigent (README, docs site and open issues)
source_url: https://github.com/omnigent-ai/omnigent
author: Databricks AI team, Neon and contributors
publisher: GitHub / omnigent.ai
published: 2026-10-24
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-portability, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
The code and docs behind the Omnigent claim, plus the live issue tracker, which is the nearest thing to independent evidence on how it behaves. Shows a broad harness list, a runner/server split, many sandbox providers, and real alpha-stage reliability and sharing-security issues.

## Themes
- [[meta-harness]]: README tagline 'The open-source meta-harness for all your AI agents'; runner wraps an agent in a uniform session, server adds policies and shared history.
- [[harness-portability]]: harnesses listed: Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, Antigravity, GitHub Copilot, Devin, Kiro, Grok Build, Goose, OpenClaw, plus custom YAML agents (README + docs).
- [[shared-persistent-sessions]]: live sharing, `omnigent attach` co-driving, `run --fork`; issue #11413 (2026-10-23, P1) says session sharing does not separate chat access from host access to terminals and files.

## Key points
- Alpha badge; Apache-2.0; about 11k stars, 1.8k forks, 892 open issues, 5,377 commits on main at retrieval (README page figures).
- Architecture per docs: a runner wraps any agent in a uniform session and can run on your machine, Modal or Daytona; a server adds policies and shared history; clients are terminal, web, native and mobile apps, REST API. Server storage Postgres/SQLite and OIDC per Atlan's explainer.
- Policies at three levels: server-wide, per-agent, per-session. Agent definitions are short YAML files (prompt, Python/MCP tools, sub-agents). Built-in agents: Polly (coding orchestrator), Debby (model debate).
- Sandbox providers listed: Modal, Daytona, Blaxel, Islo, E2B, Gensee, CoreWeave, Kubernetes, OpenShell, Boxlite, microsandbox, Databricks.
- Requires Python 3.12+, Node 22+, tmux (bubblewrap on Linux). Terminal agents run inside tmux panes wrapped by the web UI (Goose/Hermes/Devin native TUI in a pane). `omnigent import` converts local Claude Code/Codex transcripts into Omnigent sessions.
- Limitations stated: Windows degraded (no tmux wrappers or sandboxing); telemetry on by default; Grok Build and Devin depend on vendor CLI logins.
- Open issues on the first page (all opened 2026-10-23/24): OIDC login failing with Microsoft Entra ID (#11417); sessions stuck 'running' or 'failed' after turns end (#11418, #11437, #11484); auth failures with opaque errors (#11470, #11488); terminal double-reply bugs (#11497); users cannot use their own ChatGPT/Claude subscription in managed sandboxes (#11493); side chats not allowed on a shared session on another user's host (#11414). These are open issues, not a failure rate.

## Could not verify
- Which harnesses are fully supported vs community-maintained (Atlan reports tiers) was not confirmed on the repo itself.
- Last commit date not shown on the fetched page.
