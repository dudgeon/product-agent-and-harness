---
title: "Office Hours: Building the case for leaders who ship with DoorDash"
source_url: https://claude.com/customers/doordash-boris-office-hours
author: Anthropic (Boris Cherny with Andy Fang of DoorDash)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: video
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, product-coherence-over-automation, enablement-by-product, compounding-context-repo, human-review-gates]
relevance: medium
---

## Relevance to the project
DoorDash's co-founder and CTO describes a company-wide rollout (Claude Code across engineering, Cowork for all roughly 4,000 employees) where the bottleneck moved from coding to cross-functional process: product, design and ship reviews became "a huge friction point" for user-facing work. It is direct evidence for the product-coherence tension the project tracks, plus concrete adoption mechanics (open token budgets, AI champions per domain, written artifacts as the scaling unit, designers and PMs shipping code). Anthropic-published customer conversation: the 3-5x and migration claims are DoorDash's, unaudited.

## Themes
- non-engineer-builders: goals set for designers to ship code to production ("didn't go 100% smoothly"); best teams have designers and PMs embedded in the dev cycle (Andy, mid-transcript).
- product-coherence-over-automation: user-facing features need cross-functional buy-in; product/ship/design review now friction; Andy asks "do we even need to have product review?" (learnings answer).
- human-review-gates: AI code review agents led to engineers "rubber stamping" reviews; more security issues surfacing industry-wide (Andy, early).
- compounding-context-repo: a tech lead wrote 50+ architectural principles as markdown in the repo for agents; standardized team skills (e.g. mobile simulator skill) (learnings answer).
- enablement-by-product: written artifacts shared company-wide, including failures, as "the most scalable way to distribute learnings" and readable by agents (Andy, adoption and closing).

## Key points
- **Scale (DoorDash's claims)**: Claude Code across the company; all 4,000 employees have Cowork; Claude models also used in other harnesses.
- **Flex**: internal platform of security-"blessed" VMs in DoorDash's cloud to fire off Claude sessions with the right tools; built with the Claude Agent SDK; powers the AI code review agent.
- **Adoption mechanics**: special fast procurement/review process with IT security; open token budgets early ("give everyone tokens because you don't know who the innovation's going to come from", Boris); EMs asked to ship production code themselves; AI champions identified per domain (sales, marketing, ops, support) to automate workflows or build shared skills.
- **3-5x challenge**: teams asked to finish projects in 3-5x less time; handpicked teams get VP-level sponsorship and a mandate to surface non-coding blockers. Anecdote: a migration scoped at four engineers for a quarter done by one in three weeks.
- **Org shape**: small teams (3-5) as the accelerant; fewer domain experts acting as gatekeepers via agents and principle files, more generalists.
- **ROI**: code throughput as an admittedly gameable proxy for engineering; for knowledge work, "raise the floor" plus per-department workflow automation; "exploration phase".
- Limits: no hard numbers beyond anecdotes; no detail on how review processes were actually changed; quality and security downside acknowledged but not quantified.

## Notable quotes
- "It's not just an engineering problem, it's a whole company problem." (Andy Fang)
- "People are kind of just rubber stamping the code reviews." (Andy Fang)

## Could not verify
- Publication date; the video was not watched (page transcript only).
- The page labels Andy Fang "Co-founder and CTO" in the intro and "Co-founder and CEO" in pull quotes; CTO used here.
