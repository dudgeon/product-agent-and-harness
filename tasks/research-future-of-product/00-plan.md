# The future of product: research plan

*Kept as history. Steps 1 to 4 ran as written; the later steps changed after review. See [00-summary.md](00-summary.md) for where the work stands.*

**Aim:** an opinionated, evidence-based set of truths about where product development is going, written so it holds for a large regulated enterprise at scale (a national bank and card issuer), not only startups. It covers the development of all products, deterministic systems as much as AI products: more products will include AI, but most of a bank's estate (servicing, payments, ledgers, disclosures) is deterministic, and agents will help build both. The truths also name the backward ways of working an average pre-AI enterprise must get past: coordination that runs person to person, information held captive in people's heads and meetings, thousands of operational processes, hundreds of thousands of regulatory obligations, and decades of organisational memory that was never written down. The truths say these plainly, even when it seems obvious. The truths are aspirational but grounded: each one can describe a future very different from today, provided the current trajectory points there. Each truth states the capabilities and data it needs, and the talent and organisation it needs. Next to the truths sit representative scenarios: notional PMs working the new way. The final prose is yours, in your voice. Research challenges it and fills the gaps; it doesn't replace it.

## The two paths, and how they converge

| | Path A: your beliefs | Path B: the expert view |
|---|---|---|
| Input | Your doc, broken into [01-your-beliefs.md](01-your-beliefs.md) (B1-B5, 14 claims) | Lenny's podcast and newsletter (Nov 2025 to Nov 2026), plus this repo's tech-beacon teardowns |
| Built by | You, then me | Sonnet readers extract; a Fable agent synthesises |
| Weighting | Your beliefs are the table of contents, not the weighting | Evidence decides; your beliefs get no extra weight |

### Step 1. Break your beliefs apart (done)
[01-your-beliefs.md](01-your-beliefs.md): five beliefs, 14 numbered claims, what each assumes, the tensions inside them, and where you are silent.

### Step 2. Extract (running)
Six Sonnet readers, each writing a claim-by-claim extraction (`scratch/extract-*.md`) and filing source notes in `research/sources/` per the project rule:
- four on the 61 Lenny's Podcast episodes from Nov 2025 on, split evenly across the year;
- one on newsletters from the same period plus targeted searches (How I AI, older posts that set up the argument);
- one on this repo's teardowns (Ramp Glass, Shopify River, Stripe, Uber Cortana, Block, Airbnb/Spotify and others): what their tooling implies about the profession, and whether it reflects a thoughtful view of where product work is going or is just tooling.

Each claim is tagged by type (practice, data, prediction, prescription, dissent), by whether it supports, challenges or extends one of your claims or opens a new area, by whether it holds at a large regulated bank, and by the capabilities, data, talent and organisation it assumes.

### Step 3. Synthesise the expert view (Fable)
`02-expert-view.md`: a set of truths in sections that follow B1-B5, then new sections for areas you were silent on. Each truth gives: the claim; the trajectory evidence (who, what, how strong); confidence; how it lands at a bank (what's stronger, what's weaker, what breaks); capabilities and data required; talent and organisation required; and where it agrees with you, differs or goes further. Contradictions between experts are kept, not averaged.

### Step 4. Converge
`03-convergence.md`: your claims and the expert truths side by side, marked agree, differ, you go further, they go further, or you're silent. For each difference: the evidence on each side and the question that would settle it. I'll bring you only the differences that are yours to decide, one at a time, with the evidence. Gaps the synthesis flags (likely: regulated experimentation, simulation fidelity, model-risk governance of agents, bank operating models) get a short targeted round on the open web.

### Step 5. Write the truths
`04-truths.md`: the converged list, in your voice: clear, precise, concise. Each truth with its required capabilities and data, talent and organisation, and its evidence links.

### Step 6. Scenarios
the scenarios (kept local): four to six notional PMs at a large bank and card issuer working the new way. Each scenario exercises several truths and shows what changed, what the agents do, what the person decides, and what has to exist (data, platforms, controls, skills) for it to work. Candidate cast, to be fixed after Step 4: a card rewards PM running a slate of ideas through simulated and small live tests; the PM of a servicing journey and its owner agent; a payments platform PM whose agents negotiate integrations with other platforms' agents; a PM taking a disclosure-heavy change from intent to market with full traceability; a product leader funding slates instead of roadmaps; a new PM learning judgment when the drafting is done for them. A first draft can come with Step 3, marked draft, and is rewritten after Step 4.

### Step 7. Point of view
a point-of-view document (later dropped): where we are now (each statement with how we'd validate it), where leaders are heading and what they recommend, the activities a large bank would run to get there (workstreams, dependencies, signals it's working, no dates), and the future (04).

### Also delivered (the project's standing rules)
Source notes and the theme file in `research/`, `python3 research/build.py` with 0 warnings, options and key questions in `options/contributions/research-future-of-product.md`, and `00-summary.md`.

## What I'll check before calling each step done
- Step 2: every claim in an extraction has a timestamp or section reference; skipped items have reasons.
- Step 3: every truth names its evidence and its bank-scale verdict; every one of your claims is addressed (agree, differ or open), and at least the silent areas in 01 are covered or explicitly set aside.
- Steps 5-6: every sentence in the truths traces to evidence or to a decision you made; every scenario names the truths it shows.
