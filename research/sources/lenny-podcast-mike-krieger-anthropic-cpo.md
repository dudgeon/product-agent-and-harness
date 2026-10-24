---
title: "Anthropic's CPO on what comes next | Mike Krieger (co-founder of Instagram)"
source_url: https://www.lennysnewsletter.com/p/anthropics-cpo-heres-what-comes-next
author: Lenny Rachitsky (host), Mike Krieger (chief product officer, Anthropic)
publisher: Lenny's Podcast
published: 2025-06-05
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [intent-factory-before-discovery, human-review-gates, agent-factory-sdlc, opportunity-to-code-chain, org-context-grounding, pm-tool-connectivity, human-judgment-pm-jobs, outcome-measurement-gap, evals-autonomy-trust, product-coherence-over-automation, feedback-triage-agents, product-artifact-primitives]
relevance: high
---

## Relevance to the project
Anthropic's CPO describes, first-hand and in mid-2025, what happens to product development when most code is AI-written: the bottleneck moves **upstream** to "decision making and alignment" and **downstream** to merge queues, review and coherent launches; the Claude Code team shifted from line-by-line PR review to Claude reviewing Claude plus human "acceptance testing". He sketches the chain this project calls opportunity-to-code (read feedback channels, propose solutions, open a PR, run an A/B test) and says the limit is context flow, not model reasoning. This is primary evidence for the film's "the bottleneck moved to intent" claim, from a vendor insider (so first-party on Anthropic's practice, but also an interested party). It bears on intent-shaping-and-spec, review-and-autonomy, context-and-memory, sequencing and pm-agent-evaluation. Note the date: it predates the November 2025 model jump that other sources cite, so its percentages are early.

## Themes
- intent-factory-before-discovery: "there's an upstream bottleneck, which is decision making and alignment"; Krieger is working on "the minimum viable strategy to let people feel empowered to go run and type and build" and admits "I don't think I've gotten that right yet" (14:25).
- human-review-gates: the Claude Code team moved from line-by-line review to "use a different Claude to review it and then do the human almost acceptance testing"; PRs are "larger than most people are going to be able to review"; risk: a codebase "unmaintainable or even understandable by Claude" (15:43).
- agent-factory-sdlc: merge queue "completely re-architect[ed]" because of PR volume; "Over half of our pull requests are Claude Code generated" (0:03, 12:53); Claude Code itself "95% plus" written by Claude Code (his guess, 17:13); the stated anchor is ~90% of code AI-written (11:55).
- opportunity-to-code-chain: step one, the model reads Discord, user forums and X and reports "what's emergent"; step two, proposes solutions; then "I put together a pull request" and "spin up an A/B test" (19:20-20:51). Example: an Artifacts "copy" vs "export" button complaint in a feedback channel that he wanted turned into a revert PR within an hour.
- org-context-grounding: "We're limited more around making sure the context flows through all of that ... more than the model's capability to reason and propose" (19:20); his "fake equation": utility = model intelligence × context and memory × applications/UI (54:45).
- pm-tool-connectivity / product-artifact-primitives: Claude.ai's own primitives (projects, Artifacts, styles, conversations) "should all just be exposed to an MCP" so Claude can write back, e.g. add output to project knowledge (56:25-58:00); "This shouldn't be a feature that we're building. This should just be an MCP that we're exposing" (56:25).
- human-judgment-pm-jobs: product's remaining value is making AI "comprehensible", strategy ("where we'll play"), and "opening people's eyes" to close the capability "overhang" (24:38-26:55); knowing "what to ask the AI, how to compose the question" is still a specialized engineering skill (12:53).
- product-coherence-over-automation: downstream bottleneck is "how do we make sure that we're still building something coherent and packaging it up" for launch, enablement and feedback (15:43).
- feedback-triage-agents: same opportunity chain; models "can do that today" for step one (19:20).
- evals-autonomy-trust: best API customers have "a repeatable way to evaluate how well your product is serving those use cases" when a new model drops: A/B tests, internal evals, "capturing traces and being able to rerun them"; customers' own "Cursor bench", "Harvey bench" matter more than public benchmarks (52:25).
- outcome-measurement-gap: engagement metrics mislead; value is "did it actually help you get your work", e.g. a prototype in "20, 25 minutes" that would have taken "six hours", but "It's harder to quantify" (1:01:58).

## Key points
- Roles have not changed even though engineering has: "the suite of people that come together to produce a product hasn't yet ... I think for the worst"; the biggest shift is PMs and designers building functional demos earlier with Claude and Artifacts (12:53).
- Strategy partner: Krieger writes a strategy and has Claude critique it; with Opus 4 plus research it first produced "a new angle that I hadn't been looking at" (5:00). Prompting: "think hard"; "Be brutal, Claude, roast me"; Console prompt improver, since "Claude itself is a very good prompter of Claude" (27:26-29:05).
- Org design at Anthropic: almost all product leverage comes from PMs embedded with research (post-training), not UX on top of an off-the-shelf model; "the functional unit of work at Anthropic is no longer take the model and then go work with design and product" (22:07). Founder-type engineers matter more than headcount; Claude Code started as one senior IC's internal project (34:25).
- Durable startup moats (1-3 years): domain workflow knowledge (Harvey's lawyer-specific flows; healthcare and legal compliance), go-to-market that knows the buyer persona, and new interaction form factors (47:47-50:51). Relevant to regulated settings only in passing: Krieger spent early time with financial services and insurance companies building on the API (45:25).
- Collaboration design: "Claude has no chill" in a Slack channel; elicitation must balance asking versus doing so Claude acts as "a true collaborator", preserving user agency (59:40).
- Example of contributions widening: a non-TypeScript employee fixed a Claude Code annoyance "from that to pull requests in an hour" by talking to Claude (17:13).

## Notable quotes
- "We really rapidly became bottlenecked on other things like our merge queue" (0:03).
- "there's an upstream bottleneck, which is decision making and alignment" (14:25).
- "The difference between the right context and not. It's entirely the difference between a good answer and a bad answer" (54:45).
- "Got to figure out the right pithy metric dashboard version of that" (1:01:58, on measuring value delivered).

## Could not verify
- Full transcript read (Substack auto-transcription, minor errors such as "Claudia AI").
- Percentages are spoken estimates: "95% plus" for Claude Code is "my guess ... I'll come back with the real stuff"; show notes say "90-95% of code for some products". As of mid-2025; superseded by later Anthropic figures in other sources.
- First-party but vendor: Krieger is describing his own company and product.
- A separate attendee write-up of Krieger's later summit remarks is filed as note-krieger-pm-summit-remarks.
