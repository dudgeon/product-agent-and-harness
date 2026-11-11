---
title: "feat(web): open Canvas sessions in a split chat panel (omnigent-ai/omnigent #7431)"
source_url: https://github.com/omnigent-ai/omnigent/pull/7431
author: Omnigent maintainers
publisher: GitHub
published: 2026-09-15
retrieved: 2026-11-10
type: other
evidence: first-party
filed_by: film-omnigent-canvas-coach
themes: [product-artifact-primitives]
relevance: medium
---

## Relevance to the project
The pull request that puts a chat beside Omnigent's Canvas board, read to get the two-pane arrangement right for the canvas-coach concept film. It fixes the layout the film draws: sidebar, then the board, then a divider, then the chat on the right. It also shows the board and the chat are still separate things: clicking a card opens that session's chat, and the chat does not write to the board.

## Themes
- [[product-artifact-primitives]]: the layout sketch in the description reads "Sidebar | Canvas board | divider | existing session workspace", with transcript, composer, files, terminals and agents on the chat side (Summary).

## Key points
- A single click on a Canvas card opens the session's full chat on the right; the board stays mounted and the selected card is highlighted.
- The split is resizable; on a narrow screen the chat covers the board. The web source (`web/src/canvas/CanvasWorkspace.tsx`, read 2026-11-10) gives the board a default 0.54 share of the width.
- Selection lives in the URL; drafts and background streams survive switching or closing.
- Listed as open in the issue search on 2026-11-10; the `canvas` feature flag (off by default, since 0.15.0) is in `designs/FEATURE_FLAGS.md`.

## Notable quotes
- "Canvas stays where you left it while the chosen chat opens alongside it."

## Could not verify
- Whether this pull request has merged in some other form; only its description was read, not the diff.
