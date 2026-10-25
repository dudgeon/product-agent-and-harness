---
title: "frontend-design SKILL.md"
source_url: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
author: Anthropic
publisher: GitHub (anthropics/skills)
published: 2026-09-03
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, skill-standards, standard-form-spectrum, taste-and-homogenisation]
relevance: high
---

## Relevance to the project
The clearest public example of a skill that encodes taste rather than steps. It works through a persona, a list of named "defaults" to avoid (an anti-exemplar library of what generated design clusters around), a plan-then-self-critique loop, and a stated deference rule ("the brief's own words always win"). It is a model for how a PM skill could encode taste for, say, PRD prose or strategy narratives: name the generic defaults, require a plan reviewed against the brief, then critique. Date is the last commit to the folder.

## Themes
- rules-vs-judgment-encoding: taste is encoded as (a) persona ("design lead at a design studio... client has already rejected proposals that felt cliché"), (b) five named clusters of AI-generated defaults (cream background with terracotta accent, SaaS-card kit, ALL-CAPS eyebrow labels, etc.), (c) principles with reasons ("visual structure is information"), (d) a two-pass plan-review-build process (section "Process: plan, review against the brief, build, critique").
- skill-standards: a "quality floor" is stated as a short checklist (responsive, keyboard focus, reduced motion, accessible) to be met "without announcing it", alongside the taste guidance (section "Restraint and self-critique").

## Key points
- Classification: control flow loosely fixed (plan, review plan against brief, build, critique); gates are model self-review plus screenshots "if your environment supports it"; standard form = principles + anti-exemplars + a small checklist floor; stance = do then self-critique; asks the user only to confirm the subject when the brief lacks one.
- The anti-default list is framed as calibration, not prohibition: "All traits are legitimate for some briefs, but they are defaults rather than choices".
- Self-test for genericness: "work through a similar prompt to see if you arrive somewhere similar"; if so, revise and "say what you changed and why".
- Memory as a taste aid: "if you have a space to quickly jot down notes about what you've tried, it can help you in future passes."

## Notable quotes
- "Spend your boldness in one place." (Restraint and self-critique)

## Could not verify
- No published evals for this version.

## Merged from a duplicate note of the same source (research-skill-rigidity-spectrum, 2026-10-25)

The same page was filed twice by two subagents; the second note is folded in here.

### Relevance to the project
Anthropic's own attempt to encode taste as a skill, and a clean specimen of the mixed form: about 1,300 words of design philosophy framed as a persona ("a design lead whose client rejects cliché or templated work"), a handful of hard rules (line length under 80 characters, one or two typefaces), a long list of named anti-patterns (the defaults the model otherwise reaches for), a process (plan, self-review for generic choices, build, critique) and a short checklist floor (responsiveness, focus states, reduced motion, accessibility). No rubric, no scores, no worked examples. It encodes taste mostly negatively, by naming what mediocre looks like, which is a practical answer to "can taste be encoded": partly, as anti-patterns plus a process that forces a deliberate choice.

### Themes
- standard-form-spectrum: philosophy and persona, a few concrete rules, named anti-patterns (cream background with terracotta accent, near-black with acid green, identical rounded SaaS cards, all-caps eyebrow labels, 01/02/03 markers), a process, and a quality-floor checklist; no rubric and no exemplars (whole file).
- taste-and-homogenisation: the skill exists because the model's default output converges on a recognisable "AI" aesthetic; its method is to list those defaults and forbid them, and to ask the model to "spend your boldness in one place" (design principles section).
- skill-standards: frontmatter name, description with trigger ("distinctive, intentional visual design"), license; prose body with about six sections (frontmatter, structure).

### Key points
- Process: token-based plan with ASCII wireframes, self-review against the brief for generic choices, then build and critique.
- Restraint is explicit: take risks only "if justified"; one place for boldness.
- Includes a UI-copy section (active voice, plain language, clear errors).
- Absent: scoring, before/after examples, reference images; the standard is carried by words and prohibitions alone.
