---
title: "How to build your own AI developer tools with Claude Code | CJ Hess (Tenex)"
source_url: https://www.lennysnewsletter.com/p/how-to-build-your-own-ai-developer
author: Claire Vo (host), CJ Hess (software engineer, Tenex)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-02-09
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [product-artifact-primitives, docs-as-code-prd, spec-becomes-prototype-and-evals, human-review-gates, harness-over-model, skill-standards]
relevance: medium
---

## Relevance to the project
An engineer shows Flowy, a tool he built almost entirely by prompting, that renders agent-written JSON files as editable flowcharts, timing diagrams and wireframe-level UI mockups; edits in the visual editor save back to the JSON so the agent reads the human's changes. It is a concrete example of a harness rendering a planning artifact in a human-friendly form while keeping an agent-friendly substrate, and of diagrams plus mockups standing in for the written plan before "just build it". He also uses a second model (Codex) to review Claude's diff against the plan artifacts. Bears on artifact-and-project-structure (typed, renderable plan artifacts), agent-interface (artifact rendering and review UI) and review-and-autonomy. Developer workflow, not PM.

## Themes
- product-artifact-primitives: Flowy reads a `.flowy` folder of JSON (nodes, edges, shapes, styles, icons, a semantic color system); the editor writes changes back so "Claude can just read the file" (10:44, 21:40). "I want to see it visually and Claude wants to see it as Markdown so we can kind of speak in our own way" (30:26).
- docs-as-code-prd: plans live in a `.plans` folder as Markdown, iterated "having one file where you're just working through the plan, reviewing the plan" until confident to let it write code (7:06).
- spec-becomes-prototype-and-evals: after generating a user-flow diagram, an animation-timing diagram and mockups, he skips plan mode: "based on the flow charts and the mockups, build this feature"; the artifacts "almost serve as the plan" (33:31, 36:32). The host notes she is "increasingly blind to code and Markdown" and can approve a diagram faster than a text plan (28:34-30:05).
- human-review-gates: model-to-model review: Codex reviews the git diff on four questions (does the code reflect the plan and diagram artifacts; code smells; how would you refactor; what would you do differently); it caught a mismatch between the mockup's pointer landing and the built wheel (36:51-42:22). "At this point, I feel like I'm mostly a QA person" (37:06).
- harness-over-model: "I'd honestly argue GPT 5.2 is a smarter model. But working with Claude is just such a delight in Claude Code"; what he values is the harness and "intent understanding" (3:32).
- skill-standards: three skills (overview, flowcharts, UI mockups), refined by asking Claude after each failure "give me a suggestion on how to improve this skill so this doesn't happen again"; every Flowy plan includes updating docs and related skills, so skills are "living documentation ... docs for people and ... docs for agents" (12:17, 21:40, 23:21). He uses a meta-skill for writing skills and prefers a "pre-flight" section (23:21).

## Key points
- Flowy was his first "Ralph loop" experiment, built in an afternoon, with some cleanup (9:09, 33:15). He plans to release it with its skills.
- Runs Claude Code with permissions bypassed most of the time via a shell alias, relying on Git rules so "if I do something horrible, it's okay"; still does some PRs by hand and uses skills for pre-flight checks (16:34).
- Uses three to five Explore subagents in parallel to gather context in larger code bases (18:59).
- The host frames build-vs-buy as flipped for dev tools: "of course we should build this until we hit some constraint" (14:10).
- Limitation he notes: shapes in the mockup constrain the shapes built in the UI (34:27).

## Notable quotes
- "I want to see it visually and Claude wants to see it as Markdown so we can kind of speak in our own way." (30:26)
- "there's docs for people and there's docs for agents and those just end up being skills" (23:21)
- "At this point, I feel like I'm mostly a QA person." (37:06)

## Could not verify
- Whole transcript read. One engineer's personal workflow on a small demo app; no team or production evidence. Claims about model quality are his opinion.
