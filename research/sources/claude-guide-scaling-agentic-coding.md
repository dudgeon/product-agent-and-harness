---
title: Scaling agentic coding across your organization
source_url: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization
author: Anthropic (Applied AI team)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [enablement-by-product, compounding-context-repo, enterprise-admin-controls, outcome-measurement-gap, skills-marketplace]
relevance: high
---

## Relevance to the project
Anthropic's rollout playbook for taking Claude Code from a 20-50 person pilot to a whole engineering org: power-user champions, a launch hackathon, CLAUDE.md files committed to the repo as a shared knowledge layer, managed policy settings, and an internal "app store" of vetted MCP servers. It is the adoption-model counterpart to the later AI-native SDLC playbook and bears on the adoption-model, governance-control-plane and capability-distribution-trust dimensions. It is engineer-centred: product managers and designers appear only in one line as "non-technical contributors". Its ROI chapter lists candidate measures and Activity Metrics but reports no results, so it leaves the outcome-measurement gap open. The guide states it reflects practice "as of August 2025", so it predates skills, plugins and Cowork.

## Themes
- enablement-by-product: champion model: pilot group of 20-50 AI-comfortable developers become mentors at a kickoff hackathon, then "internal consultants" who run workshops (ch. 03 Rolling out).
- compounding-context-repo: project CLAUDE.md checked into the repo root on main, reviewed in onboarding, updated in PRs "when architectural decisions change", optionally branch-specific (ch. 03 Sharing CLAUDE.md; appendix example).
- enterprise-admin-controls: "enterprise managed policy settings that take precedence over user and project settings" push configuration and permitted MCP tools to all users (ch. 06 Security first).
- skills-marketplace: an internal "app store" of pre-approved MCP servers with security assessments, sandbox testing and quarterly re-audits, to prevent shadow IT (ch. 06 MCP server management). An early, pre-skills form of a curated capability catalogue.
- outcome-measurement-gap: ROI chapter offers sprint throughput, time-to-completion, migration speed, satisfaction surveys, onboarding speed and fewer engineering dependencies for prototyping, plus Activity Metrics (lines accepted, accept rate, DAU, spend per user); no achieved numbers; concedes lines of code is "notoriously spotty" (ch. 04 Measuring ROI).

## Key points
- **Structure.** Eight chapters: foreword, what agentic coding is, rollout, ROI, adoption challenges, security, "beyond the obvious" applications, appendix (example CLAUDE.md, a worked TDD session, a context-rich bug prompt, a structured build prompt).
- **Pilot tasks (ch. 03).** Champions write org-specific slash commands (e.g. /migrate-db, /add-feature, /fix-security), iterate CLAUDE.md "as you would any other agentic prompt", identify repetitive workflows with DevOps and leads, run a dedicated Slack/Teams channel, and build wrapper scripts for AWS/GCP authentication.
- **Rollout shape.** Explicitly rejects a phased queue in favour of a whole-org hackathon after the pilot; scale through internal champions rather than external training (the companion article argues champions "speak your organization's language").
- **Adoption challenges (ch. 05).** The "do everything" trap: unbounded tasks fail; the fix is test-first, incremental scope with a checkpoint after each step. Context gap: give full errors, environment, expected vs actual. Prompting as a skill: write for a colleague, one objective per command.
- **Security (ch. 06).** Security policies written into CLAUDE.md as "policy-as-code" (in practice advisory instructions, not enforced gates); /security-review before commit; a library of approved security patterns; use Claude alongside, not instead of, existing security tools. MCP servers get a standard evaluation rubric (code access, data transmission, third-party dependencies), sandboxing before production, quarterly audits and a deprecation lifecycle.
- **Agent ideas (ch. 07).** On-call automation, migration specialists, continuous documentation engines, performance agents, and regulatory-compliance agents that audit for GDPR/SOX/HIPAA; all hypothetical, no examples given beyond naming Brex and Rakuten.
- **PM/design role.** One line: product managers "write requirements informed by actual codebase constraints" and designers turn Figma mockups into prototypes (ch. 02). Nothing on rollout to non-engineers.
- **Limits.** Prescriptive, drawn from "lessons learned from our customers" with no named outcomes; the companion article's FAQ cites a Rakuten seven-hour autonomous session as the only concrete figure. Calling CLAUDE.md instructions "policy-as-code" overstates them: the later SDLC playbook says such guidance is advisory and needs hooks behind it.

## Companion pages
- https://claude.com/resources/articles/scaling-agentic-coding ("How to scale agentic coding across your engineering organization", 2025-10-15): a condensed article version of the same guide with slightly more hedged wording (e.g. migrations "still require careful oversight"); adds an FAQ.
- Guide chapters: /foreword, /what-is-agentic-coding, /rolling-out-agentic-coding-at-your-organization, /measuring-roi, /avoiding-common-challenges-to-adoption, /security-first-protecting-your-codebase, /beyond-the-obvious-innovative-agentic-coding-applications, /appendix (all under the guide URL).

## Notable quotes
- "Pilots are only impactful if they drive value and highlight the art of the possible." (ch. 04)
- "This guide reflects current insights as of August 2025." (ch. 07)

## Could not verify
- Exact publication date of the guide (only "as of August 2025"); the companion article is dated 2025-10-15.
- Whether "enterprise managed policy settings" then covered everything claimed (permitted MCP tools); not checked against docs of that date.
