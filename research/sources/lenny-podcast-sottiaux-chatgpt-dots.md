---
title: "OpenAI's Head of ChatGPT: We're entering a new era of AI (again) | Tibo Sottiaux"
source_url: https://www.lennysnewsletter.com/p/openais-head-of-chatgpt-were-entering
author: Lenny Rachitsky (host), Tibo Sottiaux (leads ChatGPT and Codex, OpenAI)
publisher: Lenny's Podcast
published: 2026-10-04
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [single-agent-many-skills, agent-as-service-many-surfaces, remote-agent-invocation, memory-architecture, work-structure-spectrum, shared-persistent-sessions, human-judgment-pm-jobs]
relevance: medium
---

## Relevance to the project
Recorded at OpenAI DevDay (October 2026) on the day "Dots" launched: a personal, always-on agent built on the Codex harness, with memory, no model picker, reachable through any channel, and a harness that "does not run on the machine" but connects to many devices. Its main bearing on the project is a strong vendor position against hand-built orchestration: "loops, graphs and fine-tuned prompts" are a passing phase, replaced by one capable agent that learns your goals. That cuts against persona sub-agent designs, though he also describes the opposite at the frontier: building "larger and larger teams of agents", then shrinking them when a better model arrives, plus planned role-specific "team dots". Bears on work-structure, harness-upkeep, runtime-location and agent-interface. It is a launch-day interview with the vendor; nothing was independently shown.

## Themes
- single-agent-many-skills: "having to set up and fiddle with your loops ... I don't think this is the way that it's going to work"; instead "an incredibly smart agent that works 24/7, understands your goals, understands your preferences, learns from feedback" (3:19).
- single-agent-many-skills (setup churn): his own agent setup goes through "expansion and shrinking": larger agent teams while pushing the frontier, then "a bigger agent can just do all of it, and keep everything in memory, and learn", so he shrinks the team (2:31). Takeaway: don't get attached to a setup.
- work-structure-spectrum: one primary Dot that learns preferences most deeply; soon users can add more Dots with specific roles to form a "virtual team", for example one that monitors Twitter because it is "the work of an entire dot" (10:55). He finds multiple Dots "not absolutely necessary".
- agent-as-service-many-surfaces: "permanent active intelligence ... available through any client, any screen": joins a meeting, takes notes, continues on email and text (4:13). The only configuration is which channels to talk through; Dots capabilities will be shipped into ChatGPT for its "1.2 billion users" (7:39).
- remote-agent-invocation: "the harness does not run on the machine"; a Dot has its own computer and can connect to many devices "a little bit like an octopus"; specialized Dots run with extra guardrails and monitoring, some on Mac minis (21:47).
- memory-architecture: two-plus years of research on long-horizon tasks and "memory systems that stay coherent", already shipped in ChatGPT; Dots combines that memory with the Codex harness and 24/7 operation (15:14).
- shared-persistent-sessions: "ChatGPT Space" is "the very start" of a shared whiteboard where humans and agents collaborate, beyond conversations (6:41); "talking to an agent is a solo adventure" is a problem they want to fix (17:50).
- human-judgment-pm-jobs: skill trending down: typing fast; up: "great taste, thinking about the user"; agrees PMs will thrive; "roles are blurring" (23:44-24:35).

## Key points
- Example of proactive judgment (20:31): his Dot noticed production was down five minutes before his live DevDay demo, linked the two, pinged him and offered to fix it; he declined ("I don't think you're there yet, little dot"). It has access to "some production systems with guardrails".
- Agents will take most internet actions (31:46): Notion's MCP server drew a flood of agent traffic that strained systems and forced economic rethinking; every product must eventually build for agents.
- Ecosystem (11:51): "Sign in with ChatGPT" with 16 partners; plugins recommended in conversation based on retention and quality, with revenue share for popular ones.
- Model picker fatigue (36:23): "You kind of need a PhD in model pickers"; Dots has none.
- Build as if models are 10x better in a year; his own forecast was too slow (32:49). Relies heavily on voice and dictation.
- Org notes: more than 120 ex-YC founders at OpenAI (23:44); a new-grad hire built much of the Codex harness and now runs the compute fleet (26:13).
- On burnout and "run 30 agents at once" pressure: the promise is less noise, "not just one more prompt per second" (19:11).

## Notable quotes
- "the harness does not run on the machine" (21:47)
- "You kind of need a PhD in model pickers." (36:23)

## Could not verify
- Medium podcast (about 37 minutes): show notes and takeaways read in full; transcript read 0:00-12:30, 15:14-24:40, 31:46-33:00 and 36:23; the rest skimmed by search.
- Everything about Dots, plugins and memory is the vendor's launch-day description; no demo in the episode. "1.2 billion users" and "120 ex-YC founders" are his figures.
- The anti-loops position is an opinion about direction, not evidence that single agents outperform orchestrated ones.
