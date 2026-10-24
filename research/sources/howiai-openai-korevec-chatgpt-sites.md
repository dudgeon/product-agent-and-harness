---
title: "How OpenAI uses ChatGPT Sites (live at DevDay!) | Kath Korevec (Product Lead)"
source_url: https://www.lennysnewsletter.com/p/how-openai-uses-chatgpt-sites-live
author: Claire Vo (host), Kath Korevec (product lead for ChatGPT Sites, OpenAI)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-10-05
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [product-artifact-primitives, identity-delegation, task-context-isolation, non-engineer-builders, skill-standards, human-judgment-pm-jobs, pm-tool-connectivity]
relevance: medium
---

## Relevance to the project
A vendor's product lead demos ChatGPT Sites, OpenAI's hosted place for agent-built web artifacts, on launch day of "plugins and sites". The idea that matters for us is a shared artifact that renders **each viewer's own data through that viewer's own connector grants**: one incident-command page, different content per team. That is a concrete pattern for artifact-and-project-structure and trust-privacy-defaults: the artifact is shared, the data scope travels with the viewer, not the author. It also shows a PM building a live, throwaway status surface instead of asking the team for updates, and a hard personal line against the agent writing in her name. Vendor demo on launch day; the incident site shown is a scrubbed replica.

## Themes
- product-artifact-primitives: Sites is "a place to basically put software someplace" built by Codex, handling deploy; comes with D1 data, an R2 bucket, co-editors; used for all DevDay keynote slides (1:32, 6:48, 9:46). Host frames the common use as hosting "an HTML PRD or slides" before connectors (5:57).
- identity-delegation / task-context-isolation: with plugins in sites, a visitor approves their own connectors and "you see only your data on that site"; the same site shows different content to the Codex team or identity team based on which Slack channels they come from (0:00, 8:04). Pitched at data and finance teams with role-scoped sensitive data (8:04). Enterprise workspaces only (1:32).
- status-update-agents: Korevec, a PM, built an incident command overview from Slack, Notion runbooks and calendar so she can follow incidents "down to the minute" without interrupting the team (3:07).
- skill-standards: a "Dungeon Site" skill distributes how to extend her game (room dimensions, controls); host calls skills as a distribution model for interacting with an app "a user experience I haven't heard before" (18:12, 20:25).
- human-judgment-pm-jobs: "if it starts emailing or talking to people for me, I get so mad"; uses Codex for research and drafting "but I don't like it writing for me" (32:35, 33:36).
- pm-tool-connectivity: about 60 connectors at the time; her staples are Slack, Notion, Google Drive, Calendar (9:07). Prompting "bring your own connector" makes Codex wire connectors in (6:48).

## Key points
- Sites launched internally about two months before DevDay and "explode[d]" inside OpenAI; uses include the team out-of-office calendar, incident command, music sharing (1:32, 4:40).
- Disposable personal software: she builds a site for a week (e.g. a business trip view of her calendar) and throws it away (9:46).
- Sites can host MCP plugins and has been used to host data and run evals (11:27).
- Analytics for site authors are lightweight (visits and traffic); she has no insight into who uses a distributed skill; plans for more "agentic" analytics (21:33). Relevant to measuring artifact use.
- Experiment: bringing inference into a site via a widget so visitors can ask ChatGPT to change it (25:42).
- Personal automation uses computer use on her open laptop every Monday at 8am (13:02, 15:06).

## Notable quotes
- "When you log in, it will actually ask you to approve your connections ... you see only your data on that site." (1:32)
- "I want to protect that. That's my voice." (32:35)

## Could not verify
- Transcript read in full (Substack auto-transcription with some garbled speaker attribution; model name "Astra" may be a transcription error).
- Internal usage ("explode") and connector count are the speaker's claims; the incident site was "demo content", rebuilt and scrubbed.
- How viewer-scoped data is enforced (per-request auth vs cached) was not explained.
