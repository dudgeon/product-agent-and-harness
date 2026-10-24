---
title: "Claude for the financial industry"
source_url: https://claude.com/resources/guides/claude-for-the-financial-industry
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [enterprise-admin-controls, enablement-by-product, human-review-gates, agent-as-service-many-surfaces, skills-marketplace]
relevance: medium
---

## Relevance to the project
Anthropic's rollout guide for regulated financial firms gives a regulated-industry variant of its adoption playbook: governance (model risk management, SEC/FINRA, GDPR/CCPA) scoped in parallel with access set-up, cloud-perimeter deployment via Bedrock, Vertex or Foundry, and an explicit order in which surfaces come online (skills and plugins first, Microsoft 365 add-ins next, Cowork last). It also shows one agent role packaged two ways, as a desktop plugin with a human in the loop or as a Managed Agents cloud service, which bears on the runtime-location and harness-layering options. The guide is product marketing for a vertical: customer outcome figures are quoted from press releases, and nothing is said about failures or how reviews are evidenced to regulators.

## Themes
- enterprise-admin-controls: Phase 1 requires SSO, SCIM, audit logs and custom data retention configured before pilot, and keeping Claude inside the firm's cloud perimeter; ISO/IEC 42001 cited (ch. 4 "Lay the foundation"; ch. 5).
- enablement-by-product: same champion-team, cold-start, weekly check-in playbook as the Cowork deployment guide, with pilot metrics of cycle time and "how often a user keeps Claude's draft without a meaningful rewrite" (ch. 4 "Pilot").
- human-review-gates: the work brought first is "reviewed by a senior person before it ships"; for the ten agent roles "analysts stay in the loop, reviewing, iterating on, and approving the agent's outputs before anything moves downstream" (ch. 4 "Industry use cases"; ch. 2).
- agent-as-service-many-surfaces: each agent role can run as a Cowork or Microsoft 365 plugin on the desktop or as a Managed Agents hosted service (ch. 2, "Pre-built finance agent reference architectures").
- skills-marketplace: scale phase rolls skills out through admin-managed plugin marketplaces; advice to provision at admin level, not ad hoc (ch. 4 "Scale").

## Key points
- Product mix (ch. 1-2): most firms run several surfaces at once: Chat, Cowork, Code (quants, COBOL/Java migration), Claude for Microsoft 365 add-ins, the Claude Platform API, and Managed Agents (long-running sessions, scoped permissions, managed credential vaults, execution tracing).
- Surface sequencing in pilots (ch. 4 "Pilot"): skills and plugins first ("low-risk and high-reuse"), then Microsoft 365 add-ins where most front- and back-office work happens, and Cowork late, when moving from single-document to project-level work.
- Pilot work selection (ch. 4): document-heavy, standard-shape work (first-draft research notes, credit memos, KYC file reviews, claims summaries); "Avoid piloting Claude on novel or high-stakes work."
- Pilot metrics (ch. 4): cycle time before and after, and draft-retention rate without meaningful rewrite. Leading signal: champions authoring skills (e.g. a credit memo skill with template, credit policy and approval flow embedded).
- Skill reuse (ch. 4 "Scale"): skills are adapted across teams with shared structure (fraud review and AML check); "adding a second team usually goes faster than the first."
- MCP connectors framed as a data-residency and entitlement control: Claude queries the provider's system directly rather than an uploaded copy (ch. 2).
- Ten pre-built agent "reference architectures" (pitch builder, meeting preparer, earnings reviewer, model builder, market researcher, GL reconciler, KYC screener, month-end closer, statement auditor, valuation reviewer) packaging skills, tools and connectors as customisable templates (ch. 2).
- Customer figures (vendor-claim, from press releases): AIG underwriting review over 5x faster and data accuracy 75% to over 90% in early rollouts; IG Group analytics saving 70 hours a week and full ROI in three months; Moody's credit memo prep from 40 hours to 2 minutes (ch. 3).
- Third-party stat cited: an NVIDIA 2026 survey reports 42% of financial firms using or assessing agentic AI (ch. 1).
- Limits: no account of how human approvals are recorded for audit or model-risk purposes, no failure cases. The Code pillar's description in ch. 2 repeats Chat's copy, an editing error.

## Companion pages
- Chapters under the source_url path: foreword, product-overview, real-world-examples, claude-adoption-roadmap, getting-started.

## Notable quotes
- "Avoid piloting Claude on novel or high-stakes work." (ch. 4, Phase 1)

## Could not verify
- Publication date (the guide cites a 2026 survey, so 2026).
- All customer outcome figures; method and baselines are not given.
