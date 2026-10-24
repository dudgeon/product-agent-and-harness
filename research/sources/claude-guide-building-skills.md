---
title: A complete guide to building skills for Claude
source_url: https://claude.com/resources/articles/complete-guide-to-building-skills-for-claude
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-01-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [skill-standards, single-agent-many-skills, evals-autonomy-trust, harness-portability, skills-marketplace]
relevance: medium
---

## Relevance to the project
Anthropic's own build manual for skills sets out the format, the three-level progressive-disclosure loading model, a three-tier testing approach and the distribution routes (individual upload, admin workspace-wide deploy, API, GitHub), which together define what a "capability" is for a Claude-based PM harness. It is the most concrete first-party source on how a team would author, test and ship skills for PMs, designers and analysts, including success criteria (trigger rate, tool calls, failed API calls). It openly admits that skill evaluation is partly "vibes-based" and that better measurement tooling is still being built, which bears on how a PM harness would evaluate its own capabilities. The guide is dated January 2026, so its distribution model may have moved on.

## Themes
- skill-standards: skill = folder with required `SKILL.md` (YAML frontmatter `name` + `description` under 1024 chars) plus optional `scripts/`, `references/`, `assets/`; Agent Skills published as an open standard "like MCP" (Fundamentals; Distribution and sharing, "An open standard").
- single-agent-many-skills: composability principle (Claude loads multiple skills at once; a skill must not assume it is alone) and the warning to review if more than 20-50 skills are enabled at once, with "skill packs" suggested (Fundamentals; Patterns and troubleshooting, "Large context issues").
- evals-autonomy-trust: three testing tiers (manual in Claude.ai, scripted in Claude Code, programmatic via the skills API) and three test kinds (triggering, functional, performance vs baseline); success targets are called "aspirational" and partly vibes-based (Planning and design, "Define success criteria"; Testing and iteration).
- harness-portability: skills claimed to work identically across Claude.ai, Claude Code and API given the dependencies; `compatibility` field for platform-specific skills (Fundamentals, "Portability"; Distribution, "An open standard").
- skills-marketplace: distribution via GitHub repo + README, partner skills directory (Asana, Atlassian, Canva, Figma, Sentry, Zapier), and admin workspace-wide deploy shipped 2025-12-18 (Distribution and sharing; Reference C).

## Key points
- **Format (Planning and design, Reference B).** Folder in kebab-case; `SKILL.md` exact spelling; no README inside the skill folder. Frontmatter: required `name`, `description` (must state what it does and when to use it, with trigger phrases); optional `license`, `compatibility` (1-500 chars, environment needs), `allowed-tools` (restricts tool access), `metadata` (author, version, mcp-server, tags).
- **Security restrictions in frontmatter.** No XML angle brackets, safe YAML parsing, names containing "claude"/"anthropic" reserved; the stated reason is that frontmatter lands in the system prompt and could inject instructions. This is the only security discussion; there is nothing on reviewing third-party skill scripts.
- **Progressive disclosure (Fundamentals).** Level 1 frontmatter always in the system prompt; level 2 SKILL.md body loaded when relevant; level 3 linked files read on demand. Keep SKILL.md under 5,000 words.
- **MCP + skills split.** MCP is connectivity ("what Claude can do"), skills are knowledge ("how Claude should do it"); the kitchen/recipe analogy. Pitched to MCP connector builders as a competitive edge over MCP-only connectors.
- **Three use-case categories Anthropic observed:** document and asset creation (e.g. frontend-design, docx/pptx/xlsx), workflow automation (e.g. skill-creator), MCP enhancement (e.g. Sentry's code-review skill).
- **Five patterns (Patterns and troubleshooting):** sequential workflow orchestration with rollback; multi-MCP coordination (worked example: Figma export, Drive storage, Linear tasks, Slack notification, i.e. a design-to-dev handoff); iterative refinement with validation scripts; context-aware tool selection; domain-specific intelligence (worked example: payment compliance check with audit trail before action).
- **Determinism advice.** For critical validations, bundle a script rather than rely on language instructions, since "code is deterministic; language interpretation isn't".
- **Testing (Testing and iteration).** Suggested targets: triggers on 90% of relevant queries (10-20 test queries), fewer tool calls and tokens vs baseline, zero failed API calls. Illustrative baseline comparison (15 messages / 12,000 tokens without vs 2 questions / 6,000 tokens with) is a made-up example, not measured data. Recommends iterating on one hard task until Claude succeeds, then extracting the approach into a skill.
- **skill-creator** generates and reviews skills (flags vague descriptions, over/under-triggering) but the guide states it "does not execute automated test suites or produce quantitative evaluation results".
- **Iteration signals:** under-triggering (users enabling it manually), over-triggering (users disabling it), execution issues (corrections needed); fixes are description edits, negative triggers, better instructions.
- **Distribution (as of January 2026):** individual upload in Claude.ai settings or the Claude Code skills directory; organisation-level admin deploy with automatic updates and central management (shipped 2025-12-18); API via `/v1/skills` and `container.skills` in the Messages API, requiring the Code Execution Tool beta; version control in the Claude Console.
- **Limits:** no data on real skill performance, no guidance on versioning conflicts, review/approval of skills inside an org, or supply-chain risk of scripts in skills.

## Notable quotes
- "Aim for rigor but accept that there will be an element of vibes-based assessment." (Planning and design)
- "Code is deterministic; language interpretation isn't." (Patterns and troubleshooting)

## Companion pages
- https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude (guide landing page and its seven chapters: introduction, fundamentals, planning-and-design, testing-and-iteration, distribution-and-sharing, patterns-and-troubleshooting, resources-and-references)

## Could not verify
- Whether the January 2026 distribution model (upload, admin deploy, API beta) is still current as of retrieval.
