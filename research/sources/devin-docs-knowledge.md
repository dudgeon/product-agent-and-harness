---
title: "Knowledge (Devin docs)"
source_url: https://docs.devin.ai/product-guides/knowledge
author: Cognition
publisher: Devin documentation
published: unknown
retrieved: 2026-10-25
type: docs
evidence: vendor-claim
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, tacit-knowledge-capture, human-review-gates]
relevance: medium
---

## Relevance to the project
A shipped product mechanism for the "curated from corrections" rung: when a user corrects Devin in chat, it proposes a Knowledge item (a few sentences plus a retrieval trigger) which the user edits, saves, dismisses or asks it to regenerate. The human stays the curator, the agent drafts the lesson. Two details matter for PM skills: each item has its own trigger description deciding when it is retrieved (the same triggering problem skills have), and the docs now say Knowledge is being retired in favour of Skills in Plugins, i.e. the correction store is converging on the skill format.

## Themes
- skill-improvement-loops: Devin "will automatically suggest Knowledge to remember based on your feedback in chat"; suggestions can be edited, dismissed or regenerated; Devin can also suggest updates to existing items (Suggestions section).
- tacit-knowledge-capture: a Knowledge item is tips or instructions plus a trigger description for when to retrieve it; retrieved when relevant, not all at once (overview).
- human-review-gates: every suggested item passes through the user before it is saved (Suggestions section).

## Key points
- Pinning: none (retrieved when triggered), one repo (always used there) or all repos.
- Macros: `!name` shorthand (e.g. `!deploy-checklist`) to invoke an item in a prompt.
- Deprecation notice: Knowledge is migrating to Skills in Plugins; new instructions should be written as Skills.
- Vendor documentation; no data on how often suggestions are accepted or how much they improve sessions.

## Could not verify
- Auto-extraction from CLAUDE.md/AGENTS.md/.cursorrules and the "Accessed Knowledge" panel appear only in search snippets of localised doc pages, not in the English page read.
