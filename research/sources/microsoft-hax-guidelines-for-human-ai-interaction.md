---
title: "Guidelines for Human-AI Interaction (the 18 HAX guidelines)"
source_url: https://www.microsoft.com/en-us/haxtoolkit/library/?content_type%5B%5D=guideline
author: Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, Adam Fourney, Besmira Nushi, Penny Collisson, Jina Suh, Shamsi Iqbal, Paul Bennett, Kori Inkpen, Jaime Teevan, Ruth Kikin-Gil, Eric Horvitz (Microsoft)
publisher: Microsoft HAX Toolkit; original paper ACM CHI 2019 (honourable mention)
published: 2019-05
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [levels-of-automation-frameworks, human-review-gates, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
The most-used practitioner checklist for human-AI interaction, validated with 49 practitioners against 20 products. Grouped by phase (initially, during interaction, when wrong, over time), it operationalises human control: efficient invocation (G7), dismissal (G8), correction (G9), scoping services when in doubt (G10), global controls (G17) and cautious adaptation (G14). For skill design it is a ready list of the affordances a PM agent must expose to keep the human in control at any autonomy level, and a useful lint for process artifacts.

## Themes
- levels-of-automation-frameworks: G10 "Scope services when in doubt" is the guideline form of Horvitz's uncertainty-scaled initiative (library page).
- human-review-gates: G7-G9 (invocation, dismissal, correction) and G16 (convey the consequences of user actions) define what a review gate must let the human do (library page).
- evals-autonomy-trust: G2 "Make clear how well the system can do what it can do" and G11 "Make clear why the system did what it did" are calibration guidelines; see Bansal et al. for the evidence that G11 alone can raise overreliance (library page; my cross-reference).

## Key points
- G1 make clear what the system can do; G2 how well; G3 time services on context; G4 show contextually relevant information; G5 match social norms; G6 mitigate social biases; G7 efficient invocation; G8 efficient dismissal; G9 efficient correction; G10 scope services when in doubt; G11 make clear why; G12 remember recent interactions; G13 learn from user behaviour; G14 update and adapt cautiously; G15 encourage granular feedback; G16 convey consequences of user actions; G17 global controls; G18 notify about changes.
- Validation: user study with 49 design practitioners testing the guidelines on 20 AI-infused products (Microsoft Research page).
- Written for 2019 ML features; the guidelines do not address multi-step agents acting over time, which is where the project's autonomy questions sit.

## Could not verify
- Derivation method beyond "multiple rounds of evaluation" (the CHI paper PDF was not read).
