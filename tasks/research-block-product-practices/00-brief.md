# Block (Square, Cash App): how it runs product and is bringing agents into product management

Date: 2026-10-24. Worker brief for research-block-product-practices. Built on 61 source notes in [research/sources/](../../research/sources/), filed or updated by this task; themes in [research/themes/research-block-product-practices.md](../../research/themes/research-block-product-practices.md). Lifecycle map: [01-pdlc-block.md](01-pdlc-block.md) and [01-pdlc-block.html](01-pdlc-block.html). Register proposals: options/contributions/research-block-product-practices.md.

Evidence tags: **FP** = first-party (Block, its leaders, goose docs), **VC** = vendor claim (Block marketing a figure), **IND** = independent press, with publication dates.

## The short version

1. **Block is not putting agents into product management. It is folding product management into a builder role around agents.**
   - The operating essay keeps three roles (IC, DRI, player-coach), and none of them is a PM ([essay](../../research/sources/block-from-hierarchy-to-intelligence.md), FP, 2026-03-31).
   - "All of our product managers are shipping PRs" ([Jennings](../../research/sources/a16z-owen-jennings-block-all-in-on-ai.md), FP, 2026-04-01).
   - Feature teams of about 14 (8 server engineers, 4 client engineers, a PM, a designer) became squads of 1-6 that rotate between products.
   - The one open Square PM role asks for AI prototypes and PRs through GitHub ([job post](../../research/sources/block-careers-staff-pm-post-checkout.md), FP, 2026-10-06).
2. **Goose is the general harness for everyone. The work that changed throughput runs on shared services built on it.**
   - goose is one general agent, desktop and CLI, with a curated bundle from about 150 internal services ([investor day](../../research/sources/block-investor-day-2025-ai-engineering-transcript.md), VC, 2025-11-19).
   - The big numbers come from services on top of it: Builderbot (Slack thread or Linear/Jira ticket to merged PR; ~1,500 PRs a week, ~15% of production changes, review of 90%+ of change requests) and the governed Data MCP plus Query Expert (2.1K monthly users).
   - Sources: [Builderbot](../../research/sources/block-builderbot-rollout.md), VC, 2026-06-17; [Q1 2026 letter](../../research/sources/block-q1-2026-shareholder-letter.md), FP; [data foundation](../../research/sources/block-eng-data-foundation-automated-analytics.md), FP, 2026-04-29.
   - Engineers are not all-goose: "We buy them all", across seven coding harnesses ([AI-assisted dev](../../research/sources/block-eng-ai-assisted-development-at-block.md), FP, 2026-01-18).
3. **The organisation changed first, and then it shrank.**
   - Functional reorganisation, July 2024 ([Fortune](../../research/sources/fortune-block-functional-reorg-memo-2024.md), IND, 2024-07-25). The CTO credits it with "more productivity than any AI tool" ([Lenny's](../../research/sources/lenny-podcast-block-dhanji-goose.md), FP, 2025-10-26).
   - Flattening in March 2025, "not replacing folks with AI" ([email](../../research/sources/techcrunch-dorsey-email-931-cuts-2025.md), FP, 2025-03-25).
   - Cut from over 10,000 people to under 6,000, credited to intelligence tools "paired with smaller and flatter teams" ([Dorsey](../../research/sources/x-jack-block-smaller-note-2026-02-26.md), FP, 2026-02-26).
4. **PM-specific evidence is thin, and that is a finding.**
   - No Block or Square PM has written or spoken first-hand about using goose or Builderbot for discovery, specs or synthesis.
   - The public goose cookbook has no PRD, research or feedback-synthesis recipe ([recipes](../../research/sources/goose-docs-recipes.md), FP).
   - Square's head of product, in a full 29-minute episode, describes the org and the customer product. He says nothing about PM tooling ([Avé](../../research/sources/productschool-willem-ave-square-org-design-ai-agents.md), FP, 2026-08-19).
   - What we know about PM work comes from executives (Jennings, Dorsey, Worboys) and job ads.
5. **The numbers are Block's own; the only independent voices dispute them.**
   - Block's figures: 8-10 hours a week saved (self-reported), "20 to 25% of manual hours saved" (unpublished formula), code per engineer up 40% and then 2.5x, 130 Square features in H1 2026 (3x).
   - Seven staff told the Guardian that every change still needs human approval, that about 95% of AI changes needed edits, and that AI use became mandatory and monitored ([Guardian](../../research/sources/guardian-block-workers-ai-cant-do-their-jobs.md), IND, 2026-03-08).

## 1. Goose as Block uses it internally

**What it is.** goose is a general-purpose, local agent (desktop app and CLI). It is model-agnostic, and all its capability comes from MCP servers ("extensions") ([CTO](../../research/sources/lenny-podcast-block-dhanji-goose.md), FP). The CTO places it between a general assistant and Claude Code or Cursor. Block open-sourced it, and it moved to the Linux Foundation's Agentic AI Foundation on 2025-12-09. The repo and docs moved on 2026-04-07 ([AAIF](../../research/sources/goose-blog-moves-to-aaif.md), FP). A former Block open-source lead said Block's ownership of the trademarks was "hampering enterprise adoption" ([The New Stack](../../research/sources/thenewstack-why-block-handed-goose-lf.md), IND, 2026-05-15).

**Who uses it, for what.**
- **Teams.** Named teams are design, product, support and risk ([goose blog](../../research/sources/goose-blog-mcp-in-enterprise-block.md), FP, 2025-04-21); HR, customer operations and legal ([investor day](../../research/sources/block-investor-day-2025-ai-engineering-transcript.md), VC); and sales and finance building their own dashboards ([Sequoia CTO](../../research/sources/sequoia-training-data-dhanji-goose.md), FP, 2025-09-30).
- **Non-engineers gain most.** The CTO says the biggest gains are outside engineering. Enterprise risk built its own self-service system, "compressing weeks of work into hours" ([Lenny's](../../research/sources/lenny-podcast-block-dhanji-goose.md), FP).
- **Data.** Query Expert grew from 700 to 2.1K monthly users between September 2025 and March 2026, more than a third of the company ([data foundation](../../research/sources/block-eng-data-foundation-automated-analytics.md), FP).
- **Internal apps.** About 80% of App Kit users are outside engineering, with 1,000+ internal apps in a quarter ([App Kit](../../research/sources/block-eng-app-kit-localhost-to-launched.md), FP, 2026-06-24).
- **Engineering.**
  - Recipes: detection engineering (one recipe orchestrating six sub-recipes to a draft PR), Goose Janitor for feature flags, and headless goose fixing CI failures ([Panther](../../research/sources/goose-blog-detection-engineering-panther-recipes.md); [Janitor](../../research/sources/goose-blog-goose-janitor-ai-teammate.md); [Actionable CI](../../research/sources/block-eng-actionable-ci.md); FP).
  - Overnight agents that draft patches from bug tickets ([Lenny's](../../research/sources/lenny-podcast-block-dhanji-goose.md), FP).
  - Gosling for Android UI tests.

**Extensions, recipes and MCP servers.**
- **Catalogue size.** The internal MCP count grew from "40 or 50" (July 2025) to "over 100" (October 2025) to "about 150 services" (November 2025) ([How I AI](../../research/sources/howiai-block-goose-brosamer-axen.md); [The New Stack](../../research/sources/thenewstack-block-12000-employees-ai-agents.md), IND; [investor day](../../research/sources/block-investor-day-2025-ai-engineering-transcript.md)).
- **Named servers.** Snowflake, GitHub, Jira, Slack, Google Drive, Calendar, Linear, Asana, PagerDuty, Glean, Databricks, Workday and Figma, plus the governed-metrics Data MCP (1,100+ metrics) and Query Expert.
- **Servers are designed around workflows, not APIs.** For example, Linear went from 30+ tools to 2 ([MCP playbook](../../research/sources/block-eng-playbook-designing-mcp-servers.md), FP, 2025-06-16).
- **Recipes are task agents inside the general harness.** A recipe is YAML holding instructions, typed parameters, the extensions to load, model settings, sub-recipes, a response schema and shell-checked retries. Recipes can be shared by link, scheduled, or run as subagents ([recipes](../../research/sources/goose-docs-recipes.md); [subagents](../../research/sources/goose-docs-subagents.md); FP).
- **Skills.** A separate internal marketplace holds 100+ skills with role bundles, reviewed by PR ([skills](../../research/sources/block-eng-3-principles-agent-skills.md), FP, 2026-02-15).

**General harness or set of task agents? Both, at three levels:**
1. One general agent per person.
2. Task agents packaged as recipes and skills inside it.
3. Shared services built on goose for the heavy jobs: Builderbot for code and review ([Builderbot](../../research/sources/block-builderbot-rollout.md), VC), and Buzz, a harness-agnostic workspace where people and agents share channels ([Buzz](../../research/sources/block-eng-buzz.md), FP, 2026-07-21).

Block's own one-page map lists goose, Builderbot, Buzz and a desktop workspace called Berd ([AI at Block](../../research/sources/block-ai-at-block-page.md), FP). A no-code "g2" tile layer for non-technical staff was announced at the 2025 investor day and has not been documented since (VC).

**Governance, sharing and distribution.**
- **Distribution.** goose was auto-installed and auto-updated through the internal software centre, with preset servers and models ([The New Stack](../../research/sources/thenewstack-block-12000-employees-ai-agents.md), IND, 2025-10-20).
- **Security review.** Even internal MCP servers go through a security review before joining the allowlist ([Jones](../../research/sources/chainofthought-angie-jones-block-goose-rollout.md), FP, 2026-01-21).
- **Upstream controls are thin.** The allowlist is a client-side list of allowed install commands; with no setting there is no restriction ([allowlist docs](../../research/sources/goose-docs-extension-allowlist.md), FP). Permission modes default to Autonomous ([permission modes](../../research/sources/goose-docs-permission-modes.md)). The adversary-mode reviewer is off by default and fails open ([adversary mode](../../research/sources/goose-docs-adversary-mode.md)). goose has no admin plane; Block builds that around it.
- **Red team.** Block's own red team ("Operation Pale Fire") succeeded with a poisoned shareable recipe and with a prompt injection hidden in a calendar invite ([red team](../../research/sources/block-eng-red-teamed-own-ai-agent.md), FP, 2026-01-15). AI integrations go through a review tiered by data-sensitivity level, which received "several hundred requests" ([GenAI security](../../research/sources/block-eng-genai-security-principles.md), FP).
- **Sharing.** Help and inspiration Slack channels, about 50 AI Champions at 30% time, and weekly workshops ([AI-assisted dev](../../research/sources/block-eng-ai-assisted-development-at-block.md), FP).
- **Models.** Claude, GPT and Gemini are served through Databricks-hosted endpoints, and users pick the model by hand ([Jones](../../research/sources/chainofthought-angie-jones-block-goose-rollout.md)). In the Q2 2026 letter: "To us the models are interchangeable" ([Q2 2026 letter](../../research/sources/block-q2-2026-shareholder-letter.md), FP).

## 2. Block's product operating model and how it changed

| Date | Change | Evidence |
|---|---|---|
| ~2023 | Dhanji Prasanna's "AI manifesto" to Dorsey: invest in AI "centrally". Special projects of 2-5 engineers and a reinstated hack week follow; he becomes CTO | [Lenny's](../../research/sources/lenny-podcast-block-dhanji-goose.md), [Sequoia](../../research/sources/sequoia-training-data-dhanji-goose.md) (FP, 2025) |
| early 2024 | goose begins (Block later calls it "the first agentic harness" to work across an enterprise) | [Q1 2026 letter](../../research/sources/block-q1-2026-shareholder-letter.md) (FP) |
| 2024-07 | GM / business-unit structure → functional org: one head of engineering, one of design; product reports to Jennings | [Fortune](../../research/sources/fortune-block-functional-reorg-memo-2024.md) (IND); [Q2 2024 call](../../research/sources/motley-fool-block-q2-2024-earnings-call.md) (FP) |
| 2025-03 | 931 cut (~8%); 80 managers cut, 193 moved to IC, org depth capped; "not replacing folks with AI" | [email](../../research/sources/techcrunch-dorsey-email-931-cuts-2025.md) (FP via TechCrunch) |
| 2025 | Single company metric: "manual hours saved by goose", weekly, 25% target by end of 2025 | [Sequoia CTO](../../research/sources/sequoia-training-data-dhanji-goose.md) (FP) |
| 2025-12 | Trigger named by Dorsey and Jennings: models became good on large legacy codebases | [Dorsey](../../research/sources/sequoia-dorsey-every-company-mini-agi.md); [Jennings](../../research/sources/a16z-owen-jennings-block-all-in-on-ai.md) (FP) |
| 2026-02-26 | Over 10,000 → under 6,000; "way larger on the development side"; compliance "basically" untouched | [Dorsey](../../research/sources/x-jack-block-smaller-note-2026-02-26.md); [Q4 2025 remarks](../../research/sources/block-q4-2025-earnings-prepared-remarks.md) (FP); [TechCrunch](../../research/sources/techcrunch-block-layoffs-4000-2026.md) (IND) |
| 2026-03 | Some laid-off staff rehired within weeks; staff dispute the gains | [Cointelegraph](../../research/sources/cointelegraph-block-rehires-laid-off-staff.md); [Guardian](../../research/sources/guardian-block-workers-ai-cant-do-their-jobs.md); [HRD](../../research/sources/hrd-block-staff-dispute-ai-layoffs.md) (IND) |
| 2026-03-31 | "From Hierarchy to Intelligence": capabilities, a world model, an intelligence layer and interfaces; three roles (IC, DRI, player-coach); roadmap from failure signals | [essay](../../research/sources/block-from-hierarchy-to-intelligence.md) (FP) |
| 2026-06 / 07 | Builderbot rollout; Buzz launched | [Builderbot](../../research/sources/block-builderbot-rollout.md) (VC); [Buzz](../../research/sources/block-eng-buzz.md) (FP) |
| 2026-08 | Q2: agentic AI wrote and reviewed "nearly all" production changes in June; 130 Square features in H1 (3x+) | [Q2 2026 letter](../../research/sources/block-q2-2026-shareholder-letter.md); [Q2 2026 call](../../research/sources/fool-block-q2-2026-earnings-call.md) (FP) |

**Builder programmes.**
- An AI enablement group ran a code-fluency programme for Cash App designers, moving them from sandbox PRs to production PRs with engineers pairing ([Worboys](../../research/sources/dive-club-cam-worboys-ai-native-design-org.md), FP, 2026-03-05).
- The Square APM programme asks applicants for "something you built using AI tools" ([APM](../../research/sources/block-square-apm-program.md), FP).
- A Builder Fellowship pilot hires ten builders chosen on proof of building ([fellowship](../../research/sources/block-builder-fellowship.md), FP).
- The CTO says hiring now looks for a "learning mindset" more than AI skill ([Lenny's](../../research/sources/lenny-podcast-block-dhanji-goose.md)).

## 3. PM practice across the lifecycle

Detail with handoffs is in [the map](01-pdlc-block.md). In brief:

- **Discovery and customer contact.**
  - No agent is named. The PM role still asks for customer research ([PM job post](../../research/sources/block-careers-staff-pm-post-checkout.md)).
  - Leaders argue the customer signal will come from customer agents instead: Managerbot and Moneybot requests "align with our roadmap" ([Q1 2026 letter](../../research/sources/block-q1-2026-shareholder-letter.md)). Composition failures would become the roadmap ([essay](../../research/sources/block-from-hierarchy-to-intelligence.md)). Dorsey: customers' queries "make the majority of the decisions" ([Sequoia](../../research/sources/sequoia-dorsey-every-company-mini-agi.md)).
- **Research and data.** This is the best-evidenced PM-adjacent use. goose works with the governed Data MCP and Query Expert. A Cash App growth manager is to "diagnose your own funnel ... without waiting on an analyst", using Claude Code or Goose ([growth job post](../../research/sources/block-careers-growth-manager-activation.md), FP, 2026-10-06).
- **Specs.**
  - Prototypes are replacing documents. Dorsey: "everyone is bringing a prototype that they built" instead of decks or Google Docs ([Sequoia](../../research/sources/sequoia-dorsey-every-company-mini-agi.md), FP, ~2026-04-02).
  - Cash App design runs Friday demos and deleted crits as an experiment ([Worboys](../../research/sources/dive-club-cam-worboys-ai-native-design-org.md)).
  - No PRD agent or recipe was found.
- **Prototyping.** Designers use Cursor, V0 and Figma Make ([designer post](../../research/sources/builtin-cash-app-staff-product-designer-access.md)); PMs use "AI tools to turn ideas into working prototypes" ([PM post](../../research/sources/block-careers-staff-pm-post-checkout.md)). The only goose blog post that names PMs says agentic coding lets them "prototype full-stack applications" ([vibe code responsibly](../../research/sources/goose-blog-vibe-code-responsibly.md), FP, 2025-04-08).
- **Build.** PMs and designers ship PRs (claims by Jennings and Worboys). Jennings says PMs and growth marketers run many agents in parallel, and Builderbot gets features to "85 or 90%" before a human finishes them ([Jennings](../../research/sources/a16z-owen-jennings-block-all-in-on-ai.md)).
- **Reviews.** AI reviews 90%+ of change requests, and a person makes the final push ([Q1 2026 letter](../../research/sources/block-q1-2026-shareholder-letter.md)). How PM-authored PRs are reviewed is not described.
- **Numbers and outcomes.**
  - Every figure comes from Block (see the evaluation row in the contributions file). There is no product-outcome measure.
  - The only product-level figure is "130 features" in H1 2026, and "feature" is not defined ([Q2 2026 call](../../research/sources/fool-block-q2-2026-earnings-call.md)).
  - A Cash App design leader says the bottleneck has moved from building to the operational processes that get work to customers ([Worboys](../../research/sources/dive-club-cam-worboys-ai-native-design-org.md)).

## 4. Contrast with the other ecosystems

The other maps are in [the cross-ecosystem map](../pdlc-cross-ecosystem-map/README.md). The [Airbnb map](../research-airbnb-spotify-product-practices/01-pdlc-airbnb.md) landed as this was finished and is included. The Spotify map had not landed yet.

| | Block | Stripe | Ramp | Shopify | Anthropic | Atlassian | Intercom | Airbnb |
|---|---|---|---|---|---|---|---|---|
| **Loop source** | Own open-source harness (goose), now foundation-governed; engineers also buy seven coding harnesses | Forked goose for Minions; own Kai, Harbor, Orbit | Own harness (Laminar) under every stage agent | Own agent (River) | Own products (Claude Code, Cowork) | Own platform agents (Rovo) plus third-party coding agents | Bought harness (Claude Code) for everyone | Own harness (AirChat) wrapping Claude Code and Codex behind one gateway |
| **Agent unit** | General agent per person + recipes + shared services (Builderbot, Query Expert) | One named agent per task | One agent per stage on one harness | One general agent in public threads, plus pipelines | General harness + skills + engineered reviewers | Narrow agents attached to platform objects | General harness, 267 skills, two custom agents | AirChat plus apps on its SDK (Insight Miner, Pascal) |
| **Interface** | Desktop/CLI per person; Slack and tickets for Builderbot; internal web apps (App Kit) | Web app, Slack, Chrome; Minions from a Slack emoji | Glass desktop app; Inspect from Slack, web, PRs | Slack only, public channels | Terminal, IDE, Slack, Cowork | Embedded in Jira, Confluence, Loom | Terminal; GitHub; Slack | AirChat CLI and apps; AirChat Remote |
| **Sharing default** | goose sessions local, single-user; the Builderbot thread is shared | Kai sessions private; Orbit workspaces shared | Glass private with share; Inspect multiplayer | Public by default, no private mode | Channels public within org | Platform permissions | Local, private; PR description is the record | Not a focus of the map |
| **Research → plan across people** | Unknown; removed by role collapse (DRI, squads of 1-6, PMs ship PRs) | Unknown; role blur ("product hat") | Named "contract", transport unknown | One public thread | Open channels | Work item carries the what, not the why | Captured at the PR | Roles widened, CEO bridges in reviews; Pascal drafts the concept brief; drift named |
| **Review** | AI on 90%+ of changes; human final push | Human on every PR + Gru | Review Buddy on 93%; humans on hard 7% | Human on every PR (a bottleneck) | Risk-tiered, 0-2 humans | Human + acceptance-criteria check | ~19% auto-approved by risk | Validation loops and a second model as critic; engineers must explain AI-written PRs; CEO reviews projects |
| **PM role** | Folding into IC builder / DRI; PMs ship PRs | Long had no PMs; engineers wear the "product hat" | Glass is the PM's define agent | Not the focus | PMs use Claude Code | PM is the platform's customer | PMs and designers in Claude Code | Classic PM split into product marketing, program management and business |
| **Evidence** | Mostly FP and VC; IND press on the cuts, with staff disputing the claims | Mostly FP | FP, VC | FP | FP | Product docs | FP (commercial interest) | Mostly FP; IND critiques of the operating model |

What Block adds to the set:
- **The opposite answer to Airbnb's.** Both moved to a functional organisation before their agent push. Airbnb split the PM's tasks across more people and puts the CEO in the gap. Block collapses the tasks into fewer people and lets agents and threads carry the rest.
- **The extreme of role collapse, and its visible cost.** Stripe blurs roles culturally, and Shopify gives everyone one public place. Block changed the org itself: functional, then flatter, then roughly 40% smaller. It names PMs shipping code as policy. It is also the only ecosystem with a documented independent counter-narrative, from staff, on whether the gains are real.
- **The originator of the open harness others fork.** Stripe's Minions fork goose. Block shows the internal setup that a fork does not bring with it: about 150 MCP servers, a governed data layer, distribution, and security review.
- **A two-tier unit.** A private general agent per person, plus shared services for the stages where output must converge (code, data). This sits between Ramp's stage agents and Intercom's one-harness-for-all.

## Options by dimension

Proposals are in options/contributions/research-block-product-practices.md, grouped under:
- loop-source
- harness-layering
- model-provider-coupling
- capability-format-portability
- capability-distribution-trust
- governance-control-plane
- work-structure (agent unit)
- intent-shaping-and-spec
- session-persistence-sharing
- agent-interface
- context-and-memory
- review-and-autonomy
- adoption-model
- target-user
- pm-agent-evaluation

There are two new option candidates:
- "Own general harness for everyone, buy coding harnesses for engineers" (loop-source).
- "Recipe as a parameterised task agent inside a general harness" (capability-format-portability).

There are also two cross-cutting key questions:
- Role collapse vs a handoff artifact.
- Separating the AI effect from the org effect.

No new dimension is proposed. The org-shape question could become one if Airbnb and Spotify show the same choice. New themes: `ai-flattened-org` and `capability-packaging-layers`.

## Could not verify

- **No first-hand PM account.** No Block or Square PM has described goose, Builderbot or agents in their own work. LinkedIn was not searched signed-in. The Agent Report's claim that 60% of employees use goose weekly, across 15 job profiles including PMs, has no source ([note](../../research/sources/agentreport-goose-recipe-60-percent.md)).
- **Builderbot.** Its internals and models, whether non-engineers invoke it directly, and whether it uses adversarial review. All its figures are VC.
- **Session sharing.** Whether goose sessions can be shared inside Block.
- **Unconfirmed systems.** How the default extensions and allowlist reach laptops (MDM or a custom build). Whether g2, the company "markdown file" or the "world model" exist as running systems.
- **Unread figures.** Jennings' reported "150%" code-change figure and The Information's "3x features" report were not read at source. The Q4 2025 shareholder letter PDF and the Q3 2026 letter were not read.
- **Dates.** The two Sequoia episodes are dated from directories (the pages carry no date). The Q1 and Q2 2026 letter dates come from coverage.

## Pattern classes

Added 2026-10-24 by teardowns-to-pattern-classes. This brief's agents are placed in the revised runtime pattern classes of the [taxonomy synthesis, B.2](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes). Every placement is sourced and marked clear, partial or contested in [the mapping, section 2.7](../../tasks/teardowns-to-pattern-classes/00-mapping.md#27-block); counts and strains are in [section 9](../../tasks/teardowns-to-pattern-classes/00-mapping.md#9-airbnb-spotify-and-block-added-2026-10-24).

- **P3 and P1:** goose is Block's own harness (clear) and every employee's general agent (partial, since P1 assumes a vendor's harness). Engineers also use seven bought coding harnesses (clear).
- **P7:** Builderbot takes a ticket or Slack tag to a merged PR (clear on behaviour; vendor-claim figures; runtime not described). Overnight goose agents are partial.
- **P10:** the PR-reviewed skills marketplace and `ai-rules` generator give both a governed registry and cross-harness distribution (clear).
- **P9:** Actionable CI wraps headless goose in deterministic gates (clear); recipes are partial.
- **P8 and P4:** Buzz is P8b, channel-scoped with each agent's own identity (clear on design, no usage figures), and partly P4. Builderbot threads are P8 with no sub-type set (partial).
- **Partial, thin:** the Data MCP and Query Expert (P6) and Berd (P5a). Managerbot, Moneybot, App Kit and g2 fit no class.
