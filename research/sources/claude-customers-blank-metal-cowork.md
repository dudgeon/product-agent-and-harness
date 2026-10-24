---
title: "How Blank Metal, a lean professional services firm, runs on Claude Cowork"
source_url: https://claude.com/customers/blank-metal-qa
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, skill-standards, artifact-standardization, enablement-by-product, build-vs-buy]
relevance: medium
---

## Relevance to the project
A 30-person AI-native consultancy (founded 2025, and itself an Anthropic services partner in effect) describes running operations on Cowork: a non-engineer CRO builds plugins, scheduled activities and projects, brand voice and visual guidelines are encoded as shared skills so decks and docs conform automatically, and a reusable-skill norm spreads every solved problem across the org. It is useful as a small-company pattern for skills-as-standards and for a task that graduated into a Cowork project after it started erroring. Evidence is an Anthropic customer Q&A with the firm's revenue lead, who also sells Claude implementation and training; time savings are their unaudited claims and the firm is not a regulated enterprise.

## Themes
- non-engineer-builders: the CRO built a lead-processor plugin (first pass about 20 minutes, about an hour across three versions) without looping in engineering ("Was there a specific moment").
- skill-standards: anything packaged as a reusable skill "gets shared across the org"; internal skills target friction points (first answer).
- artifact-standardization: brand voice and visual guidelines embedded as skills so decks, docs and deliverables align automatically rather than per person (first answer).
- enablement-by-product: about 710 people trained (as of June 1) using Lectern, an in-house live training companion run side by side with participants' terminals ("You've trained more than 700 people").
- build-vs-buy: the firm watches what comes "off the shelf from Claude" and customises only where needed; Cowork for internal work, Claude Code for ~90% of engineering, the API for client implementations ("How do you keep up").

## Key points
- **Lead processor plugin:** for 3-10 daily leads, it draws on all the firm's plugins and custom skills, scores fit, creates the deal in HubSpot, pulls contact info and posts a Slack summary; claimed to save "at least a couple of hours a day" across four people.
- **Scheduling automation:** one prompt cross-references a locked-down Microsoft calendar with Google Calendar, places holds, drafts availability text, then on client choice finalises the invite, adds Zoom and deletes other holds. Built first as a task; when it started erroring after a couple of weeks, Claude suggested converting it into a Cowork project, which the CRO did.
- **Other skills:** proposal/SOW first drafts, pre-call competitive research, and a post-call meeting processor skill.
- **Operating-layer argument:** connectors (Salesforce, Slack, M365), shareable skills and Excel/PowerPoint add-ins let the model work inside existing workflows rather than add a context switch.
- **Keeping up:** near-weekly Claude updates are tested on an internal Claude-powered platform called Shippy before rolling into training and builds.
- **Limits:** no error or quality data; the firm has a commercial interest in Claude adoption; small, young company with few legacy controls; no governance or review process described for the skills it shares.

## Notable quotes
- "I realized how much Claude could actually do without me needing to loop in engineering every time I had an idea." (Elli Rader, Chief Revenue Officer)

## Could not verify
- Publication date; what the "+700 people trained" includes (client staff vs internal).
