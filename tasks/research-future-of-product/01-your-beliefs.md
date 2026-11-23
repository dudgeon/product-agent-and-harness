# Your beliefs about the future of product, broken apart

Source: your Google Doc "Future of product loop" (one dictated paragraph, 2026-11-22), filed at [geoff-future-of-product-loop](../../research/sources/geoff-future-of-product-loop.md). Each belief below is one claim, in your words where possible, numbered so research can cite it (B1.1, B3.2 …). Under each: what the belief assumes must be true, and the first questions it raises. This is a table of contents for the research, not its boundary.

Two readings of the dictation, confirmed by you on 2026-11-22: "using creativity and inertly test you must ambitious effective solutions" is read as **"creativity to invent and test ambitious, effective solutions"**; "steward of platforms of dating integration information" is read as **"steward of platform, data and integration information"**.

---

## B1. People spend their time choosing problems and inventing solutions

- **B1.1** Most human time goes to critical thinking and empathy, used to choose and prioritise the most pressing problems.
- **B1.2** Human creativity goes to inventing (and testing) ambitious, effective solutions.
- **B1.3** (implied by B4) Human judgment and accountability stay with people.

*Assumes:* the coordination work in B3 really is most of the job today, so removing it frees most of the time; problem selection is a skill that can be developed and scaled across thousands of PMs, not only a talent a few have.
*First questions:* if everyone spends their time choosing problems, who decides between people's choices? Does empathy need direct customer contact that agents now mediate?

## B2. Validation moves upstream, into intent

- **B2.1** Prototyping and technical validation of solutions are pulled forward and become part of developing intent, not steps after it.
- **B2.2** Intent starts as a slate of competing ideas, not a single idea.
- **B2.3** Each idea goes through many short validation loops, rising in fidelity and exposure: mock or simulated, then small-scale test, then larger-scale test.

*Assumes:* building a credible prototype is cheap enough to do for every idea in a slate; simulated tests predict real behaviour well enough to cut ideas; there is enough test capacity (traffic, customers, permission) for many small tests.
*First questions:* in a regulated lender, which tests can touch real customers (fair lending, disclosures, complaints), and how much weight can simulation carry before it misleads? What kills an idea from the slate, and who decides?

## B3. Agents take the coordination work that fills most of product management today

- **B3.1** Agents displace people in the tasks that occupy most of product management today:
  - researching existing capabilities;
  - always-on monitoring;
  - negotiating integrations between systems;
  - stakeholder updates;
  - finding information that is already written down somewhere;
  - stewarding platform, data and integration information.
- **B3.2** Today people insert themselves to verify work that agents could perform on every platform; that stops.

*Assumes:* the information agents need is written down and current; platforms expose their capabilities in a form agents can read; agent verification is trusted by the people and regulators who now rely on human sign-off.
*First questions:* is "most of PM time" true by measurement (time diaries, surveys) or by feel? Is human verification removed, or moved to a smaller number of sampled, risk-weighted checks?

## B4. Every platform, experience and operational process has an owner agent

- **B4.1** Each platform, customer experience and operational process has a corresponding agent that owns it.
- **B4.2** The owner agent takes every task that doesn't need creativity, critical thinking, or human judgment and accountability.

*Assumes:* "ownership" can be split cleanly between what needs judgment and what doesn't; each owner agent has a human who answers for it; owner agents can talk to each other (B3's "negotiating integrations").
*First questions:* who is accountable when an owner agent acts wrongly? How many owner agents can one person steward?

## B5. Everything in market is traceable to the intent that produced it

- **B5.1** Every in-market test and feature is traceable to the requirements and intents that produced it.
- **B5.2** That record is available for the past and curated for the future, mostly by agents.

*Assumes:* intent is captured as a durable artifact at the time (not reconstructed); the link survives reorgs, tool changes and many small loops (B2.3).
*First questions:* who reads the record, and what decision does it change (regulators, the next PM, the owner agent)?

---

## Tensions inside the beliefs (for research to test, not conclusions)

1. **B3.2 vs B1.3/B4.2.** Removing human verification sits uneasily with keeping accountability human. The likely resolution is a different verification design (risk-sloped, sampled, evidence-producing), not none; research should say which.
2. **B2.2 vs B1.1.** A slate of competing ideas multiplies the judgment needed to pick among them. Freed time may be absorbed by deciding, not by more discovery.
3. **B2.3 at a bank.** Larger-scale tests on real customers are constrained by regulation and customer harm, so the loop may lean on simulation, whose predictive power is unproven (see the project's synthetic-users-limits theme).
4. **B4 needs B5.** An owner agent is only as good as the intent record it can read; B5 is a prerequisite, not a result.

## Where you are silent (research will cover these too)

Team shape and talent (ratios, roles, the junior pipeline, career ladders); what happens to design and engineering; strategy, portfolio and funding (how slates get funded against annual planning); direct customer contact; risk, compliance and model risk in a regulated enterprise; measuring outcomes; the economics of running agents; distribution and go-to-market; change management and adoption at scale; the human experience (burnout, meaning, deskilling); decision rights and governance; data quality as a foundation; and timing (how fast the trajectory moves).
