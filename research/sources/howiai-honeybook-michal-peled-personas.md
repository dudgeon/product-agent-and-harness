---
title: "ChatGPT agent mode: The \"little helper\" that transformed recruiting, crafted user personas, and solved parking nightmares | Michal Peled (HoneyBook)"
source_url: https://www.lennysnewsletter.com/p/chatgpt-agent-mode-the-little-helper
author: Claire Vo (host), Michal Peled (Technical Operations Engineer, HoneyBook)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-12-08
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [synthetic-users-limits, research-synthesis-agents, ai-synthesis-hallucination-risk]
relevance: low
---

## Relevance to the project
A first-party example of turning a large, expensive persona study ("hundreds of pages" from interviews with hundreds of small-business owners) into five custom-GPT personas that colleagues "talk to". NotebookLM is used as a source-restricted, cited step to draft each persona prompt. It bears on discovery and research synthesis, and on the limits of synthetic users. No validation of persona answers against real customers is shown.

## Themes
- research-synthesis-agents: research was "trapped in documents ... teams rarely referenced"; NotebookLM was chosen because it answers only from uploaded sources, lets you toggle sources and cites them (24:02, 28:51).
- ai-synthesis-hallucination-risk: the key instruction was "Don't add or modify text that is not written or implied" in the sources; citations were used to check each persona trait (31:59, 33:22).
- synthetic-users-limits: a persona's answer is said to represent "thousands of potential customers" (38:40). That is an assertion; no test against real behaviour is shown. The value claimed is reuse of existing research, not new evidence.

## Key points
- Design choice: persona as instructions ("you are that person ... this is your belief system"), not uploaded files, so you talk with the persona rather than about it (27:05).
- Prompts needed hand-tightening: Gemini drafts went over the custom GPT's 8,000-character limit and lacked guardrails (no general-assistant behaviour, no politics or slang), added with ChatGPT or Claude (34:55).
- Recruiting agent-mode demo: of 5 LinkedIn candidates found, 4 were new to the hiring manager and 1 was already in process (20:00).

## Could not verify
- Transcript read 20:00-41:00 in full; the recruiting prompt build (2:10-16:29) and parking calendar segment were skimmed. Persona usage ("one of the most talked to internal chats") isn't quantified, and nothing measures decision impact.
