# Track 6: Classes of user activity and fit to runtime pattern

Date: 2026-10-24. Filed by: research-agent-runtime-patterns-taxonomy (Track 6). Read-only web research. Source notes are in [../../research/sources/](../../research/sources/); theme register entry: `work-structure-spectrum` in [../../research/THEMES.md](../../research/THEMES.md). Options and key questions are in [../../options/DIMENSIONS.md](../../options/DIMENSIONS.md) (see "Options by dimension" below).

Evidence labels: **first-party** (author describes own system), **vendor claim**, **independent**, **anecdote**. "Judgment" marks my synthesis, not a sourced fact.

## 1. Bottom line

Geoff's hypothesis is **partly supported and needs refining**.

- Supported: the vendor guidance from Anthropic, Google, OpenAI and LangChain all draw a line between work whose path can be written down (workflow, deterministic steps) and work whose path cannot (agent, model-directed loop). The independent production study finds deployed agents are short, constrained and human-checked (68% run at most 10 steps before human intervention), so constraint is what reliability work produces.
- Refined: the dividing line in the evidence is **not "kind of user activity"** (planning vs PRD review). It is a bundle of properties of a *step of work*: how predictable the path is, whether a cheap check exists, how often it repeats and how much consistency matters, what an error costs, whether someone must audit it, and how much tacit context it carries. Planning and ideation sit at one end of most of these, review and policy checks at the other, but the same person moves between them inside one session (explore, spec, review, build).
- Not found: any controlled comparison showing a task-specific agent beating a skill inside a general harness on a standard job (for example PRD review). That is the central evidence gap for the project's question.
- Counter-evidence to a permanent split: structure that compensates for model weakness decays (Claude Code team, second-hand; Ramp's Policy Agent moved from a fixed chain to an agentic loop). What persists is structure that comes from the *work itself*: verification, audit, permissions, repeatability.

## 2. Proposed classification of activity

Axes (each scored low/high per job step; evidence in section 4). Order is not ranking.

| Axis | Low end | High end | Main evidence |
|---|---|---|---|
| A1 Step predictability | path unknown until you start | path fixed and writable | Anthropic effective agents; Google design-pattern guide |
| A2 Verifiability | no cheap check, taste decides | test, rubric or ground truth exists | Claude Code best practices; Anthropic effective agents (coding appendix); Cloudflare review |
| A3 Repeatability and consistency demand | one-off | same job on every PR/ticket/expense, must behave the same | tau-bench pass^k; 12-factor; Ramp Policy Agent (existing notes) |
| A4 Error cost and reversibility | cheap, reversible | costly or irreversible | Google HITL; Anthropic autonomy (0.8% irreversible actions); Stripe |
| A5 Audit and accountability | nobody signs | a named owner or regulator needs a trace | existing `risk-sloped-review` evidence; Cloudflare break-glass log |
| A6 Context breadth and tacit standards | self-contained | needs org context and unwritten conventions | METR RCT; PM-agent notes (`org-context-grounding`) |
| A7 Collaboration | single owner | cross-role, hand-offs, shared artifact | Ramp Glass sharing (existing notes); Atlassian Jira-to-coding-agent flow (existing notes) |
| A8 Desired human agency | person wants to do or steer it | person wants it gone | Stanford Human Agency Scale (WORKBank) |

Five working classes (judgment, derived from clustering the axes; I propose them as a starting taxonomy to test, not as findings):

| Class | Typical examples | Profile | Evidence it is real |
|---|---|---|---|
| C1 Open exploration and sensemaking | planning, ideation, strategy framing, codebase orientation, personal knowledge work | A1 low, A2 low, A3 low, A5 low, A8 high agency | Claude Code best practices say vague prompts are right when exploring; HN anecdotes of notes and vault work; Anthropic work study (27% of AI-assisted work is new work); Economic Index (iterative Claude.ai use) |
| C2 Directed construction with a check | coding, prototyping, spec-to-prototype | A2 high (tests, screenshot diff), A1 medium | Anthropic effective agents, coding appendix; Claude Code best practices (verification as highest leverage) |
| C3 Repeatable standardised judgement | code review, PRD review, policy or expense checks, compliance review, risk classification | A3 high, A5 high, A6 high, A2 medium (rubric, SME labels) | Cloudflare review (specialists, exclusions, risk tiers); Ramp Policy Agent; Geoff's risk-as-classification note (existing); CR-Bench noise findings |
| C4 Volume pipelines | migrations, triage queues, scheduled reports, fan-out over files | A1 high, A3 high, A4 medium | Claude Code `claude -p` fan-out; Stripe Minions; Google sequential/parallel patterns |
| C5 Accountable commitments | launch go/no-go, prioritisation bets, irreversible actions | A4 high, A5 high, A8 high agency | Google HITL; Anthropic work study (engineers keep judgment needing "taste"); Krieger/Dill remarks (existing) |

Notes on the classes:
- The class belongs to a **job step**, not a person or a tool. A "PRD" job contains a C1 step (framing), a C3 step (review against a team standard) and a C5 step (ratify).
- C1 is unstructured in *path* but still wants structured *context* (folders, memory, naming): the HN anecdotes and the Claude Code CLAUDE.md guidance both point that way.

## 3. Evidence for and against Geoff's hypothesis

Hypothesis (as stated): there is general-purpose planning and ideation work that is and wants to remain unstructured and needs a powerful flexible harness; and task-specific work, such as standardising PRD review, that wants a task-specific agent or workflow.

### For
1. Vendor guidance, all four majors: workflows for well-defined, predictable tasks; agents for open-ended; start simple ([Anthropic](../../research/sources/anthropic-building-effective-agents.md) first-party; [Google](../../research/sources/google-cloud-choose-design-pattern-agentic-ai.md) vendor; [OpenAI](../../research/sources/openai-practical-guide-building-agents.md) vendor, secondary read; [LangChain](../../research/sources/langchain-how-to-think-about-agent-frameworks.md) vendor).
2. Independent production evidence: [Measuring Agents in Production](../../research/sources/arxiv-measuring-agents-in-production.md): 68% of agents run at most 10 steps before human intervention, 74% rely mainly on human evaluation, reliability is the top challenge (independent, practitioner survey of 86 deployed systems).
3. Reliability on repeated policy-following work is poor without constraint: [tau-bench](../../research/sources/arxiv-tau-bench.md) pass^8 under 25% in retail (independent, 2024 models; likely improved).
4. Standardised review works as narrow specialists with explicit exclusions and risk tiers: [Cloudflare](../../research/sources/cloudflare-ai-code-review-opencode.md) (first-party; 131,246 runs, average $1.19), whose own naive single-prompt attempt was noisy. [CR-Bench](../../research/sources/arxiv-cr-bench.md) (independent, preliminary) finds exhaustive review agents have low signal-to-noise.
5. Unstructured work happens in a flexible harness: [Claude Code best practices](../../research/sources/anthropic-claude-code-best-practices.md) (first-party) endorse vague prompts for exploration and skipping the plan for exploratory tasks; [HN thread](../../research/sources/hn-ask-claude-code-non-coding-workflows.md) (anecdote); [Anthropic work study](../../research/sources/anthropic-how-ai-is-transforming-work-at-anthropic.md) (first-party self-report: 27% of AI-assisted work is new).
6. Humans want different control for different tasks: [Stanford WORKBank / Human Agency Scale](../../research/sources/arxiv-future-of-work-with-ai-agents.md) (independent).

### Against or complicating
1. **It is a spectrum, and most real systems are hybrids** ([LangChain](../../research/sources/langchain-how-to-think-about-agent-frameworks.md), vendor; [Stripe Minions](../../research/sources/stripe-minions-one-shot-coding-agents.md), first-party: deterministic nodes around an agentic core). A two-class split understates the middle.
2. **Structure can live inside the general harness**, so "task-specific" does not require a task-specific agent. Skills carry workflows, hooks and Stop hooks enforce checks deterministically, subagents give fresh-context review, `claude -p` runs unattended ([best practices](../../research/sources/anthropic-claude-code-best-practices.md); [Agent Skills](../../research/sources/anthropic-engineering-equipping-agents-agent-skills.md), first-party). Ramp consolidated to one agent with skills after teams built four versions of the same agent (existing Ramp notes).
3. **Structure decays as models improve.** Claude Code team (second-hand AI summary, [Traces](../../research/sources/traces-boris-cherny-light-cone-summary.md)): scaffolding for a 10-20% gain is wiped out by the next model; plan mode may be unnecessary soon. Ramp's Policy Agent went from a fixed chain to a full agentic loop (existing note). Weak but relevant: the class boundary moves with model capability.
4. **Open-ended assistance can hurt where tacit context is high.** [METR RCT](../../research/sources/metr-early-2025-experienced-developer-rct.md) (independent, early-2025 tools): experts took 19% longer on familiar repos while believing they were faster. This is a case of "general tool applied to a task with strict implicit standards", not of planning work.
5. **Usage data shows mixing, not clean classes.** [Economic Index](../../research/sources/anthropic-economic-index-2026-01.md) (first-party): Claude.ai about half augmentation, half automation; API about three-quarters automation. The split is by access route more than by job.
6. **Autonomy is not fixed per task class; it drifts with the user.** [Anthropic autonomy study](../../research/sources/anthropic-measuring-agent-autonomy.md) (first-party): auto-approve 20% of sessions for new users, over 40% for experienced; experienced users also interrupt more. A class-to-autonomy table would need to be per-user.
7. **Multi-agent is the wrong tool for interdependent work, right for breadth-first work** ([Cognition](../../research/sources/cognition-dont-build-multi-agents.md); [Anthropic research system](../../research/sources/anthropic-multi-agent-research-system.md), both first-party). This splits "exploration" itself: breadth-first research parallelises (about 15x tokens); design and coding do not.

### Thin or contradicted (what we do not know)
- No controlled comparison of task agent vs skill-in-general-harness on any standard job (the key gap). Closest: SkillsBench note and Glean (existing notes), not a like-for-like.
- No evidence at all specific to ideation or planning quality with agents (only anecdote and usage logs); "wants to remain unstructured" is an assertion supported by guidance and anecdote, not measurement.
- No evidence on PRD-review agents specifically; the PM-agents track found no independent evaluation of any PM agent.
- Most evidence is vendor or first-party; independent items are the production survey, tau-bench, CR-Bench, METR, Stanford.
- Unread primaries: OpenAI guide PDF (binary), Karpathy talk transcript (paywalled notes only), McKinsey "One year of agentic AI" (timed out twice), 12-factor beyond factor 10, Google page's earlier version.
- The Cognition vs Anthropic multi-agent disagreement is partly a scoping difference (coding vs research) but has not been tested head-to-head.

## 4. Reconciling one-job-per-agent and single-agent-many-skills

They answer different questions, and the evidence supports a layered reading (judgment):

| Layer | Evidence-backed position |
|---|---|
| User-facing surface | one (Ramp's single agent; Claude Code; Glass). Reason: duplicated agents (four versions of the same agent at Ramp) and discoverability. |
| Unit of reliability (the loop) | small and bounded, about 3-10 steps, inside deterministic code ([12-factor](../../research/sources/humanlayer-12-factor-agents-small-focused-agents.md); [production survey](../../research/sources/arxiv-measuring-agents-in-production.md)). |
| Unit of packaging | skill or subagent per job inside the general harness ([Agent Skills](../../research/sources/anthropic-engineering-equipping-agents-agent-skills.md)); deployed agent only when a job needs its own runtime or governance. |
| Unit of review automation | narrow specialists plus a coordinator that dedupes and grades severity ([Cloudflare](../../research/sources/cloudflare-ai-code-review-opencode.md)), risk-tiered. |
| Interdependent work | keep in one context; do not parallelise across agents ([Cognition](../../research/sources/cognition-dont-build-multi-agents.md)); parallelise only breadth-first research ([Anthropic](../../research/sources/anthropic-multi-agent-research-system.md)). |

So "one job per agent" means one bounded loop per job, not necessarily one deployed agent per job; "single agent many skills" means one surface that dispatches to those bounded jobs. Where they truly conflict is governance: a skill in a general harness inherits the harness's permissions and cannot enforce a gate, whereas a deployed agent or workflow can (open question).

## 5. Fit of runtime patterns to classes

Pattern letters are from the research plan (A general harness + skills/subagents; B own harness on a framework/SDK; C meta-harness; D harness calling deployed task agents; E cloud/background agents; F shared persistent workspace; G workflow-engine-embedded agents; H portable skill/plugin ecosystem). Ratings are **judgment**, derived from the evidence cited; they are hypotheses for Geoff to test. S = strong fit, O = workable, W = weak, ? = no evidence.

| Pattern | C1 Open exploration | C2 Directed construction | C3 Repeatable standardised judgement | C4 Volume pipelines | C5 Accountable commitments |
|---|---|---|---|---|---|
| A General harness + skills/subagents | S (best-practices guidance, anecdotes) | S (verification loop) | O (skill gives shape, but no enforced gate; consistency unproven) | O (`claude -p`, `/batch`) | W alone (needs human owner); O as assistant |
| B Own harness on SDK/framework | O (Glass shows non-engineers use it) | O | S (can enforce gates, evals, audit; Ramp Policy Agent) | S | O (can embed approval flows) |
| C Meta-harness | ? (no evidence on exploration) | O | O (policy layer) | O | O (central audit) |
| D Harness calls deployed task agents (MCP/A2A) | W (interactive, iterative work fits badly; Glean advises short read-only jobs) | O | S for read-only, bounded review returning findings | O | O |
| E Cloud/background agents | W | S for fire-and-forget PRs with tests; mixed independent results (Answer.AI 3 of 20, existing note) | O | S | W |
| F Shared persistent workspace/session | O (shared thinking, hand-off) | O | O | O | S (shared artifact, trace) |
| G Workflow engine with embedded agents | W (too rigid) | O (Stripe blueprint) | S (deterministic gates, per-step evals) | S | S (explicit approval nodes) |
| H Portable skill ecosystem (distribution) | O (skills carry context) | O | S as the cheap packaging of a team standard; weak on enforcement | O | W |

Reading: A is the default for C1 and C2; G or B is the evidenced home for C3 and C4 once consistency and audit matter; D suits the read-only slice of C3; F matters mainly for C5 and for hand-offs. A hybrid in which the general harness calls a bounded, gated job (skill with hooks, or a deployed workflow) when the user enters a C3 or C4 step has the best fit on paper but little direct evidence.

## 6. Productising a team process as an agent or skill: what the cases show

- Ramp Policy Agent (existing note, first-party): started as suggestions, user-set auto-approve slider, weekly SME labeling, evals from about five examples; expense policy doc "acts like a CLAUDE.md". Autonomy and traceability moved in opposite directions as it went from chain to agentic loop.
- Cloudflare review ([note](../../research/sources/cloudflare-ai-code-review-opencode.md)): the team standard (Engineering Codex) is one of seven specialist reviewers; "what not to flag" is the key tuning surface; human override is logged.
- Stripe Minions ([note](../../research/sources/stripe-minions-one-shot-coding-agents.md)): team-required steps (lint, CI cap) are deterministic, creative work is agentic, every PR human-reviewed.
- Atlassian Rovo, Intercom Fin, Notion agents (existing notes, vendor/first-party): bounded jobs (feedback categorisation, weekly update, support resolution); reported failures include invented content (Rovo) and prompt-injection risk (Notion); no independent outcome data. Intercom and Zapier are support/ops, not PM review.
- Vercel (existing note): agents suit "low cognitive load, high repetition" jobs built by a domain expert, with human approval.
- Pattern: **the standard is encoded as (a) a rubric or exclusions the specialists read, (b) deterministic gates, (c) evals from SME-labelled examples, (d) a logged human override.** None of the cases uses a loose general agent for the standardised step; but none is a controlled comparison either.

## 7. Options by dimension

Dimension sections added or extended in [../../options/DIMENSIONS.md](../../options/DIMENSIONS.md):

- [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-and-what-agent-shape-fits): added options (structure added on demand inside the general harness; coordinator plus narrow specialists; deterministic wrapper around an agentic core) and key questions.
- [activity-classification](../../options/DIMENSIONS.md#activity-classification-how-we-classify-user-activity-for-agent-fit) (new, proposed): axes to classify work (single structure axis vs multi-axis vs worker-desired agency).
- [autonomy-calibration](../../options/DIMENSIONS.md#autonomy-calibration-who-sets-how-much-autonomy-an-agent-gets-and-how-it-changes) (new, proposed).
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-permissions-cost-identity-audit): added enforcement-by-hooks/gates option and key question.
- Key questions appended to [pm-job-sequencing](../../options/DIMENSIONS.md#pm-job-sequencing-which-pm-jobs-to-automate-first), [target-user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first) and [target-outcome](../../options/DIMENSIONS.md#target-outcome-which-outcome-or-value-we-target).

Structure proposals for the director:
- Consider **merging `review-gating` and `review-gate-placement`** (and `governance-control-plane`'s review/autonomy rows); the same choice appears in three places.
- Consider **merging `agent-unit` into `work-structure`** or keeping it clearly as "naming unit"; the one-job vs many-skills choice appears in both plus `capability-packaging`.
- **New dimension `activity-classification`** (proposed above) as the user-facing analogue of `work-structure`: work-structure is about the agent shape; classification is about how we decide which shape applies.
- **New dimension `autonomy-calibration`**: separate from review gates (gates are where, calibration is who sets how much and how it changes over time).

## 8. Open questions for Geoff

1. Is the unit you want to classify the **user** (a PM who sometimes ideates and sometimes reviews) or the **job step**? The evidence supports the step; a persona-level split would be hard to defend.
2. Which hypothesis do you most need settled: (a) "task agents beat skills in a general harness on standardised jobs" (no evidence either way; needs a bake-off), or (b) "ideation should stay unstructured" (guidance and anecdotes support it; nothing measured)? These need different research.
3. How much weight do you put on the **bitter-lesson counter-argument** (structure decays as models improve)? It affects whether to invest in encoding PM standards as workflows or as portable context (skills, rubrics, evals) that survive model changes.
4. For PRD review specifically: is the team's standard a **rubric (judgment against criteria)** or a **checklist (completeness)**? The evidence on noise (Cloudflare, CR-Bench) suggests narrow, exclusion-heavy specialists; a rubric of five or six criteria may need different design than a long checklist.
5. Do you need the **audit and enforcement** a deployed workflow gives (A5), or is a skill plus a logged human sign-off enough? This decides pattern G/B vs A/H for C3.
6. Is a shared, persistent session more valuable for C1 (shared thinking) or C5 (accountable commitments)? Evidence is thin on C1.
7. Who are the first users: individual PMs (C1/C2-heavy) or a team lead standardising a team process (C3-heavy)? The pattern fit differs sharply.

## 9. Source notes filed by this track

New: [openai-practical-guide-building-agents](../../research/sources/openai-practical-guide-building-agents.md), [langchain-how-to-think-about-agent-frameworks](../../research/sources/langchain-how-to-think-about-agent-frameworks.md), [anthropic-multi-agent-research-system](../../research/sources/anthropic-multi-agent-research-system.md), [google-cloud-choose-design-pattern-agentic-ai](../../research/sources/google-cloud-choose-design-pattern-agentic-ai.md), [humanlayer-12-factor-agents-small-focused-agents](../../research/sources/humanlayer-12-factor-agents-small-focused-agents.md), [arxiv-measuring-agents-in-production](../../research/sources/arxiv-measuring-agents-in-production.md), [arxiv-future-of-work-with-ai-agents](../../research/sources/arxiv-future-of-work-with-ai-agents.md), [arxiv-tau-bench](../../research/sources/arxiv-tau-bench.md), [metr-early-2025-experienced-developer-rct](../../research/sources/metr-early-2025-experienced-developer-rct.md), [anthropic-claude-code-best-practices](../../research/sources/anthropic-claude-code-best-practices.md), [anthropic-measuring-agent-autonomy](../../research/sources/anthropic-measuring-agent-autonomy.md), [anthropic-economic-index-2026-01](../../research/sources/anthropic-economic-index-2026-01.md), [anthropic-how-ai-is-transforming-work-at-anthropic](../../research/sources/anthropic-how-ai-is-transforming-work-at-anthropic.md), [arxiv-cr-bench](../../research/sources/arxiv-cr-bench.md), [hn-ask-claude-code-non-coding-workflows](../../research/sources/hn-ask-claude-code-non-coding-workflows.md), [latent-space-karpathy-software-3-notes](../../research/sources/latent-space-karpathy-software-3-notes.md), [traces-boris-cherny-light-cone-summary](../../research/sources/traces-boris-cherny-light-cone-summary.md).

Extended (existing notes from another pass of this task, appended a Track 6 section): stripe-minions-one-shot-coding-agents, cloudflare-ai-code-review-opencode, anthropic-engineering-equipping-agents-agent-skills.

**Incident to report:** `anthropic-building-effective-agents.md` and `cognition-dont-build-multi-agents.md` already existed (filed by another track agent) and I overwrote both before noticing. Their INDEX lines and THEMES bullets are intact and still match; my replacement notes carry the same source facts plus Track 6 themes, but any extra detail the first versions held (for example frontmatter themes such as `agent-frameworks`/`build-vs-buy` emphasis) may be lost. Worth a check by the owner.
