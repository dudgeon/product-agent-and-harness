---
title: "\"I haven't written a single line of front-end code in 3 months\": How Notion's design team uses Claude Code to prototype"
source_url: https://www.lennysnewsletter.com/p/i-havent-written-a-single-line-of
author: Claire Vo (host), Brian Lovin (designer, Notion AI)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-02-23
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [prototyping-agents-limits, spec-becomes-prototype-and-evals, docs-as-code-prd, skills-marketplace, enablement-by-product, non-engineer-builders, pm-tool-connectivity, human-review-gates]
relevance: high
---

## Relevance to the project
A first-party, demoed account of a team-shared prototyping harness at Notion: one Next.js repo where each designer or PM has a namespaced folder, a shared CLAUDE.md plus a per-person uncommitted CLAUDE.local.md, slash commands and skills that wrap onboarding, Figma-to-code with a verification loop, and a deploy command that babysits CI. It shows how a team packages harness know-how so non-engineers can use a coding agent, and it argues that AI products cannot be designed in static tools because the "golden path" mock never survives a real model. Bears on capability-distribution-trust (team-level commands and skills in a repo), artifact-and-project-structure (files on disk, no backend), adoption-model and the "prototype as spec" option in intent-shaping-and-spec. Adoption is honest: about 5-10 heavy users.

## Themes
- prototyping-agents-limits: Figma-to-code via the Figma MCP gets "60%" by default; a slash command plus a browser verification loop with a second MCP (Chrome DevTools/Playwright) gets "80% correct 80% of the time" (24:42-24:56). MCP is "very context inefficient ... blows up your context window, but it's the best we have" (26:13). The agent hallucinated that CI checks passed (40:29).
- spec-becomes-prototype-and-evals: for Notion AI he used to design chat conversations as golden paths in Figma; engineers built them and "it just doesn't work that way" (42:39-44:13). The playground exists to connect to real models and design for errors, long thinking times, and follow-up questions.
- docs-as-code-prd: "there's no back end for prototype playground. It's just all files on disk" with a metadata file per prototype collated into the index page (10:57).
- skills-marketplace: team capabilities live in the repo as slash commands (create-prototype, figma, deploy) and skills (find-icon with a bundled TypeScript script over about 5,000 icon files) (20:30-35:03). Commands include an install check that teaches the user how to set up the MCP if it is missing (23:10).
- enablement-by-product / non-engineer-builders: the deploy command checks prerequisites (GitHub CLI, auth), creates a branch instead of pushing to main, opens the PR in the browser, then polls CI every 30-60 seconds and fixes failures itself (35:03-39:35). Goal: lower intimidation "but also not dumbed down" so people absorb Git concepts (34:49).
- human-review-gates: prototypes are "YOLO merge" with no code review; the main risk was one PR breaking someone else's prototype, fixed by a rule in CLAUDE.local.md (40:29).
- pm-tool-connectivity: slash commands force-invoke a specific MCP and tool set, which the host notes solves tool-name collisions across SaaS MCPs ("everybody has the concept of projects") (25:07).

## Key points
- Origin: he built it with one engineer; operationally just a Vercel project and a few approvals (8:12). Before it, designers each had their own Next.js repo and rebuilt Notion-looking components from scratch (6:18).
- Shared components, colors, typography, icons and templates (for example a Notion sidebar) make prototypes "close enough" to Notion quickly (6:18).
- Adoption: "Prototype Playground is still really for me"; about "five to 10 people at Notion that use it quite a lot"; others tried it and it did not stick, or prefer Figma, their own stack, v0, Lovable or Figma Make. He added links to external prototypes so the playground can index any tool (9:06). Most daily users had some technical background (10:38).
- Context layering: a committed CLAUDE.md at repo root (tooling: Bun, Tailwind; project structure) and a generated, uncommitted CLAUDE.local.md per machine (username, my directory, "don't mess with other people's files") (15:58).
- Workflow: voice dictation (Monologue) into Claude Code in plan mode; "the key thing about using plan mode is to actually read the plan", which favors people with a development background (13:18).
- His rule: "When Claude asks you to do something, teach it to do that thing itself", for example self-linting and opening the browser to check its own work (17:53-20:17).
- Commands work better with examples of success (sample code) than with instructions alone (21:39).
- He still spends 60-70% of his time in Figma; code prototyping is for AI features and interaction feel (42:39).
- Designers must keep relearning model capabilities every month; it "feels like a waste of time" but is necessary to design at the edge of what the model can do (44:13-45:48).
- Output quality tracks the quality of the human's input; when tired, his prompts make no sense (49:00).

## Notable quotes
- "you want your designs to encounter reality as early as possible" (3:09)
- "When Claude asks you to do something, teach it to do that thing itself" (show notes; demonstrated 17:53)
- "i don't think you can design a good chat experience in figma" (42:39)
- "we pretty much just YOLO merge" (40:29)

## Could not verify
- Whole transcript read. The 60% and 80% figures are his own estimates, not measured. The number of users is approximate. The episode title's "3 months" claim is not discussed in the transcript.
- No evidence that the prototypes feed engineering specs or production code; they are for exploration and sharing.
