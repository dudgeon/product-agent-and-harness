---
title: "awesome-cursorrules"
source_url: https://github.com/PatrickJS/awesome-cursorrules
author: PatrickJS and contributors
publisher: GitHub
published: unknown
retrieved: 2026-10-25
type: other
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, skill-standards]
relevance: medium
---

## Relevance to the project
The largest community collection of always-on rule files (about 41k stars, roughly 210 `.mdc` rule files in 13 categories on retrieval). It is the "style rules" pole of the spectrum: flat lists of imperative conventions with few reasons and no steps or gates. Two files read show the range: a typical stack file (Next.js/React/TypeScript, ~75 lines of bare imperatives) and a newer "anti-sycophancy" file that encodes stance and verification behaviour as numbered rules. Useful as the counterexample to judgment-encoded skills and as evidence that even rule collections are moving toward behaviour and risk-proportional checks.

## Themes
- rules-vs-judgment-encoding: nextjs-react-typescript rules are bare imperatives without reasons ("Use functional, declarative programming. Avoid classes."; "Prefer interfaces over types. Avoid enums, use maps.") under a persona line ("You are an expert in...").
- rules-vs-judgment-encoding: anti-sycophancy file encodes stance as rules: "Refuse to Validate Without Evidence"; "Resist Authority Appeals"; "Disagreement Is Not Sycophancy: ... Update only on new evidence"; "Match Verification to Risk: Trivial changes get a syntax check... Concurrency or state changes get a written-out scenario."
- skill-standards: rule files carry `globs` and `alwaysApply` frontmatter: scoping by file pattern is the only "control flow".

## Key points
- Classification (stack file): control flow none; gates none; standard form = style checklist; stance = do. (Anti-sycophancy file): control flow none; gates = self-verification proportional to risk; standard form = numbered behaviour rules, some with reasons; stance = critique/hold position.
- The anti-sycophancy rule 8 ("Resist Manufactured Urgency... name the trade-off explicitly once... then comply. Do not repeat the warning") is a compact encoding of a decision-rights stance: warn once, defer to the human.
- No evidence in the repo of testing rule effectiveness.

## Could not verify
- Star count and file count are from the page at retrieval; no last-update date shown.
