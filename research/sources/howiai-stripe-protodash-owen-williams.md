---
title: "How Stripe's design manager vibe coded an internal prototyping studio (Protodash) | Owen Williams (How I AI)"
source_url: https://www.youtube.com/watch?v=hQFEAZK__q0
author: Claire Vo (host), Owen Williams (design manager, Stripe)
publisher: How I AI; summary at https://www.chatprd.ai/how-i-ai/stripe-owen-williams-on-buildling-internal-prototyping-studio
published: 2026-05-04
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [prototyping-agents-limits, non-engineer-builders, tacit-knowledge-capture, spec-becomes-prototype-and-evals, shared-persistent-sessions, build-vs-buy]
relevance: high
---

## Relevance to the project
Protodash is a Stripe Dashboard prototyping kit and browser studio built over ~18 months by a design manager, now used by "more PMs than designers". Its core is **tacit design knowledge written down as agent rules** (how to use the Sail design system, which internal component matches which Figma pattern, what not to do when the MCP server is down), the kind of expert-curated capture the working hypothesis is about. It also shows PMs unblocking themselves without a designer, prototypes becoming the handoff source of truth, and design-review comments turned into an agent fix queue. Bears on prototyping, the PM job map and the context-creation hypothesis.

## Themes
- tacit-knowledge-capture: v1 was "a bundle of cursor rules" plus the Sail MCP server; "I feel insane writing these rules, but like once you've got them, it works pretty well" (38:00); rules "whittled down through my various experiments" (08:00).
- non-engineer-builders: "it's actually more PMs than designers these days" (04:00); a PM on an unstaffed MCP area "can unblock himself"; PMs paste a PRD from Google Docs and it builds (32:00).
- prototyping-agents-limits: gets "90% of the way most of the time ... it will make slop" (04:00); "that taste, that craft is ... why designers will always exist" (40:00).
- spec-becomes-prototype-and-evals: Radar designers' prototype became a PR an engineer worked from: "just use the prototype as the source of truth" (46:00).
- shared-persistent-sessions: prototyping feed, remix anyone's prototype, design-review mode with URL comments summarised by AI and queued as fixes (18:00, 26:00-28:00).
- build-vs-buy: internal tools can match "the culture and cadence of your team"; internal tool "doesn't have to be production grade" (20:00, 30:00).

## Key points
- Runs on devboxes (go/proto link, ready in about a minute or two); "Proto Dev Studio" adds an in-browser agent so no Cursor needed.
- Fidelity modes (monospace, greyscale) to signal work in progress; state emulation (merchant name, sandbox banner).
- Designers send pull requests to evolve the tool.

## Could not verify
- No usage numbers. Auto-caption transcript ("sale" = Sail, "Clockwork"/"Clojure" = Claude Code). Relationship between Protodash and Harbor not stated by either source.
