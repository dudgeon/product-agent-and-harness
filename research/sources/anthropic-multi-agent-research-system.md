---
title: How we built our multi-agent research system
source_url: https://www.anthropic.com/engineering/multi-agent-research-system
author: Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford (Anthropic)
publisher: Anthropic Engineering blog
published: 2025-06-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, single-agent-many-skills, cost-control-routing, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
Names which *kind of work* multi-agent fits (breadth-first, parallelizable, open-ended research) and which it does not (coding, shared-context, many dependencies), with cost data. It is the Anthropic-side companion to Cognition's post and the best published example of a "research synthesis" agent shape. Written for a research product, not for team process standardization.

## Themes
- work-structure-spectrum: open-ended research where steps cannot be planned in advance suits an orchestrator with subagents; coding has "fewer truly parallelizable tasks".
- cost-control-routing: agents use about 4x chat tokens, multi-agent about 15x; token use explained about 80% of performance variance on BrowseComp; the task must be valuable enough to pay.
- evals-autonomy-trust: start evals with about 20 real queries; LLM-as-judge with a rubric plus human testing; evaluate end state for stateful agents.

## Key points
- Lead Opus 4 plus Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on Anthropic's internal research eval (vendor-reported).
- Limits: agents "are not yet great at coordinating and delegating to other agents in real time"; small lead-agent changes can change subagent behaviour unpredictably.

## Could not verify
- Internal eval not independently reproduced.

## Added by research-skill-rigidity-spectrum (2026-10-25)
- Checked for a runtime critic role: there is none in production. Subagents self-assess with interleaved thinking after each tool result; the CitationAgent runs after the loop to attach citations (the post does not say it verifies claims); the lead agent decides when enough has been gathered without stated criteria. The LLM-as-judge (single call, 0-1 scores plus pass/fail against a rubric of factual accuracy, citation accuracy, completeness, source quality, tool efficiency) is an offline evaluation tool, not an in-loop reviewer.
- Human testers caught what the judge missed (early agents preferring SEO content farms), fixed via source-quality heuristics in prompts.
- Self-improvement: Claude 4 models diagnosed prompt failure modes and rewrote a flawed MCP tool description, cutting later task time by 40% (vendor claim). Relevant to dimension 7 (self-rewriting skill) and to dimension 5: critique here is applied to the agent's own tools and prompts, not to the human.
