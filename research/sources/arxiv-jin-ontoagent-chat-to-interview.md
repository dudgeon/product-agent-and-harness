---
title: "From Chat to Interview: Agentic Requirements Elicitation with an Experience Ontology"
source_url: https://arxiv.org/abs/2605.05828
author: Dongming Jin, Zhi Jin, Yaotian Yang, Linyu Li, Zheng Fang, Yuanpeng He, Wenchun Jing, Xiaohong Chen
publisher: arXiv (RE 2026)
published: 2026-05-07
retrieved: 2026-11-06
type: paper
evidence: independent
filed_by: design-requirements-agent
themes: [elicitation-agent-evidence, method-as-harness, agent-led-intent-shaping]
relevance: medium
---

## Relevance to the project
The follow-up to ReqElicitGym by the same group: an interview agent (OntoAgent) that builds an "experience ontology" of requirement concerns from domain requirement descriptions, then at each turn parses the user's answer, scores and re-ranks the ontology's concerns, prunes, and asks about the selected concern. It reports a 33% improvement in implicit-requirement elicitation and 21% in early key questions over baselines. The mechanism is the same one the intent-shaping brief proposes (a structured category list drives the next question) applied to feature requirements rather than enterprise obligations, and it is the first measured evidence that such structure beats free chat.

## Themes
- elicitation-agent-evidence: abstract reports it "significantly outperforms existing baselines" with +33% IRE and +21% TKQR, plus ablations and a qualitative user study.
- method-as-harness: four operations per turn (ParseUser, ScoreOnto, ReRankOnto, GatePrune) select the concern; the dialogue context then shapes the question; aimed at "the omission of implicit requirements and redundant questions".
- agent-led-intent-shaping: the ontology is mined from existing requirement descriptions in the domain, the analogue of mining past specs and obligation libraries.

## Could not verify
- Only the arXiv abstract page was read (WebFetch summary); baselines, absolute scores and the user study were not seen. Evaluated in one domain (websites); the authors state extension to other domains as a belief.
