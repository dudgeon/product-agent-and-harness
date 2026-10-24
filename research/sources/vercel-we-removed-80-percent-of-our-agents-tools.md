---
title: We removed 80% of our agent's tools
source_url: https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
author: Vercel
publisher: Vercel blog
published: 2025-12-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, build-vs-buy]
relevance: medium
---

## Relevance to the project
A vendor case where simplifying the harness (many specialised tools to one bash tool over well-documented files) improved success, speed and tokens. Another data point that harness scaffolding goes stale and that the simplest architecture should be tried first.

## Themes
- harness-over-model: d0 text-to-SQL agent success 80% to 100% on five benchmark queries; time 275 s to 77 s; tokens down 37%; steps 12 to 7.

## Key points
- Depends on well-documented, consistently named data; without it raw file access gives faster bad queries.

## Notable quotes
- "Addition by subtraction is real."

## Could not verify
- Tiny benchmark (five queries); author is also vendor of the AI SDK.
