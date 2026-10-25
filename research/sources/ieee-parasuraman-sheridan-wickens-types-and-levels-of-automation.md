---
title: "A model for types and levels of human interaction with automation"
source_url: https://doi.org/10.1109/3468.844354
author: Raja Parasuraman, Thomas B. Sheridan, Christopher D. Wickens
publisher: IEEE Transactions on Systems, Man, and Cybernetics Part A 30(3): 286-297
published: 2000-05-01
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [levels-of-automation-frameworks, decision-rights-for-agents, overreliance-and-deskilling]
relevance: high
---

## Relevance to the project
The canonical levels-of-automation model (over 4,000 citations): automation is applied separately to four stages of a task (information acquisition, information analysis, decision selection, action implementation), each on a continuum from manual to fully automatic, with Sheridan and Verplank's ten levels as the scale for the decision stage. It says autonomy is not one slider but one per stage, and it names skill degradation and complacency as primary evaluation criteria. This is the frame the project's dimension 1 (control flow) and dimension 4 (decision rights) are approximating; it also shows that a PM agent can be fully automatic at acquisition and analysis while staying low at decision selection.

## Themes
- levels-of-automation-frameworks: four functional classes, each automatable on a continuum; human performance consequences are the primary evaluative criteria, with automation reliability and the costs of decision/action outcomes as secondary (abstract via OpenAlex).
- decision-rights-for-agents: the model separates "decision selection" from "action implementation", so who decides and who acts are distinct settings (abstract; my reading).
- overreliance-and-deskilling: the primary criteria in the full paper are mental workload, situation awareness, complacency and skill degradation (well known from the paper; not confirmed in the abstract read).

## Key points
- The Sheridan-Verplank (1978) scale runs from 1 (computer offers no assistance) through 5 (executes a suggestion if the human approves), 6 (allows the human a restricted veto time before automatic execution), to 10 (computer decides everything and ignores the human); levels 5-6 are the "ask vs auto" boundary modern agent harnesses expose.
- Agent-harness equivalents (my mapping): read-only exploration = acquisition automated; Plan mode = analysis automated, decision human; acceptEdits = implementation automated for low-risk actions; auto mode with classifier = decision delegated to a second automated judge.

## Could not verify
- IEEE page returned empty content; the abstract was reconstructed from OpenAlex with gaps. The ten-level scale and the primary criteria list are from my knowledge of the paper, not the text read.
