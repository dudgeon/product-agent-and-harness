---
title: "The Codex feature that works while you sleep"
source_url: https://www.lennysnewsletter.com/p/the-codex-feature-that-works-while
author: Claire Vo (host)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-05-27
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [agent-ready-intent, evals-autonomy-trust, pm-job-stable-methods-change, human-review-gates, cost-control-routing, agent-failure-modes]
relevance: high
---

## Relevance to the project
A short, concrete walkthrough of Codex's /goal command, which turns a prompt into a loop (work, verify, decide next step) that runs until there is evidence the outcome is met. Its value for the project is the six-part structure for writing a goal (outcome, verification, constraints, boundaries, iteration policy, stop/blocked behaviour), taken from OpenAI's "Using Goals in Codex" cookbook. That is a ready-made candidate shape for "intent that's ready to ship" when the receiver is an agent: it bears on intent-shaping-and-spec and on review-and-autonomy. Vo explicitly frames writing goals as a PM skill ("outcomes, not outputs") that now needs more technical precision about verification.

## Themes
- agent-ready-intent: six components of a strong goal: outcome (what's true when done), verification (test suite, browser check, a number), constraints (what can't regress), boundaries (tools and files allowed), iteration policy (how to choose the next try), and what to do when blocked (stop and report evidence, blocker and what it needs) (7:34-9:21). Example: get P95 checkout latency below a threshold, verified by the checkout benchmark, correctness suite kept green (6:16-9:21).
- evals-autonomy-trust: goals work only with "an evidence-based finish line"; good goals have "a durable objective, an evidence-based finish line, and a path that may require several turns"; don't use for one-line edits, vague finish lines ("make my customers happy") or open refactors (24:41-25:00).
- pm-job-stable-methods-change: "Outcomes, not outputs ... you should be defining what success looks like"; PMs "are going to have to get a lot better at prompting these AIs with good goals" because the level of validation required is more technical than OKR writing (26:29-28:03).
- human-review-gates: the Vercel-errors goal ends by opening a branch and PR per fix and reporting "all PRs to review and issues that could not be fixed" to the human (14:02); the inbox goal labels ambiguous mail "needs judgment" rather than acting (18:42).
- cost-control-routing: the inbox run took 3h52m and "about six million tokens. So it was not token cheap" (18:42); she picks a medium model for a non-deep-thinking goal (14:02).
- agent-failure-modes: her agents (OpenClaw) given Linear access created many tasks they never did, leaving a backlog to clean up (20:22-21:54).

## Key points
- Prompt vs goal: a prompt is turn-based and waits; a goal keeps looping and checking until it can gather evidence the goal is met, then marks it complete (1:50-3:08). Lifecycle: set, view, pause, resume, clear (5:05).
- Her first goal ran 5h45m, the longest autonomous run she'd had; before /goal she couldn't get multi-hour autonomous tasks (4:06).
- ChatPRD case (first-party for her company): a diff-based PRD editing tool threw recurring "invalid operation" errors on complex documents; the goal replayed every Sentry trace, categorised, fixed root causes and re-ran all examples until none remained; result was a systematic fix, with zero edit errors since, per Vo (9:36-12:30).
- Live demo on Vercel API errors: Codex built a 3-5 step plan (inventory repo, pull two weeks of errors, classify user-facing vs not, fix or downgrade, publish PRs). Outcome not shown in the episode (13:18-17:09).
- Non-technical: about 3,900 unread emails to 68 needing attention, with labels and unsubscribes; Linear backlog cleanup by a stated rule (cancel non-done tasks for released episodes) (17:28-23:27).
- She feels "much more in manager mode than builder mode" and isn't sure she likes it (28:03); "my babysitting days are largely over" (26:29).

## Notable quotes
- "Prompts are an instruction of what to do. Goals is a description of what a good outcome is and how to get to that outcome." (9:21)
- "Product managers are going to have to get a lot better at prompting these AIs with good goals." (26:29)
- "It really feels like I'm much more in manager mode than builder mode." (28:03)

## Could not verify
- Full transcript read (about 30 minutes). The six-part framework is OpenAI's (cookbook "Using Goals in Codex"), presented by Vo; not read directly here.
- Results (zero errors, 3,900 to 68 emails, 6M tokens) are Vo's own report; the Vercel demo result was deferred to a follow-up. Vo runs ChatPRD.
