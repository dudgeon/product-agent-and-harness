---
title: Why We Built Our Own Background Agent
source_url: https://builders.ramp.com/post/why-we-built-our-background-agent
author: Zach Bruggeman, Jason Quense, Rahul Sengottuvelu
publisher: Ramp Builders (builders.ramp.com)
published: 2026-01-12
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [agent-factory-sdlc, shared-persistent-sessions, non-engineer-builders, human-review-gates]
relevance: high
---

## Relevance to the project

Ramp's own spec of Inspect, its background coding agent: the "write the code" step of its lifecycle and the main handoff target from Slack, Glass and OCA. It documents the mechanisms by which intent reaches code at Ramp (Slack thread, Chrome extension, web, PR comments), multiplayer sessions, and the rule that PRs open under the requesting user's identity so nobody approves their own agent's work. Key input to the PDLC map and to the session-sharing and review dimensions.

## Themes

- **agent-factory-sdlc**: Inspect closes the loop by verifying its own work: runs tests, reviews telemetry, queries feature flags, visually checks frontend with screenshots and live previews (opening).
- **shared-persistent-sessions**: "every session is multiplayer. Send your session to any colleague"; prompts attributed per person; state synced across Slack, web, Chrome extension, PR and hosted VS Code (opening; API section).
- **non-engineer-builders**: a Chrome extension lets non-engineers point at UI elements and request changes; multiplayer used to teach PMs and designers (Clients section).
- **human-review-gates**: PRs open with the user's GitHub token, not the app's, so "any user [could not] approve their own changes" (API section).

## Key points

- January 2026: ~30% of PRs merged to frontend and backend repos written by Inspect, reached in "a couple months", no mandate (opening). Later figures from other Ramp sources: >50% (March talk), 75% (Charles, Sept).
- Sandbox: Modal VMs from per-repo images rebuilt every 30 minutes; snapshots to resume; OpenCode as the agent (server-first); wired into Sentry, Datadog, LaunchDarkly, Braintrust, GitHub, Slack, Buildkite.
- Inputs: Slack (a classifier picks the repository from message, thread and channel; "unknown" asks the user), web client, Chrome extension (DOM/React tree of the selected element), PR discussion, hosted VS Code; voice. Agents can spawn sub-sessions.
- State: Cloudflare Durable Objects, one SQLite per session; follow-up prompts queued.
- Metric that matters to Ramp: share of sessions that end in a merged PR.

## Could not verify

Adoption figures are self-reported; the post is a build spec, not an evaluation. Later posts say Inspect now runs on Laminar (October 2026), so the stack described here may have changed.
