# Brief for the follow-on film: the dependency agent, v2

Date: 2026-10-28. Written by the research-dependency-agent worker as the last deliverable of the research round; the film itself is a separate task. Film 13 (`explainers/projects/13-dependency-agent-vignette`) is the draft this replaces or revises; Geoff called it directionally right and a demo. This brief says what the better film should say, who it is for, what to keep, what to change, and which scenes the research supports. Evidence references are to `../../research/sources/`, with labels.

## Audience

Product and platform leaders in large, matrixed, platform-centric companies in regulated industries, deciding whether to fund a dependency agent and what to ask of their platform teams. Secondary: the second line (risk, compliance, audit), who need to see that the agent makes gates easier to satisfy and never easier to skip. Geoff, as the first reader.

## What the film must carry

Five concepts, in this order, because each needs the one before it:

1. **What a dependency is, and why the slow ones are not the obvious ones.** Systems are the easy edges; process gates, approvals, data terms, third parties and "the person who knows" are where the time goes ([Tkalich et al.](../../research/sources/arxiv-tkalich-critical-dependencies-cse.md), independent; [FCA](../../research/sources/fca-implementing-technology-change.md), regulator).
2. **Why it is hard here.** Mandatory gates that never say no and still take weeks; onboarding as a cascade of queues with no published lead time; records stale by default; the map itself now a legal artefact ([02-challenges.md](02-challenges.md)).
3. **What doing it well is worth, honestly.** Lead with the cost side, which is independent: waiting, chasing, late discovery, fat-tailed overruns, a fine for a skipped gate. Show benefit figures as labelled illustrations ([03-value.md](03-value.md)).
4. **The destination and the road.** Seven kinds of value; two axes; the rule that the environment moves one step ahead of the agent ([04](04-destination.md), [05](05-maturity-model.md)).
5. **The first move.** Map, ask, record: the loop that makes the record better and produces the measurement nobody has; the agent-ready checklist a platform owner can act on ([06-mvp.md](06-mvp.md)).

## The arc

Film 13 is a story about an agent that works. The better film is a story about an organisation that becomes legible, with the agent as the reason. Same insurer, same feature, same people; the centre of gravity moves from "look what the agent found" to "look what the organisation now knows that it did not know before, and what that is worth".

Proposed shape, about six minutes:

- **Open on the cost, not the agent.** Noor's feature, today, without an agent: the composite from [01-dependency-management-today.md](01-dependency-management-today.md) section 7. Four intake forms with the same facts in four shapes; a six-week security queue; the state-filing question surfacing in week ten from Ruth, who happened to be in another meeting; the knowledge leaving with the people. One line of independent evidence on screen per beat.
- **Name the problem precisely.** The ten dependency types as a legend; the slow edges highlighted; the gate that approves 90% and still takes weeks; the register that was 6.5% clean. This is where the film says: this is not a planning problem, it is a legibility problem.
- **Introduce the agent as a reader first.** It walks what exists, draws the map, and the most important object on screen is the **"could not find" list**: the owner who left, the contract that does not exist, the two documents that disagree, the process rows that are empty because nothing describes them. The map is partial and says so.
- **The loop.** Asks drafted as the smallest question, riding real needs; Noor sends them; owners answer in the session; every answer written back provisional, then verified, with owner, date and source. The context layer panel from film 13 is kept, but what writes to it is now the loop, not the agent alone. The second time the same question is asked, by another team, the answer is there in a second.
- **The one question for a person**, kept from film 13 (Ruth and the filings), because it is the clearest statement of what the agent does not do.
- **The environment moves.** A platform owner, seeing asks arrive in one shape, publishes a platform card and an intake description; the agent's next map on that platform is complete; the lead time appears as a number for the first time. This is the beat film 13 lacks: the organisation changing because the agent gave it a reason to.
- **The maturity picture, in one drawn frame.** Two axes, nine cells, the four that matter, the trap, the rule.
- **Close on the measurement and the choice.** Wait time per platform, verification rate, reuse rate, on screen as the three numbers the first quarter produces. Then the funding question the viewer is left with: which two platforms first.

## What to keep from film 13

- Lantern Mutual, Noor, Ines, Kofi, Ruth; the fictional label; the mid-term vehicle add; the three phases. The grounding table in film 13's README stays valid for the scenes it covers.
- The four node shapes and the graph by phase; the context layer panel with owner, date and source; the persistence beats (days passing, owners joining from a phone, another team's agent posting its release slots); the re-plan on day nine; the SME question written back; the "illustrative" tag on every figure.
- The motion grammar and the plate look, per the project's film rules.

## What to change

- **Open on today, not on the agent.** Film 13 opens with the requirements already shaped and the agent arriving in scene two; the viewer never feels the cost. Thirty to forty seconds of the status quo, with independent evidence on screen, earns the rest.
- **Make the "could not find" list the hero object of the discovery scene**, not the count of thirty-one dependencies. The research says over-prediction is the documented failure and partial maps with explicit gaps are the honest product.
- **Show the loop, not the agent, improving the context.** In film 13 the agent flags, proposes and an owner verifies; keep that, but add the second-order effect: a platform owner changes what they publish because of how the asks arrive. That is the maturity model's mechanism and film 13 does not have it.
- **Add the gate scene.** A change record opened with its evidence linked; a privacy pre-screen ("two of nine triggers apply; here is the draft"); and the line that the agent prepares the judgement gates for a person and never decides them. The second-line viewer needs this scene.
- **Replace film 13's closing figures** ("a season of meetings became sixteen days") with the three measurements the MVP produces and a labelled independent figure on the cost side. The research found no audited figure for discovery time, so the film should not imply one; it can show the organisation measuring for the first time.
- **Cut or shorten** the asks-routing scene's channel detail (ticket, review board, mail) in favour of the single idea "the smallest question, to the owner, through the channel they read".
- **Add one frame of the agent-ready checklist** at the end, as the thing a platform owner in the audience can do on Monday.

## Candidate scenes and the evidence behind each

| Scene | What it shows | Evidence (label) |
|---|---|---|
| S1 Today | Four forms, one queue, a question surfacing in week ten, knowledge leaving | [NHS onboarding](../../research/sources/nhs-england-nrl-onboarding-guidance.md) (first-party); [Equal Experts](../../research/sources/equalexperts-smith-escape-ticketing-hell.md) (anecdote, eleven weeks); [Herbsleb and Grinter](../../research/sources/herbsleb-grinter-conways-law-revisited.md) (independent); [Stack Overflow 2024](../../research/sources/stackoverflow-dev-survey-2024-professional-developers.md) (independent) |
| S2 The problem named | Ten dependency types; slow edges; the gate that approves 90%; the register 6.5% clean | [Tkalich](../../research/sources/arxiv-tkalich-critical-dependencies-cse.md) (independent); [FCA](../../research/sources/fca-implementing-technology-change.md) (regulator); [ESAs](../../research/sources/esas-dora-dry-run-register-of-information.md) (regulator); [DORA 2019](../../research/sources/dora-state-of-devops-2019.md) (independent) |
| S3 The reader | The walk of the context layer; the map by phase; the "could not find" list; two documents that disagree | film 13 S2 and S3 grounding; [LEREDD](../../research/sources/arxiv-darif-leredd-requirement-dependencies.md) (independent, over-prediction); [Port survey](../../research/sources/port-state-of-idp-2025-metadata-trust.md) (vendor) |
| S4 The loop | Smallest questions riding real asks; owners answer; provisional then verified; the second team's instant answer | [Shopify River](../../research/sources/shopify-engineering-river-vulnerability-remediation.md) (first-party); [Stripe panel](../../research/sources/stripe-sessions-2024-10x-engineer-panel.md) (first-party); [Nudge](../../research/sources/arxiv-maddila-nudge-overdue-pull-requests.md) (first-party, randomised) |
| S5 One question for a person | Ruth and the filings, written back with her name | film 13 S6 grounding |
| S6 The gate | Change record with evidence; privacy pre-screen; judgement gates prepared, not decided; "easier to satisfy, never easier to skip" | [ServiceNow change](../../research/sources/servicenow-docs-devops-change-velocity-approval.md) (vendor); [NAB](../../research/sources/itnews-nab-cast-cloud-controls.md) (first-party via press); [ICO](../../research/sources/ico-when-do-we-need-a-dpia.md) (regulator); [Finansinspektionen](../../research/sources/fi-swedbank-change-management-sanction.md) (regulator) |
| S7 The environment moves | A platform owner publishes a card and an intake description; the next map is complete; a lead time appears | [ING](../../research/sources/techzine-nardiello-ing-decade-cloud-native.md) (first-party); [GOV.UK Notify](../../research/sources/govuk-notify-trial-mode.md) (first-party); [Backstage templates](../../research/sources/backstage-docs-writing-templates.md) (first-party) |
| S8 The picture | Two axes, four cells, the trap, the rule | [05-maturity-model.md](05-maturity-model.md); [Kapel et al.](../../research/sources/arxiv-kapel-ing-change-incident-prediction.md) (first-party, the trap) |
| S9 The measurement and the choice | Three numbers; the checklist; which two platforms first | [06-mvp.md](06-mvp.md); [Microsoft Research](../../research/sources/microsoft-research-coordination-large-scale-development.md) (independent, the cost side) |

## Dialogue as a source of beats

The notional dialogue in [10-dialogue.md](10-dialogue.md) (and its mockup, [10-dialogue.html](10-dialogue.html)) walks the same story turn by turn; its day-1 "could not find" list, the day-4 record correction at its home, the day-9 estimate labelled as an estimate, and the six-weeks-later reuse and wait-time table are candidate beats for S3, S4, S7 and S9. The taxonomy in [09-dependency-taxonomy.md](09-dependency-taxonomy.md) is the legend for S2.

## Constraints

- No real-world number may be narrated unless it is in a filed source note with its label on screen; the story's own figures stay tagged illustrative.
- No claim about any real insurer, bank or platform; the examples that name real organisations appear only as labelled evidence cards.
- One term in the project's public-check list names a bank that appears in some sources on governance-as-pipeline; the film must not name it. The two Australian banks' first-party accounts cover the same pattern.
- The film follows the project's film rules (draft voice and draft indicator until Geoff reviews).

## Open question for Geoff

Whether the film is built now, from this brief, or after Geoff has read the written deliverables and reacted; the director raised this on 2026-10-28 and it is Geoff's call. The brief is written so that either works.
