---
title: What Claude Code, Cursor, OpenAI and Copilot log, and what nobody logs
source_url: https://www.senseon.io/blog/what-claude-code-cursor-mcp-log
author: SenseOn Research Team
publisher: SenseOn blog
published: 2026-08-31
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A security vendor's survey of what each AI tool's logs contain. Its point fits the regulated-audit requirement: every vendor logs its own side, content capture is off by default and enabled source by source, and no log shows one identity's activity across tools. SenseOn sells a correlation platform, so the "missing correlation layer" conclusion is in its interest; the per-vendor facts align with the first-party pages read in this round.

## Themes
- enterprise-admin-controls (proposed): OpenAI's Compliance Logs Platform covers ChatGPT Enterprise/Edu and is "retained for 30 days unless copied out"; the API Platform audit log records configuration changes, not prompt content; Claude Code OTel export is off by default for prompts and tool details; Cursor's enterprise audit log excludes prompt/response content.
- vendor-claims-vs-independent-evidence: "None of these logs was built to answer a security team's question." "What is missing is a place built to receive all of it and correlate across sources."

## Key points
- MCP defines a logging mechanism but does not require any call log; each server decides.
- Microsoft 365 Copilot `CopilotInteraction` records hold who/when/resources, with full text on a separate Purview surface. GitHub Copilot's own products are not covered.

## Could not verify
- Not independently reproduced; model-summarised fetch. The 30-day OpenAI retention matches the help-center statement seen in search (the help page returned 403).
