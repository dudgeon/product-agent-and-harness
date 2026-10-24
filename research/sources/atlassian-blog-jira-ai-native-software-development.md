---
title: How we're evolving Jira for AI-native software development
source_url: https://www.atlassian.com/blog/company-news/ai-sdlc
author: Dave Meyer (Atlassian)
publisher: Atlassian blog (Inside Atlassian)
published: 2026-07-15
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: user-story-mapping
themes: [agent-factory-sdlc, opportunity-to-code-chain, legible-org-for-agents, agent-control-plane, harness-portability, vendor-claims-vs-independent-evidence, cost-control-routing]
relevance: high
---

## Relevance to the project
This is Atlassian's umbrella launch for the "intent to PR" chain: Jira Planner (spec), Jira for Slack and Loom video prompts (intake), agents in Jira (assign to Claude Code, Cursor, Copilot), Jira Coding Agent, agent sessions, coding-agent automations, an agentic template and DX cost tracking. It names the Teamwork Graph as the context layer that joins JPD customer insight, Confluence requirements, Slack and GitHub. It is the best single statement of the vendor's lifecycle model, so it is the frame to test a PM agent's lifecycle map against. The figures are vendor claims.

## Themes
- `agent-factory-sdlc`: "Teams can plan work with AI, turn intent into agent-ready specs, assign work to coding agents, monitor sessions, automate engineering loops, and measure AI cost against output."
- `opportunity-to-code-chain`: the Teamwork Graph brings together "that atomic task in Jira, the requirements in Confluence, the conversation in Slack, code context from GitHub, and customer insights from Jira Product Discovery."
- `legible-org-for-agents`: "the SDLC needs to become legible to agents without becoming less accountable to humans."
- `agent-control-plane` / `harness-portability`: "Agents in Jira let teams assign work items directly to Claude Code, Cursor, or GitHub Copilot, with Codex coming soon"; "The workflow should not fork every time the runtime changes."
- `cost-control-routing`: "DX AI cost management ... estimates cost per PR in DX."
- `vendor-claims-vs-independent-evidence`: "agents enriched by Teamwork Graph showed 44% more accurate results while using 48% fewer tokens" (internal benchmarking, no method given); a DX study finding AI usage up 65% but velocity gains topping out at 15%.

## Key points
- **Claimed:** Jira Planner "pulls from your codebase, Jira and Confluence history, and team context to define requirements and generate a structured technical spec in Confluence. ... One artifact, two audiences." (see [Jira Planner note](atlassian-blog-introducing-jira-planner.md))
- **Claimed:** Jira for Slack captures thread nuance, syncs conversation updates as comments, and assigns work to coding agents.
- **Claimed:** Loom video prompts produce an action plan that becomes "agent-ready Jira work items in a few clicks" (documented in the [Loom note](atlassian-loom-record-for-agent.md)).
- **Claimed:** Jira Coding Agent is "built into every paid Jira plan" (the support doc says Standard or Premium plus Rovo credits).
- **Claimed:** Agent sessions view groups sessions by "stuck, what's waiting for review, and what's complete."
- **Related launches (first-party blogs, vendor-claim):**
  - [Claude Agent for Jira](https://www.atlassian.com/blog/company-news/claude-agent-for-jira) (Himanshu Singh, Geoff Clitheroe, 2026-06-18): a Marketplace Forge app built on Anthropic's Claude Managed Agents; assign, @mention, or automate; "The agent reads directly from the work item, including acceptance criteria, target repository, and relevant design/engineering standards"; clones the repo in Anthropic's sandbox, opens a draft PR in GitHub, and "streams real-time status updates directly back to the Jira work item." Needs an Anthropic API key and GitHub service account; Standard/Premium/Enterprise with Rovo.
  - [Assign work directly to Cursor in Jira](https://jirareleases.atlassian.com/announcements/assign-work-directly-to-cursor-in-jira) (Jira release notes, 2026-05-20): assign or mention Cursor to start a cloud agent; Cursor notifies in Jira when it needs input or is ready; its PR is "automatically linked back to your work item"; "Use Rovo to enrich your task with context from across Atlassian's Teamwork Graph, then assign to Cursor."
  - [Scale AI coding agent impact with Jira Automation](https://www.atlassian.com/blog/development/scale-agent-impact-with-jira-automation) (Natalie Chung, 2026-07-29): GitHub Copilot, Cursor and Claude as native automation action steps with a per-step system prompt; examples include "If the work item is missing context, post a comment ... label it as 'Needs Refinement'"; a JSM alert + bug triggers an agent that pulls telemetry via "the Teamwork Graph MCP" and runbooks from Confluence and attaches an investigation summary; "Every agent invocation is logged in Jira's audit trail."
- **Codex status conflicts:** this post says "coming soon"; the [Jira dev product page](https://www.atlassian.com/software/jira/dev) and agentic guide list Codex as assignable now.

## Could not verify
- Method behind 44% / 48% figures. Whether third-party agents receive Teamwork Graph context automatically or only via Rovo enrichment and MCP.
