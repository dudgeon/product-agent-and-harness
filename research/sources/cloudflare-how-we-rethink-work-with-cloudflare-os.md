---
title: How we're rethinking work at Cloudflare with Cloudflare OS
source_url: https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/
author: Sam Rhea (CIO, Cloudflare)
publisher: Cloudflare Blog
published: 2026-08-05
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [org-context-grounding, non-engineer-builders, org-learning-loop, legible-org-for-agents, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
The adoption story behind Cloudflare OS: principles, the engineering vs non-engineering split, rollout mechanics and self-reported numbers. Useful for the user/product dimensions (who to serve, how adoption happens) and as a second internal-platform account next to Ramp Glass. Entirely self-reported.

## Themes
- [[non-engineer-builders]]: the early mistake was giving non-engineers developer tools with friendlier skins; they ran a 'magic AI email alias' where staff sent unwanted work to a small team, then turned patterns into skill files and connections.
- [[org-learning-loop]]: shared library of context and skills so one person's improvement benefits everyone.
- [[legible-org-for-agents]]: an 'Engineering Codex' with domain owners that agents use to plan, review MRs and designs; self-reported ~250,000 problems flagged and 16,000 merges blocked in four months.
- [[evals-autonomy-trust]]: principle 3 'humans own the output'; managers inherit a departed employee's agents; principle 5 agents never grant more access than the user has.

## Key points
- Trigger: a sales employee asked for API keys to ~a dozen production systems to build an AI 'SuperApp'.
- Five principles (customer focus, usable tools for non-engineers, human ownership, curated context over model, no more access than the user).
- v1: browser workspace in a container behind Zero Trust; MCP servers Cloudflare builds itself to add rate limits by role/region; inference via AI Gateway with logging, DLP and model gating. v2: users describe a workflow, an agent writes the app; apps run on demand/schedule/event; Gatekeepers remove API-key management.
- Self-reported: thousands of weekly users, >4,000 apps/tools in 30 days, sales estimates >10,000 hours saved in a month. Adoption via champions and interns. No method for measuring success is given.

## Could not verify
- Numbers are internal estimates and unverified. A Spanish-language outlet repeated the 10,000-hours figure; not independent.
