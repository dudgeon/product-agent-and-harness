---
title: "Ontology MCP: Sample architecture (Palantir Foundry docs)"
source_url: https://www.palantir.com/docs/foundry/ontology-mcp/sample-architecture
author: Palantir Technologies
publisher: palantir.com
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [blackboard-coordination, org-context-grounding, identity-delegation]
relevance: medium
---

## Relevance to the project
The clearest vendor form of "agents integrate through typed shared records": external agents read ontology object types through a SQL tool and may write only through predefined action types, each exposed as its own MCP tool; an orchestrating agent "reads from the ontology and delegates work to other agents" while the ontology stays "the system of record". For a dependency-mapping module, it is a precedent for typed asks and owner records that any harness can read and only mutate through governed actions.

## Themes
- blackboard-coordination: "keep the ontology as the system of record while letting specialized agents handle individual tasks".
- org-context-grounding: every object type in the Developer Console application is reachable through a SQL tool; query functions can be tools.
- identity-delegation: writes restricted to "controlled, restricted actions"; whose identity acts is on a separate auth page not read.

## Key points
- AIP Logic or AIP chatbot logic can be saved as a function and exposed over MCP, so a remote agent is just another tool.
- Typed record: object types and action types with schemas; contrast with prose markdown in spec-driven repos.
- The page does not say delegation itself happens through ontology writes, nor mention audit.

## Could not verify
- Authentication and authorisation page; audit behaviour; page date (footer 2026). Model-summarised fetch.
