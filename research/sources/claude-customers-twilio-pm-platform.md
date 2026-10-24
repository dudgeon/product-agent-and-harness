---
title: A Twilio PM on building a self-learning development platform with Claude Code
source_url: https://claude.com/customers/twilio-qa
author: Anthropic (Q&A with Michael Carpenter, Director of Product, Programmable Voice, Twilio)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, evals-autonomy-trust, risk-sloped-review, org-learning-loop, build-vs-buy]
relevance: high
---

## Relevance to the project
A Twilio product director, working solo with Claude Code, built a "Feature Factory" that takes a brainstormed idea through subagents (architect, spec, tests, development, review, docs) and packages what it learns as a Claude Code plugin with 425 MCP tools: a rare first-hand account of a PM building a spec-to-code pipeline. Its sharpest contributions are a four-tier autonomy model for agent actions (read-only autonomous through never-autonomous) and a graduated path from six human approvals per feature to headless runs, earned over about 40 days. It also offers a build-then-buy view on memory and "dreaming": single-developer memory is a file problem, multi-tenant memory with audit trails is infrastructure. It bears on review-and-autonomy, harness-upkeep, target-user and context-and-memory. One person's account on an Anthropic page; outcomes are his claims.

## Themes
- non-engineer-builders: Carpenter, a PM "not a software engineer", reports more than 1,000 commits, 425 MCP tools, a published npm package and a plugin; credits his domain knowledge plus Claude holding the codebase in context (Q&A, "You built this as a product manager").
- risk-sloped-review: four tiers: (1) autonomous read-only queries; (2) guardrailed actions like a rate-limited test SMS; (3) human approval for deploys, webhooks, buying numbers; (4) never autonomous: deleting resources, force-pushing, skipping hooks. "CLI is for humans. MCP is for agents." (Q&A, "boundaries" answer).
- evals-autonomy-trust: day one had approval gates after each phase (six interruptions per feature); headless by day 45 after 23 design decisions; stall/oscillation/idle detection, safety floors on budgets, sandbox mode and phase retry added in turn; "Graduate trust with evidence, not hope" (Q&A, autonomy answer and advice).
- org-learning-loop: hooks capture learnings on every error into a file Claude reads, auto-cleared when docs are updated; a plain learnings file "failed within four sessions" (Q&A, Feature Factory answer).
- build-vs-buy: built local memory and dreaming himself to be "a good evaluator" of Managed Agents; multi-tenant memory with audit trails is "an infrastructure problem" (Q&A, memory answer).

## Key points
- **Problem.** Twilio's API surface is huge and failure modes silent (misconfigured webhooks don't error; parent/child call status confusion; errors logged where nobody looks).
- **Pipeline.** Brainstorm idea → subagents for architect, spec, test generation, development, review, documentation; custom skills capture domain knowledge each session. Output is a Claude Code plugin that any developer can install.
- **Claimed results.** Self-service IVR from multiple iterations to "5 minutes and one pass"; a pizza-ordering voice agent (recording, transcription, SMS) in 10 minutes; Claude found 29 more instances of a bug pattern by codebase search.
- **Silent tool failure.** The MCP server failed silently for 35 sessions (spawn, EOF, no warning); work continued without tools; fix was 53 lines of TypeScript. A useful failure-mode anecdote: harness misconfiguration can go unnoticed because the agent degrades gracefully.
- **Prompt over infrastructure.** Friction events (misdiagnosis, skipped validation, wrong tools) were fixed with a 40-line markdown file naming tools, forbidding skipping live-call phases and setting per-phase retry budgets, not with a queue runner or orchestration; "CLAUDE.md is your project's constitution".
- **Collaboration norms.** A day-four CLAUDE.md line asking Claude to "push back with evidence" is called the most important instruction.
- **Limits.** Solo project; no independent measure of code quality or use of the plugin by others; inconsistent timelines on the page (51 days in the intro, 1,000 commits over 90 days, headless by day 45 after 40 days of decisions).

## Notable quotes
- "Trust is architectural, not accidental." (Q&A, boundaries answer)
- "The system that captures knowledge has to be lower-friction than the discipline it replaces." (Q&A, advice)

## Could not verify
- Publication date (not shown). Carpenter's "writeup" referenced in the Q&A was not located or read.
- Whether the plugin and npm package are public, and their adoption.
