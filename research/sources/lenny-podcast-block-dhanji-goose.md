---
title: "How Block is becoming the most AI-native enterprise in the world | Dhanji R. Prasanna (Lenny's Podcast)"
source_url: https://www.lennysnewsletter.com/p/how-block-is-becoming-the-most-ai-native
author: Lenny Rachitsky with Dhanji Prasanna (Block CTO)
publisher: Lenny's Podcast
published: 2025-10-26
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [non-engineer-builders, pm-job-stable-methods-change, leadership-permission-mandate, outcome-measurement-gap, pm-persona-role-expansion, harness-portability, human-judgment-pm-jobs, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
Block's CTO, in the fullest first-party account of how Block runs: a functional reorganisation (one head of engineering, one of design) that he credits with more productivity than any AI tool; Goose as the company-wide general agent whose value comes from MCP wrappers around internal systems; a self-reported 8-10 hours a week saved by AI-forward engineers and a modelled 20-25% of manual hours saved company-wide; and the claim that non-technical staff (legal, risk, operations) gain most. It bears on target-user, adoption, agent-unit and loop-source choices. It says almost nothing about product managers specifically, which is itself a finding.

## Themes
- non-engineer-builders: the biggest surprise is "the non-technical people using AI agents and programming tools to build things" (0:47, 48:56); the enterprise risk team built a self-service risk system, "compressing weeks of work into hours" instead of waiting for an internal apps team's roadmap (16:03).
- outcome-measurement-gap: 8-10 hours a week saved is self-reported by AI-forward engineering teams; check metrics (PRs, feature throughput) are combined by data scientists into "a complicated formula"; company-wide "trending towards 20 to 25% of manual hours saved", a figure across support, legal, risk and engineering (16:03, 20:43). No method published.
- leadership-permission-mandate: the change began with Dhanji's "AI manifesto" letter to Jack Dorsey (about 2023), arguing to do AI "centrally" (6:00); adoption is driven by leaders using the tools: Jack, the CTO and the executive team use Goose "every single day" (54:04).
- pm-job-stable-methods-change: the GM-to-functional reorg ("all engineers report into one single team now, all designers report into one single team") is credited over AI; Conway's law is the lesson (9:23, 12:13, 52:12, 1:00:13). Headcount planning changed because of the reorg, "nothing to do with AI" (44:34).
- pm-persona-role-expansion: "The lines are going to be blurred between whether you're in legal or in risk or in engineering and design" (48:56).
- harness-portability: Goose has a pluggable provider system (Claude, OpenAI, open models via Ollama) and engineers may use "any tools that they want"; Goose wins because it is "most well-integrated into all of our systems" via MCP (24:06, 25:40).
- human-judgment-pm-jobs: AI lacks "portfolio judgment"; the human asks whether the process or tool is needed at all (38:43); design leads push for "human taste to anchor these AIs" (37:56).
- evals-autonomy-trust: median Goose session about five minutes (mean seven); the next version aims for hours of unattended work, and overnight wishlists succeed on "60%" of well-described features (32:32, 36:59).

## Key points
- **Org model.** Block was run as a portfolio of companies (Square, Cash App, Afterpay, TIDAL) with GMs, separate engineering and design. It moved to a functional structure: single head of engineering, single head of design, shared levels, tools and policies, so people can move to areas of need (9:23-13:58). He says not everyone was on board; "quite a painful transformation" (12:13).
- **Early programmes.** Top-IC gatherings, eight or nine special projects of two to five engineers, and a reinstated company-wide hack week (7:53).
- **Company priority** named as "automate Block": AI automation through the entire company (16:03).
- **Goose described** as a general-purpose agent, desktop (Electron) app plus CLI, extended by MCP servers; example task: a marketing report pulling from Snowflake, Tableau and Looker, analysed in Python, charted, written to a Google Doc or PDF and emailed (21:49-25:31). "Goose can write its own MCPs" (25:40). He positions it between a general assistant and Cursor or Claude Code (58:43).
- **Background agents** run 24/7 or in CI, analysing vulnerabilities and drafting patches from filed bug tickets overnight (14:12). Gosling (Goose for Android) automates UI tests that once needed contractors (16:03). A test-selection tool cut test runs by about 50% (52:21).
- **Where AI works:** greenfield code and new platforms see "pretty aggressive gains"; large legacy codebases do not yet (20:52). Senior architecture work is where AI "still underperforms humans" (16:03).
- **Ambient experiment:** one Goose-team engineer runs Goose watching his screen and listening; it opened a PR for a feature discussed in Slack hours earlier and reschedules meetings. Labelled "mostly an experiment" (28:50-31:58).
- **Build many, discard most:** describe several experiments in detail, let agents build overnight, throw away five or six; "what would our world look like if every single release... deleted the entire app and rebuilt it" (32:32-36:09). The trick is to keep past incremental fixes "as a part of the specification".
- **Build vs buy restraint:** building replacements for vendor tools is "probably not worth it" against Block's core purpose, economic empowerment (40:31).
- **Hiring:** looking for a "learning mindset", not AI expertise; interviews starting to allow vibe-coding (44:34-48:37).
- **Open source rationale:** Goose given away because Block wants things that "outlast Block"; competitors and partners use it, Databricks named (26:51-28:18).
- **Product managers are not discussed.** The word "PM" never appears in the conversation; "product people" appears once, in Lenny's question about hiring (51:22). Design is mentioned as the human-taste anchor.

## Notable quotes
- "we went from a GM structure to a functional org structure, which was I think the key to making our transformation" (7:53)
- "we're probably trending towards 20 to 25% of manual hours saved" (16:03)
- "structure matters more than the efficacy of the tools you have" (52:21)

## Could not verify
- No method behind the 8-10 hours (self-reported) or the 20-25% composite; no baseline or period.
- The CTO intro says he oversees "over 3,500 people"; the show notes say "more than 4,000 engineers": figures differ within the page.
- An earlier pass (2026-10-24, research-pm-agents-jobs-to-be-done) read only the paywalled page's chapter list; this rewrite (2026-10-24, research-block-product-practices) is from the full transcript read through a paid subscription. Transcript is auto-generated ("games" = gains).
