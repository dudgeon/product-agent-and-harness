---
title: "How Uber Built an Agentic System to Automate Design Specs in Minutes"
source_url: https://www.uber.com/us/en/blog/automate-design-specs/
author: Ian Guisard (Uber Base design system)
publisher: Uber Engineering Blog
published: 2026-03-11
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [skill-standards, deterministic-scaffold-model-nodes, artifact-standardization, non-engineer-builders]
relevance: medium
---

## Relevance to the project
uSpec is a designer-built agent system that writes component spec pages directly into Figma: the designer invokes a skill in Cursor with a component link, the agent reads the component through an open-source Figma MCP, and one skill per spec section (anatomy, API, properties, colour, structure, screen reader) fills a template. It is a clean example of skills as packaged domain expertise authored by a non-engineer, and of "AI interprets, scripts render". It is open-sourced (github.com/redongreen/uSpec, a personal account, not github.com/uber).

## Themes
- skill-standards: each skill loads its own instruction file with validation rules, schemas and reference docs, e.g. the screen-reader skill loads VoiceOver, TalkBack and ARIA references first so the agent picks documented properties (Architecture).
- deterministic-scaffold-model-nodes: "AI handles interpretation", programmatic scripts handle rendering into Figma (Design principle).
- artifact-standardization: structured schemas and templates make every author's spec the same shape (Benefits).
- non-engineer-builders: the design-system lead built it; designers now submit pull requests (Takeaways).

## Key points
- Hundreds of components across 7 stacks (UIKit, SwiftUI, Android XML, Compose, React, Go, SDUI); screen-reader spec for three platforms in under 2 minutes; months of spec work cut to days.
- Runs locally (Cursor plus Figma Desktop over a local WebSocket); no design data leaves the network.
- Roadmap: drift detection, code-to-spec, new spec types.

## Notable quotes
- "The agent doesn't guess at property names—it selects from documented APIs."

## Could not verify
- Not linked to Uber's skills marketplace or Cortana in the post; runs in Cursor, not the internal harness wrapper.
