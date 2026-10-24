---
title: "What a harness is and how to build one with Claude Agent SDK"
source_url: https://www.lennysnewsletter.com/p/what-a-harness-is-and-how-to-build
author: Claire Vo (host; founder of ChatPRD)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-07-08
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [harness-over-model, build-vs-buy, work-structure-spectrum, one-job-per-agent, artifact-standardization, pm-tool-connectivity, scoped-governance-containers]
relevance: medium
---

## Relevance to the project
Claire Vo builds a task-specific harness live: a Sentry bug-triage harness for her company ChatPRD on the Claude Agent SDK, with a custom terminal UI (Ink) and "opinionated adapters" for Sentry, Linear, GitHub and Vercel, which gathers evidence, analyses root cause and creates follow-up artifacts. The episode outline names the decisions this project cares about: when to build a harness versus staying in Claude Code or Codex, encoding permissions in the harness, a three-component structure, and structuring harness artifacts so the whole team can use them. It bears on loop-source, work-structure (general harness vs task-specific agent), harness-upkeep and artifact-and-project-structure. Relevance is marked medium only because we have the show notes, not the transcript; the full episode is likely high and worth retrieving.

## Themes
- harness-over-model: framed against the slogan "It's not the model, it's the harness", which "almost nobody stops to explain" (show notes intro; 00:00 "What is an AI harness?").
- work-structure-spectrum / one-job-per-agent: a harness is pitched for "any repetitive, structured workflow"; segments on "When to build a harness" (03:19) and "Why not just use Claude Code?" (06:00).
- build-vs-buy: the case for a custom harness on the Agent SDK rather than a general-purpose tool (06:00); she used GPT-5.5 (Codex) and Claude Opus to write the harness code, and "both initially resisted" (13:44).
- scoped-governance-containers: "How to encode specific permissions into a harness" (show notes, "What you'll learn").
- artifact-standardization: "How to structure the artifacts your harness produces so the whole team can use the output" (show notes); architecture segment is "runs, tasks, tools, and artifacts" (11:04).
- pm-tool-connectivity: adapters for Sentry, Linear, GitHub and Vercel (show notes intro).

## Key points
- Architecture (per chapter titles): runs, tasks, tools and artifacts (11:04); code map and file layout (15:08); code walkthrough (16:51); live investigation result (19:18); "How to build your own harness" (21:01).
- Model inside the harness: Claude Sonnet 4.6; models used to build it: Claude Opus and GPT-5.5 via Codex (tools referenced).
- Stated outcome: no longer typing "dear agent, please fix this bug" (subtitle); the harness does evidence gathering, root-cause analysis and follow-up artifacts.
- Episode length about 25 minutes (video duration 1,476 s in post metadata).

## Could not verify
- No transcript was available; this note works from the show notes, chapter list and tools list only. The "three components every harness needs" are not named in the notes, nor the build-vs-use criteria, nor how permissions are encoded. Retrieve the transcript (YouTube id ofS-4RRw9zw) to fill these.
- The live investigation result is not described in the notes, so whether the harness found the right root cause is unknown.
- ChatPRD is Vo's own company; claims about its workflow are first-party for ChatPRD but one person's demo.
