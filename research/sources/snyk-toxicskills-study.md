---
title: ToxicSkills: Malicious AI agent skills in ClawHub (Snyk)
source_url: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub
author: Snyk
publisher: snyk.io
published: 2026-02-05
retrieved: 2026-10-24
type: report
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-supply-chain-security, skills-marketplace]
relevance: high
---

## Relevance to the project
The first large audit of public agent skills. Security vendor, so an incentive to find problems, but the numbers are corroborated in direction by Koi, CSA and an academic scan. Establishes that third-party skills are a supply-chain surface comparable to npm/PyPI and that a "private marketplace with review" is a security control, not just convenience.

## Themes
- skill-supply-chain-security: 3,984 skills from ClawHub and skills.sh scanned on 2026-02-05: 534 (13.4%) with a critical issue; 1,467 (36.82%) with any issue; 76 confirmed malicious payloads; 91% of confirmed-malicious combine prompt injection with traditional malware; 8 malicious skills still live at publication.
- skills-marketplace: top-100 skills.sh set used as legitimate baseline (credential-handling issues still 5.0%).

## Key points
- Method: eight policies, Snyk `mcp-scan` (models plus deterministic rules), human review of hundreds; counts de-duplicated by author and skill ID, so republished copies count separately.
- Recommendations: treat skills as a software supply chain; audit with `mcp-scan --skills`; rotate credentials; review agent memory files.

## Could not verify
- 0% false-positive claim is self-reported; the methodology says ClawHub plus skills.sh but findings refer only to ClawHub. Ecosystem here is largely OpenClaw, not Claude Code; transferability is an inference.
