---
title: "Advanced evals: How to find (and fix) hidden AI failures in your product"
source_url: https://www.lennysnewsletter.com/p/advanced-evals-how-to-find-and-fix
author: Hamel Husain and Shreya Shankar (guest authors); introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-09-22
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, human-review-gates, ai-synthesis-hallucination-risk, synthetic-users-limits, spec-becomes-prototype-and-evals, skill-standards, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
The clearest practitioner method in the library for how a team decides what to evaluate in an AI product, and it is written for PMs as well as engineers. Its core claim, that "error discovery" (humans reading traces until their definition of good stabilises) must precede metrics, bears directly on pm-agent-evaluation: a PM agent's evals cannot be written up front, because the criteria only emerge from reviewing its outputs ("criteria drift"). It also gives a concrete human-plus-agent division of labour for review (agent samples, builds the review UI, proposes labels; human sets the standard and accepts or rejects), which is a pattern for review-and-autonomy. The cited company wins (Shopify, Cursor, Ramp, Harvey) are reported second-hand.

## Themes
- evals-autonomy-trust: evals "turn your judgment about what 'good' looks like into repeatable tests" and, now that AI produces changes faster than people review them, let teams ship quickly (intro). Company results cited: Shopify workflow builder 2.2x faster and 68% cheaper; Cursor routing costs down 41%; Ramp receipt-matching precision 35% to 83% with on-device models; Harvey contract reviewer's internal quality score nearly doubled (intro).
- human-review-gates: the plugin makes the human annotate 10 traces before the agent may suggest errors, "a deliberate safeguard against automation bias"; aim for about 100 traces (Step 2). Agent proposals are accepted or rejected one by one.
- ai-synthesis-hallucination-risk: in a study of 100 production traces from a leasing assistant, agents caught failures visible inside a trace (answer contradicted by tool output) but missed those needing product judgment or outside context (Markdown in SMS, missed human handoffs, objection handling), and flagged good responses as failures (Find the errors section).
- synthetic-users-limits: synthetic queries generated from dimensions (task x persona x clarity), one model call per scenario for diversity; "synthetic data cannot replace real data", prefer real users (Step 1, pro tip).
- spec-becomes-prototype-and-evals: Lenny's intro repeats that guests argue "evals are the new PRDs"; nearly half of 25 PM job openings he shared asked for eval-writing experience (intro).
- skill-standards: the method ships as an open skills plugin installed with `npx skills add`; the error-discovery skill is "only two Markdown files", kept minimal so it generalises (closing section; appendix lists six other skills).
- outcome-measurement-gap: generic metrics such as "politeness" would have scored the failed leasing reply highly; prioritisation by frequency times severity is "ultimately a product decision" (Step 3).

## Key points
- Renames "error analysis" to "error discovery": the goal is to find which failures are worth measuring, the eval analogue of product discovery. If you only have time for one stage, do this one (intro).
- Criteria drift: reviewing examples changes your definition of good, so you cannot hand an agent a folder of traces and a rubric at the start. Example: a prospect says a unit is over budget; the assistant politely signs off; most agents call it a success, but the product goal was to offer alternatives (Find the errors section).
- Active learning: diverse sample (cluster representatives plus random picks), look at a few more instances of any failure found, then let the agent annotate for human accept/reject (Find the errors section).
- Traces: full record of input, system prompt, retrieval, tool calls, intermediate calls and final output; a coding agent can instrument the app to write JSONL locally or to a vendor (Step 1).
- The coding agent builds a custom local review app per data type (message thread for chat, text block with flags for writing), with metadata filters such as channel; the interface can be changed by chatting (Step 2). Design rules: show output as the user sees it; expose metadata for filtering.
- Annotation rules: describe the problem so a colleague or agent could act on it; no root-cause analysis; stop at the first upstream error; annotate failures only at first (Step 2).
- Step 3: the agent clusters annotations into failure modes with counts; in the leasing case, objection handling was in about 25% of traces and hit revenue, so it became the top priority, then was turned into a targeted eval (Step 3).
- Whole workflow said to take about 30 minutes once learned; based on teaching 4,500+ PMs and engineers and consulting with 50+ companies (Step 2 intro).

## Notable quotes
- "error discovery is the eval equivalent of product discovery" (intro)
- "No metric, dashboard, or automated eval can replace the intuition you build from reading traces." (closing section)

## Could not verify
- The Shopify, Cursor, Ramp and Harvey numbers are cited from those companies' own write-ups, not measured by the authors; evidence for them is vendor or first-party claim at one remove.
- The 100-trace study's method (which tools, how failures were scored) is not described.
- The authors sell an evals course, promoted in the post; the plugin is free. Screenshots of the review apps were not available in the text copy.
