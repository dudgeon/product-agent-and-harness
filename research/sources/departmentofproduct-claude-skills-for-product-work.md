---
title: What are Claude Skills and how can you use them for product-related work?
source_url: https://departmentofproduct.substack.com/p/what-are-claude-skills-and-how-can
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-10-21
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [skill-standards, single-agent-many-skills, opportunity-to-code-chain, prd-agents, artifact-standardization, agent-failure-modes]
relevance: medium
---

## Relevance to the project
The publication's PM primer on Agent Skills: what a SKILL.md is, progressive disclosure, how Skills differ from MCP, and three PM worked examples (a SaaS metrics workbook via the Excel skill, a branded strategy presentation by chaining a custom brand skill with the PowerPoint skill, and Notion's vendor "Spec to Implementation" skill turning a mock spec into a plan plus 42 Notion tasks). For the project it is evidence of how skills are being taught to PMs and of an early vendor-shipped skill that spans spec to tracked tasks, with the author noting it assumes the whole cycle lives in Notion rather than Jira or Linear. Mostly explainer material already covered by first-party notes, so medium rather than the triage guess of high.

## Themes
- skill-standards: says Anthropic made Skills an open standard; three layers of a SKILL.md (frontmatter, body, referenced files) with progressive disclosure. Matches [Anthropic engineering on Agent Skills](anthropic-engineering-equipping-agents-agent-skills.md) and the [agentskills.io spec](agentskills-specification.md).
- single-agent-many-skills: Claude picks skills automatically from the request; skills "stack"; name the skill in the prompt only when two similar skills might conflict.
- opportunity-to-code-chain: Notion's Spec to Implementation skill: eight steps from finding and reading the spec, through a plan page and tasks in the task database, to status and progress updates as Claude Code implements.
- prd-agents: the 42-task backlog with acceptance criteria and implementation detail generated from one spec in about ten minutes.
- artifact-standardization: brand-guidelines skill (rewritten from Anthropic's template with DoP colours and fonts) used to make decks match house style; the Excel skill enforces zero formula errors and financial-model formatting conventions.
- agent-failure-modes: the branded deck used Georgia instead of the specified Crimson Text body font, which the author guesses is because the font was not installed.

## Key points
- **Skills vs MCP:** MCP connects models to tools and data; Skills are task-focused packages for repeatable workflows; the two combine. Quotes Simon Willison that skills may be "bigger than MCP" (second-hand).
- **Pre-built vs custom:** pptx, xlsx, docx and pdf skills run without toggling; custom skills are uploaded as a zip in settings. Anthropic's skill-creator skill can scaffold new ones.
- **Notion skills (vendor):** Meeting Intelligence, Research and Documentation, Knowledge Capture, Spec to Implementation; the zip includes evaluations, examples and references folders beside SKILL.md.
- **Skills directory:** mentions Anthropic's December 2025 directory with partner skills from Notion, Figma, Atlassian and others, and an internal-comms skill.
- **Predicts** Jira and Linear will ship official skills, changing spec-to-code workflows.

## Notable quotes
- "Building a skill for an agent is like putting together an onboarding guide for a new hire" (Anthropic, as quoted)

## Could not verify
- The post is dated 21 October 2025 but describes a December 2025 Skills directory, so it was edited after publication; the edit date is not shown.
- Notion's skills release and Brad Abrams' and MJ Felix's comments were not checked at source. No primary note on Notion's Claude skills is filed.
