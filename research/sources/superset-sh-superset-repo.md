---
title: superset-sh/superset repository (Superset, "IDE for parallel agents")
source_url: https://github.com/superset-sh/superset
author: Superset Inc.
publisher: GitHub
published: unknown
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, harness-portability]
relevance: medium
---

## Relevance to the project
Confirms which Superset the earlier tracks meant: superset.sh / superset-sh (a desktop app that runs many CLI coding agents in parallel git worktrees), not Apache Superset (the BI tool). It is the local parallel-session-manager shape of "meta-harness" in the practitioner sense (P4 local sub-shape). The finding that matters for the project is the licence: Elastic License 2.0, source-available and not OSI open source, so it cannot be resold as a service, and it is not a governance layer.

## Themes
- meta-harness: launches 21 named CLI agents (Claude Code, Codex CLI, Cursor Agent, Gemini CLI, Copilot, OpenCode, Pi, Amp, Devin, Kiro, Polygraph and others) plus "any other CLI agent" without configuration; each task gets a git worktree, branch and terminals (README features list).
- harness-portability: the layer is at the process/terminal boundary; it never proxies model calls (homepage says so; see superset-sh-site-pricing-enterprise).

## Key points
- Licence: "The whole app is in this repo under the Elastic License 2.0"; "The only thing off the table is repackaging Superset itself as a service you sell to others."
- About 15.5k stars, 1.4k forks, 5,123 commits, 481 open issues and 548 open PRs at retrieval. Topic tag "yc-backed" (funding not stated on page).
- Features: worktrees (README notes worktrees "do not sandbox processes or prevent merge conflicts"); an MCP server so agents can create and manage workspaces; built-in superset:* skills; remote access to other machines; cloud workspaces; automations; CLI and TypeScript SDK; bring-your-own providers (OpenRouter, Bedrock, Vertex, Vercel AI Gateway).
- macOS primary; Linux experimental; Windows not available.
- No SSO, audit or admin policy described in the repo (those are on the paid Enterprise plan per the pricing page).

## Could not verify
- Whether the licence changed from an earlier open-source licence (the Dec 2025 Show HN called it "open-source"); the homepage says the company is "getting a new name soon".
- Release cadence (Releases section not captured).
