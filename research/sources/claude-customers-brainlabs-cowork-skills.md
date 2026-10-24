---
title: "How Brainlabs gave 1k+ marketers at its media agency an AI coworker with Claude Cowork and skills"
source_url: https://claude.com/customers/brainlabs
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [skills-marketplace, skill-standards, non-engineer-builders, tacit-knowledge-capture, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
A roughly 1,000-person media agency rolled Cowork out in four weeks and its staff wrote about 400 skills, then had to build a skills auditor after the library "got unwieldy from over-enthusiastic agent creation", which is concrete evidence that skill sprawl arrives fast and needs ownership, review and usage analytics. The setup (Notion as the non-developer authoring home and source of truth, auto-pushed to GitHub, named owner approval per skill, Managed Agents fired by Notion board state) is a worked option for capability distribution and remote invocation. Anthropic customer story; adoption and quality figures are the customer's claims.

## Themes
- skills-marketplace: an open org-wide library of ~400 employee-authored skills in Notion, readable by anyone, plus a "suggest a skill" intake that bypasses engineering (section "An authoring layer for skills").
- skill-standards: an org-wide skills guideline, a designated owner who reviews and approves every change, and a Claude "skills auditor" that flags duplication, overlapping instructions and token inefficiency; the analytics API is used to see which skills are actually used (section "An authoring layer").
- non-engineer-builders: strategists, planners and creative leads author skills; Notion chosen because that audience already works there (section "The solution").
- tacit-knowledge-capture: an SEO audit skill "refined across thousands of iterations" on a context layer from a decade of agency work, so audit quality no longer depends on which strategist runs it (sections "An authoring layer", "The outcome").
- remote-agent-invocation: Managed Agents inside Notion fire when board items change state; a Notion agent tags complex tickets "Claude" and a managed "Get Stuff Done" agent picks them up using the skills library and Slack and Calendar connectors (section "An authoring layer").

## Key points
- Rule driving adoption: "If you're doing something more than three times, you should try to automate it" (CTO Ben Vincent); CEO Dan Gilbert wanted it company-wide; target was one week, actual four.
- Skill packaging: Notion packages each skill and pushes it to GitHub for revision; Notion stays the source of truth.
- Access model as stated: a skill only pulls what the running person is already authorised to access.
- Library hygiene arrived after "versions 2, 3, and 4 of the library got unwieldy"; consolidation and rewrites proposed by the auditor; growth to be guided "on the basis of evidence rather than enthusiasm."
- Writing: Cowork preloaded with the house style guide and each person's writing style; drafts said to come out "around 80% of the way there".
- Headline figures (customer claims): ~400 skills in four weeks, ~1,000 employees, 91% adoption in North America (definition not given).
- Next: evaluating the Agent SDK for server-side agents alongside Notion-hosted ones; "a bunch of agents hosted in a variety of places."
- Limits: no data on skill quality, error rates or how many of the 400 skills survive consolidation; review is described as owner approval, with no detail on testing.

## Notable quotes
- "We built it after versions 2, 3, and 4 of the library got unwieldy from over-enthusiastic agent creation across the company." (Ben Vincent, CTO)

## Could not verify
- Publication date; the 91% adoption figure's definition and denominator.
