# Intercom's agent ecosystem, mapped to the tasks of the product lifecycle

Date: 2026-10-24. Same frame as the [Stripe map](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md): rows are tasks, not job titles; each handoff is marked **documented** (an Intercom source says it happens), **inferred** (consistent with the sources but not stated) or **unknown**. Built only from filed notes in `../../research/sources/`. Visual version: [04-pdlc-agent-ecosystem-map.html](04-pdlc-agent-ecosystem-map.html).

**Evidence caveat.** Almost every source is Intercom's own (its Substack ideas.fin.ai, its blog, its CTO's webinar answers, its CEO on a podcast). Intercom sells Fin and an AI-native engineering story, so these are first-party and self-reported; no independent account of Intercom's process was found (one paywalled interview aside).

## Why tasks, not job titles, at Intercom too

- **Engineers take on product work; PM and design move toward customers.** The CTO says strong engineers take on more PM work, while PM and design focus on "higher ambiguity" work near customers and go-to-market, and designers ship small fixes and prototypes ([webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md), first-party, May 2026).
- **Designers work in code.** "Our designers are now primarily working in code"; Figma is "more like a whiteboard" ([design director](../../research/sources/ideas-fin-how-we-design-when-code-writes-itself.md), first-party, Mar 2026).
- **Everyone has the same harness.** About 1,000 non-engineers, PMs included, were given Claude Code; nearly 1,100 of 1,305 employees were active users at peak ([Yakovenko](../../research/sources/intercom-we-gave-claude-code-to-everyone.md); [CTO, 2x nine months later](../../research/sources/ideas-fin-2x-nine-months-later.md), both first-party).
- **Researchers and data scientists build.** Intercom's research and data science team pulls its own data and makes product changes directly ([Church](../../research/sources/ideas-fin-nobody-changed-their-title.md), first-party, Jul 2026).

## The short answer: where context breaks

**Intercom has made intent travel well downstream of the plan, and left it to people upstream.**

1. **Downstream, the "why" is written down and checked.** A hook forces a create-pr skill that asks *why* the change exists and puts the answer in the PR description ([Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md)); review agents check that the diff matches that stated intent ([AI approving PRs](../../research/sources/intercom-ai-approving-pull-requests.md)); at launch a "what we built" doc feeds the support agent's readiness gate ([Fin NPI](../../research/sources/intercom-fin-npi-agent-readiness.md)).
2. **Upstream, no source describes a handoff from research to intent or plan.** The research team's syntheses live in sessions, reports and a queryable interview skill; no source says how they reach the designers, PMs or engineers who shape and plan the work ([Church](../../research/sources/ideas-fin-nobody-changed-their-title.md)).
3. **The plan itself is not an artifact.** Engineers spend 5–20 plan-mode turns in Claude Code before building, with no formal spec; the plan lives in the session ([Walker](../../research/sources/ideas-fin-what-were-learning-from-engineers.md), anecdote). Intent is re-captured only at PR time.
4. **Fin's customer data is not shown feeding Intercom's own roadmap.** Fin Insights is a product for customers; no source says Intercom's product teams use it to decide what to build ([Fin Insights](../../research/sources/ideas-fin-working-with-a-black-box-fin-insights.md)).

**Across people:** like Stripe, Intercom shrinks the problem by collapsing roles (engineers doing PM work, designers coding), so context often stays in one person's head and session. Where research, shaping and planning still sit with different people (the research team, designers, engineers), the break is unrecorded: research → intent → plan is carried by people, and the first durable statement of intent is the PR description.

## The lifecycle, task by task

Row names follow the Stripe map. No rows were added; two Intercom specifics are placed inside existing rows: **QA sessions** (a human QA session turned into GitHub issues) under *Review the change*, and **support-agent readiness** (Fin NPI) under *Release*, because Intercom treats it as a release gate.

| Task | Who does it at Intercom (roles seen) | Agents and tools | Artifact produced | Evidence |
|---|---|---|---|---|
| **Spot the opportunity** | Leadership, top-down: the CEO narrowed the company to customer service and bet on AI | None named | Not described | [McCabe](../../research/sources/lenny-podcast-mccabe-intercom-ai-bet.md) (first-party, Aug 2025; company-level only) |
| **Talk to customers** | Research and data science (RAD) researchers | AI-moderated interviews for churn studies, pilots and well-defined topics (tool not named); early discovery and current customers stay human | Interview transcripts; a 60+ interview study turned into a queryable skill | [Bridi](../../research/sources/ideas-fin-talk-to-the-bot-ai-interviewer.md); [Church](../../research/sources/ideas-fin-nobody-changed-their-title.md) (first-party) |
| **Research the problem, read the data** | Researchers, data scientists, PMs, sales reps | Claude Code with Claude4Data (30+ analytics skills) and guidance skills for company metrics; Cockpit (LLM clustering of customer feedback); sources: sales calls, win/loss, churn surveys, Salesforce, Slack | HTML reports, Snowflake/Streamlit reports with access control, daily win/loss feed, fortnightly leadership deal briefing | [Church](../../research/sources/ideas-fin-nobody-changed-their-title.md); [Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md); [Yakovenko](../../research/sources/intercom-we-gave-claude-code-to-everyone.md); [CTO](../../research/sources/ideas-fin-2x-nine-months-later.md) (first-party) |
| **Set the goal** | Not described (the CTO names company measures: release throughput, idea-to-release time) | None named | Not described | [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md) |
| **Shape the intent: prototype, spec** | Designers (primarily in code), PMs; work "closer to customers" | Claude Code prototypes on production components and live data; Surge design system and playground; "vibe" prototypes, then structured specs for edge cases; Figma as whiteboard | Prototypes (the "new wireframe"); "tighter briefs"; no PRD or brief template found | [Moriarty](../../research/sources/ideas-fin-how-we-design-when-code-writes-itself.md); [Mahar](../../research/sources/ideas-fin-to-vibe-code-or-not.md) (first-party) |
| **Plan the change** | Engineers, who "take responsibility for the shape of the solution" | Claude Code plan mode: 5–20 turns before building | A plan held in the session; not persisted | [Walker](../../research/sources/ideas-fin-what-were-learning-from-engineers.md) (anecdote); [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md) |
| **Write the code** | Engineers; also designers, PMs and TPMs | Claude Code (single primary tool): 13 plugins, 267 skills from 153 contributors, MDM-installed; React and migration skills; cloud agents ("Buzz") a small share; ~93–94% of PRs agent-driven | Pull request whose description states *why* (create-pr skill, hook-enforced) | [Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md); [skills post](../../research/sources/ideas-fin-claude-code-good-skills-bad-skills.md); [de Róiste](../../research/sources/ideas-fin-eight-people-hold-the-bar.md); [CTO](../../research/sources/ideas-fin-2x-nine-months-later.md); [Lenny/How I AI](../../research/sources/lenny-newsletter-how-intercom-2xd-engineering.md) (anecdote) |
| **Review the change** | A person on about 80% of PRs; repo owners set review requirements | "Shrek": specialised review sub-agents (Claude and Codex) in short-lived containers, triggered by GitHub webhooks, with their own evals; ~19% of PRs auto-approved by risk and size; a background agent watches CI. QA sessions: video-transcript and QA follow-up skills | Approved, labelled and logged PR; GitHub issues from QA | [AI approving PRs](../../research/sources/intercom-ai-approving-pull-requests.md); [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md); [Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md) |
| **Release** | Automated; the shipping engineer owns monitoring and rollback; an NPI manager owns support readiness | Automatic deploys (313 in a day; merge to production ~12 min). Fin's own changes: replayed-conversation tests with AI judges, A/B tests, staged rollout. Support readiness: Operator turns a "what we built" doc into gap analysis, draft articles and FAQ tests | Live change; for launches, updated and tested support content and sign-off | [AI approving PRs](../../research/sources/intercom-ai-approving-pull-requests.md); [CTO](../../research/sources/ideas-fin-2x-nine-months-later.md); [Tabacof](../../research/sources/ideas-fin-why-not-just-ship-it.md); [Fin NPI](../../research/sources/intercom-fin-npi-agent-readiness.md) (first-party) |
| **Operate and learn** | Engineers; support engineers, design managers and PM leaders among top users of the production console | Read-only production console over MCP; incident skill (Honeycomb, Datadog, Snowflake logs); open-ended incident agent still in progress; launch monitors on resolution rate and CX score for 2–4 weeks; SessionEnd hook mines transcripts for missing skills; weekly CLAUDE.md fact-check | Answers; GitHub issues for new skills; updated CLAUDE.md; post-launch support metrics | [Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md); [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md); [Fin NPI](../../research/sources/intercom-fin-npi-agent-readiness.md) |

## Every handoff, task to task

| From task → to task | Mechanism | Status |
|---|---|---|
| Talk to customers → research | Interview studies become a searchable repository with a queryable skill; existing evidence (calls, win/loss) is synthesised first | **documented** ([Church](../../research/sources/ideas-fin-nobody-changed-their-title.md)) |
| **Research → shape intent** | Not described. Reports, the interview skill and Cockpit clusters exist, but no source says how findings reach designers, PMs or engineers | **unknown** |
| Research, spot the opportunity → set the goal | Not described | **unknown** |
| Set the goal → shape intent | People; no tool shown | **inferred** |
| Shape intent (prototype) → plan and build | Prototypes convey intent, interaction and tone; implementation left to engineers; "tighter briefs at the start, fast review cycles, and clear criteria" replace fixed handoffs | **documented** ([Mahar](../../research/sources/ideas-fin-to-vibe-code-or-not.md); [Moriarty](../../research/sources/ideas-fin-how-we-design-when-code-writes-itself.md)) |
| Shape intent → write code, when a designer or PM codes it | The same person uses Claude Code directly; no ticket or spec hop described | **inferred** (from [Moriarty](../../research/sources/ideas-fin-how-we-design-when-code-writes-itself.md), [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md)) |
| Design system → write code | Skills encode Surge/React standards and are auto-installed; agent use of existing components went from 7% to 96% | **documented** ([de Róiste](../../research/sources/ideas-fin-eight-people-hold-the-bar.md)) |
| Plan → write code | Same Claude Code session; the plan stays in session memory | **documented** (anecdote: [Walker](../../research/sources/ideas-fin-what-were-learning-from-engineers.md)) |
| Write code → review | Hook-enforced create-pr skill writes *why* into the PR description; GitHub webhook triggers the Shrek reviewers, which check the diff against that stated intent; a background agent watches CI | **documented** ([Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md); [AI approving PRs](../../research/sources/intercom-ai-approving-pull-requests.md)) |
| QA session → tracked work | Meeting recording → video-transcript skill → QA follow-up skill → GitHub issues | **documented** ([Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md)) |
| Review → release | Auto-approved or human-approved merge triggers automatic deploy; non-approved PRs go to a person with a Slack notice | **documented** ([AI approving PRs](../../research/sources/intercom-ai-approving-pull-requests.md); [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md)) |
| Release → support knowledge (Fin) | PMs and engineers submit a "what we built" doc to the release tracker, plus walkthrough and kick-off notes; Operator drafts content and FAQ tests; the NPI manager signs off | **documented** ([Fin NPI](../../research/sources/intercom-fin-npi-agent-readiness.md)) |
| Operate → harness learning | SessionEnd hook → Haiku classifies gaps → Slack post with a pre-filled GitHub issue → new skills; skills promoted to the base plugin at 50 weekly users; CLAUDE.md fact-checked weekly | **documented** ([Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md); [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md)) |
| **Operate (Fin conversations, Insights) → Intercom's own research and roadmap** | Not described; Fin Insights is documented only as a customer product | **unknown** |

**Counts:** 9 documented (one of them anecdote-level), 2 inferred, 3 unknown.

## Diagram (text)

```
TASK:     Spot        Talk to     Research     Set    Shape intent    Plan        Write      Review       Release        Operate
          opportunity customers   problem      goal   (prototype)     change      code       change                      & learn
HUMANS    ●leaders    ●RAD        ●RAD, PMs,   ●?     ●designers      ●engineers  ●eng + PM, ●~80% of PRs ●eng owns       ●eng, support,
                      researchers  sales             (in code), PMs               design     have a person rollback; NPI   PM leaders
AGENTS                AI moderator Claude4Data,       Claude Code     plan mode   Claude Code Shrek        auto-deploy;   prod console,
                                   Cockpit            prototypes      (in session) + skills   reviewers    Operator → Fin incident skill
                                     └ - - - ? - - - ┘ (research → intent: not described)
                                                       prototype ─────► code ─(PR states why)─► review ─► deploy ─("what we built")─► Fin
SHARED    Claude Code plugins and skills (267, MDM-installed) · Surge design system · Snowflake semantic layer · GitHub · Slack · release tracker
LEARNING  sessions → SessionEnd gaps → GitHub issues → new skills (documented) · Fin data → own roadmap (?)
```

## What it means for our options

- **Intercom's answer to the seam is to re-capture intent at the PR, not to carry it from research.** The "why" is demanded when the PR is opened and checked by the reviewer. That is a cheap, enforceable pattern ([review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy)), but it captures intent after planning, so it can't stop a well-built wrong thing.
- **One general harness plus a governed skills marketplace, not a set of named agents.** Unlike Stripe (Kai, Harbor, Orbit, Minions), Intercom runs nearly everything through Claude Code with hundreds of skills and hook-enforced workflows; the only named custom agents are the reviewer (Shrek) and Operator. Evidence for the "general harness plus skills" option in [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent).
- **Write-back after release is a first-class step.** The support agent's knowledge is a launch gate fed by a "what we built" doc; harness gaps feed back as skills. Both are concrete versions of [context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory) write-back.
- **The research team is AI-heavy but disconnected on paper.** The best candidate seam to build for here is research → shaped intent, with the evidence attached.

## Cross-ecosystem notes

- Intercom is the "general harness + skills + hooks" archetype; Stripe is the "named agent per task" archetype.
- Intercom's distinctive mechanisms: intent captured at PR creation and verified in review; risk-based auto-approval (~19%); support-agent readiness as a release gate; a telemetry-driven harness learning loop.
- Both Stripe and Intercom shrink the research → intent → plan seam by collapsing roles rather than by building an agent handoff; neither documents one.
- No planning agent and no persisted plan artifact at Intercom (Stripe has Orbit with shared workspaces).
- Evidence is almost entirely first-party and recent (Jan–Aug 2026); Intercom has a commercial interest in this story.

## Could not verify

- How opportunities and goals are chosen beyond the CEO's company-level account; the CTO's "Product strategy still means saying no" (Apr 2026) is opinion and was not filed.
- Any PRD, brief or ticket template, or how an idea becomes work for an agent.
- Whether Fin Insights or Fin conversation data feed Intercom's own roadmap.
- On-call and paging; feature-flag and rollback mechanics; the proactive production-issue agent is only planned.
- Independent coverage (the one in-depth outside interview found is paywalled).
