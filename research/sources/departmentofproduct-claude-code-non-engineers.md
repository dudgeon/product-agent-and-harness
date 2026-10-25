---
title: How to use Claude Code for non-engineering use cases
source_url: https://departmentofproduct.substack.com/p/how-to-use-claude-code-for-non-engineering
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-12-05
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [non-engineer-builders, prd-agents, compounding-context-repo, single-agent-many-skills, pm-tool-connectivity]
relevance: medium
---

## Relevance to the project
A beginner's tutorial (December 2025) teaching PMs to use Claude Code as a general work harness: install it, use an IDE as the file UI, create PRD-writer and Jira-ticket-writer subagents from community templates, run SEO audits through Playwright MCP, reorganise local files, keep a "second brain" folder, and build a small app in plan mode. It is evidence of the "use a vendor harness as is" path as PMs actually meet it: the harness is borrowed and the PM's own layer is a folder of markdown agents and frameworks. The most project-relevant pointer is a practitioner's open "Claude Code Product OS" repo (frameworks, strategy templates, stakeholder profiles). Triage guessed high; it is a how-to with no adoption or outcome data, so medium. Anthropic's own claims are second-hand from its "how teams use Claude Code" post.

## Themes
- non-engineer-builders: written for readers with "zero prior experience", treating the terminal plus an IDE (Cursor) as the UI for non-code work; opens with Anthropic's report of non-engineering teams using Claude Code (intro, setup). Primary: [How Anthropic teams use Claude Code](anthropic-how-teams-use-claude-code.md).
- prd-agents: PRD-writer and Jira-ticket-writer subagents created with `/agent` from public GitHub templates; a one-line request (change a button colour) produces a full story with acceptance criteria and definition of done, which the author concedes is far too much for the change (section "Create your own PRD and Jira ticket writing agents").
- compounding-context-repo: a PM's shared "Claude Code Product OS" repo bundles JTBD, opportunity solution trees, strategy and competitive frameworks, stakeholder profiles and decision tools for Claude Code to reference, shared with his team (same section).
- single-agent-many-skills: subagents explained as preconfigured helpers with their own context window, allowed tools and system prompt, invoked by name from the main session.
- pm-tool-connectivity: notes that MCP setup was harder in Claude Code than in Claude Desktop at the time (second-brain section); uses Playwright MCP for browser work.

## Key points
- **Setup:** native installer, login with a Claude subscription, optional Cursor extension so the file tree acts as the UI.
- **Use cases:** PRD and ticket agents; SEO audit of a live page via Playwright MCP, and a linked example of keyword research to landing pages; bulk file moves and CSV edits in natural language; a weekly "brain dump analysis" command that clusters notes into themes; a to-do app built with plan mode (shift-tab twice) for review before edits.
- **Framing:** "treat Claude Code as a thought partner rather than a code generator", quoted from Anthropic.
- Ends with a gallery image of other teams' MCP and Claude Code uses (not available in text).

## Could not verify
- The Product OS and agent-template repos were not opened; their contents are as described in the post.
- Some details (slash command names, MCP difficulty) were true at December 2025 and may have changed.
- Retrieved through a paid subscription; summarised, not reproduced.
