---
title: Tessl documentation (overview)
source_url: https://docs.tessl.io/
author: Tessl
publisher: docs.tessl.io
published: unknown
retrieved: 2026-10-25
type: docs
evidence: vendor-claim
filed_by: research-skill-rigidity-spectrum
themes: [docs-as-code-prd, evals-autonomy-trust, artifact-standardization]
relevance: medium
---

## Relevance to the project
Tessl was one of the three tools in Böckeler's spec-driven development review (fowler-bockeler-sdd-kiro-speckit-tessl), framed then around spec-as-source. Its docs now describe a platform for managing agent skills: registry, governance scoring, with/without-context evals and drift detection. The shift itself is evidence that the field moved from "specs as the artifact" toward "skills and their evals as the artifact".

## Themes
- docs-as-code-prd: skills, rules, docs and config are plain repo files, "versioned, reviewed, and rolled out with the same rigor as code dependencies" (overview).
- evals-autonomy-trust: Evals run the agent on real tasks with and without a skill's context to measure its impact (overview).
- artifact-standardization: Governance scans and scores skills against best practices and company standards, with Snyk security scoring, RBAC and policies; Context and Findings reports drift, overlap and unmanaged copies (overview).

## Key points
- Six components: registry and package manager; governance; evals; observability (where skills activate; mining logs for recurring mistakes); context and findings; Tessl Agent (open beta).
- The overview page does not mention spec registries, usage specs or spec-to-test links; I did not confirm whether those still exist.
- My judgment: governance scoring is rubric-like and partly deterministic; evals are the improvement loop (dimension 7).

## Could not verify
- Whether Tessl's earlier spec-as-source features survive; dates of the pivot not established.
