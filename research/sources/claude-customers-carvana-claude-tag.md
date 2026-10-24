---
title: "Carvana turns Slack alerts into production fixes with Claude Tag"
source_url: https://claude.com/customers/carvana
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [build-vs-buy, identity-delegation, feedback-triage-agents, shared-persistent-sessions, tacit-knowledge-capture]
relevance: medium
---

## Relevance to the project
Carvana built a multiplayer Slack agent twice (a homegrown loop, then an Agent SDK Slack app) and replaced both with Claude Tag, citing maintenance cost and the difficulty of per-team permissions: a clean build-versus-buy data point for a shared company agent. The deciding feature was "bundles" (instructions, tools and access scoped to one team's channel) running under separate per-team identities against one warehouse connection. It also shows alert-to-PR-to-human-review flows and a PM/engineer "multiplayer" ambition. Anthropic customer story: the 56% and 65% figures are Carvana's claims, unaudited.

## Themes
- build-vs-buy: two homegrown Slackbots retired; maintenance "required time and resources"; one team refused to adopt the homegrown tools over support uncertainty (section "The challenge").
- identity-delegation: one warehouse connection plus separate scoped identities per team (section "Managed agents with per-team identities").
- feedback-triage-agents: alert channels monitored; agent finds owning team, tags them, posts root cause in the team's format, opens PR on request (section "From alert to merged fix").
- shared-persistent-sessions: teams share investigations in open channels; spread "organically" (section "The outcome").
- tacit-knowledge-capture: release-baseline comparison logic kept as a skill in the team repo with runbooks, so senior engineers' knowledge is version-controlled (alert section).

## Key points
- **Outcomes (Carvana's claims)**: 56% fewer alerts in the retail science channel by fixing root causes; 65% faster answers for the wholesale platform team.
- **Wholesale trial**: two weeks, read-only access to tickets, build history and code; five cases traced to cause, including walking back its own first conclusion and standing down during an outage. Small sample.
- **Scheduled checks**: hourly pipeline and stale feature-flag checks, said to cost less than continuous monitoring.
- **Migration by the agent**: told to watch the old chatbot's answers for a week or two and learn to replace it.
- **Models**: Claude Tag defaults to Opus 5; teams mix Opus, Sonnet, Haiku; Fable for select power users, e.g. a senior attorney on transaction documents.
- **Behavioural effect**: people file more issues because the agent will carry them toward a fix (no number).
- **Next**: half a dozen teams building multiplayer flows where PMs and engineers move from bug or idea to shipped fix without opening an editor (aspiration).
- Limits: no date; no costs, error rates or false-positive data.

## Notable quotes
- "In my work, a confident wrong answer is far worse than no answer." (Carvana senior attorney)
- "They're letting Tag be a teammate." (Alex Devkar, SVP of Engineering and Analytics)

## Could not verify
- Publication date; how the 56% and 65% were measured.
