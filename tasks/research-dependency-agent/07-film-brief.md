# Brief for the follow-on film: the dependency agent, v2

Date: 2026-10-28, revised the same day after Scoping direction: a simpler scenario, no character names, and a banking example. Written by the research-dependency-agent worker as the last deliverable of the research round; the film itself is a separate task. Film 13 (`explainers/projects/13-dependency-agent-vignette`) is the draft this replaces. This brief says what the better film should say, who it is for, the scenario, what to keep from film 13 and what to change, and which scenes the research supports. Evidence references are to `../../research/sources/`, with labels.

## Audience

Product, marketing and platform leaders in large, matrixed, platform-centric banks and other regulated companies, deciding whether to fund a dependency agent and what to ask of their platform teams. Secondary: the second line (risk, compliance, audit), who need to see that the agent makes gates easier to satisfy and never easier to skip. Geoff, as the first reader.

## The scenario

A large retail bank, fictional and unnamed ("the bank"). Its marketing team wants to launch an offer for a personal loan product on the home screen of the bank's servicing app, the app existing customers use to check balances and pay bills. The feature is small to describe and touches a lot: that is the point.

Roles, not names. On screen, people are their roles: **the marketing product manager** (the person steering the session), **the app platform owner**, **the offers and decisioning owner**, **the loan product owner**, **the data owner**, **the compliance reviewer**, **the release manager**. Agents are hexagons; people are circles in the accent colour; other teams' agents carry a dashed ring, as in film 13.

Two phases, not three: **show the offer** (a placement on the home screen, to eligible customers, with compliant wording) and **apply in the app** (tap through to a pre-filled application). The research says the slow edges are support functions and governance, so the dependencies should be weighted that way.

The dependencies the agent finds, by the taxonomy's six classes ([09](09-dependency-taxonomy.md)); about a dozen, not thirty-one:

| Class | Dependency | Who resolves it |
|---|---|---|
| Build | A home-screen placement slot in the app's content system | The app platform owner |
| Build | An eligibility call to the offers and decisioning engine | The offers and decisioning owner |
| Build | A pre-filled application route into loan origination (phase two) | The loan product owner |
| Grant | Customer data for eligibility (balances, existing products, marketing consent) | The data owner |
| Grant | A registered client for the decisioning API, with non-production credentials | The platform's intake |
| Decide | Financial-promotion sign-off on the wording (the offer is a regulated promotion) | The compliance reviewer |
| Decide | Fair-lending and model-risk screen, if eligibility uses a model | The second line |
| Decide | Privacy screen on targeting existing customers with their own data | The privacy team |
| Decide | Change authority for the app release | The change authority |
| Fund | The decisioning team's capacity: the work is not on their plan | The owners' product owner, via a demand |
| Time | The app's release train and the store review window; a year-end change freeze | The release manager |
| Tell | Whether "pre-approved" may appear on the home screen before an eligibility check has run, which decides whether phase one can ship without phase two's plumbing | The compliance reviewer, as the person who knows |

The "could not find" list on day one, four items: the offers engine's listed owner has moved teams; the app platform has no written intake for a home-screen slot (the last two teams asked in a chat channel); no lead time is published for financial-promotion review; and the catalogue and the decisioning runbook disagree about whether eligibility can be called in real time.

The one question for a person: the marketing PM asks the compliance reviewer whether a home-screen message that says "you may be eligible" is a financial promotion that needs the full sign-off, or a service message. The answer (it is a promotion; a softer wording is a service message, and here is the wording that has been approved before) is recorded with the reviewer as owner, the date and the policy reference, and decides the phase-one design.

The re-plan: the decisioning release slips two weeks; phase one is unaffected because the softer wording needs no eligibility call; phase two slides one train; two owners hear once.

Six weeks later: a different team wants to put a savings offer on the same home screen. Its agent starts with most of the map already verified, the placement intake now written down by the app platform owner because asks arrived in one shape, and the measured wait times per platform and gate.

Why banking fits better than the insurer: the strongest regulated-org evidence in the library is from banking regulators and banks (the FCA's million-change review, the Swedbank sanction, EU DORA's dependency map, the two Australian banks' pipeline change approval, ING's platform story, a bank's near-chance risk scoring), so each beat can carry a labelled evidence card from the same sector.

## What the film must carry

Five concepts, in this order, because each needs the one before it:

1. **What a dependency is, and why the slow ones are not the obvious ones.** The placement and the API call are the easy edges; the promotion sign-off, the data terms, the demand and the "may we say pre-approved" question are where the time goes ([Tkalich et al.](../../research/sources/arxiv-tkalich-critical-dependencies-cse.md), independent; [FCA](../../research/sources/fca-implementing-technology-change.md), regulator).
2. **Why it is hard here.** Mandatory gates that never say no and still take weeks; onboarding as a cascade of queues with no published lead time; records stale by default; the dependency map itself now a legal artefact ([02-challenges.md](02-challenges.md)).
3. **What doing it well is worth, honestly.** Lead with the cost side, which is independent: waiting, chasing, late discovery, fat-tailed overruns, a fine for a skipped gate. Benefit figures as labelled illustrations ([03-value.md](03-value.md)).
4. **The destination and the road.** Seven kinds of value; two axes; the rule that the environment moves one step ahead of the agent ([04](04-destination.md), [05](05-maturity-model.md)).
5. **The first move.** Map, ask, record: the loop that makes the record better and produces the measurement nobody has; the agent-ready checklist a platform owner can act on ([06-mvp.md](06-mvp.md)).

## The arc

Film 13 is a story about an agent that works. The better film is a story about a bank that becomes legible, with the agent as the reason. The centre of gravity moves from "look what the agent found" to "look what the bank now knows that it did not know before, and what that is worth". About six minutes.

- **Open on the cost, not the agent.** The marketing PM's feature, today, without an agent: three intake routes in three shapes (a form, a demand with a business case, a chat message to someone who knows someone); a promotion-review queue of unknown length; the "pre-approved" question surfacing in week nine from a compliance reviewer who happened to see a mock-up; the knowledge leaving with the people. One labelled evidence card per beat.
- **Name the problem precisely.** The six classes as a legend; the slow edges highlighted; the gate that approves over 90% and still takes weeks; the registers that were 6.5% clean. The film's line: this is not a planning problem, it is a legibility problem.
- **The agent as a reader first.** It walks what exists, draws the map, and the hero object is the **"could not find" list**: the owner who moved, the intake nobody wrote down, the lead time nobody measured, the two records that disagree. The map is partial and says so.
- **The loop.** Asks drafted as the smallest question, riding real needs, grouped by owner; the PM sends them; owners answer in the session; every answer written back provisional, then verified, with owner, date and source; the stale runbook line struck through and corrected at its home with the owner's consent. The second time the same question is asked, by another team, the answer is there.
- **The one question for a person.** The compliance reviewer and the wording, kept from film 13's shape because it is the clearest statement of what the agent does not decide.
- **The gate scene.** A change record opened with its evidence linked; the privacy and model-risk screens run from published criteria and pre-filled; the promotion sign-off prepared for a person and never decided by the agent; the line "easier to satisfy, never easier to skip".
- **The environment moves.** The app platform owner, seeing asks arrive in one shape, writes down the placement intake and a lead time; the next team's map on that platform is complete. This is the beat film 13 lacks: the organisation changing because the agent gave it a reason to.
- **The maturity picture, in one drawn frame.** Two axes, the four cells that matter, the trap, the rule.
- **Close on the measurement and the choice.** Wait time per platform and gate, verification rate, reuse rate, as the three numbers the first quarter produces; the agent-ready checklist; and the funding question the viewer is left with: which two platforms first.

## What to keep from film 13

- The four node shapes and the graph by phase; the context layer panel with owner, date and source rows that write themselves; the persistence beats (days passing, an owner answering from a phone, another team's agent posting its release slots); the re-plan; the SME question written back; the "illustrative" tag on every figure.
- The motion grammar and the plate look, per the project's film rules.

## What to change

- **Switch the company, the feature and the cast.** A fictional unnamed bank; a loan offer on the servicing app's home screen; roles instead of names; two phases; about a dozen dependencies. Film 13's insurer, its people and its thirty-one dependencies are retired for the film (the written deliverables keep the insurer example, labelled fictional).
- **Open on today, not on the agent.** Thirty to forty seconds of the status quo, with independent evidence on screen, earns the rest.
- **Make the "could not find" list the hero object of the discovery scene**, not the dependency count.
- **Show the loop, not the agent, improving the record**, and add the second-order effect: a platform owner changes what they publish because of how the asks arrive.
- **Add the gate scene.** The second-line viewer needs it, and banking is where the evidence for it is strongest.
- **Replace film 13's closing figures** with the three measurements the MVP produces and one labelled independent figure on the cost side. The research found no audited figure for discovery time, so the film should not imply one; it can show the bank measuring for the first time.
- **Cut the channel detail** in the routing scene in favour of "the smallest question, to the owner, through the channel they read".
- **Add one frame of the agent-ready checklist** at the end, as the thing a platform owner in the audience can do on Monday.

## Candidate scenes and the evidence behind each

| Scene | What it shows | Evidence (label) |
|---|---|---|
| S1 Today | Three intake routes, one queue of unknown length, a question surfacing in week nine, knowledge leaving | [Equal Experts](../../research/sources/equalexperts-smith-escape-ticketing-hell.md) (anecdote: eleven weeks for access at a Dutch bank); [Herbsleb and Grinter](../../research/sources/herbsleb-grinter-conways-law-revisited.md) (independent); [Stack Overflow 2024](../../research/sources/stackoverflow-dev-survey-2024-professional-developers.md) (independent); [Microsoft Research](../../research/sources/microsoft-research-coordination-large-scale-development.md) (independent: 49% chase status) |
| S2 The problem named | Six classes as a legend; slow edges; the gate that approves over 90%; registers 6.5% clean; the map as a legal artefact | [Tkalich](../../research/sources/arxiv-tkalich-critical-dependencies-cse.md) (independent); [FCA](../../research/sources/fca-implementing-technology-change.md) (regulator); [ESAs](../../research/sources/esas-dora-dry-run-register-of-information.md) (regulator); [EU DORA](../../research/sources/eu-dora-regulation-ict-risk-third-party.md) (law); [DORA 2019](../../research/sources/dora-state-of-devops-2019.md) (independent) |
| S3 The reader | The walk of the context layer; the map by phase; the "could not find" list; two records that disagree | [LEREDD](../../research/sources/arxiv-darif-leredd-requirement-dependencies.md) (independent, over-prediction); [Port survey](../../research/sources/port-state-of-idp-2025-metadata-trust.md) (vendor); [GitHub](../../research/sources/github-docs-about-code-owners.md) (first-party, silent owner drop) |
| S4 The loop | Smallest questions riding real asks; owners answer; provisional then verified; the stale runbook corrected at its home; the second team's instant answer | [Shopify River](../../research/sources/shopify-engineering-river-vulnerability-remediation.md) (first-party); [Stripe panel](../../research/sources/stripe-sessions-2024-10x-engineer-panel.md) (first-party); [Nudge](../../research/sources/arxiv-maddila-nudge-overdue-pull-requests.md) (first-party, randomised); [OpsLevel](../../research/sources/opslevel-docs-service-detection.md) (first-party, inferred-then-confirmed owners) |
| S5 One question for a person | The compliance reviewer and the wording, written back with their role, the date and the policy reference | [ICO](../../research/sources/ico-when-do-we-need-a-dpia.md) (regulator, published screening as the pattern); film 13 S6's shape |
| S6 The gate | Change record with evidence; privacy and model-risk screens pre-filled; promotion sign-off prepared, not decided; "easier to satisfy, never easier to skip" | [ServiceNow change](../../research/sources/servicenow-docs-devops-change-velocity-approval.md) (vendor); [NAB](../../research/sources/itnews-nab-cast-cloud-controls.md), [CBA](../../research/sources/itnews-cba-production-more-often-fewer-incidents.md) (first-party via press); [SR 11-7](../../research/sources/federalreserve-sr-11-7-model-risk-guidance.md) (regulator); [Finansinspektionen](../../research/sources/fi-swedbank-change-management-sanction.md) (regulator); [Kapel et al.](../../research/sources/arxiv-kapel-ing-change-incident-prediction.md) (first-party, the trap) |
| S7 The environment moves | The app platform owner writes down the placement intake and a lead time; the next map is complete | [ING](../../research/sources/techzine-nardiello-ing-decade-cloud-native.md) (first-party); [GOV.UK Notify](../../research/sources/govuk-notify-trial-mode.md) (first-party); [Backstage templates](../../research/sources/backstage-docs-writing-templates.md) (first-party) |
| S8 The picture | Two axes, four cells, the trap, the rule | [05-maturity-model.md](05-maturity-model.md); [08-maturity-model.html](08-maturity-model.html) |
| S9 The measurement and the choice | Three numbers; the checklist; which two platforms first | [06-mvp.md](06-mvp.md); [DORA 2024](../../research/sources/dora-accelerate-state-of-devops-2024.md) (independent, platforms add handoffs) |

## Dialogue as a source of beats

The notional dialogue in [10-dialogue.md](10-dialogue.md) and its mockup [10-dialogue.html](10-dialogue.html) walk the same loop turn by turn in the insurer setting; the day-1 "could not find" list, the day-4 record correction at its home, the day-9 estimate labelled as an estimate, and the six-weeks-later reuse and wait-time table are the beats to port into the bank scenario for S3, S4, S7 and S9. The taxonomy in [09-dependency-taxonomy.md](09-dependency-taxonomy.md) is the legend for S2. The dialogue can be re-cut to the bank scenario in the film task if Geoff prefers one example across everything.

## Constraints

- No real-world number may be narrated unless it is in a filed source note with its label on screen; the story's own figures stay tagged illustrative.
- No claim about any real bank; the examples that name real organisations appear only as labelled evidence cards. The bank in the story is unnamed.
- One term in the project's public-check list names a bank that appears in some sources on governance-as-pipeline; the film must not name it. The two Australian banks' first-party accounts cover the same pattern.
- Financial-promotion rules differ by jurisdiction; the film keeps the compliance question generic ("is this wording a promotion that needs the full sign-off") and does not cite a specific rule.
- The film follows the project's film rules (draft voice and draft indicator until Geoff reviews).

## Open question for Geoff

Whether the film is built now, from this brief, or after he has read the written deliverables and reacted; the director raised this on 2026-10-28 and it is Geoff's call. The brief is written so that either works.
