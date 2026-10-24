---
title: "I gave Claude Code our entire codebase. Our customers noticed. | Al Chen (Galileo) (How I AI)"
source_url: https://www.lennysnewsletter.com/p/i-gave-claude-code-our-entire-codebase
author: Claire Vo (host), Al Chen (field engineer, Galileo)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-04-06
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [org-context-grounding, compounding-context-repo, tacit-knowledge-capture, non-engineer-builders, ai-synthesis-hallucination-risk, org-learning-loop, feedback-triage-agents]
relevance: medium
---

## Relevance to the project
A non-engineer in a customer-facing role uses Claude Code over all 15 of his company's repos, plus Confluence and Slack via MCP, as the source of truth for deep technical answers, and keeps a "customer quirks" Confluence page that tailors every answer to one customer's air-gapped, security-constrained environment. It shows code as current context that beats docs, a lightweight per-customer knowledge file that compounds, and the limit: decisions that live only in meetings and hallway talk are not queryable. It bears on context-and-memory (where product context lives; code as source of truth) and on the "make context legible" thread. It is one person's workflow.

## Themes
- org-context-grounding: 15 repos (one per service) opened at the parent level in VS Code so Claude Code can traverse them; questions not answerable from public docs answered from code (4:23-6:37); "the main branch is always the source of truth" (Claire, 8:17).
- compounding-context-repo: a 16-line script (written by Claude Code) pulls main for every repo daily (8:32-9:37); Slack threads turned into help articles via Pylon and auto-published to a public knowledge base that is "way more up-to-date compared to our docs" because docs need a PR (26:33-29:18).
- tacit-knowledge-capture: the "customer quirks" Confluence page, one heading per enterprise customer with bullets on secrets storage, namespaces, sidecars, encryption; the `/dpl` custom command reads Confluence deployment pages first, then the quirks page, then the repos (11:47-14:50).
- ai-synthesis-hallucination-risk: he proofreads, cuts AI verbosity, demands line-level citations ("don't make anything up, always cite your sources"), and still checks with engineers; Claude Code is sometimes wrong because a planned refactor lives "in like a meeting note somewhere or ... hallway conversations" (20:31-22:45).
- non-engineer-builders: never held an engineering role; engineering interruptions reduced "almost down to zero" (6:37); suggests raising the technical bar for customer-facing hires (37:07).
- org-learning-loop: spreads the setup by showing results to teammates, not by mandate (32:32).
- feedback-triage-agents: clustering customer questions into themes that feed the roadmap, formerly manual in Intercom and spreadsheets (31:04).

## Key points
- Claire: "You have to be less precious about where and how you store the information" because AI traverses it (15:01); Al: "throw it into Confluence, throw it into Notion, throw it into Slack" (16:26). (A counterpoint to curated-context arguments; and in tension with his own point that unrecorded decisions are invisible.)
- Thought experiment: letting customers query a sanitized copy of the code directly; LangChain's open-source repos allow this today (18:22-19:54).
- The "and then" workflow-discovery prompt: for each step, ask what an infinitely staffed team would do next (Claire, 29:18).
- Prompting: "think hard, think harder", ask why the answer is right and for sources (42:19).

## Could not verify
- Transcript read in full (sponsor reads skipped). "Near-zero" interruptions and customer reactions are self-reported.
