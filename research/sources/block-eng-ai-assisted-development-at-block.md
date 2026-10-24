---
title: AI-Assisted Development at Block
source_url: https://engineering.block.xyz/blog/ai-assisted-development-at-block
author: Angie Jones (AI Enablement for Engineering, Block)
publisher: Block Engineering Blog
published: 2026-01-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [harness-portability, build-vs-buy, org-learning-loop, enablement-by-product, agent-factory-sdlc, human-review-gates]
relevance: high
---

## Relevance to the project
Corrects a common reading that Block runs everything through goose: for engineering, Block "buys them all" (Claude Code, goose, Cursor, Copilot, Cline, Amp, Firebender) and keeps the repo harness-neutral with AGENTS.md and a rules generator. Goose is one harness among several for engineers; the shared assets are the repo context, skills and recipes. Bears on the harness-portability and build-vs-buy questions.

## Themes
- harness-portability: open-source `ai-rules` generates CLAUDE.md, AGENTS.md, `.cursor/rules/`, `.clinerules/`, `firebender.json` from one rule set; repos carry AGENTS.md plus a human HOWTOAI.md and `.goosehints` (governance and repo practices).
- build-vs-buy: "We buy them all. Well, not all, but a lot!" (Provide the Freedom to Explore); Block plans to standardise later once the market settles.
- org-learning-loop / enablement-by-product: about 50 AI Champions spend 30% of their time on repo-level AI enablement; gamified "Repo Quest" tracks AI-readiness in four tiers; teams contribute recipes and skills to shared libraries.
- agent-factory-sdlc: agents take scoped tickets from Linear and Jira, open PRs, fix CI; "Humans only step in at review time." (Automated PRs).
- human-review-gates: AI-usage attribution in commits and PR labels for significant AI contribution.

## Key points
- About 95% of engineers regularly use AI for development. Most run one agent outside an IDE; the next group runs 3-5 in parallel; a small group is building an internal agent orchestrator.
- Three months after the Champions programme: AI-authored code +69%, reported time savings +37%, automated PRs 21x (self-reported, no method).
- Largest monorepo: 40,000+ source files, 650+ deployable services.
- Workflow: RPI (Research, Plan, Implement) across separate sessions to stop drift.

## Could not verify
- Models used internally, distribution of goose, and the internal orchestrator (later announced as Builderbot: [block-builderbot-rollout](block-builderbot-rollout.md)) are not named here.
