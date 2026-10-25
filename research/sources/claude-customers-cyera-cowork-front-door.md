---
title: "Cyera on making Claude Cowork the front door to 40 tools"
source_url: https://claude.com/customers/cyera-qa
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [agent-as-service-many-surfaces, org-context-grounding, enablement-by-product, build-vs-buy, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
A 1,500-person security company standardised on Cowork as the single agent "front door" over 40 connected tools rather than using the AI inside each SaaS tool, and grounds self-service analytics in a governed semantic layer plus a definitions skill loaded by every team plugin. It is useful for the strategy on three counts: the aggregator-versus-embedded-AI choice, governed data context as the precondition for agent analytics, and the customer's own named gap, that Cowork is a personal agent and team agents need a "graduation" process with software-engineering gates. Customer Q&A and case study published by Anthropic; all figures are the customer's claims, unaudited.

## Themes
- agent-as-service-many-surfaces: Cowork chosen as the aggregator over per-tool embedded AI: "Claude is now the aggregator" across Snowflake, Salesforce, Drive, Slack; 40 tools and several homegrown MCP servers (Q&A, "Why route work through Claude Cowork").
- org-context-grounding: a semantic layer of 30-40 documented Snowflake tables, one schema per department, role-level security by region, and a shared metric-definitions skill that fires in every team plugin before any query (Q&A, "keep it trustworthy"; case study, "The solution").
- enablement-by-product: 88% weekly active usage claimed about a month after rollout, attributed to ~20 department sessions, twice-weekly office hours, an 18-hour livestream, 24/7 on-call support and all-hands executive buy-in (Q&A, "88% adoption").
- build-vs-buy: considered building its own wrapper around Claude Code pushed to laptops and surveyed open-source harnesses; rejected them as built for people who already know what a cron job is (case study, "The solution"; Q&A).
- shared-persistent-sessions: names the gap: "Claude Cowork is great for being a personal agent", but a team agent is needed when an executive assistant's laptop is closed; proposes agent "graduation" via traditional engineering gates (Q&A, "Where does this go next").

## Key points
- Split by role: R&D on Claude Code, everyone else on Cowork. Non-engineers stalled at the terminal (running commands, connecting to Snowflake by API), which drove the Cowork choice.
- Access governance before rollout: data-mapping of which systems connect, which hold production data, and how to keep observability; the company used its own data-security product to map and re-scope Snowflake access, citing its finding that employees use about 4% of the data they are granted while agents can use all of it (case study).
- Rollout to the whole company in 17 days after a brief cross-department pilot (case study).
- Agent-to-agent pattern: every marketing team member has an Asana agent; the meeting owner's agent polls the others to keep tickets current (customer claims about 12 hours a week saved); "gatekeeper agents" block ticket submission when e.g. a Figma link is missing.
- Review pattern stated in the case study: "an agent takes the repetitive first pass, a person reviews before anything ships." Examples: Ask Claude channel triage every ~30 minutes with drafts for owner review (5-6 hours a day to ~30 minutes, customer claim); Legal plugin with 20 playbooks pre-reviewing inbound NDAs, lawyer sends; DM triage drafts replies the VP sends with a click.
- Personal maintenance agent: a GRC analyst's agent rescans their past published content whenever they post, flags what newer policy invalidates, and opens tickets assigned to them.
- Self-reported limits: "We haven't quite cracked context management in Cowork yet"; dashboard proliferation; data interpretation can be off even with a good semantic layer; hard to serve both AI-fluent staff and first-time users.
- Shadow AI stance: provide a sandbox rather than say no; Tustin calls shadow AI a sign of innovative employees, not a bad metric.
- Internal inconsistency: the case study's summary says seven homegrown MCP servers while its own quote and the Q&A say four or five; the semantic layer is "30 or 40" tables in the Q&A and 40 in the case study.
- Named people: Joe Tustin (Principal Technologist, Applied AI) and Steve Klementowski (VP of AI). The case study also carries a model-comparison quote about Claude Opus 5's training-data recency, which is marketing and not relevant here.

## Companion pages
- https://claude.com/customers/cyera (case study: "Cyera scales agentic AI across 1,500 employees with Claude Enterprise")

## Notable quotes
- "Claude is now the aggregator." (Q&A; attributed to Tustin in the text, Klementowski in the pull quote)
- "Graduation is an earned process that uses traditional software engineering gates to make sure agents last." (Tustin, Q&A)
- "Saying no AI is not a strategy." (Tustin, case study)

## Could not verify
- Publication date of either page.
- The 88% weekly-active figure, the 105-to-400 registration jump and the 12 hours a week saved are customer statements with no method or baseline.
