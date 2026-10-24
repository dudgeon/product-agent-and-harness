---
title: "Show HN: Superset – Terminal to run 10 parallel coding agents"
source_url: https://news.ycombinator.com/item?id=46368739
author: avipeltz (Superset team) and HN commenters
publisher: Hacker News (read via hn.svelte.dev mirror)
published: 2025-12 (approximate; mirror shows about 10 months before retrieval)
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
The only independent reaction found to Superset. It confirms the limits of local parallel-session managers that Track 1 noted (review is the bottleneck; worktrees do not isolate services) and that this class is a developer-throughput tool, not a knowledge-work or governance layer.

## Themes
- meta-harness: commenters list Conductor, Vibe Kanban, Claude Squad, Mux, Catnip and Cursor's agents UI as alternatives; the category is crowded and interchangeable.
- vendor-claims-vs-independent-evidence: about 96 points and about 88 comments; mixed reception.

## Key points
- Praise from users at work ("I've used superset at work this last week, and it's great!", roggenbuck); low friction to spin a worktree (~2 s).
- Criticism: review bottleneck ("The real bottleneck isn't human review per se, it's unstructured review", amortka); cost ("10x the cost with 0 to show", nickphx); worktrees as the wrong primitive (eigenvalue); shared databases and services not isolated per worktree; xterm.js performance; macOS only; name clash with Apache Superset.
- Licence was not discussed; the team described it as open source at the time.

## Could not verify
- Exact post date and final counts (read through a mirror).
