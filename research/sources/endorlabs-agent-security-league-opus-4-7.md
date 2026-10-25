---
title: Claude Opus 4.7 sets new records in the Endor Labs Agent Security League
source_url: https://endorlabs.com/learn/claude-opus-4-7-sets-new-records-in-the-endor-labs-agent-security-league
author: Robert Haynes (Endor Labs)
publisher: endorlabs.com
published: 2026-04-17
retrieved: 2026-10-24
type: report
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-over-model, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A rare third-party benchmark that holds the model fixed and varies the harness (Cursor vs Claude Code vs Codex vs SWE-Agent) on functional correctness and security of generated code, built on CMU's SusVibes. Endor Labs sells code-security tooling but is not a harness vendor. Relevant to the project's view that harness quality matters: the same model scored differently by harness, though the author attributes small gaps to non-determinism. Coding only.

## Themes
- harness-over-model: Opus 4.7 in Cursor 91.1% functional / 22.9% secure vs Claude Code 87.2% / 20.1%; Opus 4.6 in Cursor 84.4/7.8 vs Claude Code 81.0/8.4 (harness order flips on security); Gemini 3 Pro in Claude Code 41.9/8.4 vs Cursor 31.8/7.3.
- vendor-claims-vs-independent-evidence: author does not claim a harness effect: a "hypothesis we will continue to test"; possible ~10% relative difference.

## Key points
- 15 harness-model combinations, Feb to Apr 2026; task count not stated in the post (whitepaper referenced).
- Even the best scores leave about four in five solutions with vulnerabilities.
- No OpenCode, Goose, Cline or Amp entries.
- Secondary coverage (MindStudio) reports GPT-5.5 at 61.5% functional in Codex vs 87.2% in Cursor; not in this post; unverified.

## Could not verify
- Methodology details and sample sizes (whitepaper not read).
