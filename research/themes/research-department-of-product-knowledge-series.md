# Theme evidence: research-department-of-product-knowledge-series

Written only by the task `research-department-of-product-knowledge-series`. Built into ../THEMES.md by ../build.py.

## agent-as-service-many-surfaces: The agent as a service with many surfaces
- [How to develop a Headless Product Strategy](sources/departmentofproduct-headless-product-strategy.md): "capabilities, data and logic as the product, the UI as one of many consumption paths" (Salesforce headless split) (research-department-of-product-knowledge-series)
- [How to develop an MCP Product Strategy](sources/departmentofproduct-mcp-product-strategy.md): Intercom made Fin an MCP client that reaches other tools, rather than become a server hidden behind Claude. Stripe is content to be invisible behind agents (research-department-of-product-knowledge-series)

## agent-control-plane: Agent control planes above vendors
- [How to Manage AI Agents Effectively](sources/departmentofproduct-managing-ai-agents.md): DoorDash's Agent Gateway is one checkpoint before any tool call (auth, rate limit, credential hand-off, agent-to-tool allowlist); Vanta open-sourced Agentic Trust Controls, split into build-time and run-time controls. (research-department-of-product-knowledge-series)

## agent-failure-modes: Recurring agent failure modes in PM work
- [DESIGN.md Explained](sources/departmentofproduct-design-md-explained.md): agents fill a missing token with something plausible, and the divergence spreads while still looking consistent. (research-department-of-product-knowledge-series)
- [Agentic Workflows Explained](sources/departmentofproduct-agentic-workflows-explained.md): a cited benchmark classes failures as planning, execution and formatting errors. (research-department-of-product-knowledge-series)
- [What is parallel AI agent coding? An in-depth guide for product teams](sources/departmentofproduct-parallel-agent-coding.md): parallel agents bring merge conflicts and harder debugging; they're weak on architecture and on UI that needs visual feedback (research-department-of-product-knowledge-series)

## agent-frameworks: Agent frameworks
- [Multi Agent Architecture explained](sources/departmentofproduct-multi-agent-architecture.md): network, supervisor, hierarchical and custom patterns on AutoGen, LangGraph, A2A and Bedrock's supervisor toggle (research-department-of-product-knowledge-series)
- [How to build an AI Agent](sources/departmentofproduct-how-to-build-an-ai-agent.md): LangChain and AutoGen (Magentic-One roles) recommended in Jan 2025; AutoGen was later archived (research-department-of-product-knowledge-series)
- [AI Agent SDKs Explained](sources/departmentofproduct-agent-sdks-explained.md): sets model-vendor frameworks (OpenAI Agents SDK, ADK, both model-agnostic) against domain toolkits from SaaS firms (Stripe, 1Password) (research-department-of-product-knowledge-series)

## agent-led-intent-shaping: Agents shape intent, not only execute it
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): Ideate researches named apps, proposes three directions, asks the PM to pick, then drafts a PRD for approval before designing (research-department-of-product-knowledge-series)

## agent-project-failure-rates: Agent project failure rates
- [Agentic Workflows Explained](sources/departmentofproduct-agentic-workflows-explained.md): agents failed about 50% of 34 general tasks in a cited study (the post calls it "Cibench"; not verified). (research-department-of-product-knowledge-series)

## agent-protocol-security: Security of agent-to-agent and agent-to-tool protocols
- [How to develop an MCP Product Strategy](sources/departmentofproduct-mcp-product-strategy.md): cites the Asana and GitHub MCP incidents. Broad read/write scopes are hard to avoid, and servers should reject tokens with too much or irrelevant scope (research-department-of-product-knowledge-series)

## agent-ready-intent: A shared standard for agent-ready specs
- [How to speed up engineering velocity with AI: a non-engineer's guide](sources/departmentofproduct-engineering-velocity-non-engineers.md): Morgan Stanley's tool writes English specs of legacy code, which engineers then rewrite from (280k hours claimed, via WSJ) (research-department-of-product-knowledge-series)

## ai-synthesis-hallucination-risk: AI synthesis can invent or merge facts
- [How to use Perplexity's new Computer...](sources/departmentofproduct-perplexity-computer.md): the competitor-monitor prompt has to forbid invented pricing and require a URL for every data point (research-department-of-product-knowledge-series)
- [How to build a Persona Feature Tester with Claude Code and ElevenLabs](sources/departmentofproduct-persona-feature-tester.md): the personas' specific quotes and behaviours trace back to model-written "research" files (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): cites Deloitte's partial refund to the Australian government over fabricated sources as a deep-research warning (research-department-of-product-knowledge-series)

## artifact-standardization: Artifact standardization
- [How to build the ultimate Product Dashboard that generates stakeholder updates on demand](sources/departmentofproduct-product-dashboard-stakeholder-updates.md): the "decision queue" is a fixed record (the call, kind, who it waits on, age, context) that Claude pulls out of the inbox; "a forcing function", not a to-do list (research-department-of-product-knowledge-series)
- [What are Claude Skills and how can you use them for product-related work?](sources/departmentofproduct-claude-skills-for-product-work.md): a brand-guidelines skill plus the pptx skill give house-style decks; the xlsx skill enforces zero formula errors (research-department-of-product-knowledge-series)
- [DESIGN.md Explained](sources/departmentofproduct-design-md-explained.md): Google open-sourced DESIGN.md: YAML tokens ("what") plus markdown rationale ("why") in one file, with a CLI linter that includes a WCAG 4.5:1 contrast check. (research-department-of-product-knowledge-series)

## build-vs-buy: Own the agent harness as a moat
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): Square's head of product calls context management and progressive tool disclosure "at the harness layer" Managerbot's secret sauce; harness as "agentic moat" (second-hand via VentureBeat) (research-department-of-product-knowledge-series)
- [How to build an AI Agent](sources/departmentofproduct-how-to-build-an-ai-agent.md): early three-way choice (framework / from scratch / no-code), from before "extend a vendor harness" was an option (research-department-of-product-knowledge-series)

## compounding-context-repo: Context that compounds with each shipped feature
- [How to use Claude Code for non-engineering use cases](sources/departmentofproduct-claude-code-non-engineers.md): a PM's shared "Claude Code Product OS" repo of frameworks, strategy templates and stakeholder profiles (research-department-of-product-knowledge-series)
- [How to speed up engineering velocity with AI: a non-engineer's guide](sources/departmentofproduct-engineering-velocity-non-engineers.md): CLAUDE.md records code style, tests, repo etiquette and setup for new hires and the agent alike (research-department-of-product-knowledge-series)

## cost-control-routing: Cost metering and model routing built into the harness
- [Decision Models Explained - The New AI Building Block for Product Teams](sources/departmentofproduct-decision-models.md): routing steps (which tool, model or team) are usually a small LLM call returning one word; a typed-answer decision model does them faster and cheaper (Higgsfield auto-routing, Harvey Vault, both second-hand) (research-department-of-product-knowledge-series)
- [How to use Perplexity's new Computer...](sources/departmentofproduct-perplexity-computer.md): each subtask is routed to a different vendor's model; credit-metered use means always-on workers need watching (research-department-of-product-knowledge-series)
- [How to develop a Headless Product Strategy](sources/departmentofproduct-headless-product-strategy.md): Rippling claims a single code-mode MCP tool is 98% cheaper than chained tool calls (vendor claim) (research-department-of-product-knowledge-series)
- [How to Manage AI Agents Effectively](sources/departmentofproduct-managing-ai-agents.md): three spend tactics (gateway budgets at Databricks and Vercel; routing by task difficulty, where Block's Buzz benchmark found the priciest model cost about 5.5x for about 9 points more quality; dedicated spend products from Ramp and Rippling, with Rippling's set against PR volume and rework). All second-hand. (research-department-of-product-knowledge-series)
- [How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer](sources/departmentofproduct-loops-goals-slash-commands.md): /compact pitched to PMs as a token-cost saver, with a steerable focus (research-department-of-product-knowledge-series)

## enablement-by-product: The product is the enablement
- [How to Build Powerful Internal AI Productivity Tools](sources/departmentofproduct-internal-ai-tools-ramp-glass.md): auto-connect at sign-on; "configuration already happened at the identity layer" (research-department-of-product-knowledge-series)
- [How to speed up engineering velocity with AI: a non-engineer's guide](sources/departmentofproduct-engineering-velocity-non-engineers.md): Brex gives engineers a monthly tool budget and adopts company-wide whatever spreads (second-hand) (research-department-of-product-knowledge-series)

## enterprise-admin-controls: Enterprise admin controls across harnesses
- [How to Manage AI Agents Effectively](sources/departmentofproduct-managing-ai-agents.md): Notion admin controls over who may create agents and what they reach; OpenTelemetry export from Claude Cowork into existing observability stacks. (research-department-of-product-knowledge-series)

## evals-autonomy-trust: Evals, autonomy sliders and earned trust
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): Amplitude's judge feeds a classifier that predicts human thumbs-up; the tutorial starts with only small code fixes autonomous and raises the threshold "as you build trust" (research-department-of-product-knowledge-series)
- [How to develop a Headless Product Strategy](sources/departmentofproduct-headless-product-strategy.md): Rippling's 50+ golden cases judged on functions, path, execution and final answer before its MCP launch (research-department-of-product-knowledge-series)
- [How to Manage AI Agents Effectively](sources/departmentofproduct-managing-ai-agents.md): DoorDash went from about 1 human review a day to 2,000 LLM-judge-graded sessions daily (claimed +8 quality points, regression testing cut from 6h to 20m); Airbnb calibrates its judges to 80-90% agreement with humans. (research-department-of-product-knowledge-series)
- [How to Identify Opportunities for AI Automation](sources/departmentofproduct-ai-automation-opportunities.md): verifiability is the lead criterion for automation, credited to an unnamed OpenAI co-founder (likely Karpathy). (research-department-of-product-knowledge-series)
- [How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer](sources/departmentofproduct-loops-goals-slash-commands.md): a good goal states the end state, how it's verified and what must be kept; the agent marks "cause unclear" rather than inferring (research-department-of-product-knowledge-series)
- [How to build an AI Agent](sources/departmentofproduct-how-to-build-an-ai-agent.md): three autonomy levels: supervised predefined tasks, conditional autonomy with escalation, full independence (research-department-of-product-knowledge-series)
- [How to test a new AI Model](sources/departmentofproduct-model-sense-testing.md): a PM-kept "Model Sense Notebook" holding a prompt library, a claims-vs-reality changelog and a domain eval suite rerun at each model release (research-department-of-product-knowledge-series)
- [AI Agent SDKs Explained](sources/departmentofproduct-agent-sdks-explained.md): relays Stripe's doc advice to run agents in a sandbox with evals before real money moves (research-department-of-product-knowledge-series)

## feedback-triage-agents: Feedback and research triage/synthesis as an agent job
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): support tickets grouped by theme and kept only if two or more independent sources corroborate them (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): weekly routine reads Slack, Intercom and app-store reviews, groups patterns across sources, checks each against open tickets and flags untracked ones (research-department-of-product-knowledge-series)

## harness-over-model: The harness, not the model, limits real-world value
- [Context Engineering for AI Agents Explained - a simple overview of the basics](sources/departmentofproduct-context-engineering-basics.md): agent failures "aren't necessarily model failures, but context failures" (research-department-of-product-knowledge-series)
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): restates Anthropic's solo $9/20 min broken build vs harness $200/6 h working build; "the right harness for last year's model may be over-engineered for this year's" (research-department-of-product-knowledge-series)
- [What is parallel AI agent coding? An in-depth guide for product teams](sources/departmentofproduct-parallel-agent-coding.md): parallel agents pay off only after investment in CI, docs and staging environments (research-department-of-product-knowledge-series)
- [How to test a new AI Model](sources/departmentofproduct-model-sense-testing.md): defines "scaffolding" (retrieval, human-in-the-loop escalation, domain checks) as what makes a model reliable in production. It credits Box's Levie, second-hand (research-department-of-product-knowledge-series)

## harness-portability: Harness portability
- [Claude Design is here](sources/departmentofproduct-claude-design.md): "handoff to Claude Code" gives one command that pulls the design into a local copy, so work moves between surfaces (research-department-of-product-knowledge-series)

## human-judgment-pm-jobs: PM jobs that stay human-led
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): "AI led vs AI informed": human judgement keeps the final say (research-department-of-product-knowledge-series)
- [How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer](sources/departmentofproduct-loops-goals-slash-commands.md): /goal is ruled out for strategic decisions and for security-sensitive or costly-to-get-wrong work (research-department-of-product-knowledge-series)
- [How to build a Strategy Thought Partner](sources/departmentofproduct-strategy-thought-partner.md): framed as "cognitive expansion, not offloading": AI used "to think more clearly, not asking it to think for you" (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): presents discovery ("what to build and why") as the skill that keeps its value as AI eats delivery (research-department-of-product-knowledge-series)

## human-review-gates: Human review gates on agent output
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): Managerbot proposes every action (shift change, campaign, reorder) and the seller must approve it; approval is built into the loop, not bolted on, linked to Block's regulatory history (research-department-of-product-knowledge-series)
- [How to Manage AI Agents Effectively](sources/departmentofproduct-managing-ai-agents.md): Intercom made agent knowledge-base readiness a mandatory launch sign-off; Vercel returns coding-agent work as Git patches that need human approval; the AARM proposal intercepts actions before they run. (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): release notes drafted to Notion and linked in Slack for human review; the PM can open and steer a running routine (research-department-of-product-knowledge-series)
- [What is parallel AI agent coding? An in-depth guide for product teams](sources/departmentofproduct-parallel-agent-coding.md): each parallel agent's work lands as its own branch; a human compares the models' solutions and merges (research-department-of-product-knowledge-series)
- [How to use Claude Cowork as a Competitive Intelligence System](sources/departmentofproduct-cowork-competitive-intelligence.md): the author advises double-checking output before sharing. Browser automation was "a bit hit and miss" (research-department-of-product-knowledge-series)

## identity-delegation: Identity and delegation (on-behalf-of)
- [How to develop a Headless Product Strategy](sources/departmentofproduct-headless-product-strategy.md): WorkOS Agent Auth caps delegated sessions at user permissions ∩ agent ceiling, with step-up auth on sensitive calls (research-department-of-product-knowledge-series)
- [How to Manage AI Agents Effectively](sources/departmentofproduct-managing-ai-agents.md): Uber gives each agent its own cryptographic identity because "who authorised what" was lost across agent hops; Block's User Identity Delegation carries the human and the agent as two identities through every call. Second-hand. (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): attached connectors are used, writes included, with no per-action approval, so the connector list is the run's permission boundary (research-department-of-product-knowledge-series)
- [AI Agent SDKs Explained](sources/departmentofproduct-agent-sdks-explained.md): 1Password lets agents fetch and rotate vault secrets. Stripe uses restricted keys and single-use virtual cards with spend limits (research-department-of-product-knowledge-series)

## legible-org-for-agents: Make the organisation legible to agents
- [What is a Command Line Interface and why do they suddenly matter to product teams?](sources/departmentofproduct-cli-for-product-teams.md): an API leaves conventions to the caller, while a CLI exposes the vendor's recommended patterns as commands; "a distribution channel for the agent economy" (Stripe Projects, Save to Spotify, Ramp CLI) (research-department-of-product-knowledge-series)
- [Why Semantic Data Layers matter](sources/departmentofproduct-semantic-data-layers.md): the semantic layer turns company vocabulary (activation, new user, PII) into versioned, owned definitions that agents and BI tools query alike. (research-department-of-product-knowledge-series)

## memory-architecture: Memory as inspectable files from an offline pipeline
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): a reflection agent rewrites one markdown memory file per product area each cycle (worked, didn't, what the team keeps rejecting) (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): the competitor tracker keeps state between runs as a snapshot file in the repo and diffs against it each run (research-department-of-product-knowledge-series)
- [How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer](sources/departmentofproduct-loops-goals-slash-commands.md): /init writes CLAUDE.md/AGENTS.md as a standing project briefing read at the start of every session (research-department-of-product-knowledge-series)

## meta-harness: Meta harness
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): presents the Stanford Meta-Harness optimiser to PMs as "self-improving harnesses" (the optimiser sense of the term); calls it not production-ready (research-department-of-product-knowledge-series)
- [What is parallel AI agent coding? An in-depth guide for product teams](sources/departmentofproduct-parallel-agent-coding.md): GitHub Agent HQ as a multi-vendor agent command centre; Osmani warns that normalising agents tends to the lowest common denominator (research-department-of-product-knowledge-series)

## metrics-review-agents: Metrics review and analytics agents
- [How to use Claude Projects and Skills to Monitor your Product's Health](sources/departmentofproduct-claude-projects-product-health.md): five health dimensions, traffic-light scoring, then quick-check, deep-dive and exec-summary outputs on a recurring cadence (research-department-of-product-knowledge-series)
- [How to build the ultimate Product Dashboard that generates stakeholder updates on demand](sources/departmentofproduct-product-dashboard-stakeholder-updates.md): a vibe-coded health panel (users, UX, commercial, DORA plus AI-coding adoption); only GA4 and Linear are live, the rest is dummy data (research-department-of-product-knowledge-series)
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): a "sense" agent checks a product-area file's metrics against targets in analytics and returns cited candidate problems (research-department-of-product-knowledge-series)
- [Why Semantic Data Layers matter](sources/departmentofproduct-semantic-data-layers.md): Anthropic's data team reportedly automates about 95% of data requests; eval accuracy rose from about 21% to over 95% after adding a semantic layer and two skills. Second-hand. (research-department-of-product-knowledge-series)
- [How to use Cursor for Non-Engineering use cases](sources/departmentofproduct-cursor-for-non-engineers.md): a PM-built pipeline (Amplitude, Linear and Notion plugins, a context file of healthy ranges, a slash command) that flags anomalies, opens tickets and logs findings. (research-department-of-product-knowledge-series)

## non-engineer-builders: Non-engineers ship through agents
- [How to build the ultimate Product Dashboard that generates stakeholder updates on demand](sources/departmentofproduct-product-dashboard-stakeholder-updates.md): dashboards are now "akin to building spreadsheets"; Rippling's CEO built a Claude-spend dashboard (second-hand) (research-department-of-product-knowledge-series)
- [How to use Claude Code for non-engineering use cases](sources/departmentofproduct-claude-code-non-engineers.md): zero-experience PM setup with an IDE as the file UI; SEO audits, file edits, second brain (research-department-of-product-knowledge-series)
- [How to use AI agents at work](sources/departmentofproduct-ai-agents-at-work.md): the 2025 no-code route (Gumloop, Zapier Agents, Copilot Studio) for PM chores such as competitor tech-stack reports. (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): routines are set up through a form, but remote runs need a code repo, so the PM tutorial starts by creating one on GitHub (research-department-of-product-knowledge-series)
- [How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer](sources/departmentofproduct-loops-goals-slash-commands.md): /insights shows tasks repeated 10-15 times with the same shape as candidates for custom commands (research-department-of-product-knowledge-series)
- [How to build a Persona Feature Tester with Claude Code and ElevenLabs](sources/departmentofproduct-persona-feature-tester.md): a PM chains Projects, Cowork, Claude Design, Claude Code, Cursor, Linear and ElevenLabs into one internal tool (research-department-of-product-knowledge-series)
- [How to build a Strategy Thought Partner](sources/departmentofproduct-strategy-thought-partner.md): a PM builds a 26-framework sparring app entirely by prompting the Claude Code desktop app (research-department-of-product-knowledge-series)

## one-job-per-agent: One job per agent
- [Multi Agent Architecture explained](sources/departmentofproduct-multi-agent-architecture.md): the 2025 case for multi-agent: a single agent is "overwhelmed" by too many tools and too much context (research-department-of-product-knowledge-series)

## opportunity-to-code-chain: Opportunity → problem → goal → intent → plan → code
- [What are Claude Skills and how can you use them for product-related work?](sources/departmentofproduct-claude-skills-for-product-work.md): Notion's Spec to Implementation skill goes spec, plan page, 42 tracked tasks, then Claude Code status updates, but assumes the whole cycle lives in Notion (research-department-of-product-knowledge-series)
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): signal → judge → spec (codebase-checked, complexity-tagged) → routed to Claude Code or Linear → review agent checks the PR against the spec's acceptance criteria and instrumentation (research-department-of-product-knowledge-series)
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): research → shortlist → PRD → screens → stakeholder PowerPoint, all in one Claude Code session over the Stitch MCP (research-department-of-product-knowledge-series)
- [Practical Agent Skills for Product Teams](sources/departmentofproduct-practical-agent-skills.md): compound-engineering splits brainstorm (what), plan (how) and work, with an artifact between each stage. Atlassian's official skill turns a Confluence spec into a Jira epic plus tickets and shows the breakdown for approval first (research-department-of-product-knowledge-series)

## org-context-grounding: Agents work when grounded in organisation context
- [Decision Models Explained - The New AI Building Block for Product Teams](sources/departmentofproduct-decision-models.md): in Rippling's GrowthOS test a classifier won on email triage (90% vs 50%) but failed as a text-to-SQL control step because it couldn't read business definitions like "qualified pipeline"; hybrid recommended (research-department-of-product-knowledge-series)
- [Context Engineering for AI Agents Explained - a simple overview of the basics](sources/departmentofproduct-context-engineering-basics.md): calendar-agent example; a rich reply needs contacts, calendar, past threads and send tools (research-department-of-product-knowledge-series)
- [How to use Claude Cowork as a Competitive Intelligence System](sources/departmentofproduct-cowork-competitive-intelligence.md): recommends a "my-company" folder of strategy presentations and OKRs and a competitor list kept as a file so the agent can judge strategic gaps (research-department-of-product-knowledge-series)
- [Claude Design is here](sources/departmentofproduct-claude-design.md): setup starts with a design system imported from a repo, code folder or .fig file. Claude extracts the components into an editable library (research-department-of-product-knowledge-series)
- [How to build a Strategy Thought Partner](sources/departmentofproduct-strategy-thought-partner.md): a company-context settings page whose text feeds every analysis (research-department-of-product-knowledge-series)

## org-learning-loop: One person's win becomes everyone's baseline
- [How to Build Powerful Internal AI Productivity Tools](sources/departmentofproduct-internal-ai-tools-ramp-glass.md): worked SaaS example where a senior PM's research-to-prioritised-spec skill is reused by every PM; a city-launch skill sets the baseline for each new market (research-department-of-product-knowledge-series)

## outcome-measurement-gap: Nobody can yet measure PM-agent outcomes
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): ship rate vs "would do" rate as a measure, plus a per-change outcome log (research-department-of-product-knowledge-series)
- [How to test a new AI Model](sources/departmentofproduct-model-sense-testing.md): Claude read "this year" as 2024 in a Google Analytics task, and only a hand check of the numbers caught it (research-department-of-product-knowledge-series)

## pm-job-stable-methods-change: The PM job is stable; how it is done is changing
- [How to become "AI fluent"](sources/departmentofproduct-ai-fluency.md): Zapier's rubric marks manual-only work and dismissing AI as "unacceptable" for every role, product included (research-department-of-product-knowledge-series)

## pm-persona-role-expansion: PM and adjacent personas are expanding or blurring
- [How to Build Powerful Internal AI Productivity Tools](sources/departmentofproduct-internal-ai-tools-ramp-glass.md): an emerging "internal AI specialist" role at OpenAI, Figma, Replit and Ramp (second-hand) (research-department-of-product-knowledge-series)
- [How to "vibe code"](sources/departmentofproduct-vibe-coding.md): three team scenarios; the author leans to designer-led, with PMs overseeing several squads "including eventually, autonomous AI teams" (research-department-of-product-knowledge-series)
- [What is parallel AI agent coding? An in-depth guide for product teams](sources/departmentofproduct-parallel-agent-coding.md): claim that PMs, as "mini orchestrators", could judge parallel agents' output and run feature variants as experiments (research-department-of-product-knowledge-series)
- [Claude Design is here](sources/departmentofproduct-claude-design.md): reads model-native design tools as "closing the gaps between each of the traditional product disciplines" (research-department-of-product-knowledge-series)

## pm-tool-connectivity: Reaching PM tools from agents
- [What is a Command Line Interface and why do they suddenly matter to product teams?](sources/departmentofproduct-cli-for-product-teams.md): Google Workspace CLI (`gws <service> <resource> <method>`) gives Claude Code all of Workspace plus workflow commands; auth setup is "fiddly" (research-department-of-product-knowledge-series)
- [How to build the ultimate Product Dashboard that generates stakeholder updates on demand](sources/departmentofproduct-product-dashboard-stakeholder-updates.md): Slack and Gmail wiring is left as a prompt asking the agent what credentials it needs (research-department-of-product-knowledge-series)
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): progressive tool disclosure (Square); Stripe Toolshed's ~500 tools with a curated subset for each agent (research-department-of-product-knowledge-series)
- [How to develop a Headless Product Strategy](sources/departmentofproduct-headless-product-strategy.md): Linear's CEO says agent-created MCP issues now outnumber human ones; PostHog reports 50x more headless MCP requests in 6 months (vendor statements) (research-department-of-product-knowledge-series)
- [Practical ways to use MCP at work](sources/departmentofproduct-mcp-at-work.md): Zapier MCP as an aggregator behind one connector, with native connectors as fallback, for a daily briefing (research-department-of-product-knowledge-series)
- [How to use Perplexity's new Computer...](sources/departmentofproduct-perplexity-computer.md): read/write connectors (Linear, Slack, Notion, Salesforce, Snowflake), which can be embedded two-way in apps the agent builds (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): connectors listed per routine (Jira/Linear, Slack, Notion, Drive, Intercom/Zendesk via MCP, optionally Salesforce for ARR weighting) (research-department-of-product-knowledge-series)
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): Stitch MCP added to Claude Code so the agent can generate and fetch design screens (research-department-of-product-knowledge-series)
- [How to use Claude Cowork as a Competitive Intelligence System](sources/departmentofproduct-cowork-competitive-intelligence.md): at Feb 2026 the Google Drive connector read only Google Docs under 10MB, main text only (no images, comments or suggestions) (research-department-of-product-knowledge-series)
- [How to develop an MCP Product Strategy](sources/departmentofproduct-mcp-product-strategy.md): in mid-2025 Linear's MCP had 5 tools and Notion's 13. Notion reportedly built "AI-first tools" with its own agent team instead of wrapping its v1 API (research-department-of-product-knowledge-series)

## prd-agents: PRD and spec writing/review as an agent job
- [How to use Claude Code for non-engineering use cases](sources/departmentofproduct-claude-code-non-engineers.md): PRD and Jira-ticket subagents from community templates; a one-line change produced an oversized story (research-department-of-product-knowledge-series)
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): a chosen research finding becomes a short PRD, which becomes the prompt for screen generation (research-department-of-product-knowledge-series)

## product-artifact-primitives: Native PM artifact objects and project containers across platforms
- [How to use Claude Projects and Skills to Monitor your Product's Health](sources/departmentofproduct-claude-projects-product-health.md): a Project (instructions, knowledge files, history) is the PM's standing container; filename prefixes stand in for structure (research-department-of-product-knowledge-series)

## product-coherence-over-automation: Product coherence can suffer from over-automation
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): metric-chasing agents risk wins that harm the experience (Netflix autoplay), "AI optimized product slop" (research-department-of-product-knowledge-series)
- [DESIGN.md Explained](sources/departmentofproduct-design-md-explained.md): "consistency gets easier but coherence gets harder"; finished-looking AI output suppresses critique. (research-department-of-product-knowledge-series)
- [How do AI coding agents work?](sources/departmentofproduct-ai-coding-agents-explained.md): once engineering capacity stops being the constraint, the risk is "feature slop" and feature discovery becomes the bottleneck. (research-department-of-product-knowledge-series)

## project-taxonomy: How 'project' is defined
- [How to use Claude Projects and Skills to Monitor your Product's Health](sources/departmentofproduct-claude-projects-product-health.md): either one Project, or five function-owned sub-Projects plus a master; the master is fed by pasting each sub-Project's summary by hand (research-department-of-product-knowledge-series)

## prototyping-agents-limits: Prototyping agents and their limits
- [How to build AI Assistant Prototypes](sources/departmentofproduct-ai-assistant-prototypes.md): five vibe-coded clones built from chatbot ideas, then PRD, then a Lovable prompt, with no eval or user test; the author admits the inputs were illustrative (research-department-of-product-knowledge-series)
- [How to "vibe code"](sources/departmentofproduct-vibe-coding.md): Replit couldn't fix a padding bug even from a screenshot; chat-only Lovable leaves non-coders stuck: "works well - until it doesn't" (research-department-of-product-knowledge-series)
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): Stitch output is "by no means production-ready"; for discussion only; beta, free with limits (research-department-of-product-knowledge-series)
- [How to build a Persona Feature Tester with Claude Code and ElevenLabs](sources/departmentofproduct-persona-feature-tester.md): Claude Design's first pass looked like a brochure until the author redirected it (research-department-of-product-knowledge-series)
- [Claude Design is here](sources/departmentofproduct-claude-design.md): onboarding, landing page and 3D component were strong from short prompts. The stakeholder deck was "passable" but full of AI clichés, and PPT export failed (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): Alloy builds features on a screenshot of the live product and pulls specs from Jira, Linear or Notion (research-department-of-product-knowledge-series)

## research-synthesis-agents: Research synthesis agents
- [How to build a Persona Feature Tester with Claude Code and ElevenLabs](sources/departmentofproduct-persona-feature-tester.md): a Claude Project loaded with NN/g articles derives five personas from the research folders (research-department-of-product-knowledge-series)
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): Claude Code reads research transcripts and shortlists three product changes (the transcripts were mock) (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): AI-moderated interview tools (Strella, Askable, Listen) run sessions at scale and write the synthesis. Amazon reportedly uses Strella (research-department-of-product-knowledge-series)

## risk-review-as-classification: Risk review as a specification and classification problem
- [Decision Models Explained - The New AI Building Block for Product Teams](sources/departmentofproduct-decision-models.md): the same "is this safe to run?" check before every agent action, where speed matters; Vercel's CEO is relayed as claiming 18x faster safety checks (research-department-of-product-knowledge-series)

## risk-sloped-review: Human review sloped to risk
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): split actions by reversibility: easy-to-undo actions in the agent's free zone, payments, publishing and financial records in a hardcoded layer (research-department-of-product-knowledge-series)
- [How to Identify Opportunities for AI Automation](sources/departmentofproduct-ai-automation-opportunities.md): cost-if-wrong is an explicit axis, colour-coded on the canvas; drafting legal terms fails even though it is verifiable, because it is high-risk and infrequent. (research-department-of-product-knowledge-series)

## single-agent-many-skills: One agent with many skills, not many agents
- [Why Semantic Data Layers matter](sources/departmentofproduct-semantic-data-layers.md): Anthropic pairs a thin "router" knowledge skill (semantic layer first, then domain files) with an analyst-workflow skill that ends in adversarial review. (research-department-of-product-knowledge-series)
- [Multi Agent Architecture explained](sources/departmentofproduct-multi-agent-architecture.md): treats a single agent as fit only for simple cases, the opposite of Cognition's later view (research-department-of-product-knowledge-series)
- [Practical Agent Skills for Product Teams](sources/departmentofproduct-practical-agent-skills.md): gstack and Every's compound-engineering are skill families that act "like a small virtual team" in one harness. Each stage writes a file the next stage reads (research-department-of-product-knowledge-series)
- [How to use Claude Cowork as a Competitive Intelligence System](sources/departmentofproduct-cowork-competitive-intelligence.md): one Cowork session chains browser research, then xlsx/pptx/docx skills, then the PM plugin's /stakeholder-update for Slack (research-department-of-product-knowledge-series)

## skill-standards: Skill standards
- [What are Claude Skills and how can you use them for product-related work?](sources/departmentofproduct-claude-skills-for-product-work.md): PM primer on the three SKILL.md layers and progressive disclosure; vendor skill zips ship with evals, examples and references folders (research-department-of-product-knowledge-series)
- [How to develop a Headless Product Strategy](sources/departmentofproduct-headless-product-strategy.md): a tool is something an agent calls; a skill is something it reads (Webflow skills for Codex and ChatGPT) (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): process in SKILL.md and voice in a separate brand file, reused by every routine that writes customer-facing text (research-department-of-product-knowledge-series)
- [Practical Agent Skills for Product Teams](sources/departmentofproduct-practical-agent-skills.md): recaps SKILL.md as three layers (a header for selection, the instructions, and files loaded only when needed). Skills load automatically, with no explicit call (research-department-of-product-knowledge-series)

## skill-supply-chain-security: Skill supply chain security
- [Practical Agent Skills for Product Teams](sources/departmentofproduct-practical-agent-skills.md): a popular PM newsletter offers one download bundling skills from 10 repos, one of them a collection of 1,000+ skills, with no warning about review, pinning or scanning (research-department-of-product-knowledge-series)

## skills-marketplace: A versioned skills marketplace with hidden Git
- [How to Build Powerful Internal AI Productivity Tools](sources/departmentofproduct-internal-ai-tools-ramp-glass.md): Dojo skills are "executable, not just readable" and reviewed like code; Sensei means a new PM "never has to browse 350 options" (restates Ramp) (research-department-of-product-knowledge-series)
- [How to use Cursor for Non-Engineering use cases](sources/departmentofproduct-cursor-for-non-engineers.md): Cursor's Plugin Marketplace bundles MCP, skills, agents and hooks into one-click installs (Feb 2026). (research-department-of-product-knowledge-series)
- [Practical Agent Skills for Product Teams](sources/departmentofproduct-practical-agent-skills.md): cites an estimate of 40k–100k published skills and says finding the useful ones is "increasingly difficult". The post itself works as a hand-curated catalogue of 10 (research-department-of-product-knowledge-series)

## spec-becomes-prototype-and-evals: The spec is replaced by prototype plus evals
- [How to use Google's new Ideate Agent for Product Discovery and Ideation](sources/departmentofproduct-google-stitch-ideate-agent.md): the PRD is an intermediate step the agent writes; the screens are what goes to stakeholders (research-department-of-product-knowledge-series)

## status-update-agents: Status updates and 'ask the org' Q&A as an agent job
- [How to build the ultimate Product Dashboard that generates stakeholder updates on demand](sources/departmentofproduct-product-dashboard-stakeholder-updates.md): pick data points, a format (Slack, email, voice-cloned audio) and an audience (C-suite, users, team), get a draft (research-department-of-product-knowledge-series)
- [What is a Command Line Interface and why do they suddenly matter to product teams?](sources/departmentofproduct-cli-for-product-teams.md): "Prepare me for my day" over calendar and inbox; one post-sprint-review instruction chains four Workspace CLI operations (research-department-of-product-knowledge-series)
- [How to use Claude Projects and Skills to Monitor your Product's Health](sources/departmentofproduct-claude-projects-product-health.md): a master Project writes an exec health report under 500 words with talking points (research-department-of-product-knowledge-series)
- [How to use Perplexity's new Computer...](sources/departmentofproduct-perplexity-computer.md): meeting-to-ticket worker: extracts commitments, creates assigned Linear tickets, emails a summary, nudges after 3 idle days (research-department-of-product-knowledge-series)
- [Practical ways to use MCP at work](sources/departmentofproduct-mcp-at-work.md): "chief of staff" daily briefing from calendar, Linear, Zendesk, Slack and news (research-department-of-product-knowledge-series)
- [Practical ways to use Claude Routines at work - a Guide for Product Teams](sources/departmentofproduct-claude-routines-for-product-teams.md): Monday 7am backlog digest posted to Slack before standup, with separate versions for PM and engineering lead (research-department-of-product-knowledge-series)
- [How to use Claude Cowork as a Competitive Intelligence System](sources/departmentofproduct-cowork-competitive-intelligence.md): /stakeholder-update asks the update type and audience, then rewrites a research deck as a Slack-ready exec message (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): OpenAI's in-house assistant reportedly summarises research sessions and pushes insights to stakeholders in Slack (second-hand) (research-department-of-product-knowledge-series)

## synthetic-users-limits: Synthetic users and AI personas: limits
- [How to build a Persona Feature Tester with Claude Code and ElevenLabs](sources/departmentofproduct-persona-feature-tester.md): personas billed as "grounded in real world data" but built from mock data that Cowork generated; no check against real users (research-department-of-product-knowledge-series)
- [How to build a Strategy Thought Partner](sources/departmentofproduct-strategy-thought-partner.md): the base app runs features past "data-grounded" synthetic personas, including voice calls, with no validation discussed (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): Askable reportedly builds a queryable model from real interviews to answer hypothetical market questions, presented with no caveat (research-department-of-product-knowledge-series)

## tacit-knowledge-capture: Capturing tacit knowledge from people for agents
- [Why Semantic Data Layers matter](sources/departmentofproduct-semantic-data-layers.md): LLM-written metric definitions failed at Anthropic; the rule became "AI drafts, a named human owns the definition". (research-department-of-product-knowledge-series)

## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is rare
- [Decision Models Explained - The New AI Building Block for Product Teams](sources/departmentofproduct-decision-models.md): every figure comes from a vendor or CEO, and the leaderboards are only at versions 0.2.1 and 0.3 (research-department-of-product-knowledge-series)
- [How to Build Powerful Internal AI Productivity Tools](sources/departmentofproduct-internal-ai-tools-ramp-glass.md): restates Glass's 350+ skills and its moat claim without data (research-department-of-product-knowledge-series)
- [How to build a Self-improving Product](sources/departmentofproduct-self-improving-product.md): Amplitude Wave reports only ~11% of suggested fixes shipped end to end vs ~50% "would do": an unusually candid vendor number (research-department-of-product-knowledge-series)
- [How to become "AI fluent"](sources/departmentofproduct-ai-fluency.md): relays Fin 86%, Amazon 90% and Stripe 64% figures without question (research-department-of-product-knowledge-series)
- [How to speed up engineering velocity with AI: a non-engineer's guide](sources/departmentofproduct-engineering-velocity-non-engineers.md): Jellyfish, Graphite-at-Shopify (+33% PRs), Glean (-30% turnover) and Morgan Stanley figures repeated unchecked (research-department-of-product-knowledge-series)
- [Multi Agent Architecture explained](sources/departmentofproduct-multi-agent-architecture.md): Accenture says 10-15% of its clients use multi-agent systems, rising past 30% (WSJ, unchecked) (research-department-of-product-knowledge-series)
- [Practical Agent Skills for Product Teams](sources/departmentofproduct-practical-agent-skills.md): repeats "Anthropic reporting accuracy went from 21% to 95% with skills" with no source (research-department-of-product-knowledge-series)
- [How to do AI-powered product discovery sprints](sources/departmentofproduct-ai-discovery-sprints.md): repeats Strella's claims (8 weeks down to days; people are more honest with an AI moderator) without checking them (research-department-of-product-knowledge-series)
- [How to test a new AI Model](sources/departmentofproduct-model-sense-testing.md): benchmarks "are often presented in a way that flatters the model" (research-department-of-product-knowledge-series)

## work-structure-spectrum: Work structure spectrum (unstructured exploration to task-specific workflow)
- [Are Agent Harnesses the new "secret sauce" for Product Teams?](sources/departmentofproduct-agent-harnesses-secret-sauce.md): Stripe Minions blueprints and GitHub Copilot's mandatory CodeQL and secret scanning as "mix AI steps with fixed rules" (research-department-of-product-knowledge-series)
- [How to use Perplexity's new Computer...](sources/departmentofproduct-perplexity-computer.md): outcome-first planning with sub-agents, plus persistent background workers on triggers that run "indefinitely" (research-department-of-product-knowledge-series)
- [How to Identify Opportunities for AI Automation](sources/departmentofproduct-ai-automation-opportunities.md): scores each task 1-3 on safety, volume and verifiability, giving three outcomes: automate now, AI assistant, or not ready. (research-department-of-product-knowledge-series)
- [Agentic Workflows Explained](sources/departmentofproduct-agentic-workflows-explained.md): deterministic automation vs non-deterministic agentic workflow as the first mental model, with a seven-part anatomy. (research-department-of-product-knowledge-series)
- [How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer](sources/departmentofproduct-loops-goals-slash-commands.md): steps of structure inside one harness: a prompt, then a goal (a stated "done" condition), then a loop that calls a reusable command file (research-department-of-product-knowledge-series)
- [How to use Claude Cowork as a Competitive Intelligence System](sources/departmentofproduct-cowork-competitive-intelligence.md): a user-defined phrase ("Run the intel workflow") reruns the whole chain, adding structure on demand inside a general agent (research-department-of-product-knowledge-series)
- [How to build a Strategy Thought Partner](sources/departmentofproduct-strategy-thought-partner.md): product frameworks supply the structure. A recommender picks 3, then the chosen framework scripts a step-by-step sparring conversation (research-department-of-product-knowledge-series)
