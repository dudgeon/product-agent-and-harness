---
title: Open a Jira work item in an AI coding tool
source_url: https://support.atlassian.com/jira-software-cloud/docs/open-a-jira-work-item-in-an-ai-coding-tool/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [opportunity-to-code-chain, harness-portability, pm-tool-connectivity]
relevance: medium
---

## Relevance to the project
This documents the handoff from a work item to a local coding agent: a deep link that pre-fills the agent's prompt. It is the simplest way intent moves from the PM's artifact to the coder's harness. The support page and the launch blog disagree on what context is passed, which matters for any claim about how much intent survives the handoff.

## Themes
- `opportunity-to-code-chain`: "Deep linking opens your Jira work item in your local coding tool and automatically passes the summary and description." (intro)
- `harness-portability`: supported desktop apps Codex, Cursor, GitHub Copilot, VS Code; terminal tools Claude Code and Rovo CLI (copy a pre-filled command) (Supported agentic coding tools).
- `pm-tool-connectivity`: connecting the Atlassian Rovo MCP is optional and "allows your local agent to gather context from Jira and Confluence and update work items as work progresses." (Before you begin)

## Key points
- **Documented (support page):** Development panel > "Open in coding tool" > choose agent; Jira remembers the last choice. Payload: summary and description.
- **Claimed (launch blog, [Brief your local coding agent with one click from Jira](https://www.atlassian.com/blog/development/deeplink-to-your-ai-coding-tool-from-jira), Himanshu Singh and Evan Perlman, 2026-06-16):** "Jira packages that context automatically through Atlassian MCP. The work item summary, description, and linked docs go directly into the starting prompt"; elsewhere it says a good prompt "includes the work item summary, description, comments, and linked resources."
- **Discrepancy:** the support page says summary and description only; the blog adds linked docs (and implies comments). Treat linked docs and comments as unverified.

## Could not verify
- The exact prompt template Jira generates.
