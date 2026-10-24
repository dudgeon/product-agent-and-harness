---
title: "Claude Duet is beautiful. I still forgot to use it"
source_url: https://www.lennysnewsletter.com/p/claude-duet-is-beautiful-i-still
author: Claire Vo (host)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-10-21
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [product-artifact-primitives, shared-persistent-sessions, agent-as-service-many-surfaces, harness-portability, agent-failure-modes]
relevance: medium
---

## Relevance to the project
A hands-on solo review of Anthropic's phone-first personal agent, Claude Duet (research preview), by a heavy agent user. It is useful less for the product than for the harness-design vocabulary it surfaces: task lists, first-class artifacts and Slack-style channels as the agent's primitives, and three failure points that matter for any PM harness (latency breaks synchronous work, local skills don't carry across surfaces, and the agent is single-player). Bears on agent-interface, session-persistence-sharing, capability-format-portability and artifact-and-project-structure.

## Themes
- product-artifact-primitives: Duet treats artifacts as first-class and already shows the artifacts from the user's existing Claude account; task lists track both the user's and the agent's goals; "channels" are the unit for sub-threads (e.g. a sales channel) (3:07-4:38). Vo frames the industry as still "trying to decide what the primitives are for agents" across threads, chats, projects and side chats (3:50).
- shared-persistent-sessions: Duet is "clearly an agent for single player use"; Vo, with a team of about five, says without a way to share agents with them it won't enter her working stack, and that Claude in Slack and similar don't yet deliver multiplayer (14:06).
- agent-as-service-many-surfaces: phone only, no desktop presence; Vo wants async kick-off on the phone and finishing at the desk, as she does with other agents (10:20-11:05).
- harness-portability: Duet inherits Claude plugins and connectors but not her local skills, so a launch-video workflow built in Claude didn't work; "what ports over elegantly, what does not" is an open question across vendors (13:10).
- agent-failure-modes: tasks took 10+ minutes per thread with no loop closure; she forgot them. A slower but better agent loses to a fast one "even if the more responsive ones do like 10 percent worse" (7:59-9:31). Inbox and Slack triage got priorities and context wrong (6:22).

## Key points
- Positioning (Vo's reading): small business owners and busy professionals; "the things that you would reach for in Cowork on your desktop" (0:40-1:33).
- Strong onboarding: clear about what it does and what it has access to (1:39).
- "Proactive" in name but it never nudged her after setup; she argues calm design is a re-engagement (growth) problem when competing with many agents, and that morning briefings are not enough of a hook (5:27-6:22).
- Real tasks: email/Slack triage (okay, wrong priorities), sales pipeline via already-connected Slack, email and CRM (good), a Google Docs sales deck kicked off from the phone (acceptable, didn't match brand design or use Figma), ticket shopping (slow, she forgot it), launch video (blocked by missing local skills) (6:22-13:10).
- Verdict: very polished, "approximately 100 times more polished" than OpenAI's comparable launch, but unlikely to become her main agent (15:05).

## Notable quotes
- "We're all trying to decide what the primitives are for agents." (3:50)
- "If that colleague is slow ... you kind of forget and don't want to go to that colleague over your more responsive ones." (7:59)
- "I don't have a way to share my agents with them, I'm not sure if it's going to worm its way into my working stack." (14:06)

## Could not verify
- Full transcript read (about 16 minutes, Substack auto-transcription). Single reviewer, early TestFlight build of a research-preview product; behaviour may have changed.
- Whether the lack of proactivity was a notification setting is unclear; Vo says so herself (5:27).
- Vo runs ChatPRD, a PM-agent product; she is a market participant, not a neutral reviewer.
