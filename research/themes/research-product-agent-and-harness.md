# Theme evidence: research-product-agent-and-harness

Written only by the task `research-product-agent-and-harness`. Built into ../THEMES.md by ../build.py.

## intent-factory-before-discovery: Accelerate the intent factory before discovery
Automating intent refinement and delivery has to come before using AI for higher-order discovery, or more ideas just swell the backlog. This sets the order of priorities for what a product agent should do first.
- [Building and Accelerating the Intent Factory](sources/geoff-building-accelerating-intent-factory.md): the core thesis and order of operations (§Introduction) (research-product-agent-and-harness)

## agent-led-intent-shaping: Agents shape intent, not only execute it
Agents do the research, interrogation and spec-tightening that turn rough intent into shovel-ready requirements, with humans answering and deciding. This is the core job of a "product agent".
- [Building and Accelerating the Intent Factory](sources/geoff-building-accelerating-intent-factory.md): Ramp's parallel research agents write each finding to a file; seven-question interrogation; agent-originated intent (§Vision, steps 1–3) (research-product-agent-and-harness)
- [Intent Shaping in a Well-Managed Environment](sources/geoff-intent-shaping-well-managed-environment.md): an iterative owner/risk-advisor loop in which mitigations become requirements and the spec tightens (§Iterative intent-shaping) (research-product-agent-and-harness)

## agent-ready-intent: A shared standard for agent-ready specs
Intent is complete enough for agentic delivery when it meets an agreed standard (templates, examples, evals) that gates delivery and improves from delivery feedback.
- [Building and Accelerating the Intent Factory](sources/geoff-building-accelerating-intent-factory.md): a spec, not a PRD; a completeness standard as a KR (Action 3) (research-product-agent-and-harness)
- [Intent Shaping in a Well-Managed Environment](sources/geoff-intent-shaping-well-managed-environment.md): a canonical spec artifact that absorbs detail and mitigations for re-assessment (risk agent, function 1) (research-product-agent-and-harness)

## compounding-context-repo: Context that compounds with each shipped feature
A shared, agent-readable, harness-agnostic store of product context ("evidence, not yet fact", with domain owners), which every spec writes back to. This is the harness's memory layer.
- [Building and Accelerating the Intent Factory](sources/geoff-building-accelerating-intent-factory.md): a plain-text context repo, a domain owner per topic, spec write-back (Action 5) (research-product-agent-and-harness)

## risk-sloped-review: Human review sloped to risk
How much human review agent output gets depends on how risky it is. Where that line sits is a key harness and governance design choice, especially in regulated organisations.
- [Building and Accelerating the Intent Factory](sources/geoff-building-accelerating-intent-factory.md): Ramp auto-approves low-complexity PRs; Stripe requires human review on every change (§Vision, step 7) (research-product-agent-and-harness)

## risk-review-as-classification: Risk review as a specification and classification problem
Risk advisory works as classification against a known taxonomy, with a curation path for novel risks. That makes a risk agent tractable to build and straightforward to evaluate with SME labels.
- [Intent Shaping in a Well-Managed Environment](sources/geoff-intent-shaping-well-managed-environment.md): a MECE taxonomy, component-by-risk scoring, false positives and negatives as heuristic fixes (§Risk review as classification; §Evaluation) (research-product-agent-and-harness)
