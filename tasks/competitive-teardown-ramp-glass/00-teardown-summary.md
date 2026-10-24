# Teardown: Ramp Glass (summary)

Date: 2026-10-24, audited the same day (see [audit-2026-10-24.md](audit-2026-10-24.md)). Worker draft for Geoff's review.

Source notes live in the research library (`../../research/sources/`). Primary: [launch video](../../research/sources/ramp-introducing-glass.md), [Goddijn article](../../research/sources/x-sebgoddijn-glass-article.md), [Buchan build story](../../research/sources/x-shanebuchan-how-we-built-glass.md), [Charles "AI pilled"](../../research/sources/x-geoffintech-ai-pilled-article.md), [Glyman launch article](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md), [Ramp "Building Laminar"](../../research/sources/ramp-builders-building-laminar.md), [Charles on the Lenny's channel](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md), [Pragmatic Summit talk](../../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md), [Router launch posts](../../research/sources/x-ramp-router-launch-posts.md), [Notion video](../../research/sources/notion-inside-ramps-custom-agent-os.md). Independent: [The New Stack on Laminar](../../research/sources/thenewstack-ramp-laminar-agent-harness.md) (which itself relies on Ramp's post). The sourced X-post list is [06-x-posts-ramp-leaders-about-glass.md](06-x-posts-ramp-leaders-about-glass.md).

**Evidence status, up front.** Every number below is Ramp's own (employees, founders, company accounts). No customer, analyst or benchmark has verified any of it. The architecture descriptions come from the builders and are specific enough to be credible; the outcome numbers are marketing.

## What Glass is

A company-wide AI "coworker" workspace that Ramp built for its own employees from early 2026 and opened to outside companies in early access on 2026-10-13 (ramp.com/glass; "onboarding the first businesses personally"; no public pricing found). Tagline: "AI made every employee faster. Glass makes the entire company smarter." Glyman's framing: "We learn things once." A Ramp CTO post (Oct 20) calls it "glass - general purpose coworker", one of two products on "a single set of rails" with Stack, the accounting harness.

**Form factor changed between April and October, and the sources disagree accordingly.**
- April 2026 (Goddijn, Buchan, Charles): a desktop app installed on managed laptops, Okta SSO, built on Anthropic's Claude Agent SDK ("our own version of Claude Code's Cowork"), with MCP connections and scheduled automations running on the laptop ("turns your laptop into a server").
- October 2026 (Kronick, "Building Laminar"): Glass runs on Laminar, Ramp's own provider-agnostic harness, on "a fleet of generic disposable workers" in the cloud, with "Web + desktop" clients; the laptop-as-server era is called "a weird blip". Ramp Router is the LLM gateway ("Any model. Open or closed." in the launch article).
Treat April statements about where Glass runs and what SDK it uses as historical.

**Timeline (Ramp's accounts; dates partly inferred).** Weekend prototype by Jay Sobel (roughly Jan 2026, inferred from "a month later" and "within a few weeks" in Buchan's Apr 15 article) → Seb Goddijn builds it out, ~20 daily users → core team of 3 (Buchan: Goddijn, Buchan, Leavenworth) or 4 (Charles) → internal launch by about Feb–Mar 2026 (Charles on Apr 8: "700 daily active users within a month of launch") → public X articles Apr 8–15 → Ramp decides ~May 2026 to build Laminar; v1 in six weeks → Router launched externally Jul 20 → Glass external launch Oct 13 → Laminar post Oct 20. Glyman's launch article says a "$1.5 million" token week "in May" prompted "a small team" to build Glass "within weeks"; that cannot be the origin story, because Glass had 700 daily users before April and his own article has an account manager saving prompts to Glass "in May". Either the week was May 2025 or the story is compressed for effect. Unresolved.

## How it works (as described by Ramp)

- **Day-one connectivity.** One Okta SSO sign-in; 30+ tools pre-connected (Salesforce, Snowflake, Gong, Slack, Notion, Google Workspace, Figma, Linear, Datadog…) via centrally configured MCP; internal CLIs bundled (Ramp CLI, Research, Inspect). In the April desktop design, a proxy connected to each service once at app launch and shared the connection across sessions (startup ~45 s → ~2 s); integrations self-heal with plain-language re-auth. In Laminar, a central Connectors Service owns auth, credentials, access control and tool execution.
- **Skills and Dojo.** Skills are markdown files. Dojo is a Git-backed marketplace; "publish" creates the branch, PR and review invisibly so non-engineers never see Git. 350+ skills claimed. A recommender ("Sensei") suggests skills by role, connected tools and recent work.
- **Memory.** Built on first open from the user's authenticated connections; a 24-hour pipeline re-mines past sessions plus Slack/Notion/Calendar and rewrites memory files; the agent reads memory at session start and never edits it mid-conversation, so what it knows is inspectable (April design; not re-described in the Laminar post).
- **Shared company knowledge.** "323 employees … 6,500+ edits to what Glass knows" (Glyman); Finance taught it to exclude US firms with UK offices from "UK customers".
- **Automation and long-running work.** Scheduled/cron automations posting to Slack; Slack-native assistants using the user's full setup; headless runs with approvals from a phone (April). In Laminar: non-blocking async agents by default, sessions "always open to new input", human-in-the-loop approvals, steering, subagents, sandboxes and cloud browsers, tasks "that can take minutes or hours".
- **Workspace UI.** Split panes and tabs like an editor; inline rendering of markdown/HTML/CSV/images/code; layout persists.
- **Multiplayer.** Share a session with a teammate (support agent hands a ticket session to an engineer).
- **Cost control.** Per-project cost "meter, like a taxi"; limits set before they are crossed; finance visibility; every request through Ramp Router.
- **Under the hood (Laminar).** FastAPI, SSE streaming, Temporal for durable orchestration, Postgres for sessions/messages, S3, worker fleet, "sandbox-as-a-tool" (session lifetime decoupled from sandbox lifetime), own trace-debugging UI.

## Harness and agent design choices worth studying (not copying)

1. **The harness is the product.** "The models are good enough, the harness isn't" (Goddijn). Preconfigured integrations, skills and memory were what moved stuck users, not a better model.
2. **Full capability, hidden complexity.** Non-technical users keep multi-window, scheduling, memory, skills; the product hides setup rather than removing power.
3. **Organisational learning as a loop.** One person's skill, prompt or correction becomes the team default (Dojo; shared knowledge edits). "The product is the enablement": skills double as lessons.
4. **Skills as markdown in Git, with Git hidden** behind publish/published.
5. **Memory as inspectable files from an offline pipeline, read-only in session.**
6. **Cost routing and metering inside the harness** (Router as gateway; per-project meter). Note the sequence: April "kill token limits", then metering after spend ballooned.
7. **Own the harness.** Ramp went from vendor SDK (April) to its own harness (Laminar, May–Oct) for provider independence, same-day fixes and owning observability; it says the build cost was "marginal" with coding agents but that on-call engineers are still needed. No cost comparison published.
8. **Cloud-first runtime, thin clients.** Laminar reverses the April local-first design; sessions survive laptops sleeping.
9. **Async, always-open sessions with human approvals**, multiplayer and Slack as a first-class client.
10. **Self-maintaining agent-written codebases.** April (Buchan): Defrag skill, design system, doc validation, pre-commit gates, "vibe coded". October (Kronick): agent-generated but architecture-reviewed by a small senior team; "'vibe coded' doesn't capture what we've built".
11. **One agent, many skills.** The March Pragmatic Summit talk: teams had built four versions of the same agent; the direction is "a single agent with a thousand skills". Glass fits that; the talk does not name Glass.

## The wider Ramp system around Glass

- **Charles's "software factory"** (talk on the Lenny's Podcast channel, Sep 2026): Glass is the *define* step (connected to Snowflake, research, strategy, specs, design system, codebase; "AI is your tech lead"), alongside Inspect (coding; "75% of our PRs", "a million sessions", ~1,000 PRs/month from non-engineers), Review Buddy ("93% of our PRs"), Testo (browser QA; 425 bugs in 30 days), Gadget (org Q&A; "85% of questions asked to PMs"), and autonomous small loops ("60% of UX issues … fixed within 24 hours"). Principle: "the organization needs to be legible to your agents".
- **Pragmatic Summit** (Mar 2026, Ramp engineers): applied-AI service (LLM proxy with config-swap models, batching, per-team cost tracing), shared tool catalog ("many hundreds"), OmniChat, Policy Agent (suggestions → autonomy slider; weekly labelling; evals that started with five examples), Inspect (Modal sandboxes, multiplayer-first, >50% of merged PRs then). Glass is not mentioned.
- **Laminar** (Oct 2026) now sits under all of these: support chat, headless OCR, Inspect, Stack, Glass.
- **Notion video** (Feb 2026, vendor-made): Ramp's earlier layer of Notion custom agents (Slack Q&A bots, "enablement Eddie", feedback triage).

## Claims vs. evidence

| Claim | Who | Status |
|---|---|---|
| 99% (Goddijn, Glyman) / 99.5% (Charles) of Ramp uses AI daily | Ramp | Self-reported; "uses" undefined; usage is mandated and leaderboarded, which may inflate it. |
| 700 DAU within a month; "used by half the company" | Charles, Buchan | Self-reported, April. |
| Feature requests 300/month → 20,000/month; 5,000+ customer emails | Glyman, Atiyeh | Self-reported. "Captured" is a count, not quality or impact; it is one saved prompt plus Gong access, not Glass-specific. |
| "Our bill fell 30% overnight" | Glyman (Oct) | Repeats Ramp's Router launch claim (Jul 20, 2026: "30% … without any performance degradation", Zaks). No data published; a secondary outlet quotes 40%. Not a Glass result. |
| $1.5M token week in May as the trigger for Glass | Glyman | Chronology conflicts with Ramp's own April articles and with his own text; unresolved. |
| Built by 3 (Buchan) / 4 (Charles) in <3 months / "about a month" | Charles, Buchan | Internally inconsistent; plausible for a v1. |
| Laminar v1 in six weeks; every agentic product on it after five months; "tens of millions of sessions" | Kronick; daily.dev summary | Self-reported; the sessions figure is from a summary, not seen in the post. |
| 350+ skills; 323 employees; 6,500+ edits | Goddijn, Glyman | Counts only; no reuse or quality data. |
| "AI usage up 6,300%"; "revenue growth accelerated four quarters in a row" | Charles, Glyman | Not tied to Glass; correlation at best. |
| Customer value outside Ramp | — | None yet: early access, no named customers, no pricing. |
| Launch-video testimonials (financial model "single button", conversion "improved drastically") | Ramp video | Anonymous in captions, no numbers. |

## Limits of this teardown

- Transcripts are YouTube auto-captions only (no human captions exist for any of the four videos); coverage is complete by timing, but names and product terms are unreliable ("Brazilian agents", "Cloud Code", speaker names "Viral/Vimal").
- X coverage is from web search plus page reads, not timelines (login wall). Authors' replies and some post ids (Ramptables, rahul's rails thread, Patel's Router thread) were not retrieved; no posts by Sobel, Kipperman, Leavenworth, Horn or Kronick surfaced.
- Not read: Laminar's four deep-dive posts (Tools, Sandboxes, Connectors, Developer Experience), Ramp's "Agentic identity" and token-spend posts, the Ramptables video, open-inspect, third-party teardowns.
- Goddijn's X bio now reads "prev created Glass @tryramp" (search snippet, unverified): the lead builder appears to have left.
- Nothing here comes from using Glass.

## Options by dimension

Glass is one data point on the menu, not a pattern to copy. Its design choices are filed as option/evidence rows and key questions in [options/DIMENSIONS.md](../../options/DIMENSIONS.md) (consolidated structure as of 2026-10-24):

- [loop-source](../../options/DIMENSIONS.md#loop-source-who-supplies-the-agent-loop): embed a vendor SDK (Glass, April) → own harness (Laminar, October). Question: at what scale or need does an org outgrow the vendor SDK, and can the switch be designed in?
- [harness-upkeep](../../options/DIMENSIONS.md#harness-upkeep-who-maintains-the-harness-over-time-and-at-what-cadence): Ramp's own caveat about on-call engineers; no cost comparison.
- [model-provider-coupling](../../options/DIMENSIONS.md#model-provider-coupling-how-tightly-the-agent-is-coupled-to-one-model-provider): provider-agnostic harness plus Router.
- [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives): laptop-as-server (April) vs cloud worker fleet with thin clients (October).
- [capability-format-portability](../../options/DIMENSIONS.md#capability-format-portability-capability-format-and-portability) and [capability-distribution-trust](../../options/DIMENSIONS.md#capability-distribution-trust-capability-distribution-and-trust): markdown skills; Git-backed marketplace with hidden Git; shared tool catalog. Question: how much of the 350+ is reused?
- [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff) and [durability-substrate](../../options/DIMENSIONS.md#durability-substrate-how-persistence-and-recovery-are-implemented): shared sessions, async always-open sessions, Postgres/Temporal/S3, sessions decoupled from sandboxes.
- [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation): SSO plus central connectors.
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-governance-and-control-plane-policy-cost-audit): per-project meter plus Router; the 30% figure is a Router claim.
- [context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory): offline-built read-only memory; user-edited shared knowledge.
- [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent): one agent, many skills; Glass as the define-stage agent in a chain.
- [review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy): Policy Agent's autonomy slider and labelled evals.
- [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model): product-led enablement vs mandates, leaderboards and a proficiency ladder.

Cross-cutting question added: Ramp changed its answers on loop-source and runtime-location within six months; the resource request should fund a path that can be revisited, not a one-time pick.

## Pattern classes

Added 2026-10-24 by teardowns-to-pattern-classes. This summary's examples are placed in the runtime pattern classes P1-P10 of the [taxonomy synthesis, B.2](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes). Every placement is sourced and marked clear, partial or contested in [the mapping, section 2.1](../teardowns-to-pattern-classes/00-mapping.md).

- **P2 then P3:** Glass ran on the Claude Agent SDK in April 2026 (P2, clear, historical). By October 2026 it runs on Laminar, Ramp's own provider-agnostic harness, which also runs Inspect and Stack (P3, clear, first-party).
- **P7 and P8:** Glass and Inspect are background, shareable sessions (clear).
- **P10:** Dojo and the shared tool catalog are internal skill and tool registries (partial: internal, not portable).
- **P4, P5 and P9:** OCA is a partial P4 (a DIY coordinator over Claude Code or Codex) and a partial P9 (Temporal). Glass in its October form matching P5 is contested.
- **Evidence:** all Ramp first-party.
