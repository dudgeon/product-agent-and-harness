---
title: "How Devin replaces your junior engineers with infinite AI interns that never sleep | Scott Wu (Cognition CEO)"
source_url: https://www.lennysnewsletter.com/p/how-devin-replaces-your-junior-engineers
author: Claire Vo (host), Scott Wu (co-founder and CEO, Cognition)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-09-08
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [public-by-default-agent-work, shared-persistent-sessions, agent-ready-intent, agent-as-service-many-surfaces, remote-agent-invocation, compounding-context-repo, human-review-gates, org-learning-loop]
relevance: medium
---

## Relevance to the project
A vendor CEO demoing how his own company works with an asynchronous coding agent, with patterns that transfer directly to a PM harness: a short synchronous step to shape the task ("tasks, not problems") before an asynchronous hand-off; the agent tagged as "first line of response" in every issue channel; Slack threads where several humans and the agent work one issue together ("Devin is just one of the players in the thread"); and public-by-default use so both the agent's knowledge and people's prompting skill spread. It is good evidence for session-persistence-sharing, remote-invocation-route and intent-shaping-and-spec (the agent-ready task as the hand-off), and it says PMs and tech leads are among the heaviest users because they already shape and hand off work. Vendor claim: it shows Cognition's own product.

## Themes
- agent-ready-intent: Devin does "tasks, not problems"; the question becomes "how do you figure out the spec or the task exactly that you want to do?" (4:04). Demo: ask DeepWiki where the MCP server list lives, then have it turn a rough one-line ask into a full Devin prompt naming existing patterns to follow, type structures, functions and how to check the work (8:40-10:27).
- shared-persistent-sessions: Slack threads are "a naturally multiplayer experience": a second engineer joins, tells Devin to use a particular router link component, and Devin adds commits to the PR (20:55-22:25).
- public-by-default-agent-work: host argues for using agents in public channels so people learn effective prompts and what agents are good at; "hiding your AI use is kind of the worst thing you can do" (24:01). Wu: two benefits, agent knowledge transfer and "educating the humans" (24:56).
- compounding-context-repo: Devin "builds this representation of the code base over time" (6:48) and remembers prior sessions: "I just touched this piece of the code last week" (24:56). Host's GitHub Action: Devin reviews each PR, rewrites the description, and after merge writes internal docs into the repo so Devin can use them (30:41).
- agent-as-service-many-surfaces / remote-agent-invocation: start sessions from Slack, Linear, the web app or the IDE; Slack and Linear suit people in meetings, the IDE suits ICs coding all day (17:21, 37:35).
- human-review-gates: every Devin change ends as a PR a human reviews and merges, with before/after screenshots for front-end work; progress updates carry a confidence level ("confidence medium") (14:11, 20:55, 26:09).
- org-learning-loop: "institutionalizing Devin as first line of response": Devin is tagged first on every issue in channels for crashes, core infra and the web app (19:19).

## Key points
- Framing: "Devin is a junior engineer"; not for hard architecture or strategic decisions, which stay with humans (4:04).
- Sync then async: a couple of minutes of back-and-forth (search, wiki) to shape the task, then hand off and expect not to be in the loop; compared to briefing an intern (11:24). Host: async products buy tolerance for latency and allow running 5-10 tasks at once (13:01).
- PMs and tech leads are heavy users, because they already scope an issue and hand off "here's exactly what we need to build" and are often in meetings (17:21). Host recommends giving PMs GitHub access at onboarding (18:17).
- Top five tasks: front-end fixes (verifiable for agent and human via screenshots), version upgrades and migrations, documentation, incident response (Devin is first on PagerDuty and has a report ready by the time a human wakes), unit tests run locally until CI passes (26:09-30:41). Host adds Sentry triage by Devin and 24/7 rubber-ducking (30:41).
- Future interface: "Tony Stark doesn't have a laptop": you look at the product, not the code, and direct the agent (36:14).
- Also: using ChatGPT voice as a meeting participant so everyone hears the answer (32:36-35:15).

## Notable quotes
- "Really, it is just a thread where a group of you are communicating and figuring out how to work on this issue. And Devin is just one of the players in the thread." (20:55)

## Could not verify
- Transcript read in full (auto-transcription; product names garbled, e.g. "Devon", "dbookie" for DeepWiki, "Chat Priority" for ChatPRD).
- The live demo did not finish on air: Devin could not find the ChatPRD MCP docs and the host had to paste a link (15:41-16:15); the resulting PR was not shown.
- No numbers on volume, merge rates or quality. The host is a Devin enthusiast and runs ChatPRD, which appears in the demo.
