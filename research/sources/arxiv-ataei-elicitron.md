---
title: "Elicitron: An LLM Agent-Based Simulation Framework for Design Requirements Elicitation"
source_url: https://arxiv.org/abs/2404.16045
author: Mohammadmehdi Ataei, Hyunmin Cheong, Daniele Grandi, Ye Wang, Nigel Morris, Alexander Tessier (Autodesk Research)
publisher: arXiv (later JCISE 2024)
published: 2024-04-04
retrieved: 2026-11-06
type: paper
evidence: independent
filed_by: design-requirements-agent
themes: [elicitation-agent-evidence, synthetic-users-limits, agent-led-intent-shaping]
relevance: medium
---

## Relevance to the project
Elicitron generates many simulated users, has them walk through a product experience, interviews them and classifies the needs they reveal, including latent needs they did not state. Its measured results are the strongest published case for agents surfacing needs a person did not bring, and it reports that an LLM given explicit criteria and chain-of-thought classified latent versus explicit needs at F1 0.95. For the requirements agent, the transferable part is the classification result (explicit criteria lift accuracy sharply), not the simulated users, which the project's existing evidence says are shallow.

## Themes
- elicitation-agent-evidence: latent needs per agent: manual empathic-lead-user agents M = 10.9, automatic with steering prompt 9.9, automatic only 8.8; the manual versus automatic difference was significant (p < 0.05). The authors claim more latent needs than the human interview baseline but could not test it statistically because the baseline reported only means.
- agent-led-intent-shaping: classifying needs as latent or not: zero-shot F1 0.76; with criteria F1 0.92; chain-of-thought with criteria F1 0.95 (Experiment 3, 20 latent and 20 non-latent needs).
- synthetic-users-limits: serial generation of agents gave far more diverse needs than parallel generation (convex-hull diversity 0.87 versus 0.27); the authors say prioritising latent needs "remains a designer's task" and that the model struggles to separate latent from non-latent needs in several cases.

## Key points
- Four components: agent generation, product experience generation, agent interview, analysis. Cost of Experiment 2 was about $2.40 with GPT-4-Turbo.
- Human labelling agreement with the model's labels: F-score 0.83.
- No user validation study; output limited to about 20 agents per serial call by output length.

## Could not verify
- Read through WebFetch's model-summarised view of the abstract and HTML v1; the human baseline's values were not reported in the paper.
