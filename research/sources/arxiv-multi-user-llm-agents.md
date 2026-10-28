---
title: "Multi-User Large Language Model Agents"
source_url: https://arxiv.org/abs/2604.08567
author: Shu Yang, Shenzhe Zhu, Hao Zhu, José Ramón Enríquez, Di Wang, Alex Pentland, Michiel A. Bakker, Jiaxin Pei
publisher: arXiv
published: 2026-03-19
retrieved: 2026-10-26
type: paper
evidence: independent
filed_by: research-shared-persistent-agents
themes: [shared-persistent-sessions, identity-delegation, agent-failure-modes, public-by-default-agent-work]
relevance: high
---
## Relevance to the project
The first systematic test I found of what happens when one agent serves several people at once, which is the precondition for people watching and steering a shared thread (catalogue item 6) and for a teammate joining a running session (item 2). Across 19 frontier and open models, instruction accuracy drops when users' instructions conflict (e.g. Claude Haiku 4.5 from 0.86 to 0.62), and privacy erodes over turns (Claude 3.5 Haiku from above 0.95 to below 0.75 within four rounds of access-control pressure). Simulated benchmarks, but they put numbers on the identity and privacy objections to multiplayer agents.

## Themes
- shared-persistent-sessions: three scenarios: multi-user instruction following with differing authority (304 selection + 1,298 execution scenarios, 2-10 users), cross-user access control (216), meeting coordination (216) (§4.2)
- identity-delegation: "multi-user instruction following is fragile in the presence of conflict"; models do not keep stable priorities between principals such as a CEO and an engineer (§5.3, Fig. 3)
- public-by-default-agent-work: privacy scores fall across rounds for nearly all models, mostly in rounds 1-6; privacy and utility trade off (GPT-5.1 privacy 98.6 / utility 60.1; GPT-OSS-120B 92.2 / 94.4) (§5.2-5.3, Fig. 4)
- agent-failure-modes: coordination success declines with group size and turns grow roughly linearly with N; best scheduling success 77.3% (Appendix B) 

## Key points
- Frames multi-user agents as a multi-principal decision problem with conflicts, information asymmetry and privacy constraints.
- Conclusion: current models are not reliably ready for multi-user deployment.

## Could not verify
- Table values differ slightly from text in places; text values used. Simulated, not field, study.
