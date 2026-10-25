---
title: Eight trends defining how software gets built in 2026
source_url: https://claude.com/resources/articles/eight-trends-defining-how-software-gets-built-in-2026
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-01-21
retrieved: 2026-10-24
type: report
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [agent-factory-sdlc, opportunity-to-code-chain, non-engineer-builders, risk-sloped-review, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
Anthropic's framing of the "agentic SDLC": the traditional eight stages remain, but requirements and design compress into "express intent (minutes)" and human effort moves to review and to defining which problems are worth solving. It is a vendor prediction document, not evidence, but it is the vendor's own picture of where the product role sits (upstream intent, downstream review), which this project's strategy will be compared against. Its central caveat is useful: Anthropic's own research says developers use AI in about 60% of their work but can "fully delegate" only 0-20% of tasks.

## Themes
- agent-factory-sdlc: side-by-side traditional vs agentic SDLC table, eight stages each, cycle time "weeks-months" to "hours-days" (Trend 1).
- opportunity-to-code-chain: the agentic SDLC starts at "express intent" and ends with humans "defining the problems worth solving"; problem selection stays human, but the report says nothing on how intent is shaped (Foreword; Trend 1).
- non-engineer-builders: Trends 5 and 7 predict domain experts in legal, sales, ops, design build their own tools; Anthropic's legal team example (marketing review from 2-3 days to 24 hours) (Trend 7).
- risk-sloped-review: "Human oversight shifts from reviewing everything to reviewing what matters"; agents flag uncertainty and escalate decisions with business impact (Trend 4).
- vendor-claims-vs-independent-evidence: every "In practice" box is a customer claim (TELUS 500,000 hours, Fountain 50% faster screening, Rakuten 7-hour run); no method given (all chapters).

## Key points
- **Structure:** eight predictions in three groups. Foundation: (1) SDLC changes dramatically. Capability: (2) single agents become coordinated teams, (3) long-running agents build complete systems, (4) human oversight scales through intelligent collaboration, (5) agentic coding expands to new surfaces and users. Impact: (6) productivity reshapes economics, (7) non-technical use cases expand, (8) security improves for defence and attack.
- **Agentic SDLC table (Trend 1):** express intent (minutes), agent understands (seconds), agent implements (minutes), agent tests and docs (minutes), human review (minutes-hours), deploy (minutes), monitoring (continuous), learn and iterate. Requirements and system design as separate stages disappear from the right-hand column.
- **Engineer role:** from implementer to orchestrator: architecture, agent coordination, quality evaluation, problem decomposition. Predicts onboarding in hours and "surge" staffing.
- **Multi-agent (Trend 2):** predicts multi-agent hierarchies (orchestrator plus specialists for design, implementation, testing, review) replace single-agent workflows.
- **Delegation research (Trend 4):** engineers delegate tasks that are easily verifiable or low-stakes; design-dependent work stays human or collaborative. About 27% of AI-assisted work is work that would not otherwise have been done (Trend 6, Anthropic internal research).
- **Four priorities for 2026:** multi-agent coordination; scaling oversight through AI-automated review; extending agentic coding beyond engineering; security from the start.
- **Customer claims (unaudited):** Rakuten 7 hours autonomous on vLLM at 99.9% numerical accuracy; TELUS 13,000+ custom solutions, 30% faster shipping, 500,000+ hours saved; Zapier 89% adoption and 800+ internal agents; CRED doubled execution speed; Augment Code customer finished a 4-8 month project in two weeks.
- **Limits:** predictions, explicitly "not certainties"; no data on failure, cost or quality regression; the PM role is not discussed by name.

## Notable quotes
- "Developers use AI in roughly 60% of their work, they report being able to 'fully delegate' only 0-20% of tasks." (Foreword)

## Companion pages
- https://claude.com/resources/guides/2026-agentic-coding-trends-report (report landing page, and its five chapters: foreword, foundation trends, capability trends, impact trends, priorities)

## Could not verify
- The downloadable PDF was not read; the web chapters were. The Societal Impacts and internal studies cited are not linked in the extract.
