---
title: "Community Wisdom: AI doomerism, speeding up discovery in a big org, verifying engineering answers as a new PM, where analytics adds the most value, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-ai-doomerism-speeding
author: Lenny's Newsletter community (Slack members); compiled by Kiyani
publisher: Lenny's Newsletter
published: 2026-09-26
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [agent-ready-intent, spec-becomes-prototype-and-evals, docs-as-code-prd, intent-factory-before-discovery, risk-sloped-review, tacit-knowledge-capture, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
The "merging discovery and delivery in a large organization" thread starts from a new PM at a large financial company whose project has gone two months without front-end code while designs and a long PRD are finalized. One reply describes, in concrete detail, a setup that maps closely onto the project's intent-shaping options: design shipped as code in a running "showcase" app, the PRD modelled as a version-controlled typed JSON "intent model" that AI codegen builds from, open questions as a field rather than a blocker, quality enforced by lint and pre-commit checks instead of gate meetings, and a version pin separating the fast loop from the regulated release train. The same reply says the bottleneck moves to "how fast someone can decide". It is one community member's anecdote, but it is the most specific practitioner description of a structured, agent-ready spec in a regulated-style setting filed so far. Bears on intent-shaping-and-spec, artifact-and-project-structure, review-and-autonomy and adoption-model.

## Themes
- agent-ready-intent: the PRD "is modelled into a typed JSON, not prose": an "intent model" of entities, state machines, mutation contracts and acceptance rules, version-controlled; "AI codegen builds from it directly instead of from 40 pages of English"; undecided items go in an `open_questions[]` array, "a field, not a blocker" (thread 2, reply from a member who builds a white-label mail client for ISPs).
- docs-as-code-prd: the structured model is canonical; human-readable PRDs are generated from it on demand "in any level of simplicity", and an LLM can be pointed at it for answers; structure makes it "easier for the AI to traverse, enforce rules" and "LLMs are also less likely to mess with it" (thread 2, follow-up reply).
- spec-becomes-prototype-and-evals: "The design is the spec, and it already compiles": the design system is a real npm package; screens are built as interactive code in a showcase app deployed to a URL where stakeholders comment on the running screen; close to 100 key screens in 775 states (loading, empty, error, offline, dark mode, Arabic RTL) (thread 2).
- risk-sloped-review: "Quality comes from guardrails instead of gate meetings": rules (no hardcoded hex, accessibility, i18n for all user-facing strings, contrast floors) are lint rules or pre-commit checks, so "a junior dev or an AI agent literally cannot commit a violation"; finalization "became automated and continuous instead of a milestone" (thread 2).
- intent-factory-before-discovery: same reply: "This doesn't remove the bottleneck, it rather moves it. Once designs can change in an afternoon, the constraint becomes how fast someone can decide." They keep a one-line-per-entry decisions log (thread 2).
- tacit-knowledge-capture: in thread 3 (a new PM who cannot verify engineers' "yes we can" answers), one reply says decisions, architecture, constraints and the "why" often "live with people. When those people leave, that knowledge can leave with them too", so capture it somewhere durable.
- outcome-measurement-gap: a "top find" quotes Mik Kersten (Planview): in a typical enterprise "the number of development teams could be doubled with no appreciable increase in business outcomes", and "AI magnifies that distinction because it adds enormous capacity to whatever system is already there" (Top finds 1).

## Key points
- Thread 2, the original post: in a large financial company, a PM two months into a new project; the head designer (15 years at the company, Figma, perfectionist) wants designs fully signed off and user-tested before implementation, which could take another month; developers idle. The PM proposes building early concepts, releasing to internal users for feedback weekly, and iterating PRD and design together.
- The detailed reply's org answer: the fast loop and the release train are separated by a version pin. The showcase app consumes the design system straight from the monorepo and changes hourly; the shipping app consumes published, versioned packages and pulls when its engineering lead decides, with its own QA, testing and release. "This is what makes this sellable inside a regulated org." The context is described as "SLA-grade, so not a low-stakes context".
- The original poster did not understand "PRD written in JSON" and asked whether it is converted back to Word for teammates; answer: generate readable PRDs from the canonical model whenever needed.
- Other replies call the problem a transformation and politics issue; advice is to find a couple of champions who want to work differently and run a small pilot that brings developers into discovery and prototypes the risky technical pieces, rather than changing the whole process two months into the job.
- Another reply names "prototype-based discovery" (measures behavior, not stated attitude) and the "burnt pizza" problem: a rough prototype of a good idea can get the idea killed, which may be why a designer wants polish first; reframe as getting real usage signal "without risking the idea looking half-baked".
- Thread 3 advice for decisions resting on unverifiable engineering answers: match verification to stakes (hallway yes/no to rule out; T-shirt size to prioritize; a spike ticket before committing a timeline; a proof of concept when risky and uncertain); separate facts from stories; ask "how confident are you?".
- Thread 4 (analytics): one PM says their lead product analyst is building a skill to automate event-catalog and tracking work, "but guess what: it's harder to get it right than we all think".
- Thread 1 (AI doomerism) is off-topic except one member's remark on how fast everyone "switched their Claude to auto mode".

## Notable quotes
- "Your bottleneck isn't the designer being slow. It's that the design artifact is dead." (thread 2)
- "Anything undecided goes into an open_questions[] array—a field, not a blocker." (thread 2)
- "A junior dev or an AI agent literally cannot commit a violation." (thread 2)
- "the constraint becomes how fast someone can decide" (thread 2)

## Could not verify
- Community Slack thread; all claims are the posters' own and unverified. The mail-client company is not named; "regulated org" is the poster's framing of their customers (ISPs), not of a bank. The JSON example image referenced in the thread was not in the text and was "generated ... with Claude" by the poster.
- The 100-screen and 775-state numbers are the poster's own.
- Threads 1 and 4 read but filed only where relevant.
