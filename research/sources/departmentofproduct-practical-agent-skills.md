---
title: Practical Agent Skills for Product Teams
source_url: https://departmentofproduct.substack.com/p/practical-agent-skills-for-product
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-07-07
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [skill-standards, skills-marketplace, skill-supply-chain-security, single-agent-many-skills, opportunity-to-code-chain, status-update-agents, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
A curated shortlist of ten third-party skills that PMs can drop into Claude Code, read in full through a paid subscription, which shows what "skills for PM work" looks like in practice in mid-2026: mostly open GitHub repos from individuals and small studios, plus one official vendor skill (Atlassian). It is evidence for the "general harness plus skills" option and for the discovery problem a marketplace would solve (the post cites an estimate of 40,000 to 100,000 published skills). It is also an unflagged example of the supply-chain risk: readers are told to download a bundled folder of skills from many repos, with no mention of review, pinning or scanning. The company facts it cites (Anthropic, Pinterest, Ramp) are second-hand.

## Themes
- skill-standards: recaps SKILL.md as three layers (header for selection, body of instructions, referenced files loaded on demand), i.e. progressive disclosure; skills are auto-selected without explicit invocation (section "What are agent skills again?").
- skills-marketplace: opens with the claim of 40k to 100k published skills (attributed to a Perplexity estimate) and says finding the useful ones is "increasingly difficult"; the post itself acts as a hand-curated catalogue.
- skill-supply-chain-security: offers one download bundling skills from ten different repos (one of them a 1,000+ skill collection) with no security caveat; contrast [Snyk's audit](snyk-toxicskills-study.md) and [ClawHavoc](thehackernews-clawhavoc-341-malicious-skills.md).
- single-agent-many-skills: gstack (Garry Tan) and the compound-engineering plugin (Every) are families of slash-command skills that act "like a small virtual team" in one harness, each stage writing a durable file (DESIGN.md, requirements doc, plan) that the next stage reads (sections 4 and 6).
- opportunity-to-code-chain: compound engineering splits brainstorm (what) from plan (how) from work (execute), with an artifact between each; Atlassian's official skill turns a Confluence spec into a Jira epic and tickets, showing the breakdown for approval first (sections 6 and 10).
- status-update-agents: a skill that drafts internal comms in four formats (newsletter, status report, leadership update, etc.) (section 8).
- vendor-claims-vs-independent-evidence: repeats "Anthropic's reporting tool went from 21% to 95% accuracy with skills" with no source detail.

## Key points
- Intro: cites Anthropic (reporting accuracy 21% to 95%), Pinterest (automated testing) and Ramp (Glass, an internal library of shareable skills; see [Ramp's own post](ramp-introducing-glass.md)) as adopters. All second-hand.
- The ten skills, by job: idea refinement with built-in frameworks (SCAMPER, HMW, first principles, JTBD, constraint-based ideation, pre-mortem, analogy) from Addy Osmani's repo; editable consulting-style charts plus a "critic" skill that reviews a finished deck; a nine-dimension competitor benchmark with a tension quadrant; a design-consultation skill (gstack) that interviews the user, optionally researches and screenshots competitors, brings in second opinions from another model and another Claude persona, and writes DESIGN.md; a pricing-page generator that reads DESIGN.md; compound engineering's planning skill; obra/superpowers' brainstorming skill (one question at a time, two or three approaches with trade-offs, browser wireframes, then a written spec the user must review); an internal-comms skill; single-file animated HTML decks; Atlassian's spec-to-backlog skill (needs the Atlassian MCP connection).
- Recurring design patterns worth noting: skills check for an existing artifact before overwriting; they ask one consolidated question rather than a wizard; they present disagreements between perspectives as choices for the human; they end with a file, not a chat summary, and ask for review of it.
- The worked competitor-benchmark example shows the skill noticing a domain mismatch (it was built for creative studios) and adapting the test case, an honest illustration of skills being narrower than their names suggest.
- A download folder bundles all ten with example outputs, tested in Claude Code.

## Notable quotes
- "navigating them all to find the ones that are actually useful is becoming increasingly difficult."

## Could not verify
- The 21% to 95% Anthropic figure and the 40k to 100k skill count; no primary source is linked in the text.
- Screenshots and the download folder were not inspected; summarised from the post text only.
