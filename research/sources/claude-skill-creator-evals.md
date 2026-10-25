---
title: "Improving skill-creator: Test, measure, and refine Agent Skills"
source_url: https://claude.com/resources/articles/improving-skill-creator-test-measure-and-refine-agent-skills
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-03-03
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [evals-autonomy-trust, skill-standards, non-engineer-builders, harness-over-model, spec-becomes-prototype-and-evals]
relevance: medium
---

## Relevance to the project
Anthropic's skill-creator now writes evals, runs benchmarks, A/B-compares skill versions blind, and tunes trigger descriptions, aimed at skill authors who are subject-matter experts rather than engineers. That gives a no-code route to the eval-gated skills option under capability distribution, and its split between "capability uplift" skills (may become unnecessary as models improve) and "encoded preference" skills (durable, valued for fidelity to the team's process) is a useful lens for which PM skills to maintain. Evidence is the vendor's own description; the only results are a PDF-form fix and improved triggering on 5 of 6 public skills.

## Themes
- evals-autonomy-trust: evals define test prompts plus "what good looks like"; benchmark mode tracks pass rate, elapsed time and tokens; run after model updates to catch regressions ("Using evals to test and improve skills").
- skill-standards: two kinds of skill: capability uplift vs encoded preference (e.g. NDA review against set criteria, weekly updates drafted from several MCPs) ("Two kinds of skills").
- non-engineer-builders: Anthropic says most skill authors are subject-matter experts, not engineers; the tooling requires no code (intro).
- harness-over-model: if the base model passes a capability-uplift skill's evals without the skill, the skill may be retired.
- spec-becomes-prototype-and-evals: "Looking ahead": a SKILL.md is an implementation plan; evals already describe the "what", and that description may eventually be the skill.

## Key points
- Multi-agent eval runs: independent agents in clean contexts run evals in parallel with per-run token and timing metrics, avoiding context bleed between tests.
- Comparator agents judge two skill versions, or skill vs no skill, without knowing which is which.
- Trigger tuning: analyses the description against sample prompts and suggests edits to cut false positives and negatives; Anthropic reports improved triggering on 5 of 6 public document skills.
- Eval and results stay with the author: local storage, dashboards or CI.
- Example: evals isolated the PDF skill's failure on non-fillable forms; fix anchors text to extracted coordinates.
- Available in Claude.ai and Cowork, as a Claude Code plugin, and in the public repo.
- Limits: no figures on how often evals catch regressions in practice; eval quality depends on the author's test prompts and rubric; nothing on who reviews skills in an org.

## Notable quotes
- "testing turns a skill that seems to work into one you know works." ("Two kinds of skills")

## Added by research-skill-rigidity-spectrum (2026-10-25)
- The skill file itself is noted separately: anthropics-skills-skill-creator-skill-md. It carries the authoring stance behind the eval tooling: explain the why rather than "heavy-handed musty MUSTs"; all-caps ALWAYS/NEVER is "a yellow flag"; avoid overfitting to the few test prompts. Programmatic assertions are scripted, while qualitative review goes to a human in the viewer before the model revises. Theme: rules-vs-judgment-encoding.
