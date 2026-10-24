---
title: "Lessons from Anthropic on building effective human-agent teams"
source_url: https://claude.com/resources/articles/building-effective-human-agent-teams
author: Kristen Swanson (Education team, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-06-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [public-by-default-agent-work, one-job-per-agent, evals-autonomy-trust, legible-org-for-agents, shared-persistent-sessions]
relevance: high
---

## Relevance to the project
Anthropic's internal practice for "multiplayer agents" (agents with their own credentials, memory and skills that sit in Slack and work with many people at once) gives four norms: work in public inside a few workspace-level security boundaries, give every human and agent a defined role on a written roster, let humans set a north star and name which agents may propose work, and grant autonomy per task type as reliability is shown. It is a direct first-party model for the agent-interface, session-sharing and review-and-autonomy dimensions, and it differs from Shopify's River on privacy: Anthropic keeps a private path (DM to Claude, or Claude.ai and Cowork with personal connectors). Evidence is internal anecdote; the only outcome claims are "500 bug fixes" dispatched to agents and a north-star example that "measurably increased onboarding success", with no figures.

## Themes
- public-by-default-agent-work: Lesson 1: "if it's not written down and accessible, it doesn't exist" for agents; channels default public within the org; a handful of workspace-level boundaries instead of per-item sharing; private DMs and personal-connector apps kept for sensitive work.
- one-job-per-agent: Lesson 2: separate agents own data analysis, design-standard enforcement, research synthesis, release management; roles defined in skill files so others can stand up the same agent type.
- evals-autonomy-trust: Lesson 4: autonomy granted "in proportion to demonstrated reliability", tracked per task type; Doer-Verifier pairs; rubrics and style guides as verifiers for non-code work.
- legible-org-for-agents: write artifacts and meeting notes "so that agents can find them, since agents are now a primary consumer of team documentation" (Lesson 1 list).
- shared-persistent-sessions: humans and agents work in the same shared threads "so anyone can pick up where anyone left off" (Lesson 2 list); one shared metrics agent instead of fleets of personal AIs.

## Key points
- Definition: multiplayer agents need persistent memory, credentials not tied to humans, and broad ongoing access to information.
- Lesson 1 mechanism: choose a few security boundaries, map Slack workspaces, transcripts and doc libraries to them; context flows freely inside a boundary. Argued benefit: agents won't suggest deprioritised work if they can read meeting decisions.
- Lesson 2: at project kickoff humans chat with agents to assign roles; an agent may spin up sub-agents with the right memory and access (e.g. BigQuery for analysis, Playwright MCP for QA). Without roles, "people end up running fleets of personal AIs on the side, duplicating work and fracturing the team's context."
- An engineering team keeps a roster of human and agent roles; agents share codebase maintenance (triage feedback, plan, write code, review, report status), each on its own schedule; people set goals and review.
- Lesson 3: humans always set the north star; humans explicitly choose which agents may proactively suggest workstreams ("It's unlikely that every agent on the team will have the prerequisite skills and trust"). Example: onboarding-copy changes proposed by an agent.
- Lesson 4 practices: manual review at first and build verification checklists; verifier agent in the task; agents review their own misses; weekly "lessons & missteps" report; retest tasks when models change because old guardrails may constrain smarter models.
- Backlog example: one agent set scores unowned backlog items for complexity; another set writes code for medium/low items; humans first reviewed every decision, then taught agents to escalate hard-tradeoff decisions themselves.
- Human-attention guardrails: agents batch questions, repeat key context, limit items per human; some teams have an agent whose only role is to batch and elevate communication; caps on agent work per day so review stays sustainable and humans keep skills.
- Closing checklist: is information public and searchable; can you write the roster; does everyone have the right tools; are there rubrics or tests; is there a north star.
- Limits: no failure cases or costs of openness discussed; outcomes anecdotal; product context is Claude Tag and agent teams in Claude Code.

## Notable quotes
- "For an agent, if it's not written down and accessible, it doesn't exist." (Lesson 1)
- "Teams at Anthropic grant agents autonomy in proportion to demonstrated reliability, then expand it deliberately." (Lesson 4)

## Could not verify
- The embedded Slack example (a human-agent team analysing a dataset) is an image or video not present in the text extract.
- No numbers behind "measurably increased onboarding success".
