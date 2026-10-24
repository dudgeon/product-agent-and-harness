# PM artifacts: how they are created, stored, found, and how they could be standardized

Filed by user-story-mapping, 2026-10-24. Source notes are in `../../research/sources/`. Evidence labels: FP first-party, IND independent, V vendor-claim, A anecdote.

## 1. Where PM artifacts live today, and why agents struggle to reach them
- Artifacts are spread across docs tools (Notion, Confluence), roadmap/work tools (Linear, Jira), research repositories (Dovetail), analytics/BI (Amplitude, Mixpanel, Looker, Tableau, Snowflake) and local files. The only survey found is ProductPlan's (about 400 PMs, vendor): more teams want to consolidate tools because of standardization, budget and data silos. It gives no tool count or artifact-location data. [productplan-trends-product-management-2025](../../research/sources/productplan-trends-product-management-2025.md) (V)
- Connectivity exists but is uneven:
  - Hosted OAuth MCP servers: Amplitude ([note](../../research/sources/amplitude-mcp-claude-code-docs.md), FP; separate EU endpoint; inherits user permissions), Dovetail ([note](../../research/sources/dovetail-mcp-server-docs.md), FP; read and create, no update/delete tools listed, no OAuth DCR so API-token fallback), Notion ([note](../../research/sources/notion-mcp-developer-docs.md), FP; client allow-listing is Enterprise-only). Mixpanel: see existing [mixpanel-spark-agent-mcp](../../research/sources/mixpanel-spark-agent-mcp.md).
  - Admin-gated or self-run: Snowflake needs an admin to `CREATE MCP SERVER`, build an OAuth integration by hand, and grant each tool separately ([note](../../research/sources/snowflake-managed-mcp-server-docs.md), FP). Looker goes through a self-run MCP Toolbox with client ID/secret ([note](../../research/sources/google-looker-mcp-toolbox-docs.md), FP, via search summary).
- Recurring friction: per-user OAuth per tool, no dynamic client registration (the MCP spec says DCR is a SHOULD; see [mcp-authorization-spec-draft](../../research/sources/mcp-authorization-spec-draft.md)), regional endpoints, admin prerequisites, tools-only servers (Snowflake supports no resources), response truncation (250 KB). Permissions generally mirror the signed-in user, so the agent sees what the PM sees, which is also the safe default.
- Net: reach is mostly achievable per tool; there is no common way to ask "what artifacts exist for project X" across them.

## 2. PRD-in-repo / docs-as-code: how consistent is it?
- Spec-driven development tools put specs in git, but not in the same shape:
  - Spec Kit: `specs/NNN-feature/{spec,plan,tasks,research,data-model}.md`, `contracts/`, and `memory/constitution.md` ([note](../../research/sources/github-spec-kit-sdd.md), FP).
  - Kiro: `requirements.md` (or `bugfix.md`), `design.md`, `tasks.md`, plus steering files ([note](../../research/sources/kiro-specs-docs.md), FP).
  - Tessl: `*.spec.md` mapped to code files (via Böckeler only).
- The best independent evidence is Böckeler on martinfowler.com ([note](../../research/sources/fowler-bockeler-sdd-kiro-speckit-tessl.md), IND). All tools are spec-first, few are spec-anchored, none are mature at spec-as-source. Specs behave like change requests (spec-kit makes a branch per spec). Review burden is high and agents ignore specs. It is unclear whether SDD is for developers or product people. These specs are developer-feature specs, not PM artifacts (research, strategy, roadmap).
- PM-side evidence is anecdotal or vendor-made: Lenny's episode on PRDs in Cursor with source control ([note](../../research/sources/lenny-cursor-better-product-manager.md), A), and vendor guides that recommend a rules file or AGENTS.md pointing at a PRD template path (not fetched, V). Conclusion: docs-as-code for PRDs is a visible trend among AI-forward PMs, but no layout is common and there is no evidence on adoption share, review, or permissions in git for non-engineers.
- Established in-repo precedents with real adoption: ADR/MADR ([note](../../research/sources/adr-madr-template.md), FP) and Gherkin ([note](../../research/sources/cucumber-gherkin-reference.md), FP).

## 3. How "project" is defined
- No cross-tool definition. Linear: initiative (strategic objective, can nest) > project (time-bound work stream) > issue, with documents attached as resources ([note](../../research/sources/linear-initiatives-docs.md), FP). Backstage: Domain > System > Component ([note](../../research/sources/backstage-descriptor-format.md), FP). SDD tools: the unit is the feature folder. ADR: the unit is the decision.
- Search for Pragmatic/Product-Ops taxonomy writing returned no first-party Pragmatic source; other sources define product line, family, group and portfolio inconsistently, and initiatives as sitting above features at company, line or product level. Treat "project" as a local convention.

## 4. Menu of standardization methods
| Method | Standardizes | Example | Maturity | Note |
|---|---|---|---|---|
| Entity manifest (envelope + kind) | identity, owner, lifecycle, relations | Backstage catalog-info.yaml | Mature, CNCF | [backstage](../../research/sources/backstage-descriptor-format.md) |
| Typed doc template + status frontmatter | one artifact type, file location, naming, lifecycle | MADR in `docs/decisions/` | Mature | [madr](../../research/sources/adr-madr-template.md) |
| Doc-type taxonomy | artifact types by reader need | Diátaxis (4 types) | Mature for tech docs | [diataxis](../../research/sources/diataxis-framework.md) |
| Behaviour-example syntax | acceptance criteria | Gherkin `.feature` | Mature | [gherkin](../../research/sources/cucumber-gherkin-reference.md) |
| Feature-spec folders | spec/plan/tasks per feature | Spec Kit, Kiro | Young, divergent | [speckit](../../research/sources/github-spec-kit-sdd.md), [kiro](../../research/sources/kiro-specs-docs.md) |
| Agent context files | repo-level instructions | AGENTS.md | Wide adoption claimed | existing [agentsmd](../../research/sources/agentsmd-agents-md.md) |
| Skill packaging | name, description, metadata, progressive disclosure | Agent Skills `SKILL.md` | Young, multi-vendor | existing [agentskills](../../research/sources/agentskills-specification.md) |
| Protocol resources | uri, mimeType, title, audience, priority, lastModified, subscribe | MCP resources | Spec stable, under-implemented | [mcp resources](../../research/sources/mcp-spec-resources.md) |
| Agent-to-agent artifacts | task outputs between agents | A2A | Young | existing [a2a spec](../../research/sources/a2a-project-specification-v1.md) |
| Auth and permissions | who may read | MCP OAuth 2.1, per-tool RBAC | Spec mature, vendor support uneven | [mcp auth](../../research/sources/mcp-authorization-spec-draft.md), [snowflake](../../research/sources/snowflake-managed-mcp-server-docs.md) |
| Provenance | who or what produced, from what | W3C PROV, C2PA | PROV a 2013 Recommendation; C2PA media-focused | [prov](../../research/sources/w3c-prov-overview.md), [c2pa](../../research/sources/c2pa-explainer.md) |

Observation (my inference): no existing method covers "project containing typed PM artifacts with owner, status, version and provenance". The nearest compositions are Backstage envelope + MADR-style frontmatter, exposed through MCP resources; versioning is delegated to git (or tool history) and MCP resources carry only `lastModified`.

## 5. What's unverified
- Any average PM tool count or share of PMs keeping artifacts in git.
- Mixpanel official docs (only directory listings), Tableau MCP official repo, Atlassian Rovo MCP details (page truncated), Looker-managed MCP server.
- C2PA and PROV content came from search summaries; PROV-DM and in-toto/attestations not read.
- Pragmatic Institute's own taxonomy; Product-Ops writing.
- Kiro storage path and EARS use; Tessl first-party docs; the Fowler article date (October 2025 per snippet).
- Whether the 2026-07-28 MCP revision changes resources.
- Vendor PRD-in-Cursor guides (Builder.io, ChatPRD, Humanx, Alloy) were seen only as search snippets.
