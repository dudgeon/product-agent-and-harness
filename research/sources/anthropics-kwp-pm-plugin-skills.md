---
title: "knowledge-work-plugins: product-management plugin skills (write-spec, product-brainstorming, synthesize-research)"
source_url: https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management/skills
author: Anthropic
publisher: GitHub (anthropics/knowledge-work-plugins)
published: 2026-01-30
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [rules-vs-judgment-encoding, prd-agents, human-thinking-skills, research-synthesis-agents, artifact-standardization]
relevance: high
---

## Relevance to the project
These are the actual SKILL.md files behind Anthropic's Cowork product-management plugin (the plugin itself is noted in anthropic-cowork-plugins-product-management). Read side by side they show three different points on the rigidity spectrum for PM work in one first-party bundle: a template-and-criteria PRD writer, a deliberately non-deliverable sparring partner, and a methods-heavy synthesis workflow. None has a deterministic gate; all standards are prose criteria the model applies to itself. Files read from the installed plugin and checked identical to the repo (last change to the skills folder 2026-03-18).

## Themes
- rules-vs-judgment-encoding: write-spec is a fixed 5-step workflow (understand, gather context, pull from connected tools, generate, review) plus a required 8-section PRD outline, plus judgment criteria per section ("goals should be outcomes, not outputs"; "if everything is P0, nothing is P0"); no scripts or schema checks.
- prd-agents: write-spec tells the agent to ask conversationally ("do not dump all questions at once"), to tag each open question with who must answer and blocking/non-blocking, and "do not include questions you can answer from context".
- human-thinking-skills: product-brainstorming states "Your job is not to generate deliverables. Your job is to think alongside the PM" and lists Do Not rules such as "Do not generate a list and hand it over" and "Do not agree with everything".
- research-synthesis-agents: synthesize-research fixes the extraction fields (observations, quotes, behaviours, pain points) and a frequency x impact matrix, and adds judgment tips ("a finding from 2 interviews is a hypothesis, not a conclusion"; "5-8 strong findings are better than 20 weak ones").
- artifact-standardization: the PRD shape is standardised (problem, goals, non-goals, user stories, P0/P1/P2 requirements with acceptance criteria, metrics, open questions, timeline); acceptance criteria in Given/When/Then or checklist form.

## Key points
- Classification (my reading):
  - write-spec: control flow fixed steps; gates none (only "ask the user if any sections need adjustment"); standard form = template + rubric-like criteria + a worked SSO example; stance = do, with light ask.
  - product-brainstorming: control flow model-chosen ("identify which mode fits the conversation and adapt"; four modes: problem exploration, solution ideation, assumption testing, strategy); gates none; standard form = frameworks as "thinking tools, not templates" (HMW, JTBD, opportunity solution trees, SCAMPER, OODA, reverse brainstorming) plus a five-phase session rhythm (frame, diverge, provoke, converge, capture) and named anti-patterns (feature parity trap, one-idea brainstorm, brainstorming when you should be researching); stance = critique and ask ("be opinionated", "push back").
  - synthesize-research: control flow fixed steps; gates none; standard form = methods reference (thematic analysis, affinity mapping, triangulation) + output outline; stance = do.
- The brainstorm skill keeps decision rights with the PM: "The brainstorm is not the decision"; "If one idea excites the PM, explore it".
- Size: SKILL.md files run 94 to 388 lines; most of the length is domain reference (frameworks, metric lists), not procedure.
- Tool use is conditional: "If these tools are not connected, work entirely from what the user provides. Do not ask the user to connect tools."

## Notable quotes
- "Use frameworks as thinking tools, not templates to fill in." (product-brainstorming)
- "Be ruthless about P0s." (write-spec)

## Could not verify
- No eval results or usage data for these skills are published. The README's skill names (feature-spec etc.) differ from the folder names (write-spec etc.), suggesting renames.
