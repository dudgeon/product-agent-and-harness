---
title: "From Figma to Claude Code and back | Gui Seiz & Alex Kern (Figma)"
source_url: https://www.lennysnewsletter.com/p/from-figma-to-claude-code-and-back
author: Claire Vo (host), Gui Seiz (designer, Figma), Alex Kern (engineer, Figma)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-03-11
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [intent-factory-before-discovery, artifact-standardization, pm-tool-connectivity, skills-marketplace, org-learning-loop, shared-persistent-sessions, human-judgment-pm-jobs, prototyping-agents-limits, tacit-knowledge-capture]
relevance: medium
---

## Relevance to the project
Figma's own designer and engineer demo a bidirectional loop: a coding agent (Codex or Claude Code) sends a running page, or every state of a flow, into an editable Figma frame via the Figma MCP; the team edits it together; the agent then reconciles the Figma frame back into the codebase. It is a concrete example of an artifact that stays synchronized across a human-editable surface and code, which bears on artifact-and-project-structure and on how a PM harness might keep specs, designs and code from drifting. It also supplies a first-party "design moved upstream to planning and downstream to craft" claim that parallels the film's "bottleneck moved to intent", and an SOP-to-skill pattern. Caveat: this is Figma promoting its own MCP launch, so the demo is real but the framing is a vendor's.

## Themes
- intent-factory-before-discovery: Seiz says the design role "really moved upstream": more time in planning and "what should we be building", because "the building will happen a lot quicker" (19:11); more priorities make it "above the cut line" (19:11).
- artifact-standardization: the problem is that "sources of truth diverge between design and code" (7:53); the MCP does structured-to-structured translation rather than screenshot-to-vision (Vo, 18:07), and pushes Figma edits back as a patch reconciled with the local codebase (15:12, 21:37).
- shared-persistent-sessions: once a page is in Figma, "my whole team can also jump in" (10:58); Figma becomes "shared common ground where different people can plug in" versus work "living on my machine" (14:32); prompting tools are not built for multiplayer collaboration (Vo, 11:41).
- human-judgment-pm-jobs: direct manipulation beats prompting for precision: "You can do a lot with a click that would take you 100 words" (13:05); humans in the loop for fine motor and taste judgments like colour (Vo, 13:46).
- skills-marketplace / org-learning-loop: Kern's `/ship` skill runs preflight checks, lint, Bazel build checks, pushes, watches Buildkite CI and auto-fixes minor failures "up to five times with a one hour timeout" (29:24-32:40); Vo: turn every onboarding wiki page into a skill: "shifted from this idea of an SOP into a skill" (33:02).
- pm-tool-connectivity: the hosted Figma MCP works from Codex and Claude Code; skills optional: "you could also just ask the MCP directly" (10:44).
- tacit-knowledge-capture: asking Claude to trace a service's naming history from commit history recovered "lore" from a contributor who left years ago (36:20).
- prototyping-agents-limits: code tools still lack precise editing: "I don't think we're there yet ... in terms of the precision editing" (13:05).

## Key points
- Demo 1 (7:53-21:51): Codex sends a locally hosted finance app's "budget allocation page" into Figma; Seiz edits it; Kern copies the frame URL into Claude Code, "bring the changes from this component into my code base", and the app updates to match.
- Demo 2 (22:55-25:23): "send all five states of the signup flow to Figma": the agent reads the codebase, finds the states and imports each into one Figma file so the designer can work while the engineer continues coding.
- Workflow collapse: the linear increasing-fidelity workflow is gone because "it's just as cheap to riff in code as it is to riff in design"; the team is "reinventing a workflow almost every day" depending on scale of change (4:04).
- Engineering practice: Kern runs "two, three, up to five" Claude Code instances, some reconciling design and code, some exploring, some "writing specs and documentation ... grounding technical specifications inside of code bases" (16:58). Figma uses hosted "dev boxes" with per-user bootstrap config, including a skill for creating skills (29:24).
- Sync vs async: async is Kern's default, but both value live, multiplayer canvas sessions; Seiz likens file hand-offs to "handing over USB sticks" (25:50-26:42).
- Lightning round: Seiz picks design first, Kern code first; "it depends" is the honest answer (35:06).

## Notable quotes
- "AI basically collapsed that. And it's just as cheap to riff in code as it is to riff in design" (4:04).
- "we've created this kind of shared common ground where different people can plug in" (14:32).
- "processes that would otherwise just be ... based on best intentions ... can be fully automated and brought into people's workflows by default" (33:55).

## Could not verify
- Full transcript read. The show notes claim structuring a codebase "so AI can write 90% of your code"; that figure was not stated in the transcript.
- Demo apps were built for the episode, not production Figma features; no data on adoption of the loop inside Figma.
- Vendor context: Figma had just launched the Claude Code and Codex MCP integrations.
