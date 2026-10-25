---
title: 3 Principles for Designing Agent Skills
source_url: https://engineering.block.xyz/blog/3-principles-for-designing-agent-skills
author: Angie Jones (AI Enablement for Engineering, Block)
publisher: Block Engineering Blog
published: 2026-02-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [skills-marketplace, skill-standards, harness-portability, org-learning-loop]
relevance: high
---

## Relevance to the project
Block runs an internal Skills marketplace of 100+ SKILL.md skills with role bundles, versioned in a repo with PR review, consumed by whichever agent the engineer uses. With recipes and MCP servers, this is the third packaging unit at Block, and the one that is cross-harness. The design rule (scripts own what must be consistent, the agent owns interpretation) is directly reusable for PM skills.

## Themes
- skills-marketplace: "over 100 skills" plus curated bundles (`frontend`, `android`, `iOS`); skills in a version-controlled repo with PR, review and history.
- skill-standards: SKILL.md folders with scripts, templates, MCP servers and config; supported by Claude Code, goose, Cursor, Amp, Copilot, Gemini CLI, VS Code.
- harness-portability: skills are the harness-neutral layer at Block.
- org-learning-loop: documentation becomes something an agent can execute; examples: POS crash investigation, feature-flag experiments, oncall runbook, API style guide, code review.

## Key points
- Principle 1: know what the agent should not decide (Repo Readiness uses a bash script with binary checks so scores reproduce).
- Principle 2: know what the agent should decide (interpretation, tailored content, conversation).
- Principle 3: "Write a constitution, not a suggestion": explicit constraints such as never recalculating script scores.
- Bonus: design for the arc: let output become input for follow-ups in the same session.

## Could not verify
- Whether non-engineering roles have skill bundles; the examples are engineering.

## Added by research-skill-rigidity-spectrum (2026-10-25)
- Form of the standard: Block's third principle, "write a constitution, not a suggestion", is the explicit-constraint form (named prohibitions such as never recalculating script scores) rather than the explained-reasoning form Anthropic's January 2026 constitution for Claude takes; both reject soft phrasing, but Block's version is closer to a short rule list and Anthropic's to a long argument. Together with Principle 1 (binary bash checks so scores reproduce) it puts Block's skills at the checklist-plus-hard-rules end of dimension 3, with interpretation (Principle 2) left to the model and no rubric or exemplar layer described in the post. Themes: standard-form-spectrum, gate-judge-separation.
