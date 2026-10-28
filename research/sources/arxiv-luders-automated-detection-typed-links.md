---
title: "Automated Detection of Typed Links in Issue Trackers"
source_url: https://arxiv.org/abs/2206.07182
author: Clara Marie Lüders, Tim Pietz, Walid Maalej (University of Hamburg)
publisher: arXiv / IEEE RE 2022
published: 2022-06-14
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-detection-automation, stale-records-mislead-agents, ai-synthesis-hallucination-risk]
relevance: high
---
## Relevance to the project
The best-known benchmark for automatically detecting typed links (Epic, Subtask, Block, Depend, Duplicate, Relate) between Jira issues: a BERT model on titles and descriptions reaches macro F1 0.64 across nine link types, far better on hierarchy links (Epic 0.97, Subtask 0.89) than on the relational ones a dependency agent cares about. It sets the realistic ceiling for "read the tracker and propose blocked-by links": detecting that two issues are linked is much easier than saying how. The finding that "Relate" is a default dumping ground also says the existing link data an agent would learn from is noisy.

## Themes
- dependency-detection-automation: BERT on linked-issue text, 15 public Jira repositories, average macro F1 0.64 across 9 popular link types (weighted F1 0.73); Subtask 0.89, Epic 0.97 (abstract).
- stale-records-mislead-agents: Relate links are often confused with other types, suggesting people use them when the relationship is unclear; repositories differ significantly by how and by whom they are used (abstract), so training data from one tracker transfers badly.
- ai-synthesis-hallucination-risk: shorter issue text predicted better (correlation about -0.70), and the model "does not simply learn textual similarity" (abstract): long, rich specs are not automatically easier.

## Key points
- Block and Depend are near-synonyms, but some trackers use both, so the authors keep them separate (per the journal version's discussion, via search summary).
- The journal extension ("On understanding and predicting issue links", Requirements Engineering 28(4), 2023, Lüders, Pietz, Maalej) reports the same 0.64 macro F1 for typed links and an average macro F1 of 0.95 when the task is only whether a link exists.
- Per-type F1 for Block/Depend is not in the abstract.

## Could not verify
- Per-type figures for Block and Depend, and the journal version's claim that only about 36% of issues carry any link (seen only in a search summary; the Springer page was not reachable).
