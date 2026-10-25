---
title: "Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate"
source_url: https://doi.org/10.1145/3640543.3645199
author: Chun-Wei Chiang, Zhuoran Lu, Zhuoyan Li, Ming Yin (Purdue)
publisher: ACM IUI 2024 (29th International Conference on Intelligent User Interfaces), pp. 103-119; NSF PAR record 10524816
published: 2024-03-18
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [red-team-stance, human-thinking-skills, overreliance-and-deskilling]
relevance: high
---

## Relevance to the project
The direct test of the "critique" stance: an LLM devil's advocate added to group decisions. The design varied two things, interactivity and target (argue against the AI's recommendation or against the group majority), and the version that argued against the AI promoted more appropriate reliance on it. That is evidence that a red-team agent is most useful when pointed at the other agent's output, not at the humans, and that it need not raise perceived workload. For PM review it supports a second agent whose job is to attack the first agent's spec or recommendation before humans see it.

## Themes
- red-team-stance: four devil's-advocate styles varying interactivity and whether they challenged the AI's recommendation or the group's majority (abstract via OpenAlex).
- overreliance-and-deskilling: advocates arguing against the AI's recommendation "promoted more appropriate reliance on AI" (abstract).
- human-thinking-skills: devil's advocates generally did not substantially increase perceived workload; interactive ones were seen as more collaborative and higher quality (abstract).

## Key points
- Randomised human-subject experiment with groups making AI-assisted decisions; 90 citations by retrieval (OpenAlex).
- A 2025 follow-up from a Korean group (IUI 2025, "Amplifying Minority Voices") extends the idea to surfacing minority opinions; not read.
- Fits the library's goose "Adversary Mode" and Block's red-team exercise as product-side instances of a reviewer agent.

## Could not verify
- ACM page returned 403; design details (group size, task, N) and effect sizes were not read.
