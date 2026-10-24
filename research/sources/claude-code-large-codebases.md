---
title: "How Claude Code works in large codebases: Best practices and where to start"
source_url: https://claude.com/resources/articles/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-14
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [harness-over-model, compounding-context-repo, skills-marketplace, legible-org-for-agents, enterprise-admin-controls]
relevance: high
---

## Relevance to the project
Anthropic's Applied AI team lays out the harness as five ordered extension points (CLAUDE.md, hooks, skills, plugins, MCP, plus LSP and subagents) and argues the harness determines performance "more than the model alone". Two points bear directly on harness upkeep and ownership: configuration should be reviewed every 3-6 months because instructions written for one model can constrain the next, and successful rollouts had a named owner (a DRI, a devex team, or an emerging hybrid PM/engineer "agent manager" role). It also gives regulated-industry starting governance (approved skills, required review, limited initial access) and is aimed at engineering, not PM, codebases. First-party guidance from observed deployments, with anonymized examples and no metrics.

## Themes
- harness-over-model: "the harness—determines how Claude Code performs more than the model alone" (section "The harness matters as much as the model").
- compounding-context-repo: lean, layered CLAUDE.md files; stop hooks proposing CLAUDE.md updates from each session; root codebase maps (section "Making the codebase navigable at scale").
- skills-marketplace: plugins bundle skills, hooks and MCP configs; updates distributed via managed marketplaces so setups don't "stay tribal" (extension-point list and table).
- legible-org-for-agents: upfront investment in making the codebase legible; path-scoped skills; committed permissions.deny rules (navigability section).
- enterprise-admin-controls: governance questions in regulated orgs; start with approved skills, required review, limited access, and cross-functional working groups with infosec (ownership section).

## Key points
- **Agentic search, not RAG**: Claude Code reads the live file tree (grep, references) with no index; Anthropic argues embedding indexes go stale at scale; tradeoff is it needs starting context to know where to look.
- **Build order matters**: CLAUDE.md first; hooks for self-improvement and deterministic checks; skills via progressive disclosure, optionally path-scoped (e.g. payments deployment skill bound to its directory); plugins to distribute; LSP for symbol-level navigation (one enterprise deployed LSP org-wide before rollout for C/C++); MCP last ("building MCP connections before the basics are working" is listed as a common mistake); read-only subagents to map a subsystem before editing.
- **Non-engineer example**: a large retailer built a skill linking Claude to an internal analytics platform for business analysts and shipped it as a plugin before broad rollout.
- **Harness decay**: rules for earlier models (e.g. single-file refactors) can block newer ones; a Perforce hook became redundant when native support shipped; review config every 3-6 months or after major model releases.
- **Ownership**: fastest rollouts had infrastructure ready before access; owners usually sit in devex/dev productivity; "agent manager" named as an emerging hybrid PM/engineer role; minimum is one DRI over settings, permissions policy, plugin marketplace and CLAUDE.md conventions. Bottom-up adoption "can fragment" without someone centralizing.
- **Limits stated**: assumes git, engineer contributors and conventional layouts; non-engineers contributing to the codebase "require additional configuration work"; very large or non-git estates deferred to future posts. No outcome numbers.

## Notable quotes
- "An emerging role in several organizations is an agent manager: a hybrid PM/engineer function dedicated to managing the Claude Code ecosystem."
- "Without that work, knowledge will stay tribal and adoption will plateau."

## Could not verify
- Which customers the anonymized examples refer to; no evidence offered for the claim that harness outweighs model.
