---
title: "Build agents that run automatically (Cursor Automations)"
source_url: https://cursor.com/blog/automations
author: Jack Pertschuk, Jon Kaplan, Josh Ma (Cursor)
publisher: Cursor blog
published: 2026-03-05
retrieved: 2026-10-26
type: article
evidence: vendor-claim
filed_by: research-shared-persistent-agents
themes: [remote-agent-invocation, shared-persistent-sessions, human-review-gates, risk-sloped-review, memory-architecture, verification-capacity-gap]
relevance: high
---
## Relevance to the project
Cursor's launch post for Automations: always-on cloud agents triggered by schedules or by Slack, Linear, GitHub, PagerDuty and webhook events, each run in a fresh sandbox, with a memory tool so later runs learn from earlier ones. It gives concrete patterns for several catalogue items at once: overnight/morning runs (daily test-coverage PRs, weekly digest), a reviewer agent waiting on every push to main, an "agentic codeowners" agent that routes risky PRs to the right two humans, and incident agents that ping on-call with a proposed fix. All outcomes are vendor self-report with no numbers beyond Bugbot volume (also linked: changelog https://cursor.com/changelog/03-05-26).

## Themes
- remote-agent-invocation: triggers are schedules plus events from Slack, Linear, GitHub, PagerDuty and webhooks; "the agent spins up a cloud sandbox and follows your instructions using the MCPs and models you've configured" (changelog and blog, 2026-03-05; vendor-claim)
- risk-sloped-review: "agentic codeowners" scores each PR by blast radius, complexity and infra impact; "Low-risk PRs get auto-approved", higher-risk PRs get up to two reviewers picked by contribution history; decisions logged to Notion so the team can audit and "tweak the instructions" (Review and monitoring section; vendor-claim)
- human-review-gates: security review runs after merge to main so it "can take longer" without blocking the PR, posting high-risk findings to Slack; incident response produces a PR, not a production change (vendor-claim)
- memory-architecture: agents get a memory tool that "lets them learn from past runs and improve with repetition"; storage, scope and review are not described (vendor-claim)
- verification-capacity-gap: stated motivation is that review, monitoring and maintenance have not sped up as code generation did, so agents take on those later stages (intro; vendor-claim)
- shared-persistent-sessions: Rippling example: useful automations are shared across the team; a cron agent every two hours compiles one engineer's Slack notes, PRs, Jira and mentions into a dashboard (customer example; anecdote)

## Key points
- Examples: per-push security audit; agentic codeowners; PagerDuty-triggered incident agent that reads Datadog logs via MCP and messages on-call with a fix PR ("significantly reduced our incident response time", no figure); weekly Slack digest of merged work; morning test-coverage agent that opens a PR; Slack bug-report triage that dedups, files Linear issues, attempts a fix and replies in thread.
- Bugbot is called "in many ways the original automation" and "gets triggered thousands of times a day".
- Not stated: identity the automation runs as, billing, run counts, guardrails on auto-approval beyond the audit log.

## Notable quotes
- "Low-risk PRs get auto-approved."
- "Anything can be an automation!" (Tim Fall, Rippling)

## Could not verify
- Internal run counts ("hundreds of automations per hour") appear only in secondary coverage, not in the post.
- No independent measure of incident-response improvement or auto-approval error rates.
