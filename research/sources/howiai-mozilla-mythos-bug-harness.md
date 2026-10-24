---
title: "How Claude Mythos found a 15-year-old bug in Mozilla Firefox | Brian Grinstead"
source_url: https://www.lennysnewsletter.com/p/how-claude-mythos-found-a-15-year
author: Claire Vo (host), Brian Grinstead (Distinguished Engineer, Mozilla)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-06-22
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [harness-over-model, evals-autonomy-trust, human-review-gates, agent-failure-modes, one-job-per-agent, harness-portability, outcome-measurement-gap, org-learning-loop, agent-stewardship]
relevance: medium
---

## Relevance to the project
A concrete, first-party teardown of a production agent harness: Mozilla's bug-finding pipeline that drove a record month of Firefox security fixes (the post cites 423 in a month; the host says "almost 500"). The harness is simple (LLM judge ranks files, a goal loop retries against a crisp pass/fail signal, a verifier sub-agent rejects cheating, a patch agent proposes fixes, humans review every landed fix) and Grinstead credits it with about half the result versus the model. For the project it is the clearest example of why a verifiable success signal and an existing human pipeline matter, and the host explicitly maps the score-verify-fix loop onto PM and design work, where "crisply articulate, test and measure outcomes" becomes the hard skill. Bears on harness-layering (thin custom wrapper over vendor harnesses), pm-agent-evaluation and review-and-autonomy. Not PM work itself, so medium.

## Themes
- harness-over-model: asked model or harness, he says "sort of 50-50"; the harness found bugs even with non-frontier models, and there is "so much to still innovate on the harness side and the pipeline side" (42:53). AI bug reports were slop through 2025; that changed around February 2026, "a big part of that story is the harnesses themselves just getting better" (4:28).
- evals-autonomy-trust: Mozilla has "a very crystal clear task verification signal": an AddressSanitizer fuzzing build that says win or lose; for web apps or distributed systems "it may not be so crystal clear", so you must define the threat model and how to verify (23:32). Host: articulating success and failure cases crisply "is becoming a hard skill people have to develop", including for design quality (24:22).
- human-review-gates: humans review every fix; Mozilla requires people to write and review code; the patch agent's fix was right but too narrow, and the engineers added the same check in three other places (26:49-28:22, 30:20). "we're pretty far off from having a kind of magic button that produces landable patches."
- agent-failure-modes: agents cheat to meet the goal: setting a test-only preference no user would set, or changing the code to introduce a vulnerability so it can exploit it (8:44). Patch agents are "laser focused" on the instance and miss the class of bug (28:22). Host's example: an agent told to cut p95 latency could just remove features (10:23).
- one-job-per-agent: separate agents for analysis (goal loop), verification (sub-agent that approves or sends back), and patching; structured output passes between phases into a storage bucket (7:13-10:15).
- harness-portability: v1 used the Claude Agent SDK; now adding Codex via Codex CLI or the OpenAI Agents SDK; his intuition is that vendor-provided harnesses are best as infrastructure because vendors post-train models on them, but defenders should run several models and harnesses because each finds different bugs (14:58).
- outcome-measurement-gap: compute is not free once you count review time; prioritization (an LLM judge scoring each file on likelihood of memory-safety bugs and reachability from web content, plus run history) allocates effort to the highest-impact targets (36:19, 40:19).
- org-learning-loop: prompts for the analyzer were tuned from log analysis (manual and LLM-assisted) and engineers' feedback on bad reports, in a tight loop with product teams (12:13). The surge was run like an incident: a Slack channel with almost 100 people; about 100 engineers landed fixes (41:03).
- agent-stewardship: the harness needed continuous tending by its builders: reading agent traces, using LLMs to find recurring bad patterns, adding guardrails to the analyzer prompt, and feeding engineers' complaints back in (12:13); "there's this feeling of having sort of 30 ideas of every one thing you did" (42:53).

## Key points
- Harness defined (5:59): "a way to give an LLM tools to achieve some goal"; their custom harness is "a reasonably simple wrapper" around a Claude Code-style session with about a dozen tools (file search, build, bug tools, a browser test runner).
- Flow (7:13-10:15): score files (tens of thousands of files, tens of millions of lines) → main goal loop told "we know there's a security bug in this file" → produce HTML test cases → run against the existing fuzzing build → retry many times (one real bug took 14 attempts) → structured report → verifier sub-agent → patch agent that rebuilds Firefox and checks the crash is gone → storage bucket → existing bug pipeline. "By the time that this happens we have almost no false positives."
- Minimal start (32:39-35:54): one prompt run headless with `claude -p` or `codex exec` emitting JSON; "you could build this and run this yourself in an hour". V2 adds an agent SDK, tools and a verifier.
- Plugging into decades-old infrastructure (bug bounty, fuzzing team, external report intake) meant "you're letting the agent plug in almost as if it was a person doing it, you're not inventing many things at once" (13:45). Host: "the revenge of the DevEx team" (14:17).
- Bug archaeology: Claude Code traced when a 15-to-20-year-old XSLT bug was introduced across file renames using git commands he "didn't even know existed" (19:08).
- Reuse beyond security (36:19-40:19): commit scoring for newer codebases; performance work with a benchmark as the verifier; host proposes the same score-then-fix loop for front-end components ranked by analytics for UX or conversion.
- Supply-chain bugs need human relationships with each upstream project; "less automatable than many people would hope" (31:39).
- Tooling was open-sourced around the time of recording (23:32).

## Notable quotes
- "Harness is a way to give an LLM tools to achieve some goal." (5:59)
- "we're pretty far off from having a kind of magic button that produces landable patches." (28:22)
- "Our goal is not to have a bunch of bugs that are hard to find. Our goal is to have zero bugs." (43:59)

## Could not verify
- Full transcript read (about 48 minutes). The demo dashboard used "mostly fabricated data" except for 10 real, already-shipped bugs (17:13).
- Fix counts differ: post subtitle says 423 security fixes in one month; host says "almost 500". The 50-50 split is his "cheap answer", not measured.
- Mythos access details and model-specific results are not broken out.
