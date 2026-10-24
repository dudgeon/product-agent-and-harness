---
title: About agent skills (GitHub Copilot docs)
source_url: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
author: GitHub
publisher: docs.github.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, harness-portability]
relevance: medium
---

## Relevance to the project
Copilot reads skills from `.github/skills`, `.claude/skills` and `.agents/skills`: it deliberately honours Claude's directory, which makes a repo-committed skill reusable across Claude Code, Codex and Copilot. But support varies by surface.

## Themes
- harness-portability: project skills in `.github/skills`, `.claude/skills`, `.agents/skills`; personal in `~/.copilot/skills` or `~/.agents/skills`; surfaces: Copilot app, CLI, cloud agent and code review, agent mode in VS Code/Visual Studio/JetBrains. "Supported locations depend on the surface"; do not assume a personal skill is available to the cloud agent.
- skill-standards: page does not cover org/enterprise-level skills.

## Could not verify
- Org-level Copilot skills or custom-agent distribution (the separate custom agents `.agent.md` format in `.github/agents/`, with org/enterprise scope via `.github-private`, was only seen in search snippets).
