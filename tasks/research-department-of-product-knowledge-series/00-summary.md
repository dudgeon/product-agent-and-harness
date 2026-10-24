# Summary: Department of Product, Knowledge Series

Task: [research-department-of-product-knowledge-series](../research-department-of-product-knowledge-series.md). Swept 2026-10-24. Triage: [01-triage.md](01-triage.md). Theme evidence: [research/themes/research-department-of-product-knowledge-series.md](../../research/themes/research-department-of-product-knowledge-series.md). Proposed options: [options/contributions/research-department-of-product-knowledge-series.md](../../options/contributions/research-department-of-product-knowledge-series.md).

## What was done

- **Archive.** 437 posts in the publication; 121 tagged Knowledge Series. Geoff set a cut-off (via the director) at posts dated 2024-10-24 or later, which leaves **73 tagged posts in scope plus 2 untagged posts numbered in the series**. The 48 older posts are listed in the triage as out of scope. The series has no podcasts or guest posts.
- **Triage** (in scope): 13 high, 26 medium, 32 low, 2 none, plus 1 untagged medium post.
- **Read and filed: all 40 high and medium posts**, read in full through Geoff's logged-in paid subscription in Chrome. Nothing stayed paywalled. After reading, relevance was re-rated honestly: **6 high, 20 medium, 14 low**. Most of the drops are 2025 primers that later first-party sources in the library supersede.
- Notes are summaries in our own words with section references. There is no full text, and no prompts or templates are reproduced. Every company fact is marked second-hand.
- The existing DoP notes ([Stripe Kai](../../research/sources/departmentofproduct-stripe-kai.md), [internal AI tools PDF](../../research/sources/departmentofproduct-internal-ai-tools-for-non-engineers.md)) were left as they were. They are not Knowledge Series posts.

### The six high-relevance notes
| Note | Why it matters |
|---|---|
| [Are Agent Harnesses the new "secret sauce"?](../../research/sources/departmentofproduct-agent-harnesses-secret-sauce.md) (2026-04-29) | PM-language harness design in five principles. Square's head of product calls the harness Managerbot's moat. Introduces the **reversibility test** for which actions an agent may take alone |
| [How to build a Self-improving Product](../../research/sources/departmentofproduct-self-improving-product.md) (2026-06-22) | The most complete public PM agent loop in the library: sense, judge, spec, route, review against acceptance criteria, then write memory for each product area. Amplitude's candid **~11% shipped vs ~50% "would do"** |
| [How to Manage AI Agents Effectively](../../research/sources/departmentofproduct-managing-ai-agents.md) (2026-08-10) | The widest catalogue of governance patterns filed: gateway, dual identity, LLM-judge evals, launch-readiness gate, spend against output. Leads, not evidence |
| [How to Identify Opportunities for AI Automation](../../research/sources/departmentofproduct-ai-automation-opportunities.md) (2025-11-26) | A three-axis classification canvas (safety, volume, verifiability) that PMs can use in a workshop |
| [Practical ways to use Claude Routines](../../research/sources/departmentofproduct-claude-routines-for-product-teams.md) (2026-06-02) | Scheduled agents for PM jobs (backlog digest, feedback aggregation, release notes, deprecation watch, competitor tracker). The connector list acts as the permission boundary |
| [Practical Agent Skills for Product Teams](../../research/sources/departmentofproduct-practical-agent-skills.md) (2026-07-07) | The skills ecosystem PMs actually meet: public GitHub repos with no vetting, and skill families split into stages that each write a file |

## What this publication adds

DoP is the **practitioner's view of the "general harness plus skills" path**. Almost every tutorial runs inside a vendor harness (Claude Code, Cowork, Claude Design, Cursor, Perplexity Computer), using off-the-shelf skills, connectors and a few markdown files. None of them is a custom PM agent. Its value to the project is threefold: concrete job-level playbooks, PM vocabulary for harness concepts, and pointers to company cases. It is not evidence. Every company number is relayed unchecked, nothing the author built is measured, and several demos run on mock data.

### By dimension
- **activity-classification:** the three-axis canvas is a simpler, PM-packaged sibling of Track 6's seven axes. It agrees that error cost and verifiability drive fit, and adds volume. Claude Code's `/insights` gives a second, usage-mined route to candidates.
- **review-and-autonomy:** three new shapes. A *reversibility split* hard-coded in the harness. A *propose-only* agent (Square Managerbot, a second regulated-payments case beside Stripe's review-every-change floor). *Autonomy set by a spec complexity tag* (Amplitude). Plus `/goal` "describe done" runs, with an explicit carve-out that keeps judgement work out.
- **pm-agent-evaluation:** the *proposal funnel* (would do vs shipped) is a measure no other note offers, and one of the few vendor numbers that admits most proposals don't ship. Calibrated LLM-judge stacks (Airbnb, DoorDash) and a PM-kept "model sense" eval log at each release complete the picture.
- **governance-control-plane and agent-identity-delegation:** agent-to-tool gateway (DoorDash), dual human-plus-agent identity on every hop (Block, Uber), user ∩ agent permission ceiling (WorkOS), spend against output (Rippling, Ramp), typed classifiers for pre-action checks (Vercel, Rippling). All second-hand.
- **context-and-memory:** a *semantic layer with a named human owner per definition* (the Anthropic data team, second-hand, 21%→95%). Repo snapshot files as state between runs. Memory per product area written by a reflection agent. Vendor CLIs as a third tool route beside MCP and APIs.
- **artifact-and-project-structure:** a *decision queue* as an artifact ("a forcing function, not a to-do list"). The Claude Projects roll-up gap: function sub-projects feed a master project only by copy-paste. Stage-artifact skill chains.
- **intent-shaping-and-spec:** a closed sense-to-learn loop as evidence for "agent-originated intent". A diverge-first ideation agent (Stitch). A framework-scripted sparring partner ("cognitive expansion, not offloading"). DESIGN.md's two-layer shape (machine tokens plus rationale) as a model for a lintable spec standard.
- **capability-distribution-trust:** mainstream PM media hands PMs bundles of public skills with no security framing. That strengthens the case for a gated registry.
- **adoption-model:** the posts teach PMs to build *personal* tools (local dashboards, their own Projects, their own loops). That is the opposite model to Glass, where one person's win becomes everyone's baseline. Nothing in DoP covers packaging and sharing.

### Themes most reinforced
Most reinforced, by bullet count: `pm-tool-connectivity` (10), `vendor-claims-vs-independent-evidence` (9), `status-update-agents` (8), `evals-autonomy-trust` (8), `work-structure-spectrum` (7), `non-engineer-builders` (7), `prototyping-agents-limits` (6). In total, 166 bullets across 53 existing themes. No new theme was needed.

## Agreement and contradiction with what's filed

**Agrees with:**
- The harness-over-model thesis and the brain/hands/session split ([Anthropic, Scaling Managed Agents](../../research/sources/anthropic-engineering-scaling-managed-agents.md); [Stripe Minions part 2](../../research/sources/stripe-minions-part-2.md)).
- Ramp Glass as the reference internal platform. The DoP Glass post only restates [Seb Goddijn's article](../../research/sources/x-sebgoddijn-glass-article.md) and adds nothing new.
- Stripe's "domain owners as QA". The semantic-layer case adds "AI drafts, a named human owns the definition".
- "Meta-harness" having competing meanings: DoP uses it for the Stanford optimiser ([paper](../../research/sources/arxiv-meta-harness-optimization.md)).
- Routines docs on stored prompts and connectors ([scheduled tasks](../../research/sources/anthropic-claude-code-scheduled-tasks.md)). DoP adds one friction the docs don't mention: PMs need a repo first.

**Contradicts or complicates:**
- **Synthetic users.** DoP's persona tester and discovery-sprint posts present AI personas and "queryable models of real interviews" with no caveat, and the "grounding" data in the demo was itself AI-generated. That runs against [NN/g](../../research/sources/nngroup-synthetic-users.md) and [Torres](../../research/sources/producttalk-ai-hallucination-glossary.md). Treat these as claims.
- **Skill security.** DoP's bundle download sits uneasily with the [Snyk ToxicSkills](../../research/sources/snyk-toxicskills-study.md) and [ClawHavoc](../../research/sources/thehackernews-clawhavoc-341-malicious-skills.md) findings.
- **Multi-agent advice ages fast.** The 2025 primers recommended multi-agent architectures and AutoGen. [Cognition](../../research/sources/cognition-dont-build-multi-agents.md) and [AutoGen's archive notice](../../research/sources/github-microsoft-autogen-archive-notice.md) later contradicted both. It is a dated marker of how quickly the advice PMs get goes stale.
- **A correction to a filed note:** [Stripe Kai DoP](../../research/sources/departmentofproduct-stripe-kai.md) gives the automation canvas's axes as "frequency vs volume". The source post's axes are safety, volume and verifiability. The note belongs to another task, so it is flagged here and in the contribution file rather than edited.
- The Skills post (dated 2025-10-21) describes a December 2025 directory, so it was edited after publication. The note says so.

## Options by dimension

Proposed in [options/contributions/research-department-of-product-knowledge-series.md](../../options/contributions/research-department-of-product-knowledge-series.md), for the director to merge into: activity-classification, review-and-autonomy, pm-agent-evaluation, governance-control-plane, agent-identity-delegation, session-persistence-sharing, context-and-memory, artifact-and-project-structure, intent-shaping-and-spec, capability-distribution-trust, agent-interface, loop-source, adoption-model. Plus one cross-cutting question: trace every figure to its primary source before the deck uses it. No new dimensions are proposed.

## For the film (tasks/strategy-story-and-explainer-video/)

- **Helm's Intake stage has an honest number to show.** The prototype design has analyst agents proposing feature candidates. The nearest public analogue, Amplitude's loop, reports ~11% of agent-proposed fixes shipped against ~50% judged worth doing (vendor claim, relayed by DoP). That beat could show the proposal funnel narrowing, which fits the film's evidence-honest tone.
- **A second regulated case for Ratify.** Square's Managerbot proposes every action and does nothing until the seller approves (second-hand via VentureBeat). Alongside Stripe's review-every-change rule, it supports the human ratify step without implying it is unusual.
- **The reversibility test as a one-line visual.** "Which decisions belong to the model, and which to the system?" Easy-to-undo actions in a free zone, payments and publishing behind a hard-coded gate. It could sit beside the Risk Advisor's grid in S10.
- **The automation canvas** (verifiability against volume, coloured by risk: bug triage in the green corner, legal terms in the red) is a clean diagram for S6 or S7, for "which steps are standardised judgement".
- **Caution on synthetic users.** If any walkthrough shows simulated personas, the DoP demo is a ready example of the trap: personas "grounded in real data" built from AI-generated data.
- **Metaphors:** a loop as "a recurring calendar reminder that actually does something with what it finds"; the decision queue as "a forcing function, not a to-do list"; "finished-looking artifacts suppress criticism" (from the DESIGN.md post; relevant to how polished Helm's screens look).
- **Don't cite DoP for numbers.** Every figure in it belongs to a vendor. If the film uses one (Amplitude, DoorDash, Anthropic's 21%→95%), trace it to the primary source first. The primaries are listed below.

## Primary sources cited by DoP and not yet filed (candidates for follow-up)

Highest value first:
1. VentureBeat on Block's Managerbot (the Square head of product quote)
2. Amplitude's Wave write-up (11% ship rate)
3. Anthropic data team on its self-service analytics agent (21%→95%)
4. Rippling GrowthOS test of decision models; Rippling MCP code-mode post
5. DoorDash Agent Gateway and LLM-judge posts; Airbnb evaluation post
6. Block User Identity Delegation; Uber agent identity
7. Vanta Agentic Trust Controls and the AARM paper
8. Google DESIGN.md spec
9. Atlassian spec-to-backlog skill; Notion Spec to Implementation
10. OpenAI's Codex `/goal` guide
11. Addy Osmani on agent harness engineering
12. Linear's CEO on agent-created issues outnumbering human ones

The full list of leads is in the "Could not verify" sections of the notes.

## Could not read
Nothing in scope. All 40 high and medium posts were read in full. The 32 low and 2 none posts were triaged from title and subtitle only, as the brief allows. Embedded images and PDF attachments (for example the 20+ example table in the harness post, and the downloadable PDFs) were not opened.
