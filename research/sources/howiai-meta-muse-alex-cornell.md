---
title: "How Meta designed Muse: an AI agent people actually want to talk to | Alex Cornell (Design Director)"
source_url: https://www.lennysnewsletter.com/p/how-meta-designed-muse-an-ai-agent
author: Claire Vo (host), Alex Cornell (Design Director, Muse, Meta)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-10-12
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [shared-persistent-sessions, agent-as-service-many-surfaces, human-review-gates]
relevance: medium
---

## Relevance to the project
Meta's design director for Muse, a consumer agent, explains interface decisions that transfer to any agent people delegate background work to: a three-layer progressive-disclosure status (is it working, what on, the step list, down to raw calls and code for auditing), a single canonical "main chat" with optional side chats as the session model, proactive messages that need message bubbles to separate, and generated artifacts (dashboards, catalogs, podcasts) rendered from the user's data. It is consumer, not product work, but it bears on agent-interface and session-persistence-sharing, especially the open problem he names: how people should organize main versus side threads "in the agentic era".

## Themes
- shared-persistent-sessions: Muse has "a canonical main chat that is kind of very intentionally the primary main line" that you could use entirely; side chats exist because people are used to threading. Once models could hold the context in one chat, a single line felt more like talking to an entity: "I don't side thread with my mom" (25:51). He calls main versus side chat "an underexplored area" with "a lot more that we could do in terms of helping people organize" (27:21).
- human-review-gates: status by progressive disclosure: top line says it is working; then what it is working on; tap for the list of everything it has done; further down "the curl and all the code and everything, which is really important from an auditing perspective. But it's only there if you need it" (6:39-8:10). Chain of thought is kept out of the core chat by default (8:10).
- agent-as-service-many-surfaces: because the agent works in the background and can message proactively, the design borrowed messaging patterns (bubbles, an embodied avatar, quick acknowledgement then long work) rather than AI-app patterns (3:37-5:07, 9:53).

## Key points
- Framing that clarified "almost every decision": treat the interface as an exchange between you and an entity, and ask how a person would handle it (3:37).
- Primitives chosen for a non-technical audience: a character/avatar, chats, "ideas" (personalized suggestions that tell you what it can do, based on what you've talked about) and a prompt-defined feed; contrast with software-centric primitives in coding and knowledge-work agents (threads, projects, files, diffs, connectors) (5:33, 12:09).
- Generative UI is "on the rails": the avatar's states and feed units are designed native surfaces powered by personalization, "not yet like a fully generative surface" (12:09, 14:09).
- Designers must learn that the system is non-deterministic and personal; design the scaffolding rather than pixel outcomes, and accept artifacts that are useful but not pixel-perfect (32:12-33:44).
- Use cases demoed: Instagram saves turned into a daily SkyMall-style catalog; monitoring and price alerts; golf round recaps from watch data; chess.com dashboard; a 20-year-old blog recovered via the Wayback Machine and read back as a daily podcast (14:51-30:42).

## Notable quotes
- "you may want to know exactly what your agent has done ... you maybe just want to know, like, is it doing something?" (0:15)
- "there's a canonical main chat that is kind of very intentionally the primary main line" (25:51)

## Could not verify
- Whole transcript read. Consumer product; the host is an enthusiastic user. No usage numbers. How main chat and side chats share context or memory is not explained.
