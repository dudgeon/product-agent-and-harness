---
title: "How to turn your AI into a world-class designer"
source_url: https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world
author: Anshu Chimala (guest author; former Apple engineering and design lead), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-09-01
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [prototyping-agents-limits, one-job-per-agent, task-context-isolation, cost-control-routing, human-review-gates, evals-autonomy-trust, product-coherence-over-automation]
relevance: medium
---

## Relevance to the project
A guest post on getting coding agents past generic "AI slop" design, organised as a Double-Diamond-style process "reimagined for a team of AI agents". Its most transferable idea for a PM harness is the **critic subagent loop**: the builder agent may not judge its own work; a separate, stronger model in a fresh context sees only a screenshot (no code, no prior critiques), scores against an explicit bar, and the loop stops only when the critic independently clears it. This is a concrete, tested pattern for the persona-critique sub-agents in the film's Helm concept, with a cost result (the strong critic used under 10% of output tokens) and practical cautions (objective criteria, reference examples, stopping rules). It also reinforces that the human's job is steering and subtraction: most polishing effort goes into removing things and rewriting copy by hand. Bears on work-structure, review-and-autonomy, model-provider-coupling (routing models by role) and prototyping limits.

## Themes
- prototyping-agents-limits: LLMs default to the most predictable design choice ("the ultimate case of design-by-committee"); asking for randomness doesn't help because the model "can only predict the most likely token" (Discover, Technique 1). Agents "love to add more, but rarely take away" (Technique 6).
- one-job-per-agent / task-context-isolation: the critic is invoked "in a fresh context, with just the screenshot, not the code, implementation details, or earlier iterations/critiques"; the agent "isn't objective: it reviews its own code, past decisions, and previous rationale" (Technique 3).
- cost-control-routing: a cheap, fast model implements while a big model critiques; the critic (Claude Fable 5) accounted for "less than 10% of output tokens" and direct redesign by the big model would have cost about twice as much (Technique 3). The author recommends scoped, spend-limited API keys stored in a gitignored file for agents (Technique 4).
- evals-autonomy-trust: critic criteria graded bad/OK/great; best is concrete and comparative ("Here are 5 designs: 4 professional examples and 1 screenshot of our product. Rank them"); keep the pass threshold out of the critic prompt so scoring stays objective; set stopping criteria or the agent "will helplessly burn tokens" (Technique 3).
- human-review-gates: human judgment in Deliver: cut elements, check for listed AI tells, and have "a human read each line of copy" (Techniques 6-8).
- product-coherence-over-automation: banning AI patterns up front is discouraged because it makes the model "overthink and introduce even stranger patterns"; review against the list instead (Technique 7).

## Key points
- **Discover:** seed strings (String Seed of Thought, Sakana AI): have the agent generate a random string by shell script and derive the creative direction from it, producing genuinely varied outputs (Technique 1). Ambitious, specific prompts grounded in the human's own taste; use AI to list ideas, react to them in your own words, then have AI write the build prompt (Technique 2). Save failed prompts and retry them on new models.
- **Define:** critic loop (Technique 3); image generation via built-in tools, the Codex CLI on a ChatGPT subscription, or a scoped API key (Technique 4); video models via an aggregator for animated graphics and keyframe-interpolated transitions (Technique 5).
- **Deliver:** subtraction, AI-tell review and hand-written copy (Techniques 6-8).
- Models named: Claude Opus 5, Claude Fable 5, GPT-5.6 Sol, Seedance 2.5; demos built "in two" or "three prompts" (intro).

## Notable quotes
- "Your work is only complete when the critic independently deems it 9/10 or higher" (Technique 3 prompt).
- "When polishing AI designs, most of my effort goes into removing things" (Technique 6).

## Could not verify
- Post read in full (text only; demo images and videos not viewed).
- The "<10% of tokens" and "twice as much" cost figures are the author's own runs; the number of runs is not stated. Results are aesthetic judgments by the author.
- About design of landing pages and consumer apps, not product-management artifacts; transfer of the critic pattern to specs is our inference.
