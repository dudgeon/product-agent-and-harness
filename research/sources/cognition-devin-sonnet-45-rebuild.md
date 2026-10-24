---
title: Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges
source_url: https://cognition.com/blog/devin-sonnet-4-5-lessons-and-challenges
author: Cognition
publisher: Cognition blog
published: 2025-09-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [harness-over-model, build-vs-buy]
relevance: high
---

## Relevance to the project
A vendor that owns its harness had to rebuild parts of it for one new model (context anxiety, parallel tool use, note-taking), reporting 2x speed and 12% better evals. A direct example of recurring harness maintenance cost caused by model changes, and the same effect Anthropic cites as stale assumptions.

## Themes
- build-vs-buy: model swap is not drop-in; harness assumptions break.
- harness-over-model: remedies were prompt reminders, capping context at 200k under the 1M beta, keeping own memory and compaction.

## Key points
- Sonnet 4.5 aware of its own context window; summarises early and cuts corners near the limit.
- Model writes notes to the filesystem but not thoroughly enough to replace Cognition's memory system.
- Parallel tool use speeds sessions but eats context.

## Notable quotes
- "Sonnet 4.5 is the first model we've seen that is aware of its own context window"

## Could not verify
- Rebuild effort/cost not stated in the post.
