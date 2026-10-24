---
title: "Why We Built Our Own Background Agent (Ramp Builders blog)"
source_url: https://builders.ramp.com/post/why-we-built-our-background-agent
author: Zach Bruggeman, Jason Quense, Rahul Sengottuvelu (Ramp)
publisher: builders.ramp.com
published: 2026-01-12
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: user-story-mapping
themes: [shared-persistent-sessions, non-engineer-builders, legible-org-for-agents]
relevance: high
---

## Relevance to the project

Ramp's own account of Inspect, the background coding agent that Open-Inspect reimplements. For the artifact question it shows that Inspect's unit of organisation is the session (own SQLite database, shareable by URL, multiplayer, attributed prompts) and its output is the pull request (plus before/after screenshots appended to PR descriptions). There is no mention of specs, PRDs, projects or folders: work enters from Slack threads, PR comments, the web UI or a Chrome extension, and leaves as PRs. Title, authors and date are from the page's meta tags; body quotes are via WebFetch (the page is JS-rendered).

## Themes

- shared-persistent-sessions: "Send your session to any colleague, and they can help take it home."; "All changes are synced to the session, so you never lose your work while switching around."; each session has its own SQLite database so sessions do not affect one another.
- non-engineer-builders: clients are Slack, a Chrome extension, the web UI, PR comments and a web VS Code; a Slack classifier picks the repository from message, thread and channel name.
- legible-org-for-agents: sessions are "wired into" Slack and GitHub; "a crucial tool is one that allows it to spawn sessions itself" to split work across repositories or PRs.

## Key points

- Sandboxed VM per session on Modal with an engineer's local toolset; warm the sandbox as the user starts typing.
- "Because Inspect sessions are fast to start and effectively free to run", engineers run many versions of one prompt concurrently.
- PR opened by the API with the user's GitHub token, so the author cannot approve their own agent's change ("a vector for unreviewed code").
- "~30% of all pull requests merged to our frontend and backend repos are written by Inspect" (January 2026 figure; later sources say 50% and 75%).
- Statistics page tracks sessions that end in a merged PR.
- Meta description: "The craft of engineering is rapidly changing. We built our own coding agent to accelerate faster."

## Could not verify

Body text was read only through WebFetch (model summary with short quotes), because the page's HTML is a 5 KB JS shell. Full paragraphs and section headings were not captured. No statement about Glass, Notion, Linear or any artifact store beyond GitHub was reported by the fetch; absence is from that summary, not a verbatim read.
