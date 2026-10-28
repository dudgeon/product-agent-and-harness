---
title: "Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining"
source_url: https://arxiv.org/abs/2606.20363
author: Yuexing Hao, Xiaomin Li
publisher: arXiv
published: 2026-06-18
retrieved: 2026-10-26
type: paper
evidence: independent
filed_by: research-shared-persistent-agents
themes: [skill-improvement-loops, skill-standards, vendor-claims-vs-independent-evidence]
relevance: medium
---
## Relevance to the project
A diagnostic study with a largely negative result for automatic standardisation from traces (catalogue item 7): skills mined from GUI interaction trajectories were readable (5 of 8 clusters at 0.95+ purity) but did not reliably improve downstream agents, and on key source-domain metrics the trained policy underperformed trivial frequency priors. The authors' phrase "readability does not imply transfer" is a useful caution: a skill that looks right to a person reviewing mined traces may not make the agent better, so mined candidates still need evals.

## Themes
- skill-improvement-loops: pipeline segments trajectories, clusters segments into candidate skills, and trains a skill-aware policy; gains were marginal (IW skill-step accuracy 18.5% to 20.5% with GRPO; BrowseComp+ essentially unchanged) (abstract)
- skill-standards: mined SKILL.md clusters are human-readable but "readability does not imply transfer" (abstract)
- vendor-claims-vs-independent-evidence: a negative independent result against the common assumption that traces can be auto-distilled into skills (abstract, 2026-06)

## Key points
- Authors attribute limits to the boundary detector, orderless segment representation and offline reward model, so the negative result may be method-specific.

## Notable quotes
- "readability does not imply transfer"

## Could not verify
- Read via abstract; not peer-reviewed as far as the page shows.
