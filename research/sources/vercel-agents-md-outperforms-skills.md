---
title: AGENTS.md outperforms skills in our agent evals
source_url: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
author: Jude Gao (Vercel)
publisher: Vercel blog
published: 2026-01-27
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, single-agent-many-skills, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The most-cited independent-of-Anthropic report of skills failing to fire. On Next.js 16 API tasks the agent never invoked the available skill in 56% of cases, so skills performed like no docs at all unless the prompt told the agent to use them. It shows that "agent decides when to load" (progressive disclosure) is also the failure point, and that always-on context (AGENTS.md) can beat on-demand skills for reference knowledge.

## Themes
- skill-standards: skill discovery depends on the agent choosing to load; description-matching is unreliable.
- single-agent-many-skills: counter-evidence for the "thousand skills" approach for knowledge that is always needed; Vercel sees skills as better for user-triggered, action-specific workflows (upgrades, migrations).
- evals-autonomy-trust: behaviour-based assertions on Build, Lint, Test; retries.

## Key points
- Pass rates: baseline 53%; skill default 53%; skill with explicit instruction 79%; AGENTS.md compressed docs index (40KB to 8KB) 100%.
- Instruction wording mattered ("MUST invoke" worse than "explore project first").
- Authors expect the gap may narrow as models improve at tool use.

## Could not verify
- Single-task-family, single-shot evals, vendor-run; not replicated independently. Critics (CircleCI, Codeminer42 etc. in search results) not read.
