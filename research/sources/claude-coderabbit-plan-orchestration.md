---
title: "How CodeRabbit used Claude to build an agent orchestration system"
source_url: https://claude.com/resources/articles/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-27
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [opportunity-to-code-chain, prd-agents, spec-edge-case-review, agent-ready-intent, cost-control-routing]
relevance: high
---

## Relevance to the project
CodeRabbit, reviewing about 2M PRs a week, reports the commonest AI-PR failure is code that compiles and passes tests but doesn't do what was meant, and traces it to unstated assumptions upstream of the model. Its fix is a planning layer in front of Claude Code that surfaces assumptions and produces a stakeholder-validated collaborative PRD, which Claude Code then turns into an implementation plan: direct evidence for plan-as-artifact and for the intent step in the opportunity-to-code chain. It also built an eval harness for plan quality, comparing runs with and without planning. Anthropic customer story; claims are CodeRabbit's, with no numbers on the planning layer's effect.

## Themes
- opportunity-to-code-chain: a planning phase before code generation; the plan "becomes a quality gate" (sections "An orchestration layer", "Catching errors before any code gets written").
- prd-agents: output is a "collaborative product requirements document" validated by stakeholders before implementation (orchestration section).
- spec-edge-case-review: best-practice questions ask Claude what is missing, which assumptions are implicit, which edge cases are forgotten (best practices box).
- agent-ready-intent: experienced developers omit "obvious" requirements; the login-page anecdote (section "Addressing the internal knowledge gap").
- cost-control-routing: Opus orchestrates, Sonnet sequences planning steps, Haiku for distillation and narrow tool use; eval-driven tier choice (section "Routing across the Claude model family").

## Key points
- **Failure mode (CodeRabbit's observation)**: compiles, passes tests, wrong intent; "late validation can be very expensive".
- **Layering**: explicitly not a replacement for Claude Code's Plan Mode but a higher-level orchestration before it; PRD then fine-grained implementation plan by Claude Code.
- **Plan eval harness**: hand-tuned examples, then a library of LLM judges scoring plan-quality dimensions; downstream measures of whether code worked, extra scope, tokens used; A/B with and without planning. Finding: too-granular plans go stale as the codebase shifts, too-high-level plans let assumptions back in.
- **Record of work**: a saved, reused "chronicle of planning artifacts" to check output against intent and onboard engineers.
- "MPP (maximum possible product)" is mentioned in best practices without explanation.
- Limits: no quantified gain from planning; no detail on who the stakeholders are or how validation happens; marketing format.

## Notable quotes
- "The plan itself becomes a quality gate." (David Loker, VP of AI)
- "If Haiku does as well as Sonnet on a given task, we use Haiku." (David Loker)

## Could not verify
- Any result numbers from the with/without-planning comparison; whether the planning system is a shipped CodeRabbit product or internal.
