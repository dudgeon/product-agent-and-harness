---
title: How We Use goose to Maintain goose
source_url: https://goose-docs.ai/blog/2025/12/28/goose-maintains-goose
author: Rizel Scarlett and Tyler Longwell (Block)
publisher: goose blog
published: 2025-12-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-factory-sdlc, human-review-gates, remote-agent-invocation, memory-architecture]
relevance: medium
---

## Relevance to the project
A `/goose` comment on a GitHub issue launches a containerised headless goose running a six-phase recipe that ends in a draft PR. It is the open-source twin of Block's internal issue-to-PR flows and shows the recipe shape (understand, research, plan, implement, verify, confirm) and the gates.

## Themes
- remote-agent-invocation: maintainers comment `/goose`; a GitHub Action starts a container with issue metadata.
- human-review-gates: only permitted users can invoke; file-modification restrictions; a maintainer must approve every PR; nothing auto-merges.
- memory-architecture: TODO extension used as external memory because context compaction can drop instructions.
- agent-factory-sdlc: issue #6066 got a PR 14 minutes after the trigger; #6232 a draft with four tests within an hour.

## Could not verify
- No aggregate success or merge rates.
