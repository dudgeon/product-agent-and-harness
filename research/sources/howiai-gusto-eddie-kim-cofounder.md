---
title: "No Figma. No Jira. No docs. How Gusto built a new product line with Claude Code | Eddie Kim (CTO)"
source_url: https://www.lennysnewsletter.com/p/no-figma-no-jira-no-docs-how-gusto
author: Claire Vo (host), Eddie Kim (co-founder and CTO, Gusto)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-06-29
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, non-engineer-builders, human-review-gates, pm-persona-role-expansion, harness-over-model, product-coherence-over-automation, leadership-permission-mandate, agent-as-service-many-surfaces]
relevance: high
---

## Relevance to the project
A first-party account from the CTO of a payroll and HR company (over 1,000 people in R&D) of a five-person team (four engineers including the CTO, one designer, no PM) that shipped a new AI product line, Gusto Cofounder, from zero code to a tier-one launch in 10 weeks with no specs, no Figma, no Jira, no stand-ups: the only artifact was a whiteboard photo. Scope decisions were made by writing review-ready pull requests and closing the ones the team didn't want ("PR as the PRD"), and bugs in agent behaviour were fixed eval-first. It is strong evidence for "the spec is replaced by prototype plus evals" in a zero-to-one setting, and an honest counterweight for the film: Kim says it worked partly because a co-founder gave implied permission to break the rules, and that it fits "a subset of projects, kind of more zero to one" (43:31). It bears on intent-shaping-and-spec, review-and-autonomy, adoption-model and target-user (who is the PM when there is no PM).

## Themes
- spec-becomes-prototype-and-evals: scope was decided by building a feature, opening a non-draft, review-ready PR, discussing it on the team's always-on Zoom, then merging or deleting it (13:27); host names this "PR as like the PRD" (19:08). Agent bug fixes start from a failing eval reproduced from a real customer conversation in a GitHub issue, then a fix, then a passing eval (36:38-38:09).
- non-engineer-builders: the designer, not a trained engineer, reached the 94th percentile of "true throughput" (PRs landed to production, measured in DX) across the whole R&D org (22:27); her own explanation: technical curiosity plus three or four engineers who reviewed her code and coached her prompting and taste.
- human-review-gates: every PR still gets human code review; median review time on the team was nine minutes because someone was always on the "perma-Zoom" (25:59-26:13). Kim's loop ends with him reviewing the generated code and eval "and then and only then" opening a PR (38:09). Host: review non-engineers' PRs as fast as engineers' (24:18).
- pm-persona-role-expansion: "everybody was kind of a product manager" (13:27); no titled PM on the team; the CTO went into IC mode and was ~95th percentile in DX for three months (45:35).
- harness-over-model: the product's stack is "surprisingly simple": Cloudflare Workers for the agent loop plus Vercel AI SDK, "we don't have any other harness on top"; memory is "a tool that writes to a database column called memory" (17:38). A counterpoint to the idea that agent products need heavy harness frameworks.
- leadership-permission-mandate: Kim says the model needs explicit permission to scale: other teams that skip tech specs "might get a slap on the wrist"; he would mandate the new way, even penalising docs or Figma, because teams "don't feel like they're allowed to" (41:12). (Theme slug proposed in this filing; see themes file.)
- agent-as-service-many-surfaces: Cofounder is reached over SMS and Slack as first-class channels, calling the same tools as the web app (29:30-31:47); idea came from the CTO running OpenClaw himself (47:48).
- product-coherence-over-automation: "at any given time there was always something wrong with it in production" while the team "chipped away" behind a feature flag (21:07); host: "now we can ship all our bad ideas" is the risk side (not in this episode; see summit note).

## Key points
- **Origin (4:59-7:06):** CTO vibe-coded a prototype on a five-hour layover with Claude Code, shared a Loom, gathered the senior engineers and designer who leaned in. The team rewrote from scratch on day one (TypeScript, a stateless agent in its own repo on Cloudflare Workers); he deleted his own prototype code (15:43).
- **Process (8:58-11:22):** whiteboard at a quarterly leadership week was the only documentation; a 24/7 Zoom room replaced meetings, stand-ups, retros and Slack threads. Primitives on the whiteboard (tasks, task runs, assets, chats, suggested tasks) survived nearly unchanged; "assets" were renamed "artifacts" (11:48).
- **Shipping in place (19:36-21:07):** a hidden page in the production web app behind a feature flag. The designer first shipped a fake front end with canned responses; engineers built data models and the agent loop behind it, so the prototype was "brought to life" in place rather than thrown away.
- **Regulated-adjacent demo (31:47-34:51):** a real customer (a spa) whose owner exports from Mindbody, calculates bonuses, commissions and pooled tips in a spreadsheet, then runs payroll. Cofounder reads the sheet via connectors (QuickBooks, Google Sheets, Notion), applies the owner's plain-language rules, updates payroll, and stops for explicit confirmation before submitting. A human gate on a money-moving action.
- **Portfolio argument (34:57-36:10):** five people for 10 weeks is a small fraction of a 1,000-person R&D budget; Kim: run ten such bets and two or three may change the business's trajectory.
- **Leaders hands-on (45:35):** a leader's prototype alone leads to "underappreciation of the actual nuances" of production work; he took his all the way to reviewed production code.
- **Host aside on docs (43:37):** Claire Vo says docs may survive but "for the agents, not for the humans"; agent-written docs that are "none of my business". This is the host's view, not Gusto's practice.

## Notable quotes
- "We had no meetings, we had no tech specs, we had no figmas, we had no JIRA board" (0:00).
- "The cost to write code is now so low that you can actually build products in this way" (13:27).
- "Always write a failing eval first then write the code to fix it" (38:09).
- "We're not giving you permission to do it in any other way" (41:12).

## Could not verify
- Transcript is a Substack auto-transcription (e.g. "Gustav" for Gusto, "cloud code" for Claude Code). Read in full.
- All metrics (10 weeks, 94th percentile, nine-minute median review, 95th percentile for the CTO) are the speaker's own from DX; not independently verified. "Tier one launch" is Gusto-internal terminology; launch scope and customer numbers not stated.
- Kim says the approach needed nights and weekends (27:42), was zero-to-one, and carried co-founder permission; generalisation to an established product line or a regulated change process is untested in the episode.
