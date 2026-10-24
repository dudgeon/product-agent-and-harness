---
title: "How Block Deployed AI Agents to 12,000 Employees in 8 Weeks w/ MCP | Angie Jones"
source_url: https://chainofthought.transistor.fm/episodes/how-block-deployed-ai-agents-to-12-000-employees-in-8-weeks-w-mcp-angie-jones
author: Conor Bronsdon (host), Angie Jones (Block)
publisher: Chain of Thought (Galileo)
published: 2026-01-21
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-block-product-practices
themes: [enterprise-admin-controls, human-review-gates, harness-portability, agent-as-service-many-surfaces, agent-factory-sdlc, non-engineer-builders]
relevance: medium
---

## Relevance to the project
Angie Jones (Block) on governance and surfaces of the internal goose deployment, read via the episode transcript. Confirms the two-step allowlist rule (even internal servers need security review), destructive-only approval, OAuth through the identity provider, Databricks-hosted multi-vendor models, and goose embedded in Slack, Jira and Linear. The "12,000 in 8 weeks" figure is the host's framing, not her claim in the episode.

## Themes
- enterprise-admin-controls: "We have developed an allowed list of MCP servers"; "even if I built one, security needs to review it"; non-listed servers fail to install (~27:50-29:09).
- human-review-gates: tools annotated destructive or not; non-destructive tools run automatically, destructive ones "ask my permission first" (~29:25).
- harness-portability: Claude, GPT and Gemini hosted via Databricks; engineers mostly Claude; local models "a very small percentage" (~07:10-09:33). "We don't have a dog in the fight" (~38:05).
- agent-as-service-many-surfaces: goose joins Slack threads, reads context, checks GitHub and opens a PR (~35:04); embedded in Jira and Linear, where it finished sprint work early (~35:22).
- non-engineer-builders: natural-language data queries for people who "don't know SQL"; prototypes win buy-in faster than documents (~21:46-23:47).

## Key points
- Rollout began when non-engineering teams asked why engineers "get to go fast"; team-tailored workshops; "there's no playbook for this" (~02:24).
- Block built extra servers for non-engineering systems such as Workday and Figma (~05:12).
- Recipes bundle instructions, prompts and MCP servers; hidden characters can make them malicious, as the red team found (~27:00).
- Roadmap: goose in IDEs via ACP (JetBrains, Zed); $100K/year contributor grants (~47:00).

## Could not verify
- Timestamps approximate (transcript page); no velocity figures given.
