# Modular user stories for PM work: format and derivation recipe

Task: [user-story-mapping](../user-story-mapping.md). Filed 2026-10-24. Index of stories: [INDEX.md](INDEX.md).

## What these stories are

A **modular story** fixes the *need* and leaves the *approach* open. It says who is doing what job, why now, what "done" is and how we'd know it went well, and nothing about which product feature serves it. The same story can then be told as a journey in many harness embodiments (local general harness with skills, deployed shared task agent, desktop workspace, and so on). That journey is the input to prototypes and walkthrough videos.

Decisions Geoff made when checking the format (2026-10-24):

- **Stories first, solutions later.** Each story is plain. Variants come last and stay short; dimension options are only used to *name* variants, never to define the need.
- **Performer-agnostic.** The unit is the PM *job*, not the person. The performer can be a PM, analyst, designer or engineer. Stories name the job and the performer role in the trigger, but are always written from the point of view of whoever is doing the job.
- **Spans.** A story may run across days. Each story marks its span: *sitting* (one sitting), *multi-session* (days, with a hand-off to self or others) or *recurring*.
- **Today (the baseline) is inconsistent Claude Code use with poor artifact management.** It is not a no-AI PM. This is Geoff's statement of the baseline, marked `[G]`. A one-line "before agents" note appears only where it helps.

## Story format

Every story has these sections, in this order.

```
### S<nn>. <name, written as the performer's outcome>
Source job: <J-id from the JTBD map>   Span: sitting | multi-session | recurring

NEED (fixed: this is the part that does not vary by embodiment)
- Performer: <role doing the job; who else is involved>
- Goal: <what they are trying to get done, in their words>
- Trigger and context: <what makes them start; what state the world is in>
- Done looks like: <the observable end state, including where the result lives>
- Success criteria: <how we would tell it went well: quality, time, trust, reuse>

TODAY (baseline: inconsistent Claude Code use, poor artifact management)
- Steps: <what people actually do now>
- Tools: <what they touch>
- Pain: <specific pains, each tagged with evidence>
- Hand-offs: <who they depend on or give to>
- Time cost: <how long, or "not established">
- Before agents (optional, one line)

VARIANTS (ways an agent or harness could serve it; short)
- V<n> <name>: <what changes for the performer: who does what, where the human stays in the loop, what they see>
  Varies by: <dimension slugs>   Hinges on: <the unknown that decides whether this fits>
```

### Evidence tags (used in Today sections)

| Tag | Meaning |
|---|---|
| `[G]` | Stated by Geoff (baseline definition or experience). Not independently evidenced. |
| `[E: source]` | Supported by a source note in `../../research/sources/`. The note says whether it is first-party, independent, vendor claim or anecdote; follow the link for that. |
| `[A]` | Assumed by this task. Plausible from the job map or general experience; no source. These are candidates for a user interview. |
| `[E: findings §n]` | Points at a section of this task's own research syntheses ([platforms](research-artifacts-platforms.md), [standardization](research-artifacts-standardization.md)), which link on to the source notes. |

Time cost is rarely sourced. Where we have only a vendor or survey number it is quoted with its caveat; otherwise it says "not established" and `[A]` gives an order of magnitude only to help prototypes pick a realistic scale.

## Variants and dimensions

A variant names a *distinct way* an agent or harness could serve the need. To keep the menu comparable, each variant is tagged with the [options/DIMENSIONS.md](../../options/DIMENSIONS.md) dimensions it varies by. The ones these stories use most:

| Dimension slug | What varies in the PM's experience |
|---|---|
| [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives) | Is the work done on my laptop, in a vendor cloud session, or by an org-deployed service? Does it run when I'm away? |
| [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff) (sub-choices [session-handoff-portability](../../options/DIMENSIONS.md#sub-choice-session-handoff-portability--handing-a-session-between-people-devices-and-harnesses) ) | Is the session mine and gone when closed, resumable, shared live, or an always-on thing others can address? How does work pass between people or devices? |
| [capability-format-portability](../../options/DIMENSIONS.md#capability-format-portability-capability-format-and-portability) | Do I invoke a skill in my harness, call a deployed agent, or use an always-on context file? ([capability-distribution-trust](../../options/DIMENSIONS.md#capability-distribution-trust-capability-distribution-and-trust) covers how it reaches me and whether it is trusted.) |
| [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent) (sub-choice [work-structure/agent-unit](../../options/DIMENSIONS.md#sub-choice-agent-unit--persona-job-or-stage-as-the-unit-of-an-agent)) | General harness for everything, or a task-specific agent per job? |
| [review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy) (sub-choices [review-and-autonomy/review-gating](../../options/DIMENSIONS.md#sub-choice-review-gating--how-human-review-of-agent-output-is-gated), [review-and-autonomy/review-gate-placement](../../options/DIMENSIONS.md#sub-choice-review-gate-placement--where-review-gates-sit-on-pm-agent-output), [review-and-autonomy/autonomy-calibration](../../options/DIMENSIONS.md#sub-choice-autonomy-calibration--who-sets-how-much-autonomy-an-agent-gets-and-how-it-changes)) | Where is the human looking, at what, and who decides how far the agent goes alone? |
| [context-and-memory](../../options/DIMENSIONS.md#context-and-memory-context-and-memory) (sub-choices [context-and-memory/context-location](../../options/DIMENSIONS.md#sub-choice-context-location--where-product-context-lives-for-agents), [context-and-memory/org-context-grounding-source](../../options/DIMENSIONS.md#sub-choice-org-context-grounding-source--how-organisation-context-reaches-the-agent), [context-and-memory/memory-design](../../options/DIMENSIONS.md#sub-choice-memory-design--memory-design)) | Where does the agent get product and org knowledge, and what does it remember? |
| [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) | What is a project here, which artifact types exist, where do they live, and how does anyone (human or agent) find, trust and share them? Always part of the profile when the story produces or consumes artifacts. |
| [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation) | Whose identity does the agent act under, and who may direct it or see what it holds? |
| [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-governance-and-control-plane-policy-cost-audit) | What does it cost, what is logged, what policy applies? |
| [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model) | How does the performer find out this exists and learn to use it? |
| [intent-shaping-and-spec](../../options/DIMENSIONS.md#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard) (sub-choices [intent-shaping-and-spec/intent-shaping-mode](../../options/DIMENSIONS.md#sub-choice-intent-shaping-mode--who-shapes-intent-and-how), [intent-shaping-and-spec/spec-standard](../../options/DIMENSIONS.md#sub-choice-spec-standard--what-counts-as-agent-ready-intent)) | Who drives the thinking: the performer, or the agent interrogating them? What counts as a complete spec? |
| [loop-source](../../options/DIMENSIONS.md#loop-source-who-supplies-the-agent-loop), [harness-layering](../../options/DIMENSIONS.md#harness-layering-is-there-a-layer-above-the-vendor-harnesses), [durability-substrate](../../options/DIMENSIONS.md#durability-substrate-how-persistence-and-recovery-are-implemented) | Rarely a story-level variant; they appear in embodiment profiles (who supplies the loop, whether a layer sits above harnesses, how persistence is implemented). |

Slug convention: `parent/sub` names a sub-choice inside a consolidated dimension (the register was consolidated on 2026-10-24; old slugs such as `context-location` or `review-gating` now live as sub-choices).

Artifact and project structure is a dimension that touches nearly every story: S11, S12, S13 and S16–S18 are written around it, and job stories carry a variant for it.

Product and user dimensions ([target-user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first-including-for-shared-agents), [sequencing/pm-job-sequencing](../../options/DIMENSIONS.md#sub-choice-pm-job-sequencing--which-pm-jobs-to-automate-first), [target-outcome](../../options/DIMENSIONS.md#target-outcome-which-outcome-or-value-we-target), [pm-agent-evaluation](../../options/DIMENSIONS.md#pm-agent-evaluation-how-we-would-know-a-pm-agent-works)) are not variants of a story; they are about *which stories matter first* and *how success is judged*. The stories' success criteria feed `pm-agent-evaluation`.

## Derivation recipe: story + chosen options = a journey

A **journey** is one story told in one embodiment: a concrete sequence of beats a person goes through, with what they see and what artifacts are made. Use these steps.

1. **Fix the need.** Copy the story's NEED block unchanged. If a journey cannot meet the success criteria, that is a finding about the embodiment, not a reason to edit the need.
2. **Choose the embodiment profile.** Pick one option per dimension that matters for this story (usually the six to eight in the story's "Varies by" lines). **Always include artifact-and-project-structure** for any story that produces or consumes artifacts: say what a project is in this embodiment, which artifact types it uses, where each lives, and who can see them. Write it as a table: dimension, option (use names from DIMENSIONS.md). Name the profile in a few words (e.g. "local harness + skills + shared repo"). Dimensions not chosen are marked "n/a" or "default"; do not leave them silently open.
3. **Walk TODAY step by step.** For each baseline step mark one of: *kept by the performer*, *delegated to the agent*, *removed*, *moved to someone else*, *moved earlier or later*. The profile decides which. Write down why in a few words.
4. **Pick the variant(s) that match the profile.** A story's variants are patterns; the profile selects one or combines two. Note where the profile does not fit any listed variant: that is a new variant for the story.
5. **Write the beats.** One row per beat: *actor* (performer, agent, teammate, system), *action*, *what the performer sees* (screen, message, file), *artifact and where it lives*, and whether a gate or hand-off occurs. Include: how the work starts (trigger path), where context comes from, which project and artifact types it belongs to, the first output, the review beat, the hand-off beat (if any), and where the final artifact ends up (project, type, status, version) and how someone finds it later.
6. **Add one failure beat.** The most likely way this goes wrong in this embodiment (stale context, wrong source, laptop closed, teammate lacks access) and what the performer sees and does. Take it from the story's Pain list or from the failure modes research ([agent-failure-modes](../../research/THEMES.md#agent-failure-modes-recurring-agent-failure-modes-in-pm-work)).
7. **Check against success criteria.** For each criterion say *met*, *at risk* or *not met* and why. Do not tune the journey to make everything green.
8. **List assumptions and unknowns.** Any beat that depends on something not established (a connector exists, a policy allows it, a latency is acceptable) is flagged. Each unknown maps to a key question in DIMENSIONS.md, and where none exists, one is added.
9. **Prototype and video hooks.** Say which beats must be shown on screen to make the embodiment legible (the minimum set of screens), which can be narrated, and which are the *contrast beats* that differ from the other embodiments. Videos should be built around contrast beats.

### Journey template

```
## Journey: S<nn> in <embodiment name>
Profile: table of dimension -> option
Cast: performer, agent(s), teammates, systems
Walk of TODAY steps: step -> kept / delegated / removed / moved (why)
Beats: # | actor | action | performer sees | artifact and where it lives | gate or hand-off
Failure beat
Success criteria check
Assumptions and unknowns -> key questions
Prototype and video hooks: must-show screens, contrast beats
```

A fully worked example (S05 in two contrasting embodiments) is in [worked-derivation-s05.md](worked-derivation-s05.md). It is the model for later journeys.

## Rules this set follows

- Needs never mention features. If a variant seems to belong in the Need, rewrite the Need until it doesn't.
- No variant is recommended and none is ranked. Where one variant plainly depends on a missing fact, the "Hinges on" line says so and the fact is a key question in DIMENSIONS.md.
- Evidence for Today comes from the research library. The first pass did no new web research; the artifact-management follow-up added 40 source notes ([platforms](research-artifacts-platforms.md), [standardization](research-artifacts-standardization.md)).

## Limits

- Today sections lean on the [JTBD map](../research-pm-agents-jobs-to-be-done/01-jobs-to-be-done-map.md), the [in-practice cases](../research-pm-agents-jobs-to-be-done/03-in-practice-cases-and-failures.md) and [Geoff's Intent Factory doc](../../research/sources/geoff-building-accelerating-intent-factory.md). Those are mostly vendor surveys, talks and anecdotes; no source documents how a PM *with inconsistent Claude Code use* manages artifacts. That baseline is `[G]` and `[A]` throughout and is the single biggest candidate for a short user interview round (key questions added to [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) and [context-and-memory/context-location](../../options/DIMENSIONS.md#sub-choice-context-location--where-product-context-lives-for-agents)).
- Time costs are mostly not established.
- Variants use the dimensions as consolidated in DIMENSIONS.md on 2026-10-24 (23 dimensions, sub-choices for the merged ones). The audit log is [audit-2026-10-24.md](audit-2026-10-24.md).
