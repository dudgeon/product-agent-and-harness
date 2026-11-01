---
title: "BMad Knowledge Base (BMAD-METHOD v4, bmad-core/data/bmad-kb.md)"
source_url: https://github.com/bmad-code-org/BMAD-METHOD/blob/v4.44.3/bmad-core/data/bmad-kb.md
author: BMad Code
publisher: GitHub
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, relay-information-loss, human-review-gates]
relevance: medium
---

## Relevance to the project
The v4 generation of BMAD, the version most practitioner write-ups describe: PM and architect documents are "sharded" into small files, a Scrum Master agent writes story files, Dev and QA agents implement and review, and the person approves every status change and starts a fresh chat for each agent. It is first-party evidence that the method treats clean context per role as a feature and the human as the router between agents.

## Themes
- process-artifacts-as-coordination: "Documents created by PM/Architect (in Web or IDE) MUST be sharded for development"; "Include story file content to save dev agent lookup time"; cycle "Continue SM → Dev → QA cycle until all epic stories complete".
- relay-information-loss: "ALWAYS start new chat between SM, Dev, and QA work"; "Context windows matter! Always use fresh, clean context windows": the method deliberately cuts the transcript at every seam and relies on the story file.
- human-review-gates: "You → Review and approve story"; "Each status change requires user verification and approval before proceeding."

## Key points
- Planning often happens in a web chat UI and is then moved into the IDE; the KB warns not to shard in the web UI.
- Who decides the next step: the person, every time (human as router).
- Typed record: story files from templates with status fields; prose bodies.
- Superseded in later versions by Sofia and tickets.toml (see bmad-docs-choose-a-planning-path).

## Could not verify
- Fetched from raw.githubusercontent.com at tag v4.44.3; exact tag date not checked; model-summarised fetch.
