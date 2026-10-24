# Teardown: Shopify River and Aquifer (summary)

Date: 2026-10-24. Worker draft for Geoff's review (task: [competitive-teardown-shopify-river](../competitive-teardown-shopify-river.md)). Source notes are in the research library (`../../research/sources/`); this summary links to them and doesn't copy them.

**Evidence status, read this first.** Almost everything here is Shopify's own account: engineering blog posts, Tobi Lütke's X posts and podcast remarks, and executives' interviews. The independent sources found (ZenML, Port, adaptordie, Internal Agents Map, Dealroom, Simon Willison, others listed below) mostly restate Shopify's numbers. Nobody outside Shopify has measured River's outcomes, quality, cost or privacy effects. The architecture descriptions (Aquifer's session/harness/sandbox split, profiles, session cells) come from the builders and are specific and technically credible. The outcome numbers (merge rate, PR share, backlog cuts) have no stated method. Dates matter: the River story runs from March to October 2026 and the numbers change fast.

## Sources read in full

Primary, first-party Shopify:
- [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (Burke Libbey, Javier Moreno, "and River", Shopify Engineering, 2026-05-28): the architecture post.
- [Learning on the Shop floor](../../research/sources/x-tobi-learning-on-the-shop-floor.md) (Tobi Lütke, X article, 2026-05-09): the philosophy post, public-only rule, Lehrwerkstatt, 36%→77%.
- [Tobi's replies under that post](../../research/sources/x-tobi-river-replies-may-2026.md) (2026-05-09/11) and [River's own reaction](../../research/sources/x-tobi-river-reaction-to-shop-floor-post.md) (2026-05-10), which names the chilling-effect cost.
- [River floods Shopify chart](../../research/sources/x-tobi-river-floods-shopify-chart.md) (Tobi, X, 2026-10-19): March vs September 2026 usage.
- [Knowledge Project podcast with Tobi](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md) (Shane Parrish, 2026-09-10; [transcript](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.transcript.md)): memory per person and per channel, "dreaming", persona, "up to about 50%" of PRs created from chat conversations.
- [How River takes security work from a fix to merge](../../research/sources/shopify-engineering-river-vulnerability-remediation.md) (Erin Son, Kaiyi Li, 2026-09-02): River in automation mode.
- [We gave AI agents a mobile dev environment (Remote Dev)](../../research/sources/shopify-engineering-remote-dev.md) (2026-10-22): River on remote Macs, 6%→61% of merged mobile PRs, the Jev classifier that mines threads.
- [Quick](../../research/sources/shopify-engineering-quick.md) (2026-06-10): internal hosting for agent-made sites, open to all employees with no owners.
- Context posts: [Dispatch security harness](../../research/sources/shopify-engineering-agentic-harness-outlasts-model.md) (2026-07-29), [Roast](../../research/sources/shopify-engineering-introducing-roast.md) (2025-06-18), [Farhan Thawar on Beyond the Pilot](../../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md) (2026-06), [BVP playbook](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md) (2026-04-02), [First Round on Shopify's AI culture](../../research/sources/firstround-shopify-ai-culture.md) (2025-07-15).

Independent or secondary: [ZenML on Under the River](../../research/sources/zenml-llmops-shopify-river-durable-infrastructure.md), [ZenML on the public workspace](../../research/sources/zenml-llmops-shopify-river-public-workspace.md), [VentureBeat on Shopify's model-agnostic stack](../../research/sources/venturebeat-shopify-ai-stack-model-agnostic.md), [Port software-factories profile](../../research/sources/port-software-factories-shopify.md), [adaptordie](../../research/sources/adaptordie-shopify-river-agent-stack.md), [Internal Agents Map](../../research/sources/internal-agents-shopify-river.md), [Dealroom](../../research/sources/dealroom-river-threads-121804.md), [Simon Willison](../../research/sources/simonwillison-learning-on-the-shop-floor.md). Counter-evidence for the privacy question: [Bernstein, The Transparency Paradox (ASQ 2012)](../../research/sources/asq-bernstein-transparency-paradox.md) and [Slack information barriers](../../research/sources/slack-information-barriers-docs.md). Further secondary notes filed by the subagent are listed in [research/INDEX.md](../../research/INDEX.md) under filed_by `competitive-teardown-shopify-river`.

## What River and Aquifer are, and how they relate

- **River** is an AI agent that lives in Shopify's Slack. You @-mention it in a channel, it replies in thread, and it reads code, runs tests, opens PRs, queries the data warehouse and reads production traces. It **refuses DMs and private channels**: "River only works in the open" ([Under the River](../../research/sources/shopify-engineering-under-the-river.md), Part II); "you can't go into a private channel and say, 'Hey, River, help me build'" (Farhan Thawar, [Beyond the Pilot](../../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md), ~2026-06). It is pull-only: "you can talk to it, but it doesn't talk to you". It has a name, an avatar, a "she", a sarcastic persona and a "soul" markdown file ([Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md)). The name: "Rivers shape the world" (the monorepo is called World) ([Tobi reply](../../research/sources/x-tobi-river-replies-may-2026.md)).
- **Aquifer** is Shopify's internal platform for running agents: session, harness, sandbox, gateway, durable event log, credentials proxy and observability pipeline. "River is a profile on top of it." Other profiles include PR review and "Vanilla, the headless 'pi' agent" ([Under the River](../../research/sources/shopify-engineering-under-the-river.md), Part III).
- **World** is the monorepo (2024 decision), built with **Nix** (dev = CI = prod). It holds code plus skills, conventions, intent documents, runbooks, AGENTS.md and "zone knowledge". Shopify calls it "an intelligence layer" that sessions add to ("a pebble, a skill update, an AGENTS.md diff").
- **Relationship:** the slogan is "Rivers shape the World. The Aquifer holds the water." River is the visible surface, Aquifer the substrate, World the context. Shopify's own claim is that "the agent will not be the interesting part" two years from now; the substrate will be.

**Timeline (dated):**
- Spring 2024: monorepo and Nix bets.
- Jul 2025: Quick launched.
- Early 2026: River launched. Under the River says "a couple of months" before 2026-05-28, but Tobi's chart shows 35,418 threads already in March 2026, so launch was probably Q1.
- 2026-05-09: Tobi's article.
- 2026-05-28: Under the River.
- 2026-09-02: security remediation.
- 2026-09-10: Knowledge Project.
- 2026-10-19: September usage chart.
- 2026-10-22: Remote Dev.

Tobi says the public-only rule was "a late choice in the process" ([Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md)), and in May called the learning effect "somewhat accidental".

## Teardown by dimension

Each heading is a dimension in [options/DIMENSIONS.md](../../options/DIMENSIONS.md). "Not disclosed" means nothing was found in any source.

### Loop source and harness layering
Aquifer runs **its own harness**: "The agent loop. Reads history, calls the model, emits tool intents. Cheap to recreate, disposable." The harness lives **outside the sandbox** ("decouple the brain from the hands"), which Shopify credits to the same insight as Anthropic's Managed Agents essay (Apr 2026). That split gives three properties: safety (the loop is outside the `rm -rf` blast radius), replaceability ("swap models, runtimes, even languages on the harness side") and observability (the whole decision stream is in one place).

There is no layer above vendor harnesses. Instead, one substrate sits under many agent "profiles". The headless "pi" profile may be the open-source Pi agent; the adaptordie commentator calls that "likely", and it is unverified. Tobi credits OpenClaw with the "stable patterns by which we can now build Rivers" (file systems, soul files) ([Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md)).

Earlier Shopify tooling embedded Claude Code inside Roast workflows ([Roast](../../research/sources/shopify-engineering-introducing-roast.md), 2025), so the move to an own harness is recent. **Glass comparison:** Glass embeds Anthropic's Agent SDK inside a desktop app. River runs an own loop on an own substrate, the opposite end of [[loop-source]].

### Runtime location and durability substrate
Server-side and org-deployed. A live session materialises a **session cell**: an ephemeral process on a host, running a Go runtime and the harness in one process group. It exits when idle, and the next message may land on a different host. "Cattle, not pets, at the session level."

The **session is an append-only, Postgres-backed event log**, the "canonical truth". Sandboxes are disposable, "sometimes warm, often fresh". The orchestrator is not named ("matters less than the principle"). Remote Dev adds a warm pool of remote Macs plus Linux VMs for Android, claimed over SSH per session, so mobile work no longer needs laptops ([Remote Dev](../../research/sources/shopify-engineering-remote-dev.md)).

**Glass comparison:** Glass "turns your laptop into a server"; River never depended on a laptop.

### Capability format, portability and distribution
- **Profiles are data:** "a system prompt, a set of skills, a set of extensions, a sandbox policy, model defaults", all built with Nix and shipped as bundles. A new agent product is a new bundle, not a new platform.
- **Skills** are files in World, loaded on demand. Channels "pre-load the zones, skills, and instructions" their team needs ([Tobi](../../research/sources/x-tobi-learning-on-the-shop-floor.md)). One team's checkout-warehouse skill "gets reused by twelve other teams".
- **Distribution** is the monorepo itself: skill changes go through normal code review, merge queue and CI. No separate marketplace was mentioned.
- **Glass comparison:** Glass's Dojo is a Git-backed marketplace with the Git hidden from users. Shopify keeps skills in the same repo as code and doesn't hide it.
- **Not disclosed:** whether skills follow SKILL.md or another format, and any review or trust process specific to skills.

### Remote invocation route
Slack is the invocation channel for humans. Aquifer names three modes on one stack:
- **Interactive:** River, a durable session with a live human.
- **Automation:** PR review, woken by an external system, "often no human in the loop".
- **Job:** CI and batch work, ephemeral, with the session log optional.

The security workflow shows automation mode in practice: River reads a ledger, opens one Slack thread per finding (four threads covering 35 findings went up within a minute), and later runs check back on them ([vuln remediation](../../research/sources/shopify-engineering-river-vulnerability-remediation.md)). Overnight mobile bug-fix runs are scheduled the same way ([Remote Dev](../../research/sources/shopify-engineering-remote-dev.md)).

**Not disclosed:** any API, MCP or A2A route for calling River from another harness. Tobi says River "has the ability, although not really utilized, to join Google Meets".

### Session persistence and sharing
This is the core of the design. Sessions are durable (the event log), threaded (Slack), multiplayer (anyone can join a thread) and searchable. The "good thread" pattern: one person asks; River posts partial findings; "a second human... drops in with a constraint or a redirect"; River continues. Shopify claims a median session of 19 minutes and 50 tool calls.

Co-participation grew from 61,680 "wrote in the same thread" links in March 2026 to 171,853 in September ([chart](../../research/sources/x-tobi-river-floods-shopify-chart.md)). That is the only multiplayer metric anyone has published (Glass has none).

Remote Dev's Live Preview streams the running app to a shareable web link that several people can use at once.

### Agent identity and delegation (thin evidence)
Shopify says almost nothing here:
- Aquifer has a **credentials proxy** and a **gateway** (Under the River). Dispatch uses "deterministic code that owns credentials, Git, and storage so the agents don't have to" ([Dispatch](../../research/sources/shopify-engineering-agentic-harness-outlasts-model.md)).
- Tobi: River "has access to all the code, all the systems, all the tools. It's all sandboxed and secure" ([Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md)).
- The open question is whose permissions River uses when someone in a public thread asks it to query the data warehouse. "All the systems" for anyone who can post suggests a **service identity**, not on-behalf-of. That would make the Claude Tag critique apply (whoever can post in the channel can direct the agent) ([Tenable](../../research/sources/tenable-claude-tag-slack-access-model.md)). **Unverified.**
- Thawar: "River can see Slack messages, it can query into our data warehouse, it can see our product management system" ([Beyond the Pilot](../../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md)). Shopify's assistant MCP tools, by contrast, go "through the same auth flow that you have", so they see only what the user can ([BVP](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md), 2026-04; not about River). Port reports the LLM proxy does PII masking and injection detection ([Port](../../research/sources/port-software-factories-shopify.md); secondary).
- PRs are "coauthored" by River and "reviewed by us", which looks like the agent-as-co-author pattern.

### Governance, cost and audit
- **Audit by construction:** every session is a public Slack transcript plus an event log, River writes a `river_sessions` domain table every session, and the harness-side decision stream is observable.
- **Cost:** not disclosed for River. Shopify-wide there are no token caps, but there are "circuit breakers" and $250/day spend alerts ([BVP](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md); [VentureBeat](../../research/sources/venturebeat-shopify-ai-stack-model-agnostic.md)). Shopify-wide, Farhan Thawar says they replaced a token leaderboard with a usage dashboard on which "any person in the company can see their spend in AI", and leaders ask high spenders "What are you actually trying to do here?" ([Beyond the Pilot](../../research/sources/venturebeat-beyond-the-pilot-farhan-thawar.md), 2026-06). River token spend is "going up", with no figure.
- Model routing goes through an internal LLM proxy, which failed users over automatically "when Claude Fable 5 shut down" ([VentureBeat](../../research/sources/venturebeat-shopify-ai-stack-model-agnostic.md)). Distillation to smaller models is a stated cost strategy.
- **Glass comparison:** Glass meters cost per project and routes through Ramp Router. River's governance story is visibility, not metering.

### Model-provider coupling and harness upkeep
River's models are **not disclosed**. The design is explicitly built for model swaps: the harness is replaceable and profiles carry "model defaults". The company proxy is model-agnostic. Tobi's personal agent mixes Grok, ChatGPT, Opus, Kimi and Fable, but that is not River.

Upkeep is done by a platform team ("Aquifer is rolling out underneath it, profile by profile") and by everyone: skills improve through the corpus and nightly "dreaming" ([Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md)). Remote Dev shows the cost of upkeep: River "always stated that an iOS build cannot run on Linux" until a skill was iterated several times ([Remote Dev](../../research/sources/shopify-engineering-remote-dev.md)).

### Context, memory and data (what Aquifer and World provide)
- **Context = World.** One repo with code, skills, AGENTS.md, intent documents, runbooks and zone knowledge. River sits at the repo root and can navigate across zones, from a production log line to the commit that caused it.
- **Data:** the data warehouse and production traces are reachable as tools.
- **Memory:** per-person crystallised memory is injected at session start, plus channel memory depending on where the session runs. It is produced by an off-hours **"dreaming"** job that reviews the day's conversations and skill use and rewrites "text files, skill files and instructions", not weights. Tobi's May article calls it a memory "constantly learning and un-learning".
- **Corpus mining:** the public transcript corpus is mined and patterns fed back into skills, prompts and defaults. On mobile, the "Jev" classifier tags every River mobile conversation by outcome, and the failures are fed to an LLM to propose improvements ([Remote Dev](../../research/sources/shopify-engineering-remote-dev.md)).
- **Ledgers:** the security workflow keeps a work ledger, treated as "a claim to be checked, not a fact".
- **Glass comparison:** both use offline pipelines that rewrite file-based memory (Glass every 24 hours, River nightly "dreaming"). Glass memory is per user, read-only during a session and inspectable. River adds channel memory and a public corpus.

### Artifacts and projects
There is no project object. The **channel is the de facto project container** (Tobi's #tobi_river, team channels that pre-load skills), and the **thread is the unit of work**.

Outputs are PRs (in World), Quick sites (50,000+ sites, open to all employees, no owners ([Quick](../../research/sources/shopify-engineering-quick.md))), Live Preview links, and explainer videos River generates from simulator recordings ([Remote Dev](../../research/sources/shopify-engineering-remote-dev.md)). Tobi describes threads ending in "summarize this, create a ticket... make a diagram... create a prototype", with the result "an hour or so later".

**Not disclosed:** where non-code artifacts (specs, decks) are stored or how they're found other than by Slack search.

### Target users and outcomes
The nominal target is everyone: 7,000+ people touched in 30 days (May), 6,273 "Shopifolk" in the September graph, out of roughly 7,600 employees ([Port](../../research/sources/port-software-factories-shopify.md), 10-K headcount). The examples are mostly engineering: PRs, tests, rebases, CI, security, mobile.

Non-engineers appear only in examples: a support engineer copying a log query, and on Remote Dev "a designer can iterate on a UI, and a PM can test a feature, all through Slack". No breakdown by role is published.

The stated outcome is **organisational learning and speed** ("the company moves at the speed of its slowest secret"), not individual productivity.

### Evaluation and results (numbers, all self-reported)

| Claim | Date / window | Source | Status |
|---|---|---|---|
| 5,938 employees, 4,450 channels | 30 days to ~2026-05-09 | [Tobi](../../research/sources/x-tobi-learning-on-the-shop-floor.md) | Self-reported |
| 1,870 PRs opened in a week; ~1 in 8 merged PRs "authored by River, reviewed by us" | week to ~2026-05-09 | [Tobi](../../research/sources/x-tobi-learning-on-the-shop-floor.md) | Self-reported. ZenML conflates the two figures ([note](../../research/sources/zenml-llmops-shopify-river-public-workspace.md)) |
| Merge rate 36% → 77% in two months, "did not retrain... did not switch models" | ~Mar–May 2026 | [Tobi](../../research/sources/x-tobi-learning-on-the-shop-floor.md) | No definition of merge rate or base. Attributed to people writing skills |
| 59,918 sessions, 5,170 channels, 7,000+ people, 3,536 coauthored merged PRs; median 19 min, 50 tool calls | 30 days to ~2026-05-28 | [Under the River](../../research/sources/shopify-engineering-under-the-river.md) | From River's own `river_sessions` table |
| River threads 35,418 → 121,804 per month; people 4,147 → 6,273; same-thread links 61,680 → 171,853 | Mar → Sep 2026 | [chart](../../research/sources/x-tobi-river-floods-shopify-chart.md) | Volume only. Dealroom notes it proves nothing about productivity ([Dealroom](../../research/sources/dealroom-river-threads-121804.md)) |
| "Up to about 50%" of PRs "created... out of conversations in our common company chat" | said ~Sep 2026 | [Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md) | Hedged ("I want to say"). Secondary outlets inflated it to "River writes half of PRs" |
| Dependency vulnerability backlog −70% in 11 days; security merges via freshness-gated queue ~10% → ~80% | from launch, reported 2026-09-02 | [vuln remediation](../../research/sources/shopify-engineering-river-vulnerability-remediation.md) | Self-reported, no base count. The post itself warns "PR count and green-branch count measure motion, not remediation" |
| River's share of merged mobile PRs 6% → 61% | window not in text, reported 2026-10-22 | [Remote Dev](../../research/sources/shopify-engineering-remote-dev.md) | Self-reported. Attributed to Remote Dev plus internal ad campaigns |

There are no published evals, no quality or defect data, no cost per session, no comparison with a private-agent control, and no independent measurement.

### Review and autonomy
Humans review and merge: "authored by River, reviewed by us". In security work River runs "draft-only" under "human merge authority", and hands off "the decision, not the investigation" with "the smallest question that an owner has to answer". It also left a branch alone when a human had taken it over.

The sharpest lesson: "Prompts are the right place to express judgment and the wrong place to express a guarantee." Rules that decide closure must be enforced in code ([vuln remediation](../../research/sources/shopify-engineering-river-vulnerability-remediation.md)). Review is now the bottleneck: "We still require a human PR reviewer, which is now becoming a big bottleneck" (Thawar, [BVP](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md), 2026-04), and Tobi names "slop grenades": unread agent PRs that push the review load onto colleagues ([Knowledge Project](../../research/sources/fs-knowledge-project-tobi-lutke-ai-agents.md)). Public threads add what River calls an "honesty pressure" on both agent and user ([River's reaction](../../research/sources/x-tobi-river-reaction-to-shop-floor-post.md)).

### Work structure, sequencing, intent shaping
- **Work structure:** one general agent (River) for open-ended work, with specialised workflows layered on as skills and profiles (PR review, security remediation, migrations, compliance scans). Separately, Dispatch and Helix are structured multi-stage harnesses for narrow jobs.
- **Sequencing:** substrate first (monorepo, Nix, CI, 2024), agent second (2026). Shopify says the order is the point: "If your second agent forces a second platform, you haven't built the substrate yet."
- **Intent shaping:** "intent documents" live in World, and threads often turn a human discussion into a ticket, diagram or prototype. Nothing more specific on specs was found.

### Adoption and enablement
Adoption ran on four things:
- **The surface plus visibility:** osmosis learning, the CEO working in public (#tobi_river, 100+ watchers).
- **Culture:** AI-reflexiveness is part of performance reviews ([BVP](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md)), building on Tobi's 2025 "reflexive AI usage" memo.
- **Internal marketing:** the mobile team made AI-generated ads with River as a character, including a Mac-vs-PC parody, to win back people who had tried early River and gone back to local work ([Remote Dev](../../research/sources/shopify-engineering-remote-dev.md)).
- **Usage visibility:** a usage dashboard, not a leaderboard.

Tobi's framing is "no curriculum, no training plan, no manager". **Glass comparison:** Ramp also relies on the product itself and on mandates. Shopify adds visibility as the enablement mechanism.

### Agent interface (new dimension)
River is **chat-native only**: no app, no DMs, invoked with "@river" in a top-level post, then the thread. Tobi contrasts it with "private windows" (ChatGPT, Claude) and Cursor ("between you and the IDE"). The rationale is reach plus visibility in a remote-first company where "a lot of Shopify's work happens... in Slack", and the agent being pulled into threads already in progress.

Shopify still built companion surfaces for what Slack can't show: Quick sites, Live Preview, generated videos. **Glass is the opposite bet:** its own desktop app with panes and inline rendering, sessions private unless shared.

Open questions: whether chat-only works for artifact-heavy PM work (specs, decks), and how much of River's adoption is the surface versus the culture. Options and questions: [agent-interface](../../options/DIMENSIONS.md#agent-interface-agent-interface-own-app-chat-or-embedded).

### Trust and privacy model (new dimension)
River is **public by default org-wide with no private mode**: "Every conversation with River becomes a public Slack transcript, open by default to other Shopify employees." Quick sites apply the same idea to artifacts.

**Why** (Shopify's reasons):
1. Osmosis learning: the Lehrwerkstatt.
2. A corpus to mine into skills ("the privacy of an agent thread is a disadvantage").
3. Speed: private DMs are slow for the organisation.
4. Honesty pressure.
5. Tobi on what's being learned: "It's not about the transcript of the work. It's about seeing how other people begin the work."

**Risks:**
- **Chilling effect.** River itself: "Some questions that would have been asked in a DM just don't get asked", which it calls "mostly the right tradeoff... but it isn't free". Tobi: "Asking for help feels different when the whole company can see the question."
- **Sensitive data.** The sources say nothing on how HR, legal, M&A, security findings or customer PII are handled. The security remediation post doesn't say where its threads live. A commentator notes "A pricing conversation may need a tighter audience" ([adaptordie](../../research/sources/adaptordie-shopify-river-agent-stack.md)).
- **Permissions.** If River acts with broad access ("all the systems") for anyone in a public channel, channel membership becomes the access control (the Claude Tag pattern).
- **Regulated settings.** Slack's information barriers don't stop interaction in shared channels ([Slack docs](../../research/sources/slack-information-barriers-docs.md)), so a public-by-default agent inherits that gap.
- **Critiques found:**
  - [AI Slopcast](../../research/sources/oleg-guru-ai-slopcast-shopify-river-lehrwerkstatt.md) (2026-05-14) says a public archive of everyone's gaps is "a treasure trove" for HR, and that metrics are curated.
  - [Magica](../../research/sources/magica-shopify-river-agent-context-cost.md) (2026-08-25) quotes Slack's CPO: there is a boundary for "genuinely sensitive work", and "psychological safety should determine where openness stops". It also calls the metrics activity, not ROI.
  - On HN, one commenter said the way they speak to agents wouldn't be "kosher in a company slack" ([HN](../../research/sources/hn-shopify-river-discussion.md), anecdote).
- **No first-party answer** to any of these critiques was found.
- **Counter-evidence on learning.** Bernstein's field experiment found that broad visibility bred hiding, and that small privacy zones raised output 10–15% ([Bernstein](../../research/sources/asq-bernstein-transparency-paradox.md); factory floor, 2009).

Options and questions: [trust-privacy-defaults](../../options/DIMENSIONS.md#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context).

## River vs Glass at a glance

| | Shopify River | Ramp Glass |
|---|---|---|
| Surface | Slack only, no DMs | Own desktop app (plus Slack assistants) |
| Default visibility | Public to all employees | Private, share a session on demand |
| Loop | Own harness on own substrate (Aquifer), outside the sandbox | Anthropic Agent SDK embedded in the app |
| Runtime | Server-side session cells; durable Postgres event log | Laptop is the server |
| Capability packaging | Profiles (prompt, skills, extensions, sandbox policy, model defaults) as Nix bundles; skills in the monorepo | Skills in a Git-backed marketplace (Dojo) with Git hidden |
| Memory | Per-person + per-channel, from nightly "dreaming"; public corpus mined | Per-user files from a 24-hour pipeline, read-only in session |
| Cost control | Usage dashboard, personal spend visible; River cost not disclosed | Per-project meter, model router, claimed 30% saving |
| Users | Nominally everyone; evidence mostly engineering | Whole company, positioned for non-engineers |
| Strongest number | ~1 in 8 merged PRs coauthored (May 2026); 121,804 threads (Sep 2026) | 99.5% daily AI use; 700 DAU in a month |
| Independent evidence | None on outcomes | None on outcomes |

## Design choices worth stealing (as options, not recommendations)
1. **Session as the thing that survives:** an append-only event log, with harness and sandbox disposable. "You will not be able to retrofit it."
2. **Next agent = a profile, not a platform:** config bundles on one substrate, with interactive, automation and job modes.
3. **Make the org legible first:** monorepo, reproducible environments, written-down skills. "Agent-friendly ≈ human-friendly."
4. **Mine sessions for improvements:** a classifier over threads, failures fed to an LLM, nightly "dreaming" that edits skills.
5. **Guarantees in code, judgement in prompts,** and hand off one small question with the evidence.
6. **Chat-native front door with companion links** for rich output.
7. **Public by default** as a learning mechanism, which is the most contested choice and needs its own trial.

## What remains unverified / gaps
- River's models, cost per session, identity model (whose credentials, what scoping), how sensitive or private work is handled, and whether any exceptions to the no-DM rule exist (private channels? security threads?).
- What "merge rate" means; the time window for 6%→61%; River's exact launch date.
- Whether "pi" is the open-source Pi agent.
- Not read: a LinkedIn post about Javier Moreno's Toronto talk (it reportedly says River is used by engineering, support, sales and design; LinkedIn blocked access), Burke Libbey's SCALE 23x and NixCon talks, WSJ 2026-08-24, shopifreaks (403), and YouTube captions for Shopify's 64-second River promo.
- No independent outcome, quality or privacy-effect evidence. No interviews with Shopify staff outside leadership and the authors. LinkedIn coverage: see the subagent's notes in INDEX; anything behind login was not read.
- I read Tobi's X article via the fxtwitter API JSON (cross-checked against a mirror) and found his replies via X search in the logged-in browser (read-only). X search may miss replies that don't use the searched words.

## Options by dimension

River and Aquifer are one data point each on the menu, not a pattern to copy. Rows and key questions are filed in [options/DIMENSIONS.md](../../options/DIMENSIONS.md):

- **New, opened by this task:** [agent-interface](../../options/DIMENSIONS.md#agent-interface-agent-interface-own-app-chat-or-embedded) (own app vs chat-native vs IDE vs embedded vs multi-surface) and [trust-privacy-defaults](../../options/DIMENSIONS.md#trust-privacy-defaults-trust-and-privacy-defaults-for-sessions-and-context) (private by default → public by default org-wide). The Stripe teardown appended Kai and Minions rows to both.
- **Existing dimensions with River/Aquifer rows added:** [loop-source](../../options/DIMENSIONS.md#loop-source-who-supplies-the-agent-loop), [harness-layering](../../options/DIMENSIONS.md#harness-layering-is-there-a-layer-above-the-vendor-harnesses), [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives), [capability-format-portability](../../options/DIMENSIONS.md#capability-format-portability-capability-format-and-portability), [remote-invocation-route](../../options/DIMENSIONS.md#remote-invocation-route-how-a-primary-harness-reaches-a-remote-or-deployed-agent), [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff), [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation), [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-governance-and-control-plane-policy-cost-audit), [durability-substrate](../../options/DIMENSIONS.md#durability-substrate-how-persistence-and-recovery-are-implemented), [context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory), [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found), [pm-agent-evaluation](../../options/DIMENSIONS.md#pm-agent-evaluation-how-we-would-know-a-pm-agent-works), [review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy), [sequencing](../../options/DIMENSIONS.md#sequencing-which-jobs-first-and-which-layer-first), [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model).
- **Cross-cutting question added:** does the strategy assume the target org will accept work being visible by default? It bears on interface, trust, memory, adoption and identity at once.
