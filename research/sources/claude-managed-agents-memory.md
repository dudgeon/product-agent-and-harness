---
title: "Memory for Claude Managed Agents: agents that learn across sessions"
source_url: https://claude.com/resources/articles/claude-managed-agents-memory
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-04-23
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [memory-architecture, org-learning-loop, enterprise-admin-controls, build-vs-buy]
relevance: medium
---

## Relevance to the project
Anthropic's launch of built-in, file-based memory for Managed Agents describes a concrete memory architecture with enterprise controls: stores mounted as a filesystem, shareable across agents with different scopes (org-wide read-only, per-user read-write), concurrent-safe, versioned, auditable to the agent and session that wrote each memory, with rollback and redaction. That gives the strategy a specific vendor option for the context-and-memory dimension and a reference point for what governed agent memory should support. It is a beta announcement: the customer outcome numbers are the customers' claims and no failure modes (poisoned or stale memories) are discussed.

## Themes
- memory-architecture: memory mounts onto a filesystem so the agent uses bash and code execution on it; memories are files exportable and manageable by API (sections "How memory works", "Portable memories").
- org-learning-loop: agents "learn from every session" and stores can be shared so agents share what they have learned; Netflix carries human mid-conversation corrections across sessions "instead of manually updating prompts and skills" (sections "How memory works", "What teams are building").
- enterprise-admin-controls: scoped permissions per store, audit log of every change by agent and session, rollback, redaction from history, session events in the Console (section "Portable memories").
- build-vs-buy: Ando and Wisedocs say the feature replaced memory infrastructure they would otherwise build (section "What teams are building", quotes).

## Key points
- Anthropic states memory is "optimized against internal benchmarks for long-running agents" and that its latest models save more organised memories and are more discerning about what to keep; no benchmark detail given.
- Access pattern example: an org-wide store read-only, per-user stores read-write; multiple agents can write the same store concurrently without overwriting each other.
- Customer claims: Rakuten 97% fewer first-pass errors with 27% lower cost and 34% lower latency; Wisedocs 30% faster document verification, including issues "we didn't think about"; Netflix and Ando described qualitatively.
- Public beta on the Claude Platform at launch.
- Limits: nothing on memory quality review, conflicting or wrong memories, retention policy, or how human approval of learned rules works; the Netflix point implies learned memory can bypass the reviewed skills path.

## Notable quotes
- "Memories are files that can be exported and independently managed via the API" (section "Portable memories")

## Could not verify
- The internal benchmarks; Rakuten, Wisedocs figures and their baselines.
