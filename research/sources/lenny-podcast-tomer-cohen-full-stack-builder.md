---
title: "Why LinkedIn is turning PMs into AI-powered \"full stack builders\" | Tomer Cohen (LinkedIn CPO)"
source_url: https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms
author: Lenny Rachitsky (host), Tomer Cohen (CPO, LinkedIn)
publisher: Lenny's Podcast
published: 2025-12-04
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [agent-led-intent-shaping, spec-edge-case-review, one-job-per-agent, org-context-grounding, harness-over-model, build-vs-buy, pm-persona-role-expansion, human-judgment-pm-jobs, leadership-permission-mandate, outcome-measurement-gap, intent-factory-before-discovery, agent-factory-sdlc]
relevance: high
---

## Relevance to the project
The clearest first-party description of a large company building **persona critique agents for the front of the product process**: LinkedIn's heads of craft each built an agent (trust, growth, research, analyst) that critiques a spec or idea against LinkedIn's own history, plus a "product jam" agent meant to orchestrate them. Cohen says investment went first to "code to launch" and only later to "idea to design", which he calls "a material part of work" and where quality originates (26:43-27:28). That is close to the film's Helm concept (persona sub-agents that critique intent before hand-off) and to "the bottleneck moved to intent". It also carries two hard lessons for the register: giving agents access to all of Drive "failed miserably and hallucinates like crazy" (48:21), so curated "golden examples" won; and no off-the-shelf tool worked on LinkedIn's code or design system without customisation. Bears on context-and-memory, work-structure (one job per agent, later orchestrated), intent-shaping-and-spec, adoption-model and pm-agent-evaluation.

## Themes
- agent-led-intent-shaping / spec-edge-case-review: the trust agent takes a spec and lists "vulnerabilities, what harm vectors potentially you're introducing"; run against the two-year-old Open to Work spec it found the original issues and "all the holes that we did not catch until later" (19:58-21:59). The research agent, grounded in member personas, past research and support tickets, critiqued a marketing spec and "shifted the direction of the team" (21:59).
- one-job-per-agent: agents are single-job by design so each can be rated and graded; an orchestrator ("product jam agent") will hide them later and let them work back and forth rather than in sequence (23:31, 25:41).
- org-context-grounding: "Just reasoning over your entire knowledge base did not work"; the work was curating "gold examples" and linking past specs to outcomes (28:54-29:03); the drive-wide approach "failed miserably and hallucinates like crazy" (48:21).
- harness-over-model / build-vs-buy: "we haven't seen anybody be able to work off the shelf" on LinkedIn's code base and design system (18:16); knowledge agents start from Copilot Enterprise and ChatGPT Enterprise but "by far the most important part was basically our own customization" including the orchestrator (23:31). Platform pillar: rearchitecting core platforms into composable UI components "so AI can reason over it" (16:35).
- agent-factory-sdlc: two halves, idea-to-design and code-to-launch; maintenance agent plus QA agent handle "close to 50%" of failed builds (26:43).
- pm-persona-role-expansion: Full Stack Builder title and career ladder; APM program replaced by Associate Product Builder from January 2026 (coding, design and PM taught together); cross-functional pods assembled for about a quarter (14:55, 35:58, 49:52). A user researcher became a growth PM using the tools (42:57). Not everyone must be a full stack builder: "system builders" and specialists remain, in smaller numbers (48:21).
- human-judgment-pm-jobs: builders should keep vision, empathy, communication, creativity and judgment; "everything else, I'm working really hard to automate" (12:03-13:33).
- leadership-permission-mandate: 20/80 tech to change management (show notes); only the "cutting edge 5%" adopt unaided (38:24); levers: AI agency and fluency in hiring and the biannual performance review, 360s for his directs rated by other functions, celebrating wins at all-hands, exclusive access pods that must give feedback (40:39-44:45).
- outcome-measurement-gap: value formula is experimentation volume times quality divided by time to launch (31:54); evidence so far is "hours of work a week" saved and better insight discussions; not GA internally; "in six months or so" for top-line numbers (37:11).
- intent-factory-before-discovery: research used to mean "10 to 15 sources of information"; reviews multiplied (design, privacy, security); a small feature took "multiple teams, multiple code bases, multiple sprints" (7:07). His thesis: the work isn't complex, the process made it complex.

## Key points
- **Pilot status (late 2025):** announced end of 2024; first agent MVPs four to five months later after a couple of months of dedicated work, most of it cleaning the corpus (27:59). Agents are "MVP+"; internal GA expected in the following months. A core FSB team builds the track for all of R&D; pods get access on condition they give feedback (33:47).
- **Tool sprawl:** teams gravitated to different design tools (Figma, Subframe, Magic Patterns); "I don't want to have eight design agents in the company" (24:44). Convergence on tools proved hard (48:21).
- **Wins cited:** PMs building their own dashboards; designers and PMs picking up bugs from Jira and pushing PRs; a head of partnerships built a developer-portal connector himself (32:00, 34:27, 41:23). Semantic people and job search teams used parts of the toolset.
- **Top performers adopt most:** AI amplifies the best rather than levelling (38:24).
- **Retrospective lesson:** the small core team should have shown the wider org early tools sooner rather than working on the side (52:58).
- **Dating:** Cohen announced in this episode that he was leaving LinkedIn after 14 years (1:04:13), so the program's later fate is not covered here.

## Notable quotes
- "The work itself is not complex, but the process we made very complex" (7:07).
- "Just reasoning over your entire knowledge base did not work" (28:54).
- "I see a lot of companies roll out their agents and just expecting companies to adopt. It doesn't work this way" (38:24).
- "If you're looking for a formal reorg or declaration to start building differently, you're waiting too long" (44:45).

## Could not verify
- Transcript is a Substack auto-transcription; read in full.
- "70% of skills will change by 2030" and the fastest-growing-jobs stat are LinkedIn Economic Graph claims; method not given in the episode.
- "Close to 50%" of failed builds fixed by the maintenance agent and "hours a week" saved are spoken claims with no measurement shown. The trust-agent Open to Work example is a retrospective replay, not a prospective test.
- No numbers on how many people hold the Full Stack Builder title or use the agents.
