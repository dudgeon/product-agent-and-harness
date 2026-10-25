# Product agent and harness

Research and strategy work on agent harnesses for product work. The question is how product managers, and anyone else in a product role, could work with agents in sessions that are persistent and shareable rather than local and private, with common product jobs handed to standardised task agents, and without being tied to one vendor's tool.

The site is at [dudgeon.org/product-agent-and-harness](https://dudgeon.org/product-agent-and-harness/) ([index.html](index.html)): the films and the lifecycle maps in one place.

## What this is for

The project builds a **menu of options, split by dimension**, with the **key questions** that would decide among the options in each. It is not a PRD for one implementation, and it does not converge on one answer. Where the evidence leans, the lean is written down along with what would change it.

Dimensions cover both runtime and architecture choices (who supplies the agent loop, where it runs, how capability is packaged, how sessions are shared, how review is gated) and user and product choices (which users, which jobs first, what outcome, how adoption happens). The reference job is **intent shaping**: turning an opportunity into a spec that coding agents can act on, in a regulated setting where audit matters.

The phases are research, concepts, prototypes to settle certain dimensions, competitive teardowns as needed, and explainer films. Research and teardowns are largely done and the films are made; prototypes have not started. Every date in this repo is 2026.

## How the folder is organised

- [research/](research/): the shared library, under the rules in [research/README.md](research/README.md).
  - [sources/](research/sources/): one note per primary source (about 1,000), each with a link to the original, why it matters to the project, the themes it supports, and an evidence label (first-party, vendor claim, independent, anecdote).
  - [INDEX.md](research/INDEX.md): one line per source. Generated; don't edit.
  - [THEMES.md](research/THEMES.md): the recurring ideas (about 65) and the sources behind each. Generated; don't edit.
  - [themes/](research/themes/): one theme file per piece of work, the input to THEMES.md.
  - [build.py](research/build.py): regenerates INDEX.md and THEMES.md from the notes and theme files.
- [options/](options/): the options register, under the rules in [options/README.md](options/README.md).
  - [DIMENSIONS.md](options/DIMENSIONS.md): the register itself. Each dimension has an options table (examples, what it gives, what it costs, maturity, evidence links) and numbered key questions, and there are cross-cutting questions at the end.
- [tasks/](tasks/): one folder of deliverables per piece of work, listed below.
- [films/](films/): the explainer films shown on the site.
- [scripts/](scripts/): `public-check.sh` (checks what would be published) and `strip-full-text.py` (the git filter that removes third-party full text on commit).

## Deliverables

### Research

**Prior work found** ([00-prior-work-found.md](tasks/research-product-agent-and-harness/00-prior-work-found.md))
The first research step found the author's earlier intent-shaping work: two documents (an intent factory to automate shaping and delivery before discovery; risk review treated as specification and classification), filed as source notes. From them came five dimensions in the register: review gating, context location, intent-shaping mode, spec standard and investment sequencing.

**Product management agents and jobs to be done**
Maps ten recurring PM jobs and where job- or persona-based PM agents have worked. The jobs are stable and the methods are changing. The best-evidenced agent jobs are bounded, fed with org context and reviewable (feedback synthesis, status drafting, first-draft specs, prototyping); the weakest are strategy, prioritisation and interviewing. No independent evaluation of any PM agent doing a PM job was found. A later source check re-checked about 540 claims and corrected about 110.
Deliverables: [brief](tasks/research-pm-agents-jobs-to-be-done/00-brief.md), [jobs-to-be-done map](tasks/research-pm-agents-jobs-to-be-done/01-jobs-to-be-done-map.md), [commercial PM agents](tasks/research-pm-agents-jobs-to-be-done/02-commercial-pm-agents.md), [in-practice cases and failures](tasks/research-pm-agents-jobs-to-be-done/03-in-practice-cases-and-failures.md), [Intercom lifecycle map](tasks/research-pm-agents-jobs-to-be-done/04-pdlc-agent-ecosystem-map.md).

**Taxonomy of agent runtime patterns**
Six research tracks and a synthesis. It names pattern classes around the general harness (vendor harness plus skills, embedded SDK, own harness, meta-harness, org-deployed workspace, general harness calling deployed agents, background agents, shared sessions, durable workflow engines, portable skill ecosystems) and consolidates the register's dimensions. Main findings: the agent loop is cheap and upkeep is the cost; skill files are portable but behaviour isn't; "shared and persistent" is five separate decisions, with identity the sharpest split.
Deliverables: [research plan](tasks/research-agent-runtime-patterns-taxonomy/00-research-plan.md), [synthesis](tasks/research-agent-runtime-patterns-taxonomy/01-synthesis.md), [pattern map](tasks/research-agent-runtime-patterns-taxonomy/map.html), track reports: [1 meta-harnesses](tasks/research-agent-runtime-patterns-taxonomy/track-1-meta-harnesses.md), [2 harness frameworks](tasks/research-agent-runtime-patterns-taxonomy/track-2-harness-frameworks.md), [3 remote and deployed agents](tasks/research-agent-runtime-patterns-taxonomy/track-3-remote-deployed-agents.md), [4 portable skills and plugins](tasks/research-agent-runtime-patterns-taxonomy/track-4-portable-skills-plugins.md), [5 shared persistent sessions](tasks/research-agent-runtime-patterns-taxonomy/track-5-shared-persistent-sessions.md), [6 work structure fit](tasks/research-agent-runtime-patterns-taxonomy/track-6-work-structure-fit.md).

**Runtime patterns follow-up round**
Covered the thin spots the synthesis named. Still no independent evidence of production A2A traffic, and among coding harnesses only Gemini CLI has a native A2A client. Omnigent now has one independent hands-on review and a mixed security record. None of the open harnesses is a governance layer above Claude Code. Codex, Copilot and Claude Code are converging on the same admin-policy shape, with audit the weak point everywhere. The market term is "agent control plane", not "agent OS".
Deliverables (in the taxonomy folder): [1 A2A in production](tasks/research-agent-runtime-patterns-taxonomy/followup-1-a2a-production.md), [2 Omnigent reaction](tasks/research-agent-runtime-patterns-taxonomy/followup-2-omnigent-reaction.md), [3 open harnesses](tasks/research-agent-runtime-patterns-taxonomy/followup-3-open-harnesses.md), [4 Codex and Copilot admin](tasks/research-agent-runtime-patterns-taxonomy/followup-4-codex-copilot-admin.md), [6 enterprise agent platforms](tasks/research-agent-runtime-patterns-taxonomy/followup-6-enterprise-agent-os.md).

**Pattern classes and the teardowns** ([00-mapping.md](tasks/teardowns-to-pattern-classes/00-mapping.md))
The teardowns and ecosystems mapped to the pattern classes, each placement sourced and marked clear, partial or contested.

**Lenny's Newsletter archive sweep**
Triaged the 564 posts from 2024-10-24 on and filed 157 notes. It adds first-party operating models from the model vendors' own product teams and a dozen large companies; evidence that adoption is about permission and mandate more than tooling; strong demand but no supply for shared, persistent sessions; and practitioners disputing prototype-as-spec. 23 episodes had no transcript and rest on show notes.
Deliverables: [summary](tasks/research-lennys-newsletter-archive/00-summary.md), [triage](tasks/research-lennys-newsletter-archive/01-triage.md).

**Department of Product knowledge series sweep**
Triaged 75 in-scope posts and read and filed the 40 rated high or medium. After reading, six stay high, among them a PM-language take on harness design with a reversibility test for what an agent may do alone, a full self-improving product loop, a catalogue of agent governance patterns, and a classification canvas for automation opportunities. No new themes.
Deliverables: [summary](tasks/research-department-of-product-knowledge-series/00-summary.md), [triage](tasks/research-department-of-product-knowledge-series/01-triage.md).

**Claude resources articles**
Read Anthropic's AI-native SDLC playbook and triaged 695 pages from claude.com's resources and customer stories, filing 95 notes. The playbook is the most explicit vendor version of the opportunity-to-code chain: each stage commits one file (intent, spec, plan, diff, review, incident) and the chain of commits is the audit trail. All of it is Anthropic's own publication, and none of it reports a controlled outcome.
Deliverables: [summary](tasks/research-claude-resources-articles/00-summary.md), [triage](tasks/research-claude-resources-articles/01-triage.md), [Anthropic lifecycle map](tasks/research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md).

**Airbnb and Spotify product practices**
Deliverables: [brief](tasks/research-airbnb-spotify-product-practices/00-brief.md), lifecycle maps for [Airbnb](tasks/research-airbnb-spotify-product-practices/01-pdlc-airbnb.md) and [Spotify](tasks/research-airbnb-spotify-product-practices/02-pdlc-spotify.md).

**Block (Square) product practices and Goose**
Deliverables: [brief](tasks/research-block-product-practices/00-brief.md), [lifecycle map](tasks/research-block-product-practices/01-pdlc-block.md).

### Teardowns

**Ramp Glass**
Glass is Ramp's company-wide AI coworker workspace, built for its own staff and opened to other companies in early access in October. It began as a desktop app on the Claude Agent SDK and has since moved to Laminar, Ramp's own provider-agnostic harness running in the cloud. Every outcome number is Ramp's own; nothing has been independently verified. A second pass traced its claims back to the sources and found the Laminar move.
Deliverables: [teardown summary](tasks/competitive-teardown-ramp-glass/00-teardown-summary.md), [X posts from Ramp leaders](tasks/competitive-teardown-ramp-glass/06-x-posts-ramp-leaders-about-glass.md), [lifecycle map](tasks/competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md).

**Shopify River and Aquifer**
River is an agent that lives in Shopify's Slack and works only in public channels; Aquifer is the platform it runs on, and the monorepo is the context it reads and adds to. The teardown covers every register dimension and opened two new ones: agent interface (own app or chat) and trust and privacy defaults (are sessions public by default?). Almost all of the evidence is Shopify's own.
Deliverables: [teardown summary](tasks/competitive-teardown-shopify-river/00-teardown-summary.md), [lifecycle map](tasks/competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md).

**Stripe's knowledge-worker agents**
Kai, Stripe's company-wide agent for people who don't write code, with Agent Studio for domain owners, Harbor for prototyping, and compliance review agents. A second pass sourced the Opportunity → Problem → Goal → Intent → Plan → Code chain to a whiteboard in a Stripe video, and tested the hypothesis that a context creation agent is needed: the need is well supported, but no company found runs a dedicated capture agent; capture happens as a by-product of work, with a human owner verifying it.
Deliverables: [teardown summary](tasks/competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md), [lifecycle map](tasks/competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md).

**Lifecycle across ecosystems** ([index.html](tasks/pdlc-cross-ecosystem-map/index.html), [method](tasks/pdlc-cross-ecosystem-map/README.md))
All nine ecosystem maps in one frame: the matrix of tasks against ecosystems, where context breaks, a comparison by dimension, and the common gaps.

### Design and story

**User story mapping: harness-agnostic modular stories**
Eighteen stories: ten PM jobs and eight cross-cutting needs. Each gives the goal and need, how it is done today without an agent harness, and the variants an agent could take, linked to the jobs map and the register. A worked example derives spec writing (S05) into two contrasting harnesses. A follow-up on artifacts and project structure added that dimension and three stories.
Deliverables: [index](tasks/user-story-mapping/INDEX.md), [format and recipe](tasks/user-story-mapping/README.md), [job stories](tasks/user-story-mapping/stories-jobs.md), [cross-cutting stories](tasks/user-story-mapping/stories-cross-cutting.md), [worked derivation of S05](tasks/user-story-mapping/worked-derivation-s05.md), [artifacts research: platforms](tasks/user-story-mapping/research-artifacts-platforms.md), [artifacts research: standardisation](tasks/user-story-mapping/research-artifacts-standardization.md), [Atlassian SDLC agents](tasks/user-story-mapping/research-atlassian-sdlc-agents.md), [Atlassian lifecycle map](tasks/user-story-mapping/01-pdlc-agent-ecosystem-map.md).

**Strategy story**
A strategy-shaped story: the delivery factory sped up, so the bottleneck moved upstream to intent; the evidence is thin and mostly the vendors' own; a regulated setting adds audit, identity and visibility constraints. It lays the options out in banks and illustrates them with Helm, a notional product workspace that is explicitly a concept, not the answer, compared against other implementations. Film 04 is built from it; its second version is restructured on three dimensions.
Deliverables: [outline](tasks/strategy-story-and-explainer-video/00-outline.md), [story with claim check](tasks/strategy-story-and-explainer-video/01-story.md), [Helm prototype design](tasks/strategy-story-and-explainer-video/02-prototype-design.md), [reference frames](tasks/strategy-story-and-explainer-video/frames/) and the [look comparison page](tasks/strategy-story-and-explainer-video/frames/checkpoint-b.html); [v2 story spine](tasks/strategy-film-v2/00-story.md).

## Films

All are 16:9 and play on the [site](https://dudgeon.org/product-agent-and-harness/).

| Film | Covers |
|---|---|
| [04 · The product agent and harness (v2)](films/04-product-agent-harness-v2.mp4) | The strategy story in about 15 minutes: three dimensions, the lifecycle and the stories |
| [05 · PM agents: what the evidence says](films/05-pm-agents-evidence.mp4) | The PM jobs map and the evidence for PM agents, using re-checked figures only |
| [06 · Ramp Glass, taken apart](films/06-ramp-glass.mp4) | The Glass teardown, with Ramp's claims labelled as first-party |
| [08 · Shaping intent: the options](films/08-intent-shaping-options.mp4) | The five intent-shaping dimensions (who shapes intent, what counts as ready, review gating, context location, investment sequencing) |
| [09 · Stripe, taken apart](films/09-stripe-teardown.mp4) | Kai, Agent Studio, Trailhead, Orbit, Minions, the whiteboard chain and the verdict on context creation |

## What is left out of the public repo

Verbatim transcripts and full texts of third-party sources are omitted here: transcript files are not tracked, and a git filter strips "Full text" sections from source notes on commit. Each note links to its original. Working notes used to run the project stay local.

Written with Claude (Anthropic) agents directed by Geoff Dudgeon. Third-party content belongs to its owners and is summarised and quoted for research.
