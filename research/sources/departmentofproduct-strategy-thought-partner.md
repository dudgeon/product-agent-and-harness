---
title: How to build a Strategy Thought Partner Grounded in Product Frameworks with Claude Code
source_url: https://departmentofproduct.substack.com/p/how-to-build-a-strategy-thought-partner
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-05-27
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [non-engineer-builders, human-judgment-pm-jobs, org-context-grounding, synthetic-users-limits, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
A build tutorial in which a PM vibe-codes, in the Claude Code desktop app, a local web app that walks a feature idea through any of 26 product frameworks as a guided conversation, framed as "cognitive expansion" rather than "cognitive offloading". It matters as an example of the strategy and prioritisation job handled by a framework-structured sparring partner rather than an answer generator, and of a PM building a bespoke tool instead of using skills in a general harness. It is the author's own prototype (local storage, no database, "by no means production-ready"), so it is not evidence of use at work. The framing quote is attributed to Adobe's former CPO, second-hand.

## Themes
- human-judgment-pm-jobs: the stated aim is to use AI "to think more clearly, not asking it to think for you"; each framework runs as a step-by-step conversation that asks for inputs and pushes back (section 6).
- non-engineer-builders: the whole tool is built by prompting Claude Code, extending an earlier DoP "persona feature tester" app; prompts are given for each step (sections 1 to 7).
- org-context-grounding: adds a company-context settings page whose text is fed into every analysis, replacing a hard-coded fictional company (section 5).
- synthetic-users-limits: the base app runs features past "data-grounded" synthetic personas, including voice calls via ElevenLabs; no validation of the personas is discussed. See [NN/g](nngroup-synthetic-users.md).
- work-structure-spectrum: frameworks act as the structure: a recommender picks three frameworks for a described situation, then the chosen one scripts the conversation; outputs end as a downloadable visual (e.g. a 2x2).

## Key points
- Flow: describe or import a feature (from Linear), then choose "run past personas" or "apply frameworks"; a frameworks gallery sits in the sidebar.
- Framework library of 26 across discovery, strategy, prioritisation, delivery and decision-making (Kano, JTBD, pre-mortem, Porter's Five Forces, RICE, MoSCoW, North Star, opportunity scoring, impact/effort and others), each with a longer description and links to sources.
- Recommender: describe your situation and get the three most applicable frameworks with a reason each.
- Conversations are saved locally as history; a visual (PNG) can be generated at the end for a few frameworks; the author suggests giving each framework its own visual spec for consistency.
- Distributed as a pre-built app plus the prompts to rebuild it.

## Could not verify
- The Adobe former-CPO "cognitive offloading" remark (no link in the text).
- Screenshots and the downloadable app were not inspected.
