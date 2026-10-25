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
- [Uber Agentic Pods (CTO post)](sources/x-praveen-uber-agentic-pods.md): 16 two-week pods in 16 functions: shadow, prioritise, build with the expert, validate, ship ('building with them, not for them') (first-party) (competitive-teardown-stripe-knowledge-agents)
- [How Stripe Built a new Internal AI Knowledge Platform (Department of Product)](sources/departmentofproduct-stripe-kai.md): 'start with one domain and one surface', the most repeatable job in the tool people already use (independent) (competitive-teardown-stripe-knowledge-agents)

## build-vs-buy: Own the agent harness as a moat
- [Meet Stripe's Knowledge AI Platform](sources/stripe-meet-knowledge-ai-platform.md): built after a no-code agent builder and coding agents for non-engineers both failed (quality sprawl; security and support burden); core primitives shared with Stripe's customer-facing agents (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): 'it's not about providing AI it's about providing the correct governance structures'; v0 by 1.5 people in two weeks; core team under 10 (competitive-teardown-stripe-knowledge-agents)
- [Emily Glassberg Sands on Latent Space](sources/latentspace-emily-sands-stripe.md): Sands: build-vs-buy is 'sequential': built GoLLM when no safe vendor existed, then replaced it with open-source LibreChat; buys via RFP 'spotlight' (Braintrust for evals) (competitive-teardown-stripe-knowledge-agents)

## non-engineer-builders: Non-engineers ship through agents
- [Harbor: Stripe's AI-assisted prototyping tool](sources/stripe-harbor-ai-prototyping.md): 3,000+ Stripes made 12,000 prototypes in Harbor (25% of Stripes); Finance presents actuals as clickable prototypes; AEs build ROI calculators (competitive-teardown-stripe-knowledge-agents)
- [Jeff Weinstein: Kai, Minions' sibling](sources/x-jeff-weinstein-kai-sibling.md): a Stripe product lead uses Kai 'all day long' (competitive-teardown-stripe-knowledge-agents)
- [Protodash (How I AI, Owen Williams)](sources/howiai-stripe-protodash-owen-williams.md): Stripe's Dashboard prototyping studio is used by 'more PMs than designers these days'; a PM on an unstaffed area 'can unblock himself' (competitive-teardown-stripe-knowledge-agents)

## legible-org-for-agents: Make the organisation legible to agents
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): org chart, projects/OKRs and a tiered data catalog are what let Kai 'do the right thing' without users explaining their job (competitive-teardown-stripe-knowledge-agents)
- [An Inside Look Into How This $159B Tech Company Ships So Fast](sources/youtube-notmybusiness-inside-stripe-ships-fast.md): Orbit plans by 'reading files in our code base, it's reading Trailhead' (internal docs); Compass tracks projects (competitive-teardown-stripe-knowledge-agents)
- [Inside Stripe's Engineering Culture: Part 2](sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md): pre-AI internal tools: Trailhead (docs structured like the external docs), Compass (project status, linked docs, standups), Home intranet search (2024) (competitive-teardown-stripe-knowledge-agents)

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
- [Protodash (How I AI, Owen Williams)](sources/howiai-stripe-protodash-owen-williams.md): gets '90% of the way most of the time ... it will make slop'; taste and craft stay with designers (competitive-teardown-stripe-knowledge-agents)

## org-context-grounding: Agents work when grounded in organisation context
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): Kai knows the user and org chart by default, reads the project-management system, and connects Drive, Slack and DMs only if the user opts in (toggleable per session) (competitive-teardown-stripe-knowledge-agents)
- [Emily Glassberg Sands on Latent Space](sources/latentspace-emily-sands-stripe.md): Hubert (text-to-SQL) failed most at data discovery; fixed by deprecating low-quality tables, owner-written docs, and org-position persona context (competitive-teardown-stripe-knowledge-agents)
- [How can we help everyone become a 10x engineer? (Stripe Sessions 2024)](sources/stripe-sessions-2024-10x-engineer-panel.md): Stripe put an LLM bot over Trailhead only after owners verified docs and the hierarchy was trusted, so answers 'were going to be accurate' (competitive-teardown-stripe-knowledge-agents)

## agent-failure-modes: Recurring agent failure modes in PM work
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): 'There were agents that went rogue ... may have almost taken down core systems'; 'when in doubt an agent will just brute force it' (competitive-teardown-stripe-knowledge-agents)

## human-review-gates: Human review gates on agent output
- [Production-grade AI agents for financial compliance: Lessons from Stripe](sources/aws-stripe-compliance-agents.md): compliance agents answer sub-questions as pre-fetched research; the human reviewer answers every sub-task; 26% faster median review, >96% helpfulness (competitive-teardown-stripe-knowledge-agents)
- [Build your own company brain (How I AI, Krishnamurthy)](sources/howiai-stripe-kai-krishnamurthy.md): per-project human-in-the-loop confirmation on sensitive tools, deliberately not for everyone, because prompting on every call makes people 'press the wrong button' (competitive-teardown-stripe-knowledge-agents)
- [An Inside Look Into How This $159B Tech Company Ships So Fast](sources/youtube-notmybusiness-inside-stripe-ships-fast.md): deploys to 1% of boxes with automatic pause and rollback; mandated code review; review agent tested against past bad changes (competitive-teardown-stripe-knowledge-agents)

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
- [How Stripe Built a new Internal AI Knowledge Platform (Department of Product)](sources/departmentofproduct-stripe-kai.md): analogous combination guardrails (two candidates, two patients, performance plus pay) that must be enforced at infrastructure or session level, not by skill owners (independent) (competitive-teardown-stripe-knowledge-agents)

## agent-factory-sdlc: Agents across the whole product development loop
- [An Inside Look Into How This $159B Tech Company Ships So Fast](sources/youtube-notmybusiness-inside-stripe-ships-fast.md): Orbit: research, shareable plan teammates comment on, one-button handoff to a minion that may run 12 hours and pause to ask; 'Gru' code-review agent (competitive-teardown-stripe-knowledge-agents)
- [Stripe's Internal Agent Ecosystem for Product Development](sources/claude-doc-geoff-stripe-internal-agent-ecosystem.md): five-stage PM-to-code flow: Kai research, Harbor/Protodash prototype, Orbit plan, Minions build, review agent plus human (competitive-teardown-stripe-knowledge-agents)

## spec-becomes-prototype-and-evals: The spec is replaced by prototype plus evals
- [AI didn't write our SDK. It changed how we built it.](sources/stripe-ai-didnt-write-our-sdk.md): a two-day prototype moved a scope decision weeks earlier; agents draft specs reviewed as GitHub issues before implementation (~20 lint rules) (competitive-teardown-stripe-knowledge-agents)
- [Protodash (How I AI, Owen Williams)](sources/howiai-stripe-protodash-owen-williams.md): engineers worked from a designer's prototype PR: 'just use the prototype as the source of truth' (competitive-teardown-stripe-knowledge-agents)

## tacit-knowledge-capture: Capturing tacit knowledge from people for agents
How know-how that lives in people's heads (how the business works, which data to trust, design and architectural judgment) gets written down, verified and kept current so agents can use it: by passive mining of work exhaust, by experts curating docs, rules and skills, by interview-style elicitation, or by write-back from finished work. Bears on the working hypothesis that a context-creation agent is needed.
- [How can we help everyone become a 10x engineer? (Stripe Sessions 2024)](sources/stripe-sessions-2024-10x-engineer-panel.md): Trailhead makes owners verify docs or they 'drift away and get archived'; the docs complaint dropped steeply in the next engineering survey (competitive-teardown-stripe-knowledge-agents)
- [An Inside Look Into How This $159B Tech Company Ships So Fast](sources/youtube-notmybusiness-inside-stripe-ships-fast.md): a 2013 Stripe engineer: once 'no one has all of the state in their heads anymore' Stripe wrote documents, then robots, and now AI 'can ingest all of this documentation that we'd written' (competitive-teardown-stripe-knowledge-agents)
- [Protodash (How I AI, Owen Williams)](sources/howiai-stripe-protodash-owen-williams.md): a design manager encoded design-system judgment as agent rules over 18 months: 'I feel insane writing these rules, but ... once you've got them, it works' (competitive-teardown-stripe-knowledge-agents)
- [AI didn't write our SDK. It changed how we built it.](sources/stripe-ai-didnt-write-our-sdk.md): repo-local docs 'written for AI consumption' (principles, boundaries, anti-patterns) raised agent output and cut onboarding for humans (competitive-teardown-stripe-knowledge-agents)
- [Inside Stripe's Engineering Culture: Part 2](sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md): CEO- and CTO-led internal writing culture; 'vastly more people consume the writing than produce it' (competitive-teardown-stripe-knowledge-agents)
- [Investing in Internal Documentation (First Round, David Nunez)](sources/firstround-nunez-internal-documentation.md): knowledge 'trapped in an early hire's head'; internal docs lose to external docs and to the to-do list unless built into career expectations (competitive-teardown-stripe-knowledge-agents)
- [Stripe's payment method factory](sources/stripe-payment-method-factory.md): planning agent interviews the engineer for context and writes it to a shared knowledge base; learning and decision logs feed prompt updates (competitive-teardown-stripe-knowledge-agents)
- [Latent Space, Emily Sands](sources/latentspace-emily-sands-stripe.md): canonical-dataset docs written by domain owners ('brute-forcing it with humans'); Sands did not yet trust an LLM to write them (competitive-teardown-stripe-knowledge-agents)
- [Agentic memory in Copilot](sources/github-blog-agentic-memory-copilot.md): write-back with verification: agents store memories with code citations, re-checked on read; A/B merge rate 83% to 90% (first-party) (competitive-teardown-stripe-knowledge-agents)
- [InterviewBot: LLM-led interviews](sources/arxiv-interviewbot-mllm-led-interviews.md): against interview agents as-is: LLM interviewers are 'acknowledgment-heavy but probe-light', 4.9% deepening probes in 428 turns (independent) (competitive-teardown-stripe-knowledge-agents)
- [Anthropic Interviewer](sources/anthropic-interviewer-launch.md): 1,250 AI-led interviews, 97.6% satisfied: scalable and liked, but it captures attitudes, not expertise (first-party) (competitive-teardown-stripe-knowledge-agents)
- [Knowledge elicitation automation with LLMs](sources/swj-knowledge-elicitation-automation-llms.md): AI interviews were more efficient, but AI-built ontologies missed data and hallucinated (independent, weak) (competitive-teardown-stripe-knowledge-agents)
- [Generative AI and the SECI model](sources/arxiv-uchihira-genai-seci-model.md): GenAI work on tacit knowledge is still 'fragmentary'; most GenAI KM handles explicit knowledge (independent position paper) (competitive-teardown-stripe-knowledge-agents)
- [Scaling expertise with generative AI](sources/tandf-osullivan-scaling-expertise-genai.md): governance that needs persistent state can't be done by prompting alone; GenAI drifts and flatters (independent) (competitive-teardown-stripe-knowledge-agents)
- [Knowledge activation with curated skills](sources/arxiv-yahoo-knowledge-activation-skills.md): 87 curated skills saved 2.6 h/week; contribution barriers, authoring cost and unmeasured staleness (first-party) (competitive-teardown-stripe-knowledge-agents)
- [AI-generated table documentation](sources/databricks-ai-generated-table-documentation.md): agent drafts, owner accepts or edits: '>80%' of metadata updates AI-assisted (vendor claim) (competitive-teardown-stripe-knowledge-agents)
- [Generative AI at Work](sources/nber-brynjolfsson-generative-ai-at-work.md): an assistant trained on top performers' work exhaust raised productivity 14% overall, 34% for novices, about 0 for experts (independent, causal) (competitive-teardown-stripe-knowledge-agents)
- [LLMs reduce public knowledge sharing](sources/pnas-nexus-llms-reduce-public-knowledge-sharing.md): Stack Overflow posting fell ~25% within six months of ChatGPT: people stop writing knowledge down once they can ask an AI (independent) (competitive-teardown-stripe-knowledge-agents)
- [Knowledge hiding meta-analysis](sources/ebr-knowledge-hiding-meta-analysis.md): 131 studies, 47,348 people: knowledge hiding is distinct from (uncorrelated with) sharing, so easier sharing won't fix it (independent) (competitive-teardown-stripe-knowledge-agents)
- [Copilot and works councils (Microsoft Inside Track)](sources/microsoft-insidetrack-copilot-works-councils.md): works councils objected to features that rank or monitor employees; staged rollout (first-party) (competitive-teardown-stripe-knowledge-agents)
- [Resolution extraction from Slack vs tickets](sources/neurips-2025-resolution-extraction-slack-vs-tickets.md): knowledge mined from Slack is more relevant but noisier; needs high-precision filtering (independent) (competitive-teardown-stripe-knowledge-agents)
- [Expertise estimation from Slack](sources/arxiv-watanabe-expertise-estimation-slack.md): 'who knows what' inferred from 27k Slack messages had a best error of 21 points out of 100 (independent) (competitive-teardown-stripe-knowledge-agents)
- [Encoding Your Domain Expert (Spotify Vedder)](sources/spotify-engineering-vedder-context-layer.md): experts own clusters of datasets, vetted question-SQL pairs and docs; curators rejected 87.5% of examples auto-generated from query history as noise; clusters carry a health score (first-party) (competitive-teardown-stripe-knowledge-agents)
- [Intercom Fin NPI](sources/intercom-fin-npi-agent-readiness.md): a feature counts as shipped only when the support agent can answer about it; a 'what we built' doc plus meeting notes go to an agent that drafts and tests content (first-party) (competitive-teardown-stripe-knowledge-agents)
- [Uber Agentic Pods (CTO post)](sources/x-praveen-uber-agentic-pods.md): engineers shadow domain experts for two days before building, because workflows can't be automated 'by looking at process diagrams or documentation' (first-party) (competitive-teardown-stripe-knowledge-agents)
- [Internal AI tools for non-engineers (DoP PDF)](sources/departmentofproduct-internal-ai-tools-for-non-engineers.md): a 15-company table; three rows (Spotify, Intercom, Uber) are capture mechanisms (independent summary) (competitive-teardown-stripe-knowledge-agents)

## opportunity-to-code-chain: Opportunity → problem → goal → intent → plan → code
A stage chain for product work, drawn by a Stripe engineer, in which agents today own the lower stages (intent research, plan, code, review) and people own the upper ones (opportunity, problem, goal) through customer conversations. It gives the strategy a spine: where each agent sits, where hand-offs and artifacts are, and where captured context must feed in.
- [An Inside Look Into How This $159B Tech Company Ships So Fast](sources/youtube-notmybusiness-inside-stripe-ships-fast.md): whiteboard at ~12:24 reads Opportunity → Problem → Goal → Intent → Plan, with a brace over Problem and Goal labelled (partly legible) "Customer conv…"; "This is the part that today is happening a lot more in Orbit now"; the plan is then handed to a minion to code (competitive-teardown-stripe-knowledge-agents)
- [Building and Accelerating the Intent Factory](sources/geoff-building-accelerating-intent-factory.md): Geoff's eight-step Stripe/Ramp loop starts at informal intent and runs to staged release; Stripe's chain adds the three human stages above intent (opportunity, problem, goal) that the loop leaves implicit (competitive-teardown-stripe-knowledge-agents)
- [Stripe's Internal Agent Ecosystem for Product Development](sources/claude-doc-geoff-stripe-internal-agent-ecosystem.md): Geoff's flow maps Kai (research), Harbor/Protodash (prototype), Orbit (plan), Minions (build), review agent plus human onto the same chain (competitive-teardown-stripe-knowledge-agents)
- [AI didn't write our SDK. It changed how we built it.](sources/stripe-ai-didnt-write-our-sdk.md): between intent and code, agents draft specs that humans review as GitHub issues before implementation (competitive-teardown-stripe-knowledge-agents)
- [Intercom Fin NPI](sources/intercom-fin-npi-agent-readiness.md): adds a step after code: shipped work is written back into the agent's knowledge, tested, and monitored for 2-4 weeks (first-party) (competitive-teardown-stripe-knowledge-agents)
