---
title: How We Red-Teamed Our Own AI Agent
source_url: https://engineering.block.xyz/blog/how-we-red-teamed-our-own-ai-agent-
author: Josiah Peedikayil and Wes Ring (Block Offensive Security), with contributors
publisher: Block Engineering Blog
published: 2026-01-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-protocol-security, skill-supply-chain-security, enterprise-admin-controls, agent-failure-modes]
relevance: high
---

## Relevance to the project
"Operation Pale Fire" is Block's internal red-team exercise against goose as deployed to employees. It is the best first-party evidence of how a shareable task package (a goose recipe) and a connected tool (Google Calendar MCP) become attack paths for a company-wide agent, and of which fixes were shipped upstream. Directly relevant to any project design where PMs share skills or recipes with each other.

## Themes
- agent-protocol-security: a prompt injection hidden in a calendar invite description, encoded in zero-width Unicode, told goose to call a command-and-control server through the developer shell tool (attack vectors).
- skill-supply-chain-security: shareable recipes were base64 blobs in URLs whose content was appended to the system prompt "with little transparency"; a poisoned recipe was the successful vector. Fix: goose now shows recipe instructions on load (PR 3537) (fixes).
- enterprise-admin-controls: Google Calendar policy changed so external invites only reach primary calendars from known senders; DART added agent-to-host telemetry and AI paths in runbooks (detection and response).
- agent-failure-modes: the third campaign worked by social engineering: a fake right-to-left text bug report in public goose channels; a goose developer ran the poisoned recipe while debugging and launched a simulated infostealer (results).

## Key points
- Campaign 1 (calendar invites, ~5 days) failed: Google Calendar API rate limits (~50 invites/day), model and MCP variability, and an MCP update broke the payload. Campaign 2 (recipes via Meet links) failed on a typo. Campaign 3 succeeded and was detected by DART.
- Fixes shipped in goose: zero-width character stripping (PRs 4080, 4047), recipe transparency (3537), first prompt-injection detection (4237).
- Internal users "can choose from many models across several vendors"; context windows vary with enabled tools.
- Recommendations: treat AI output like user input, enforce authorization outside the AI, sanitise all inputs including calendar entries, behavioural monitoring, regular AI red teams.

## Notable quotes
- "goose along with the other LLM coding tools can not effectively isolate untrusted context." (Conclusion)

## Could not verify
- No count of internal goose users or how many employees received the test payloads.
