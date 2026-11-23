# The product system: a working description

A draft that is meant to keep changing. It describes, loosely, the system the thesis ([04-truths.md](04-truths.md)) implies: who does what, what the agents are, how an idea moves, and where people decide. The scenarios (kept local) test it. When a scenario and this description disagree, either may be wrong, and so may the thesis; the last section records what each scenario strained and which way I lean. Nothing here is a rule.

## What the system is for

Pointing human talent at the work where it counts most: finding the problems worth solving, inventing answers, and owning how things turn out. Most of the rest is carried by agents and by shared material that anyone can reach.

## The people

- **People who carry ideas.** Anyone close enough to a problem to see it: a product manager, an engineer, a designer, someone in operations. Carrying an idea means forming the conviction, shaping an answer and seeing it tested. It doesn't need a title.
- **People who answer for outcomes.** Someone answers for how a product area, a customer journey or a platform performs. They set the direction and the appetite for risk in that area, and they give attention to the changes that matter most. They don't look at every change.
- **People with a specialist craft.** Risk, legal, design, engineering, finance. They are needed for the hard calls: an ambiguous rule, a real trade-off, a standard of quality. Routine questions that used to reach them are answered from what they have already written down.

How these overlap is unsettled. One person is often all three.

## The agents

- **Agents that work for a person or a team.** They gather signals, lay out competing explanations, interview customers at scale, build versions of an idea, run replays and simulations, and argue the other side when asked.
- **Steward agents.** Each platform, customer journey and operational process has one. It knows its area, keeps it running, fixes small things, notices emerging problems, helps new uses come aboard, and drafts how a change fits. Stewards settle routine questions between themselves, including trade-offs that turn on facts; the person who answers for the area is informed, and is pulled in for questions of risk appetite.
- **Coding agents.** They write the production change and its tests from the statement of intent and the solution design. Changes to a platform often come from the team that needs them, applied by the platform's steward once its owner approves.
- **Checking agents.** They verify changes and are kept apart from the agents that built them.
- **Risk agents.** They hold the limits for what ships on its own, within policy the risk function owns, and watch changes after release.

## The artifacts

- **Statement of intent.** Written by the person: what will change, the outcome it should move, the accepted risk, what would prove it wrong, and the trade-offs. Short, because agents supply the standing rules.
- **Solution design.** Drafted by agents, settled by people where it matters: how the change fits the existing platforms, the connections, what it depends on, the alternatives and the trade-offs.
- **Decision record.** What was chosen or stopped, and why, linked to the evidence.

## The shared material

- **Signals:** what customers say and do, and how operations are running, reachable by people and agents, with summaries that lead back to their sources.
- **What exists:** a current account of what each platform, journey and process does.
- **The rules:** standards and obligations in a form agents can apply, with people to interpret the unclear cases.
- **Somewhere safe to try things:** places to build against, and the ability to replay real history.
- **The trail:** what is in market stays connected to the problem, the evidence and the trade-offs behind it.

## The moves

Product work in this future runs through eleven recurring moves in flexible order. A shaping loop—investigating, hypothesizing, prototyping, and challenging—cycles many times before a bet is chosen, and delivery sends work back whenever checks or results surface a flaw. After a change ships, shaping and delivery often repeat for the next iteration. One person holds the thesis and makes the calls; colleagues and agents supply evidence and challenge.

1. **Sense.** Spot a problem or an opportunity worth acting on: a customer difficulty, a shortfall against an outcome, or an opening in the data. *Agents lead, watching outcomes and customer signals continuously and surfacing problems and opportunities nobody asked about.*
2. **Investigate.** Find out why. *Agents cover the breadth, drawing explanations from existing data and running interviews at scale;* the person goes directly to customers for depth.
3. **Hypothesize.** State a belief about the problem and its answer, the outcome it should move, the accepted risk, and what would prove it wrong. Written down, this is the statement of intent. A human move.
4. **Prototype.** Make the idea concrete enough to test, often within hours. *Agents build;* the person decides what is worth building.
5. **Challenge.** Attack the hypothesis with data, historical replays, simulations, customers, and colleagues. *Agents run the replays, simulations, and analysis, and argue the other side when asked;* people bring customers and experience.
6. **Decide.** Commit to a bet, stop an idea, or go another round. A human move.
7. **Design.** Fit the change into existing systems. Written down, this is the solution design. *Steward agents propose the design and work out connections across platforms;* people settle the trade-offs.
8. **Build.** Create the production change. *Coding agents write the code and tests;* engineers review the design and high-risk code.
9. **Verify.** Validate the change and assemble the evidence the bank's rules require. *Independent checking agents run the checks;* people handle exceptions and rule on ambiguous cases.
10. **Release.** Put the change live. Small, reversible changes ship automatically within pre-agreed limits; people set bounded live tests for higher-stakes changes.
11. **Learn.** Read results against the hypothesis and keep the rationale with what shipped. *Agents maintain the trail and keep watching, feeding back into Sense.*

## How decisions get made

It depends on the decision. Small changes that are easy to observe and reverse go out without a person approving each one, inside limits agreed by the person who answers for the area and a risk agent. Those limits move with experience. Changes that move money, alter what customers pay, or carry real risk get the attention of whoever answers for the outcome, and of a specialist when a rule is unclear. One person holds the thesis for a bet and makes the calls; colleagues and agents supply evidence and challenge.

## Ambition and money

Because learning is cheap, teams try bolder answers, and the organization can consider bigger moves such as an acquisition. Money follows evidence in stages more than it follows a case made up front. How this meets annual planning is not yet described.

## What the scenarios have taught so far

Six scenarios have been run against the thesis: Priya (card rewards), Kofi (small-business payouts, carried by an engineer), Amara (a servicing journey and its steward), Dele (a fee change), Ruth (an acquisition) and Sam (a newcomer learning judgment). The leans below are the research's; either side can bend, and each is the project lead's to settle.

**Settled since the first scenario**
- The artifact a person writes is the statement of intent; how a change fits existing systems is a separate solution design. Truth 7 now says so.
- Sense is defined: spotting a problem or an opportunity worth acting on.
- The limits for unreviewed release are agreed between the person who answers for the area and a risk agent.

**Open**
1. **Truth 5 (testing converges with describing).** In every scenario, prototypes shape and test the idea, and the production change is built later as its own move. *Lean:* say prototyping is how ideas are shaped, and keep production separate.
2. **Truth 6 (multiple answers in parallel).** Answers are tested in rounds against a sharp hypothesis, and one person judges them. *Lean:* reword toward judgment: many answers are tested against a sharp hypothesis.
3. **Truth 8 (loops of rising realism).** Challenge recurs in every round, using whatever fits: data, replay of real history, simulation, customers, colleagues. Replay of real history did most of the deciding; simulated customers barely appear. *Lean:* the truth bends from a ladder to a recurring move, and separates replaying history from simulating people.
4. **Truth 4 (thresholds for shipping without sign-off).** Amara's story shows a change inside the limits going wrong, being caught in hours, and the limit moving. *Lean:* say the limits are adjusted from experience. Also say AI parts of a product need a different kind of checking from deterministic steps.
5. **Truth 3 (judgment beyond the PM title).** An engineer carries Kofi's bet and an operations lead sees what Ruth's mapping missed; in each case another craft covers a gap. *Lean:* the truth holds, and should say other crafts stay close by.
6. **Truth 7 (rules supplied by agents).** In Dele's story the rules agent missed two items. *Lean:* admit the record of obligations will be incomplete for a long time.
7. **Truth 14 (portfolio ambition).** The thing most likely to sink Ruth's acquisition was written nowhere and came from a person. *Lean:* say that at this scale people's experience carries what records cannot.
8. **No truth covers Design, Build and Verify.** Three of the eleven moves rest only on steward agents and verification thresholds. *Open:* add a truth on where engineering attention goes, or keep it here.
9. **No truth covers how judgment is learned.** Agents take the fetch-and-carry work that was also how newcomers learned the business (Sam). *Open:* add a truth or an open question.
