---
title: How Atlassian builds AI agents teams can trust with Claude and Google Cloud
source_url: https://claude.com/customers/atlassian
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [cost-control-routing, org-context-grounding, legible-org-for-agents, non-engineer-builders, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
Atlassian routes work between models by difficulty through its own model gateway: Claude for complex, long-running agent work (Rovo Chat, Rovo CLI, Rovo Max) and Gemini Flash as the default for high-volume customer agents, with each team writing its own evals to pick a model. Its Head of AI argues the durable differentiator is context (Teamwork Graph), not model intelligence, and frames the next task as making Atlassian's capabilities usable by agents as "an equivalent customer". This bears on model-provider coupling and context strategy for anyone building product agents on top of Jira and Confluence. Figures are vendor claims, from a page in which both parties are vendors.

## Themes
- cost-control-routing: an internal AI model gateway on Google's agent platform routes across providers; high-volume custom agents moved to Gemini Flash, Claude kept for complex work; teams benchmark models on quality and cost and deploy the winner ("An open platform, built on Google Cloud").
- org-context-grounding: Rovo Max draws on Teamwork Graph's map of billions of objects; demo agent followed Jira links to Figma and Google Docs to build a release reel ("The outcome").
- legible-org-for-agents: "How do I make sure agents are an equivalent customer of our software?" (Sherif Mansour, "The challenge").
- non-engineer-builders: an internal pilot extended Claude Code to non-technical teams; PMs and designers prototyped, committed small code changes and built internal apps ("The solution").
- vendor-claims-vs-independent-evidence: 5 million+ agent executions per month and "millions" of Rovo Chat users are vendor figures; no quality or trust metrics despite trust being the headline.

## Key points
- **Claude's role:** base model in Rovo Chat (choosing among thousands of tools and skills), Rovo CLI (primary developer AI), Rovo Max (early access: takes a goal, works until reached, runs in a managed environment where admins control packages and network access), and one of several models in Rovo Studio (low-code agents). Jira tickets can be handed straight to a Claude-powered agent.
- **Why Claude:** instruction-following consistency, long-context handling, tool orchestration, for "workloads where the cost of a wrong answer is highest".
- **Portability stance:** when vendors retire models the team swaps in newer ones without re-architecting; "a long-term roadmap in the world of AI is probably no more than three months".
- **Customer job targets:** contract first-pass review, ticket triage, lead surfacing; finding steps inside "billions" of existing Jira/Confluence workflows where an agent can deflect or speed work.
- **Limits:** "trust" is asserted, not measured; no evals, error rates or admin-control detail beyond Rovo Max's sandbox; the demo is internal.

## Notable quotes
- "The context is really just the knowledge they have everywhere." (Sherif Mansour, Head of AI)

## Could not verify
- Publication date; how "agents executed" is counted.
