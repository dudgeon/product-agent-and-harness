---
title: "Coordination in Large-Scale Software Development: Helpful and Unhelpful Behaviors"
source_url: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/coordination-techreport08.pdf
author: Christopher Poile, Andrew Begel, Nachiappan Nagappan, Lucas Layman
publisher: Microsoft Research (technical report; companion to the ICSE CHASE 2009 paper)
published: 2009-09-28
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [coordination-cost-and-waiting, dependency-value-evidence, stale-records-mislead-agents]
relevance: high
---

## Relevance to the project
The clearest survey evidence of what dependency management costs individual engineers inside one large company: of 775 Microsoft engineers, 49% frequently have to ping the people they depend on for status, only 34% say dependencies proactively tell them, 67% say work they depend on changes without their knowledge, and 79% want more status. Coordination is mostly about schedules, features and priorities, not code. It describes almost exactly the status-chasing and change-notification job a dependency agent would take on. Microsoft researchers studying Microsoft; 31% response rate.

## Themes
- coordination-cost-and-waiting: "I need to ping the people I depend on for status": 49% frequently or more; "My dependencies proactively communicate their status to me": 34%; "I need to maintain constant contact with my dependent team in order to get what I want": 78% agree (Table 2).
- stale-records-mislead-agents: "Work items I depend on are changed without my knowledge": 67% occasionally or more; "My team has problems deciding which team has responsibility for a work item": 47% agree (Table 2).
- dependency-value-evidence: "It is difficult to work with dependent teams because our commitments are not aligned": 60% agree; "I find it difficult to get a team I depend on to implement a change I require": 25% frequently or more (Table 2); "tool support for dependency management is currently limited" and no tool was used universally to communicate status (section 4.2).

## Key points
- Method: 31 interviews with 26 members of a 300-person application team coordinating with a platform library team in Redmond and teams in Boston and Hyderabad; survey sent to about 2,500 technical employees, 775 responses (31%).
- 69% of respondents chase status by email; some teams rely on being pinged by their dependency as their tracking mechanism.
- 88% say personal relationships with teams they depend on help; 84% want a better relationship. Coordination is framed as communication, capacity and cooperation.
- The CHASE 2009 paper's abstract reports schedules and features, not code or interfaces, as the most common objects of coordination.

## Notable quotes
- "It's a question of priorities. It always comes down to priorities." (interviewee, section 4.2.2)
