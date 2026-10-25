---
title: How to build a Self-improving Product
source_url: https://departmentofproduct.substack.com/p/how-to-build-a-self-improving-product-2e5
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-06-22
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [metrics-review-agents, feedback-triage-agents, opportunity-to-code-chain, evals-autonomy-trust, outcome-measurement-gap, memory-architecture, human-judgment-pm-jobs, product-coherence-over-automation, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The clearest end-to-end PM agent loop in this publication: sense (analytics, support, errors), decide (a quality judge plus a spec agent that checks the codebase), act (route by complexity to a coding agent or a ticket), learn (measure outcomes, update per-area memory), built as markdown agent files in a Claude Code repo and run on a schedule. Its case is Amplitude's Wave, and the most useful numbers are Amplitude's own: about 11% of suggested fixes ship end to end against a roughly 50% "would do" rate. The Amplitude facts are second-hand from Amplitude's write-up; the build is the author's own tutorial on a mock product. It bears directly on pm-job-sequencing (metrics review and feedback triage feeding specs), review-and-autonomy (start with only small code fixes autonomous, raise the threshold later) and pm-agent-evaluation (ship rate vs would-do rate as a measure).

## Themes
- metrics-review-agents: the "sense" agent reads one product-area file, queries analytics (Mixpanel in the example) for drop-offs and below-target metrics over 14 days, and returns cited candidate problems (step 3).
- feedback-triage-agents: the same sense agent groups 30 days of Zendesk tickets by theme and checks GitHub issues for the area; a corroboration rule keeps only problems seen in two or more independent sources (step 3).
- opportunity-to-code-chain: a full chain from signal to opportunity to spec (acceptance criteria, files to change, complexity tag) to routed execution (Claude Code for small code fixes; Linear for medium and large; experiment and research paths) to a review agent that checks the PR against the spec (steps 4-5).
- evals-autonomy-trust: Amplitude's judge scores each opportunity with a rubric and feeds a classifier that predicts whether a human would thumbs-up it; the tutorial's router starts with only Small+Code autonomous and says to raise the threshold "gradually as you build trust" (Amplitude section, step 5).
- outcome-measurement-gap: Amplitude reports an end-to-end ship rate in its own codebase around 11% (the post also says "low single digits"), against about 50% "would do"; a Learn stage logs outcomes per shipped change (Amplitude section, step 6).
- memory-architecture: a reflection agent rewrites one markdown memory file per product area each cycle: what worked, what didn't, what the team keeps rejecting, standing context for the next run (step 6).
- human-judgment-pm-jobs: "AI led vs AI informed": the author argues human judgement should keep the final say, by analogy with data-led vs data-informed teams (section "AI led vs AI informed").
- product-coherence-over-automation: warns that metric-chasing agents could ship wins that damage the overall experience (Netflix autoplay analogy) and closes on the risk of "AI optimized product slop".
- vendor-claims-vs-independent-evidence: Wave is in closed beta; all its facts are Amplitude's own, though the low ship rate is an unusually candid vendor number.

## Key points
- **Concept:** credited to a talk by YC partner Tom Blomfield and to Amplitude Wave, which Amplitude markets as enabling "self improving products". The author notes this reaches into the decision layer people assumed would stay human.
- **Five parts:** product map (areas, journeys, events, pages, success metrics with targets) → sense → decide → act → learn.
- **Amplitude Wave (second-hand):** a network of agents maps the product, sends scoped agent swarms to the weakest areas, scores candidates with an LLM judge plus classifier, scans the codebase via GitHub before writing a spec (Amplitude's biggest quality gain, because the commonest rejection was proposing something that already exists), tags each spec with execution method, autonomy level, size and location, routes self-contained fixes to a Cursor agent and the rest to humans, and distils decisions into per-area memories. Ran internally for months before the beta. Amplitude's earlier agents launch is filed as [Amplitude AI agents launch](amplitude-ai-agents-launch.md); Wave itself is not filed.
- **The tutorial build:** a repo with `/product-areas/` (one file per area), `/agents/` (sense, judge, spec, router, review, reflect, plus a run-loop orchestrator), `/opportunities/`, `/outcomes/log.csv` and `/memory/`. Data connected through MCP. The judge uses a fixed list of rejection reasons (for example insufficient evidence, inaccurate citation, already shipped, already in backlog, not a coding task) and logs every rejection. The review agent passes a PR to a human only if every acceptance criterion is met and the analytics events needed to measure it are present.
- **Running it:** demo on a mock prompt-library product wired to Google Analytics, GitHub and Linear; it found a broken copy button, judged it a small fix and recorded it in memory. Scheduled with Claude's `/loop` command.
- **Author's caveat:** a lightweight version will likely ship even less than Amplitude's 11%.

## Notable quotes
- "Raise this threshold gradually as you build trust in the system." (router rules, step 5)
- "we don't end up with a web full of AI optimized product slop" (close)

## Could not verify
- Amplitude's Wave write-up and Tom Blomfield's talk are cited but not filed or read here; the 11% and ~50% figures are as the post reports them.
- The downloadable agent files and the demo video were not retrieved.
- Retrieved through a paid subscription; agent templates are described, not reproduced.
