---
title: "HTML is the new Markdown: How Anthropic engineers are building with Claude Code | Thariq Shihipar (How I AI)"
source_url: https://www.lennysnewsletter.com/p/html-is-the-new-markdown-how-anthropic
author: Claire Vo (host), Thariq Shihipar (engineer, Claude Code team, Anthropic)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-05-18
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [artifact-standardization, agent-ready-intent, docs-as-code-prd, product-artifact-primitives, human-review-gates]
relevance: medium
---

## Relevance to the project
An Anthropic Claude Code engineer argues that HTML, not Markdown, should be the format of agent plans and specs, because richer visual artifacts get more human engagement and so better review. The episode description lists interactive HTML plans, throwaway micro-UIs built to edit one part of a plan, a living HTML design system kept in the repo, comments and annotations on HTML plans, and the claim that "99% of your AI-generated tokens should go to planning, interfaces, and communication—not production code". This bears on intent-shaping-and-spec (what format the handoff spec takes and how humans review it) and artifact-and-project-structure. Only the show notes were available, so it is filed at medium.

## Themes
- artifact-standardization: HTML proposed as the default format for agent communication and planning, replacing Markdown (02:39); a living design system in HTML "lives in your repo and travels with every project" (26:39).
- agent-ready-intent / docs-as-code-prd: brainstorm in HTML, then turn the brainstorm into a full implementation plan, then use "plans as artifacts for implementation" (06:48, 09:24, 25:39); a chapter on "the future of PRDs and tech specs" (13:50).
- human-review-gates: the stated reason for HTML is engagement: richer formats "lead to better human engagement—and, ultimately, better products"; "complexity has to earn its keep" and HTML helps you "stay in the loop without over-constraining Claude" (description; 11:20).
- product-artifact-primitives: throwaway micro-UIs to edit specific parts of a plan; making HTML specs editable; adding comments and annotations to HTML plans (18:16, 24:17, 30:16).

## Key points
- The "compute allocator" mindset: the engineer allocates compute rather than writing code (04:30); the "abundance mindset" and Jevons paradox (20:23).
- Prompting philosophy: trust Claude but give it constraints; a technique that gives Claude flexibility while ensuring you get what you need (11:20).
- Just-in-time documentation and throwaway software (24:17).
- Filmed at Anthropic's Code with Claude event; tools referenced include Claude Code and Claude Design.

## Notable quotes
- "99% of your AI-generated tokens should go to planning, interfaces, and communication—not production code" (episode description)

## Could not verify
- **No transcript available**; this note is built from the episode description and chapter list only. None of the demos, numbers or specific prompts were checked.
- The 99% figure is a headline from the description; method and context unknown.
- Related: a separate note quotes Thariq on other topics (`claude-fable-finding-unknowns`).
