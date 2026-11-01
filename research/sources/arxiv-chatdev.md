---
title: "ChatDev: Communicative Agents for Software Development"
source_url: https://arxiv.org/abs/2307.07924
author: Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun
publisher: arXiv (ACL 2024)
published: 2023-07-16
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, relay-information-loss, agent-frameworks]
relevance: medium
---

## Relevance to the project
ChatDev is the chat-based foil to MetaGPT's document pool: agents talk in pairs inside each phase, but between phases only the phase's solution (not the dialogue) is carried forward. So even the "agents talk" design is a finish-to-start relay of artifacts at the phase seam, chosen because full dialogue does not fit in context. Bears on what model A should carry at a seam: the artifact alone, or the artifact plus reasons.

## Themes
- process-artifacts-as-coordination: "the chat chain only transmits the solutions from previous phases as long-term memories" (Section 3.1); dialogue stays as short-term memory inside a phase.
- relay-information-loss: the stated reason for dropping dialogue is limited context length; the paper does not ablate this memory split, so its cost is unmeasured.
- agent-frameworks: phases design, coding, testing; instructor-assistant role pairs; "communicative dehallucination" (the assistant asks for specifics before answering).

## Key points
- Results (Table 1, as reported): quality 0.3953 vs MetaGPT 0.1523; executability 0.88 vs 0.4145; completeness 0.56 vs 0.4834; about 22,950 tokens vs 29,280. Note MetaGPT's own paper reports the reverse ordering on its benchmark (see arxiv-metagpt): each paper wins on its own measures.
- Limits: simple logic and low information density under vague requirements; evaluation of general software is hard; better for prototypes than complex systems.

## Could not verify
- Retrieved via WebFetch (v5 HTML, model-summarised); version dates v1 2023-07-16 to v5 2024-06-05.
