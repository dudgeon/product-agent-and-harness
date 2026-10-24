---
title: The Meta-Harness Pattern: Orchestrating Codex CLI and Claude Code as Sub-Agents Through Pi
source_url: https://codex.danielvaughan.com/2026/07/27/meta-harness-pattern-orchestrating-codex-claude-code-pi-sub-agents/
author: Daniel Vaughan
publisher: codex.danielvaughan.com
published: 2026-07-27
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-portability, cost-control-routing]
relevance: high
---

## Relevance to the project
A practitioner write-up of a DIY meta-harness (Pi as coordinator calling `codex exec` and `claude -p`), with concrete failure modes. Useful as the 'lightweight, CLI-composition' option and as independent evidence on cost multiplication and security gaps.

## Themes
- [[meta-harness]]: coordinator spawns Claude Code and Codex as sub-agents via profiles; hand-offs through workspace files; headless mode with allowlisted backends.
- [[cost-control-routing]]: one delegation to a high-reasoning Codex model can fan out into ~23-25 internal sessions.
- [[harness-portability]]: cross-agent context transfer is weak; 'no interop standard exists yet'.

## Key points
- Works for heterogeneous review and staged implement-then-review; poor for tight edit-test-fix loops (serialisation overhead, lost conversational context).
- Failure modes: token/latency overhead, debugging opacity (Codex inter-agent payloads encrypted), no bound on nested spawning, pi-flow bypasses Codex approvals and Claude permission checks in shared CI.
- Updated 2026-10-24.
