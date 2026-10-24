---
title: "The secret to better AI prototypes: Why Tinder's CPO starts with JSON, not design | Ravi Mehta"
source_url: https://www.lennysnewsletter.com/p/the-secret-to-better-ai-prototypes
author: Claire Vo (host), Ravi Mehta (product advisor; former CPO at Tinder, EIR at Reforge)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-09-29
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [prototyping-agents-limits, agent-ready-intent, one-job-per-agent, ai-synthesis-hallucination-risk, pm-tool-connectivity, spec-becomes-prototype-and-evals]
relevance: medium
---

## Relevance to the project
Mehta demonstrates "data-driven prototyping": instead of a prose spec or design images, the PM first has Claude generate a realistic JSON data set (with real photos via the Unsplash MCP), then gives that data to the prototyping tool with a one-line prompt. The point for this project is that the **data schema is a sharper intent artifact than a prose spec**: it codifies ambiguous parts of the idea "in a really concrete way", the way engineering does when it defines the schema that drives the front end. That bears on intent-shaping-and-spec (what form agent-ready intent takes) and work-structure (split the job into separate agent passes rather than one prompt that averages across UX, data and code). Mehta was a Reforge EIR and demos Reforge Build, so the tool choice is not neutral.

## Themes
- agent-ready-intent: three ways to give a prototyping tool context: spec-driven (detailed prompt), design-driven (images, Figma), and data-driven; engineering's first move is "here's the data schema that's actually going to drive the front end", which takes what is "ambiguous around designs or specs" and codifies it (3:49); Vo advises: "get your engineering to give your definition of your data schema and just copy and paste that in" as context for PRDs and prototyping tools (26:04).
- one-job-per-agent: a single prompt asks the tool to do UX, data structure and code at once, so "the output is kind of an average across those things, rather than really spiking each" (7:16); "you want individual agents with individual context working together in sequence" (18:27); better result attributed to "separation of concerns" (25:54).
- ai-synthesis-hallucination-risk: the spec-driven prototype hallucinated image URLs (broken links) and used a French Polynesia hotel photo for Paris (10:13-11:08); the Unsplash MCP returns real URLs instead (14:01).
- pm-tool-connectivity: Unsplash MCP installed via Smithery; Claude calls its search tool repeatedly while building the JSON (14:01, 16:27). Vo suggests pulling representative samples from production data via SQL MCPs (19:50).
- prototyping-agents-limits: realistic data matters for feedback: "users never" gloss over data; stakeholders and users need something that "looks and feels as it actually will be" (23:07); real data stress-tests edge cases like long profiles or badly cropped photos (19:50-21:20).
- spec-becomes-prototype-and-evals: the generated JSON is "a much more detailed spec, you know, in the form of data" (18:27).

## Key points
- Demo (5:23-33:02): a TripAdvisor-inspired multiplayer Paris itinerary. Spec-driven prompt ("Make it look nice") in Reforge Build produced 22 files with mock data but wrong or broken photos. Data-driven: a natural-language schema prompt to Claude (itinerary, 3-4 travelers with travel styles, 12-15 items with times, ratings, tags, photos, threaded notes) produced JSON; pasted into Build with "generate a trip itinerary feature based on the sample data below", yielding a cleaner prototype.
- Iteration: edit the sample data file directly (rename a traveler, swap a photo); ask Claude for "the same travelers going to Thailand" and swap the JSON; add a free-time-cards feature that works on any data set because functionality is not baked to the data (26:44-32:37).
- Workflow split: Mehta uses ChatGPT and Claude roughly 50-50, choosing Claude for human-sounding generated content (16:04).
- Writing the schema in natural language "helped me understand the feature a little bit better" (14:01): the data-first pass doubles as a thinking tool for the PM.
- Second half of the episode (34:34 onward) covers a subject-setting-style framework and film-stock cues for Midjourney images; not relevant here.

## Notable quotes
- "when you provide data in this way, the AI doesn't get fuzzy with it" (18:27).
- "As product builders, we're used to thinking about data separately from the UX ... but users never do" (23:07).

## Could not verify
- Transcript read 0:00-34:34 in full; the Midjourney segment (34:34-end) skimmed only.
- Quality comparisons are the host's and guest's judgment in a live demo; no user testing reported. Reforge Build is the guest's former employer's product.
