# Prior work found (2026-10-24)

What was found before starting any new research: earlier intent-shaping and intent-factory work. The full notes are in the shared research library.

## The two substantial artifacts (Claude Docs, written in Claude)

- **Building and Accelerating the Intent Factory**: [source note](../../research/sources/geoff-building-accelerating-intent-factory.md)
  - Automate intent shaping and delivery before using AI for discovery.
  - Models Stripe's and Ramp's eight-step loop.
  - Five actions: delivery automation as a goal, factory capacity, agent-ready intent, a versioned shaping skill, a compounding context repo.
- **Intent Shaping in a Well-Managed Environment**: [source note](../../research/sources/geoff-intent-shaping-well-managed-environment.md)
  - Risk review as specification and classification.
  - A risk-advisor agent that specifies, classifies and augments, with evaluation via SME labels.

Themes extracted from them are in [THEMES.md](../../research/THEMES.md):
- `intent-factory-before-discovery`
- `agent-led-intent-shaping`
- `agent-ready-intent`
- `compounding-context-repo`
- `risk-sloped-review`
- `risk-review-as-classification`

## Options by dimension

These are the options and key questions the two docs imply, filed in [options/DIMENSIONS.md](../../options/DIMENSIONS.md).

**New dimensions I propose:**
- [review-gating](../../options/DIMENSIONS.md#review-gating-how-human-review-of-agent-output-is-gated): human review of every change vs risk-scored auto-approve vs upstream risk classification at shaping time
- [context-location](../../options/DIMENSIONS.md#context-location-where-product-context-lives-for-agents): scattered vs a shared plain-text context repo vs systems of record queried by agents. Overlaps with [memory-design](../../options/DIMENSIONS.md#memory-design-memory-design); they may later be merged.
- [intent-shaping-mode](../../options/DIMENSIONS.md#intent-shaping-mode-who-shapes-intent-and-how): PM-led bespoke vs a versioned shaping skill vs agent-led interrogation vs prototype-first vs agent-originated intent
- [spec-standard](../../options/DIMENSIONS.md#spec-standard-what-counts-as-agent-ready-intent): narrative PRD vs an evidence-tied spec with a completeness standard vs prototype-as-spec vs a canonical spec plus mitigations vs a spec pushed straight to coding agents
- [investment-sequencing](../../options/DIMENSIONS.md#investment-sequencing-where-to-invest-first): delivery factory first vs shaping layer first vs discovery first

**Added to existing sections:**
- [harness-ownership](../../options/DIMENSIONS.md#harness-ownership-who-owns-the-harness-the-agent-loop): key question 7, on deferring build-vs-buy by keeping the shaping and context layer harness-agnostic
- [Cross-cutting key questions](../../options/DIMENSIONS.md#cross-cutting-key-questions): question 3, on whether the target is a regulated organisation

- [pm-agent-evaluation](../../options/DIMENSIONS.md#pm-agent-evaluation-how-we-would-know-a-pm-agent-works): two options (intent-factory KRs; classification accuracy against SME labels) and key question 3

**Possible overlaps** (not merged):
- review-gating vs review-gate-placement: same axis, but one covers delivery and code, the other PM-agent output.
- context-location vs org-context-grounding-source: largely the same choice.
- investment-sequencing vs pm-job-sequencing: stage-level vs job-level "what first".

None of these pick a winner. Where Geoff's docs lean, the lean is recorded together with what would change it.

## Related, not yet read or filed

- From PM idea to code: how Stripe and Ramp actually do it: https://claude.ai/artifact/5VxwzYPzfWwGPUx4iQ3eQD
- Current State: sources and endnotes: https://claude.ai/artifact/LTjj2wcKTSbKQPXY8DLhmb
- Specs as Theory Building (and Extended Cut): https://claude.ai/artifact/Rmg9fZP8QWFJtY8XE9C2dr, https://claude.ai/artifact/967zr5dq9oxSreAzzy3zxe
- `~/repos/pm-harness`: an open-source "PM harness" project covering:
  - goals for harness design R&D
  - a PM moves taxonomy
  - beacon teardowns (Ramp, including a Glass / intent-shaping hypothesis test)
  - an effort-delegation baseline
  - a context ecosystem

  Its `project/` folder holds the vision, decisions, open questions and wiki.
