---
title: Claude Cowork and chat are now one Claude
source_url: https://claude.com/resources/articles/cowork-is-now-claude
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-09-16
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-as-service-many-surfaces, product-artifact-primitives, enterprise-admin-controls, cost-control-routing, human-review-gates]
relevance: medium
---

## Relevance to the project
Anthropic merged its separate agentic workspace (Cowork) into ordinary chat, so one conversation now escalates from a quick answer to long-running cloud work that continues after the laptop closes, with Docs, Slides and Design produced in the same thread at shareable links. For the project this is a strong first-party signal on the agent-interface question: the vendor concluded that making users choose "where a task belongs" was the main friction, and moved routing into the agent. The Enterprise follow-up (2026-10-23) adds the governance shape: isolated per-session cloud VMs with egress off by default, credentials outside the sandbox, role-based access, and four cost controls including a new "Efficient mode". Customer quotes on the Enterprise page are vendor-curated testimonials, not evidence of outcomes.

## Themes
- agent-as-service-many-surfaces: one Claude on web, desktop and mobile; start on a computer, check progress or answer questions on a phone; work continues in the cloud (Pro/Max launch, "What it looks like"; Enterprise, "One Claude for every task").
- product-artifact-primitives: Claude Docs and Claude Slides launched (beta, paid plans), Claude Design available inside conversations; artifacts live at one shareable link, editable directly or by commenting to Claude, exportable to PowerPoint or PDF (Pro/Max launch).
- enterprise-admin-controls: admins choose when to enable Docs/Slides/Design, control access by role, get 30 days' notice before changes; SSO and Compliance API carry over; ZDR, HIPAA-ready and customer-managed-key orgs stay on current config (Enterprise, "Maintaining security", "Getting started").
- cost-control-routing: Efficient mode keeps the unified experience on Sonnet and Haiku; per-role model entitlements; spend limits at org, group and member level; pooled group budgets (Enterprise, "Managing cost").
- human-review-gates: default is that Claude asks before taking an action; users can opt into it working on and checking in only when something needs a closer look (Pro/Max launch, "What it looks like").

## Key points
- **Why merge.** Anthropic says users found deciding where a task belonged frustrating and work did not carry between Cowork and Design; Claude now "can figure out what a task needs" and brings Cowork and Design capabilities into any conversation with existing context, skills and connectors.
- **Worked example.** A weekly pipeline report: asked before leaving home, progress checked by phone, delivered as a doc plus five matching slides from the same conversation, then scheduled to run every Monday unprompted.
- **Check-in default.** By default Claude asks before taking an action; users can switch to letting it keep working and check in only when something needs a closer look. This is a per-user autonomy setting, not an admin policy, as described.
- **Rollout.** Pro and Max from 2026-09-16; Team and Free to follow; Enterprise generally available 2026-10-23 with admin-managed rollout.
- **Enterprise runtime (first-party claims).** Agentic work runs in an Anthropic-managed cloud; each session in its own isolated VM; network egress off by default for Enterprise; connector credentials kept outside the sandbox; central visibility for security teams. Data encrypted in transit and at rest; not used for training by default.
- **Pricing claims.** Usage-based; Anthropic states Opus 5.5 costs 40% less than Opus 5 and Sonnet 5.5 up to 30% less than Sonnet 5 on typical workloads, while agentic work can use more tokens than chat.
- **Customer quotes (vendor-curated).** LabX CTO says nothing broke across connectors, skills or MCPs in the transition; a CFO describes a multi-week budget-mapping report done with under ten minutes of prompting; Carvana cites start-on-desktop, finish-on-phone.
- **Limits:** launch announcements; no usage data, no detail on how Claude decides to escalate to cloud work, and no admin control over the per-user check-in setting is mentioned.

## Notable quotes
- "People used both, and told us the frustrating part was deciding where a task belonged." (Pro/Max launch)
- "By default, Claude asks before taking an action." (Pro/Max launch)

## Companion pages
- https://claude.com/resources/articles/unified-claude-enterprise ("Claude Cowork and chat come together for Enterprise", 2026-10-23)
