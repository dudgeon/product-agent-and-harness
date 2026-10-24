---
title: "\"Engineers are becoming sorcerers\" | The future of software development with OpenAI's Sherwin Wu"
source_url: https://www.lennysnewsletter.com/p/engineers-are-becoming-sorcerers
author: Lenny Rachitsky (host), Sherwin Wu (Head of Engineering, OpenAI API platform)
publisher: Lenny's Podcast
published: 2026-02-12
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [human-review-gates, risk-sloped-review, harness-over-model, tacit-knowledge-capture, enablement-by-product, org-context-grounding, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
First-party numbers from inside OpenAI's API engineering org. 95% of engineers use Codex daily, Codex reviews 100% of PRs, review time fell from 10-15 to 2-3 minutes, heavy users open 70% more PRs, and engineers steer 10-20 parallel threads. Two claims matter most for the project. First, agent failures are "usually a problem with context", fixed by encoding tribal knowledge into the repo as .md files and skills. Second, "models will eat your scaffolding for breakfast", including today's skills and file-based context. Bears on review-and-autonomy, context-and-memory, harness-upkeep and adoption-model. Note that the speaker is a model vendor.

## Themes
- human-review-gates / risk-sloped-review: Codex reviews every PR; human attention goes "from 100% attention to 30%"; small PRs sometimes need no human review; the team is "very thoughtful ... around which PRs are completely just Codex-reviewed" (15:27-18:03).
- tacit-knowledge-capture: when the agent fails, "you've either underspecified or there's just not enough information"; the fix is to "encode more tribal knowledge" in comments, code structure, .md files and skills (12:44-14:16). An internal team maintains a 100% Codex-written codebase with no manual "escape hatch" to surface these problems (12:44).
- harness-over-model (counterpoint): "the current scaffolding which is fashionable is Skills, files-based context management", and it may be eaten as models improve, as vector stores and agent frameworks were (44:13-47:20). Build for where models will be (49:08).
- enablement-by-product: many enterprise deployments are probably negative ROI because they are top-down mandates without bottom-up adoption; recommends a staffed "tiger team", often technical-adjacent non-engineers such as an ops lead or "Excel wizard" (37:59-43:39).
- org-context-grounding: managers use ChatGPT connected to GitHub, Notion and Google Docs to write performance-review research; he expects larger spans of control (21:20).
- evals-autonomy-trust: engineers' "bar of trust" rises over time; longer coherent tasks (METR: multi-hour at 50%, about an hour at 80%) will need products that give feedback mid-run (5:26, 50:34).

## Key points
- Engineers are "managing fleets and fleets of agents" and their job is to steer and review (7:28). Stress when agents stall is real (12:27).
- CI and post-push work (lint fixes, restarts) are automated with Codex to cut engineer toil (16:57).
- The API stack in layers: Responses API, Agents SDK (sub-agents, guardrails), AgentKit UI widgets, evals API (1:05:37-1:07:08).
- Business-process automation (SOP-driven work outside tech) is underrated (53:47).

## Notable quotes
- "The models will eat your scaffolding for breakfast." (0:51, attributed to a Fintool founder)
- "It's more like going from 100% attention to 30% attention." (18:03)

## Could not verify
- Transcript read 0:00-23:33, 37:40-52:05 and 1:05:37-1:08:17; the rest (management philosophy, startup advice, lightning round) was skimmed by search. The 95%, 100%, 70% and 2-3 minute figures are spoken; the method behind them isn't given. He says the code-authorship share is hard to attribute and he "wouldn't make the statement" that 100% of production code is AI-written (19:08). The negative-ROI claim is his impression, explicitly not quantitative (37:59).
