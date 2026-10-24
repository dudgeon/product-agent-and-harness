---
title: Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue
source_url: https://blog.cloudflare.com/agents-platform-flue-sdk
author: Thomas Gauvin (Cloudflare)
publisher: Cloudflare Blog
published: 2026-06-17
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, agent-frameworks, meta-harness]
relevance: high
---

## Relevance to the project
Gives a useful three-layer vocabulary: framework / harness / runtime-platform, with Cloudflare's Agents SDK positioned as the base any harness can target. It is the closest Cloudflare gets to a harness-agnostic layer, but at the platform level: harnesses must be ported to it, and Claude Code/Codex are not claimed to run there.

## Themes
- [[harness-portability]]: Agents SDK is a runtime layer any harness or framework can target; Flue (from the Astro team, built on the Pi harness) is first; Pi and Project Think are the harnesses.
- [[agent-frameworks]]: framework = structure, conventions, CLI, DX; harness = the loop that calls tools and manages context; runtime = compute, state, storage.
- [[meta-harness]]: the post lists Codex, Claude Code, OpenCode, Pi and Project Think as matured harnesses but does not say they run on Cloudflare; contrast with Omnigent which wraps them.

## Key points
- Flue 1.0 Beta; each agent runs in its own Durable Object using Agents SDK fibers; supports Slack, GitHub, Linear and Discord channels.
- Any harness targeting the SDK gains durable execution, dynamic code execution, durable filesystem and dynamic workflows.
