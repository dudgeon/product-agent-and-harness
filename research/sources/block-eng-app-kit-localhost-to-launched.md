---
title: "From Localhost to Launched: Safely Shipping Apps That Anyone Can Build"
source_url: https://engineering.block.xyz/blog/from-localhost-to-launched-safely-shipping-apps-that-anyone-can-build
author: Jude Edwards (Block)
publisher: Block Engineering Blog
published: 2026-06-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [non-engineer-builders, enterprise-admin-controls, skill-standards, ai-synthesis-hallucination-risk, org-learning-loop]
relevance: high
---

## Relevance to the project
Block App Kit is the sanctioned path for employees to publish agent-built internal apps on real company data: the agent generates, the platform owns auth, secrets, data access and hosting. It was first an MCP server and is now distributed to employees as a skill, so it is harness-neutral. About four in five users are outside engineering. This is the most concrete first-party example of "packaging a capability as a skill plus a platform" for non-engineers, and the successor to the earlier BlockCell publishing MCP.

## Themes
- non-engineer-builders: ~80% of users outside engineering (Sales, Support, Legal and Compliance, Finance, Marketing), 50+ orgs; examples: support ticket triage, sales-call analysis against win rates, a people-ops policy Q&A (who uses it).
- enterprise-admin-controls: auth, authorization, secrets and data access by default; hard limits on what apps can connect to and who can open them; security team as design partner (security controls).
- skill-standards: the deploy CLI was "first packaged as an MCP server and later distributed to employees as a skill" (design approach).
- ai-synthesis-hallucination-risk: a pilot dashboard showed plausible but wrong numbers from a sampling flaw, so test scaffolding went into the default template; "a tool that's easy to use and quietly wrong is more dangerous than one that doesn't exist at all." (What was hard).
- org-learning-loop: support channel audited weekly, learnings fed back into the skill.

## Key points
- Launched mid-March 2026. In the quarter since: weekly active users from low hundreds to thousands; 1,000+ distinct apps, hundreds more each week; weekly app views up more than 10x.
- Fixed, opinionated stack chosen so security guarantees hold: "the constraints are what make those guarantees real."
- goose is not named; the agent is whichever one the employee uses.

## Could not verify
- Relationship to the BlockCell publishing MCP described in 2025 ([howiai-block-goose-brosamer-axen](howiai-block-goose-brosamer-axen.md)); no formal approval workflow described.
