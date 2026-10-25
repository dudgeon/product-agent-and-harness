---
title: "Principles of mixed-initiative user interfaces"
source_url: https://doi.org/10.1145/302979.303030
author: Eric Horvitz (Microsoft Research)
publisher: ACM CHI 1999, pp. 159-166
published: 1999-05
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [levels-of-automation-frameworks, human-review-gates]
relevance: medium
---

## Relevance to the project
The 1999 paper that framed the choice between direct manipulation and autonomous agents as a design space rather than a war, and proposed principles for when an agent should act, ask or stay quiet based on uncertainty about the user's goals and the expected cost and benefit of acting. Its principles (significant value-added automation; dialog to resolve uncertainty; efficient invocation and termination; minimising the cost of poor guesses; scoping precision of service to uncertainty; remembering interactions; continuing to learn) are the ancestors of Microsoft's 18 HAX guidelines and of the "ask when unsure, act when safe" logic in agent harnesses.

## Themes
- levels-of-automation-frameworks: mixed initiative means the system decides, per moment, whether to take initiative, using inferred goals and decision theory (abstract via OpenAlex).
- human-review-gates: the LookOut scheduling system illustrates asking versus acting under uncertainty (abstract).

## Key points
- About 1,470 citations (OpenAlex).
- The twelve "critical factors" listed in the paper are known from the full text, not confirmed in the abstract read; they are reflected almost one-to-one in Amershi et al. 2019 (G7 efficient invocation, G8 dismissal, G9 correction, G10 scope services when in doubt, G12 remember recent interactions, G13 learn from behaviour).

## Could not verify
- Full text (ACM page returned 403; the PDF at erichorvitz.com could not be parsed); the principle list is from memory of the paper and from the HAX guidelines that cite it.
