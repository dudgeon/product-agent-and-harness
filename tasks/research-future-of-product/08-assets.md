# Assets that would support the product loop (first draft)

A first pass at what a bank would need to build or buy for the moves to work as the Priya scenario shows them. It is a working list, open to argument, and it will change as more scenarios test it. Where something already exists in our own work, it is named (Flight Deck corrections from its own agent, 2026-11-23): the Flight Deck prototype (the cut-down Omnigent fork, with Product Aviator as its interface) and this project's agent designs.

## Agents

- **Problem discovery agent** (Sense, Investigate). Watches the outcomes and customer signals for an area, raises problems nobody asked about, and lays out competing explanations with the evidence for each. *Exists in part:* Flight Deck's `problem-discovery` skill, which runs when asked; nothing yet watches continuously.
- **Customer research agent** (Investigate, Challenge). Recruits, runs consented structured interviews at scale, links every answer to its recording, and suggests who the person should meet directly.
- **Prototyping agent** (Prototype). Builds working versions in safe copies of the real systems within hours.
- **Challenge agent** (Challenge). Replays real history, runs simulations and the economics, tests for bias such as selection effects, and argues the other side when asked.
- **Steward agents**, one per platform, journey or operational process (Sense, Design, Learn). Know their area, keep it running, fix small things, propose how a change fits, and work out connections with other stewards. *Related:* this project's dependency agent, which finds and asks the owners a change depends on.
- **Coding agents** (Build). Write the production change and its tests from the intent and the design.
- **Checking agents** (Verify). Independent of the builders. Test, check security and accessibility, and assemble the evidence the bank's rules require.
- **Risk agent** (Release). Holds the limits for automatic release within policy the risk function owns, and watches changes after release.

## Skills a person's agent would carry

- **Framing a hypothesis:** the problem, the answer, the outcome it should move, the risk accepted, and what would prove it wrong. *Exists in part:* Flight Deck's `intent-shaping` skill (its template has no field yet for the risk accepted or what would prove it wrong); this project's requirements agent design.
- **Arguing the other side:** the strongest case against the current hypothesis and the evidence that would settle it.
- **Writing short intent** and **finding what a change depends on** and who must be asked. *Exists in part:* Flight Deck's "Solution design" arc, which goes from a written description of the change to its requirements, dependencies and alternatives. It produces most of a solution design, and today one Flight Deck template holds both the statement of intent and the solution design; this project's dependency agent.
- **Recording a decision** with its reasons, so it travels with what ships. *Exists in part:* `decision-review` and `decision-brief`.
- **Engaging the owners a change depends on**, including exchanging with an owner's agent. *Planned:* Flight Deck's "Engage owners" arc, the person's side of a steward agent.
- **Reporting where work stands** from the systems where it happens. *Exists in part:* `delivery-status`.

## Artifacts

Three artifacts carry the work. The first two are easily confused and are different things; neither is called a spec or a PRD, because people read their own meaning into those words.

- **Statement of intent** (Hypothesize). Written by the person: what will change, the outcome it should move, the risk accepted, what would prove it wrong, and the trade-offs accepted. Short, because agents supply the standing rules.
- **Solution design** (Design). Drafted by agents, settled by people: how the change fits the existing platforms, the connections between them, what it depends on, the alternatives considered, and the trade-offs decided.
- **Decision record** (Decide, Learn). What was chosen or stopped, and why, linked to the evidence.

## Shared material

- **Customer signals** people and agents can reach, with consent, and summaries that lead back to recordings.
- **A current account of each platform:** what it does, its limits, who answers for it; kept by its steward.
- **The bank's rules** (standards, policies, regulatory obligations) in a form agents can apply, with named people to interpret the unclear cases.
- **Safe copies** of the key systems to build in, and the ability to replay real history and model the money.
- **Agreed definitions** of the measures that matter, such as what counts as a redemption.
- **The trail:** each change linked to the problem, the evidence, the trade-offs and the decision. *Exists in part:* Flight Deck initiatives keep evidence, open questions, decisions and readiness with dated artifacts.
- **Release limits:** which kinds of change go out on their own, held where the risk agent and the people who set them can see them.

## The workspace

- **A place where one person runs their agents and skills**, sees what they produced, challenges it, and hands work to the stewards and builders. This is what Flight Deck prototypes, on top of the Omnigent meta-harness.

## Open questions

- Which of these a bank would buy, which it would build, and which come with the coding and agent platforms it already uses.
- Whether steward agents are one kind of agent configured per area, or separate agents.
- How much of the shared material exists today in usable form; the starting state suggests little.
