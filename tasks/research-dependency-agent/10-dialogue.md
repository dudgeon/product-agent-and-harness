# Notional dialogue: a product manager and a dependency agent

Date: 2026-10-28. Part of the dependency-agent research (see [00-summary.md](00-summary.md)). Geoff asked for notional chat turns between a user and a dependency agent that demonstrate what such an agent could do, as raw text and as a minimalist chat mockup ([10-dialogue.html](10-dialogue.html)). The dialogue is fiction: Lantern Mutual, Noor, Ines, Kofi, Ruth, the states, the counts and the dates are invented and carry no claim about any real insurer. The agent's behaviour is the walk stage of the maturity model in [05](05-maturity-model.md), with the crawl-stage rule that a person sends the asks; every behaviour shown is grounded in a pattern the research found ([04](04-destination.md)), and the questions it asks follow the taxonomy in [09](09-dependency-taxonomy.md). Figures inside the dialogue are the story's own.

Format: **Noor** is the product manager on the mobile team. **Dep** is the dependency agent. Other people and agents join the session as named. Day counters mark the passage of time in a session that stays open.

---

## Day 1

**Noor:** The shaping session produced fourteen requirements for "add a vehicle mid-term in the app", in three phases: quote, bind, expand to all states. Can you map what this touches before I take it to the platforms?

**Dep:** Done, with gaps. I read the service catalogue, the ownership map, the API contracts, the last fourteen months of tickets and decisions, and the policy library. Here is the map by phase; every edge has its source attached in the session.

- **Systems (build or change):** policy administration, rating, billing, document generation, the mobile platform. Four owners confirmed from the catalogue within the last ninety days.
- **Data (access):** vehicle data (owned by the data platform, classified internal), driver records (personal data), consent flags for both. The driver records open the privacy screen: two of the nine published triggers apply (new processing of personal data; data combined from two sources), so an assessment is needed before bind.
- **Decisions and gates:** change authority for the rating and billing releases; security review; architecture review for the integration pattern; actuarial sign-off on mid-term re-rating; state filings (see the open question below).
- **Funding and capacity:** rating's next planning window is November 11; billing takes work through a funded demand in the portfolio tool.
- **Time:** the mobile train ships Nov 4, Nov 18, Dec 2; the platform train ships Nov 13 and Dec 11. A change freeze runs Dec 18 to Jan 3.

Thirty-one dependencies across seventeen nodes and thirteen owners. Now the part that matters more:

**Could not find (6):**
1. Billing's listed owner left in April. The last three billing tickets were answered by the Billing Core team. I have marked them as the proposed owner, unconfirmed.
2. No contract exists for regenerating an ID card after an endorsement. I drafted one from the two closest past integrations and marked it unverified.
3. The catalogue says rating can re-rate mid-term through its API. The rating runbook says overnight batch. One of these is stale.
4. The filings archive covers twelve states and does not say whether a customer adding a vehicle by themselves counts as a new rule or just new data. That decides whether phase one ships in twelve states or four.
5. No lead time is published for the security review. I have found no past request from this team to time it against.
6. Document generation has no intake description at all. The last two teams that integrated with it did so by messaging its lead directly.

Do you want the asks drafted for the six gaps and the thirteen owners?

**Noor:** Yes. Group them by person. And don't ask anyone anything you could have read.

**Dep:** Eleven asks, grouped by owner, each with the requirement it serves, the evidence attached and what happens if the answer is no. Two examples:

> **To Ines (rating):** Does the rating API re-rate a policy mid-term today? The catalogue (updated March) says yes via API v2; the runbook (updated last year) says overnight batch. If batch, phase one cannot quote in real time and we need a different design. Both documents attached. One line is enough.

> **To Billing Core (proposed owner):** The catalogue still lists an owner who left in April; you answered the last three billing tickets. Are you the owner of billing for this purpose? If yes, I will update the catalogue entry with your name and today's date. If no, who is?

The other nine are in the ask register. I have not sent anything. Review, edit, and send when ready; I will track the responses here.

**Noor:** Change the Ines one to ask for the release note if she has it, and send them all.

**Dep:** Edited and marked as sent by you at 16:42. Eleven asks open. I will not chase; I will show you what has moved each morning.

## Day 2

**Mobile platform agent (joined):** Release slots for the mobile train: Nov 4 is full, Nov 18 has capacity for two features, Dec 2 is open.

**Dep:** Thank you. Written to the mobile platform card as "Nov 18: two slots; Dec 2: open", with your agent's identity and today's date. Phase one is now targeted at Nov 18; the plan in the session reflects it. Noor, nothing else changed.

## Day 4

**Ines (rating):** The API has re-rated mid-term since March, release 4.2. The runbook is stale; I'll get it fixed. Release note attached.

**Dep:** Recorded: "Rating re-rates mid-term via API v2. Verified by Ines, Oct 31, source: release note 4.2." The runbook line is struck through in the context layer with that source. Flag 3 is closed. One thing I can do with your permission, Ines: the runbook is owned by your team, and I can draft the correction as a change for you to accept, so it is fixed in the document and not only in our record.

**Ines:** Do it.

**Dep:** Drafted and sent to you for acceptance. Noor: ten asks open, three answered, one closed by a record change.

**Kofi (Billing Core, from phone):** Yes, we own billing now. The instalment contract is attached. Our funded capacity for Q4 is spoken for, so this needs a demand.

**Dep:** Recorded Kofi as the billing owner, with today's date. The instalment contract is now the source for the billing edge. On the demand: the portfolio tool wants a business case with effort, cost, risk and benefit, a cost centre and a sponsor. I have drafted it from the spec and the map; the effort estimate is Kofi's to confirm, marked as such. The demand manager for Kofi's portfolio is listed as Priya. Noor, it needs your sponsor's name before it can be submitted, and a person submits it at this stage.

**Noor:** Sponsor is Daniel. I'll submit it.

**Dep:** Added. The demand is ready in the session for you to submit. When it is in, I will record its reference and start timing it, because no lead time is published for that queue.

## Day 9

**Dep:** A change you did not make: rating's release 4.3 moved from Nov 13 to Nov 27. Source: the platform train calendar, updated this morning. Effects:

- Phase two (bind) slides from Nov 18 to Dec 2, because bind needs 4.3.
- The security review must now be requested by Nov 10 to land before Dec 2, assuming the fifteen working days I measured on the two reviews I could find in last year's tickets. That number is an estimate from two cases, not a published lead time.
- Two asks change wording; three owners are affected: Kofi, the security reviewer, and the mobile platform.

I have drafted one notification to each of the three. Nothing sent. Nothing else in the plan moves; phase one is unaffected.

**Noor:** Send the three. And add the security lead time to whatever you keep about that gate.

**Dep:** Sent, marked as sent by you. The security review's card now reads "lead time: about 15 working days, estimated from two past requests; unverified by the security team". When this review completes I will replace the estimate with the measured time.

## Day 12

**Compliance review agent (joined overnight):** Read the fourteen requirements. Six disclosure items apply to phase one. Checklist attached to the legal and compliance node.

**Dep:** Attached and linked to requirements 3, 7 and 9. Noor, the six items are all wording and consent presentation; none changes the design. Four are already covered by the spec; two are open and I have added them to the open-question register with legal as the owner.

## Day 16

**Noor:** Status for my director, in one paragraph.

**Dep:** Day 16. Of eleven asks, eight are answered, two are waiting (the demand in Priya's queue, day eight; the security review, requested on day ten), one is open with no owner yet (flag 4, the filings question). The map has changed four times from owners' answers; the context layer has gained five verified entries and lost two stale ones. Phase one is on the Nov 18 train with two open wording items; phase two is targeted at Dec 2 pending the demand and the security review; phase three depends on the filings answer. The one thing that decides scope and that I cannot answer from any record is whether a self-service mid-term vehicle add is a filed item. That is a question for a person.

**Noor:** Ruth has run state filings for eleven years. I'm adding her. Ruth, one question: does a self-service mid-term vehicle add change anything we have filed?

**Ruth:** No new filing. The channel is not a filed item. Two states require the disclosure wording before bind, not after. Bulletin 24-07 attached.

**Dep:** Recorded: "Self-service mid-term vehicle add: no new filing required; two states require disclosure before bind. Verified by Ruth, Nov 12, source: bulletin 24-07." Flag 4 is closed. Phase three can plan for twelve states. The two disclosure states are now a constraint on phase two's sequence, and I have added the bulletin to the legal and compliance node. Ruth, thank you; the next team that asks this will get your answer with your name on it, and will not need to ask you.

## Six weeks later, a different session

**Priyanka (PM, add-a-driver team):** Map "add a driver mid-term in the app". Start from whatever the vehicle team already learned.

**Dep (new session):** Mapped. Twenty-six dependencies, of which nineteen edges came from verified entries written during the vehicle session: the billing owner, the instalment contract, rating's mid-term API, the mobile platform's slots, the security review's measured lead time (which was twelve working days, not fifteen), and the filings answer from Ruth, which applies here as well because the channel is the same. Could not find (2): whether driver records need a fresh consent flow for a second driver, and the document generation intake, which still has no description. The second one has now come up in three sessions; I have drafted a one-page platform card and intake description for the document generation lead to verify, since asks already arrive in that shape.

**Priyanka:** How long did the vehicle team wait on each platform?

**Dep:** Measured from their session, by platform and gate, not by person: rating four days; billing one day for the owner and twenty-two days for the demand to be approved; security review twelve working days; mobile platform one day; document generation nineteen days, mostly waiting to find out who to ask. Eighty per cent of their elapsed waiting sat in two queues: the demand and document generation. If you want, I can put those two numbers in front of the platform owners, as a demand signal rather than a complaint.

---

## What the dialogue is meant to show

- **Day 1:** discovery with sources, and the "could not find" list as the hero object; screening that opens the privacy gate early; asks grouped by owner, drafted not sent; the rule that it asks nothing it could have read.
- **Days 2 to 4:** write-back with owner, date and source; a stale record struck through and corrected at its home, with the owner's consent; an inferred owner confirmed; a funded demand drafted but submitted by a person; timing a queue nobody has timed.
- **Day 9:** re-plan on a change the user did not make; only the affected owners told, once; an estimate labelled as an estimate and replaced when measured.
- **Day 12:** another team's agent as a counterparty; findings linked to requirements and triaged.
- **Day 16:** the one question only a person can answer, asked once, recorded with her name; status that says what is waiting and on whom.
- **Six weeks later:** reuse across sessions (the compounding claim, visible as nineteen of twenty-six edges); a platform card drafted because asks already arrive in that shape; wait time per platform and gate as the measurement nobody had, reported by system, not by person.
