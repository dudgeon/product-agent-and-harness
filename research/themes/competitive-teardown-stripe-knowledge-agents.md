# Theme evidence: competitive-teardown-stripe-knowledge-agents

Written only by the task `competitive-teardown-stripe-knowledge-agents`. Built into ../THEMES.md by ../build.py.

## harness-over-model: The harness, not the model, limits real-world value
- [Stripe's AI minions ship 1,300 PRs weekly from a Slack emoji (How I AI)](sources/howiai-stripe-minions-kaliski.md): minions succeed because of years of devex: hosted devboxes, CI, docs, a 'blessed path for 90% of the common activities' (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): data-agent quality depends on pre-AI investments: tiered data catalog, blessed analytics layer, a warehouse hardened for agent query load (competitive-teardown-stripe-knowledge-agents)

## org-learning-loop: One person's win becomes everyone's baseline
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): roadmap: Kai reflects on traces involving a skill, proposes and tests improvements, submits them for the skill owner's review (competitive-teardown-stripe-knowledge-agents)
- [Stripe's payment method factory](sources/stripe-payment-method-factory.md): learning logs, decision logs, transcripts and PR comments from each run feed an agent that proposes updates to 100+ reusable prompts; an observer agent hardens prompts (competitive-teardown-stripe-knowledge-agents)

## skills-marketplace: A versioned skills marketplace with hidden Git
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): Agent Studio: domain owners build, test and monitor skills, custom Kai agents and tool selections, with usage and quality signals per asset, organised in 'areas' (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): skill-creator turns a session into a skill; publish private or to an area; IDE-like draft editor; automatic improvement suggestions to authors (competitive-teardown-stripe-knowledge-agents)
- [Emily Glassberg Sands on Latent Space](sources/latentspace-emily-sands-stripe.md): pre-Kai GoLLM 'presets' (saved, shared prompts): hundreds created overnight (Oct 2025) (competitive-teardown-stripe-knowledge-agents)

## memory-architecture: Memory as inspectable files from an offline pipeline
- [How Stripe Built Kai on Deep Agents (LangChain)](sources/langchain-how-stripe-built-kai-deep-agents.md): Kai keeps session state in an S3-backed virtual filesystem; sandbox calls sync files in and out so the agent sees one persistent file environment per session (competitive-teardown-stripe-knowledge-agents)

## cost-control-routing: Cost metering and model routing built into the harness
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): Kai projects set the default model and can block expensive models for a workflow (competitive-teardown-stripe-knowledge-agents)
- [Production-grade AI agents for financial compliance: Lessons from Stripe](sources/aws-stripe-compliance-agents.md): all LLM calls go through an LLM Proxy (noisy-neighbour limits, fallbacks, usage tracking by privacy class); prompt caching cut cost 60% (competitive-teardown-stripe-knowledge-agents)

## single-agent-many-skills: One agent with many skills, not many agents
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): one Kai harness over 1,000+ skills and tools; a no-code builder that produced 4,000+ micro-agents was replaced because of duplicated, uneven, hard-to-maintain agents (competitive-teardown-stripe-knowledge-agents)
- [How Stripe Built Kai on Deep Agents (LangChain)](sources/langchain-how-stripe-built-kai-deep-agents.md): skills gate tools via allowedTools (two-pass); foundational skills pinned; frontier-model quality degrades past ~150 skills with the system prompt (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): ~2,000 skills: ~50 used heavily daily, 100-150 by sub-orgs, many by 2-3 people; telemetry pipeline decides what to promote or move out of the general context (competitive-teardown-stripe-knowledge-agents)

## enablement-by-product: The product is the enablement
- [How Stripe Built Kai on Deep Agents (LangChain)](sources/langchain-how-stripe-built-kai-deep-agents.md): adoption came from removing knobs: users who bounced off configurable tools found Kai needed none (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): pilot with GTM (200-300 users), then a company-wide demo triggered the ramp (competitive-teardown-stripe-knowledge-agents)

## build-vs-buy: Own the agent harness as a moat
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): built after a no-code agent builder and coding agents for non-engineers both failed (quality sprawl; security and support burden); core primitives shared with Stripe's customer-facing agents (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): 'it's not about providing AI it's about providing the correct governance structures'; v0 by 1.5 people in two weeks; core team under 10 (competitive-teardown-stripe-knowledge-agents)
- [Emily Glassberg Sands on Latent Space](sources/latentspace-emily-sands-stripe.md): Sands: build-vs-buy is 'sequential': built GoLLM when no safe vendor existed, then replaced it with open-source LibreChat; buys via RFP 'spotlight' (Braintrust for evals) (competitive-teardown-stripe-knowledge-agents)

## non-engineer-builders: Non-engineers ship through agents
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): 3,000+ Stripes made 12,000 prototypes in Harbor (25% of Stripes); Finance presents actuals as clickable prototypes; AEs build ROI calculators (competitive-teardown-stripe-knowledge-agents)
- [Jeff Weinstein: Kai, Minions' sibling](sources/x-jeff-weinstein-kai-sibling.md): a Stripe product lead uses Kai 'all day long' (competitive-teardown-stripe-knowledge-agents)

## legible-org-for-agents: Make the organisation legible to agents
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): org chart, projects/OKRs and a tiered data catalog are what let Kai 'do the right thing' without users explaining their job (competitive-teardown-stripe-knowledge-agents)

## evals-autonomy-trust: Evals, autonomy sliders and earned trust
- [Production-grade AI agents for financial compliance: Lessons from Stripe](sources/aws-stripe-compliance-agents.md): each compliance sub-question is validated against human quality standards before it may inform reviewers in production (competitive-teardown-stripe-knowledge-agents)

## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is rare
- [Stripe Got 83% of Staff Using One AI Agent. Don't Copy Its Sales Numbers.](sources/aifounders-stripe-kai-dont-copy-sales-numbers.md): independent critique: Kai's +39% deals compares the same sellers' Kai and non-Kai weeks; early adopters are the best sellers; cause open (competitive-teardown-stripe-knowledge-agents)
- [Sharadh Krishnamurthy LinkedIn Kai launch post](sources/linkedin-sharadhk-kai-launch-post.md): Kai usage stated as 80% weekly / 20,000+ sessions a day (LinkedIn), 83% (blog), 86%+ (podcast), '>60k sessions' (LangChain): inconsistent bases (competitive-teardown-stripe-knowledge-agents)

## metrics-review-agents: Metrics review and analytics agents
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): Kai's 'ask data' skill: existing reports first, then the blessed analytics layer, then the data catalog; 5,000+ Kai sessions a day are data analysis (competitive-teardown-stripe-knowledge-agents)

## outcome-measurement-gap: Nobody can yet measure PM-agent outcomes
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): Kai's outcome numbers are within-person usage comparisons (Kai weeks vs non-Kai weeks; power vs low users), not controlled tests (competitive-teardown-stripe-knowledge-agents)
- [Emily Glassberg Sands on Latent Space](sources/latentspace-emily-sands-stripe.md): Sands (Oct 2025): 'I have a really hard time understanding impact. Like I don't quite know what statistic to look at' (competitive-teardown-stripe-knowledge-agents)

## prototyping-agents-limits: Prototyping agents and their limits
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): Harbor prototype animation shipped 'nearly one-for-one'; prototypes became inputs to reviews; next step is live data and prototype-scoped databases (competitive-teardown-stripe-knowledge-agents)

## org-context-grounding: Agents work when grounded in organisation context
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): Kai knows the user and org chart by default, reads the project-management system, and connects Drive, Slack and DMs only if the user opts in (toggleable per session) (competitive-teardown-stripe-knowledge-agents)
- [Emily Glassberg Sands on Latent Space](sources/latentspace-emily-sands-stripe.md): Hubert (text-to-SQL) failed most at data discovery; fixed by deprecating low-quality tables, owner-written docs, and org-position persona context (competitive-teardown-stripe-knowledge-agents)

## agent-failure-modes: Recurring agent failure modes in PM work
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): 'There were agents that went rogue ... may have almost taken down core systems'; 'when in doubt an agent will just brute force it' (competitive-teardown-stripe-knowledge-agents)

## human-review-gates: Human review gates on agent output
- [Production-grade AI agents for financial compliance: Lessons from Stripe](sources/aws-stripe-compliance-agents.md): compliance agents answer sub-questions as pre-fetched research; the human reviewer answers every sub-task; 26% faster median review, >96% helpfulness (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): per-project human-in-the-loop confirmation on sensitive tools, deliberately not for everyone, because prompting on every call makes people 'press the wrong button' (competitive-teardown-stripe-knowledge-agents)

## one-job-per-agent: One job per agent
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): Stripe: 'keep agents specialized (on research, coding, or browser-native tools) while exposing them to capabilities in other systems' (competitive-teardown-stripe-knowledge-agents)

## harness-portability: Harness portability
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): a Kai project can be backed by a different API and harness while keeping Kai's features; Kai skills follow the open skill spec (competitive-teardown-stripe-knowledge-agents)
- [Stripe Got 83% of Staff Using One AI Agent. Don't Copy Its Sales Numbers.](sources/aifounders-stripe-kai-dont-copy-sales-numbers.md): 'the skills are the durable asset'; keep them exportable from any vendor harness (competitive-teardown-stripe-knowledge-agents)

## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): Kai sessions are cloud-hosted and long (one hit 932 turns) but single-user; context is 'locked in'; sharing and multi-person artifacts are on the roadmap (competitive-teardown-stripe-knowledge-agents)
- [Stripe's AI minions ship 1,300 PRs weekly from a Slack emoji (How I AI)](sources/howiai-stripe-minions-kaliski.md): minions run in a public Slack 'robots' channel watched by 76 people: open-by-default observation and 'pair prompting' (competitive-teardown-stripe-knowledge-agents)
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): Harbor shares artifacts, not sessions: one published snapshot per URL, anchored comments that re-resolve after agent rewrites, remix into a copy (competitive-teardown-stripe-knowledge-agents)

## remote-agent-invocation: Remote agent invocation
- [Stripe's AI minions ship 1,300 PRs weekly from a Slack emoji (How I AI)](sources/howiai-stripe-minions-kaliski.md): minions start from a Slack emoji reaction (message = prompt, emoji picks the repo), also from Docs and tickets, and from a phone (competitive-teardown-stripe-knowledge-agents)
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): Harbor's toolset is exposed on Stripe's internal MCP so Kai and devbox coding agents can create, read, update and publish prototypes; its renderer is a separate service (competitive-teardown-stripe-knowledge-agents)

## agent-frameworks: Agent frameworks
- [How Stripe Built Kai on Deep Agents (LangChain)](sources/langchain-how-stripe-built-kai-deep-agents.md): Kai built on LangChain Deep Agents: 'solves all the non-Stripey problems'; minions on a Goose fork: Stripe uses two different open-source harnesses for two agent families (competitive-teardown-stripe-knowledge-agents)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): 'agentic identity ... we haven't solved this yet'; agent identity tags the use case an agent serves, used for priority and load shedding after agents nearly took down core systems (competitive-teardown-stripe-knowledge-agents)

## skill-standards: Skill standards
- [AI steering experiments (Stripe)](sources/stripe-ai-steering-experiments.md): modular, progressively disclosed skills beat a monolithic skill by ~10% on Stripe's eval suite and used fewer tokens (competitive-teardown-stripe-knowledge-agents)

## work-structure-spectrum: Work structure spectrum (unstructured exploration to task-specific workflow)
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): coding work is uniform enough for one agent architecture; knowledge work needs different tools, data, outputs and definitions of done per task (competitive-teardown-stripe-knowledge-agents)
- [Production-grade AI agents for financial compliance: Lessons from Stripe](sources/aws-stripe-compliance-agents.md): compliance review decomposed into a DAG of bite-sized, quality-tested sub-questions; the review tool, not an LLM, orchestrates (competitive-teardown-stripe-knowledge-agents)
- [Stripe's payment method factory](sources/stripe-payment-method-factory.md): 'although an LLM can orchestrate a workflow, predictable coordination is better implemented in code' (competitive-teardown-stripe-knowledge-agents)

## agent-as-service-many-surfaces: The agent as a service with many surfaces
One agent service behind an API, reached through a web app, Slack, browser extensions and embedding in existing tools, rather than a single app or a separate agent per surface. Matters for the agent-interface choice (own app vs Slack vs embedded).
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): "The agent is a service, not an application, and surfaces are simply customized views into it"; web app, Slack, Chrome extension in third-party tools, internal apps embed via API (competitive-teardown-stripe-knowledge-agents)
- [Stripe built their own in-house Glean alternative](sources/groundedhallucination-stripe-kai-teardown.md): "Surfaces are views, not the product" (independent restatement) (competitive-teardown-stripe-knowledge-agents)
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): Harbor is its own browser app but also an MCP toolset and a rendering service other agents call (competitive-teardown-stripe-knowledge-agents)

## scoped-governance-containers: Governance scoped to a project or workspace
Policy (default model, allowed tools, human-in-the-loop rules, data back end, even which harness) set once by a project owner and applied to everyone working in that project, rather than per user or org-wide. Matters for governance and trust defaults.
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): "projects are primarily a governance mechanism"; owners set default model, tool policies, HITL; HR has a separately backed secure project; projects of 5 to 500 people (competitive-teardown-stripe-knowledge-agents)
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): domain-owned custom Kai agents load a team's skills and data sources by default (competitive-teardown-stripe-knowledge-agents)

## task-context-isolation: Isolation by task context, not only by user permission
Limiting what a session may combine based on the task (e.g. never two customers' data in one analysis), even when the user could access each separately. Matters for trust/privacy defaults of shared or discoverable sessions.
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): "you shouldn't combine data from two unrelated customer contexts in a single analysis"; the boundary is "what should this task be allowed to view given this context?" (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): tool policies stop sensitive HR data being written to a Stripe-wide doc without banning tools (competitive-teardown-stripe-knowledge-agents)
