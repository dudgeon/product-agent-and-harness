---
title: How the product designer who built Claude Design uses it
source_url: https://claude.com/resources/articles/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them
author: Nate Parrott (product designer, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-07-24
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [spec-becomes-prototype-and-evals, agent-led-intent-shaping, artifact-standardization, prototyping-agents-limits, product-artifact-primitives]
relevance: high
---

## Relevance to the project
The designer who built Claude Design describes an explore-before-build workflow (many options, remix, wireframe first, design system as guardrail, hand off to Claude Code) and argues that as code generation gets cheaper the valuable work moves earlier: ideas, alignment and feedback. That directly supports the intent-shaping and spec dimension, where prototypes and HTML artifacts become the medium for shaping intent before engineering. It is one product's maker describing their own tool; no adoption, quality or outcome data beyond anecdotes.

## Themes
- spec-becomes-prototype-and-evals: interactive click-through prototypes built by handing Claude assets and saying "make it work"; each artifact has a shareable link like a doc ("Giving Claude an HTML playground").
- agent-led-intent-shaping: "ask for ten options, then remix"; generate 15 versions of a flow to collect colleague feedback; Claude provides starting points and the human chooses ("Best practices").
- artifact-standardization: brand files become a design system Claude builds with and checks its output against before showing it; teams can keep several; an admin can approve one standard and lock edits.
- prototyping-agents-limits: not for production software (use Claude Code), no image model so poor for logos; left undirected Claude falls back to recognisable house aesthetics ("What Claude Design is not meant to do", "Tell Claude what it should look like").
- product-artifact-primitives: HTML as the universal medium for decks, one-pagers, emails, animations, and "designs that are also their own editors" ("Make it alive").

## Key points
- Origin: sole designer on Claude Code for VS Code could not keep pace with engineers shipping faster after Opus 4.5; text-only prompting for designs failed; switching to HTML output in a chat-plus-preview split view plus prompts distilling Anthropic's brand worked. Spread internally after an Anthropic Labs offsite where everyone made pitch slides in it; Labs then staffed it.
- Scope widened from product mockups to any visual communication; decks were common enough to get their own entry point, Claude Slides.
- Integration: Claude Design works inside Claude Code (desktop or terminal) and `/design` creates, edits and syncs design projects; handing a design to Claude Code continues from existing work "instead of starting over from a screenshot".
- Context: connect GitHub or work from a local codebase so Claude fetches real components and screens; mid-conversation designs use files, memory, projects and skills already in context.
- Practices: do the thinking before prompting (voice notes, phone notes); specify fonts/colours or a moodboard; sketch on paper and upload; point-and-talk comments via dictation; wireframe first; make the last mile manual with direct edits (no tokens); queue messages while Claude works.
- Opus 5 claimed better than prior Opus models at reading charts, diagrams and screenshots.
- Availability: beta on Pro, Max, Team and Enterprise plans.
- Limits: single author's practice; no data on handoff fidelity to code, design-system compliance rates, or review of generated options.

## Notable quotes
- "As models get better at building production software, the work that matters most moves earlier in the process" ("What Claude Design is not meant to do")
- "Everything we draw should be alive by default." (quoting Bret Victor's talk blurb, "Make it alive")
