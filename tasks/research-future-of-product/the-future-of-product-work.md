# The Future of Product Work

*A vision thesis for rethinking product development, written for executive sponsorship. This file gathers the current version in one place: the truths, the moves of the product loop, the system they imply, the assets that would support it, and the tensions still open. The working files beside it hold the same material with their history; the evidence base is [02-expert-view.md](02-expert-view.md).*

**Contents:** [The thesis and truths](#the-thesis-where-human-leverage-lives) · [The moves](#the-moves-of-the-product-loop) · [People, agents and artifacts](#people-agents-and-artifacts) · [Assets](#assets-that-would-support-the-loop) · [Open tensions](#open-tensions)

## The Thesis: Where Human Leverage Lives

When building becomes abundant, the central question for a product organization stops being *"How do we execute faster?"* and becomes *"Where does human talent create the highest leverage?"*

In a large, regulated enterprise, much of what we call "product work" today is actually organizational glue: tracking down context, translating requirements across handoffs, restating compliance rules, and sitting in review queues for low-risk changes. None of that requires genuine product judgment.

As agents take over the mechanics of gathering context, enforcing known constraints, and maintaining steady-state systems—across deterministic software just as much as AI products—tooling brings clean standards to routine work while leaving wide room for open-ended exploration, critical thinking, and creative leaps. Human attention concentrates where it matters most: **deciding which problems are worth solving, inventing bold answers, owning the outcomes, and making genuinely novel discoveries atop everything the organization has already learned.**

What follows is not a rigid operating manual or a set of mandates to impose. It is a description of what becomes normal when human talent is pointed at its highest-leverage work, alongside the institutional conditions that make it possible—and the open questions we still need to test.

## I. High-Leverage Human Work

### 1. Problem discovery becomes the primary human craft

Choosing the right problem determines more of a product's success than anything downstream, yet it routinely gets squeezed out by delivery mechanics. In this model, agents widen the aperture—ingesting and synthesizing raw customer signals, operational telemetry, support calls, and complaints—while humans build real empathy, talk directly to users where nuance matters, and form the conviction around what actually hurts.

- *The shift:* Product teams spend a growing share of their energy with customers and inspectable evidence, dramatically reducing the number of things built that nobody wanted.
- *What makes it possible:* Easy access to consented customer and operational signals, agent syntheses that trace cleanly back to raw sources, and leadership protecting time for discovery. *(Evidence: V1, V3; [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md), [Snyder](../../research/sources/lenny-podcast-rob-snyder-power-of-pull.md))*

### 2. Solution work shifts from assembly to invention

With agents handling routine assembly and constraint checking, human creativity goes toward framing ambitious answers, defining the target outcome, setting risk tolerance, and making explicit trade-offs.

- *The shift:* More original answers reach customers, and hard trade-offs are surfaced and settled up front rather than discovered by accident late in delivery.
- *What makes it possible:* A sharp definition of the problem and low-cost ways to test competing ideas early. *(Evidence: V1; [Ambrosino](../../research/sources/lenny-podcast-ambrosino-codex-product-work.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 3. Standards elevate routine work while keeping exploration open-ended

Much of product work benefits from clear structure: baseline standards applied by agents, shared formats for capturing decisions, and automated checks for routine mechanics. Yet the highest-leverage pursuits—prioritizing which problems deserve focus, exercising critical judgment, and inventing ambitious solutions—remain inherently open-ended and defy deterministic step-by-step checklists. Good tooling elevates the floor on repeatable work while deliberately leaving space for curiosity, rigorous debate, and creative leaps.

- *The shift:* Repeatable mechanics run reliably to standard, while problem framing and invention stay fluid—allowing teams to challenge assumptions, discard early prototypes, and pursue unconventional angles.
- *What makes it possible:* On-demand tools that sharpen thinking through fast prototypes, counterarguments, and evidence synthesis while leaving the path open, paired with leadership that evaluates discovery by the caliber of problems chosen and ideas surfaced. *(Evidence: [Anthropic](../../research/sources/anthropic-building-effective-agents.md), [Ambrosino](../../research/sources/lenny-podcast-ambrosino-codex-product-work.md), [Fadell](../../research/sources/lenny-podcast-tony-fadell-taste-judgment.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 4. Product judgment spreads beyond the PM title

Choosing problems, shaping intent, and deciding what ships—work historically bottlenecked on product managers—increasingly happens among engineers, designers, operations leads, and others closest to the customer or system. Specialist craft still matters and still sets the quality bar inside each discipline, but ownership moves closer to the signal.

- *The shift:* Fewer handoffs between the people who see the friction and the people who build the fix, with more shipped improvements originating outside a formal PM role.
- *What makes it possible:* Safe sandboxes where anyone can test an idea and shared, self-serve access to customer evidence. *(Evidence: V18; [Avasare](../../research/sources/lenny-podcast-amol-avasare-anthropic-growth.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 5. Accountability attaches to outcomes, not individual diffs

Today, senior talent spends enormous energy reviewing every small change with roughly the same weight as a major bet. When changes fall below clear, agreed thresholds for impact, observability, and reversibility, agents and deterministic checks handle verification—allowing many changes to ship without manual human sign-off. Humans remain squarely accountable for how a product area performs and focus their scrutiny where the stakes are genuinely high.

- *The shift:* Review bandwidth goes where it actually changes results; small improvements stop waiting in queues, while incident rates and customer harm stay flat or fall.
- *What makes it possible:* Strong observability and instant rollback, thresholds accepted by risk partners and regulators, and verification agents kept strictly independent from the agents doing the building. *(Evidence: V8; [Sherwin Wu](../../research/sources/lenny-podcast-sherwin-wu-openai-codex.md), [FSB](../../research/sources/fsb-sound-practices-responsible-ai-adoption-2026.md))*

## II. How Ideas Become Products

### 6. Testing an idea converges with describing it

When the cost of prototyping approaches the cost of describing the idea precisely, describing an idea and trying it stop being sequential phases. Neither has to come first; teams can sketch in working software or simulation just as easily as in prose.

- *The shift:* Evidence arrives before commitment rather than after, compressing the time from initial spark to real feedback from months to days.
- *What makes it possible:* Safe, realistic test environments backed by current representations of what underlying platforms can actually do. *(Evidence: V4; [Stripe](../../research/sources/stripe-harbor-ai-prototyping.md), [Embiricos](../../research/sources/lenny-podcast-embiricos-codex-human-bottleneck.md))*

### 7. Teams explore multiple answers in parallel

Because early testing is inexpensive, teams no longer have to fall in love with their first plausible solution. They can test several distinct candidates against the same problem side by side, killing weak paths early and doubling down on what works.

- *The shift:* Stronger solutions make it to market, with far less sunk-cost attachment to early drafts.
- *What makes it possible:* A well-defined problem to aim at and funding mechanisms that follow evidence rather than upfront business cases. *(Evidence: V5; [Pincus](../../research/sources/lenny-podcast-mark-pincus-proven-better-new.md), [Silber](../../research/sources/lenny-podcast-ian-silber-openai-design.md))*

### 8. The statement of intent shrinks to the change, the outcome, the risk, and the trade-offs

Writing down a new idea no longer requires reciting every architectural standard, regulatory rule, or internal obligation a change must meet. Agents supply and verify those baseline rules automatically. The person's statement of intent becomes short and crisp: what will change, the outcome it should produce, the risk accepted, what would prove it wrong, and the trade-offs the team is willing to accept. How the change fits the existing systems is a separate artifact, the solution design, which agents draft and people settle. Human focus and time shift to the change itself, while solution design and navigating dependencies are increasingly automated.

- *The shift:* Shorter statements of intent and far less late-stage rework triggered by a forgotten obligation or compliance requirement.
- *What makes it possible:* Rules, standards, and obligations maintained in a machine-usable form, paired with human experts available to rule on edge-case interpretation. *(Evidence: V13; [EY](../../research/sources/ey-how-regulatory-inventories-deliver-more-value.md))*

### 9. Validation runs in short loops of rising realism

Ideas earn exposure progressively. Candidates are tested first in simulation or replayed against historical data—especially effective for modeling how systems, money, and operations behave—before moving to small live cohorts and, eventually, broad release. The stakes dictate the number of rungs.

- *The shift:* Failures happen cheaply in simulation; full launches carry far fewer operational or customer surprises.
- *What makes it possible:* Safe replay of real operational activity and pre-agreed guardrails for live experimentation in regulated products. *(Evidence: V6; [American Express](../../research/sources/americanexpress-io-migrating-the-payments-network-twice.md))*

### 10. Customer insight comes from the highest-signal method

Telemetry, live experiments, and agent-analyzed support logs answer many questions that once defaulted to slow interview cycles. Agents can even run structured outreach where appropriate, freeing direct human interviews for the deep, ambiguous questions where human conversation has no substitute.

- *The shift:* Decisions draw on richer, multi-modal customer evidence delivered in days rather than weeks.
- *What makes it possible:* Consented access to customer interactions and audit trails linking agent summaries back to source recordings or transcripts. *(Evidence: V3; [Snyder](../../research/sources/lenny-podcast-rob-snyder-power-of-pull.md))*

## III. The Agent Fabric, Shared Knowledge & Lineage

### 11. Agents take over the fetch-and-carry of information

A huge portion of product management today is locating existing capabilities, checking system status, drafting stakeholder updates, and keeping documentation current. Agents absorb this logistical layer—answering *"Can we already do this?"* in seconds rather than days of Slack archaeology.

- *The shift:* Status meetings and document hunts shrink dramatically, returning hours of cognitive capacity to product teams.
- *What makes it possible:* Documentation that is actually written down and kept current—currently the single widest gap in most large enterprises. *(Evidence: V7; [Stripe](../../research/sources/stripe-meet-knowledge-ai-platform.md), [Singhal](../../research/sources/lenny-podcast-nikhyl-singhal-half-of-pms.md))*

### 12. Every platform, journey, and process has a dedicated steward agent

Rather than relying on tribal knowledge or ticket queues, each core platform, customer experience, and operational workflow is tended by a persistent agent. It handles steady-state maintenance—clearing minor paper cuts and surfacing emerging friction—while onboarding new use cases and negotiating routine integrations with peer agents. Humans step in only when trade-offs or judgment are required. More platform changes will come from the feature owners who need them ("away teams") rather than from the platform team. They arrive as pull requests from the feature team, or as well-shaped requests the steward agent executes, sometimes after the platform owner approves.

- *The shift:* Paper cuts get fixed without waiting for quarterly planning; platform onboarding drops from months to days; integration questions get answered in minutes.
- *What makes it possible:* An accurate, live model of each domain and explicit boundaries on what its steward agent can execute autonomously. *(Evidence: V9, V10; [Shipper](../../research/sources/lenny-podcast-dan-shipper-ai-paradox.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 13. Work draws on and compounds a shared body of knowledge

Lessons learned, tests attempted, newly uncovered constraints, and the breakthroughs that overcame them flow into a living body of knowledge that both humans and agents draw from and replenish. Because agents bring prior experiments, past failures, and proven workarounds directly into the flow of new work, teams build from the frontier of what the enterprise already knows. The highest calling of people in this system is novel discovery—uncovering what nobody in the institution knew yet.

- *The shift:* Duplicate experiments and rediscovered constraints drop, while a growing share of human ingenuity goes toward genuinely uncharted questions.
- *What makes it possible:* Capturing lessons, test outcomes, constraints, and workarounds automatically as a by-product of work, agents that surface relevant history at the moment of need, and cultural norms that reward sharing informative failures. *(Evidence: V12; [Ramp](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md), [Shopify](../../research/sources/x-tobi-learning-on-the-shop-floor.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 14. Production stays linked to intent

Every live feature and test traces cleanly back to the customer problem, intent, and constraints that produced it. Rather than relying on heroic post-hoc documentation, agents capture this lineage automatically as a by-product of the work.

- *The shift:* *"Why does the system work like this?"* becomes an answerable query rather than a scavenger hunt, dramatically cutting effort for audits, incident response, and onboarding.
- *What makes it possible:* Capturing intent at the moment decisions happen and preserving context before key people rotate off. *(Evidence: V11, V12; [Uber](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md), [Shopify](../../research/sources/x-tobi-learning-on-the-shop-floor.md))*

## IV. Where Ambition Goes

### 15. Feature-level ambition rises

When an idea can be tested before heavy commitment and reversed cheaply if it misses, teams stop defaulting to safe, incremental tweaks. They take bolder swings at hard customer problems, knowing a clean, early kill is a success rather than a career scar.

- *The shift:* More experiments that break from existing product patterns and a wider gap between top-performing bets and average ones.
- *What makes it possible:* Fast, low-cost validation loops and leaders who visibly reward bold bets that were stopped cleanly on evidence. *(Evidence: V5; [Pincus](../../research/sources/lenny-podcast-mark-pincus-proven-better-new.md), [Söderström](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md))*

### 16. Portfolio-level ambition rises

At enterprise scale, strategy is often quietly capped by what leadership believes the organization can actually coordinate and deliver. As agents lower the friction of cross-team coordination, legacy mapping, compliance verification, and integration, the organization can take on larger moves—new product lines, M&A integrations, and entries into new markets—with far lower execution risk.

- *The shift:* Bigger strategic bets get started and finished; integrations and market entries compress; fewer major initiatives stall out mid-delivery.
- *What makes it possible:* Institutional memory, steward agents, and machine-readable obligations operating at scale, paired with stage-gated capital that follows evidence. *(Evidence: early and inferred. [Morgan Stanley](../../research/sources/entrepreneur-morgan-stanley-devgen-ai-legacy-code.md) on legacy estates, [American Express](../../research/sources/americanexpress-io-migrating-the-payments-network-twice.md) on traffic-replay migrations, [Acharya](../../research/sources/lenny-podcast-anish-acharya-company-loops.md) on compressed roadmaps)*

### 17. Reclaimed capacity funds bigger bets and sustainable work

The point of freeing human capacity is not simply to squeeze more routine output from the same people, nor is headcount reduction the primary goal—even if smaller, sharper teams naturally coordinate with less friction. Reclaimed time is a strategic asset that leaders must deliberately allocate toward harder problems and healthier, more sustainable pace.

- *The shift:* Teams take on more ambitious problems while burnout and workload metrics hold steady or improve.
- *What makes it possible:* Executive clarity on what the reclaimed capacity is explicitly meant to buy. *(Evidence: V1, V20; [Tech Workers Survey](../../research/sources/lenny-newsletter-tech-workers-2026-survey.md))*

## V. Where a Large Enterprise Starts From

To make this vision credible in a large, regulated institution, we have to be honest about our baseline. Today, we operate with structural friction that prevents agents—and people—from working this way:

- **Tribal context:** Much of what matters lives in people's heads, inboxes, and recurring meetings.
- **Human routing:** Work moves through interpersonal coordination and knowing who to ask.
- **Unstructured obligations:** Thousands of operational processes and hundreds of thousands of regulatory or policy obligations exist, very few in a form an agent can read and apply.
- **Missing lineage:** Decades of architectural and product decisions were never recorded, and many of the people who made them have left.
- **Uniform friction:** Review and governance are applied broadly, imposing similar weight on trivial changes and high-stakes bets alike.

## VI. Open Questions to Test

As we build notional walkthroughs and test these ideas in practice, nine questions remain genuinely open:

1. **Autonomy thresholds (Truth 5):** Where exactly should the line sit for shipping without human review, and what evidence will satisfy risk partners and regulators?
2. **Limits of simulation (Truth 9):** How far can simulated customers be trusted to predict human desire, as opposed to modeling system and financial behavior?
3. **Agent-to-agent integration (Truth 12):** Can steward agents reliably negotiate system integrations at enterprise scale? *(There is no proven production example yet.)*
4. **Baseline time allocation (Truths 1, 11):** How is product time actually spent across our organization today? *(We have anecdotes, not hard measurements.)*
5. **Candor under total recall (Truth 14):** Does recording every decision and rationale automatically chill honest debate?
6. **Role diffusion in regulated settings (Truth 4):** How far can product decision-making realistically spread beyond PMs inside a regulated enterprise?
7. **Portfolio-scale proof (Truth 16):** How much does portfolio-level ambition rise in practice outside of tech-native companies?
8. **Structure and creative room (Truth 3):** How much tooling structure sharpens discovery and invention before it begins to narrow open-ended exploration?
9. **Compounding institutional knowledge (Truth 13):** What incentives encourage teams to contribute candid lessons—including failed tests—and how do we retire stale findings before they mislead future work?

## The moves of the product loop

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

## People, agents and artifacts

### What the system is for

Pointing human talent at the work where it counts most: finding the problems worth solving, inventing answers, and owning how things turn out. Most of the rest is carried by agents and by shared material that anyone can reach.

### The people

- **People who carry ideas.** Anyone close enough to a problem to see it: a product manager, an engineer, a designer, someone in operations. Carrying an idea means forming the conviction, shaping an answer and seeing it tested. It doesn't need a title.
- **People who answer for outcomes.** Someone answers for how a product area, a customer journey or a platform performs. They set the direction and the appetite for risk in that area, and they give attention to the changes that matter most. They don't look at every change.
- **People with a specialist craft.** Risk, legal, design, engineering, finance. They are needed for the hard calls: an ambiguous rule, a real trade-off, a standard of quality. Routine questions that used to reach them are answered from what they have already written down.

How these overlap is unsettled. One person is often all three.

### The agents

- **Agents that work for a person or a team.** They gather signals, lay out competing explanations, interview customers at scale, build versions of an idea, run replays and simulations, and argue the other side when asked.
- **Steward agents.** Each platform, customer journey and operational process has one. It knows its area, keeps it running, fixes small things, notices emerging problems, helps new uses come aboard, and drafts how a change fits. Stewards settle routine questions between themselves, including trade-offs that turn on facts; the person who answers for the area is informed, and is pulled in for questions of risk appetite.
- **Coding agents.** They write the production change and its tests from the statement of intent and the solution design. Changes to a platform often come from the team that needs them, applied by the platform's steward once its owner approves.
- **Checking agents.** They verify changes and are kept apart from the agents that built them.
- **Risk agents.** They hold the limits for what ships on its own, within policy the risk function owns, and watch changes after release.

### The artifacts

- **Statement of intent.** Written by the person: what will change, the outcome it should move, the accepted risk, what would prove it wrong, and the trade-offs. Short, because agents supply the standing rules.
- **Solution design.** Drafted by agents, settled by people where it matters: how the change fits the existing platforms, the connections, what it depends on, the alternatives and the trade-offs.
- **Decision record.** What was chosen or stopped, and why, linked to the evidence.

### The shared material

- **Signals:** what customers say and do, and how operations are running, reachable by people and agents, with summaries that lead back to their sources.
- **What exists:** a current account of what each platform, journey and process does.
- **The rules:** standards and obligations in a form agents can apply, with people to interpret the unclear cases.
- **Somewhere safe to try things:** places to build against, and the ability to replay real history.
- **Shared knowledge:** lessons learned, tests attempted, constraints found and the ways around them, drawn on and added to by people and agents alike, so new work starts from what is already known.
- **The trail:** what is in market stays connected to the problem, the evidence and the trade-offs behind it.

### How decisions get made

It depends on the decision. Small changes that are easy to observe and reverse go out without a person approving each one, inside limits agreed by the person who answers for the area and a risk agent. Those limits move with experience. Changes that move money, alter what customers pay, or carry real risk get the attention of whoever answers for the outcome, and of a specialist when a rule is unclear. One person holds the thesis for a bet and makes the calls; colleagues and agents supply evidence and challenge.

### Ambition and money

Because learning is cheap, teams try bolder answers, and the organization can consider bigger moves such as an acquisition. Money follows evidence in stages more than it follows a case made up front. How this meets annual planning is not yet described.

## Assets that would support the loop

A first pass at what a bank would need to build or buy for the moves to work as the Priya scenario shows them. It is a working list, open to argument, and it will change as more scenarios test it. Where something already exists in our own work, it is named (Flight Deck corrections from its own agent, 2026-11-23): the Flight Deck prototype (the cut-down Omnigent fork, with Product Aviator as its interface) and this project's agent designs.

### Agents

- **Problem discovery agent** (Sense, Investigate). Watches the outcomes and customer signals for an area, raises problems nobody asked about, and lays out competing explanations with the evidence for each. *Exists in part:* Flight Deck's `problem-discovery` skill, which runs when asked; nothing yet watches continuously.
- **Customer research agent** (Investigate, Challenge). Recruits, runs consented structured interviews at scale, links every answer to its recording, and suggests who the person should meet directly.
- **Prototyping agents** (Prototype). Build working versions within hours, in safe copies of the real systems where that matters. One per channel (web, app, branch screen, voice, letter and so on), reached through a single Prototype move: a default enterprise prototyper takes channel teams' design-system packs, and platform teams can own their own. *Exists in part:* designed in Flight Deck, not built.
- **Challenge agent** (Challenge). Replays real history, runs simulations and the economics, tests for bias such as selection effects, and argues the other side when asked.
- **Steward agents**, one per platform, journey or operational process (Sense, Design, Learn). Know their area, keep it running, fix small things, propose how a change fits, and work out connections with other stewards. *Related:* this project's dependency agent, which finds and asks the owners a change depends on.
- **Coding agents** (Build). Write the production change and its tests from the intent and the design.
- **Checking agents** (Verify). Independent of the builders. Test, check security and accessibility, and assemble the evidence the bank's rules require.
- **Risk agent** (Release). Holds the limits for automatic release within policy the risk function owns, and watches changes after release.

### Skills a person's agent would carry

- **Framing a hypothesis:** the problem, the answer, the outcome it should move, the risk accepted, and what would prove it wrong. *Exists in part:* Flight Deck's `intent-shaping` skill (its template has no field yet for the risk accepted or what would prove it wrong); this project's requirements agent design.
- **Arguing the other side:** the strongest case against the current hypothesis and the evidence that would settle it.
- **Writing short intent** and **finding what a change depends on** and who must be asked. *Exists in part:* Flight Deck's "Solution design" arc, which goes from a written description of the change to its requirements, dependencies and alternatives. It produces most of a solution design, and today one Flight Deck template holds both the statement of intent and the solution design; this project's dependency agent.
- **Recording a decision** with its reasons, so it travels with what ships. *Exists in part:* `decision-review` and `decision-brief`.
- **Engaging the owners a change depends on**, including exchanging with an owner's agent. *Planned:* Flight Deck's "Engage owners" arc, the person's side of a steward agent.
- **Reporting where work stands** from the systems where it happens. *Exists in part:* `delivery-status`.

### Artifacts

Three artifacts carry the work. The first two are easily confused and are different things; neither is called a spec or a PRD, because people read their own meaning into those words.

- **Statement of intent** (Hypothesize). Written by the person: what will change, the outcome it should move, the risk accepted, what would prove it wrong, and the trade-offs accepted. Short, because agents supply the standing rules.
- **Solution design** (Design). Drafted by agents, settled by people: how the change fits the existing platforms, the connections between them, what it depends on, the alternatives considered, and the trade-offs decided.
- **Decision record** (Decide, Learn). What was chosen or stopped, and why, linked to the evidence.

### Shared material

- **Customer signals** people and agents can reach, with consent, and summaries that lead back to recordings.
- **A current account of each platform:** what it does, its limits, who answers for it; kept by its steward.
- **The bank's rules** (standards, policies, regulatory obligations) in a form agents can apply, with named people to interpret the unclear cases.
- **Safe copies** of the key systems to build in, and the ability to replay real history and model the money.
- **Agreed definitions** of the measures that matter, such as what counts as a redemption.
- **The trail:** each change linked to the problem, the evidence, the trade-offs and the decision. *Exists in part:* Flight Deck initiatives keep evidence, open questions, decisions and readiness with dated artifacts.
- **Release limits:** which kinds of change go out on their own, held where the risk agent and the people who set them can see them.

### The workspace

- **A place where one person runs their agents and skills**, sees what they produced, challenges it, and hands work to the stewards and builders. This is what Flight Deck prototypes, on top of the Omnigent meta-harness.

### Open questions

- Which of these a bank would buy, which it would build, and which come with the coding and agent platforms it already uses.
- Whether steward agents are one kind of agent configured per area, or separate agents.
- How much of the shared material exists today in usable form; the starting state suggests little.

## Open tensions

Six scenarios have been run against the thesis: Priya (card rewards), Kofi (small-business payouts, carried by an engineer), Amara (a servicing journey and its steward), Dele (a fee change), Ruth (an acquisition) and Sam (a newcomer learning judgment). The leans below are the research's; either side can bend, and each is the project lead's to settle.

**Settled since the first scenario**
- Two truths added at the project lead's direction: standards raise the routine while exploration stays open-ended (truth 3), and work draws on and adds to a shared body of knowledge, with novel discovery as people's highest calling (truth 13). The truths are renumbered.
- The artifact a person writes is the statement of intent; how a change fits existing systems is a separate solution design. Truth 8 now says so.
- Sense is defined: spotting a problem or an opportunity worth acting on.
- The limits for unreviewed release are agreed between the person who answers for the area and a risk agent.

**Open**
1. **Truth 6 (testing converges with describing).** In every scenario, prototypes shape and test the idea, and the production change is built later as its own move. *Lean:* say prototyping is how ideas are shaped, and keep production separate.
2. **Truth 7 (multiple answers in parallel).** Answers are tested in rounds against a sharp hypothesis, and one person judges them. *Lean:* reword toward judgment: many answers are tested against a sharp hypothesis.
3. **Truth 9 (loops of rising realism).** Challenge recurs in every round, using whatever fits: data, replay of real history, simulation, customers, colleagues. Replay of real history did most of the deciding; simulated customers barely appear. *Lean:* the truth bends from a ladder to a recurring move, and separates replaying history from simulating people.
4. **Truth 5 (thresholds for shipping without sign-off).** Amara's story shows a change inside the limits going wrong, being caught in hours, and the limit moving. *Lean:* say the limits are adjusted from experience. Also say AI parts of a product need a different kind of checking from deterministic steps.
5. **Truth 4 (judgment beyond the PM title).** An engineer carries Kofi's bet and an operations lead sees what Ruth's mapping missed; in each case another craft covers a gap. *Lean:* the truth holds, and should say other crafts stay close by.
6. **Truth 8 (rules supplied by agents).** In Dele's story the rules agent missed two items. *Lean:* admit the record of obligations will be incomplete for a long time.
7. **Truth 16 (portfolio ambition).** The thing most likely to sink Ruth's acquisition was written nowhere and came from a person. *Lean:* say that at this scale people's experience carries what records cannot.
8. **No truth covers Design, Build and Verify.** Three of the eleven moves rest only on steward agents and verification thresholds. *Open:* add a truth on where engineering attention goes, or keep it here.
9. **No truth covers how judgment is learned.** Agents take the fetch-and-carry work that was also how newcomers learned the business (Sam). *Open:* add a truth or an open question.
