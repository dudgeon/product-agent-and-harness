---
title: goose Permission Modes (docs)
source_url: https://goose-docs.ai/docs/guides/managing-tools/goose-permissions
author: goose maintainers (AAIF)
publisher: goose-docs.ai
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-block-product-practices
themes: [evals-autonomy-trust, human-review-gates, risk-sloped-review]
relevance: medium
---

## Relevance to the project
goose's autonomy slider: Completely Autonomous (the default), Manual Approval, Smart Approval and Chat Only, settable per session. Smart Approval is risk-sloped review but rests on a best-effort read/write classification "interpreted by your LLM provider". Useful as a reference for how a general harness exposes autonomy to non-engineers.

## Themes
- evals-autonomy-trust: four modes; autonomous by default; per-session mode with `/mode auto|smart_approve|approve|chat`.
- risk-sloped-review: Manual and Smart modes only ask for tools classified as "write" (text editor writes, rm/cp/mv); granular per-tool permissions in both.
- human-review-gates: when goose drives Claude Code as a CLI provider in approve mode, Claude Code's permission prompts surface in goose.

## Key points
- Subagents only spawn autonomously in Autonomous mode ([goose-docs-subagents](goose-docs-subagents.md)).

## Could not verify
- How Smart Approval scores risk beyond tool annotations; whether an admin can lock the mode.
