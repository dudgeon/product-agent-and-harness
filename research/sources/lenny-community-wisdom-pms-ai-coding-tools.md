---
title: "Community Wisdom: How PMs are using AI coding tools, implementing reverse free trials, distinguishing yourself as a product manager vs. project manager, pricing your consulting work, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-how-pms-are-using
author: Lenny's Newsletter community (digest edited by Kiyani)
publisher: Lenny's Newsletter
published: 2026-02-14
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [agent-ready-intent, one-job-per-agent, org-context-grounding, human-review-gates, ai-synthesis-hallucination-risk, pm-persona-role-expansion, prd-agents, intent-factory-before-discovery]
relevance: high
---

## Relevance to the project
Two threads from the members-only Slack bear on the project; the rest (consulting pricing, reverse trials) do not. The "How PMs are using AI coding tools" thread contains two of the most concrete practitioner descriptions of an intent-to-agents pipeline we have: an engineer-founder whose requirements file, checked by a "project manager" agent for dependencies and open questions, is the handoff to TDD, front-end and back-end agents; and a Director of Product at a healthcare data company (a regulated setting) running 13 role-based agent configs (clinical lead, data architect, commercial strategist) preloaded with a 400+ line project instruction file. Both say the human's time moves to refining requirements and verification. This is close to the film's "Helm" concept (persona sub-agents, human steers) and to intent-shaping-and-spec and review-and-autonomy. Community anecdotes, self-reported numbers.

## Themes
- agent-ready-intent: the engineer-founder's "two big unlocks" start with "keeping exhaustive requirements for everything I do. Quality acceptance requirements and context for a change significantly improves agent outputs" (thread 4).
- intent-factory-before-discovery / prd-agents: his flow: unstructured brain-dump to Claude, a dedicated requirements agent drafts a requirements file, he reads and edits the whole thing ("my most valuable step"), then a "project manager" agent with its own context checks "for dependencies and unanswered questions" before any build agent runs (thread 4).
- one-job-per-agent: he runs a TDD agent writing tests against acceptance criteria, a front-end agent and a back-end agent; "more than that and I lose the ability to validate quality" (thread 4). The healthcare director runs 13 role configs via BMAD and GSD with a Compound Engineering plugin as meta-context (thread 4).
- org-context-grounding: the healthcare director's project instruction file is "400+ lines: data model, team contacts, release schedule, SQL conventions"; "Every session starts with all of that loaded. The agents aren't guessing" (thread 4). Claude connects to Notion, Asana and GitHub for wiki, feedback tickets and reports.
- human-review-gates: "The ceiling is verification ... I review more than I produce now ... the skill shifts from doing to directing and QA" (healthcare director, thread 4); the engineer-founder spends most time "refining requirements, reviewing acceptance criteria and spot-checking tests".
- ai-synthesis-hallucination-risk: another PM finds AI summaries of 15 Zoom transcripts "often mischaracterizes and misses nuances" and warns against relying on them for discovery (thread 4).
- pm-persona-role-expansion: thread 2 (product vs project manager): a PM in a non-Silicon-Valley org says where "you have org-level processes to adhere to (either for audit reasons or just org history)" a PM cannot do product work without separate project management support; dependency, funding and deadline load pushes PMs into project management (thread 2).

## Key points
- Healthcare director's claimed results: customer feedback analysis from half a day to 20 minutes; 36 drug-specific slide decks in 83 minutes using Python and parallel execution; SQL from plain English; weekly status reports, 1:1 prep, Slack announcements. Voice (Wispr Flow) to Claude-structured PRDs; Obsidian knowledge base read and written by Claude (thread 4).
- His caveat: "If you can articulate what 'good' looks like in your domain, these tools get you there 10x faster. If you can't, they'll confidently hand you garbage." And "how do you ever know if you've built the right thing?" is unchanged by AI (thread 4).
- Slides: he points to Anthropic's pptx skill but says it still needs template slides, context, assets and ideally 4-6 example decks (thread 4).
- A founder prototypes before involving engineers ("gets my ideas through about 100x faster"), has delayed GTM hiring, and fixes small cosmetic bugs himself because engineers now use Claude Code and bugs are rare (thread 4).
- The engineer-founder writes ~90% of code with agents; the Claude Chrome extension gave agents visibility into front-end errors (thread 4).

## Notable quotes
- "I specifically have it check for dependencies and unanswered questions." (engineer-founder, thread 4)
- "The ceiling is verification." (Director of Product, healthcare data company, thread 4)
- "They'll confidently hand you garbage." (same, thread 4)

## Could not verify
- Read the full digest; filed threads 2 and 4 only. Threads 1 (consulting pricing) and 3 (reverse trials) are out of scope.
- All numbers are self-reported by community members. The healthcare company's regulatory controls on agent access to clinical data were not described.
