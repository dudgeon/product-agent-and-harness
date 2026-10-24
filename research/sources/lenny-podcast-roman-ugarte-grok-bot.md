---
title: "How we built Grok Bot in a month | Roman Ugarte (SpaceXAI)"
source_url: https://www.lennysnewsletter.com/p/how-we-built-grok-bot-in-a-month
author: Lenny Rachitsky (host), Roman Ugarte (Grok Bot, SpaceXAI; formerly head of growth at Cursor)
publisher: Lenny's Podcast
published: 2026-09-08
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [agent-as-service-many-surfaces, shared-persistent-sessions, identity-delegation, product-coherence-over-automation, single-agent-many-skills, enablement-by-product, harness-over-model, one-job-per-agent]
relevance: medium
---

## Relevance to the project
A vendor's account of the design choices behind a knowledge-work agent product that, by the host's account, took off fast. The choices map directly onto our register: runtime always in the cloud ("you should never have to think about local and cloud"), each bot gets its own computer and credentials rather than sharing the user's, long-lived role-scoped bots rather than a chat per task, internals hidden (no tool-call stream), automations created in natural language, and skills hidden from users. It also argues for a separate app over adding a tab to the coding product ("shipping your org chart"). Bears on runtime-location, agent-identity-delegation, agent-interface, work-structure and session-persistence-sharing. It is a product pitch from the builder, with no numbers beyond onboarding counts and "99% of automations".

## Themes
- agent-as-service-many-surfaces: everything runs in the cloud so a bot "has the same state everywhere you interact with it"; text it, start it from a phone, call it in future (30:28).
- identity-delegation: each bot has its own computer, so it can use tools with no API by clicking pixels; sharing your machine is like telling a new hire "you're going to have access to my credentials, I'm going to have access to your credentials" (31:58).
- shared-persistent-sessions: "these are long-lived agents. These are not individual one-off sessions"; work grouped by roles or swim lanes, with long memory of past interactions; a new chat per unit of work causes copy-paste between chats (47:33-49:05). (Persistent, but per user; nothing about multi-user sharing.)
- one-job-per-agent: internal users ran five to ten bots each scoped to a lane; by week two some "promoted" a standout bot to chief of staff that fans tasks out to the others; the team encouraged the pattern only after early-access users found it unprompted (12:48).
- product-coherence-over-automation: chose a separate app over a tab in Cursor because bundled surfaces feel like "three different visions that all kind of share a screen ... shipping your org chart" (9:20).
- single-agent-many-skills: users should "not even have to know what a skill is"; skills created in the background (37:52).
- enablement-by-product: the team personally onboarded 200-300 early users in two weeks and fixed what broke the next day (11:41); internal launch at an all-hands drove switching from other tools (5:47).
- harness-over-model: where AI seems dumb it is often "harnessed in the wrong way"; giving the bot its own computer and tools raises the ceiling (36:20). "Unshipping": exposed model thinking, memory traces and debug tools were removed before launch; progress shown as a typing indicator, not tool calls (14:32, 19:21).

## Key points
- Timeline: a handful of people, isolated in a separate office area with private Slack, a month from first line of code to internal product; public launch about three weeks later (4:12-7:18).
- "Colleague-pilled" test for split decisions: ask how you would want a human teammate to behave; answers are "pretty unanimous" (39:31). Led to hidden internals, natural-language automations and a planned huddle-style voice mode (41:04).
- Natural-language automations: "Remind me at 8:00 AM every day" instead of a trigger/action builder; "99% of automations on the platform" are built this way (29:33). Product framing: "Grok Bot can now", not "Grok Bot now has" (27:48).
- GTM team as heavy users because sales tools lack APIs; 10-20 computer-use fixes (e.g. mouse precision on a Salesforce dashboard) unlocked workflows that had failed seven days running (21:56-23:30). Infrastructure work hill-climbed on categories of real user tasks week over week (21:02).
- QA tester bot runs the product inside its own computer against 10 regression workflows and logs results to a Notion document (50:14). "Infovore" chief-of-staff bot watches Slack, email and mentions and sends a daily roundup; some users let bots page them (51:13-52:56).
- Work and personal: expects many people to keep them separate, but one product for both (44:23).

## Notable quotes
- "We as humans don't do our jobs via MCPs and APIs." (31:58)
- "Grok Bot can now ... is I think a much more human way of describing these capabilities." (27:48)
- "Power tools of the future ... it is mostly just intent being expressed and good steering on the part of the human." (42:49)

## Could not verify
- Show notes read in full; transcript read 0:00-23:45 and 27:48-53:00 in full; the recruiting, speed-culture, moats and lightning-round sections (24:00-27:48, 53:36-end) skimmed by search.
- All adoption claims are the builder's; no usage numbers beyond onboarding counts and "99%". No enterprise governance, audit or admin controls discussed beyond Lenny's aside about SOC 2.
