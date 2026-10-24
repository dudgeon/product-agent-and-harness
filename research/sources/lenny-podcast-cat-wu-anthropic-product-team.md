---
title: "How Anthropic's product team moves faster than anyone else | Cat Wu (Head of Product, Claude Code)"
source_url: https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves
author: Lenny Rachitsky (host), Cat Wu (Head of Product, Claude Code and Cowork, Anthropic)
publisher: Lenny's Podcast
published: 2026-04-23
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [pm-job-stable-methods-change, spec-becomes-prototype-and-evals, pm-persona-role-expansion, harness-over-model, human-judgment-pm-jobs, evals-autonomy-trust, harness-portability, product-coherence-over-automation, org-context-grounding, non-engineer-builders, enablement-by-product, shared-persistent-sessions, agent-failure-modes, human-review-gates, cost-control-routing, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
The head of product for Claude Code and Cowork describes, first-hand, how a frontier AI product team runs: feature timelines cut from six months to one month, a week or a day; most features shipped as "research preview"; an evergreen launch room; team principles and weekly metrics readouts used in place of most PRDs; and engineers with product taste shipping end-to-end with no PM involved. It is the clearest first-party account of an AI-native product operating model, and of what the PM role keeps: setting goals, choosing what to build, defining success (including writing about ten evals), and the stakeholder "common sense" the model still lacks. It also gives a harness-upkeep practice (audit and strip the system prompt at every model release) and a Cowork PM workflow (connect sources, agent proposes an outline, PM decides, agent builds). It bears on intent-shaping-and-spec, pm-agent-evaluation, harness-upkeep, review-and-autonomy and target-user. Caveat: Anthropic is the vendor, and its conditions (frontier models, generous tokens, a 30-40 PM org) are unusual.

## Themes
- pm-job-stable-methods-change: the PM shifts from aligning multi-quarter roadmaps with partner teams to "how can we figure out the fastest way to get something out the door" (5:03); PM sets clear goals (key user, main problem, use case), creates a repeatable shipping process, and sets the framework for when to pull in cross-functional partners (6:57-8:59).
- spec-becomes-prototype-and-evals: PRDs are "sometimes": a one-pager for ambiguous features (goals, delightful use cases, current failure modes), full PRDs only for multi-month infrastructure work (10:03). When a feature needs more definition, Wu's output is "five evals that I made ... how you run them ... which succeed", plus the prompt that raised the success rate (55:46). "Just building 10 great evals" is enough to quantify the goal (55:02).
- pm-persona-role-expansion: "all of the roles are merging"; Claude Code hires engineers with product taste who go "from see user feedback on Twitter through to like ship a product at the end of the week with almost no product involvement" (16:15). Almost all PMs on the team were engineers or ship code; designers were front-end engineers (17:27).
- human-judgment-pm-jobs: product taste ("deciding what to write") is the scarce skill (18:16); humans still supply "tacit common sense, like EQ" about stakeholders, their preferences and venues (21:43). In the Cowork deck example the model generates options and "the role of the PM is still to make the end decision" (39:25).
- harness-over-model / harness-portability: every model launch, the team reads the entire system prompt and removes reminders the model no longer needs (1:03:04); the to-do list was a crutch for pre-Opus 4 models (1:01:03). Code review failed several times and only became reliable with Opus 4.5/4.6 and Sonnet 4.6; because the prototype existed they could swap models in and test (1:03:04-1:05:12).
- agent-failure-modes / evals-autonomy-trust: Wu asks the model to introspect on unexpected behaviour; answers include a confusing system prompt, not realising front-end verification was in scope, or "I delegated the verification to this subagent and the subagent didn't do the test and I didn't check its work" (53:31). A handful (~5) of trusted users' qualitative model feedback forms hypotheses, then data tests them (55:02, 57:01-58:36).
- product-coherence-over-automation: the explicit cost of speed is "product consistency": overlapping features, new users unsure of the best path, users on a "treadmill" (25:42-27:48). /powerup onboarding was added against the team's earlier no-onboarding principle (27:57).
- org-context-grounding: Cowork first step is connecting Calendar, Slack, Gmail, Drive, "where you store your source of truth data" (36:08, 39:07); design-system fidelity came from giving it the standard deck template (~20 example slides), or Figma MCP (41:15).
- shared-persistent-sessions: desktop as "a one-stop control plane" showing CLI, desktop, web and mobile sessions (32:44-34:16); roadmap is many parallel remote tasks with interfaces to know "which tasks you need to look into" (1:05:32).
- human-review-gates: the source-code leak was "human error", a Claude-assisted PR that passed "two layers of human review" (12:15). Code review agents now gate merges at Anthropic (1:03:04).
- non-engineer-builders / enablement-by-product: a Claude Code salesperson built a web app that pulls Salesforce, Gong and call notes to tailor decks (20-30 minutes to seconds) (43:12); Applied AI is the second-heaviest token user, with nightly Cowork meeting dossiers (47:04-49:26). Wu admits customising skills requires "too many concepts" today (1:11:29).
- cost-control-routing: token cost per knowledge worker rises with every model jump; "still much lower than" salary but rising as a share (49:50); wasting tokens is "frowned upon" but left to individual judgment (50:49).
- outcome-measurement-gap: weekly team-wide metrics readouts exist (9:11), but no PM-agent outcome metric is described; the evidence is speed and anecdote.

## Key points
- Role split: Boris Cherny is tech lead and product visionary (3-6 month "AGI-pilled" view); Wu plots the path from today and does cross-functional alignment (marketing, sales, finance, capacity) (2:16).
- Shipping system (6:57-8:59): research preview branding lowers the commitment; an evergreen launch room where engineers post dogfooded features and docs, PMM and DevRel turn round the announcement the next day.
- Decisions without the PM: weekly metrics readouts and written team principles (key users and why, what we trade off) so "people make decisions by themselves without feeling like they're blocked on PM" (9:11).
- Anthropic PM org: roughly 30-40 PMs across research PM, Claude Developer Platform (APIs, Managed Agents), Claude Code/Cowork, Enterprise (cost controls, RBAC, security), and Growth (14:26).
- Speed attributed mostly to process and expectations, "very low on process", not mainly to internal models such as Mythos (11:03-11:22).
- Product split: Claude Code for code output, Cowork for non-code output (Slack/inbox zero, decks, goal docs, launch plans) (35:04).
- Cowork deck workflow (36:08-41:15): sources connected; prompt with PMM's points, two drafts she disliked, and a constraint not to overlap the keynote; Claude proposes an outline; Wu decides the narrative (local tasks successful, then every PR green, then more PRs landed); Cowork works for hours and produces a ~20-page deck she then gives one round of feedback on.
- Stack: Claude Code, Cowork and Slack ("the core OS of our company"); many internal custom apps instead of SaaS; ~30% of her time spent pushing the products to find where they fail (42:04).
- Vision as building blocks (1:05:32-1:07:23): make single tasks succeed; multi-Clauding; then 50-100 concurrent remote tasks needing triage interfaces, agents that fully verify their work "to your spec", and self-improving feedback loops.
- Automation advice: take automations to 100%; a 95% automation has little value; building it is often slower than doing the task (1:09:45). Simple setups beat heavily customised ones (1:12:49).
- 2024 products were chat-based; the Claude Code generation is action-based (1:14:36).

## Notable quotes
- "As code becomes much cheaper to write, the thing that becomes more valuable is deciding what to write." (18:16)
- "You don't need to build hundreds of evals for them to be useful. Just building 10 great evals." (55:02)
- "If an automation doesn't work 100% of the time, it's not really an automation." (1:09:45)
- "We're sacrificing product consistency." (25:42)

## Could not verify
- Full transcript read (Substack auto-transcription; names garbled, e.g. "Cloud Code" for Claude Code, "Kat" for Cat).
- Cadence numbers (six months to a day), the 30-40 PM count, and the 20-30 minute deck saving are the speaker's own; no method given.
- Anthropic is the vendor of the tools discussed; claims about Cowork's quality are first-party and promotional in context.
- Regulated settings appear only in passing (a sales deck adds HIPAA/security slides for such customers, 43:12).
