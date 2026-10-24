---
title: "The new product introduction process: How to make sure your Agent is ready every time you ship"
source_url: https://www.intercom.com/blog/npi-how-to-ensure-your-agent-is-ready-every-time-you-ship/
author: Intercom (Fin NPI Manager; byline not captured)
publisher: The Intercom Blog
published: 2026-06-26
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, human-review-gates, opportunity-to-code-chain, org-learning-loop, compounding-context-repo]
relevance: high
---

## Relevance to the project
A release process that treats the AI support agent's knowledge as a **launch gate**: "A feature should only be considered 'shipped' when the Agent can answer questions about it correctly." Each release produces an input package: a "what we built" doc that PMs and engineers submit to the release tracker, plus notes from walkthroughs, demos and GTM kick-offs. An agent (Operator) turns that package into gap analysis, draft public articles and internal guidance, and FAQ tests. A named NPI manager owns it, and resolution rate and CX score are monitored for 2-4 weeks. This is the strongest example of "write-back from shipped work" in the library, applied to business knowledge rather than code. It shows where a context-creation step sits in the opportunity-to-code chain: at the *end* (code → knowledge), owned by a human, with an agent drafting.

## Themes
- tacit-knowledge-capture: knowledge managers join product walkthroughs and GTM kick-offs; notes and demo summaries go into a single input package with the "what we built" doc.
- human-review-gates: agent readiness is a hard release sign-off; content is drafted by Operator and tested before launch.
- opportunity-to-code-chain: adds a step after code: shipped → the agent's knowledge is updated, tested and monitored.
- org-learning-loop / compounding-context-repo: duplicates are retired, a canonical source is chosen, and early support conversations are folded into tests.

## Key points
- The "what we built" doc fields: owner, beta start date, planned release date, plan availability, how it works, troubleshooting.
- Operator prompts: find content to update, likely wrong answers and gaps; then draft public and internal articles.
- Testing: generated FAQs plus beta feedback, tested in the customer environment; root causes classed as a content gap, inaccurate content, or poorly structured content.
- Monitoring: a Monitor on launch topics, with resolution rate and CX score for 2 weeks (standard launches) or 4 weeks (complex ones).

## Could not verify
- No outcome numbers. Vendor blog (Intercom sells Fin and Operator), so partly product marketing.
