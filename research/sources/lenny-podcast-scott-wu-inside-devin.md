---
title: "Inside Devin: The world's first autonomous AI engineer that's set to write 50% of its company's code by end of year | Scott Wu (CEO and co-founder of Cognition)"
source_url: https://www.lennysnewsletter.com/p/inside-devin-scott-wu
author: Lenny Rachitsky (host), Scott Wu (CEO and co-founder, Cognition)
publisher: Lenny's Podcast
published: 2025-05-04
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [remote-agent-invocation, agent-as-service-many-surfaces, harness-over-model, compounding-context-repo, shared-persistent-sessions, evals-autonomy-trust, human-review-gates, enablement-by-product, pm-tool-connectivity]
relevance: medium
---

## Relevance to the project
Cognition's CEO on how his own 15-engineer team works with Devin, an asynchronous cloud coding agent invoked from Slack, Linear and GitHub: up to five Devins per engineer, about a quarter of PRs from Devin in May 2025 with a forecast of more than half by year end. For the project the useful parts are the interaction design lessons (start with small, verifiable tasks; "give Devin tasks, not problems"; a scoping step with a confidence level before work starts; separate ask/search/wiki tools for control), the claim that value now comes from teaching the agent real-world idiosyncrasies rather than base model IQ, and stickiness from accumulated team knowledge and multiplayer use in Slack and PR threads. A vendor CEO describing his own product: treat numbers as claims. An independent month-long test from January 2025 found far weaker results (see Agrees/contradicts in the report). Bears on remote-invocation-route, session-persistence-sharing and review-and-autonomy.

## Themes
- remote-agent-invocation / agent-as-service-many-surfaces: tag Devin on an issue in Slack, in Linear (add the Devin label), or have it open PRs in GitHub; built "to work with engineering teams as your junior engineer" (6:10). Linear automation shows Devin's scoping thoughts, relevant files and a confidence level before a human starts the session (44:51-45:44).
- harness-over-model: "in terms of base intelligence, we're honestly basically already there"; the work is "teaching it all of the idiosyncrasies of real-world engineering", e.g. using Datadog and making a GitHub PR (1:02:20-1:03:52). Improvement over a year was "50/50" capability and product interface (Slack, GitHub, Linear integration, interactive planning, editing Devin's code) (7:02-8:37).
- compounding-context-repo: Devin "accumulates a lot of the knowledge from working with every member of your team" and brings it into each new session (9:24); Devin Wiki gives an architectural representation used to onboard new engineers (43:46). Stickiness, not moat: Devin builds a representation of "your code base and of your stack and of your process over time" (57:30).
- shared-persistent-sessions: multiplayer: an engineer starts a Devin session in Slack, a colleague adds why something was built that way, Devin adjusts; reviewers comment on Devin's PRs and it responds (59:06).
- evals-autonomy-trust: "you want to be giving Devin tasks, not problems"; best on well-defined, easy-to-verify work (front-end tweaks, bug fixes, tests, docs); bigger asks need more steering (47:55). Devin can spawn other Devins via the API, off by default and needing credentials (1:13:37).
- human-review-gates: sometimes Devin does a task fully and you merge; sometimes you step in for "the 10 or 20% that really needs your help" on scoping, architecture or front-end testing (21:28); the human keeps "the full specification" (25:06).
- enablement-by-product: adoption pattern: a few enthusiasts set up repos, lint and CI, give starter tasks; others see "this Devin person ... knocking out PRs" and join, finding Devin already knows the repos (1:07:42-1:08:17). Advice: "treat Devin like your new junior engineer", start with easy tickets (1:09:31).
- pm-tool-connectivity: PMs use Devin in Linear to scope tasks and ask code and data questions ("is this merged", "is this behind a feature flag", "what percent of people are getting this"); Claire Vo, then at LaunchDarkly, is named as a heavy user (45:44).

## Key points
- Numbers (his): about 15 engineers, "up to five Devins at once" each; Devin merges "several hundred pull requests into production" a month; "in the neighborhood of a quarter" of PRs; ">half" expected by end of 2025 (0:00-0:21, 22:25-23:31, 30:33).
- Customers range from one-person startups to "Fortune 100 companies or public banks" using Devin across engineering teams (9:24). No detail on regulated deployments.
- "Bricklayer to architect": defining the problem and architecture is about 10% of an engineer's time; the rest is implementation and debugging that agents can take (23:31). He prefers "architect" to "manager of Devins" because the agent removes the emotional and ownership load of management (1:11:29).
- Product debate: one comprehensive agent vs a suite (Devin, Devin Search, Devin Wiki, Linear scoping); users want control to "just ask" without starting work (50:49-52:23). Long-run vision: working on the running product directly without looking at code (55:07).
- Human vs agent context: humans couple one thread with one context; agents could run parallel explorations sharing context (1:14:05).

## Notable quotes
- "You want to be giving Devin tasks, not problems." (47:55)
- "In terms of base intelligence, we're honestly basically already there." (1:02:20)
- "Treat Devin like your new junior engineer." (1:09:31)

## Could not verify
- Transcript (about 1h32m) read 0:00-1:20, 6:00-34:00, 42:41-1:04:15 and 1:07:27-1:14:05; demo narration (34:39-42:41), founding story, career and lightning-round sections skimmed by search. Show notes not separately reviewed beyond the title.
- All usage figures are the vendor CEO's, from May 2025, with no method; whether Devin reached ">half" of PRs is not checked here.
