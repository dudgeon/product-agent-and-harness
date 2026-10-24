---
title: "Why your AI product needs a different development lifecycle"
source_url: https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different
author: Aishwarya Reganti and Kiriti Badam (guest authors), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2025-08-19
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, risk-sloped-review, human-review-gates, outcome-measurement-gap, human-judgment-pm-jobs]
relevance: high
---

## Relevance to the project
The written source of the Continuous Calibration/Continuous Development (CC/CD) framework that the authors later discussed on the podcast (see [lenny-podcast-reganti-badam-ai-deployments](lenny-podcast-reganti-badam-ai-deployments.md)). It gives the project a concrete, borrowable method for two open questions: how a PM agent should earn autonomy (review-and-autonomy) and how we would know it works (pm-agent-evaluation). The core moves are: version by agency rather than by feature set, start high-control and low-agency, build "control handoffs" so humans can take back any decision and every correction is logged as eval signal, and only climb a rung when calibration stops surprising you. It is written for AI features in products, not for PM tooling, so applying it to a PM harness is our inference. Evidence is the authors' consulting experience across "over 50" deployments; they sell a course on it.

## Themes
- evals-autonomy-trust: "Every time you give an AI system more agency, you give up some control" (section 2); "If you haven't tested how the system behaves under high control, you're not ready to give it high agency." Each version is defined by agency granted, not features (CD 1); the loop "turns into a flywheel" as the system earns agency each cycle.
- risk-sloped-review: start with "simple decisions that are easy to verify and easy for humans to override" (CD 1); examples of three-rung ladders: support (route, suggest resolution for human review, auto-resolve with human fallback), marketing (draft copy, build campaigns, launch and auto-optimise), coding (completions, larger blocks for review, autonomous PRs), the last said to be how Copilot and Cursor climbed.
- human-review-gates: "control handoffs" designed in from the start, e.g. a misrouted ticket is easily rerouted by the receiving agent, and that correction is logged (CD 2); handoff logs double as eval data (CC 4).
- outcome-measurement-gap: evals are application-specific and change per rung (routing accuracy at v1, retrieval relevance at v2); evals built from the reference dataset will miss real behaviour, so "step 6 may also involve revisiting and rebuilding your evals" (CC 6).
- human-judgment-pm-jobs: "At the heart of CC/CD is judgment": what to ship, how to protect users, when to hand control back, what "good enough" means; the framework only gives existing product instinct "a loop, a rhythm, and a shared language" (closing section).

## Key points
- Two reasons AI products differ: non-determinism on both ends (open-ended user input and model output) and the agency-control trade-off (sections 1-2).
- Continuous Development: (1) scope capability and curate a reference dataset of 20-100 examples with expected outputs and the metadata that drives the decision, which also reveals what context the system needs; (2) set up the simplest application that gives signal, with logging of inputs, outputs and user interactions and guardrails/compliance basics; "Don't overengineer"; (3) design evals and run them against the reference set for broad coverage, not perfection.
- Deploy to a small cohort as a transition, not a finish line.
- Continuous Calibration: (4) run evals on live logs, sampling by system-specific proxies (e.g. human reroutes as routing accuracy; turn counts, thumbs feedback) or the full set if only 2,000-3,000 logs; (5) manually review 20-50 worst cases per segment and document recurring error patterns in a table; (6) apply fixes (prompt, model, retrieval, task decomposition), "engineer more" only now and only backed by data, re-run evals offline without redeploying.
- Worked failure chain: if v3 ships first, a refund mis-tagged as billing pulls the wrong SOP and yields a plausible wrong answer; the error starts at routing, compounds through missing context and is hard to untangle (putting it together).
- "Never lead with the tech. Let the problem, evals, and data guide what gets added next."
- Analogy: onboarding a brilliant new teammate who doesn't know how the team works; expand scope as trust is earned.

## Notable quotes
- "Every time you give an AI system more agency, you give up some control." (section 2)
- "Never lead with the tech. Let the problem, evals, and data guide what gets added next." (CC 6)

## Could not verify
- Post read in full (free edition). The tables and diagrams referenced in the text were images and not available; their content is inferred from the surrounding prose.
- The "over 50 AI implementations" and the claim that Copilot and Cursor followed this ladder are the authors' assertions; no deployment data is given.
