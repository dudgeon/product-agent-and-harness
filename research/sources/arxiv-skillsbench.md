---
title: "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks"
source_url: https://arxiv.org/html/2602.12670v1
author: Xiangyi Li (BenchFlow) et al. (about 36 authors)
publisher: arXiv
published: 2026-02-13
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, harness-portability, evals-autonomy-trust, single-agent-many-skills]
relevance: high
---

## Relevance to the project
The best cross-harness measurement of skills: same skills evaluated in Claude Code, Codex CLI and Gemini CLI. It finds that curated skills help on average, self-generated ones do not, and that harnesses differ in whether they actually use provided skills. Direct evidence on "portable vs quietly harness-specific": the format is portable, effective use is not.

## Themes
- harness-portability: Claude Code gains +13.9 to +23.3pp; Gemini CLI +13.6 to +17.4pp (best raw performance, 48.7% with Gemini 3 Flash); Codex CLI (GPT-5.2) reached 44.7% with skills but "frequently neglected provided Skills and implemented solutions independently".
- evals-autonomy-trust: 84 tasks, 11 domains, 7 harness-model configurations, 7,308 trajectories, three arms (no skills, curated, self-generated).
- skill-standards: curated skills +16.2pp average (24.3% to 40.6%), but 16 of 84 tasks got worse; self-generated skills -1.3pp; 2-3 skills best (+18.6pp), 4+ skills +5.9pp; comprehensive documentation -2.9pp; domain range Healthcare +51.9pp to Software Engineering +4.5pp.
- single-agent-many-skills: small model plus skills (Haiku 4.5: 27.7%) beat the same model without (11.0%) and approached Opus 4.5 without skills (22.0%); but stacking many skills dilutes gains.

## Key points
- Authors' limits: terminal-based containerised tasks, top-quartile skill quality (optimistic), no length-matched control, Gemini CLI timeout bug.
- Conclusion: "Skills efficacy is not universal but context-dependent."

## Could not verify
- Figure 2 caption (+12.66pp) disagrees with the text (+16.2pp); last third of the HTML not read; abstract says 86 tasks, body 84. Not peer reviewed (preprint).
