---
title: DESIGN.md Explained - The Format Reshaping How AI Builds UI
source_url: https://departmentofproduct.substack.com/p/designmd-explained-the-format-reshaping
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-04-27
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [artifact-standardization, product-coherence-over-automation, agent-failure-modes, pm-persona-role-expansion, prototyping-agents-limits, docs-as-code-prd]
relevance: medium
---

## Relevance to the project
Explains Google's open-sourced DESIGN.md: one plain-text file that gives agents a design system as machine-readable tokens (YAML at the top) plus human-readable rationale (markdown below), separating the "what" from the "why". For the project it is a clean precedent for an agent-native artifact standard that pairs exact values with prose for judgement calls, the same split a PM spec or intent standard could use, and it comes with a linter (including a WCAG contrast check). Its strongest PM-relevant argument is a failure mode: AI output that looks finished suppresses the critique the PM-design-engineering hand-off used to supply, and consistency is not coherence. The facts about Google's spec are second-hand; the hands-on parts are the author's own trials.

## Themes
- artifact-standardization: DESIGN.md as a design counterpart to README.md, standardised by Google after a year of ad hoc copies; works in Stitch, Cursor, Claude Code and Claude Design ("What is DESIGN.md").
- docs-as-code-prd: the two-layer file (tokens for machines, prose for judgement) is a pattern a PM artifact standard could copy; prose like "never crowd elements" guides cases tokens don't cover ("two layer structure").
- product-coherence-over-automation: "consistency gets easier but coherence gets harder": shared components don't make a journey feel coherent; Spotify's large component library with screens that feel chaotic is the example ("potential impact").
- agent-failure-modes: agents don't notice a missing token, they fill the gap plausibly, and the divergence spreads while looking consistent, so it is harder to diagnose; and polished output suppresses criticism ("feedback loop breaks down"; "design system becomes more critical").
- pm-persona-role-expansion: predicts "design-flavoured" PM and engineering roles, PMs adjusting flows directly in AI design tools, designers moving to system stewardship; cites VC Gokul Rajaram's claim that design is "the first AI casualty" and notes the pushback.
- prototyping-agents-limits: author's trial: Stitch builds a draft app plus design system in one shot from an uploaded DESIGN.md; Claude asks clarifying questions before producing a brand guidebook ("Hands-on").

## Key points
- **Format:** YAML front matter with exact tokens (hex colours, type sizes, spacing, radii, component styles); markdown body with rationale and do's and don'ts.
- **Linter:** Google's CLI checks files for errors and rule violations; one rule resolves a component's background and text tokens to hex and warns below WCAG AA 4.5:1 contrast.
- **Impacts argued:** the design system becomes a more critical artifact because agents amplify its gaps; design literacy becomes a baseline for PMs; designers freed for interaction, motion and new metaphors.
- **Prompts offered (described, not reproduced):** a live split-pane DESIGN.md editor/preview; an interview wizard that generates a DESIGN.md; a plain-language completeness reviewer for non-technical staff; a migration mapper from Tailwind/CSS variables/Figma tokens.
- **Resources:** Google's spec repo (github.com/google-labs-code/design.md) and Stitch docs.

## Notable quotes
- "Finished-looking artifacts suppress criticism" (section "The feedback loop starts to break down")

## Could not verify
- Google's spec and CLI behaviour were not checked against the repo; the contrast rule is as described by the author.
- Gokul Rajaram's quote was an embedded image.
- Paywalled text summarised, not reproduced.
