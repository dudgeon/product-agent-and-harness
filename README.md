# Product agent and harness

Research and strategy work on agent harnesses for product work. The question is how product managers, and anyone else in a product role, could work with agents in sessions that are persistent and shareable rather than local and private, with common product jobs handed to standardised task agents, and without being tied to one vendor's tool.

## What this is for

The end product is a **strategy deck that informs a resource request**: funding to do the hard work of picking the right pattern. It is not a PRD for one implementation. So the project builds a **menu of options, split by dimension**, with the **key questions** that would decide among the options in each. It does not converge on one answer. Where the evidence leans, the lean is written down along with what would change it.

Dimensions cover both runtime and architecture choices (who supplies the agent loop, where it runs, how capability is packaged, how sessions are shared, how review is gated) and user and product choices (which users, which jobs first, what outcome, how adoption happens). The reference job is **intent shaping**: turning an opportunity into a spec that coding agents can act on, in a regulated setting where audit matters.

Phases (from [PROJECT.md](PROJECT.md)): research; define concepts (the strategy deck); prototypes to settle certain dimensions; competitive teardowns as needed; and explainer films. Research and teardowns are largely done, the story and films are in production, and the deck and prototypes have not started.

The work is done by Claude agents: a director session hands each piece of work to a worker session and checks what comes back. Every date in this repo is 2026.

## How the folder is organised

- [PROJECT.md](PROJECT.md): goal, phases, decisions and the standing rules every agent follows.
- [research/](research/): the shared library. Every task files its research here, under the rules in [research/README.md](research/README.md).
  - [sources/](research/sources/): one note per primary source (about 820), each with a link to the original, why it matters to the project, the themes it supports, and an evidence label (first-party, vendor claim, independent, anecdote).
  - [INDEX.md](research/INDEX.md): one line per source. Generated; don't edit.
  - [THEMES.md](research/THEMES.md): the recurring ideas (about 65) and the sources behind each. Generated; don't edit.
  - [themes/](research/themes/): one theme file per task, the input to THEMES.md.
  - [build.py](research/build.py): regenerates INDEX.md and THEMES.md from the notes and theme files.
- [options/](options/): the options register, under the rules in [options/README.md](options/README.md).
  - [DIMENSIONS.md](options/DIMENSIONS.md): the register itself. 25 dimensions, each with an options table (examples, what it gives, what it costs, maturity, evidence links) and numbered key questions, plus cross-cutting questions.
  - [contributions/](options/contributions/): option proposals from the newsletter and article sweeps, kept as filed. They have been merged into DIMENSIONS.md.
- [tasks/](tasks/): one note per piece of work (the request in Geoff's words, what counts as done, dated progress lines), with its deliverables in a folder of the same name.
- [scripts/](scripts/): `public-check.sh` (checks what would be published), `strip-full-text.py` (the git filter that removes third-party full text on commit), `digest.py` (builds the director's digest page) and `workboard-data.py` (data for the workboard artifact).
- [DIRECTOR.md](DIRECTOR.md), [log.md](log.md), [LINTING.md](LINTING.md): the director's live state, its action log, and the lint pass run on each finished task.

## Tasks

Status is the task note's own `status` field. Most finished work is waiting for Geoff's acceptance, so it still reads "active".

### Research

**[Research: product agent and harness](tasks/research-product-agent-and-harness.md)** (in progress)
The first research task. At Geoff's direction it started by finding his earlier intent-shaping work: two documents of his (an intent factory to automate shaping and delivery before discovery; risk review treated as specification and classification), filed as source notes. From them it added five dimensions to the register: review gating, context location, intent-shaping mode, spec standard and investment sequencing.
Deliverable: [00-prior-work-found.md](tasks/research-product-agent-and-harness/00-prior-work-found.md).

**[Research: product management agents and jobs to be done](tasks/research-pm-agents-jobs-to-be-done.md)** (active, done and awaiting acceptance)
Maps ten recurring PM jobs and where job- or persona-based PM agents have worked. The jobs are stable and the methods are changing. The best-evidenced agent jobs are bounded, fed with org context and reviewable (feedback synthesis, status drafting, first-draft specs, prototyping); the weakest are strategy, prioritisation and interviewing. No independent evaluation of any PM agent doing a PM job was found. A later audit checked about 540 claims and corrected about 110.
Deliverables: [brief](tasks/research-pm-agents-jobs-to-be-done/00-brief.md), [jobs-to-be-done map](tasks/research-pm-agents-jobs-to-be-done/01-jobs-to-be-done-map.md), [commercial PM agents](tasks/research-pm-agents-jobs-to-be-done/02-commercial-pm-agents.md), [in-practice cases and failures](tasks/research-pm-agents-jobs-to-be-done/03-in-practice-cases-and-failures.md), audit logs ([lead](tasks/research-pm-agents-jobs-to-be-done/audit-2026-10-24.md), [01](tasks/research-pm-agents-jobs-to-be-done/audit-2026-10-24-01-jobs-map.md), [02](tasks/research-pm-agents-jobs-to-be-done/audit-2026-10-24-02-commercial.md), [03](tasks/research-pm-agents-jobs-to-be-done/audit-2026-10-24-03-in-practice.md)).

**[Research: taxonomy of agent runtime patterns](tasks/research-agent-runtime-patterns-taxonomy.md)** (active, done and awaiting acceptance)
Six research tracks and a synthesis. It names ten pattern classes around the general harness (vendor harness plus skills, embedded SDK, own harness, meta-harness, org-deployed workspace, general harness calling deployed agents, background agents, shared sessions, durable workflow engines, portable skill ecosystems) and consolidates the register's dimensions. Main findings: the agent loop is cheap and upkeep is the cost; skill files are portable but behaviour isn't; "shared and persistent" is five separate decisions, with identity the sharpest split. Geoff's answers to its open questions are recorded in the synthesis.
Deliverables: [research plan](tasks/research-agent-runtime-patterns-taxonomy/00-research-plan.md), [synthesis](tasks/research-agent-runtime-patterns-taxonomy/01-synthesis.md), [pattern map](tasks/research-agent-runtime-patterns-taxonomy/map.html), track reports: [1 meta-harnesses](tasks/research-agent-runtime-patterns-taxonomy/track-1-meta-harnesses.md), [2 harness frameworks](tasks/research-agent-runtime-patterns-taxonomy/track-2-harness-frameworks.md), [3 remote and deployed agents](tasks/research-agent-runtime-patterns-taxonomy/track-3-remote-deployed-agents.md), [4 portable skills and plugins](tasks/research-agent-runtime-patterns-taxonomy/track-4-portable-skills-plugins.md), [5 shared persistent sessions](tasks/research-agent-runtime-patterns-taxonomy/track-5-shared-persistent-sessions.md), [6 work structure fit](tasks/research-agent-runtime-patterns-taxonomy/track-6-work-structure-fit.md).

**[Research: runtime patterns follow-up round](tasks/research-runtime-patterns-follow-up-round.md)** (active; the worker stalled and was stopped, and its results were merged by the director)
Covered the thin spots the synthesis named. Still no independent evidence of production A2A traffic, and among coding harnesses only Gemini CLI has a native A2A client. Omnigent now has one independent hands-on review and a mixed security record. None of the open harnesses is a governance layer above Claude Code. Codex, Copilot and Claude Code are converging on the same admin-policy shape, with audit the weak point everywhere. The market term is "agent control plane", not "agent OS". No addendum to the synthesis was written, and there is no fifth report (on Cowork and Claude Enterprise plugin administration).
Deliverables (in the taxonomy folder): [1 A2A in production](tasks/research-agent-runtime-patterns-taxonomy/followup-1-a2a-production.md), [2 Omnigent reaction](tasks/research-agent-runtime-patterns-taxonomy/followup-2-omnigent-reaction.md), [3 open harnesses](tasks/research-agent-runtime-patterns-taxonomy/followup-3-open-harnesses.md), [4 Codex and Copilot admin](tasks/research-agent-runtime-patterns-taxonomy/followup-4-codex-copilot-admin.md), [6 enterprise agent platforms](tasks/research-agent-runtime-patterns-taxonomy/followup-6-enterprise-agent-os.md).

**[Research: Lenny's Newsletter archive sweep](tasks/research-lennys-newsletter-archive.md)** (active, done and awaiting acceptance)
Triaged the 564 posts from 2024-10-24 on and filed 157 notes. It adds first-party operating models from the model vendors' own product teams and a dozen large companies; evidence that adoption is about permission and mandate more than tooling; strong demand but no supply for shared, persistent sessions; and practitioners disputing prototype-as-spec. 23 episodes had no transcript and rest on show notes.
Deliverables: [summary](tasks/research-lennys-newsletter-archive/00-summary.md), [triage](tasks/research-lennys-newsletter-archive/01-triage.md), [options proposed](options/contributions/research-lennys-newsletter-archive.md).

**[Research: Department of Product knowledge series sweep](tasks/research-department-of-product-knowledge-series.md)** (active, done and awaiting acceptance)
Triaged 75 in-scope posts and read and filed the 40 rated high or medium. After reading, six stay high, among them a PM-language take on harness design with a reversibility test for what an agent may do alone, a full self-improving product loop, a catalogue of agent governance patterns, and a classification canvas for automation opportunities. No new themes.
Deliverables: [summary](tasks/research-department-of-product-knowledge-series/00-summary.md), [triage](tasks/research-department-of-product-knowledge-series/01-triage.md), [options proposed](options/contributions/research-department-of-product-knowledge-series.md).

**[Research: Claude resources articles](tasks/research-claude-resources-articles.md)** (active, done and awaiting acceptance)
Read Anthropic's AI-native SDLC playbook and triaged 695 pages from claude.com's resources and customer stories, filing 95 notes. The playbook is the most explicit vendor version of the opportunity-to-code chain: each stage commits one file (intent, spec, plan, diff, review, incident) and the chain of commits is the audit trail. All of it is Anthropic's own publication, and none of it reports a controlled outcome.
Deliverables: [summary](tasks/research-claude-resources-articles/00-summary.md), [triage](tasks/research-claude-resources-articles/01-triage.md), [options proposed](options/contributions/research-claude-resources-articles.md).

### Teardowns

**[Competitive teardowns of existing products and features](tasks/competitive-teardowns.md)** (suggested)
The parent placeholder for phase 4. The three teardowns below came out of it.

**[Competitive teardown: Ramp Glass](tasks/competitive-teardown-ramp-glass.md)** (active, done and awaiting acceptance)
Glass is Ramp's company-wide AI coworker workspace, built for its own staff and opened to other companies in early access in October. It began as a desktop app on the Claude Agent SDK and has since moved to Laminar, Ramp's own provider-agnostic harness running in the cloud. Every outcome number is Ramp's own; nothing has been independently verified. An audit traced its claims back to the sources and found the Laminar move.
Deliverables: [teardown summary](tasks/competitive-teardown-ramp-glass/00-teardown-summary.md), [X posts from Ramp leaders](tasks/competitive-teardown-ramp-glass/06-x-posts-ramp-leaders-about-glass.md), [audit log](tasks/competitive-teardown-ramp-glass/audit-2026-10-24.md).

**[Competitive teardown: Shopify River and Aquifer](tasks/competitive-teardown-shopify-river.md)** (active, done and awaiting acceptance)
River is an agent that lives in Shopify's Slack and works only in public channels; Aquifer is the platform it runs on, and the monorepo is the context it reads and adds to. The teardown covers every register dimension and opened two new ones: agent interface (own app or chat) and trust and privacy defaults (are sessions public by default?). Almost all of the evidence is Shopify's own.
Deliverable: [teardown summary](tasks/competitive-teardown-shopify-river/00-teardown-summary.md).

**[Competitive teardown: Stripe's knowledge-worker agents](tasks/competitive-teardown-stripe-knowledge-agents.md)** (active)
Kai, Stripe's company-wide agent for people who don't write code, with Agent Studio for domain owners, Harbor for prototyping, and compliance review agents. A second pass sourced Geoff's Opportunity → Problem → Goal → Intent → Plan → Code chain to a whiteboard in a Stripe video, and tested his hypothesis that a context creation agent is needed: the need is well supported, but no company found runs a dedicated capture agent; capture happens as a by-product of work, with a human owner verifying it.
Deliverable: [teardown summary](tasks/competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md).

### Design and story

**[User story mapping: harness-agnostic modular stories](tasks/user-story-mapping.md)** (active, done and awaiting acceptance)
Eighteen stories: ten PM jobs and eight cross-cutting needs. Each gives the goal and need, how it is done today without an agent harness, and the variants an agent could take, linked to the jobs map and the register. A worked example derives spec writing (S05) into two contrasting harnesses. A follow-up on artifacts and project structure added that dimension and three stories.
Deliverables: [index](tasks/user-story-mapping/INDEX.md), [format and recipe](tasks/user-story-mapping/README.md), [job stories](tasks/user-story-mapping/stories-jobs.md), [cross-cutting stories](tasks/user-story-mapping/stories-cross-cutting.md), [worked derivation of S05](tasks/user-story-mapping/worked-derivation-s05.md), [artifacts research: platforms](tasks/user-story-mapping/research-artifacts-platforms.md), [artifacts research: standardisation](tasks/user-story-mapping/research-artifacts-standardization.md), [audit log](tasks/user-story-mapping/audit-2026-10-24.md).

**[Strategy story and 15-minute explainer video](tasks/strategy-story-and-explainer-video.md)** (active)
A strategy-shaped story, "Ready to ship": the delivery factory sped up, so the bottleneck moved upstream to intent; the evidence is thin and mostly the vendors' own; a regulated setting adds audit, identity and visibility constraints. It lays the options out in five banks and illustrates them with Helm, a notional product workspace that is explicitly a concept, not the answer, compared against other implementations. The film (04) is being built from it.
Deliverables: [outline](tasks/strategy-story-and-explainer-video/00-outline.md), [story with claim check](tasks/strategy-story-and-explainer-video/01-story.md), [Helm prototype design](tasks/strategy-story-and-explainer-video/02-prototype-design.md), [reference frames](tasks/strategy-story-and-explainer-video/frames/) and the [look comparison page](tasks/strategy-story-and-explainer-video/frames/checkpoint-b.html).

### Films

Five tasks for the shorter explainer films; see [Films](#films) below for what each covers.

- [Explainer film: the PM-agents evidence](tasks/pm-agents-evidence-film.md) (active): film 05.
- [Explainer film: the Ramp Glass teardown](tasks/ramp-glass-film.md) (active): film 06.
- [Explainer film: runtime patterns taxonomy](tasks/runtime-patterns-film.md) (active): film 07.
- [Explainer film: the intent-shaping options menu](tasks/intent-shaping-options-film.md) (active): film 08.
- [Explainer film: the Stripe teardowns](tasks/stripe-teardown-film.md) (active): film 09.
- [Explainer video and its style](tasks/explainer-video-style.md) (dropped): superseded by the strategy story task, which defines the style.

### Later phases

- [Define concepts and build the strategy deck](tasks/define-concepts-strategy-deck.md) (suggested): phase 2, the deck itself. Not started.
- [Prototypes to define key dimensions](tasks/prototypes-define-dimensions.md) (suggested): phase 3. Not started.

### This README

- [Update the project README with tasks and deliverables](tasks/project-readme.md) (active).

## Claude artifacts

Pages on claude.ai that the tasks refer to. They are private unless Geoff has shared them.

- [Workboard](https://claude.ai/artifact/7fwBzcE3FQPAZujKjShvKj): a dashboard of every task and its stage, kept by the director.
- [Film 04 Script Doc](https://claude.ai/artifact/BNJKVeJdDxGmiwfVNSBqVy): the two-column script for the main film, with its claim check as an appendix.
- [Building and Accelerating the Intent Factory](https://claude.ai/artifact/KD7oCzhwgca9bvr2mq3ADC): Geoff's document, filed as [a source note](research/sources/geoff-building-accelerating-intent-factory.md).
- [Intent Shaping in a Well-Managed Environment](https://claude.ai/artifact/LKZqiLtGYeAxEnAQZXoJMM): Geoff's document, filed as [a source note](research/sources/geoff-intent-shaping-well-managed-environment.md).
- [Stripe's Internal Agent Ecosystem for Product Development](https://claude.ai/artifact/PG1sfq8UxAJzhVxRgrmeu3): Geoff's document, reviewed in the Stripe teardown's second pass and filed as [a source note](research/sources/claude-doc-geoff-stripe-internal-agent-ecosystem.md).
- Earlier related work listed in [00-prior-work-found.md](tasks/research-product-agent-and-harness/00-prior-work-found.md) but not yet read or filed: [From PM idea to code: how Stripe and Ramp actually do it](https://claude.ai/artifact/5VxwzYPzfWwGPUx4iQ3eQD), [Current State: sources and endnotes](https://claude.ai/artifact/LTjj2wcKTSbKQPXY8DLhmb), [Specs as Theory Building](https://claude.ai/artifact/Rmg9fZP8QWFJtY8XE9C2dr) and its [Extended Cut](https://claude.ai/artifact/967zr5dq9oxSreAzzy3zxe).

## Films

The films are made with a separate explainers toolkit and live in a private folder outside this repo, so they are named here but not linked. All are 16:9 in film 04's look. Geoff reviews each one after it is rendered end to end, then edits its Script Doc. As of 2026-10-24 none has finished rendering: they take turns on one GPU, with 04 first.

| Film | Covers | State |
|---|---|---|
| 04 · Ready to ship: the product agent and harness | The strategy story in about 15 minutes, with walkthrough demos of Helm as a conversational thread | Script complete; voicing under way; full build next |
| 05 · PM agents: what the evidence says | The PM jobs map and the evidence for PM agents, using audited figures only | Script approved by Geoff; most lines voiced; full build queued after 04 |
| 06 · Ramp Glass, taken apart | The Glass teardown, with Ramp's claims labelled as first-party | Script and scenes drafted; full build queued |
| 07 · Where the agent runs: runtime patterns, a menu not a winner | The ten pattern classes, the dimensions as a menu, evidence quality, Geoff's answers and the open questions | Script trimmed and scenes built; waiting for its GPU turn |
| 08 · Shaping intent: the options | The five intent-shaping dimensions (who shapes intent, what counts as ready, review gating, context location, investment sequencing), grounded in Geoff's two documents | Script and scenes built; waiting for its GPU turn |
| 09 · Stripe, taken apart | Kai, Agent Studio, Trailhead, Orbit, Minions, the whiteboard chain and the verdict on context creation | Script and scenes drafted; waiting for its GPU turn |

## What is left out of the public repo

Verbatim transcripts and full texts of third-party sources are omitted here: transcript files are not tracked, and a git filter strips "Full text" sections from source notes on commit. Each note links to its original. Geoff's own documents are published in full.

Written with Claude (Anthropic) agents directed by Geoff Dudgeon. Third-party content belongs to its owners and is summarised and quoted for research.
