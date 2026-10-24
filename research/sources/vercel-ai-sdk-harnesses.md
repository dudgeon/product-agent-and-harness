---
title: AI SDK Harnesses (HarnessAgent)
source_url: https://ai-sdk.dev/docs/ai-sdk-harnesses
author: Vercel
publisher: ai-sdk.dev docs
published: 2026-06-12
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-portability, agent-frameworks, meta-harness]
relevance: high
---

## Relevance to the project
A code-level harness-agnostic layer: one AI SDK interface (HarnessAgent) to drive Claude Code, Codex, Pi and later others inside sandboxes, so a product can swap harnesses like models. This is the 'framework as meta-harness' option, as opposed to Omnigent's server-level one.

## Themes
- [[harness-portability]]: swap `claudeCode` for `codex` or `pi` while keeping the same flow; later reports add Cursor, Cline, Deep Agents, Grok Build, OpenCode (dated 2026-08-27, secondary).
- [[agent-frameworks]]: harnesses are separate from the provider/model abstraction; sessions hold runtime, sandbox, working dir, native history and pending approvals; resumable via detach()/stop().

## Key points
- Experimental canary API in AI SDK 7 (changelog early June 2026); packages warn of breaking changes.
- Execution environment varies by adapter; the docs advise a security review per adapter.
- Customisation points: instructions, skills, AI SDK tools, permission settings, sandbox setup hooks.

## Could not verify
- Exact release date taken from search summaries of the changelog; adapter list page not read.
