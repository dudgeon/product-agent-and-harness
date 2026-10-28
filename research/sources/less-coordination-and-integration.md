---
title: "Coordination & Integration (LeSS framework)"
source_url: https://less.works/less/framework/coordination-and-integration
author: The LeSS Company (Craig Larman, Bas Vodde)
publisher: less.works
published: unknown
retrieved: 2026-10-28
type: docs
evidence: independent
filed_by: research-dependency-agent
themes: [dependency-types-and-practices, coordination-cost-and-waiting, dependency-knowledge-carriers]
relevance: medium
---

## Relevance to the project
Large-Scale Scrum (LeSS) takes the opposite stance to SAFe on dependencies: it recommends against Scrum of Scrums and central coordinators, treats the urge to hold one as a symptom of component teams and single-function groups, and pushes coordination down to teams ("Just Talk", "Communicate in Code", scouts, travelers). It is the clearest statement that many dependencies are self-inflicted by org design. Its assumption, feature teams able to change any part of the code, rarely holds in regulated platform-centric enterprises, where core systems are owned by separate teams with their own controls, so its remedies transfer only partly.

## Themes
- dependency-types-and-practices: seven practices: Just Talk ("You do not need a formal, official, usually slow coordination mechanism in order to coordinate"), Communicate in Code (shared mainline, no branches), Scouts (a member monitors another team or interface for a Sprint), component communities and mentors, multi-team meetings, Travelers (scarce experts rotate), Leading Team (one feature team leads a large feature).
- coordination-cost-and-waiting: on Scrum of Scrums, "it is recommended to not do this in LeSS"; the urge to hold one "can be a sign of unnecessary dependency or coordination problems caused by single-function groups and component teams".
- dependency-knowledge-carriers: a component mentor is "a teacher and steward of the component, not a gate" and "doesn't review code for approval before it's committed".

## Key points
- No central coordinator, project manager or coordination role is defined; dependencies are a symptom to reduce rather than manage centrally.
- Transfer note (this filer's reading): the component-mentor-not-gate model conflicts with regulated environments where platform owners are accountable for change to systems of record and must approve; an agent cannot assume "just talk" when the other side is a controlled intake.
