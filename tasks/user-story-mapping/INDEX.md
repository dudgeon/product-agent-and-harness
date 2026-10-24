# User story mapping: index

Task note: [user-story-mapping](../user-story-mapping.md). Format, evidence tags and derivation recipe: [README](README.md). Backbone: the [PM jobs-to-be-done map](../research-pm-agents-jobs-to-be-done/01-jobs-to-be-done-map.md).

Baseline for every "Today" section: inconsistent Claude Code use with poor artifact management (Geoff's definition). Stories are performer-agnostic; the unit is the PM job.

## Job stories ([stories-jobs.md](stories-jobs.md))

| ID | Story | JTBD job | Span | Variants (dimensions they lean on) |
|---|---|---|---|---|
| [S01](stories-jobs.md#s01-turn-a-batch-of-customer-conversations-into-what-we-learned) | Turn a batch of customer conversations into what we learned | J1 | multi-session | runtime, capability-packaging, intent-shaping, review gating |
| [S02](stories-jobs.md#s02-triage-incoming-feedback-into-ranked-themes) | Triage incoming feedback into ranked themes | J10 (J1) | recurring | runtime, persistence, autonomy |
| [S03](stories-jobs.md#s03-form-a-view-of-the-market-and-competitors) | Form a view of the market and competitors | J2 | multi-session | context-location, persistence, handoff |
| [S04](stories-jobs.md#s04-explore-solution-options-and-make-something-to-react-to) | Explore solution options and make something to react to | J3 | multi-session | runtime, work-structure, handoff |
| [S05](stories-jobs.md#s05-write-and-ratify-a-spec-engineers-can-act-on) | Write and ratify a spec engineers can act on | J4 | multi-session | persistence, intent-shaping, spec-standard, review gating. **Worked derivation** |
| [S06](stories-jobs.md#s06-decide-whats-next-prioritise-and-maintain-the-roadmap) | Decide what's next: prioritise and maintain the roadmap | J5 | recurring | grounding, autonomy, memory |
| [S07](stories-jobs.md#s07-know-where-delivery-stands-and-unblock-it) | Know where delivery stands and unblock it | J6 | recurring | grounding, runtime, review gate placement |
| [S08](stories-jobs.md#s08-get-a-launch-ready) | Get a launch ready | J7 | multi-session | work-structure, persistence, governance |
| [S09](stories-jobs.md#s09-tell-stakeholders-where-we-stand) | Tell stakeholders where we stand | J8 | recurring | review gating, runtime, governance |
| [S10](stories-jobs.md#s10-read-the-metrics-and-decide) | Read the metrics and decide | J9 | recurring | grounding, autonomy, memory |

## Cross-cutting stories ([stories-cross-cutting.md](stories-cross-cutting.md))

| ID | Story | Span | Variants (dimensions) |
|---|---|---|---|
| [S11](stories-cross-cutting.md#s11-pick-up-where-i-or-someone-else-left-off-and-find-the-artifacts) | Pick up where I (or someone else) left off, and find the artifacts | multi-session | context-location, persistence, durability |
| [S12](stories-cross-cutting.md#s12-get-the-agent-to-know-our-product-and-organisation) | Get the agent to know our product and organisation | recurring | context-location, grounding, memory |
| [S13](stories-cross-cutting.md#s13-hand-work-to-a-teammate-and-get-their-input) | Hand work to a teammate and get their input | multi-session | handoff, persistence, governance |
| [S14](stories-cross-cutting.md#s14-have-recurring-work-happen-without-me-prompting) | Have recurring work happen without me prompting | recurring | runtime, governance |
| [S15](stories-cross-cutting.md#s15-know-whether-i-can-trust-what-came-back) | Know whether I can trust what came back | sitting | review gating, autonomy, evaluation |

| [S16](stories-cross-cutting.md#s16-start-a-piece-of-work-with-a-defined-project-and-the-right-artifacts) | Start a piece of work with a defined project and the right artifacts | sitting | artifact-and-project-structure, adoption |
| [S17](stories-cross-cutting.md#s17-find-and-reuse-an-earlier-artifact-across-tools) | Find and reuse an earlier artifact across tools | sitting | artifact-and-project-structure, grounding |
| [S18](stories-cross-cutting.md#s18-share-an-artifact-with-a-multi-party-team-and-keep-it-correct) | Share an artifact with a multi-party team and keep it correct | multi-session | artifact-and-project-structure, handoff, governance |

S16–S18 were added after the artifact-management follow-up; S01 and S08 also gained V4 variants in the audit. Research: [platforms](research-artifacts-platforms.md), [standardization](research-artifacts-standardization.md). Job stories S02–S06, S09, S10 each gained a V4 artifact-structure variant; S11–S13 were rewritten around the research.

## Worked derivation

[S05 in two contrasting embodiments](worked-derivation-s05.md): A = local general harness with skills and a shared context repo; B = deployed, shared, task-specific spec agent. Model for later journeys, prototypes and videos.

## Key questions this raised (filed in options/DIMENSIONS.md)

New dimension: [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found), with 10 key questions. Reconciliation with context-location, org-context-grounding-source and memory-design is noted in the dimension; a merge is the director's call.


Added to [context-and-memory/context-location](../../options/DIMENSIONS.md#sub-choice-context-location--where-product-context-lives-for-agents), [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff) (and its handoff sub-choice), [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives), [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent), [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation) (the director moved the shared-thread permissions question there from governance), [review-and-autonomy/review-gating](../../options/DIMENSIONS.md#sub-choice-review-gating--how-human-review-of-agent-output-is-gated), [sequencing/pm-job-sequencing](../../options/DIMENSIONS.md#sub-choice-pm-job-sequencing--which-pm-jobs-to-automate-first), [target-user](../../options/DIMENSIONS.md#target-user-which-users-and-personas-we-serve-first-including-for-shared-agents), [pm-agent-evaluation](../../options/DIMENSIONS.md#pm-agent-evaluation-how-we-would-know-a-pm-agent-works) and the cross-cutting list. Each is tagged `(user-story-mapping)`. Unranked. Dimension slugs in the stories follow the consolidated register (`parent/sub` for sub-choices).

The three facts the stories most often hinge on: how PMs keep artifacts today; whether reviewers will enter agent sessions; whether a machine-checkable spec standard exists.
