---
title: "How Warp builds self-improving agents on Claude"
source_url: https://claude.com/resources/articles/how-warp-builds-self-improving-agents-on-claude
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-08-26
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [org-learning-loop, skill-standards, feedback-triage-agents, human-review-gates, memory-architecture]
relevance: medium
---

## Relevance to the project
Warp's pattern is a concrete, reusable mechanism for agents that learn from their reviewers: a base skill does the job, people leave feedback where they already work, and a scheduled improver agent proposes a small edit to the base skill as a PR that a human merges. That is a governable form of the org-learning loop (changes are diffs, reviewed, versioned) and a clean answer to the skills-vs-memory question for harness upkeep. Warp runs it on spec-writing, review and triage agents in its open-source repo. Evidence is a customer story with no before/after quality metrics; growth figures are Warp's own.

## Themes
- org-learning-loop: feedback "typically disappears when the session ends"; the improver skill turns accumulated human feedback into skill edits so "the next run of the inner skill inherits the improvement" (section "Agent self-improvement loops built on skills").
- skill-standards: skills as plain files with progressive disclosure and bundled scripts; tips: principles not rules, explain the why, keep skills small (section "How to write self-improving skills").
- feedback-triage-agents: issue-triage agent fired by a GitHub Action labels issues, assesses complexity and suggests a fix direction; maintainer feedback on a missed "ready to spec" label became a skill PR (section "The loop in action").
- human-review-gates: improver output goes through normal code review; "That final human step closes the loop and keeps a person in control of what actually changes."
- memory-architecture: sidebar distinguishes skills (procedural, stable, changed deliberately) from memory (auto-written at inference time, always changing).

## Key points
- Problem: Warp's internal code-review agent produced noisy, low-quality comments; hand-rewriting prompts and improving AGENTS.md helped but did not scale.
- Architecture: two skills with human feedback between them. Inner/base skill = domain knowledge for the task. Outer/improver skill = observer agent on a schedule (not per task) that compares agent suggestions with human responses and proposes "a small, focused edit".
- Triage walk-through: improver runs in Oz (Warp's orchestration platform) as a scheduled "update triage" agent; authenticates to GitHub, runs a bundled Python script to pull issues with feedback into JSON, finds signals, opens a PR with a description of which signals prompted the change.
- Feedback design: capture it where work happens (PR or issue comments), no extra submission step; detailed domain feedback from a senior engineer beats many thumbs; explanation of why is what makes it usable.
- Improver skills are said to be largely reusable across agents; suggested middle path: a templated base loop with domain-specific layers ("A handful of improvers can each own one; a hundred should share").
- Wrong feedback: assume it happens; let the agent sanity-check, filter whose input counts, and keep a human at filtering or final review.
- Verifiable domains: build the verification harness first; otherwise deterministic evals against golden outputs and feedback restricted to domain experts.
- System-level measure suggested: time to merge, contributor count, cost, fed back to improvers; deploy crawl-walk-run.
- Warp's stated scale (its claims): 800K monthly developers, 56% of the Fortune 500, 10M Claude Code sessions run inside Warp, thousands of code reviews with hundreds of contributors on the open-source repo.
- Limits: no measured improvement in review quality or triage accuracy is given; one worked example.

## Notable quotes
- "If you make it too hard you're not going to get the feedback and you're not going to be able to improve the skill." (Zach Lloyd, CEO, Warp)

## Could not verify
- The linked webinar was not watched.
