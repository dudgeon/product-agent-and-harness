---
title: "Introducing Roast: Structured AI workflows made easy"
source_url: https://shopify.engineering/introducing-roast
author: Obie Fernandez (Shopify Augmented Engineering DX team)
publisher: Shopify Engineering blog
published: 2025-06-18
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [harness-over-model, skill-standards, agent-frameworks, org-learning-loop]
relevance: low
---

## Relevance to the project
This is the pre-River precursor of Shopify's agent tooling (mid-2025). It established the pattern that recurs in later posts (Dispatch, the River remediation ledger): interleave deterministic steps with agent steps, use Claude Code as the "CodingAgent" step, and save every run for replay. It matters to the teardown mainly as lineage and for one privacy-relevant use case: an SRE workflow that **scans internal Slack channels**.

## Themes
- `harness-over-model`: "AI agents need help staying on track ... Allowing AI to roam free around millions of lines of code just didn't work very well. Non-determinism is the enemy of reliability."
- `agent-frameworks`: Roast is a convention-over-configuration Ruby gem / CLI. YAML workflows plus markdown prompts (ERB), shell steps, inline prompts, Ruby steps and parallel steps. Built on Raix. An OpenAI key or OpenRouter is required.
- `skill-standards`: workflows are version-controlled and testable. Its stated hope is "Workflow marketplaces emerge where teams share battle-tested workflows."
- `org-learning-loop`: steps share a conversation transcript. Session replay lets a run resume from any step.

## Key points
- **CodingAgent tool** "integrates Claude Code directly into workflows". Inline prompts prefixed `^` go to Claude Code.
- **Internal uses:** test grading at scale, and **Boba** (Sorbet type annotations: deterministic sed/autocorrect, then the CodingAgent fixes the rest). An SRE team "periodically scan[s] internal Slack channels for early indicators of emerging issues". There is also competitive-intelligence aggregation (web, CRM customer conversations), and a "Chesterton's Fence" code-history research tool.
- Sam Schmidt's quote: use an AI step as a placeholder, then replace it with deterministic code once the problem is understood.
- Open source at github.com/Shopify/roast.

## Notable quotes
- "Non-determinism is the enemy of reliability."
- "I have also joked that Roast helps you set your money on fire as you find new ways to burn millions of tokens."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- Whether Roast is still used under River/Aquifer in 2026. Port's software-factories page lists "Workflow: Roast, Boba" in Shopify's stack, but no 2026 first-party post was found that connects Roast to Aquifer.
