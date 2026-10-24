## ai-flattened-org: AI as the reason to flatten the organisation
Leaders cite AI as the reason to remove management layers, shrink feature teams to squads and replace the information-routing job of managers with agents and a shared "world model". Distinct from leadership-permission-mandate (authority and incentives): this is about the org's shape, which decides who does PM tasks and how many handoffs there are.
- [Jack Dorsey is about to overhaul Block in a reorg](sources/fortune-block-functional-reorg-memo-2024.md): July 2024 move from business units to functions; the memo gave collaboration and craft as reasons, not AI (research-block-product-practices)
- [Block Q2 2024 earnings call](sources/motley-fool-block-q2-2024-earnings-call.md): Dorsey ties the functional org to moving "much, much faster" with AI models (research-block-product-practices)
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): CTO calls the GM-to-functional reorg "the key" to becoming AI-native and worth more than any tool (research-block-product-practices)
- [Read the email Jack Dorsey sent when he cut 931 of Block's staff](sources/techcrunch-dorsey-email-931-cuts-2025.md): 2025 flattening (80 managers cut, 193 moved to IC, depth capped) explicitly "not replacing folks with AI" (research-block-product-practices)
- [we're making @blocks smaller today](sources/x-jack-block-smaller-note-2026-02-26.md): over 10,000 to just under 6,000 people, credited to intelligence tools "paired with smaller and flatter teams" (2026-02-26) (research-block-product-practices)
- [Block Q4 2025 prepared remarks](sources/block-q4-2025-earnings-prepared-remarks.md): the cut announced alongside +24% gross profit; only metric given is code shipped per engineer up 40%+ (research-block-product-practices)
- [Block lays off 4,000](sources/techcrunch-block-layoffs-4000-2026.md): independent account of the February 2026 cut and its AI rationale (research-block-product-practices)
- [From Hierarchy to Intelligence](sources/block-from-hierarchy-to-intelligence.md): a company world model replaces middle management's routing; three roles only (IC, DRI, player-coach) (2026-03-31) (research-block-product-practices)
- [Jack Dorsey: Every Company Can Now Be a Mini-AGI](sources/sequoia-dorsey-every-company-mini-agi.md): five management layers today, target two to three (research-block-product-practices)
- [Block CTO Dhanji Prasanna: Building the AI-First Enterprise with Goose](sources/sequoia-training-data-dhanji-goose.md): funded special projects, then "progressively we started to unwind our GM structure" (research-block-product-practices)
- [What Happens When a Public Company Goes All In on AI](sources/a16z-owen-jennings-block-all-in-on-ai.md): feature teams of ~14 became squads of 1-6; development layers cut 50-60%; meetings down 70-80% (research-block-product-practices)
- [Block leans into its AI future](sources/paymentsdive-block-leans-into-ai-future.md): analysts judge the reorganisation on financials (research-block-product-practices)

## capability-packaging-layers: Choosing the layer a capability lives in
Block deliberately packages capability at four layers (MCP server, skill, recipe, platform service) and moves capabilities between them; the rule it states is that scripts and platforms own what must be consistent, skills and recipes own the procedure. Matters for how a PM agent's capabilities would be packaged, versioned and governed.
- [From Localhost to Launched](sources/block-eng-app-kit-localhost-to-launched.md): the internal app-publishing capability moved from an MCP server (BlockCell) to a distributed skill plus a fixed stack (research-block-product-practices)
- [3 Principles for Designing Agent Skills](sources/block-eng-3-principles-agent-skills.md): "know what the agent should not decide": deterministic scripts inside skills for anything that must reproduce (research-block-product-practices)
- [Recipes, Recipe Reference and Shareable Recipes (goose docs)](sources/goose-docs-recipes.md): recipe = instructions, typed parameters, extensions, model, sub-recipes, response schema and shell-checked retries (research-block-product-practices)
- [Block's Playbook for Designing MCP Servers](sources/block-eng-playbook-designing-mcp-servers.md): MCP servers designed around workflows, not APIs (Linear from 30+ tools to 2) (research-block-product-practices)
- [Block rolls out Builderbot](sources/block-builderbot-rollout.md): the shared coding capability became a platform service on goose, not a per-user recipe (research-block-product-practices)

## single-agent-many-skills: One agent with many skills, not many agents
- [Block Investor Day 2025: Arnaud Weber](sources/block-investor-day-2025-ai-engineering-transcript.md): one "general AI agent" integrated with about 150 services for every function (research-block-product-practices)
- [How Block Got 12,000 Employees Using AI Agents in Two Months](sources/thenewstack-block-12000-employees-ai-agents.md): 100+ pre-approved MCP servers behind one agent (research-block-product-practices)
- [MCP in the Enterprise: Real World Adoption at Block](sources/goose-blog-mcp-in-enterprise-block.md): one agent with a curated default MCP bundle used by design, product, support and risk (research-block-product-practices)
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): goose as a general agent whose value is MCP wrappers; "Goose can write its own MCPs" (research-block-product-practices)
- [Block Open-Sourced Goose: How a YAML Recipe File Scaled](sources/agentreport-goose-recipe-60-percent.md): one binary, a directory of recipes and a directory of MCP servers (aggregator, unsourced figures) (research-block-product-practices)

## one-job-per-agent: One job per agent
- [Recipes, Recipe Reference and Shareable Recipes (goose docs)](sources/goose-docs-recipes.md): recipes package a task agent inside the general one (research-block-product-practices)
- [Subagents (goose docs)](sources/goose-docs-subagents.md): temporary task instances from a prompt or recipe; no recursion or scheduler access (research-block-product-practices)
- [Streamlining Detection Development with Goose Recipes](sources/goose-blog-detection-engineering-panther-recipes.md): a main recipe orchestrates six single-purpose sub-recipes to a draft PR (research-block-product-practices)
- [Configuring Agents in Buzz](sources/block-eng-configuring-agents-in-buzz.md): orchestrator, executors and a cross-family reviewer, each defined by harness, model and instructions (research-block-product-practices)
- [Goose Janitor](sources/goose-blog-goose-janitor-ai-teammate.md): a single-purpose recipe agent that removes stale feature flags (research-block-product-practices)

## skills-marketplace: A versioned skills marketplace with hidden Git
- [3 Principles for Designing Agent Skills](sources/block-eng-3-principles-agent-skills.md): internal marketplace of 100+ skills with role bundles, PR-reviewed in a repo (research-block-product-practices)

## skill-standards: Skill standards
- [From Localhost to Launched](sources/block-eng-app-kit-localhost-to-launched.md): App Kit ships as an employee-distributed SKILL.md skill usable from any harness (research-block-product-practices)

## harness-portability: Harness portability
- [AI-Assisted Development at Block](sources/block-eng-ai-assisted-development-at-block.md): "We buy them all": seven coding harnesses; `ai-rules` generates per-harness configs from one rule set (research-block-product-practices)
- [Buzz!](sources/block-eng-buzz.md): harness-agnostic workspace for people and agents; switch harness without losing identity or history (research-block-product-practices)
- [Why Block handed Goose to the Linux Foundation](sources/thenewstack-why-block-handed-goose-lf.md): Block's trademark ownership and opaque governance were "hampering enterprise adoption" (research-block-product-practices)
- [goose moves to the AAIF](sources/goose-blog-moves-to-aaif.md): repo and docs moved to the foundation on 2026-04-07 (research-block-product-practices)
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): pluggable providers; staff may use "any tools that they want" (research-block-product-practices)

## build-vs-buy: Own the agent harness as a moat
- [Q2 2026 Shareholder Letter](sources/block-q2-2026-shareholder-letter.md): "the models are interchangeable"; the harness, data and distribution are Block's (research-block-product-practices)
- [Block rolls out Builderbot](sources/block-builderbot-rollout.md): built a goose-based orchestration layer because no bought tool spanned the whole codebase (research-block-product-practices)

## enterprise-admin-controls: Enterprise admin controls across harnesses
- [goose Extension Allowlist (docs)](sources/goose-docs-extension-allowlist.md): an env-var URL to a YAML list of allowed install commands, enforced on the client (research-block-product-practices)
- [Chain of Thought: Angie Jones on Block's goose rollout](sources/chainofthought-angie-jones-block-goose-rollout.md): even internal MCP servers need security review before joining the allowlist (research-block-product-practices)
- [GenAI Security Principles](sources/block-eng-genai-security-principles.md): the AI-integration review drew several hundred requests; design-phase checklist (research-block-product-practices)

## skill-supply-chain-security: Skill supply chain security
- [How We Red-Teamed Our Own AI Agent](sources/block-eng-red-teamed-own-ai-agent.md): a poisoned shareable recipe was the winning vector; recipe instructions are now shown on load (research-block-product-practices)

## agent-protocol-security: Security of agent-to-agent and agent-to-tool protocols
- [How We Red-Teamed Our Own AI Agent](sources/block-eng-red-teamed-own-ai-agent.md): zero-width-Unicode prompt injection delivered in a calendar invite through the Calendar MCP (research-block-product-practices)
- [Agent Guardrails and Controls](sources/block-eng-agent-guardrails-and-controls.md): a CORS-style gate on chained tool calls, decided in code, not by the model (research-block-product-practices)
- [Securing the Model Context Protocol](sources/block-eng-securing-the-model-context-protocol.md): MCP threat model; allowlists of pre-validated servers (research-block-product-practices)

## policy-enforcement-fail-open: Agent policy layers that fail open
- [Adversary Mode (goose docs)](sources/goose-docs-adversary-mode.md): the reviewer agent allows the call if it errors, and is off by default (research-block-product-practices)
- [goose Extension Allowlist (docs)](sources/goose-docs-extension-allowlist.md): no env var means no restriction (research-block-product-practices)

## evals-autonomy-trust: Evals, autonomy sliders and earned trust
- [goose Permission Modes (docs)](sources/goose-docs-permission-modes.md): Autonomous by default; Smart Approve relies on the model to classify write tools (research-block-product-practices)
- [Building the Data Foundation for Automated Analytics](sources/block-eng-data-foundation-automated-analytics.md): eval tests iterated to 100% on priority questions before rollout (research-block-product-practices)
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): median session about five minutes; overnight wishlists succeed on about 60% of well-described features (research-block-product-practices)

## human-review-gates: Human review gates on agent output
- [Block rolls out Builderbot](sources/block-builderbot-rollout.md): ticket to merged PR for ~15% of production changes; humans steer and decide (vendor claim) (research-block-product-practices)
- [How We Use goose to Maintain goose](sources/goose-blog-goose-maintains-goose.md): a `/goose` comment yields a draft PR; a maintainer approves every merge (research-block-product-practices)
- [Q1 2026 Shareholder Letter](sources/block-q1-2026-shareholder-letter.md): Builderbot reviewed 90%+ of change requests; a human makes the final push decision (research-block-product-practices)
- [Block (XYZ) Q2 2026 Earnings Call Transcript](sources/fool-block-q2-2026-earnings-call.md): AI in "basically every single production code change or production code review" (research-block-product-practices)
- [Current and former Block workers say AI can't do their jobs](sources/guardian-block-workers-ai-cant-do-their-jobs.md): staff say every change needs human approval and ~95% of AI changes needed edits (late 2025) (research-block-product-practices)

## metrics-review-agents: Metrics review and analytics agents
- [Building the Data Foundation for Automated Analytics](sources/block-eng-data-foundation-automated-analytics.md): governed-metrics MCP (1,100+ metrics) plus Query Expert; 2.1K monthly users, over a third of the company (research-block-product-practices)
- [Growth Manager, Activation & Habituation (Cash App)](sources/block-careers-growth-manager-activation.md): "diagnose your own funnel ... without waiting on an analyst" with AI-assisted SQL (research-block-product-practices)

## non-engineer-builders: Non-engineers ship through agents
- [From Localhost to Launched](sources/block-eng-app-kit-localhost-to-launched.md): ~80% of App Kit users outside engineering; 1,000+ internal apps in a quarter (research-block-product-practices)
- [Block Investor Day 2025: Arnaud Weber](sources/block-investor-day-2025-ai-engineering-transcript.md): g2 tiles let non-technical staff build persistent autonomous workflows (vendor claim) (research-block-product-practices)
- [Cameron Worboys: Inside an AI-native design org](sources/dive-club-cam-worboys-ai-native-design-org.md): over 90% of Cash App designers ship production PRs after a sandbox-to-production programme (research-block-product-practices)
- [Staff Product Manager, Post-Checkout Experience](sources/block-careers-staff-pm-post-checkout.md): the one open Square PM role requires AI prototypes and PRs via GitHub (research-block-product-practices)
- [Staff Product Designer, Access & Identities (Cash App)](sources/builtin-cash-app-staff-product-designer-access.md): designers expected to vibe-code interfaces with Cursor, V0 and Figma Make (research-block-product-practices)
- [Square APM Program](sources/block-square-apm-program.md): APM applicants submit "something you built using AI tools" (research-block-product-practices)
- [Block Builder Fellowship](sources/block-builder-fellowship.md): a pilot hiring ten builders selected on proof of building (research-block-product-practices)
- [Block CTO Dhanji Prasanna (Sequoia Training Data)](sources/sequoia-training-data-dhanji-goose.md): sales and finance staff write their own dashboards (research-block-product-practices)
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): enterprise risk built its own self-service system, "weeks of work into hours" (research-block-product-practices)

## pm-persona-role-expansion: PM and adjacent personas are expanding or blurring
- [What Happens When a Public Company Goes All In on AI](sources/a16z-owen-jennings-block-all-in-on-ai.md): "All of our product managers are shipping PRs"; fewer PMs per roadmap, more overall (research-block-product-practices)
- [Jack Dorsey: Every Company Can Now Be a Mini-AGI](sources/sequoia-dorsey-every-company-mini-agi.md): "product person" folded into the IC builder role; DRIs own strategy and roadmap (research-block-product-practices)
- [From Hierarchy to Intelligence](sources/block-from-hierarchy-to-intelligence.md): no PM among the three roles; "No product manager decided to build either solution" (research-block-product-practices)
- [Growth Manager, Activation & Habituation (Cash App)](sources/block-careers-growth-manager-activation.md): a growth role that "blurs growth and product", owns roadmap and experiments, uses Claude Code or Goose (research-block-product-practices)
- [Cameron Worboys: Inside an AI-native design org](sources/dive-club-cam-worboys-ai-native-design-org.md): "even product managers are coding stuff"; roles blur to who can ship (research-block-product-practices)
- [Square Global Head of Product (Product School)](sources/productschool-willem-ave-square-org-design-ai-agents.md): the DRI must "synthesize product technology and business" across the whole arc (research-block-product-practices)

## agent-led-intent-shaping: Agents shape intent, not only execute it
- [From Hierarchy to Intelligence](sources/block-from-hierarchy-to-intelligence.md): when the intelligence layer cannot compose a solution, "that failure signal is the future roadmap" (research-block-product-practices)
- [Jack Dorsey: Every Company Can Now Be a Mini-AGI](sources/sequoia-dorsey-every-company-mini-agi.md): customers' queries "make the majority of the decisions" (research-block-product-practices)
- [we're making @blocks smaller today](sources/x-jack-block-smaller-note-2026-02-26.md): customers will "build their own features directly, composed of our capabilities" (research-block-product-practices)

## spec-becomes-prototype-and-evals: The spec is replaced by prototype plus evals
- [Jack Dorsey: Every Company Can Now Be a Mini-AGI](sources/sequoia-dorsey-every-company-mini-agi.md): meetings moved from decks and Google Docs to prototypes "that they built" within about two months (research-block-product-practices)
- [Cameron Worboys: Inside an AI-native design org](sources/dive-club-cam-worboys-ai-native-design-org.md): prototypes set direction faster than documents; Friday demos; design crits deleted (research-block-product-practices)
- [Chain of Thought: Angie Jones on Block's goose rollout](sources/chainofthought-angie-jones-block-goose-rollout.md): prototypes win buy-in faster than documents (research-block-product-practices)

## leadership-permission-mandate: Leadership permission and mandates drive AI-native ways of working
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): CTO's "AI manifesto" to do AI "centrally"; Dorsey and the execs use goose "every single day" (research-block-product-practices)
- [Block CTO Dhanji Prasanna (Sequoia Training Data)](sources/sequoia-training-data-dhanji-goose.md): single weekly metric, "manual hours saved by goose", with a 25% target (research-block-product-practices)
- [Q1 2026 Shareholder Letter](sources/block-q1-2026-shareholder-letter.md): "100% of Block employees are using AI tools" (research-block-product-practices)
- [What Happens When a Public Company Goes All In on AI](sources/a16z-owen-jennings-block-all-in-on-ai.md): "unlimited access to tokens"; the cut as "a massive forcing function" (research-block-product-practices)
- [Inside Block's major lay-off](sources/hrd-block-staff-dispute-ai-layoffs.md): AI use became expected and tracked in performance discussions (research-block-product-practices)
- [Current and former Block workers say AI can't do their jobs](sources/guardian-block-workers-ai-cant-do-their-jobs.md): encouragement became a requirement; tool- and token-level monitoring; reviews ask about AI proficiency (research-block-product-practices)

## enablement-by-product: The product is the enablement
- [How Block Got 12,000 Employees Using AI Agents in Two Months](sources/thenewstack-block-12000-employees-ai-agents.md): auto-install through the software centre, pre-configured servers and models; the inspiration Slack channel was the top adoption driver (research-block-product-practices)
- [AI-Assisted Development at Block](sources/block-eng-ai-assisted-development-at-block.md): about 50 AI Champions at 30% time; Repo Quest (research-block-product-practices)

## legible-org-for-agents: Make the organisation legible to agents
- [From Hierarchy to Intelligence](sources/block-from-hierarchy-to-intelligence.md): remote-first work artifacts are the raw material for a company world model (research-block-product-practices)
- [Q1 2026 Shareholder Letter](sources/block-q1-2026-shareholder-letter.md): decisions, code and designs are "recorded and machine readable" (research-block-product-practices)
- [What Happens When a Public Company Goes All In on AI](sources/a16z-owen-jennings-block-all-in-on-ai.md): the company as "a markdown file" of values, metrics and non-goals that agents iterate against (research-block-product-practices)
- [Square Global Head of Product (Product School)](sources/productschool-willem-ave-square-org-design-ai-agents.md): knowledge once held by the org chart "encoded in data that agents have access to" (research-block-product-practices)

## opportunity-to-code-chain: Opportunity → problem → goal → intent → plan → code
- [Block rolls out Builderbot](sources/block-builderbot-rollout.md): a seller-request backlog shipped "in days"; the ticket or Slack thread is the handoff (research-block-product-practices)
- [Moving to issues as the new PRs](sources/goose-blog-issues-are-the-new-prs.md): issue lifecycle Inbox → design → Ready → agent → human verification (research-block-product-practices)

## agent-ready-intent: A shared standard for agent-ready specs
- [Moving to issues as the new PRs](sources/goose-blog-issues-are-the-new-prs.md): only "Ready" issues with agreed design, constraints and verification go to agents (research-block-product-practices)

## agent-factory-sdlc: Agents across the whole product development loop
- [Block rolls out Builderbot](sources/block-builderbot-rollout.md): Slack tag or Linear/Jira ticket to branch, PR, CI and iteration; ~1,500 merged PRs a week (vendor claim) (research-block-product-practices)
- [What Happens When a Public Company Goes All In on AI](sources/a16z-owen-jennings-block-all-in-on-ai.md): PMs and growth marketers run many agents in parallel; Builderbot gets features to 85-90% (research-block-product-practices)
- [Actionable CI](sources/block-eng-actionable-ci.md): headless goose turns CI failures into draft-PR fixes (research-block-product-practices)

## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Block rolls out Builderbot](sources/block-builderbot-rollout.md): teammates steer @builderbot in the same Slack thread (research-block-product-practices)
- [Buzz!](sources/block-eng-buzz.md): channels shared by people and agents, with agent memory (research-block-product-practices)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Buzz!](sources/block-eng-buzz.md): per-agent keypairs with owner-signed, scoped authorisation (research-block-product-practices)
- [Block's Playbook for Designing MCP Servers](sources/block-eng-playbook-designing-mcp-servers.md): OAuth on first use through SSO, minimum scopes, tokens in the OS keychain (research-block-product-practices)

## pm-tool-connectivity: Reaching PM tools from agents
- [Block's Playbook for Designing MCP Servers](sources/block-eng-playbook-designing-mcp-servers.md): Linear MCP cut from 30+ tools to 2; Calendar exposed as SQL (research-block-product-practices)
- [Scaling MCP at Block (MCP Dev Summit summary)](sources/glama-scaling-mcp-at-block.md): named internal servers include Jira, Asana, Glean, Databricks, PagerDuty (secondary) (research-block-product-practices)

## risk-review-as-classification: Risk review as a specification and classification problem
- [GenAI Security Principles](sources/block-eng-genai-security-principles.md): AI requirements tiered by data-sensitivity level DSL-1 to DSL-4 (research-block-product-practices)

## human-judgment-pm-jobs: PM jobs that stay human-led
- [Jack Dorsey: Every Company Can Now Be a Mini-AGI](sources/sequoia-dorsey-every-company-mini-agi.md): tools build about 80%; taste and judgment are the last 20% (research-block-product-practices)
- [Q2 2026 Shareholder Letter](sources/block-q2-2026-shareholder-letter.md): "Judgment, trust, depth of understanding, and capability will become scarce" (research-block-product-practices)
- [Staff Product Manager, Post-Checkout Experience](sources/block-careers-staff-pm-post-checkout.md): the PM judges "AI-generated work against real customer scenarios" (research-block-product-practices)
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): AI lacks "portfolio judgment": whether the tool or process is needed at all (research-block-product-practices)
- [Current and former Block workers say AI can't do their jobs](sources/guardian-block-workers-ai-cant-do-their-jobs.md): a laid-off product-department employee says vision and strategy were what the tools could not do (research-block-product-practices)

## outcome-measurement-gap: Nobody can yet measure PM-agent outcomes
- [How Block is becoming the most AI-native enterprise (Lenny's Podcast)](sources/lenny-podcast-block-dhanji-goose.md): 8-10 h/week self-reported; 20-25% of manual hours saved from an unpublished formula (research-block-product-practices)
- [Block Q4 2025 prepared remarks](sources/block-q4-2025-earnings-prepared-remarks.md): the only metric for the cut is code shipped per engineer, up 40%+ (research-block-product-practices)
- [Q1 2026 Shareholder Letter](sources/block-q1-2026-shareholder-letter.md): throughput up 2.5x and post-change incidents down 70%+, credited jointly to AI and reliability work (research-block-product-practices)
- [Block (XYZ) Q2 2026 Earnings Call Transcript](sources/fool-block-q2-2026-earnings-call.md): the only product-level measure is features shipped (130 in H1 2026, 3x+), undefined (research-block-product-practices)

## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is thin
- [Current and former Block workers say AI can't do their jobs](sources/guardian-block-workers-ai-cant-do-their-jobs.md): seven staff dispute that a much smaller team can do more; a data scientist saw "very limited gains" (research-block-product-practices)
- [Inside Block's major lay-off](sources/hrd-block-staff-dispute-ai-layoffs.md): relays staff estimates that ~95% of AI code still needs human changes (research-block-product-practices)
- [Block rehires some staff initially fired](sources/cointelegraph-block-rehires-laid-off-staff.md): some people rehired within weeks of the AI-sized cut (research-block-product-practices)
- [Block Open-Sourced Goose: How a YAML Recipe File Scaled](sources/agentreport-goose-recipe-60-percent.md): the widely repeated "60% weekly" figure carries no citation (research-block-product-practices)

## prd-agents: PRD and spec writing/review as an agent job
- [Recipes, Recipe Reference and Shareable Recipes (goose docs)](sources/goose-docs-recipes.md): 46 cookbook recipes, none for PRDs, research or feedback synthesis (an absence) (research-block-product-practices)

## status-update-agents: Status updates and 'ask the org' Q&A as an agent job
- [Recipes, Recipe Reference and Shareable Recipes (goose docs)](sources/goose-docs-recipes.md): a community daily-standup recipe turns GitHub PRs and issues into dated standup files (research-block-product-practices)

## compounding-context-repo: Context that compounds with each shipped feature
- [What Happens When a Public Company Goes All In on AI](sources/a16z-owen-jennings-block-all-in-on-ai.md): the company "markdown file" iterated by agents (research-block-product-practices)

## memory-architecture: Memory as inspectable files from an offline pipeline
- [Configuring Agents in Buzz](sources/block-eng-configuring-agents-in-buzz.md): agents keep core and cold memory inside the workspace (research-block-product-practices)

## agent-as-service-many-surfaces: The agent as a service with many surfaces
- [AI at Block](sources/block-ai-at-block-page.md): Block's own map of its AI estate: customer agents (Managerbot, Moneybot) and builder tools (Buzz, Berd, Builderbot) (research-block-product-practices)
- [MCP Apps in goose](sources/goose-blog-mcp-apps.md): MCP servers can return interactive HTML UIs rendered inside the chat (experimental, v1.19.0) (research-block-product-practices)

## prototyping-agents-limits: Prototyping agents and their limits
- [How to Vibe Code Responsibly (with goose)](sources/goose-blog-vibe-code-responsibly.md): the only goose post naming PMs: agentic coding lets designers and PMs "prototype full-stack applications"; the rest is guardrails (research-block-product-practices)
