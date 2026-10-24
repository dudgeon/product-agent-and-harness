---
title: "\"PMs who use AI will replace those who don't\": Google's AI product lead on the new PM toolkit | Marily Nika"
source_url: https://www.lennysnewsletter.com/p/pms-who-use-ai-will-replace-those
author: Claire Vo (host), Marily Nika (AI product lead, Google; founder, AI Product Academy)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-12-01
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [synthetic-users-limits, research-synthesis-agents, prd-agents, prototyping-agents-limits, agent-control-plane, single-agent-many-skills, ai-synthesis-hallucination-risk]
relevance: medium
---

## Relevance to the project
A canonical late-2025 picture of the "AI-enhanced PM" workflow as a chain of separate tools, each output pasted into the next: Perplexity's Reddit-only filter for research, a pro/con "agent debate" to derive a minimum feature set, a custom GPT that writes PRDs from a personal template, v0 for a clickable prototype taken to product review, and Flow/Sora for a promo video; the host calls the whole chain a 15-20 minute job. It is useful to the project mainly as the baseline a PM harness would replace: the hand-offs between steps are manual copy-paste, there is no shared context, and the guest herself ends by pointing to a coming tool that will make "tool hopping" unnecessary. Two claims bear on open questions: a PRD is a better prototype input than a bare prompt (fewer later tweaks), and the prototype's main job is influence in product review. Evidence is a scripted demo on a hypothetical smart fridge; the guest sells a PM bootcamp.

## Themes
- synthetic-users-limits / research-synthesis-agents: "within minutes, I can literally see what the entirety of the world is thinking about" via Perplexity's "discussions and opinions" (Reddit) filter, in place of a UXR team or agency (6:29). Then: create a pro and an against agent, "have these two agents debate at least 20 times" and output the minimum features needed "to convince the against agent" (8:02). The host frames this as a counter to model sycophancy (9:54). No check of the debate against real users is described.
- ai-synthesis-hallucination-risk: the guest claims this makes finding product-market fit "much more likely" (9:32); nothing in the episode tests that, and the source population (Reddit posters) is not questioned.
- prd-agents: a custom GPT holds "a template of my favorite PRD" and writes "in the style that I speak in my own voice"; output is "not going to be perfect immediately" but a head start (11:17-12:48).
- prototyping-agents-limits: the whole PRD is pasted into v0; experiments showed that skimping on input meant "the number of tweaks I had to do later on really got me overwhelmed" (15:59). v0 added features beyond the PRD and guessed the UI (18:21); she typically does "at least five to ten follow-ups" (21:31).
- single-agent-many-skills / agent-control-plane: "tool hopping" between specialised apps is presented as the method (9:32), with each step's output formatted as the next tool's input ("features is the input I need for the next tool", 11:17). She closes by promoting a new tool where "you do everything on this one tool" (38:41).

## Key points
- Old flow: idea, PRD, debate it with engineers and scientists, MVP. New flow: the PM also "puts on the AI builder hat" and prototypes before review (14:07).
- Prototypes are for product review: reviews happen "more often now with AI because things move fast"; a clickable link "adds credibility" compared with a PRD turned into a deck (17:00).
- Video mockups via Google Flow (Veo) and Sora to show the user's experience to stakeholders (21:31); the demo produced comically flawed results.
- NotebookLM as a judge: audio of ~200-person bootcamp demo-day pitches uploaded, hosts instructed to pick the top three by innovation, impact and storytelling; she says the AI's picks matched "the best demos" alongside live judges (32:24-34:01).
- When a tool fails: kill the instance, have AI write a longer, more detailed prompt, start over (38:11).

## Notable quotes
- "PMs that use AI are the ones that are going to take over the role of people who don't use AI." (31:41)
- "have these two agents debate at least 20 times about it and give me the minimum set of features" (8:02)

## Could not verify
- Transcript read 5:39-39:21 in full; 0:00-5:39 (intro, fridge anecdote) and the video-generation segment 21:31-30:16 skimmed via show notes and the host's recap.
- The example is hypothetical and the research step was not validated against real users. "AI really chooses the best demos" is the guest's impression; no agreement figures given.
- The guest's role at Google is stated in the title; nothing in the episode describes Google's internal PM practice.
