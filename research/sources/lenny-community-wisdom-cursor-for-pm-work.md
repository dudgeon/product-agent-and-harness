---
title: "Community Wisdom: Using Cursor for PM work, AI workflows for writers, tips for writing cold emails, building defensible moats, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-using-cursor-for
author: Lenny's Newsletter community (digest compiled by the Community Wisdom editor)
publisher: Lenny's Newsletter
published: 2025-11-30
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [non-engineer-builders, agent-failure-modes, human-review-gates, one-job-per-agent, prototyping-agents-limits, org-context-grounding, org-learning-loop, prd-agents]
relevance: medium
---

## Relevance to the project
Thread 2 ("Using Cursor for PM work") is a grounded practitioner discussion of PMs and designers making small production changes through a coding agent, at a B2B SaaS company with 5 PMs each paired with 5-8 developers. It lists concrete agent failure modes (unrelated "fixes", oversized changes such as upgrading a library, cheating on tests, ignoring conventions) and the guardrails teams put in place before opening the codebase to non-developers (documented practices as agent instructions, task sub-agents, a QA agent that can't edit code and a coding agent that can't edit tests). The consensus: the question is whether the whole SDLC supports a new contributor, not whether a PM can use the tool, and the best PM use today is prototyping on a branch. It bears on target-user, review-and-autonomy, work-structure (one job per agent) and the coding-agent hand-off at the edge of a PM harness. Thread 3 (writing with Claude Code) is marginal; threads 1, 4 and 5 are not relevant.

## Themes
- agent-failure-modes: an engineer's list: agents make unrelated "fixes"; escalate a failed UI tweak into upgrading the whole library; "cheat to ensure the tests pass", hardcoding outputs or rewriting the test; and ignore codebase conventions such as naming (thread 2). Another PM: poorly structured front-end code leads the AI to "either tries small fixes and fails or tries to rebuild the whole thing".
- one-job-per-agent / human-review-gates: teams heavy on AI split responsibilities so "the QA agent can never modify the code and that the coding agent can never modify the tests"; a hypothetical "copy change agent" would be a small team of agents, one of which checks for disallowed changes such as new modules or packages (thread 2).
- non-engineer-builders: a PM on a 3-engineer team treats "me + Cursor as a junior engineer": tickets groomed as normal and engineers PR-review every change; this "greatly increased our velocity" on deprioritised quality-of-life items (thread 2). Another PM on a 5-person team uses Cursor for bug investigation and Cursor plus Claude Code to write Jira tickets with codebase context, and has committed copy fixes to staging.
- prototyping-agents-limits: "the best use case for PMs today is in prototyping": branch or fork production, change with Cursor, deploy to a test environment, get user feedback, then hand engineering a change request with the branch, which they may merge or reimplement (thread 2).
- org-context-grounding: the friction "isn't the change itself, it's the surrounding knowledge" (tests, error handling, logging, styling); copy kept in a headless CMS lowers risk; a good design system lets you tell the agent which component or token to use (thread 2).
- org-learning-loop: weekly AI roundtables and pairing a developer with a PM early; "10x easier when you have an engineering partner that wants you to succeed" (thread 2).
- prd-agents: the more specific the change request, explained "as you would to an engineer", the better the agent performs (thread 2).

## Key points
- Costs: "If you spend 2 mins to do a text change and create 30 mins of work for someone else ... the whole practice becomes pointless" (thread 2). One PM is unsure it saves time in aggregate yet, but reports an unexpected benefit: the group understands the product and processes more holistically.
- Skills PMs say they needed: Git branches and frequent commits as rollback points, browser dev tools and DOM inspection, tightly scoped iterative changes; escalate to an engineer after 5-6 failed prompts (thread 2).
- A paradox raised by one engineer: if engineering has built the guardrails that make non-developer access safe, copy changes are no longer a chore for engineers, so the case for non-developer access weakens.
- Thread 3: a product-discovery author describes writing with Claude Code (outline feedback, per-section feedback, defined review criteria for intros and conclusions, fact-checking), framing it as "Claude on your machine with access to your file system" rather than a vibe-coding tool.

## Notable quotes
- "the question isn't whether a PM or a designer would be able to make changes ... but whether the whole SDLC supports that kind of thing" (thread 2)
- "Sometimes the agents cheat to ensure the tests pass." (thread 2)

## Could not verify
- Digest read in full; thread 2 filed in full and thread 3 briefly. Contributors are community members; evidence is anecdote. Names omitted, roles used (one contributor is a named product-discovery author in the digest).
- No numbers on velocity or defect rates were given; "greatly increased our velocity" is one PM's impression.
