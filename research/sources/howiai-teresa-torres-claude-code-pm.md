---
title: "Claude Code for product managers: research, writing, context libraries, custom to-do system, and more | Teresa Torres"
source_url: https://www.lennysnewsletter.com/p/claude-code-for-product-managers
author: Claire Vo (host), Teresa Torres (author of Continuous Discovery Habits, Product Talk)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-01-19
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [memory-architecture, compounding-context-repo, org-context-grounding, research-synthesis-agents, human-judgment-pm-jobs, non-engineer-builders, harness-portability, docs-as-code-prd]
relevance: medium
---

## Relevance to the project
A well-known discovery coach shows a working personal PM harness built on Claude Code plus an Obsidian vault of Markdown files: a task system, a daily research digest, and a context library. Its strongest contribution is a concrete, tested context-management pattern: many small context files behind index files, loaded on demand, written by the agent itself at the end of each session ("what did you learn today that we should document?"). That bears directly on context-and-memory and capability-format-portability (she keeps the vault model-neutral so she can switch to Codex). It is one solo practitioner, not a team or enterprise, so it shows feasibility, not adoption.

## Themes
- memory-architecture: separate project-level and global CLAUDE.md; a dedicated "LLM context" vault of small files, each topic split (business vs personal profile, one file per product); index files tell Claude what exists, and the global CLAUDE.md routes business requests to the business profile (25:35-30:42).
- compounding-context-repo: context files are written by Claude, iteratively, prompted at session end with "what did you learn today that we should document?" (32:43); the tag taxonomy for tasks lives in the project CLAUDE.md and is co-maintained (11:29).
- org-context-grounding: too much irrelevant context degrades results: "if we give it too much irrelevant context it's still going to not be very good at its job" (31:48); her own documentation lets her `/clear` freely without re-explaining (41:14).
- research-synthesis-agents: a plugin with two cron'd Python scripts searches arXiv daily and Google Scholar weekly from a keyword config, tracks seen papers, and next day spawns Claude Code agents to summarise PDFs she saved, focusing on methods and effect sizes; she hand-picks papers in 5-10 minutes a day (16:04-21:55).
- human-judgment-pm-jobs: she frames every task as "automation or augmentation" and chooses to keep writing herself; Claude critiques against a co-written style guide rather than writing (25:35, 33:28). She catches a weak study only because the summary surfaced its method (17:35).
- non-engineer-builders: started coding in the AWS console with no version control; VS Code plus Claude Code made her "pair everything" (2:42).
- harness-portability: she calls the vault "LLM context because sometimes I switch to codex. It doesn't matter which model you're using" (25:35).
- docs-as-code-prd (adjacent): tasks are Markdown files with YAML front matter (type, due date, tags) that Claude searches and tags; a `/today` slash command plus a Python script assembles the day (6:09-8:38).

## Key points
- Motivation for leaving Trello: notes locked in a third-party tool, poor search; with Markdown files Claude "will try every permutation of searches till it finds it" (4:36, 14:10).
- She still uses a Trello MCP server to coordinate with her team, but her own tasks live locally (8:51). Personal system, team tool at the edge.
- Two blog posts were mostly LLM-written, disclosed (interview transcripts turned into stories; podcast themes) (33:28).
- The Claude-built context files were long and co-edited; she "did not write this myself at all" for the style guide (27:08).

## Notable quotes
- "We have to document everything in teeny tiny files." (28:42)
- "Claude, what did you learn today that we should document? And I make Claude do it." (32:43)

## Could not verify
- Transcript read in full (Substack auto-transcription; lower-case run-ons in places).
- Single-user system; no measures of time saved or quality. The research plugin had "one user" at the time (19:45).
