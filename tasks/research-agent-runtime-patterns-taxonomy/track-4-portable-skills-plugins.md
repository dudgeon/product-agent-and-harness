# Track 4: Portable skills, subagents and plugin ecosystems

Date: 2026-10-24. Filed by research-agent-runtime-patterns-taxonomy. Pattern class (H) in the plan, plus the packaging axis (4) and harness-coupling axis (3). Not a recommendation: a map of what is portable, what is not, and what we would need to learn.

## Headline findings

1. **The portable core is real but small.** The Agent Skills format (SKILL.md, six frontmatter fields, scripts/references/assets, progressive disclosure at ~100 tokens per skill) is read by Claude Code, Codex, Copilot, Gemini CLI, Cursor and OpenCode, and several honour each other's directories (`.claude/skills`, `.agents/skills`). Sources: [spec](../../research/sources/agentskills-specification.md), [Codex](../../research/sources/openai-codex-skills-docs.md), [Copilot](../../research/sources/github-copilot-agent-skills-docs.md), [Gemini/OpenCode](../../research/sources/gemini-cli-and-opencode-skills-support.md). Vendor docs, so first-party.
2. **Portability of the file is not portability of behaviour.** Claude Code adds 13 extension fields (`context: fork`, `hooks`, `paths`, `model`...) that claude.ai and the Skills API reject outright and other harnesses silently ignore ([Claude skills docs](../../research/sources/anthropic-claude-code-skills-docs.md)). Subagent definitions have no shared spec (Markdown vs Codex TOML, implicit vs explicit delegation) ([subagents](../../research/sources/anthropic-claude-code-subagents-docs.md), [Vaughan](../../research/sources/danielvaughan-codex-vs-claude-code-multi-agent.md), blog). Plugins are per-vendor manifests ([Claude](../../research/sources/anthropic-claude-code-plugins-reference.md), [Cursor](../../research/sources/cursor-plugins-building.md)); Cursor even expands `${CLAUDE_PLUGIN_ROOT}`, i.e. convergence by imitation.
3. **Independent evidence: skills help on average, but triggering is the weak link.** SkillsBench (preprint, 84 tasks, three harnesses): curated skills +16.2pp on average, self-generated skills about -1.3pp, 16 of 84 tasks worse, 2-3 skills better than 4+, and Codex CLI often ignored the skills it was given ([SkillsBench](../../research/sources/arxiv-skillsbench.md)). Vercel's eval (vendor-run): skill never invoked in 56% of cases, so it scored the same as no docs (53%) until the prompt told the agent to use it; an always-on AGENTS.md index scored 100% ([Vercel](../../research/sources/vercel-agents-md-outperforms-skills.md)). Counterweight: an ETH study found AGENTS.md files reduce success and add 20%+ cost ([arXiv](../../research/sources/arxiv-evaluating-agents-md.md)). Claude's own eval tool names "Claude isn't choosing your skill" as the usual first finding ([plugin evals](../../research/sources/anthropic-claude-code-plugin-evals.md)).
4. **Third-party skills are a measured supply-chain risk.** Snyk: 36.8% of 3,984 skills with any issue, 13.4% critical, 76 malicious ([Snyk](../../research/sources/snyk-toxicskills-study.md), vendor); an academic scan of 150k skills across 7 registries confirmed 400 malicious ([MalSkills](../../research/sources/arxiv-malskills.md), independent); a 341-skill ClawHavoc campaign ([report](../../research/sources/thehackernews-clawhavoc-341-malicious-skills.md)); CSA says scanners miss natural-language payloads ([CSA](../../research/sources/csa-skill-md-context-poisoning.md)). Caveat: most incidents are OpenClaw/ClawHub, not Claude Code's curated marketplaces. Anthropic's own doc says a plugin "can execute arbitrary code on your machine" and that hooks, monitors and MCP servers run outside the sandbox ([plugin security](../../research/sources/anthropic-claude-code-plugin-security.md)).
5. **Private registries are appearing, but only as architecture write-ups.** PayPal (2026-10-09): teams author in their own repos, a registry runs fail-closed checks plus human approval and versions each skill, distributing to Claude Desktop and Codex ([PayPal](../../research/sources/paypal-agent-skills-at-enterprise-scale.md)); Ramp's Dojo is the other case (already filed). Anthropic productises the same shape: org marketplace via managed settings, claude.ai/Cowork org sync, per-plugin analytics ([org mgmt](../../research/sources/anthropic-claude-code-plugins-org-management.md), [org sync](../../research/sources/anthropic-claude-org-plugin-sync.md)). Nobody publishes reuse, quality or incident data.
6. **How far can a skill go before it needs a runtime?** With scripts, `context: fork` to a named subagent, skill-scoped hooks, preloaded skills in subagents, plugin MCP servers, background monitors and JS workflows, a Claude Code plugin can carry multi-step, partially deterministic workflows with no server of our own. What it cannot carry: guaranteed triggering, per-user credentials beyond `userConfig`, shared state across users, long-running or unattended execution, uniform audit across harnesses, a sandbox for plugin-run code. OpenAI's own advice is "prefer instructions over scripts unless you need deterministic behavior" ([Codex docs](../../research/sources/openai-codex-skills-docs.md)). The boundary is an inference from these docs; no source tests it directly.

## Comparison table

| Layer | Spec / owner | Portable across | Harness-specific edges | Maturity | Evidence |
|---|---|---|---|---|---|
| SKILL.md core | agentskills.io (Anthropic-originated, "open") | Claude Code, Codex, Copilot, Gemini CLI, Cursor, OpenCode, ChatGPT | triggering behaviour, `allowed-tools` (experimental), script runtime | early-adopter | first-party + independent (SkillsBench) |
| Skill extensions | per vendor | none | `context: fork`, hooks, `agents/openai.yaml` | early-adopter | first-party |
| AGENTS.md | AAIF / Linux Foundation (ex-OpenAI) | ~20 tools listed | Claude Code reads CLAUDE.md (AGENTS.md support not verified) | mainstream | vendor claim; mixed independent evidence |
| Subagent defs | none | none | MD vs TOML; delegation semantics | emerging | first-party + blog |
| Plugins | per vendor (`.claude-plugin`, `.cursor-plugin`, Codex plugins) | partial (skills + MCP only) | hooks, monitors, bin/, LSP, workflows | early-adopter | first-party |
| Registries | skills.sh, ClawHub, Anthropic marketplaces; PayPal/Ramp private | installers translate to per-agent folders | per-vendor admin controls | emerging | vendor claim; independent security audits |
| Eval tooling | `claude plugin eval`, skill-creator, SkillsBench | Claude Code only for vendor tool | no cross-harness runner found | emerging | first-party |

## Trade-offs

- Portable-core-only skills: maximum reach, lowest power (no fork, hooks), and triggering depends on each harness.
- Harness-extended skills and plugins: more complexity, but you are choosing a vendor (and claude.ai rejects some of it).
- Always-on context vs on-demand skill: context files avoid the trigger failure but cost tokens every turn and can hurt; skills scale to many capabilities but may not fire.
- Public registry convenience vs supply-chain risk; private registry removes the risk only if the review is real and plugin code is sandboxed.
- Governance is per vendor today; a skills estate spanning harnesses has no single control plane (none found in this track).

## Options by dimension

Added to [options/DIMENSIONS.md](../../options/DIMENSIONS.md):
- [capability-packaging](../../options/DIMENSIONS.md#capability-packaging-how-skills-and-agents-are-packaged-and-invoked): 7 new options (open-standard skill, harness-extended skill, plugin bundle, subagent definition, always-on context file, private registry, public registries) and key questions 5-9 (portable vs extended, triggering reliability, when a skill is not enough, lifecycle owner, whether cross-harness movement matters).
- [harness-ownership](../../options/DIMENSIONS.md#harness-ownership-who-owns-the-harness-the-agent-loop): option "stay in vendor harnesses, keep assets portable" and key question 6.
- [governance-control-plane](../../options/DIMENSIONS.md#governance-control-plane-permissions-cost-identity-audit): vendor-managed plugin policy, registry-gate, eval-gated skills; key questions 4-6.
- [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-and-what-agent-shape-fits): role/function plugin packs; key question 4 (which job families gain most).
- [adoption-model](../../options/DIMENSIONS.md#adoption-model-adoption-and-enablement-model): decentralised authoring with central trust; key question 3.

Proposed structural changes (director's call): split `capability-packaging` into **capability-format-portability** (skill/subagent/plugin formats, harness coupling) and **capability-distribution-trust** (registries, versioning, scanning, evals, org control); consider a dedicated **skill-trigger-reliability / evaluation** dimension or cross-cutting question, since it bears on skills vs deployed agents vs always-on context. No user/product dimension was added beyond the adoption-model and work-structure entries; "which jobs first" is where SkillsBench's domain variance is relevant.

## Open questions for Geoff (unranked)

- Do our target users move between harnesses, or is portability mainly our own concern?
- Is a skills-only internal marketplace an acceptable trust boundary, or must plugin code (hooks, MCP) be in scope?
- Which one workflow (PRD review?) do we prototype as a portable skill and test in two harnesses?
- Do we have access to Ramp or PayPal people for reuse/quality data on their registries?
- Should Codex/Copilot admin controls and Cowork/Claude Enterprise be trialled (not covered here)?

## Could not verify / gaps

- No independent field reports of enterprise skills registries; PayPal and Ramp are first-party. HN/Reddit threads on real-world skill failures were not located (searches returned blogs only).
- Several sources read via search summaries: Gemini CLI, OpenCode, AAIF press release, Vercel skills, ClawHavoc. Copilot custom-agent (`.agent.md`) format and Codex subagents page not read first-hand. Claude Code reading AGENTS.md not confirmed.
- Number discrepancies noted in source notes (MalSkills 262 vs 400; SkillsBench +16.2 vs +12.66pp).
- Cowork-specific plugin admin and Notion's skill upload/download tools (seen in this environment's tool list) not researched.
