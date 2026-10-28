---
title: "GitHub MCP Exploited: Accessing private repositories via MCP"
source_url: https://invariantlabs.ai/blog/mcp-github-vulnerability
author: Marco Milanta, Luca Beurer-Kellner (Invariant Labs)
publisher: Invariant Labs blog
published: 2025-05-26
retrieved: 2026-10-26
type: article
evidence: independent
filed_by: research-shared-persistent-agents
themes: [identity-delegation, agent-protocol-security, task-context-isolation, agent-failure-modes]
relevance: high
---
## Relevance to the project
A concrete, reproduced case of an agent acting with one person's full authority on instructions written by someone else: a malicious issue in a public repo hijacks a developer's agent, which uses the developer's GitHub access to copy private-repo data into a public PR. For shared, persistent agents that read shared inputs (issues, channels, threads), this is the core identity failure: whoever can write into the agent's input stream can borrow its principal's authority. Independent security research (Invariant sells guardrail products, so not disinterested).

## Themes
- identity-delegation: the agent acts through the user's connected GitHub account; the attacker never holds a credential, only writes an issue (attack walkthrough, 2025-05-26)
- task-context-isolation: proposed mitigation is a policy restricting the agent to one repository per session, blocking cross-repo flows even when the token could reach both (Mitigations)
- agent-protocol-security: "this is not a flaw in the GitHub MCP server code itself"; it is "a fundamental architectural issue that must be addressed at the agent system level" (Why it's architectural)
- agent-failure-modes: users who choose "Always Allow" on tool confirmations remove the remaining human check (attack setup)

## Key points
- Steps: public repo open to issues; attacker files an issue with injected instructions; user asks the agent to look at open issues; agent reads private repos and opens a PR on the public repo containing the data (demo leaked project names, relocation plans, salary).
- Model alignment alone was insufficient: the demo used Claude 4 Opus.
- Recommends least-privilege permissions and continuous monitoring (Invariant's own MCP-scan, a vendor product).

## Notable quotes
- "a fundamental architectural issue that must be addressed at the agent system level"

## Could not verify
- Whether GitHub changed the MCP server or token scoping afterwards.
