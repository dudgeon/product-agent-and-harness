---
title: "Omnigent's HTML preview: agent-written HTML rendered in the file viewer (omnigent-ai/omnigent #12716, #12154, #9427 and web/src/shell/HtmlCommentViewer.tsx)"
source_url: https://github.com/omnigent-ai/omnigent/pull/12716
author: Omnigent maintainers
publisher: GitHub
published: 2026-11-04
retrieved: 2026-11-11
type: other
evidence: first-party
filed_by: film-omnigent-canvas-coach
themes: [product-artifact-primitives]
relevance: high
---

## Relevance to the project
Confirms that Omnigent already renders the HTML an agent writes, in a pane beside the chat, which is the surface the canvas-coach concept film builds on. This corrects the film's first draft, which treated Omnigent's page named Canvas (a board of session cards) as the only canvas. What Omnigent lacks is not a place to render artifacts but the product artifacts themselves, and an open feature request (#9427) says so for slides and wireframes.

## Themes
- [[product-artifact-primitives]]: "When an agent writes an HTML file and you open it in the file viewer", it is shown rendered (#12154 summary); the maintainers call it "an HTML artifact" (#12716 title and summary). #9427 (open): "Agents are good at writing slides and wireframes as HTML, but Omnigent has nowhere to show them as what they are".

## Key points
- **Where it renders:** the file viewer, which sits in the Workspace rail to the right of the chat (see [omnigent-docs-web-ui](omnigent-docs-web-ui.md)). The preview is a sandboxed iframe with an opaque origin (`HtmlCommentViewer.tsx` header comment; #12716 design notes).
- **Comments:** the viewer "renders agent-generated HTML in the same sandboxed iframe as the read-only preview, but injects a bridge script so users can select rendered text and attach review comments", for parity with the Markdown and code viewers (source header, read 2026-11-11).
- **Zoom:** Cmd/Ctrl plus, minus and 0 zoom only the rendered file (#12154, merged 2026-10-29).
- **Scroll position:** kept across tab and session switches (#12716, merged 2026-11-04).
- **What is missing, in a user's words (#9427, open, 2026-10-07):** a deck opens "in the plain HTML preview: one long page"; no brand kit or templates; no single place to find designs; hard to share or review. The request proposes slide and wireframe viewers that reuse the existing preview.
- The page named Canvas is a different thing: a board of session cards ([github-omnigent-canvas-split-chat-pr-7431](github-omnigent-canvas-split-chat-pr-7431.md)).

## Could not verify
- Pull request descriptions and one source file header were read, not the running app. Whether the agent can open the preview itself, or the person must open the file, was not checked.
