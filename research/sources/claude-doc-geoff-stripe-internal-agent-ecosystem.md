---
title: Stripe's Internal Agent Ecosystem for Product Development
source_url: https://claude.ai/artifact/PG1sfq8UxAJzhVxRgrmeu3
author: Geoff Dudgeon (doc byline; compiled with Claude)
publisher: Claude Docs (private doc shared by Geoff)
published: 2026-10-24
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [agent-factory-sdlc, one-job-per-agent, non-engineer-builders, legible-org-for-agents]
relevance: high
---

## Relevance to the project
Geoff's own map of Stripe's internal agents for product development. It widens this teardown from Kai to about six tools across the PM-to-code loop (Kai, Orbit, Minions, the "Gru" code-review agent, Harbor, Protodash), on a shared foundation (Toolshed, devboxes, Trailhead internal docs, Compass project tracking). It names Orbit and Trailhead, which the first pass of this teardown had not covered, and it prompted Geoff's hypothesis that a business and operational context-creation agent is needed. It is a secondary compilation: every claim traces to the linked sources, which are filed separately.

## Themes
- agent-factory-sdlc: a five-stage flow diagram: 1 Research (Kai, PM pulls data and docs) → 2 Prototype (Harbor or Protodash) → 3 Plan (Orbit, engineer; team comments) → 4 Build (Minions on a devbox) → 5 Review (review agent plus a human; every PR human-reviewed); shortcut: prototype straight to a coding agent, or a PM starts a minion from Slack.
- one-job-per-agent: "specialized agents that call each other's capabilities, not one tool that does everything".
- non-engineer-builders: PMs are heavy users of Protodash and Harbor; a PM (Stripe Projects) built a prototype CLI and revised it between morning and afternoon research sessions.
- legible-org-for-agents: Toolshed (nearly 500 MCP tools), devboxes, Trailhead (internal docs) and Compass (project tracking) form the shared foundation.

## Key points
- Table of tools with job, main users and key facts; Orbit "first shown Oct 22, 2026": reads codebase and Trailhead, writes a plan teammates comment on, hands it to a minion with one button; minion may run up to 12 hours and pause to ask; engineers run 3-7 projects in parallel.
- Code-review agent name "Gru" inferred from auto-captions ("Grew").
- Caveats listed by the doc itself: Orbit documented only by one video and one tweet; whether PMs use Orbit directly isn't stated; Kai figures differ by date; the Department of Product piece is paywalled.

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- "PMs and designers in equal numbers" for Protodash: the Protodash episode says "more PMs than designers these days"; no numbers.
- "Rami Banna" as the PM in the Clay video is the doc's inference (captions say "Romi"/"Ramy"); Banna is the author of the Stripe Projects post.

## Added 2026-10-24
- The Department of Product piece is no longer unread: read in full through Geoff's subscription; see [departmentofproduct-stripe-kai](departmentofproduct-stripe-kai.md).
