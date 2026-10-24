---
title: How to use Claude Projects and Skills to Monitor your Product's Health
source_url: https://departmentofproduct.substack.com/p/how-to-use-claude-projects-and-skills
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-01-05
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [metrics-review-agents, product-artifact-primitives, project-taxonomy, scoped-governance-containers, status-update-agents]
relevance: medium
---

## Relevance to the project
A tutorial that uses Claude Projects (chat history, knowledge files, custom instructions) as a PM's container for a recurring product-health check across five dimensions, then uses Skills to turn the output into Excel and PowerPoint for leadership. Its most useful part for the project is the choice it lays out between one Project for everything and five owner-delegated sub-Projects feeding a "master" Project, and how the master is fed: by manually pasting summaries from each sub-Project. That is a clear, PM-taught example of the missing roll-up between project containers, and of filename prefixes standing in for structure. It bears on the artifact-and-project-structure and metrics-review questions.

## Themes
- metrics-review-agents: five health dimensions (user data fundamentals, value-proposition clarity, UX health, commercial health, strategic health) with traffic-light scoring and three output modes (quick check, deep dive, executive summary); recurring prompts for a weekly check, a cross-dimension diagnosis of a falling metric and a monthly executive report.
- product-artifact-primitives: a Project as the PM's standing container: name, description, custom instructions, knowledge files, chat history ("What is Claude Projects?"). See [Claude Help Center on Projects](anthropic-claude-projects-support.md).
- project-taxonomy: "Approach 2": one Project per dimension, owned by the relevant function (design owns UX health, commercial owns business health), plus a sixth master Project; the author notes this costs more to set up and maintain.
- scoped-governance-containers: delegation of each sub-Project to a different team is the stated reason for the multi-Project design, not context size alone.
- status-update-agents: the master Project's job is an executive-ready report under 500 words with leadership talking points.

## Key points
- **Single Project:** custom instructions set a "product health analyst" role, the five dimensions, scoring and output formats, plus slots for the org's definitions (what counts as an active user, strategic priorities, competitors, pricing). Files are categorised by a filename prefix per dimension; the author suggests using Claude Code to rename them.
- **Multi-Project:** each sub-Project gets its own instructions and files (the strategy one lists vision, roadmaps, board decks, past decisions and "what we said no to"). One stated reason is that a single Project "bloats the context window".
- **Roll-up is manual:** the master Project "can only give you the relevant information you need if you upload the summaries" from each sub-Project; the PM runs a summary prompt in each and pastes the five results into the master.
- **Skills for output:** the Excel and PowerPoint skills (and a brand-guidelines skill from the earlier Skills post, [note](departmentofproduct-claude-skills-for-product-work.md)) produce shareable artifacts.
- **Framing:** health checks as "institutional memory that survives team changes".
- Templates and prompts are given in full in the post; not reproduced here.

## Could not verify
- Whether Projects could reference each other directly at the time; the post implies not.
