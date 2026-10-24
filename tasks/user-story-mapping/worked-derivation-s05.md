# Worked derivation: S05 in two contrasting embodiments

Story: [S05. Write and ratify a spec engineers can act on](stories-jobs.md#s05-write-and-ratify-a-spec-engineers-can-act-on). Recipe: [README](README.md#derivation-recipe-story--chosen-options--a-journey).

Why S05: it is multi-session, has real hand-offs (engineering lead, designer, a risk reviewer), and sits where "general harness with skills" and "task-specific shared agent" plausibly differ most. The two embodiments below are chosen for *contrast*, not because either is favoured. Neither is recommended.

Scenario (illustrative, invented for the walkthrough; not a real product): Sam, a PM, has to turn a chosen direction, "let finance approvers approve invoices in bulk", into a ratified spec. Reviewers: Priya (engineering lead), Jo (designer), and Alex from risk. Sam has research notes from S01 and a prototype from S04.

## 1. Need (copied from S05, unchanged)

Goal: turn a chosen solution into a spec complete enough for delivery, which engineering and design agree with. Done: an agreed spec in the team's form, open questions closed or owned, sign-offs recorded, evidence linked, stored where delivery and later specs can read it. Success criteria: few gaps at first review; fewer mid-delivery questions; meets the completeness standard if one exists; short time from decision to ratified spec; evidence per requirement traceable.

## 2. Embodiment profiles

| Dimension | Embodiment A: local harness + skills + shared repo | Embodiment B: deployed shared spec agent |
|---|---|---|
| [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives) | Local process on Sam's laptop | Org-deployed service |
| [loop-source](../../options/DIMENSIONS.md#loop-source-who-supplies-the-agent-loop) | Vendor harness as is | Org-owned agent built on a vendor SDK (details open) |
| [capability-format-portability](../../options/DIMENSIONS.md#capability-format-portability-capability-format-and-portability) | Skills (shaping skill, review skill) in a team-shared plugin or repo | Deployed agent, invoked from chat or a web page |
| [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent) | General harness plus skills | Task-specific agent for specs |
| [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff) | Ephemeral-private; sharing via files | Persistent and shared; the spec thread lives in the service |
| [session-persistence-sharing/session-handoff-portability](../../options/DIMENSIONS.md#sub-choice-session-handoff-portability--handing-a-session-between-people-devices-and-harnesses) | Branch/file hand-off (PR to the context repo) | People join the same thread |
| [context-and-memory/context-location](../../options/DIMENSIONS.md#sub-choice-context-location--where-product-context-lives-for-agents) | Shared plain-text context repo | Systems of record via connectors, plus a spec store |
| [intent-shaping-and-spec/intent-shaping-mode](../../options/DIMENSIONS.md#sub-choice-intent-shaping-mode--who-shapes-intent-and-how) | PM-led with a versioned shaping skill | Agent-led interrogation against a spec standard |
| [review-and-autonomy/review-gating](../../options/DIMENSIONS.md#sub-choice-review-gating--how-human-review-of-agent-output-is-gated) | Human reviews everything (reviewers read a PR) | Automated spec-standard check first; humans review flagged gaps and sign off |
| [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation) | Agent acts as Sam, with Sam's access | Service identity with scoped access; reviewers' rights must be reconciled with it |
| [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-governance-and-control-plane-policy-cost-audit) | Sam's own harness settings; cost on Sam's account | Per-run log and cost on the service |
| [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) | Repo-native convention: the project is a folder `projects/bulk-approval/` in the context repo with `spec.md`, `evidence/`, `decisions.md` and a short `PROJECT.md` descriptor; types and status are file frontmatter | Harness-defined typed artifacts: the project is an object with a spec (typed, versioned, status), evidence items, decisions and sign-offs; synced views to the ticket tool; permissions mirror source systems |
| [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model) | Skills discovered via team plugin/marketplace; Sam must set it up | Agent appears in the channels people already use |

## 3. Walk of TODAY's steps

| TODAY step (S05) | A | B |
|---|---|---|
| Gather research and prior decisions by hand | Delegated: the skill reads the context repo and Sam's research folder | Delegated: the agent pulls from connected systems and the spec store |
| Prompt for a PRD draft | Kept by Sam, but guided: the shaping skill asks the standard questions | Moved: the agent interrogates Sam; Sam answers |
| Edit | Kept | Kept (Sam edits in the thread/page) |
| Paste into a doc, circulate | Moved: spec committed to the repo, reviewers get a PR link | Removed: the thread *is* the shared document |
| Collect comments in several places | Partly kept: comments on the PR, but Slack side-talk persists | Removed: comments and answers land in the thread |
| Revise | Kept (Sam re-runs the review skill) | Kept (the agent re-runs the check on each revision) |
| Re-gather context for the next spec | Removed if the spec writes back to the repo | Removed if the spec store feeds the next run |
| Decide where it lives and what it's called (implicit today; see S16) | Moved earlier: the shaping skill scaffolds the project folder and `PROJECT.md` from the team template | Moved earlier: the agent creates the project object at step 1 and asks for owner and reviewers |

## 4. Journey A: local harness + skills + shared repo

Cast: Sam (PM) with a local agent session; Priya, Jo, Alex (reviewers); the context repo (Git).

| # | Actor | Action | Sam/reviewer sees | Artifact and where it lives | Gate or hand-off |
|---|---|---|---|---|---|
| 1 | Sam | Opens a terminal/desktop session in the product repo and runs the shaping skill by name; the skill scaffolds `projects/bulk-approval/` with `PROJECT.md` (owner, reviewers, sources, artifact types) | Skill greets with the standard question list, shows which context files it loaded and the new folder layout | Project folder and `PROJECT.md`; session transcript (local, ephemeral) | None |
| 2 | Agent | Reads the repo's research notes, the prototype description and past specs; lists what it found and what it could not | A short "what I read / what I couldn't find" list | None yet | Sam confirms or points to missing items |
| 3 | Sam + agent | Work through the questions; the agent drafts sections and marks unanswered ones `OPEN` | The draft spec in a file, `OPEN` markers highlighted | `projects/bulk-approval/spec.md` (frontmatter: type, status, owner, version) in the working tree | None |
| 4 | Agent | Runs the review skill: checks the draft against the team's completeness list and finds gaps and contradictions | A findings list pointing to spec lines | Findings file beside the spec | Sam decides which findings to fix |
| 5 | Sam | Commits to a branch and opens a PR in the context repo, tagging Priya, Jo, Alex | PR with the spec and the evidence links | PR in the repo | Hand-off: reviewers read in their normal tools |
| 6 | Priya, Jo, Alex | Review in the PR; each comments; Alex asks for a risk mitigation | Their comments on PR lines | PR comments | Human review of everything |
| 7 | Sam | Reopens a *new* session (the earlier one ended), asks the skill to "address PR comments" | The skill reads the PR and proposes edits | Updated spec on the branch | Sam approves edits |
| 8 | Reviewers | Approve | Approvals on PR | Merged spec; context repo updated with decisions | Ratification recorded as merge |
| 9 | Later | Next spec's session loads this spec as context; another PM asks the agent "what did we ratify for bulk approval?" and it reads the project folder | Agent cites it with status and version | Same repo | None |

Failure beat: at beat 7 Sam's earlier session transcript was cleaned up (default retention) and Sam is working from the PR only; the agent doesn't know why a decision was made at beat 3, so it re-proposes an option Sam rejected. Sam sees the same suggestion again and has to re-explain. Mitigation inside this embodiment: the spec's `Decisions` section captures reasons; otherwise the loss is real (S11).

Success criteria check: few gaps at first review: *met* if the review skill is good (unknown); fewer mid-delivery questions: *at risk* (not testable here); completeness standard: *met* only if the team keeps one; time to ratify: *at risk* (Sam is the relay between PR and agent); traceable evidence: *met* when links are kept in the file.

Assumptions and unknowns: Sam has access to the context repo and is comfortable with branches and PRs (or a tool hides them); reviewers will review in a PR rather than a document; a completeness list exists. → [context-and-memory/context-location](../../options/DIMENSIONS.md#sub-choice-context-location--where-product-context-lives-for-agents) Q3 (will engineering allow product context near code), [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model), and the `(user-story-mapping)` questions in [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) (Q2: will reviewers work in Git).

## 5. Journey B: deployed shared spec agent

Cast: Sam; the spec agent (deployed service with its own identity); Priya, Jo, Alex; connected systems (research store, ticket tool, spec store).

| # | Actor | Action | Sam/reviewer sees | Artifact and where it lives | Gate or hand-off |
|---|---|---|---|---|---|
| 1 | Sam | Messages the spec agent in the product channel: "start a spec for bulk invoice approval" and attaches the prototype link; the agent creates the project (asks owner, reviewers) | A thread opens with a link to the project page showing its artifact slots (spec, evidence, decisions, sign-offs) | Project object + spec thread in the service | None |
| 2 | Agent | Pulls research notes, the prototype and prior related specs from connected systems; posts what it used and what is missing | "Used 6 sources, could not find pricing constraints; who owns that?" | Source list on the page | Sam answers or names an owner |
| 3 | Agent | Interrogates Sam against the team's spec standard, one cluster of questions at a time | Questions in the thread; completeness meter on the page | Answers recorded on the page, each with its author | None |
| 4 | Agent | Drafts the spec; runs the standard check automatically; lists gaps | Draft + gap list; unresolved items tagged to owners | Versioned spec in the spec store | Automated check |
| 5 | Agent | Notifies Priya, Jo, Alex with what each needs to look at (feasibility, usability, risk) | A message with a link to their section | Review requests on the page | Hand-off: reviewers join the same thread |
| 6 | Priya, Jo, Alex | Answer in the thread/page; the agent updates the draft and re-checks | Live edits, a change log | Thread history; spec versions | Human review of flagged gaps and sign-off |
| 7 | Sam | Returns two days later in any device; opens the thread | Full history and where things stand | Same thread | None (continuity from the service) |
| 8 | Reviewers | Sign off on the page | Sign-offs recorded with names and versions | Ratified spec (typed, versioned, status ratified) in the project, linked from tickets | Ratification |
| 9 | Agent | Offers to create tickets from the ratified spec | Draft tickets for engineering review | Tickets in the ticket tool | Engineering review (S07) |

Failure beat: at beat 5 Alex is not in the channel and cannot open the thread; or, worse, the thread is visible to everyone in a public channel including content only risk should see. Sam sees "Alex has no access" or learns after the fact. The agent's service identity can read more than any individual reviewer, so channel membership becomes an access boundary the team must have designed on purpose.

Success criteria check: few gaps at first review: *met* if the automated standard check is good (unknown; depends on there being a standard); mid-delivery questions: *at risk* (not testable here); completeness standard: *met by construction*, which is a cost: the standard has to exist first; time to ratify: *met more plausibly* since there is no manual relay; traceability: *met* if answers and sources are attached on the page.

Assumptions and unknowns: connectors exist for research, prior specs and tickets; the org will host a persistent service and name an owner; a spec standard exists and is machine-checkable; the agent's identity and the reviewers' permissions can be reconciled. → [runtime-location](../../options/DIMENSIONS.md#runtime-location-where-the-agent-runtime-lives) Q2/Q5, [agent-identity-delegation](../../options/DIMENSIONS.md#agent-identity-delegation-agent-identity-and-delegation) (the shared-thread permissions question), [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-governance-and-control-plane-policy-cost-audit), [intent-shaping-and-spec/spec-standard](../../options/DIMENSIONS.md#sub-choice-spec-standard--what-counts-as-agent-ready-intent), [target-user/shared-agent-users-and-jobs](../../options/DIMENSIONS.md#sub-choice-shared-agent-users-and-jobs--which-users-and-jobs-a-shared-persistent-agent-serves-first).

## 6. What the contrast shows

Artifact and project structure is a real difference between the two: A's structure is a folder convention plus frontmatter that people and the skill keep to, so it survives any harness but depends on discipline and Git literacy. B's structure is enforced by the service (typed slots, status, version, sign-offs), so reviewers need nothing but a link, but the types and project definition belong to whoever built the service. The unknowns for both are in the key questions of [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) (Q1, Q4, Q6, Q9).

| Beat that differs | A | B |
|---|---|---|
| Where the work lives while it is in progress | Sam's laptop, then a repo branch | The service |
| Who relays between reviewers and the agent | Sam | Nobody (the agent) |
| What a reviewer needs to do to take part | Open a PR | Open a link in chat |
| What survives if Sam disappears for a week | The repo (not the reasoning) | The thread and its history |
| What must exist before the first use | A convention, a skill, a context repo | A deployed service, connectors, an owner and a spec standard |
| Main failure risk | Lost reasoning and relay burden | Access scope and a never-ending requirement to maintain the service |
| What a "project" is | A folder with a descriptor, by convention | An object the service defines |
| How the next person finds the ratified spec | Opens the folder or asks an agent reading it | Queries the project for the ratified spec |

The decision between A and B is not made here. It hinges on facts we lack, now filed as key questions in DIMENSIONS.md (see INDEX).

## 7. Prototype and video hooks

Must-show screens: A (add the project folder layout and `PROJECT.md` at beat 1): the skill's "what I read / couldn't find" list (beat 2), the PR with the spec and findings (5), the "address PR comments" run in a fresh session (7). B: the thread with source list (2), the interrogation with completeness meter (3), reviewers answering inside the thread (6), the returning-Sam view (7).

Contrast beats for a side-by-side video: beats 5–7 (how reviewers join and how Sam picks up later) and the two failure beats. Narration alone is enough for beats 1, 8, 9.

Both journeys can run on the same fixture: one invented spec, three reviewers, one risk mitigation, one forgotten decision. That keeps the videos comparable.
