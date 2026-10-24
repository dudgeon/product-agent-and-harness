---
title: "A guide to AI prototyping for product managers"
source_url: https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product
author: Colin Matthews (guest author), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2025-01-07
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [prototyping-agents-limits, non-engineer-builders, spec-becomes-prototype-and-evals, prd-agents]
relevance: medium
---

## Relevance to the project
An early (January 2025) and widely read how-to that framed AI prototyping as a PM skill: a three-way tool taxonomy (chatbots, cloud dev environments, local IDE assistants), a "which tool when" guide, prompt templates including "PRD to prototype", and four debugging tactics for non-coders. It is useful as a baseline for how fast the prototyping layer has moved and for the limits it names (hosting, lost context, debugging). It is thin on harness or workflow design beyond single-tool prompting, so downgraded from the triage call of high to medium. Bears on prototyping as a step inside intent shaping, and on the "prototype as spec" option.

## Themes
- prototyping-agents-limits: limits named: Claude Artifacts could not be edited directly (prompt-only changes); Bolt ran server code in the browser so could not natively support logins, multi-user state, payments or persistence without Supabase; Lovable had no code editor, so the author moved to Cursor to debug; tools "rewrite entire sections of your prototype and you lose hours of work" when instructions are vague ("Choosing your tooling", "Lost context"). A presentation app with auth, database and real-time features took about 10 days, "most of that time was spent resolving bugs".
- non-engineer-builders: core promise is building "with no coding ability"; a 2-D tank game in 10 minutes from six prompts; an Airbnb-style price filter from a screenshot in under 10 minutes; personal internal tools (MP4-to-GIF converter, Substack image resizer) used weekly (intro, "Building your prototype").
- spec-becomes-prototype-and-evals: "turn your PRD into a working prototype in minutes"; template #5 pastes a PRD into Bolt with "Follow the exact specifications in the document"; prototypes put in customers' hands to get feedback before building ("Building a prototype from scratch").
- prd-agents: a PRD here is input to a prototyping agent rather than a document for humans only (template #5); planning before coding ("Reflection": "Start by detailing out the minimum requirements. Do not write any code.").

## Key points
- Taxonomy and picks (as of January 2025): chatbots (ChatGPT, Claude Artifacts) for one-page prototypes; cloud dev environments for multi-page or designed prototypes: v0 for good default design (Next.js, shadcn), Bolt for quick flexible prototypes, Replit for internal tools and data apps (full stack, Python), Lovable for production-bound apps with GitHub and Supabase integrations; local assistants (Copilot, Cursor, Windsurf, Zed) for people who code. Copilot recreated existing components when given vague instructions where Cursor edited existing files.
- Two PM use cases: design to functional prototype (screenshot plus "Match it exactly") and idea to prototype from public design systems.
- Six prompt templates: Figma to prototype (Bolt), from scratch (v0), data dashboard with Python/Streamlit (Replit), sketch to prototype (v0), PRD to prototype (Bolt), personal productivity tool (Replit).
- Four tactics for non-coders: reflection (plan first, and ask for possible causes of an error instead of a fix), batching (smallest working iteration first, data model first; more context up front is worse), be specific (like briefing a junior engineer), and avoid lost context (checkpoints and rollback, scope each change).

## Notable quotes
- "Most people think that providing the most context up front will help the AI make the right decisions, but the opposite is true." ("Batching")
- "AI prototyping tools have been available for less than six months and have already absolutely changed the speed at which teams can ship." ("Building a prototype from scratch")

## Could not verify
- Read in full (subscriber-only post, paid text). Screenshots and linked example prototypes not viewed.
- Tool capabilities are as of January 2025 and are now dated (for example, Artifacts and Lovable editing, Bolt hosting); do not cite them as current.
- Author teaches a paid course on the subject; the post promotes it.
