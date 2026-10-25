---
title: Skill authoring best practices
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
author: Anthropic
publisher: Claude Platform Docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, skill-standards, work-structure-spectrum, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
Anthropic's own authoring guide states the rigidity question directly: "set appropriate degrees of freedom" by matching specificity to "the task's fragility and variability", with high, medium and low freedom tiers and a narrow-bridge vs open-field analogy. It is the clearest first-party statement of where scripts, templates and free text each belong in a skill, and the closest thing to a vendor rule for the research-skill-rigidity-spectrum question. It bears on how PM skills should mix fixed checks (completeness) with judgment (quality).

## Themes
- rules-vs-judgment-encoding: three tiers: high freedom (text instructions, "multiple approaches are valid", "decisions depend on context"); medium (pseudocode or parameterised scripts, "a preferred pattern exists"); low (exact scripts, "operations are fragile", "consistency is critical", "a specific sequence must be followed") (section "Set appropriate degrees of freedom").
- rules-vs-judgment-encoding: template pattern has two strictness levels: "ALWAYS use this exact template" for data formats vs "a sensible default format, but use your best judgment" (section "Template pattern").
- skill-standards: the validator need not be code: a style-guide file serves as the "validator" Claude checks against, in a draft-review-revise loop (section "Implement feedback loops").
- work-structure-spectrum: plan-validate-execute: write a plan file, check it with a script, then act; recommended for "batch operations, destructive changes, complex validation rules, high-stakes operations" (section "Create verifiable intermediate outputs").
- evals-autonomy-trust: evaluation-driven development: run without the skill, record failures, build three scenarios, then "write minimal instructions" to pass them (section "Build evaluations first").

## Key points
- Default assumption is that "Claude is already very smart": add only context it lacks; every paragraph must "justify its token cost".
- Degrees of freedom: the robot analogy. Narrow bridge with cliffs: exact instructions (example: database migrations in a fixed sequence). Open field: general direction (example: code review where "context determines the best approach").
- Checklists the model copies into its response and ticks off are the recommended form for multi-step work, both for code (PDF form filling) and for non-code work (a research synthesis workflow with a "verify citations" step that loops back).
- Conditional workflow pattern: decision points that route to sub-workflows (create vs edit).
- Examples pattern: input/output pairs convey style "more clearly than descriptions alone".
- Scripts: "prefer scripts for deterministic operations"; scripts should "solve, don't defer" (handle errors rather than leave them to Claude); make clear whether to run or read a script.
- Iteration: "Claude A" writes the skill, "Claude B" uses it on real tasks; observed failures go back to A. One suggested fix is stronger wording ("MUST filter" instead of "always filter"), which sits in some tension with skill-creator's advice to avoid all-caps MUSTs (see anthropics-skills-skill-creator-skill-md).
- Test with every model you will run: what works for Opus may need more detail for Haiku. Rigidity is partly a function of model capability (my reading).

## Notable quotes
- "Match the level of specificity to the task's fragility and variability." (Set appropriate degrees of freedom)
- "Narrow bridge with cliffs on both sides: There's only one safe way forward." (same)

## Could not verify
- No publication date on the page. No data on how much each tier improves outcomes; the guidance is assertion plus examples.
