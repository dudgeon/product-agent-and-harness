---
title: "Deploying Claude across your organization: How Anthropic uses Cowork"
source_url: https://claude.com/resources/guides/deploying-claude-across-your-organization
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-04-29
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [enablement-by-product, skills-marketplace, single-agent-many-skills, tacit-knowledge-capture, prd-agents]
relevance: high
---

## Relevance to the project
Anthropic's own playbook for rolling Cowork out to non-engineers lays out a five-level adoption ladder (chat, deliverable, skill, scheduled bundle, admin-provisioned department plugin) and a six-month champion-led rollout, which is a ready-made sequencing and adoption-model option for the strategy. Its product-management section describes PRDs drafted by "stacking" four plugins (productivity, data, sales, product) in one session, the clearest first-party statement of the single-agent, many-skills pattern applied to PM work. It is a vendor guide: the outcome claims are anecdotal and unmeasured, and it says almost nothing about failure, review or governance beyond admin provisioning and OpenTelemetry export.

## Themes
- enablement-by-product: the whole guide is a staged enablement programme: champion teams, pre-built plugins to beat the cold-start problem, weekly pilot check-ins, live demos to adjacent teams (ch. 5, "Driving adoption at scale").
- skills-marketplace: Level 4 is "admin-provisioned plugin marketplace" per department with version control and push updates; admin provisioning is framed as the cure for "shadow AI" (ch. 3, ch. 4 "Structure your evaluation", ch. 5 "Months 4-6").
- single-agent-many-skills: PMs stack productivity, data, sales and product plugins in one session rather than using one PM plugin (ch. 6, "Product management").
- tacit-knowledge-capture: skills turn "tribal knowledge" into organizational infrastructure; the Legal plugin was built in an afternoon from existing memos, risk frameworks and policy docs (ch. 2 "Scale"; ch. 6 "Legal").
- prd-agents: the Product starting point is "PRD drafting from customer feedback and analytics", measured by time to first reviewable draft (ch. 4 table); PRDs drafted from usage data and customer quotes (ch. 6).

## Key points
- Surfaces (ch. 2): Chat for quick Q&A, Cowork for finished deliverables from files and systems (folder access, connectors, browser, scheduled tasks, plugins), Code for engineers. "The three share the same Claude underneath; what changes is the workspace around it."
- Plugin anatomy (ch. 2): skills (markdown workflows, slash-invoked or auto-triggered), subagents (autonomous end-to-end workflows), connectors (MCP, read/write; "Claude sees what the user sees"). Plugins are file-based markdown, so portable and version-controllable; Anthropic says no engineering team is needed.
- Maturity model (ch. 3): Level 0 chat Q&A; Level 1 a real deliverable from files and tools; Level 2 a skill; Level 3 bundled and scheduled skills; Level 4 a curated, admin-provisioned plugin per department. Goal of a deployment: move each user one level up, not reach Level 4 in month one.
- Pilot design (ch. 4): run the security review first (data boundaries, connector permissions, auditability; OpenTelemetry export to Datadog or Splunk); pilot with two or three champion teams, not one; define success up front ("hours saved per week"); provision plugins at admin level.
- Pilot selection heuristics (ch. 4): high-volume repetitive work, information-dense synthesis, bottleneck work, and expertise-dependent but process-driven work (said to pay back most). Suggests asking Cowork to categorise a department's intake queue; Anthropic Legal did this on 742 Jira tickets and restructured intake.
- Rollout timeline (ch. 5): Month 1 evaluate (champions to Level 1), Months 2-3 pilot (Levels 2-3), Months 4-6 scale (department plugins). Leading indicator: number of champion-authored skills at pilot end. "Bottom-up discovery, top-down scale." New hires installing the department plugin "start at Level 2".
- Supervision-to-autonomy anecdote (ch. 6 Sales): a rep ran a Salesforce auto-update skill with a validation step on every update, then removed it after enough manual checks; the guide calls this the Level 2 to 3 move. No error rate or criteria for removing the check are given.
- Finance (ch. 6): four skills over the warehouse via MCP, then a company-wide data skill that knows schema and table quirks so non-SQL staff can query; Anthropic states dashboard work went from weeks to hours.
- Product management (ch. 6): failure mode named is decisions and customer insights lost between meetings and PRDs; before Cowork, Claude "lacked the organizational context" for strategy, roadmap and PRD work. Plugin stacking supplies context, usage data, customer quotes and a PRD framework together; "the PM's job shifts from gathering to deciding."
- Customer vignettes (vendor-claim): Jamf encoded a seven-facet performance review spreadsheet as a skill in 45 minutes instead of a custom React app; Zapier product marketing generates HTML homepage mockups from a PMM-guidelines skill plus Slack and Glean via MCP before design or engineering are involved; Thomson Reuters says the human role becomes validation and decision-making.
- Limits: no quantitative adoption or quality data, no failure cases, no discussion of skill sprawl, conflicting plugins, or review gates beyond the single Sales anecdote. Pike (Anthropic Legal) is named only by surname.

## Companion pages
- https://claude.com/resources/articles/new-guide-deploying-claude-across-the-enterprise-with-claude-cowork (launch post, 2026-04-29; summarises the guide's contents)
- Guide chapters: foreword, introducing-claude-cowork, maturity-model, getting-started, adoption-at-scale, how-anthropic-teams-use-cowork, leveling-up (all under the source_url path)

## Notable quotes
- "The pattern is bottom-up discovery, top-down scale." (ch. 5)
- "The PM's job shifts from gathering to deciding." (ch. 6, Product management)

## Could not verify
- Publication date of the guide itself; 2026-04-29 is the launch post's date.
- None of the time-saving figures (30 to 2 minutes call prep, four hours to 45 minutes contract review, weeks to hours dashboards) come with method or baseline.
