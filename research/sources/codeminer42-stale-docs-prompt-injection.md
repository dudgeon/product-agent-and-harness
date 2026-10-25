---
title: Stale docs are prompt injection you wrote yourself
source_url: https://blog.codeminer42.com/stale-docs-are-prompt-injection-you-wrote-yourself/
author: Edy Silva
publisher: The Miners (Codeminer42 blog)
published: 2026-10-16
retrieved: 2026-10-25
type: article
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [stale-records-mislead-agents, decision-rationale-records, human-review-gates]
relevance: high
---

## Relevance to the project
The most concrete account found of a team keeping a decision-record set healthy when agents both read and write it: deterministic CI checks for structure and drift, an AI review skill for code-vs-record contradictions, and a human who attests. Its counts of decay before the controls are rare numbers on how process artifacts rot in multi-party, agent-heavy repos.

## Themes
- stale-records-mislead-agents: once an agent reads an ADR it is an instruction; an untrue record misleads and the agent cannot tell (thesis).
- decision-rationale-records: one decision per file with imperative title; status and relations in frontmatter; merged records immutable, changed by superseding; index generated from frontmatter and omits superseded records (body).
- human-review-gates: "AI checks; humans attest": agent drafts the record and maintains the index, deterministic scripts check structure and drift in CI, an AI skill checks code against records, a human makes the final call (body).

## Key points
- Observation (unmeasured method): agents open individual records far more often than the index, so each record must stand alone.
- Before controls: three duplicate record numbers; seven phrasings for four status relations; five accepted records rewritten after merge.
- One record mandated Conventional Commits; 178 of the last 200 commits used ticket prefixes instead.
- Of 289 ADR citations in code, 225 used numbers that existed in two or more stacks; 24 exception comments pointed to the wrong record.
- Index grew to 156 standing records in about 2,800 words; CI warns above 800 words per record.
- Three example AI reviews caught code drifting from accepted records while tests and ADR checks were green.
- Next step proposed: turn checkable decisions into lint rules with a shrinking baseline and a canary violation per rule.
- Promotes an adr-setup skill (vendor-adjacent; Codeminer42 is a consultancy).

## Notable quotes
- "AI checks; humans attest."
