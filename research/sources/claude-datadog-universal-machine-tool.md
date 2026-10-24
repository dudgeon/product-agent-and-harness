---
title: How Datadog built a "universal machine tool" for Claude Code
source_url: https://claude.com/resources/articles/how-datadog-built-a-universal-machine-tool-for-claude-code
author: Anthropic (quoting Sesh Nalla, VP of Engineering, Datadog)
publisher: Claude (claude.com/resources)
published: 2026-07-21
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [spec-becomes-prototype-and-evals, agent-control-plane, docs-as-code-prd, agent-factory-sdlc]
relevance: medium
---

## Relevance to the project
Datadog's Temper flips the agent's output from code to specifications: the agent writes a behaviour, data-contract and authorization spec, a deterministic kernel verifies it through four layers (symbolic proof, exhaustive state exploration, deterministic simulation with fault injection, property testing) and then runs it, so "the artifact that gets verified is the artifact that runs". It is the strongest version seen of spec-as-executable, and argues the bottleneck is verification, not generation. For the project it bears on intent-shaping-and-spec and review-and-autonomy, though it targets control logic for infrastructure, not product specs. Datadog's claims, retold by Anthropic; tied to a talk with a live demo not reviewed here.

## Themes
- spec-becomes-prototype-and-evals: "instead of producing application code, agents produce specifications"; the kernel verifies and deploys the system the spec describes, so there is no drift (§Temper).
- agent-control-plane: in the Helix "dark factory", Temper is the agent control plane for Managed Agents sessions (roles, work queues, lifecycle), a tool-builder layer bridging Git/CI/deploy, and the service's control API (§The dark factory for Helix).
- agent-factory-sdlc: path from Courier (built by hand in a year) to BitsEvolve (evolutionary optimisation harness, a "council of models" with benchmark cascades) to Helix (Kafka-comparable service built in days by Claude Code with one human steering) to Temper (§The road to Temper).
- docs-as-code-prd: the transition table is "data, not spaghetti control flow"; agents change it and hot-reload it under policy without CI (§Why not just build a CRUD app?).

## Key points
- **Usage claims.** All Datadog engineers use AI coding tools for production code; Claude Code drives at least two-thirds of that; examples range from bug fixes to replacing MongoDB with Postgres.
- **Role shift.** Nalla: engineers are "shaping the work", deciding what the agent sees, its tools, what success means and how failure is detected, "like everyone's promoted three levels up".
- **Three contracts per capability.** Behaviour (states, transitions, preconditions, safety properties); data contract (entities and actions, machine-parseable so agents discover the API without docs); authorization (default-deny, scope-based, with denials recorded as pending decisions a human can approve and hot-load into the policy engine).
- **Verification cascade.** Symbolic reasoning proves guards satisfiable and invariants inductive; exhaustive state exploration; seeded deterministic simulation with drops, delays, reordering and crashes; about a thousand random action sequences with shrinking to a minimal counterexample; "well under a second" on a small spec.
- **Production reality.** Helix showed 2-5x cost savings in shadowing, but getting it to production "took a lot more mileage" and is still rolling out: building collapsed, coordination and hardening did not.
- **Best practices (box).** Assume verification is the bottleneck; have agents emit specs for control logic and keep compilation and proof outside the LLM; make the state machine explicit; keep each artifact small enough to hold in your head.
- **Limits.** Applies to software shaped like "control logic around database APIs"; no data on failures caught, adoption beyond the Helix team, or the cost of writing specs; the denial-as-pending-decision pattern is the only human-in-loop mechanism described.

## Notable quotes
- "You're no longer writing the code; you're shaping the work." (Sesh Nalla, §The flow problem)
- "The compilation step is outside the LLM, the same way you hand Rust code to the Rust compiler." (Sesh Nalla, §Why not just build a CRUD app?)

## Could not verify
- The full session video and live demo referenced at the end; not watched.
- Whether Temper is public or internal-only.
