---
title: "A conversation with Seth Hain about Epic's internal AI adoption"
source_url: https://claude.com/customers/epic-systems
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, org-learning-loop, spec-becomes-prototype-and-evals, outcome-measurement-gap, status-update-agents]
relevance: medium
---

## Relevance to the project
A regulated-industry (healthcare) data point: Epic's SVP of R&D says over half of Epic's Claude Code usage is from non-developers, and gives the example of a pharmacist who brought a working MyChart prototype instead of slides. It argues governance should remove "unnecessary roadblocks" and frames trust in clinical AI through verifiable outputs and monitoring of draft-acceptance rates, a usable pattern for measuring PM-agent output. Evidence is an edited conference Q&A on an Anthropic customer page; figures are Epic's claims and no PM-specific practice is described.

## Themes
- non-engineer-builders: "Over half of Claude Code usage is from non-developers" (page header stat); pharmacist's interactive prototype of new MyChart functionality became a shared link others iterate on.
- org-learning-loop: adoption spread person to person; Epic built internal tools to show who was using AI and for what so others could copy; a development-leads meeting was given over to hands-on use.
- spec-becomes-prototype-and-evals: the prototype went "beyond slides or written documentation" as the way to show what was wanted.
- outcome-measurement-gap: monitoring draft acceptance: 100% unedited use and 0% use are both signs something is wrong (answer on clinical trust).
- status-update-agents: a team's shared Claude project answers status questions; "whenever I ask for a status update, I get a link to a Claude conversation".

## Key points
- Setting: Anthropic event "The Briefing: Enterprise Agents"; interviewer Jonathan Dahlberg (head of applied AI, Anthropic). Edited for length.
- Adoption approach: everyone given access to explore; leaders expected to use the tools daily; governance reviewed for unnecessary blockers (Excel analogy).
- Quality in a "do no harm" setting: skills and MCP servers used to add checks in Epic's own development pipelines; record summarisation released with links back to source passages so clinicians can verify.
- Observed shift (Hain's view): in the prior 8 to 12 weeks, fewer points where a human had to step in mid-task, giving "contiguous" blocks of agent work.
- Domain immersion: developers spend time on-site with clinicians; Hain says people who understand the 100+ handoffs in a care episode are best placed to direct the tools.
- Claims: MyChart used by over 195 million patients; 85% of organisations Epic works with already use AI in production; Epic building medical event models on health records and seeing scaling laws.
- Limits: no controls, data-handling or compliance specifics for Claude Code use by non-developers; no metrics on output quality.

## Notable quotes
- "It's functioning as part of the team, not just as an assistant." (Seth Hain, SVP of R&D, Epic, on a shared Claude project)

## Could not verify
- Publication date (page shows none; content refers to "what's ahead for healthcare in 2026").
- What governance or sandboxing applies to non-developer Claude Code use at Epic.
