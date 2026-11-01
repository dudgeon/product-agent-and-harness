## sdd-input-contracts: What spec-driven toolchains consume
The file layout, required sections, requirement notation, constraint and dependency slots that each spec-driven development tool reads as its input. It matters because the intent-shaping and dependency-mapping modules aim to produce output these tools consume without translation, and the tools differ more in where they put constraints, standing rules and outside dependencies than in how they write a requirement.
- [EARS: The Easy Approach to Requirements Syntax](sources/alistairmavin-ears.md): five clause patterns with one system name and "shall"; the notation Kiro's requirements use (research-sdd-ready-intent)
- [spec-kit templates and commands](sources/github-spec-kit-templates.md): FR-001 "System MUST", SC-001 success criteria, Given/When/Then per prioritised story, Assumptions as the slot for dependencies on existing systems, "Blocking Prerequisites" phase in tasks (research-sdd-ready-intent)
- [OpenSpec docs: Concepts, Writing Good Specs, Customization, Agent contract](sources/openspec-docs-concepts.md): "one statement, one SHALL/MUST" with named GIVEN/WHEN/THEN scenarios; external constraints belong in the spec; `config.yaml` context and per-artifact rules (research-sdd-ready-intent)
- [Stores: Plan in Its Own Repo](sources/openspec-docs-stores-beta.md): a planning-only repo that code repos reference read-only, with an index of upstream specs injected into the agent's instructions (research-sdd-ready-intent)
- [BMAD-METHOD prd-tmpl.yaml (v4.44.3)](sources/bmad-v4-prd-template.md): FR and NFR as two numbered lists; story acceptance criteria told to carry critical NFRs (research-sdd-ready-intent)
- [Specs (Kiro docs)](sources/kiro-specs-docs.md): requirements.md in EARS, `.kiro/specs/<feature>/`, import from trackers and wikis over MCP, a central specs repo across teams, correctness properties from requirements (research-sdd-ready-intent)
- [Using PLANS.md for multi-hour problem solving](sources/openai-cookbook-codex-exec-plans.md): self-contained prose plan with Validation and Acceptance and Interfaces and Dependencies sections; no requirement IDs or blocked state (research-sdd-ready-intent)
- [Steering (Kiro docs)](sources/kiro-steering-docs.md): product, tech and structure files with inclusion modes; the standing-rules slot beside per-feature specs (research-sdd-ready-intent)
- [AGENTS.md](sources/agentsmd-agents-md.md): one plain-Markdown always-on file read by many coding agents; no schema (research-sdd-ready-intent)
- [Evaluating AGENTS.md](sources/arxiv-evaluating-agents-md.md): context files lowered task success and raised cost; argues for minimal standing rules (research-sdd-ready-intent)

## agent-ready-intent: A shared standard for agent-ready specs
- [spec-kit templates and commands](sources/github-spec-kit-templates.md): the clarify command's coverage taxonomy includes "Compliance / regulatory constraints" and "Integration & External Dependencies"; the checklist command tests requirements as "Unit Tests for English" (research-sdd-ready-intent)
- [OpenSpec docs: Concepts, Writing Good Specs, Customization, Agent contract](sources/openspec-docs-concepts.md): "A spec is a behavior contract, not an implementation plan"; lite and full rigour, full for security, privacy and cross-team changes (research-sdd-ready-intent)

## requirements-partitions: How requirements are partitioned, and why every single-axis partition leaks
- [EARS: The Easy Approach to Requirements Syntax](sources/alistairmavin-ears.md): its patterns sort requirements by behaviour type, which aligns with an attribute axis, not a source axis (research-sdd-ready-intent)
- [BMAD-METHOD prd-tmpl.yaml (v4.44.3)](sources/bmad-v4-prd-template.md): the functional versus non-functional split is the only partition any spec-driven template keeps (research-sdd-ready-intent)

## docs-as-code-prd: PRDs and specs as files in the repo
- [Stores: Plan in Its Own Repo](sources/openspec-docs-stores-beta.md): planning in its own repo, consumed by code repos by reference: "The wiki version drifts, and your coding agent can't read it anyway" (research-sdd-ready-intent)

## dependency-types-and-practices: What a dependency is and how large organisations manage dependencies today
- [spec-kit templates and commands](sources/github-spec-kit-templates.md): the only dependency vocabulary is between tasks ("depends on T012") and phases ("BLOCKS all user stories"); dependencies on outside teams have no slot beyond Assumptions (research-sdd-ready-intent)

## handoff-context-transfer: What crosses a handoff
- [Stores: Plan in Its Own Repo](sources/openspec-docs-stores-beta.md): each code repo opens a small local change that cites the shared contract; branches linked in pull-request descriptions (research-sdd-ready-intent)
