---
title: "Introducing Xirp"
source_url: https://portal.spotify.com/blog/introducing-xirp
author: Tyson Singer (Spotify)
publisher: Spotify Portal blog
published: 2026-08-10
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [harness-portability, agent-control-plane, compounding-context-repo, skills-marketplace, cost-control-routing, org-learning-loop]
relevance: high
---

## Relevance to the project
Xirp is Spotify's vendor-neutral environment for running many coding-agent sessions (Claude Code, Gemini CLI, Codex) in parallel worktrees, with context that moves between agents and comes from the Portal catalog. Its problem statement is ours: context fragmented into personal CLAUDE.md files, MCP setups and prompt libraries, so agents kept rediscovering what other sessions had solved, and leaders could not see activity across thousands of sessions. Session transcripts flow back into Portal, and a shared marketplace spreads skills, rules, plugins and MCP configs.

## Themes
- harness-portability: works across Claude Code, Gemini CLI, Codex; switch tool or model mid-task and keep working state; "vendor neutrality is an architectural requirement".
- agent-control-plane: visibility for leaders across thousands of concurrent sessions; 50+ parallel sessions per user.
- compounding-context-repo: sessions start with catalog context (architecture, dependencies, ownership, architectural decisions); transcripts and metadata flow back to Portal.
- skills-marketplace: shared marketplace for skills, rules, plugins and MCP configurations.
- cost-control-routing: route jobs to the best price-performance model, including self-hosted open-source models.
- org-learning-loop: framed as the same problem Backstage solved for services a decade ago.

## Key points
- Internal adoption: "thousands" of engineers, 36,000+ sessions (Spotify claim, Aug 2026; no time period). A trade report (runtimewire) gives 1,300+ engineers.
- Public beta 10 Aug 2026 at xirp.spotify.com, free, with a Portal instance for external users.
- Notes non-engineers began orchestrating agents in general, but does not say they use Xirp.

## Could not verify
- Relationship to Honk v2 / "Chirp" (named in the June 2026 post); engineer count differs between sources.
