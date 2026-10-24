---
title: "OpenAI Codex lead on the new shape of product work | Andrew Ambrosino"
source_url: https://www.lennysnewsletter.com/p/openai-codex-lead-on-the-new-shape
author: Lenny Rachitsky (host), Andrew Ambrosino (product and engineering lead, Codex app, OpenAI)
publisher: Lenny's Podcast
published: 2026-06-28
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [human-judgment-pm-jobs, pm-persona-role-expansion, spec-becomes-prototype-and-evals, product-coherence-over-automation, status-update-agents, agent-as-service-many-surfaces, memory-architecture, intent-factory-before-discovery]
relevance: medium
---

## Relevance to the project
A first-party account from the lead of a major agent harness (the Codex desktop app) of how product work inside OpenAI has inverted: implementation is cheap, so dozens of uncoordinated prototypes of the same idea appear and the scarce work is curation and steering. He rejects "PRDs are dead": choose the medium for the point (document for clarity on a vague area, prototype for testing an interaction), and say aloud what stage an artefact is at because polish no longer signals maturity. Also useful: the Codex app was adopted by marketing, comms, finance and legal staff despite being "actively hostile" to them, and people would not move to general-purpose surfaces built for them. Bears on intent-shaping-and-spec, target-user, agent-interface and work-structure.

## Themes
- human-judgment-pm-jobs: "The implementation is actually not the expensive part anymore. It's, dare I say, taste. But it's the curation process" across, he guesses, "90 different uncoordinated teams" trying the same feature (3:09-4:50). Taste is mostly "If we can build anything, what's the goal here" (10:46).
- spec-becomes-prototype-and-evals: contradicts "PRDs are dead": non-engineers jump to prototypes and engineers write "a lot of documents that are not worth reading"; pick the format for the point (7:05). Medium used to imply process stage; now a production-looking prototype may have had no research, so state the stage explicitly (9:04, 35:39).
- pm-persona-role-expansion: "role collapse" is strongest in the Codex org because it is a technical product; your role is "the average of where you're working" (21:38). But eliminating the PM role is "a terrible idea" because disciplines have knowable best practices: "Yes, you can use Excel, but you cannot work on the finance team" (24:38-26:12). ICs now manage agents, managers manage at a different granularity: "everyone's kind of both now" (30:40).
- product-coherence-over-automation: product people run "zone defense", spread across the company to find gaps and guide from inception; hire product-minded engineers so a full team is not needed to review code "for product coherence" (29:00). Models "usually increase complexity"; "please make the models better at deleting code" (40:07).
- intent-factory-before-discovery: planning detail inversely proportional to horizon; nine-month plans stay hazy because precision is false (32:00). At his previous company: list all ideas, prototype all, ship what current models can do, re-test the rest at each model leap (32:00). The Codex app shipped February 2026 would have failed in November 2025 with the same shape; only models changed (33:31).
- status-update-agents: his "first vibe coordinated release": a Notion doc of everything that needed to happen, with automation gathering updates from PRs and Slack channels into the status tracker (43:51). Daily brief across "3,000 Slack channels" set up as a scheduled task he coaches in natural language ("next time this runs, can you please worry about this instead") (44:53).
- agent-as-service-many-surfaces: OpenAI tried putting Codex into the ChatGPT desktop app and Atlas for non-engineers, but "nobody would leave the Codex app"; marketing, comms, finance and legal used it although it showed code and asked approval to run commands (52:18-55:30). Vision: a "home base" where you start, end and automate work, which drives other apps (for example, the Excel add-in) instead of containing everything (56:23).
- memory-architecture: people build their own Obsidian or Notion "mind palace" for the agent; "You shouldn't have to do that. There should be a memory feature"; the product job is deciding which personal workflows become primitives (47:58).

## Key points
- Team shape (27:29): "double digits of engineers", about half that in design, a few product people; mostly ICs, many former founders. Everyone dogfoods the app even when it is not the best tool, so it becomes the best tool (21:38-23:11).
- Original Codex Web (give a task, get it back finished) was "too AGI-pilled for the moment"; Claude Code, local and asking questions, fit model capability better (35:39-37:10). Lesson: "you might need to release this thing six different times before it works", same shape; keep premature prototypes as artefacts to re-test.
- Supervised vs unsupervised code is the real question now that "100% of our product right now is AI written code" (40:07). Fully autonomous "improve the app" loops that listen to Twitter, Slack and email are not there yet; hard parts are choosing which features to build and building the right abstractions.
- Connector vs in-app browser vs Chrome extension vs computer use: the decision boundary was "all done through just feeling it out" (47:39).
- Bottom-up exploration culture is deliberate, because a team maintaining a product cannot also disrupt it (38:44).

## Notable quotes
- "Yes, you can use Excel, but you cannot work on the finance team" (26:12)
- "we were too AGI-pilled for the moment" (37:10)
- "Is the code written supervised versus unsupervised?" (40:07)

## Could not verify
- Medium podcast: read show notes and takeaways in full; transcript read 0:00-11:30, 21:38-56:30; design discussion (12:24-21:30) and lightning round skimmed by search.
- "90 explorations", "3,000 Slack channels" and adoption by non-engineering functions are his own unquantified remarks. No numbers on Codex app usage given.
- He leads a vendor product, so claims about its shape are partly promotional.
