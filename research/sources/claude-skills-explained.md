---
title: "Skills explained: How Skills compares to prompts, Projects, MCP, and subagents"
source_url: https://claude.com/resources/articles/skills-explained
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-03-05
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [skill-standards, single-agent-many-skills, task-context-isolation, pm-tool-connectivity, compounding-context-repo]
relevance: medium
---

## Relevance to the project
Anthropic's own division of labour between five building blocks (prompts for the moment, Projects for background knowledge, Skills for procedure, MCP for connectivity, subagents for isolated delegation) is a usable vocabulary for the capability-format and context dimensions. Its worked example is a PM-adjacent competitive-intelligence research agent assembled from all five. It is an explainer with no evidence of outcomes and no discussion of failure, trigger misfires or governance.

## Themes
- skill-standards: skills are folders of instructions, scripts and resources with progressive disclosure: metadata about 100 tokens, full instructions under 5k tokens, bundled files only as needed ("What are Skills?").
- single-agent-many-skills: "Skills vs. subagents": put shared expertise in a skill any agent can load rather than baking it into individual subagents; subagents can use skills.
- task-context-isolation: subagents have their own context window, system prompt and tool permissions; example read-only code-reviewer subagent (Read, Grep, Glob, no Write/Edit).
- pm-tool-connectivity: "MCP connects Claude to data; Skills teach Claude what to do with that data" ("What is MCP?").
- compounding-context-repo: heuristics for promotion: a prompt typed repeatedly should become a skill; instructions copied across Projects should become a skill.

## Key points
- Comparison table (section "Comparison: choosing the right tool"): Skills = procedural knowledge, persist across conversations, load dynamically, can include code; Prompts = moment-to-moment, single conversation; Projects = background knowledge, always loaded within the project, no code; Subagents = task delegation, full agent logic, load when invoked; MCP = tool connectivity, always available.
- Projects: 200K context window per project; when knowledge nears the limit, Claude switches to RAG mode to expand capacity "by up to 10x" (Anthropic's figure). Shared projects on Team and Enterprise plans.
- Worked example (section "Example agentic workflow: research agent"): a "Competitive Intelligence" Project with reports, competitor docs, CRM feedback; MCP for Google Drive, GitHub, web search; a skill encoding the company's Drive folder layout, naming conventions (`_FINAL`, `_DRAFT`) and "source of truth" rules; two subagents (market-researcher with Read/Grep/web search; technical-analyst with Read/Bash/Grep). Note the example labelled "competitive-analysis skill" is actually a Drive-navigation skill: an org-legibility skill, not an analysis framework.
- One-line framing: Projects say what you need to know, Skills say how to do things.
- Distribution: Claude.ai users enable Skills in settings; Claude Code users install via plugin marketplaces; API has a Skills endpoint.
- Missing: no guidance on who authors or reviews skills, versioning, trigger reliability, security of third-party skills, or cost.

## Notable quotes
- "MCP connects Claude to data; Skills teach Claude what to do with that data." ("What is MCP?")

## Could not verify
- The RAG "up to 10x" capacity figure; no method given.
