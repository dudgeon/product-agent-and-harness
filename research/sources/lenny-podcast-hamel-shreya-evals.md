---
title: "Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar (creators of the #1 eval course)"
source_url: https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill
author: Lenny Rachitsky (host), Hamel Husain and Shreya Shankar (eval course creators)
publisher: Lenny's Podcast
published: 2025-09-25
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, spec-becomes-prototype-and-evals, human-review-gates, human-judgment-pm-jobs, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
The podcast version of the method already filed from their guest post (lenny-newsletter-evals-hamel-shreya): error analysis on real traces by one domain expert, axial coding, counting, binary LLM judges validated against human labels. What the episode adds for the project is the explicit "evals are the new PRDs" exchange and its limit: Shankar says the judge prompt encodes the PM's expectations but those expectations only appear after looking at outputs, so PRDs remain but "it's going to change". It also argues coding agents are a misleading template for other AI products because the developer is the domain expert and dogfoods all day, which bears on whether PM agents can borrow coding-agent eval practice (pm-agent-evaluation, intent-shaping-and-spec).

## Themes
- spec-becomes-prototype-and-evals: Lenny: the judge prompt "is the purest sense of what a product requirements document should be ... automatic and running constantly" (1:00:56); Shankar: people "put in what their expectations are before looking at their data", but reviewing data uncovers more; "PRDs are a great abstraction ... It's not the end all, be all" (1:01:45-1:02:28).
- evals-autonomy-trust: criteria drift from Shankar's "Who Validates the Validators?" study: experts "can't figure out your rubrics upfront"; opinions of good and bad change after seeing outputs (1:03:35); people "anti evals" were often burned by Likert-scale judges that didn't match expectations (1:10:19).
- human-review-gates: open coding is not a job for an LLM yet: "in this stage of free form, note-taking is not the place for an LLM" (24:58); LLMs can help cluster notes into axial codes, but proposing fixes is the human's job (35:53).
- human-judgment-pm-jobs: the "benevolent dictator" for error analysis is the domain expert (a lawyer for legal, a clinician for mental health), "though oftentimes, it is the product manager" (27:16-27:42).
- outcome-measurement-gap: when someone reports judge "agreement", ask for the confusion matrix (59:18); evals cover online monitoring of product metrics too, not only unit tests (1:10:19).

## Key points
- Coding agents are a special case: "the developer is the domain expert", dogfooding is constant, so the eval process can collapse; generalizing from Claude Code's "we just vibe" stance to other AI products is "a mistake" (1:13:53-1:14:35). Shankar adds that domains like medicine lack that dogfooding (1:14:51).
- Claude Code "vibes" debate: Shankar argues it stands on model-level coding benchmarks and implicit error analysis through dogfooding (1:11:49-1:13:53).
- Effort: 3-4 days up front, then about 30 minutes a week, with a cron job sampling traces (1:30:45); most products need 4-7 judges (show notes takeaways).
- Evals vs A/B tests is a false choice; teams run premature A/B tests on hypothesized problems without error analysis (1:17:27).
- Show notes include their open-codes-to-axial-codes prompt for a CSV of trace notes.

## Notable quotes
- "You don't really know what you want until you see it with these LLMs." (Shankar, 1:02:28)
- "Coding agents are fundamentally very different than other AI products, because the developer is the domain expert." (Husain, 1:13:53)

## Could not verify
- Show notes and takeaways read in full; transcript read by search: 0:00-1:09, 24:55-27:44, 59:18-1:05:23, 1:09:57-1:18:34, 1:30:45-1:31:41. The live walk-through of trace review and judge building (roughly 6:00-59:00) was skimmed; its method is covered in the guest-post note.
- The authors sell the leading course on this method; claims about time and number of evals are their experience, not measured.
