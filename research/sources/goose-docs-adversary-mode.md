---
title: Adversary Mode (goose docs)
source_url: https://goose-docs.ai/docs/guides/security/adversary-mode
author: goose maintainers (AAIF)
publisher: goose-docs.ai
published: unknown (blog announcement 2026-03-31)
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-protocol-security, policy-enforcement-fail-open, human-review-gates]
relevance: medium
---

## Relevance to the project
goose's answer to the red-team findings: an optional second agent that reviews each tool call against plain-language rules and returns ALLOW or BLOCK. It is a reviewer-agent pattern inside a single harness, and it fails open.

## Themes
- agent-protocol-security: the reviewer sees the original task, recent messages and the tool call; built for compromise, prompt injection or drift.
- policy-enforcement-fail-open: if the reviewer errors, the call is allowed ("fail-open").
- human-review-gates: blocked calls are denied and cannot be retried; complements pattern-based prompt-injection detection and permission modes.

## Key points
- Off by default; enabled when `~/.config/goose/adversary.md` exists; uses the same model and provider as goose.
- Reviews only `shell` unless a `tools:` line names others (e.g. computer control).

## Could not verify
- Whether Block enables it on managed laptops.
