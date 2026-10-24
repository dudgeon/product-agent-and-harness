---
title: "Feature: Add Agent-to-Agent (A2A) Protocol Support with AgentCardBuilder (openai/openai-agents-python #1245, with #3567 and #3683)"
source_url: https://github.com/openai/openai-agents-python/pull/1245
author: OpenAI Agents SDK maintainers (seratch) and contributors
publisher: GitHub
published: 2025-07-25
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, agent-frameworks, harness-portability]
relevance: medium
---

## Relevance to the project
OpenAI's own maintainers have declined A2A support in the OpenAI Agents SDK three times (July 2025, June 2026 twice), each time saying there are no immediate plans and suggesting a community package. Together with Codex having no A2A code (its `codex-rs` tree has MCP and app-server crates, no A2A crate) this is first-party evidence that OpenAI's agent stack does not speak A2A natively as of October 2026, even though A2A now sits in the same foundation (AAIF) that OpenAI co-founded.

## Themes
- `remote-agent-invocation`: 2025-07-25 maintainer: "we don't have immediate plans to add A2A support to this SDK"; 2025-11-06: prefer to "hold off on adding this adapter layer as part of the core SDK" and invites a community package; 2026-06-04 (#3567): "we don't have immediate plans to add this module within this SDK"; 2026-06-24 (#3683): "We still don't have immediate plans to add A2A support as a feature within this SDK."
- `agent-frameworks`: Contrast: Google ADK, AWS Strands, CrewAI and AWS bedrock-agentcore ship A2A as optional extras; Microsoft has `agent-framework-a2a` (see [pepy note](pepy-a2a-sdk-downloads.md)).
- `harness-portability`: The HN story "OpenAI rejects 1,200-line community PR for Google's A2A agent protocol" (2025-10-30, item 45766384) framed this as vendor politics; a contributor argued the SDK should stay lightweight.

## Key points
- PR #1245 closed as stale 2025-08-13, not merged. Comment thread revived 2025-10-30 after the HN post.
- Codex: three community items titled "feat(a2a)" (#11977, #11978, #11980, Feb 2026) describe an A2A server in a contributor's `codex-rs/a2a`; closed, and no A2A crate exists in `openai/codex` `codex-rs` at retrieval (checked via GitHub contents API).

## Could not verify
- Whether OpenAI Responses API, AgentKit or ChatGPT agents have any A2A endpoint; none found.
