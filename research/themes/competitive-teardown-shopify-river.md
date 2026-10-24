# Theme evidence: competitive-teardown-shopify-river

Written only by the task `competitive-teardown-shopify-river`. Built into ../THEMES.md by ../build.py.

## compounding-context-repo: Context that compounds with each shipped feature
- [Under the River](sources/shopify-engineering-under-the-river.md): monorepo World holds code, skills, conventions, intent documents, runbooks, AGENTS.md and zone knowledge; sessions leave "a pebble, a skill update, an AGENTS.md diff" (competitive-teardown-shopify-river)
- [River's reaction to the Shop floor post](sources/x-tobi-river-reaction-to-shop-floor-post.md): "AGENTS.md files are mirror surfaces": writing them forces teams to find they "didn't quite agree with each other" (competitive-teardown-shopify-river)
- [Shopify's River: The AI Agent as Organizational Memory](sources/aienabledpm-shopify-river-organizational-memory.md): agent failures as context, permission and taste gaps, fixed by making knowledge explicit (competitive-teardown-shopify-river)

## risk-sloped-review: Human review sloped to risk
- [How River takes security work from a fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): "Hand off the decision, not the investigation"; River recommended dropping its own patch when a developer surfaced the original requirement (competitive-teardown-shopify-river)

## harness-over-model: The harness, not the model, limits real-world value
- [Building an agentic harness that outlasts the model](sources/shopify-engineering-agentic-harness-outlasts-model.md): better models gave more noise; all 30+ candidates in one audit were downgraded; the harness is the durable asset (competitive-teardown-shopify-river)
- [Introducing Roast](sources/shopify-engineering-introducing-roast.md): "Non-determinism is the enemy of reliability"; YAML + markdown steps interleaved with a Claude Code CodingAgent (competitive-teardown-shopify-river)
- [Learning on the Shop floor](sources/x-tobi-learning-on-the-shop-floor.md): 36%→77% merge rate "did not retrain a model... did not switch models" (self-reported) (competitive-teardown-shopify-river)

## org-learning-loop: One person's win becomes everyone's baseline
- [Learning on the Shop floor](sources/x-tobi-learning-on-the-shop-floor.md): River refuses DMs so others learn by watching (Lehrwerkstatt); a checkout-warehouse skill reused by 12 teams; merge rate 36%→77% credited to people writing down what River should have known (self-reported) (competitive-teardown-shopify-river)
- [Tobi's replies about River](sources/x-tobi-river-replies-may-2026.md): "It's not about the transcript of the work. It's about seeing how other people begin the work with the ai" (competitive-teardown-shopify-river)
- [Under the River](sources/shopify-engineering-under-the-river.md): the public transcript corpus is mined and fed back into skills, prompts and defaults; "the privacy of an agent thread is a disadvantage" (competitive-teardown-shopify-river)
- [Tobi Lütke: AI Agents, Better Decisions (Knowledge Project)](sources/fs-knowledge-project-tobi-lutke-ai-agents.md): open channels only, to recreate office "osmosis learning"; "a late choice ... one of my favorite calls" (competitive-teardown-shopify-river)
- [We gave AI agents a mobile dev environment](sources/shopify-engineering-remote-dev.md): the cheap "Jev" classifier tags every mobile River thread, scores outcomes, and failures feed an LLM to improve River (competitive-teardown-shopify-river)
- [Learning on the Shop floor (Simon Willison)](sources/simonwillison-learning-on-the-shop-floor.md): compares River to Midjourney's public-Discord interface as a way to learn a finicky new skill (independent opinion) (competitive-teardown-shopify-river)
- [The Transparency Paradox (Bernstein)](sources/asq-bernstein-transparency-paradox.md): counter-evidence: broad visibility bred hiding; curtained lines +10–15% output; learning shared upward once there was data (independent, factory 2009) (competitive-teardown-shopify-river)
- [Shopify River (Ashgaliyev wiki)](sources/ashgaliyev-wiki-shopify-river.md): River as "organizational apprenticeship" (competitive-teardown-shopify-river)
- [River: Shopify's Slack-native AI agent (video)](sources/youtube-shopify-river-slack-native-agent.md): official one-line positioning is the public-only constraint (competitive-teardown-shopify-river)

## memory-architecture: Memory as inspectable files from an offline pipeline
- [Tobi Lütke: AI Agents, Better Decisions (Knowledge Project)](sources/fs-knowledge-project-tobi-lutke-ai-agents.md): River "dreams" off-hours over the day's threads and rewrites skill files; per-person and per-channel memory injected at session start (competitive-teardown-shopify-river)
- [How River takes security work from a fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): the work ledger is "useful memory, but it isn't the operational truth"; each entry a claim to re-check (competitive-teardown-shopify-river)

## cost-control-routing: Cost metering and model routing built into the harness
- [Building an agentic harness that outlasts the model](sources/shopify-engineering-agentic-harness-outlasts-model.md): full scan $50–300, diff scan $5–50; partitions sized to 20–30% of the context window (competitive-teardown-shopify-river)
- [Small Models, Massive Wins (Beyond the Pilot)](sources/venturebeat-beyond-the-pilot-farhan-thawar.md): no token limits but "circuit breakers"; token leaderboard replaced by a usage dashboard where anyone sees their own spend (competitive-teardown-shopify-river)
- [How Shopify built an AI stack that doesn't care which models survive](sources/venturebeat-shopify-ai-stack-model-agnostic.md): the proxy auto-moved users to Opus or GPT 5.5 when "Claude Fable 5 shut down" (competitive-teardown-shopify-river)
- [From Memo to Movement](sources/firstround-shopify-ai-culture.md): in 2025 a token-spend leaderboard was "a cool proxy for value"; by 2026 it was removed (competitive-teardown-shopify-river)

## single-agent-many-skills: One agent with many skills, not many agents
- [Under the River](sources/shopify-engineering-under-the-river.md): new agents are "profiles" (prompt, skills, extensions, sandbox policy, model defaults) on one substrate: "a new bundle, not ... a new platform" (competitive-teardown-shopify-river)
- [Shopify Just Showed the Agent Stack](sources/adaptordie-shopify-river-agent-stack.md): "Pi is the engine room. River is the shop floor interface" (commentator's inference) (competitive-teardown-shopify-river)

## enablement-by-product: The product is the enablement
- [We gave AI agents a mobile dev environment](sources/shopify-engineering-remote-dev.md): adoption needed internal ads with a River persona; River went from 6% to 61% of merged mobile PRs (competitive-teardown-shopify-river)
- [Learning on the Shop floor](sources/x-tobi-learning-on-the-shop-floor.md): learning "does not require a curriculum, a training plan, or a manager. It just requires everyone's work to be visible" (competitive-teardown-shopify-river)
- [Make the Work Visible](sources/airealized-make-the-work-visible.md): visibility as the adoption lever; peer practices (AI Corner, failure labs) (competitive-teardown-shopify-river)

## non-engineer-builders: Non-engineers ship through agents
- [Quick: An internal hosting platform for the AI era](sources/shopify-engineering-quick.md): 50,000+ agent-made internal sites; over half the company has made one; skills bundled so any agent can deploy (competitive-teardown-shopify-river)

## legible-org-for-agents: Make the organisation legible to agents
- [Under the River](sources/shopify-engineering-under-the-river.md): 2024 monorepo + Nix bets; "agent-friendly ≈ human-friendly"; "The work to make a codebase legible to an agent is simply the debt you owe to your human engineers" (competitive-teardown-shopify-river)
- [How Shopify powers "World" (Flagship)](sources/flagship-ai-first-series-2-shopify-tectonix-nix.md): Nix reproducibility narrows agent build errors to pure code errors (competitive-teardown-shopify-river)

## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is rare
- [River threads jump to 121,804 (Dealroom)](sources/dealroom-river-threads-121804.md): thread volume alone does not prove productivity or quality; no independent impact measure (competitive-teardown-shopify-river)
- [Shopify: Building River (ZenML)](sources/zenml-llmops-shopify-river-durable-infrastructure.md): no models, cost, error rates or baselines disclosed (competitive-teardown-shopify-river)
- [Building a Public AI Agent Workspace (ZenML)](sources/zenml-llmops-shopify-river-public-workspace.md): security and permission model "aren't described"; the 23% unmerged are not discussed (competitive-teardown-shopify-river)
- [Inside Shopify's software factory (Port)](sources/port-software-factories-shopify.md): "1 in 8" has no definition of "coauthored"; best detail comes from press and VC interviews, not the blog (competitive-teardown-shopify-river)
- [Shopify's River shows why agent context costs more (Magica)](sources/magica-shopify-river-agent-context-cost.md): no like-for-like comparison against private agents; migration and Aquifer cost undisclosed (competitive-teardown-shopify-river)
- [AI SLOPCAST #9](sources/oleg-guru-ai-slopcast-shopify-river-lehrwerkstatt.md): only positive metrics; review load on seniors unreported (competitive-teardown-shopify-river)
- [Tobi Lutke: River Now Writes Half (Podcast Alpha)](sources/podcastalpha-tobi-lutke-river-half-of-prs.md): "founder-stated, not audited"; headline overstates Tobi's "up to about 50%... created out of conversations" (competitive-teardown-shopify-river)
- [How to Make AI Work Visible (MindStudio)](sources/mindstudio-make-ai-work-visible-shopify-river.md): loose restatement used as a product pitch (competitive-teardown-shopify-river)

## outcome-measurement-gap: Nobody can yet measure PM-agent outcomes
- [Shopify's River shows why agent context costs more (Magica)](sources/magica-shopify-river-agent-context-cost.md): names the missing evidence: resolution time, rollback rate, retention, infrastructure cost against a baseline (competitive-teardown-shopify-river)
- [How River takes security work from a fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): "PR count and green-branch count measure motion, not remediation"; measure items reaching fixed, rejected or escalated (competitive-teardown-shopify-river)

## agent-failure-modes: Recurring agent failure modes in PM work
- [How River takes security work from a fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): told to enumerate fully, River rechecked only the oldest claim; "Prompts are the right place to express judgment and the wrong place to express a guarantee" (competitive-teardown-shopify-river)
- [AI SLOPCAST #9](sources/oleg-guru-ai-slopcast-shopify-river-lehrwerkstatt.md): public-by-default archives everyone's gaps, "a treasure trove" for HR (critique) (competitive-teardown-shopify-river)

## human-review-gates: Human review gates on agent output
- [How River takes security work from a fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): draft-only, human merge authority; hand off "the smallest question that an owner has to answer"; River left a human-owned branch alone (competitive-teardown-shopify-river)
- [Tobi Lütke: AI Agents, Better Decisions (Knowledge Project)](sources/fs-knowledge-project-tobi-lutke-ai-agents.md): "slop grenades", unread agent PRs that shift review load onto colleagues (competitive-teardown-shopify-river)
- [Inside Shopify's AI-first engineering playbook](sources/bvp-inside-shopifys-ai-first-engineering-playbook.md): "We still require a human PR reviewer, which is now becoming a big bottleneck" (competitive-teardown-shopify-river)

## harness-portability: Harness portability
- [Under the River](sources/shopify-engineering-under-the-river.md): harness outside the sandbox lets Shopify "swap models, runtimes, even languages on the harness side" (competitive-teardown-shopify-river)
- [Small Models, Massive Wins (Beyond the Pilot)](sources/venturebeat-beyond-the-pilot-farhan-thawar.md): "River ... switches between models"; "I don't care what harness you wanna use" (competitive-teardown-shopify-river)

## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Under the River](sources/shopify-engineering-under-the-river.md): Aquifer session = append-only Postgres event log; harness and sandbox disposable; idle "session cells" rehydrate on any host; "Cells die, sandboxes die, machines die. The conversation doesn't." (Part III) (competitive-teardown-shopify-river)
- [River floods Shopify chart](sources/x-tobi-river-floods-shopify-chart.md): "wrote in the same thread" links 61,680 (Mar) → 171,853 (Sep 2026), the only published multiplayer metric (self-reported) (competitive-teardown-shopify-river)
- [We gave AI agents a mobile dev environment](sources/shopify-engineering-remote-dev.md): each River session claims a warm Mac plus Android VM, destroyed after use; tasks start from Slack or run overnight; Live Preview links shareable (competitive-teardown-shopify-river)
- [Shopify: Building River (ZenML)](sources/zenml-llmops-shopify-river-durable-infrastructure.md): Postgres event-log session, harness outside the sandbox, idle "session cells" restart anywhere (competitive-teardown-shopify-river)
- [Case Study: Shopify River (Wallfacer)](sources/wallfacer-case-study-shopify-river.md): "the resume mechanism and the audit record are the same artifact" (competitive-teardown-shopify-river)
- [Hacker News: River submissions and comments](sources/hn-shopify-river-discussion.md): practitioners compare River to Managed Agents and say "we built something similar" (competitive-teardown-shopify-river)

## remote-agent-invocation: Remote agent invocation
- [Under the River](sources/shopify-engineering-under-the-river.md): one stack, three modes: interactive (River), automation (PR review, woken by external systems), job (CI/batch, log optional) (competitive-teardown-shopify-river)
- [How River takes security work from a fix to merge](sources/shopify-engineering-river-vulnerability-remediation.md): River opens one Slack thread per finding from a ledger; 4 threads / 35 findings in a minute, each progressing independently (competitive-teardown-shopify-river)
- [Small Models, Massive Wins (Beyond the Pilot)](sources/venturebeat-beyond-the-pilot-farhan-thawar.md): River is pull-only: "you can talk to it, but it doesn't talk to you" (competitive-teardown-shopify-river)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Small Models, Massive Wins (Beyond the Pilot)](sources/venturebeat-beyond-the-pilot-farhan-thawar.md): "River can see Slack messages ... data warehouse ... product management system"; "you can't go into a private channel" (competitive-teardown-shopify-river)
- [Inside Shopify's AI-first engineering playbook](sources/bvp-inside-shopifys-ai-first-engineering-playbook.md): MCP servers go "through the same auth flow that you have", so AI sees only what you can see (assistant tools, not River) (competitive-teardown-shopify-river)
- [River at Shopify (Internal Agents Map)](sources/internal-agents-shopify-river.md): credentials and sandbox marked "Not reported" in public sources (competitive-teardown-shopify-river)
- [Shopify's Aquifer, in the Open (Lobu)](sources/lobu-shopifys-aquifer-in-the-open.md): a proxy swaps placeholder tokens for real ones at egress, so the worker never holds secrets (vendor's own design, contrasted with Aquifer) (competitive-teardown-shopify-river)
- [Create information barriers in Slack](sources/slack-information-barriers-docs.md): barriers block DMs and huddles between IdP groups, but members "will still be able to interact in public and private channels" they share (competitive-teardown-shopify-river)

## artifact-standardization: Artifact standardization
- [Quick: An internal hosting platform for the AI era](sources/shopify-engineering-quick.md): one artifact form (static folder + fixed API: db, files, AI, warehouse, websockets, identity); "All Quick sites are open to all employees", no owners (competitive-teardown-shopify-river)

## agent-as-service-many-surfaces: The agent as a service with many surfaces
- [Under the River](sources/shopify-engineering-under-the-river.md): the counter-case: River has one surface (Slack, no DMs), with companion links (Quick sites, Live Preview) for rich output (competitive-teardown-shopify-river)
- [Tobi Lütke: AI Agents, Better Decisions (Knowledge Project)](sources/fs-knowledge-project-tobi-lutke-ai-agents.md): River can join Google Meet when invited, "although not really utilized" (competitive-teardown-shopify-river)

## public-by-default-agent-work: Public-by-default agent work and its costs
Agent sessions that are visible to the whole organisation by default (no DMs, no private mode), so others learn by watching and the transcripts can be mined; and the costs of that default: questions not asked, sensitive data in open threads, channel membership as access control, regulated walls. Matters for the trust-privacy-defaults and agent-interface choices.
- [Learning on the Shop floor](sources/x-tobi-learning-on-the-shop-floor.md): River "does not respond to direct messages"; "Asking for help feels different when the whole company can see the question" (competitive-teardown-shopify-river)
- [Under the River](sources/shopify-engineering-under-the-river.md): "Every conversation with River becomes a public Slack transcript, open by default to other Shopify employees" (competitive-teardown-shopify-river)
- [River's reaction to the Shop floor post](sources/x-tobi-river-reaction-to-shop-floor-post.md): "Some questions that would have been asked in a DM just don't get asked"; also an "honesty pressure" on agent and user (competitive-teardown-shopify-river)
- [Small Models, Massive Wins (Beyond the Pilot)](sources/venturebeat-beyond-the-pilot-farhan-thawar.md): River refuses private channels too: "you can't go into a private channel and say, 'Hey, River, help me build'" (competitive-teardown-shopify-river)
- [Quick](sources/shopify-engineering-quick.md): the same default for artifacts: all sites open to all employees, no owners (competitive-teardown-shopify-river)
- [Shopify's River shows why agent context costs more (Magica)](sources/magica-shopify-river-agent-context-cost.md): Slack's CPO: a boundary for "genuinely sensitive work"; "psychological safety should determine where openness stops" (competitive-teardown-shopify-river)
- [Shopify Just Showed the Agent Stack](sources/adaptordie-shopify-river-agent-stack.md): "A pricing conversation may need a tighter audience" (competitive-teardown-shopify-river)
- [Hacker News: River submissions and comments](sources/hn-shopify-river-discussion.md): one-line anecdote: the way people speak to agents wouldn't be "kosher in a company slack" (competitive-teardown-shopify-river)
- [The Transparency Paradox (Bernstein)](sources/asq-bernstein-transparency-paradox.md): broad visibility can breed hiding; privacy zones raised output 10–15% (independent; factory setting) (competitive-teardown-shopify-river)
- [Create information barriers in Slack](sources/slack-information-barriers-docs.md): chat-tool walls don't stop interaction in shared channels, so a channel-native agent inherits that gap (competitive-teardown-shopify-river)
- [Tenable on Claude Tag](sources/tenable-claude-tag-slack-access-model.md): in channel agents, public-channel join policy effectively governs access to the agent's credentials; new members see scrollback (competitive-teardown-shopify-river)
