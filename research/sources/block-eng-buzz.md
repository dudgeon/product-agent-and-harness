---
title: "Buzz! 🐝"
source_url: https://engineering.block.xyz/blog/buzz
author: Tyler Longwell (Block)
publisher: Block Engineering Blog
published: 2026-07-21
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [shared-persistent-sessions, harness-portability, identity-delegation, agent-control-plane, one-job-per-agent]
relevance: high
---

## Relevance to the project
Buzz is Block's open-source, self-hostable workspace where people and agents collaborate in channels (built on Nostr, with Git hosting). It is harness-agnostic: Claude Code, Codex, goose or any ACP agent can sit in a channel. It marks a shift in Block's thinking from "a better individual agent" (goose) to coordination: "the bottleneck moved from intelligence to coordination." Relevant to shared sessions, agent identity and whether the PM's workspace should be a channel with agents in it.

## Themes
- shared-persistent-sessions: short-lived channels hold discussion, patches, CI results, reviews and merge decisions so reasoning stays searchable; "a project becomes a conversation with code in it."
- harness-portability: teams can change models or harnesses without losing project identity, permissions or history.
- identity-delegation: each agent has its own keypair; the owner signs a narrowly scoped authorisation and the agent signs its own work; revoking an agent does not touch the human identity.
- one-job-per-agent: a frontier agent coordinates cheaper, faster agents via ordinary @mentions; humans redirect mid-task.
- agent-control-plane: open protocol specs, test vectors and formal (TLA+) models at github.com/block/buzz.

## Key points
- Motivation: early AI use had people copying agent output into Slack and back, making individuals faster and teams slower.
- Shared inference: run requests on a teammate's machine (MeshLLM) without routing prompts through the server.

## Could not verify
- No usage figures; relation to Builderbot and g2 not stated; whether non-engineers use it.
