---
title: "Blackboard system"
source_url: https://en.wikipedia.org/wiki/Blackboard_system
author: Wikipedia contributors
publisher: Wikipedia
published: unknown
retrieved: 2026-10-31
type: article
evidence: independent
filed_by: research-agent-handoff-models
themes: [blackboard-coordination]
relevance: low
---

## Relevance to the project
A secondary overview standing in for the classic sources (Nii 1986, AI Magazine; Hayes-Roth 1985, "A blackboard architecture for control"), which could not be fetched. It gives the original model's three parts and the opportunistic-control idea that 2025 LLM blackboard papers revive, so the project can name what "the repo as blackboard" inherits and what it leaves out (a control component).

## Themes
- blackboard-coordination: model = "a common knowledge base, the 'blackboard', is iteratively updated by a diverse group of specialist knowledge sources"; "The specialists all watch the blackboard, looking for an opportunity to apply their expertise"; parts = knowledge sources, blackboard, and a control shell "which controls the flow of problem-solving activity".

## Key points
- Origin: Hearsay-II speech understanding (1970s); BB1 (Hayes-Roth) applied the blackboard to its own control problem, with control knowledge sources reasoning about which domain knowledge source should act next.
- Opportunistic control: activation is not scheduled in advance; the control component chooses each cycle from the current state.
- Point for the project (my reading): the classic model always had a control component. A repo or ticket store used as a blackboard without one (no scheduler, no hook, no human router) has specialists but nobody deciding who goes next.

## Could not verify
- Nii (1986) full text: the AAAI OJS page blocked automated access and the Stanford tech report (STAN-CS-86-1123) host refused connection; Hayes-Roth (1985) not read. Claims about them here are via this secondary page.
