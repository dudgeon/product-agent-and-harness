---
title: "How to build prototypes that actually look like your product | Colin Matthews (product leader, AI prototyping instructor at Maven)"
source_url: https://www.lennysnewsletter.com/p/how-to-build-prototypes-that-actually
author: Claire Vo (host), Colin Matthews (PM, founder, Maven AI prototyping instructor)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-06-30
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [prototyping-agents-limits, non-engineer-builders, artifact-standardization]
relevance: low
---

## Relevance to the project
A PM workflow for making AI prototypes match an existing product: build a component library from screenshots (or extract components from a live site), then compose prototypes from those components and fork rather than edit the baseline. For the project it is a small, practical point about prototyping as an intent-shaping artifact: prototypes are only useful in hand-offs if they look like the real product, which pushes toward a shared, reusable component layer (artifact-and-project-structure). Downgraded from medium because no transcript was available and the show notes carry the method only in outline. The same author's longer guide is filed as lenny-newsletter-ai-prototyping-guide-pms.

## Themes
- prototyping-agents-limits: the episode's premise is that out-of-the-box AI prototypes don't look like your product; the fix is a component library generated from screenshots in v0, or extracted from any website with the Magic Patterns Chrome extension (show notes, 02:46-18:38). Notes also promise "the debugging approach that solves 90% of AI prototyping errors" (show notes, what you'll learn).
- artifact-standardization: improve the components rather than the composed application (18:38); use forks and versions so iteration doesn't break a baseline (20:15).
- non-engineer-builders: covers introducing AI prototyping to a team "without stepping on designers' toes" (25:05).

## Key points
- The show notes include the full v0 prompt: analyse a screenshot, identify components (buttons, inputs, nav bars, cards, modals, typography), build each as a custom React functional component styled with Tailwind, responsive and accessible, with props and a comment, then an index page showing each with example usage, using no external component libraries (show notes).
- Tools: v0, Magic Patterns and its Chrome extension, Cursor, Bolt; a public prompt library from the guest (show notes).
- Guest background: eight years in healthtech, most recently a PM at Datavant (show notes), which gives some regulated-industry context but none is discussed in the notes.

## Could not verify
- No transcript file was available; this note works from the show notes and chapter list only. The forking workflow, structured-prompting technique, debugging approach and team-dynamics advice are described in titles only, so their content is not verified.
- The guest sells a prototyping course; the "90%" claim is his own.
