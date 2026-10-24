---
title: Stripe deploys Claude Code to 1,370 engineers with zero-configuration enterprise rollout
source_url: https://claude.com/customers/stripe
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [enablement-by-product, skill-supply-chain-security, enterprise-admin-controls, build-vs-buy, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
Shows how Stripe's developer-infrastructure team rolled out Claude Code: a signed enterprise binary co-produced with Anthropic over two to three months (to avoid the npm supply chain), pre-installed and pre-configured on every laptop and devbox, alongside five other coding assistants with no consolidation. That is a concrete adoption-model and runtime-distribution pattern (central pre-configuration, tool plurality, education as the main work) to set beside the Stripe teardown's knowledge-agent findings. Evidence is an Anthropic customer story; the 1,370 figure is engineers enabled, not active users, and the team states it has not isolated metrics for any single assistant.

## Themes
- enablement-by-product: pre-installed on every laptop and dev box, pre-configured with rules, tokens and authentication so no one makes an account or reads configuration ("Treating AI assistants like capable new engineers").
- skill-supply-chain-security: random JavaScript packages on corporate laptops were unacceptable; the signed binary bypassed the npm dependency chain ("Claude Code enables zero-friction adoption").
- enterprise-admin-controls: security concerns initially blocked deployment until the signed enterprise binary existed.
- build-vs-buy: six coding assistants enabled for different personas (infra engineers prefer CLI, product engineers in-editor); "going broad", no consolidation yet.
- vendor-claims-vs-independent-evidence: outcomes are sentiment ("The vibes are good") plus one migration anecdote; no productivity metric attributed to Claude Code.

## Key points
- Headline numbers (customer/Anthropic claims): 1,370 engineers with Claude Code enabled company-wide; 10,000 lines of Scala migrated to Java in four days vs an estimated ten engineering weeks by hand, unblocking a newer JDK.
- Biggest challenge stated as educational, not technical: engineers treated the assistant as a replacement and gave too little context. Mental model taught: a "new, capable engineer" who knows every language but lacks business context, the codebase and "the Stripe way". Delivered via all-hands, training sessions and "hint buttons" in internal tools; local, team-level prompt sharing worked better than central training.
- Ambition: agents for incident detection and resolution on the Agent SDK, given 5.5 nines reliability; MacVicar's four quadrants (humans only, humans with agents, agents with humans, agents only), aiming eventually for agents only.
- Named person: Scott MacVicar, developer infrastructure team lead.
- Limits: no date; engineering-only; no PM or knowledge-work use; no usage or retention data.

## Notable quotes
- "It's pre-configured with the rules, the tokens, the authentication." (MacVicar)

## Could not verify
- Publication date; whether 1,370 is enabled seats or active users over a period.
