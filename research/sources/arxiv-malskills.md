---
title: "MalSkills: Detecting Malicious Skills in the Agentic Supply Chain via Neuro-symbolic Reasoning"
source_url: https://arxiv.org/abs/2603.27204
author: Shenao Wang, Junjie He, Yanjie Zhao, Yayi Wang, Kan Yu, Haoyu Wang
publisher: arXiv (accepted ASE 2026)
published: 2026-03-28
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-supply-chain-security]
relevance: medium
---

## Relevance to the project
Academic, independent-of-vendor measurement of malicious skills across seven public registries, and a detector that beats five baselines. Supports the claim that registry-side checks are incomplete and that scanning needs to reason over instructions plus code together.

## Themes
- skill-supply-chain-security: 150,108 skills collected from 7 registries; 620 flagged, 400 confirmed malicious by manual review (v2, revised 2026-08-21); the earlier version/search summary reported 262; ~90% of confirmed cases were data theft/exfiltration (v1 summary). Benchmark of 200 skills, F1 93%, +5 to +87 points over baselines.

## Key points
- Neuro-symbolic: symbolic parsing plus LLM semantic analysis, dependency graph of artifacts, operations, operands and value flows.
- Authors reported findings responsibly; platform confirmation pending.

## Could not verify
- Count differs between versions (262 vs 400); only the abstract page was read.
