---
title: How Vercel built an ecosystem on the open skills standard
source_url: https://claude.com/customers/vercel-qa
author: Anthropic (Q&A with Andrew Qu, Chief of Software, Vercel)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [skill-standards, skills-marketplace, single-agent-many-skills, non-engineer-builders, metrics-review-agents]
relevance: medium
---

## Relevance to the project
Vercel's Chief of Software describes running an internal data-science agent (d0) on roughly 100 skills, keeping internal skills in dedicated repos, and building skills.sh, a public registry and installer on Anthropic's open Skills spec, where some of the most popular skills are written by non-developers. For the project it is a practitioner view of the "one agent, many skills" pattern for analyst work and of skill distribution as editable local copies rather than locked packages, which bears on capability distribution and trust. Vercel is both a Claude customer and a vendor of the registry and an agent framework (eve), so claims are promotional and unmeasured ("anecdotally, it makes us move a lot faster").

## Themes
- skill-standards: skills.sh built on the open Skills spec; a Cloudflare-proposed `/.well-known/skills` URL-discovery convention was adopted into the `npx skills` installer and "move[d] up the official spec progression" (open standard answer).
- skills-marketplace: skills.sh installs give a local copy that users edit (e.g. swapping CSS guidance for Tailwind in Anthropic's front-end design skill); designed as "mutable knowledge" (LLMs authoring skills answer).
- single-agent-many-skills: d0, the internal data-science agent, runs on ~100 skills; descriptive names ("aggregating product metrics month over month") let Opus 4.8 route intent; no collisions yet, though Qu expects them (d0 answers).
- non-engineer-builders: a marketer who had never coded has two skills in the skills.sh top 100; legal, marketing and sales skills seen (surprises answer).
- metrics-review-agents: d0 answers Slack questions like total user growth via skills for aggregation, customer metrics, product metrics and time series (d0 answers).

## Key points
- **Deploy to Vercel skill** (Claude Code, Claude Desktop) turns work in Claude into a shareable deployed link, claimable into a Vercel account later; positioned as shortening idea to production.
- **First skill origin.** An engineer's performance "web bible"; docs felt too slow and an MCP server "too heavy for what was basically documentation", so it became a nested-directory skill (React best practices).
- **Internal use.** Migrations, on-call debugging and design-system matching encoded as skills in mini repos dedicated to internal agent skills. d0 went through sub-agent and file-system phases before settling on skills; "once we've done something accurately we can capture it".
- **Layering.** Vercel's Claude Code plugin bundles the Vercel MCP, library/platform skills and built-in subagents; Qu says MCP, skills and memory are complements, not replacements.
- **Obsolescence expectation.** Qu hopes many current skills become obsolete as models absorb best practices, with future skills composing these primitives into fuller experiences.
- **Agent anatomy (eve framework).** Four parts: tools, initial system instructions, skills, and channels (interfaces); skills are what people customise most.
- **Limits:** no metrics on d0 accuracy, skill quality or registry security; nothing on vetting third-party skills before install, despite the local-copy model; page undated.

## Notable quotes
- "We haven't hit a ceiling where there are so many skills that the agent reaches for the wrong one." (d0 answers)
- "Skills have opened up the door for non-technical people with a background in a specific field to contribute to the AI ecosystem." (surprises answer)

## Could not verify
- Publication date (page undated; mentions Opus 4.8).
- skills.sh popularity rankings and the non-developer author claim.
