---
title: "How Braintrust uses AI agents, evals, and CI to ship better software | Ankur Goyal"
source_url: https://www.lennysnewsletter.com/p/how-braintrust-uses-ai-agents-evals
author: Claire Vo (host), Ankur Goyal (founder and CEO, Braintrust)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-06-15
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, evals-autonomy-trust, tacit-knowledge-capture, risk-sloped-review, human-review-gates]
relevance: medium
---

## Relevance to the project
The episode's headline claim, "evals are the modern version of a PRD", is a direct statement of the option that the spec handed to an agent should be an executable definition of "what good looks like" rather than prose, and its "agent line" framework is a delegation rule for what to hand off. It also describes encoding one designer's taste into a scoring function so quality scales beyond that person, which is the same move as a checker agent encoding a reviewer's standard. But only the show notes were available (no transcript), and the guest sells an evals platform, so treat every claim as a vendor's framing. Bears on intent-shaping-and-spec, pm-agent-evaluation and review-and-autonomy.

## Themes
- spec-becomes-prototype-and-evals: show notes headline "Evals are the modern version of a PRD": encode "what good looks like" so a model can figure out the "how" (What you'll learn; chapter 23:06 "Demystifying evals").
- evals-autonomy-trust: a live demo builds a scoring function for documentation answers and lets an agent improve the prompt inside "a safe playground" (chapter 26:02); the alternative is "vibe checks and whack-a-mole" (chapter 30:20).
- tacit-knowledge-capture: "How Ankur turned his designer David's taste into a repeatable eval so quality scales beyond one person" (chapter 32:09, "Capturing designer taste in scoring functions").
- risk-sloped-review / human-review-gates: the "agent line" framework decides "which decisions, directions, and interactions you can hand off to an agent" (chapter 11:30). Content not available beyond the chapter title.

## Key points (from show notes only)
- Coding agents for deep infrastructure work: he uses Codex to run week-long benchmark experiments across database indexes, column-store formats and execution engines to speed up slow queries; "no excuse to skip rigorous benchmarking now that agents can run them tirelessly" (chapters 03:00, 06:10).
- Claims staff engineers are wrong about AI limitations; human attention decays on tedious work, which is where agents beat people in practice (chapter 09:03).
- Personal workflow: 4 to 6 concurrent agents; foreground agents, background agents and cloud environments (chapters 14:00, 17:16).
- Velocity: fixing CI is called "the highest-leverage way to speed up engineering velocity" for AI-accelerated teams (chapter 35:40).
- Audience is stated as senior and staff engineers, VPs of engineering and CTOs, not PMs.

## Could not verify
- No transcript was available; this note is from the episode's show notes and chapter list only. Nothing here was heard in the guest's own words beyond the show-notes paraphrase. The "agent line" framework, the eval demo, and how the designer's taste was encoded are known only by chapter title.
- Guest is CEO of an evals and observability vendor (customers listed in the notes include Notion, Stripe, Vercel and Zapier); "evals as PRD" is also his product's thesis.
- Relevance downgraded from the triage's "high" to medium because the substance could not be read.
