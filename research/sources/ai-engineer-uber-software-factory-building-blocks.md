---
title: "Building Blocks for Uber's Software Factory (Agentic SDLC at Uber)"
source_url: https://www.youtube.com/watch?v=17-YSUHo6Lk
author: Uday Kiran Medisetty and Adam Huda (Uber)
publisher: AI Engineer (YouTube)
published: 2026-08-21
retrieved: 2026-11-02
type: video
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [agent-factory-sdlc, agent-as-service-many-surfaces, org-context-grounding, legible-org-for-agents, skills-marketplace, skill-improvement-loops, agent-control-plane, cost-control-routing, opportunity-to-code-chain, human-review-gates, verification-capacity-gap, shared-persistent-sessions, identity-delegation]
relevance: high
---

## Relevance to the project
The primary public description of Uber's Cortana: the company-wide AI assistant that packages Uber's skills marketplace, MCP gateway and context graph on Slack, CLI and web, lets employees make team personas bound to Slack channels, and hands off from ideation and design to Minion, Uber's cloud coding agent. It is the sixth of six "building blocks" (model gateway, MCP gateway, agentic DevPods, skills marketplace, context graph, Cortana) behind what Uber calls a managed software factory, so it is one of the clearest published cases of an "agent as a service on many surfaces" sitting on a shared platform layer. Adam Huda's half walks one feature from a Slack idea through Cortana research, requirements, Figma mock-ups and code-change planning to a Minion draft PR, inner-loop validation, review and managed maintenance loops, which bears directly on intent shaping and the opportunity-to-code chain. Talk delivered at AI Engineer (the AI Engineer site lists it as "Agentic SDLC at Uber"); figures are Uber's own, undated within the talk beyond "in the last one month".

## Themes
- agent-factory-sdlc: "more than 70% of our PRs now either by local or cloud agents", "twice the number of lines of code per engineer year-over-year", 250+ automated migrations and 9M lines changed (00:13-01:10); six building blocks "in various stages of maturity and rollout" (01:36).
- agent-as-service-many-surfaces: Cortana has skills, MCPs and the context graph "plugged into that in every surface possible whether it's on Slack, CLI, web" (10:19-10:36).
- shared-persistent-sessions: employees attach custom skills and a custom prompt to a persona bound to a team Slack channel so "it knows all of the things about that team and works like ... that teammate"; "one or more people can even collaborate on the same Slack channel" (10:49-11:17).
- org-context-grounding: context graph with 150 node and edge types and 40M entries covering mobile apps, back end, data lake, design docs, Jira, incidents and bugs (09:15-09:41); built because traces showed agents spending turns finding owners, dependencies and patterns across 20-30 systems (08:37-09:12).
- legible-org-for-agents: the graph's purpose is to let agents "quickly find the right context within our ecosystem"; skills for on-call RCAs, planning, data analysis and security scans are being plugged into it (09:41-09:53).
- skills-marketplace: managed skills marketplace with core and domain skills, 2,500 skills, lint checks and automated reviews, one command to discover and install, persona-based auto-install, 20,000+ executions a day (07:09-08:31).
- skill-improvement-loops: traces, comments and continuous evals fed back to skill authors (08:13-08:26); landed-or-not diffs from maintenance skills used as labels to improve the skill (16:50-17:00); monthly mining of incident reviews into new maintenance skills (17:00-17:10).
- agent-control-plane: model gateway as one OpenAI/Anthropic-compatible endpoint with Spire identity, PII anonymiser for 20+ types, an "AI guard" of five specialised models, all under 100 ms; audit logs and session traces captured there (01:46-03:19).
- cost-control-routing: per user, per project, per team attribution in real time and in the data lake, enabling spend tiers and guardrails (02:54-03:09); MCP token optimisations (Omni MCP, CLI projection, code-mode skill) saved "more than 40% fleetwide" (04:49-05:36).
- opportunity-to-code-chain: demo of a World Cup stadium pickup feature: Slack thread, tag Cortana, open in web, business research, product requirements (North America only), Figma mock-ups with two A/B variants, code-change analysis, then "we hand off from that Cortana agent" to Minion (11:46-13:25); claim that alignment that "could take weeks" is compressed (13:05-13:14).
- human-review-gates: Minion stops at a draft PR and does not push to CI until validated; the PR carries a table of the checks passed, with screenshots, to give the human reviewer confidence (13:47-15:49).
- verification-capacity-gap: bottlenecks named as CI capacity, how many experiments can be run, and "should we build it" decision-making (17:27-17:50).
- identity-delegation: model gateway authenticates every request with Spire (SPIFFE) identity (02:28).

## Key points
- Context: "a few thousand engineers across 12 global tech sites"; monorepo and Bazel moves over six years cited as the foundation (00:13, 01:12).
- Model gateway: no PII to vendors by default, latency-bounded guardrails, attribution per user, project and team; 800+ projects, 100M+ model requests a day across frontier and open models (01:46-03:44).
- MCP gateway: an automated crawler projects internal APIs into MCPs "with one single config change"; SaaS MCPs (Google, Slack, Jira) are hosted with token exchange; Omni MCP (one MCP that discovers and invokes others), CLI projection, and an auto-installed code-mode skill; 1,000+ MCP tools (03:46-05:36).
- Agentic DevPods: pre-provisioned Kubernetes "balloon pods" with repos snapshotted and search index built, so agents start in seconds; a "mega devpod" holds all repos for autonomous coding agents; non-engineers get any harness "in matter of seconds" (05:41-07:06).
- Cortana: anyone can ask a question; it can look up the graph, invoke any skill, check code in any codebase and answer on any surface (10:19-10:47). Personas: custom skills, custom prompt, bound to a team Slack channel (10:49-11:04). "300 unique personas created and more than 20,000 sessions per day" in "the last one month" (11:19-11:26).
- Lifecycle demo: Cortana helps judge whether the idea is "a good business opportunity" using the context graph, opens from Slack into a web interface, drafts requirements, mock-ups and code-change analysis (11:46-13:14). Minion runs interactive or autonomous on a DevPod across repos (back end and front end) and stops at a draft PR (13:17-13:51).
- Inner loop: static analysis, visual validation (simulator screenshot compared with Figma), staging-environment integration checks; outer loop: self-healing CI, two-tier code review (smaller model in the inner loop, larger reasoning model with a skill in the outer loop) (14:14-15:27).
- Maintenance: services enrol in maintenance skills (e.g. feature-flag cleanup) run as a "managed loop" from a managed surface, scheduled for spare CI capacity (Sunday) and rate-limited so engineers aren't flooded on Monday; "We don't want thousands of loops being set up across the company without any bounds" (15:53-16:50).

## Notable quotes
- "We have our AI assistant called Cortana." (10:23)
- "it knows all of the things about that team and works like ... that teammate." (10:59)
- "it's more of a question of should we build it" (17:48)

## Could not verify
- Transcript is YouTube auto-captions; names and numbers checked against independent write-ups but not against slides. No date for the 300-persona and 20,000-sessions figures beyond "the last one month" before the talk.
- How the Cortana-to-Minion handoff is carried (a link, a spec file, the Slack thread) is not shown; the podcast suggests Minion can read a Slack thread.
