---
title: Cloudflare Sandbox SDK documentation
source_url: https://developers.cloudflare.com/sandbox/
author: Cloudflare
publisher: Cloudflare Developers docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
Confirms that Claude Code, Codex and Devin can be run inside a Cloudflare sandbox as a per-task environment, i.e. Cloudflare as a session runtime for third-party harnesses, separate from Cloudflare OS.

## Themes
- [[shared-persistent-sessions]]: sandbox identity can persist; a Lifetime page covers snapshots; R2 mounting is possible; rywalker's survey notes Cloudflare keeps sandbox identity but not a stopped container's files.

## Key points
- Two environments: Containers (each instance in its own microVM, your image) and Dynamic Workers (runtime-created isolates).
- Has a 'Coding agents' guide for running Claude Code, Codex, Devin in a sandbox dedicated to one task; details not read.
- Workers Paid plan; the page labels only the DO scheduling policy 'public beta'; 0.x users are pointed to a migration guide.

## Could not verify
- Overall GA status and the coding-agents guide contents were not retrieved.
