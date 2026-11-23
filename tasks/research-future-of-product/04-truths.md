# The Future of Product Work

*A vision thesis for rethinking product development, written for executive sponsorship and paired with notional walkthroughs of how the work actually runs.*

Current version. The wording began as the project lead's preferred rewrite and has since taken his edits. The moves of the product loop and the working description of the system are in [07-product-system.md](07-product-system.md); the assets that would support it are in [08-assets.md](08-assets.md). V-numbers refer to the evidence base, [02-expert-view.md](02-expert-view.md).

## The Thesis: Where Human Leverage Lives

When building becomes abundant, the central question for a product organization stops being *"How do we execute faster?"* and becomes *"Where does human talent create the highest leverage?"*

In a large, regulated enterprise, much of what we call "product work" today is actually organizational glue: tracking down context, translating requirements across handoffs, restating compliance rules, and sitting in review queues for low-risk changes. None of that requires genuine product judgment.

As agents take over the mechanics of gathering context, enforcing known constraints, and maintaining steady-state systems—across deterministic software just as much as AI products—human attention concentrates where it matters most: **deciding which problems are worth solving, inventing bold answers, and owning the outcomes.**

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

### 3. Product judgment spreads beyond the PM title

Choosing problems, shaping intent, and deciding what ships—work historically bottlenecked on product managers—increasingly happens among engineers, designers, operations leads, and others closest to the customer or system. Specialist craft still matters and still sets the quality bar inside each discipline, but ownership moves closer to the signal.

- *The shift:* Fewer handoffs between the people who see the friction and the people who build the fix, with more shipped improvements originating outside a formal PM role.
- *What makes it possible:* Safe sandboxes where anyone can test an idea and shared, self-serve access to customer evidence. *(Evidence: V18; [Avasare](../../research/sources/lenny-podcast-amol-avasare-anthropic-growth.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 4. Accountability attaches to outcomes, not individual diffs

Today, senior talent spends enormous energy reviewing every small change with roughly the same weight as a major bet. When changes fall below clear, agreed thresholds for impact, observability, and reversibility, agents and deterministic checks handle verification—allowing many changes to ship without manual human sign-off. Humans remain squarely accountable for how a product area performs and focus their scrutiny where the stakes are genuinely high.

- *The shift:* Review bandwidth goes where it actually changes results; small improvements stop waiting in queues, while incident rates and customer harm stay flat or fall.
- *What makes it possible:* Strong observability and instant rollback, thresholds accepted by risk partners and regulators, and verification agents kept strictly independent from the agents doing the building. *(Evidence: V8; [Sherwin Wu](../../research/sources/lenny-podcast-sherwin-wu-openai-codex.md), [FSB](../../research/sources/fsb-sound-practices-responsible-ai-adoption-2026.md))*

## II. How Ideas Become Products

### 5. Testing an idea converges with describing it

When the cost of prototyping approaches the cost of describing the idea precisely, describing an idea and trying it stop being sequential phases. Neither has to come first; teams can sketch in working software or simulation just as easily as in prose.

- *The shift:* Evidence arrives before commitment rather than after, compressing the time from initial spark to real feedback from months to days.
- *What makes it possible:* Safe, realistic test environments backed by current representations of what underlying platforms can actually do. *(Evidence: V4; [Stripe](../../research/sources/stripe-harbor-ai-prototyping.md), [Embiricos](../../research/sources/lenny-podcast-embiricos-codex-human-bottleneck.md))*

### 6. Teams explore multiple answers in parallel

Because early testing is inexpensive, teams no longer have to fall in love with their first plausible solution. They can test several distinct candidates against the same problem side by side, killing weak paths early and doubling down on what works.

- *The shift:* Stronger solutions make it to market, with far less sunk-cost attachment to early drafts.
- *What makes it possible:* A well-defined problem to aim at and funding mechanisms that follow evidence rather than upfront business cases. *(Evidence: V5; [Pincus](../../research/sources/lenny-podcast-mark-pincus-proven-better-new.md), [Silber](../../research/sources/lenny-podcast-ian-silber-openai-design.md))*

### 7. The statement of intent shrinks to the change, the outcome, the risk, and the trade-offs

Writing down a new idea no longer requires reciting every architectural standard, regulatory rule, or internal obligation a change must meet. Agents supply and verify those baseline rules automatically. The person's statement of intent becomes short and crisp: what will change, the outcome it should produce, the risk accepted, what would prove it wrong, and the trade-offs the team is willing to accept. How the change fits the existing systems is a separate artifact, the solution design, which agents draft and people settle. Human focus and time shift to the change itself, while solution design and navigating dependencies are increasingly automated.

- *The shift:* Shorter statements of intent and far less late-stage rework triggered by a forgotten obligation or compliance requirement.
- *What makes it possible:* Rules, standards, and obligations maintained in a machine-usable form, paired with human experts available to rule on edge-case interpretation. *(Evidence: V13; [EY](../../research/sources/ey-how-regulatory-inventories-deliver-more-value.md))*

### 8. Validation runs in short loops of rising realism

Ideas earn exposure progressively. Candidates are tested first in simulation or replayed against historical data—especially effective for modeling how systems, money, and operations behave—before moving to small live cohorts and, eventually, broad release. The stakes dictate the number of rungs.

- *The shift:* Failures happen cheaply in simulation; full launches carry far fewer operational or customer surprises.
- *What makes it possible:* Safe replay of real operational activity and pre-agreed guardrails for live experimentation in regulated products. *(Evidence: V6; [American Express](../../research/sources/americanexpress-io-migrating-the-payments-network-twice.md))*

### 9. Customer insight comes from the highest-signal method

Telemetry, live experiments, and agent-analyzed support logs answer many questions that once defaulted to slow interview cycles. Agents can even run structured outreach where appropriate, freeing direct human interviews for the deep, ambiguous questions where human conversation has no substitute.

- *The shift:* Decisions draw on richer, multi-modal customer evidence delivered in days rather than weeks.
- *What makes it possible:* Consented access to customer interactions and audit trails linking agent summaries back to source recordings or transcripts. *(Evidence: V3; [Snyder](../../research/sources/lenny-podcast-rob-snyder-power-of-pull.md))*

## III. The Agent Fabric & Institutional Memory

### 10. Agents take over the fetch-and-carry of information

A huge portion of product management today is locating existing capabilities, checking system status, drafting stakeholder updates, and keeping documentation current. Agents absorb this logistical layer—answering *"Can we already do this?"* in seconds rather than days of Slack archaeology.

- *The shift:* Status meetings and document hunts shrink dramatically, returning hours of cognitive capacity to product teams.
- *What makes it possible:* Documentation that is actually written down and kept current—currently the single widest gap in most large enterprises. *(Evidence: V7; [Stripe](../../research/sources/stripe-meet-knowledge-ai-platform.md), [Singhal](../../research/sources/lenny-podcast-nikhyl-singhal-half-of-pms.md))*

### 11. Every platform, journey, and process has a dedicated steward agent

Rather than relying on tribal knowledge or ticket queues, each core platform, customer experience, and operational workflow is tended by a persistent agent. It handles steady-state maintenance—clearing minor paper cuts and surfacing emerging friction—while onboarding new use cases and negotiating routine integrations with peer agents. Humans step in only when trade-offs or judgment are required. More platform changes will come from the feature owners who need them ("away teams") rather than from the platform team. They arrive as pull requests from the feature team, or as well-shaped requests the steward agent executes, sometimes after the platform owner approves.

- *The shift:* Paper cuts get fixed without waiting for quarterly planning; platform onboarding drops from months to days; integration questions get answered in minutes.
- *What makes it possible:* An accurate, live model of each domain and explicit boundaries on what its steward agent can execute autonomously. *(Evidence: V9, V10; [Shipper](../../research/sources/lenny-podcast-dan-shipper-ai-paradox.md), [Mansour](../../research/sources/lenny-podcast-sherif-mansour-first-principles-pm.md))*

### 12. Production stays linked to intent

Every live feature and test traces cleanly back to the customer problem, intent, and constraints that produced it. Rather than relying on heroic post-hoc documentation, agents capture this lineage automatically as a by-product of the work.

- *The shift:* *"Why does the system work like this?"* becomes an answerable query rather than a scavenger hunt, dramatically cutting effort for audits, incident response, and onboarding.
- *What makes it possible:* Capturing intent at the moment decisions happen and preserving context before key people rotate off. *(Evidence: V11, V12; [Uber](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md), [Shopify](../../research/sources/x-tobi-learning-on-the-shop-floor.md))*

## IV. Where Ambition Goes

### 13. Feature-level ambition rises

When an idea can be tested before heavy commitment and reversed cheaply if it misses, teams stop defaulting to safe, incremental tweaks. They take bolder swings at hard customer problems, knowing a clean, early kill is a success rather than a career scar.

- *The shift:* More experiments that break from existing product patterns and a wider gap between top-performing bets and average ones.
- *What makes it possible:* Fast, low-cost validation loops and leaders who visibly reward bold bets that were stopped cleanly on evidence. *(Evidence: V5; [Pincus](../../research/sources/lenny-podcast-mark-pincus-proven-better-new.md), [Söderström](../../research/sources/colossus-ilb-gustav-soderstrom-how-spotify-thinks.md))*

### 14. Portfolio-level ambition rises

At enterprise scale, strategy is often quietly capped by what leadership believes the organization can actually coordinate and deliver. As agents lower the friction of cross-team coordination, legacy mapping, compliance verification, and integration, the organization can take on larger moves—new product lines, M&A integrations, and entries into new markets—with far lower execution risk.

- *The shift:* Bigger strategic bets get started and finished; integrations and market entries compress; fewer major initiatives stall out mid-delivery.
- *What makes it possible:* Institutional memory, steward agents, and machine-readable obligations operating at scale, paired with stage-gated capital that follows evidence. *(Evidence: early and inferred. [Morgan Stanley](../../research/sources/entrepreneur-morgan-stanley-devgen-ai-legacy-code.md) on legacy estates, [American Express](../../research/sources/americanexpress-io-migrating-the-payments-network-twice.md) on traffic-replay migrations, [Acharya](../../research/sources/lenny-podcast-anish-acharya-company-loops.md) on compressed roadmaps)*

### 15. Reclaimed capacity funds bigger bets and sustainable work

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

As we build notional walkthroughs and test these ideas in practice, seven questions remain genuinely open:

1. **Autonomy thresholds (Truth 4):** Where exactly should the line sit for shipping without human review, and what evidence will satisfy risk partners and regulators?
2. **Limits of simulation (Truth 8):** How far can simulated customers be trusted to predict human desire, as opposed to modeling system and financial behavior?
3. **Agent-to-agent integration (Truth 11):** Can steward agents reliably negotiate system integrations at enterprise scale? *(There is no proven production example yet.)*
4. **Baseline time allocation (Truths 1, 10):** How is product time actually spent across our organization today? *(We have anecdotes, not hard measurements.)*
5. **Candor under total recall (Truth 12):** Does recording every decision and rationale automatically chill honest debate?
6. **Role diffusion in regulated settings (Truth 3):** How far can product decision-making realistically spread beyond PMs inside a regulated enterprise?
7. **Portfolio-scale proof (Truth 14):** How much does portfolio-level ambition rise in practice outside of tech-native companies?
