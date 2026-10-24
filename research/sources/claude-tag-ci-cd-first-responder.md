---
title: "How Claude Tag serves as Anthropic's first responder for CI/CD failures"
source_url: https://claude.com/resources/articles/ai-ci-cd-on-call
author: Sachin Malhotra (Member of Technical Staff, Anthropic), with Michael Segner (Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-08-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [shared-persistent-sessions, compounding-context-repo, org-learning-loop, status-update-agents, human-review-gates]
relevance: high
---

## Relevance to the project
A detailed first-party build of a channel-resident, shared agent: Claude Tag sits in Anthropic's CI on-call Slack channel with its own service account, memory across the channel, schedules set in natural language, and skills plus a self-appended lessons.md kept in a GitHub repo. It is the clearest concrete example in the library of the "maintain" stage of an agent-assisted product loop and of a compounding-context loop (incident log promoted into skills). It also shows where humans stay: fixes come as PRs for the on-call to merge, and the ci-weather status report needed several rounds of human taste, though only for an engineering team, not for PM work.

## Themes
- shared-persistent-sessions: the agent lives in the on-call channel, holds memory across it, watches adjacent channels for alerts and PR updates, and multiple engineers steer one investigation "in multi-player mode" (sections "Our Claude on call setup", "Triage").
- compounding-context-repo: standing instructions are markdown skills in a GitHub repo so teammates iterate on them like code; a 617-line investigation skill per bug class was built by debugging turn-by-turn with Claude and having it write the file (sections "setup", "Triage").
- org-learning-loop: Claude appends every resolved incident (cause, fix, gotcha) to lessons.md, reads it first on each new investigation, and recurring patterns are promoted into the skill (section "Triage").
- status-update-agents: a ci-weather agent compiles incident channels, build metrics, merge-queue stats and deploy lag into a newsroom-style post in a public channel; daily and weekly human handoff summaries (section "Verification, communication, and handoff").
- human-review-gates: most frequent resolution is a PR "that the on-call can review, merge, and then deploy"; org-wide rule that every PR has a named human owner and every change needs approval to merge (sections "Resolution", "From monitoring incidents").

## Key points
- Four ingredients named for an on-call agent: memory, connections and access, schedules, instructions (section "setup").
- Identity and access: Claude Tag has its own service account with the tools a CI engineer needs (Datadog, Grafana), configured once by an admin for the channel. A separate progressive-deployment agent runs in Claude Code "with my permissions", so two identity models coexist.
- Detection: alerting stays deterministic; escalation has deterministic and agentic paths, with paging criteria written as rules in oncall.md (e.g. error rate over 2% for 5 minutes outside a deploy window). Claude also proposes and tunes alert rules for new services.
- Triage: an orchestrator spins up executor subagents per dependency (Grafana, logs, PagerDuty, GitHub, Kubernetes, Slack) via MCP connectors and synthesises a SITREP. Anthropic reports a median of 14 minutes to first evidence-grounded analysis, as fast as 4 minutes to root cause, and that Claude wrote the first situation report in every recent incident that had one.
- Admitted limit: "Claude doesn't always get it right the first time"; human intuition steers. Report format needed several iterations: "what makes it readable is team-specific taste."
- Context claim: Anthropic engineers "on average ship 8x as much code per quarter" as in 2021-2025; framed as why agentic CI is needed. No method given.
- Setup kit on GitHub turns a team's incident history into triage playbooks and yields a read-only Claude in the incident channel. Requires Team or Enterprise plan, org owner adding Claude Tag, connectors, GitHub repo and Claude Code Remote.
- Limits: single team's account written by its engineer; opening anecdote is "redesigned from a real exchange"; no false-positive or wrong-diagnosis rates.

## Notable quotes
- "query the data first, then theorize. Config tells you what could go wrong; metrics tell you what did." (lessons.md entry Claude wrote, section "Triage")
- "It's human communication, not plumbing." (on the status report, section "Verification")

## Could not verify
- The 14-minute median, 4-minute fastest and 8x code figures: no sample size or method.
- Contents of the setup kit (not fetched).
