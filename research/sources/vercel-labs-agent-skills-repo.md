---
title: "vercel-labs/agent-skills (react-best-practices, web-design-guidelines, writing-guidelines)"
source_url: https://github.com/vercel-labs/agent-skills
author: Vercel
publisher: GitHub (vercel-labs/agent-skills)
published: unknown
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, skill-standards, artifact-standardization]
relevance: medium
---

## Relevance to the project
Vercel's own public skills show two standards-enforcement designs worth copying for PM standards. react-best-practices is a rule library: 70 rules in 8 categories ranked by impact (CRITICAL to LOW), each in its own file with why it matters plus incorrect and correct examples. web-design-guidelines and writing-guidelines are thin shells (39 lines) whose only job is to fetch a centrally maintained rule list at run time and report findings in `file:line` form. The second pattern keeps the standard in one place, owned by its authors, and lets the skill stay stable while the rules change.

## Themes
- rules-vs-judgment-encoding: rule library prioritised by impact; each rule file pairs a reason with incorrect/correct code exemplars (react-best-practices "How to Use").
- skill-standards: "Fetch fresh guidelines before each review" from a raw GitHub URL; "Check against all rules in the fetched guidelines"; output in terse `file:line` format (web-design-guidelines, writing-guidelines).
- artifact-standardization: the same standard ships as a full compiled AGENTS.md for always-on use and as a skill for on-demand use (react-best-practices).

## Key points
- Classification: react-best-practices: control flow free; gate none (model applies rules); standard form = prioritised rule list with exemplars; stance = do/critique. Guidelines skills: control flow fixed four steps; gate = model check against fetched rules; standard form = remote checklist; stance = critique (review only).
- The thin-shell skill separates who owns the standard (a design or docs team editing one file) from who maintains the skill.
- Asks the user for files only if none are given.

## Could not verify
- No evals for these skills in the repo files read. The fetched rule files (command.md) were not read. The existing note vercel-agents-md-outperforms-skills covers Vercel's finding that an AGENTS.md index beat skills on its evals.
