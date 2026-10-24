# Theme evidence: competitive-teardown-ramp-glass

Written only by the task `competitive-teardown-ramp-glass`. Built into ../THEMES.md by ../build.py.

## harness-over-model: The harness, not the model, limits real-world value
Ramp found models were good enough; the preconfigured environment (integrations, skills, memory, UX) decided whether non-experts got value. Central to what a "product agent and harness" is. Related: [[compounding-context-repo]].
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): "The Models are Good Enough, The Harness Isn't"; 99% adoption but most stuck (§intro) (competitive-teardown-ramp-glass)
- [How to get your company AI pilled](sources/x-geoffintech-ai-pilled-article.md): same finding framed as lesson 6, "the harness wasn't" (competitive-teardown-ramp-glass)
- [Ramp built an AI agent harness in six weeks](sources/thenewstack-ramp-laminar-agent-harness.md): the harness (sessions, sandboxes, connectors, observability, routing) is what Ramp chose to own; models stay swappable (competitive-teardown-ramp-glass)
- [Building Laminar: Ramp's Managed Agents Platform](sources/ramp-builders-building-laminar.md): the harness's 15 responsibilities listed; provider-agnostic; own trace-debug UI (competitive-teardown-ramp-glass)

## org-learning-loop: One person's win becomes everyone's baseline
Skills, prompts and corrections made by one employee propagate to the team so the organisation learns once. Overlaps with [[compounding-context-repo]] (product context) but is about workflow/skills and shared sessions.
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): principle 2 and Dojo, 350+ skills (competitive-teardown-ramp-glass)
- [Introducing Glass: Learn Things Once.](sources/x-eglyman-introducing-glass-learn-things-once.md): 323 employees, 6,500+ edits to what Glass knows; Finance taught it the UK-customer rule (competitive-teardown-ramp-glass)
- [Introducing Glass. Make your entire company smarter](sources/ramp-introducing-glass.md): shareable sessions, 0:48-1:01 (competitive-teardown-ramp-glass)
- [How to get your company AI pilled](sources/x-geoffintech-ai-pilled-article.md): L0-L3 ladder, leaderboards, center + spokes (competitive-teardown-ramp-glass)
- [Inside Ramp's Custom Agent Operating System](sources/notion-inside-ramps-custom-agent-os.md): pre-Glass layer; sales feedback piped into Notion and triaged to the roadmap by agents (0:40-1:20) (competitive-teardown-ramp-glass)
- [Eric Glyman April 2026 posts on Glass and AI adoption](sources/x-eglyman-april-glass-posts.md): "when one person on a team figures out a better workflow, everyone on that team gets it" (competitive-teardown-ramp-glass)
- [Today, we're launching Glass (Geoff Charles X post)](sources/x-geoffintech-glass-launch.md): "Adoption, it turns out, is the easy part. The hard part is making AI work compound." (competitive-teardown-ramp-glass)
- [Introducing Glass (Ramp X post)](sources/x-tryramp-introducing-glass.md): tagline contrasts individual speed with company-level learning (competitive-teardown-ramp-glass)
- [Other Ramp (@tryramp) posts about Glass, Apr-May 2026](sources/x-tryramp-other-glass-posts.md): company-account amplification; Ramptables episode on the Glass builders (competitive-teardown-ramp-glass)

## skills-marketplace: A versioned skills marketplace with hidden Git
Skills as markdown in a Git repo, reviewed like code, with the VCS hidden from non-engineers behind publish. A concrete mechanism for sharing agent know-how.
- [How We Built Glass: Vibe Coding a Product Used by 700 People](sources/x-shanebuchan-how-we-built-glass.md): Dojo publish = branch + PR + review behind the scenes (competitive-teardown-ramp-glass)
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): Dojo plus the Sensei recommender (competitive-teardown-ramp-glass)

## memory-architecture: Memory as inspectable files from an offline pipeline
Agent memory built on first connection, refreshed by a periodic pipeline, read-only during sessions.
- [How We Built Glass: Vibe Coding a Product Used by 700 People](sources/x-shanebuchan-how-we-built-glass.md): 24h pipeline, write-once-read-many memory files (competitive-teardown-ramp-glass)
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): memory built from authenticated connections, 24h synthesis and cleanup (competitive-teardown-ramp-glass)

## cost-control-routing: Cost metering and model routing built into the harness
Open access to frontier models blew budgets; Ramp added per-project meters, limits and a router that picks the model.
- [Introducing Glass: Learn Things Once.](sources/x-eglyman-introducing-glass-learn-things-once.md): $1.5M week, taxi meter, Ramp Router, 30% drop claimed (competitive-teardown-ramp-glass)
- [Ramp: Lessons from Building a New AI Product - The Pragmatic Summit](sources/pragmatic-engineer-ramp-lessons-new-ai-product.md): LLM proxy with per-team cost tracing and config-only model swaps (competitive-teardown-ramp-glass)
- [Introducing Glass. Make your entire company smarter](sources/ramp-introducing-glass.md): budget blown in weeks; users default to frontier models (competitive-teardown-ramp-glass)
- [How to get your company AI pilled](sources/x-geoffintech-ai-pilled-article.md): the opposite stance in April: "Kill token limits and access restrictions", "treat AI usage as an infinite learning budget"; metering came later with Router/Glass (competitive-teardown-ramp-glass)
- [Ramp Router launch posts (Jul 20, 2026)](sources/x-ramp-router-launch-posts.md): the 30% bill cut is a Router claim from July 2026, 'without any performance degradation' (Zaks); no published data (competitive-teardown-ramp-glass)
- [Ramp built an AI agent harness in six weeks](sources/thenewstack-ramp-laminar-agent-harness.md): independent data point on in-harness routing, LangChain Open SWE -64% median cost/thread, no significant quality change (competitive-teardown-ramp-glass)
- [Building Laminar: Ramp's Managed Agents Platform](sources/ramp-builders-building-laminar.md): Ramp Router sits in the harness as the LLM gateway; model choice per cost/latency/performance (competitive-teardown-ramp-glass)

## single-agent-many-skills: One agent with many skills, not many agents
Consolidate to one agent and one conversational surface, extended by skills and tools.
- [Ramp: Lessons from Building a New AI Product - The Pragmatic Summit](sources/pragmatic-engineer-ramp-lessons-new-ai-product.md): "single agent with a thousand skills"; OmniChat (competitive-teardown-ramp-glass)
- [Introducing Glass. Make your entire company smarter](sources/ramp-introducing-glass.md): "one single agent" with pre-built connectivity (competitive-teardown-ramp-glass)

## enablement-by-product: The product is the enablement
Teach users by what the product does (suggested skills, memory, self-healing) rather than training.
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): principle 3; "every feature is secretly a lesson" (competitive-teardown-ramp-glass)
- [Introducing Glass: Learn Things Once.](sources/x-eglyman-introducing-glass-learn-things-once.md): feature-request prompt example (competitive-teardown-ramp-glass)
- [Karim Atiyeh Glass launch post](sources/x-karimatiyeh-glass-feature-requests.md): an account manager's saved prompt took feature-request capture from ~300 to ~20,000 a month (vendor claim) (competitive-teardown-ramp-glass)

## build-vs-buy: Own the agent harness as a moat
Reasons to build internally: moat, speed of fixes, learning for the external product.
- [We Built Every Employee at Ramp Their Own AI Coworker](sources/x-sebgoddijn-glass-article.md): three reasons (competitive-teardown-ramp-glass)
- [Eric Glyman April 2026 posts on Glass and AI adoption](sources/x-eglyman-april-glass-posts.md): "we decided to own it" (competitive-teardown-ramp-glass)
- [How We Built Glass: Vibe Coding a Product Used by 700 People](sources/x-shanebuchan-how-we-built-glass.md): a 3-person team, vibe-coded (competitive-teardown-ramp-glass)
- [Introducing Glass: Learn Things Once.](sources/x-eglyman-introducing-glass-learn-things-once.md): "as is often the case at Ramp, a small team built something"; now sold externally as a product, so the build also became a revenue line (vendor claim) (competitive-teardown-ramp-glass)
- [How to get your company AI pilled](sources/x-geoffintech-ai-pilled-article.md): "our own version of Claude Code's Cowork, built on Anthropic's Claude Agent SDK"; "a team of four built it in under three months" (competitive-teardown-ramp-glass)
- [Ramp built an AI agent harness in six weeks](sources/thenewstack-ramp-laminar-agent-harness.md): Ramp replaced vendor SDKs with its own harness Laminar (six-week V1, now under Glass and Inspect) after testing Claude Agent SDK, Claude Managed Agents, OpenAI Agents SDK, OpenCode, LangChain, Sierra; no cost comparison published (competitive-teardown-ramp-glass)
- [Building Laminar: Ramp's Managed Agents Platform](sources/ramp-builders-building-laminar.md): Ramp built its own harness (~May 2026, v1 in six weeks) after trying vendor SDKs, managed-agent APIs and frameworks; 'you still need good engineers to be on-call' (competitive-teardown-ramp-glass)

## non-engineer-builders: Non-engineers ship through agents
Product, CX, finance and sales build tools and PRs via agent harnesses; shifts who builds.
- [How to get your company AI pilled](sources/x-geoffintech-ai-pilled-article.md): 12% of human PRs, 1,500+ apps, 800+ builders (competitive-teardown-ramp-glass)
- [What product looks like when coding is solved | Geoff Charles (Ramp CPO)](sources/lenny-podcast-geoff-charles-product-when-coding-solved.md): ~1,000 non-engineer PRs/month via Inspect (competitive-teardown-ramp-glass)
- [Ramp: Lessons from Building a New AI Product - The Pragmatic Summit](sources/pragmatic-engineer-ramp-lessons-new-ai-product.md): PM vibe-coded ~20 tools (competitive-teardown-ramp-glass)
- [Inside Ramp's Custom Agent Operating System](sources/notion-inside-ramps-custom-agent-os.md): "turning everybody at Ramp into a builder" (competitive-teardown-ramp-glass)

## agent-factory-sdlc: Agents across the whole product development loop
A chain of specialised agents (insight, define, build, review, test, coordinate) removes bottlenecks one after another; Glass is the define-stage agent. Related: [[intent-factory-before-discovery]].
- [What product looks like when coding is solved | Geoff Charles (Ramp CPO)](sources/lenny-podcast-geoff-charles-product-when-coding-solved.md): Glass/Inspect/Review Buddy/Testo/Gadget loop (competitive-teardown-ramp-glass)
- [How We Built Glass: Vibe Coding a Product Used by 700 People](sources/x-shanebuchan-how-we-built-glass.md): Glass builds Glass with Defrag, doc validation, gates (competitive-teardown-ramp-glass)
- [Ramp built an AI agent harness in six weeks](sources/thenewstack-ramp-laminar-agent-harness.md): one harness under customer-service agents, Inspect and Glass (competitive-teardown-ramp-glass)
- [Building Laminar: Ramp's Managed Agents Platform](sources/ramp-builders-building-laminar.md): one harness for support chat, headless OCR, Inspect, Stack and Glass (competitive-teardown-ramp-glass)

## legible-org-for-agents: Make the organisation legible to agents
Roadmaps, specs, tickets and tools must be agent-readable so agents can answer and act. Related: [[compounding-context-repo]].
- [What product looks like when coding is solved | Geoff Charles (Ramp CPO)](sources/lenny-podcast-geoff-charles-product-when-coding-solved.md): "the organization needs to be legible to your agents"; Gadget (competitive-teardown-ramp-glass)
- [Ramp: Lessons from Building a New AI Product - The Pragmatic Summit](sources/pragmatic-engineer-ramp-lessons-new-ai-product.md): shared internal tool catalog of hundreds of tools (competitive-teardown-ramp-glass)

## evals-autonomy-trust: Evals, autonomy sliders and earned trust
Start agents as suggestions, measure against ground truth, then let users raise autonomy. Related: [[risk-sloped-review]].
- [Ramp: Lessons from Building a New AI Product - The Pragmatic Summit](sources/pragmatic-engineer-ramp-lessons-new-ai-product.md): Policy Agent suggestions -> auto-approve slider; weekly labeling; evals from five examples (competitive-teardown-ramp-glass)
- [What product looks like when coding is solved | Geoff Charles (Ramp CPO)](sources/lenny-podcast-geoff-charles-product-when-coding-solved.md): autonomous small loops, Review Buddy 93%, Testo 425 bugs (competitive-teardown-ramp-glass)

## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Building Laminar: Ramp's Managed Agents Platform](sources/ramp-builders-building-laminar.md): async-by-default, always-open sessions with HITL approvals, steering and multiplayer; session state in Postgres decoupled from sandboxes; cloud workers so 'laptop goes to sleep' no longer matters (first-party) (competitive-teardown-ramp-glass)
