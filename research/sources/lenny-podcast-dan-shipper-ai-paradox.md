---
title: "The AI paradox: More automation, more humans, more work | Dan Shipper"
source_url: https://www.lennysnewsletter.com/p/the-ai-paradox-dan-shipper
author: Lenny Rachitsky (host), Dan Shipper (co-founder and CEO, Every)
publisher: Lenny's Podcast
published: 2026-05-24
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [agent-as-service-many-surfaces, agent-stewardship, human-review-gates, product-coherence-over-automation, pm-persona-role-expansion, non-engineer-builders, status-update-agents, harness-over-model, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
Dan Shipper (CEO of Every, about 30 people, all heavy AI users) reports reversing his view on agent architecture: personal agents for everyone (an "AI shadow org chart") failed at Every because each agent needs a human who keeps it working, so the model that works "for now" is one company "super-agent" in Slack maintained by a forward-deployed engineer, trickling down to team agents later (he names Shopify's and Ramp's). He also predicts most knowledge work moves inside an agent workspace (Codex, Cowork) with SaaS used inside it, and that software must be designed for human and agent working on the same artefact: approvals, a summarizing inbox, logs and quick rollback. Both bear directly on target-user, agent-interface, harness-upkeep and session-persistence-sharing. Evidence is one small, unusually AI-forward company.

## Themes
- agent-stewardship: "in order for an AI agent to be useful right now, it really needs a human who cares about it"; once someone stops maintaining their personal agent "the agent is not really that useful anymore" (13:36). Forward-deployed engineers who run internal agents are "the new most essential role"; big model companies have teams doing this (53:15). One AI engineer at Every spends most of his time in Slack talking to "Claudy", the agent that runs their consulting practice (54:53). The job is less "babysitting" than building "a system that makes it so that people who have less knowledge can use that system without doing something dumb" (1:02:11).
- agent-as-service-many-surfaces: two modes of work: async agents you delegate to, probably in Slack; and an on-computer workspace (Codex, Claude Cowork) that becomes "an operating system for how you do all of your work" (10:29-12:01). He works in one Codex thread per project with an in-app browser so the agent sees what he sees (21:32); "take the AI agent ... and put a browser in it" rather than AI in the browser (23:04).
- human-review-gates: software for human-plus-agent co-work needs "approval, ... a inbox that summarizes, 'Here's all the stuff that's going to happen,' or has happened ... logs and the ability to roll it back real quick" (29:34). Codex once sent an investor email without asking; it happened to be right, but he notes it usually asks (1:05:33).
- product-coherence-over-automation: non-technical staff (consultants, ops, editors) now make pull requests; this moves pressure to whoever merges: "would it make sense with the rest of what we've built and how do we keep a sense of a coherent whole. And also, what do we delete?" (50:25-51:55).
- outcome-measurement-gap: "Automation is a lie": every automation needs a human on top; benchmarks overstate autonomy because they score problems already framed (39:15). His own "senior engineer benchmark" (rewrite a vibe-coded app from first principles): models scored about 30/100 until GPT 5.5 scored about 62 (with an Opus 4.7 plan), versus high 80s to low 90s for human senior engineers; models fix the issues they are told about instead of reframing (41:46-44:50).
- status-update-agents: Every ran its end-of-2025 quarterly planning through one Notion agent: each person talked to it about last year, goals and metrics; it pushed back and tied plans to company strategy; he then read the reports to see which teams needed to talk and which plans were weak (1:02:11-1:04:02).
- pm-persona-role-expansion / non-engineer-builders: a "lightly technical" former PM (previously ran Axios' writing product) runs Every's Spiral app, "ships faster than almost anyone on the team", and could not have been hired for the role a year earlier (1:08:40). Full-stack designers who build their own work are "superheroes".
- harness-over-model: "every model company is starting to realize how important it is to have a harness to get the most out of the model"; the platforms now run the model on a cloud computer (he cites Anthropic's managed agents) (25:52-27:23).

## Key points
- Personal vs company agent (13:36-17:25): everyone at Every adopted OpenClaw at first; it proved "way too much work" (breaks, SSH into servers). The working pattern: one agent at the top, often for a job everyone needs (data requests is his example), maintained by one person; more personal agents later as models get less fiddly. Every paused its hosted OpenClaw product because the harness changes too fast to support.
- Agent-to-agent setup (33:38-36:22): assume users arrive through Codex or Cowork; their agent passes context about the user to your app or app agent, replacing onboarding forms; users' agents file better bug reports (exact repro steps) that become GitHub issues an agent fixes (29:34).
- SaaS economics (24:02, 36:41): when users bring their own agent, they pay the tokens; Every's SaaS spend is up because agents need seats; GitHub strain is attributed to agent traffic.
- AI-written internal writing (1:02:11-1:07:10): plans, strategy docs and email are fine as AI output if the sender stands behind every line; slop is when "it took them less time to make it than it takes me to read it".
- Every doubled in headcount in the year despite heavy automation (show notes).

## Notable quotes
- "it really needs a human who cares about it" (13:36)
- "Automation is a lie" (39:15)
- "You need logs and the ability to roll it back real quick." (29:34)

## Could not verify
- Medium podcast: show notes and takeaways read in full; transcript read 10:22-36:22, 39:15-45:00, 50:25-1:10:30; the rest skimmed by search.
- The Ramp company agent is mentioned but not named in the transcript; "River" for Shopify is Lenny's recollection. Benchmark scores are his personal test, not published.
- Different episode from the July 2025 Shipper interview filed as lenny-podcast-dan-shipper-every-ai-native.
