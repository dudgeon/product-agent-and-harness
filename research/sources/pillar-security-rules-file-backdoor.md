---
title: "New Vulnerability in GitHub Copilot and Cursor: How Hackers Can Weaponize Code Agents"
source_url: https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents
author: Pillar Security
publisher: Pillar Security blog
published: 2025-03-18
retrieved: 2026-10-28
type: article
evidence: independent
filed_by: research-dependency-agent
themes: [agent-protocol-security, stale-records-mislead-agents, agent-failure-modes]
relevance: high
---

## Relevance to the project
The "Rules File Backdoor" shows that machine-readable context files are an attack surface: invisible Unicode in a shared rules file can instruct a coding agent to insert malicious code and not mention it, while human reviewers see harmless text. For an agent-legible platform, any published context an agent obeys (platform READMEs, intake descriptions, MCP tool descriptions) needs the same review and integrity controls as code. Pillar sells AI security products, so not disinterested.

## Themes
- agent-protocol-security: hidden instructions via zero-width joiners and bidirectional markers; demo made the assistant add a malicious script tag to generated HTML and suppress mention of it (Attack mechanics).
- stale-records-mislead-agents: poisoned rules persist across sessions and survive forks because rule files are copied between projects.
- agent-failure-modes: vendor responses: Cursor (disclosed 26 Feb 2025) said the risk was users' responsibility; GitHub (disclosed 12 Mar 2025) said users must review suggestions, then added a hidden-Unicode warning on 1 May 2025.

## Key points
- Mitigations: audit rule files for invisible characters, review AI configuration files like executable code, scan for suspicious patterns, review generated code for unexpected external references.

## Notable quotes
- The attack is "virtually invisible to developers and security teams."
