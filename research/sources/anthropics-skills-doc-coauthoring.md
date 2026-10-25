---
title: "doc-coauthoring SKILL.md"
source_url: https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md
author: Anthropic
publisher: GitHub (anthropics/skills)
published: 2025-12-04
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [human-thinking-skills, prd-agents, rules-vs-judgment-encoding, tacit-knowledge-capture]
relevance: high
---

## Relevance to the project
A first-party, human-in-the-loop workflow for writing specs, PRDs, RFCs and decision docs: three stages (context gathering, section-by-section refinement, reader testing with a fresh no-context Claude). It is the strongest public example of a skill that is rigid in sequence but leaves every content decision to the human, and that tests the document with a sub-agent "reader" rather than a rubric. Bears on how a PM agent co-writes a PRD without taking authorship.

## Themes
- human-thinking-skills: per section: 5-10 clarifying questions, then brainstorm options, then the user picks what to keep "with brief justifications to help learn priorities for the next sections" (Stage 2, steps 1-3).
- prd-agents: explicit offer up front: "Ask if they want to try this workflow or prefer to work freeform. If user declines, work freeform" (When to Offer This Workflow).
- rules-vs-judgment-encoding: the gate is a simulated reader, not a checklist: predict 5-10 reader questions, then test them with "a fresh Claude instance (no context from this conversation)" to "catch blind spots" (Stage 3).
- tacit-knowledge-capture: "info dumping" asks for organisational context, "team dynamics, past incidents, politics", and "why alternative solutions aren't being used" (Stage 1).

## Key points
- Classification: control flow fixed stages, human chooses section order; gates = human approval per section + sub-agent reader test; standard form = questions and a reader test, no rubric; stance = ask, then draft under direction.
- Learns the author's style in-session: asks the user to say what to change instead of editing directly, "This helps learning of their style for future sections".
- Convergence rule: "After 3 consecutive iterations with no substantial changes, ask if anything can be removed".
- Sufficiency test for context: when "edge cases and trade-offs can be asked about without needing basics explained".

## Could not verify
- No outcome data. Last commit 2025-12-04 per GitHub API.
