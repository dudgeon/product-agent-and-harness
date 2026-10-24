---
title: "How to do AI analysis you can actually trust"
source_url: https://www.lennysnewsletter.com/p/how-to-do-ai-analysis-you-can-actually
author: Caitlin Sullivan (guest author), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-02-17
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [ai-synthesis-hallucination-risk, research-synthesis-agents, feedback-triage-agents, org-context-grounding, human-review-gates, agent-failure-modes]
relevance: high
---

## Relevance to the project
A practitioner's catalogue of how LLM synthesis of customer research goes wrong (invented and stitched quotes, generic themes, counts that do not decide anything, buried contradictions) with a concrete fix for each. For a PM harness this reads as a design spec for a research-synthesis job: structured context loading, a calibrated scale per decision, and a mandatory verification pass before output reaches a deck. It bears on review-and-autonomy (what verification is built in), context-and-memory (what context a synthesis agent needs), and pm-agent-evaluation (quote verification is a cheap, checkable eval). Evidence is one consultant's testing, not a controlled study, and she sells a course on the method.

## Themes
- ai-synthesis-hallucination-risk: two hallucination types seen "all the time": fully invented quotes (all three major models) and "Frankenstein" quotes stitched from several places (especially ChatGPT); prompts with word limits such as "punchy ... quote (≤12 words)" reliably trigger mash-ups; participant IDs and timestamps can be faked too (section "Failure mode #1"). In her verification run, most quotes in a ChatGPT output were paraphrases, not verbatim.
- research-synthesis-agents: a four-step method for synthesis: quote rules, context loading, few-shot calibration, verification pass ("Try this with your latest analysis"). She says she has built agents that interpret data "the way a senior researcher would, but in near real time as data comes in" (Failure mode #3), a claim not demonstrated in the post.
- feedback-triage-agents: survey and churn-feedback specifics: tell the model which CSV columns are customer voice versus internal metadata (she has seen AI treat an internal "flagged for follow-up" note as a customer statement); explain scale coding; one answer like "It's not for me" can carry four different product implications ("Why AI struggles with customer research data", "Failure mode #2").
- org-context-grounding: generic insights come from missing context; effective context has four parts: project context (the specific decision), business goal, product context, participant overview. More context is not better; unstructured "four paragraphs" dictated at lunch do not help (Failure mode #2 fix).
- human-review-gates: "The first pass is always a hypothesis"; every analysis needs a verification pass checking quotes, per-participant contradictions (stated preference vs described behaviour, confidence then hedging), and thin-evidence findings (Failure mode #4).
- agent-failure-modes: the core failure is invisible confidence: output "always looks confident" and nothing signals "check me again"; most teams have one enterprise LLM and never see what it misses by comparison ("What each LLM is best used for").

## Key points
- Model comparison (her testing, "over 100 times", plus prompt testing with Maze): Claude gives the most depth and quotes but does not filter (validated patterns and half-formed hypotheses on equal footing); Gemini/NotebookLM gives fewer, better-grounded themes, needs longer-quote prompting, and can analyse non-verbal behaviour in video; ChatGPT is best for stakeholder framing but least reliable for real evidence because it combines quotes. Her recommendation: Claude for analysis.
- Quote selection rules (Failure mode #1): start where the thought begins, keep reasoning, hedges and emotion, cite participant and approximate timestamp, never combine statements, split quotes over three sentences. Then a verification prompt that labels each quote VERIFIED / PARAPHRASE / NOT FOUND with actual wording and location. Adds about five minutes.
- Why: LLMs generate likely-looking text rather than retrieve; "verbatim" is ambiguous to a model.
- Generic themes (Failure mode #2): models default to consensus and to training priors (for example, price as the top churn theme); a few people's edge case or the gap between stated want and behaviour may matter more. Mentioning "pricing issues" in a prompt inflates pricing-coded responses.
- Counts are not decisions (Failure mode #3): "22 respondents mentioned a screen" says nothing about who would be retained. Fix: a decision-specific scale with an example and a rationale for each level (her five-level "solution fit" scale for a Whoop screen decision: screen would retain, cheaper fix would retain, engagement fix, operational fix, unrelated competitive loss). With context loaded, her example tally said 30% would be retained by a screen. The examples use fictional Whoop data.
- Verification pass (Failure mode #4): a self-audit prompt for quotes, contradictions and confidence; "When you push any LLM to review its own labeling and interpretation, it actually will find errors."
- Framing: "Fifteen minutes of verification now or six months of building the wrong thing later".

## Notable quotes
- "Generation and retrieval are fundamentally different." (Failure mode #1)
- "The first pass is always a hypothesis." (Failure mode #4)
- "Nothing in the output signals 'check me again.'" (closing)

## Could not verify
- Read in full (paid text via Geoff's session). Screenshots of model outputs referenced in the post were not available in the text; claims about what they show are the author's.
- "2,000 hours of testing" and "over 100 times" are her own figures, method not stated; data is fictional (Whoop), not a real study.
- Author sells a course ("Claude Code for Customer Insights"), so this is partly promotional.
- The self-verification approach relies on the same model checking itself; the post does not test how often the verifier misses errors.
