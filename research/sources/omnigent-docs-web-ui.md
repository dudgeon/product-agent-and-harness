---
title: "Web UI (Omnigent documentation)"
source_url: https://omnigent.ai/docs/interact/web-ui
author: Omnigent maintainers (Databricks and contributors)
publisher: omnigent.ai
published: unknown
retrieved: 2026-11-10
type: docs
evidence: vendor-claim
filed_by: film-omnigent-canvas-coach
themes: [meta-harness, product-artifact-primitives]
relevance: medium
---

## Relevance to the project
Omnigent's own description of its web app layout, read to draw a recognisable (not copied) workspace for the canvas-coach concept film. It shows what the product has today: a chat with a composer, a right-hand Workspace rail for files, diffs, shells and side chats, and a Canvas page that is a spatial board of session cards. It has no agent-generated planning artifacts, which is the gap the concept film imagines filling.

## Themes
- [[meta-harness]]: the web UI is one of several clients on the same session (terminal, web, desktop, mobile, Slack are listed under Interfaces in the docs sidebar).
- [[product-artifact-primitives]]: the Canvas page "gives you a spatial view of your work": top-level sessions as draggable cards, one canvas per project. The objects on the board are sessions, not product artifacts (Canvas section).

## Key points
- **Sidebar (left):** My sessions (Pinned, project folders, Sessions) and Shared with me; Inbox, Automations and Canvas are reached from it.
- **Chat (centre):** composer with `/` commands, `@` file mentions, attachments, a model and effort picker and a permissions dropdown. A follow-up sent mid-turn steers the agent by default.
- **Workspace rail (right):** tabs for Files, Changes, GitHub (pull requests) and Agents, plus shells, browser tabs and side chats; collapsed by default on a new chat.
- **Files:** a markdown editor with syntax highlighting; Changes shows syntax-highlighted diffs.
- **Canvas:** off by default; an operator enables the `canvas` release feature.

## Notable quotes
- "The Canvas page gives you a spatial view of your work."
- "Canvas is off by default."

## Could not verify
- Read through a summarising fetch, so wording outside the quotes is paraphrase. The page does not say how agents render HTML or images in the UI.
- An npm package named `omnigent` (v2.0.0) carries a macOS "Canvas" doc about an agent-controlled WKWebView panel, but its paths and commands say "OmniAgent" and match OpenClaw's docs; it looks like a different project and was not used.
