# Theme evidence: user-story-mapping

Written only by the task `user-story-mapping`. Built into ../THEMES.md by ../build.py.

## agent-ready-intent: A shared standard for agent-ready specs
- [What is an idea (Jira Product Discovery docs)](sources/atlassian-jira-product-discovery-ideas.md): an idea is the basic unit; custom idea types (user problem, customer, bet, opportunity, solution), each with its own workflow. (user-story-mapping)
- [Documents (Linear docs)](sources/linear-docs-documents.md): documents can be referenced from issue descriptions, comments and agent guidance fields via @mention. (user-story-mapping)
- [Connect a coding agent to Spark via MCP (Productboard support)](sources/productboard-mcp-server-spark.md): specs live in a Specification tab on initiatives, features and subfeatures; Spark's 'Write spec' skill drafts them; agents read, edit, comment and update status. (user-story-mapping)
- [github/spec-kit (README)](sources/github-spec-kit-readme.md): a standard command set and Markdown artifacts per stage; constitution is the project-level baseline. (user-story-mapping)
- [Spec-Driven Development (spec-kit spec-driven.md)](sources/github-spec-kit-spec-driven.md): spec.md has user stories and acceptance criteria, ambiguity marked [NEEDS CLARIFICATION] instead of guessed; templates act as structured prompts with self-review checklists. (user-story-mapping)

- [Check acceptance criteria in a code review](sources/atlassian-rovo-dev-acceptance-criteria-code-review.md): named fields (AC, Requirements, Definition of Done) are the machine-checked contract; empty description means no check (user-story-mapping)
- [Introducing Jira Planner](sources/atlassian-blog-introducing-jira-planner.md): rough idea to agent-ready spec in a Confluence Live Doc (user-story-mapping)
- [Record for AI agents (Loom)](sources/atlassian-loom-record-for-agent.md): each prompt task has title, bullets, transcript quote, keyframes, timestamps (user-story-mapping)
## compounding-context-repo: Context that compounds with each shipped feature
- [github/spec-kit (README)](sources/github-spec-kit-readme.md): state kept under .specify/ (memory, bugs/<slug>/, assessments/<slug>/ with decision.md). (user-story-mapping)
- [How Claude remembers your project (Claude Code docs)](sources/anthropic-claude-code-memory-docs.md): the hierarchy managed policy > user > project > local lets org, team and personal context layer. (user-story-mapping)

- [Using the Ops Expert agent](sources/atlassian-rovo-ops-expert-agent.md): past PIRs are summarised for new incidents (user-story-mapping)
## memory-architecture: Memory as inspectable files from an offline pipeline
- [How Claude remembers your project (Claude Code docs)](sources/anthropic-claude-code-memory-docs.md): CLAUDE.md (human-written instructions) vs auto memory (Claude-written learnings; first 200 lines or 25KB loaded each session). (user-story-mapping)
- [Organize work with projects (Claude Cowork docs)](sources/anthropic-cowork-projects-docs.md): a dedicated project-scoped memory store persisting across sessions; archiving deletes metadata including memory but not local files. (user-story-mapping)

## legible-org-for-agents: Make the organisation legible to agents
- [Descriptor Format of Catalog Entities (Backstage)](sources/backstage-descriptor-format.md): annotations link entities to external systems; owner field is for display, not authorization. (user-story-mapping)
- [Teamwork Graph glossary (Atlassian developer docs)](sources/atlassian-teamwork-graph-glossary.md): the graph is explicitly the layer that links work data across Atlassian apps and connected external tools (Core concepts, 'Teamwork Graph'). (user-story-mapping)
- [Teamwork Graph object types (Atlassian developer docs)](sources/atlassian-teamwork-graph-object-types.md): a fixed set of connector object types lets Rovo Search/Chat treat Asana tasks, Figma files and Google events uniformly. (user-story-mapping)
- [Atlassian Rovo MCP server: supported tools](sources/atlassian-rovo-mcp-server-supported-tools.md): agents can read work items, projects, boards, sprints, pages, whiteboards, databases, goals and projects. (user-story-mapping)
- [What is a Jira space (formerly project)](sources/atlassian-jira-space-definition.md): 'A Jira space is a collection of related work items' for a product, team, service or project; items carry a space key prefix (e.g. GDT-1). (user-story-mapping)
- [Working with databases (Notion API docs)](sources/notion-api-databases-data-sources.md): schema lives on the data source so an agent can read property types. (user-story-mapping)
- [Projects (Linear docs)](sources/linear-docs-projects.md): Project = 'a grouping of issues that have a clear outcome or planned completion date'. (user-story-mapping)
- [Initiatives (Linear docs)](sources/linear-docs-initiatives.md): Initiatives are workspace-level containers for projects tied to a shared objective; IDs like I-<n>. (user-story-mapping)
- [Documents (Linear docs)](sources/linear-docs-documents.md): Documents attach to projects, initiatives, teams, issues or cycles; same editor as issues; realtime collaboration; version history including agent edits; templates at workspace/team level. (user-story-mapping)
- [About Projects (GitHub Docs)](sources/github-docs-about-projects.md): Project = adaptable table, board and roadmap integrating issues and PRs, at user or organisation level; two-way sync with issues. (user-story-mapping)
- [Glean Enterprise Graph (product page)](sources/glean-enterprise-graph-product-page.md): entities are inferred automatically by machine learning rather than declared. (user-story-mapping)
- [Atlassian Rovo MCP server: supported tools](sources/atlassian-rovo-mcp-server-supported-tools.md): verbatim re-read: getTeamworkGraphContext returns 'all relationships and linked objects in one traversal' from Jira, Confluence, Goals/Projects/Focus Areas, people, DevOps, Loom, Compass entry points; Confluence spaces carry agent-readable 'space instructions' (getConfluenceSpaceInstructions / setConfluenceSpaceInstructions). (user-story-mapping)
- [Scopes (Teamwork Graph API)](sources/atlassian-teamwork-graph-scopes.md): 'All Teamwork Graph API scopes are read-only'; a missing scope returns success and empty rows ('fails closed rather than leaking data'), so an agent cannot tell 'no data' from 'no permission'. (user-story-mapping)

- [Work with Jira Delivery agent](sources/atlassian-rovo-jira-delivery-agent.md): documented TWG work-item context returns related PRs, commits, branches, pages and hierarchy; user summary returns work items, pages, PRs, Loom videos, projects and goals (user-story-mapping)
- [How we're evolving Jira for AI-native software development](sources/atlassian-blog-jira-ai-native-software-development.md): 'the SDLC needs to become legible to agents without becoming less accountable to humans' (user-story-mapping)
## prd-agents: PRD and spec writing/review as an agent job
- [Spec Kit and spec-driven.md (GitHub)](sources/github-spec-kit-sdd.md): templates force `[NEEDS CLARIFICATION: ...]` markers instead of guessing, a spec-quality convention. (user-story-mapping)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](sources/fowler-bockeler-sdd-kiro-speckit-tessl.md): unclear target user (developers, product people, or both); Kiro turned a small bug into 4 stories / 16 acceptance criteria. (user-story-mapping)
- [Connect a coding agent to Spark via MCP (Productboard support)](sources/productboard-mcp-server-spark.md): Beta, included with Spark-enabled workspaces at no extra cost; admins enable it under Settings > MCP Server and choose roles. (user-story-mapping)

- [Introducing Jira Planner](sources/atlassian-blog-introducing-jira-planner.md): spec published as an editable, co-edited Confluence Live Doc linked to Jira (user-story-mapping)
## vendor-claims-vs-independent-evidence: Vendor claims dominate; independent evidence is rare
- [Trends Shaping Product Management in 2025 (ProductPlan)](sources/productplan-trends-product-management-2025.md): vendor-run survey of nearly 400 product professionals; survey dates and exact percentages for consolidation not given. 92% 'somewhere on AI journey', 46% adopted for at least one use case. (user-story-mapping)

- [RovoDev Code Reviewer (ICSE 2026)](sources/arxiv-rovodev-code-reviewer-icse26.md): peer-reviewed but all-Atlassian authors: PR cycle time -30.8%; a separate Atlassian blog claims -45%, unreconciled (user-story-mapping)
- [How we're evolving Jira for AI-native software development](sources/atlassian-blog-jira-ai-native-software-development.md): '44% more accurate results while using 48% fewer tokens' with Teamwork Graph, no method (user-story-mapping)
- [Rovo Dev in Jira launch blog](sources/atlassian-blog-rovo-dev-in-jira.md): feature-flag cleanup 'around 85%' faster; 29 of 31 PRs needed no manual changes (user-story-mapping)
## feedback-triage-agents: Feedback and research triage/synthesis as an agent job
- [Add features to your hierarchy (Productboard support)](sources/productboard-product-hierarchy.md): feature has an Insights tab for linked insights; notes land in an inbox (web-search summary of a 2019 post, unverified here). (user-story-mapping)

- [Record for AI agents (Loom)](sources/atlassian-loom-record-for-agent.md): related Loom AI workflow turns a recording into a bug report work item in Jira or Linear (user-story-mapping)
- [Make Rovo your research assistant - Deep research mode](sources/atlassian-rovo-deep-research.md): blog names customer-feedback analysis as a use case (user-story-mapping)
## spec-becomes-prototype-and-evals: The spec is replaced by prototype plus evals
- [github/spec-kit (README)](sources/github-spec-kit-readme.md): Workflow: /speckit-constitution (once per project), then per feature /speckit-specify, -plan, -tasks, -implement, -converge. Runs as skills in the agent's chat. (user-story-mapping)
- [Spec-Driven Development (spec-kit spec-driven.md)](sources/github-spec-kit-spec-driven.md): contrast; here the spec stays primary and code is regenerated. (user-story-mapping)

## research-synthesis-agents: Research synthesis agents
- [Build on Dovetail (docs)](sources/dovetail-build-on-dovetail.md): MCP can read workspace content and create projects, docs, data, highlights and channel data. (user-story-mapping)

- [Make Rovo your research assistant - Deep research mode](sources/atlassian-rovo-deep-research.md): planned multi-step report over org and connected sources with sources list; Confluence export claimed only in a 2025 blog (user-story-mapping)
## org-context-grounding: Agents work when grounded in organisation context
- [Teamwork Graph glossary (Atlassian developer docs)](sources/atlassian-teamwork-graph-glossary.md): ACLs are specified per object that a connector adds, so permissions travel with the object. (user-story-mapping)
- [What are projects? (Claude Help Center)](sources/anthropic-claude-projects-support.md): uploaded knowledge is the grounding, switching to RAG on paid plans when nearing context limits (up to 10x capacity per the page). (user-story-mapping)
- [Organize work with projects (Claude Cowork docs)](sources/anthropic-cowork-projects-docs.md): Project holds: description (Dispatch reads it to choose a project for a task), folders (one or more local), instructions, links, linked Chat projects, memory. (user-story-mapping)
- [Glean Enterprise Graph (product page)](sources/glean-enterprise-graph-product-page.md): graph of high-value entities (projects, people, customers, products) linked to docs, tickets and specs; permissions-enforced via connectors. (user-story-mapping)

- [View and manage agents in your Jira space](sources/atlassian-jira-manage-agents-in-space.md): per-space agent Sources (Confluence pages, Loom recordings) and instructions (user-story-mapping)
- [Using the Ops Expert agent](sources/atlassian-rovo-ops-expert-agent.md): incident triage grounded in runbooks, past incidents, Slack history (user-story-mapping)
## agent-failure-modes: Recurring agent failure modes in PM work
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](sources/fowler-bockeler-sdd-kiro-speckit-tessl.md): spec-kit ignored research notes and duplicated existing classes; over-applied constitution; Tessl regeneration non-deterministic. (user-story-mapping)

## human-review-gates: Human review gates on agent output
- [Atlassian Rovo MCP server: supported tools](sources/atlassian-rovo-mcp-server-supported-tools.md): delete and project-management tools are disabled by default and need an admin to enable. (user-story-mapping)
- [Atlassian Rovo MCP server: supported tools](sources/atlassian-rovo-mcp-server-supported-tools.md): confirmed verbatim: delete_jira and manage_jira are disabled by default; executeDestructive is a separate pathway 'used to apply agent-level confirmation'; updateJiraScreen 'Returns a plan by default; changes are applied only with an explicit commit'. (user-story-mapping)
- [DACI decision template (Confluence)](sources/atlassian-confluence-daci-decision-template.md): decision pages name a Driver and 'a single approver who ultimately makes the call'. (user-story-mapping)

- [Generate code from a work item in Jira (Jira Coding Agent)](sources/atlassian-jira-coding-agent-generate-code.md): always a draft PR; 'It doesn't merge pull requests' (user-story-mapping)
- [Using Jira for agentic engineering](sources/atlassian-jira-agentic-engineering-guide.md): a review status holds the transition to done until a human approves and CI passes (user-story-mapping)
- [RovoDev Code Reviewer (ICSE 2026)](sources/arxiv-rovodev-code-reviewer-icse26.md): reviewer posts comments only; humans accept or decline (user-story-mapping)
## harness-portability: Harness portability
- [Teamwork Graph object types (Atlassian developer docs)](sources/atlassian-teamwork-graph-object-types.md): external tools are mapped into the vendor's types rather than exposed natively. (user-story-mapping)
- [Getting started with the Atlassian Rovo MCP server](sources/atlassian-rovo-mcp-server-getting-started.md): any MCP-compatible client can connect; setup guides for Claude Code, Claude Desktop, Cursor, Codex, VS Code/Copilot, Windsurf. (user-story-mapping)
- [Notion MCP supported tools](sources/notion-mcp-supported-tools.md): companion overview page says it is a hosted remote MCP using OAuth, with Claude Code, Cursor, Codex as examples; Enterprise plan needed to restrict which clients members may connect. (user-story-mapping)
- [Linear for Agents (developer docs)](sources/linear-developers-agents.md): Agents can be @mentioned, assigned issues, comment, and collaborate on projects and documents; installed agents are not billable users. (user-story-mapping)
- [Connect a coding agent to Spark via MCP (Productboard support)](sources/productboard-mcp-server-spark.md): documented for Claude Cowork, Claude Code, Cursor; remote MCP at mcp.productboard.com, browser sign-in, agent sees only what the user can see. (user-story-mapping)
- [Build on Dovetail (docs)](sources/dovetail-build-on-dovetail.md): Three options: MCP server, REST API (default 200 requests/min per workspace), CLI 'dt' for bulk import from Notion, Confluence, Google Drive and files (no sync after import). (user-story-mapping)
- [How Claude remembers your project (Claude Code docs)](sources/anthropic-claude-code-memory-docs.md): Claude reads AGENTS.md when no CLAUDE.md exists in or above the working directory (v2.1.277+); otherwise CLAUDE.md wins, and a CLAUDE.md can @import AGENTS.md. (user-story-mapping)

- [Open a Jira work item in an AI coding tool](sources/atlassian-jira-open-work-item-in-coding-tool.md): Codex, Cursor, Copilot, VS Code, Claude Code, Rovo CLI (user-story-mapping)
- [Record for AI agents (Loom)](sources/atlassian-loom-record-for-agent.md): 'Send to agent' pre-fills Rovo, Claude or a copied markdown prompt (user-story-mapping)
## shared-persistent-sessions: Shared, persistent, multi-user agent sessions
- [Notion MCP supported tools](sources/notion-mcp-supported-tools.md): notion-spawn-session, wait-session, send-message-to-session, read-session-event let an outside agent start and observe Custom Agent sessions. (user-story-mapping)
- [Linear for Agents (developer docs)](sources/linear-developers-agents.md): agent sessions start automatically on mention or delegation; webhook expects a thought activity within 10 seconds. (user-story-mapping)
- [What are projects? (Claude Help Center)](sources/anthropic-claude-projects-support.md): 'Can view' vs 'Can edit' sharing for Team/Enterprise. (user-story-mapping)
- [Organize work with projects (Claude Cowork docs)](sources/anthropic-cowork-projects-docs.md): projects live on the computer only, not synced or shared; claude.ai projects are shareable on Team/Enterprise and can be linked, not merged. (user-story-mapping)
- [Why We Built Our Own Background Agent (Ramp Builders)](sources/ramp-builders-why-we-built-our-own-background-agent.md): 'Send your session to any colleague, and they can help take it home.'; each session has its own SQLite database; PRs are opened with the user's GitHub token so authors cannot self-approve agent changes. (user-story-mapping)

## identity-delegation: Identity and delegation (on-behalf-of)
- [Amplitude MCP in Claude Code (Amplitude docs)](sources/amplitude-mcp-claude-code-docs.md): server inherits the authenticating user's Amplitude permissions and grants nothing extra. (user-story-mapping)
- [Dovetail MCP (Dovetail developer docs)](sources/dovetail-mcp-server-docs.md): access matches the user's own account/role (from search summary of the main Dovetail help page). (user-story-mapping)
- [Snowflake-managed MCP server (Snowflake docs)](sources/snowflake-managed-mcp-server-docs.md): 'Access to the MCP Server does not give access to the tools'; each tool needs its own grant; users sign in with own credentials. (user-story-mapping)
- [Notion MCP (Notion developer docs)](sources/notion-mcp-developer-docs.md): workspace owners manage allowed MCP clients in Settings; restricting clients requires Enterprise; org owners can list/revoke members' connections via Admin API. (user-story-mapping)
- [Getting started with the Atlassian Rovo MCP server](sources/atlassian-rovo-mcp-server-getting-started.md): OAuth 2.1 primary; actions respect each user's existing access controls; API token optional. (user-story-mapping)
- [Linear for Agents (developer docs)](sources/linear-developers-agents.md): assigning an issue to an agent sets it as delegate; the human stays assignee. (user-story-mapping)
- [What are Confluence's roles?](sources/atlassian-confluence-roles-space-permissions.md): role-based space access (Admin, Manager, Collaborator, Viewer, custom); public links, guest access and anonymous access are separate admin grants; 'you can't assign or remove roles that include permissions you don't have.' (user-story-mapping)
- [Add or remove page restrictions (Confluence)](sources/atlassian-confluence-page-restrictions.md): per-item states open / edit-restricted / restricted / restricted-by-parent; view restrictions inherit to children, edit restrictions do not; the Rovo MCP server can read and set these states. (user-story-mapping)

- [Generate code from a work item in Jira (Jira Coding Agent)](sources/atlassian-jira-coding-agent-generate-code.md): acts as the initiating user, who is PR and commit author; automations run as the connection owner (user-story-mapping)
- [View and manage agents in your Jira space](sources/atlassian-jira-manage-agents-in-space.md): agents run on their own account (needs a space role) or the triggering user's account (user-story-mapping)
## skill-standards: Skill standards
- [Notion MCP supported tools](sources/notion-mcp-supported-tools.md): tools to convert a page to a Skill, upload/download Skills; enabled-skill lists capped at 30; uploads up to 20 MiB compressed / 1,000 files. (user-story-mapping)

## work-structure-spectrum: Work structure spectrum (unstructured exploration to task-specific workflow)
- [What is a Jira space (formerly project)](sources/atlassian-jira-space-definition.md): team-managed (each team controls its own config) vs company-managed (admin-standardised) is a built-in structured-vs-flexible dial. (user-story-mapping)
- [What is a Confluence space](sources/atlassian-confluence-space-definition.md): a space is a loose knowledge container (knowledge base, launch or campaign space) with no enforced artifact types. (user-story-mapping)
- [What is an idea (Jira Product Discovery docs)](sources/atlassian-jira-product-discovery-ideas.md): connection fields (Premium) link ideas without imposing a fixed hierarchy. (user-story-mapping)
- [Working with databases (Notion API docs)](sources/notion-api-databases-data-sources.md): databases give typed structure, pages give free-form body, in the same object. (user-story-mapping)
- [Projects (Linear docs)](sources/linear-docs-projects.md): strong opinionated structure (one issue in one project; lead team sets statuses). (user-story-mapping)
- [Initiatives (Linear docs)](sources/linear-docs-initiatives.md): initiative > project > issue, with team-led sub-initiatives rolling up to company goals. (user-story-mapping)
- [Add features to your hierarchy (Productboard support)](sources/productboard-product-hierarchy.md): Hierarchy: Product > Component > Feature > Subfeature. Features can be imported from spreadsheet, Jira or Zapier. (user-story-mapping)
- [About Projects (GitHub Docs)](sources/github-docs-about-projects.md): items are issues, PRs or draft issues with up to 50 custom fields; table, board and roadmap views. (user-story-mapping)

## artifact-standardization: Artifact standardization
Conventions, manifests and protocol primitives that make artifacts typed, discoverable and attributable (file layouts, frontmatter, MCP resources, provenance).
- [Spec Kit and spec-driven.md (GitHub)](sources/github-spec-kit-sdd.md): defines a per-feature folder (`specs/003-chat-system/`) with spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md plus `memory/constitution.md` (spec-driven.md). (user-story-mapping)
- [Specs (Kiro docs)](sources/kiro-specs-docs.md): three-file spec per feature with three phases (requirements/bug analysis, design, tasks); Spec Kit uses a different file set for the same job. (user-story-mapping)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](sources/fowler-bockeler-sdd-kiro-speckit-tessl.md): three different layouts (Kiro steering + per-feature folders; spec-kit constitution + numbered folders of ~8 files; Tessl `.tessl/framework` plus `*.spec.md`). Memory-bank files (AGENTS.md) distinguished from task specs. (user-story-mapping)
- [Resources (MCP specification 2025-06-18)](sources/mcp-spec-resources.md): resource = uri, name, title, description, mimeType, size, plus annotations `audience` [user|assistant], `priority` 0-1, `lastModified` ISO-8601; resource templates via RFC 6570 URI templates; `resources/list`, `resources/read`, `r (user-story-mapping)
- [Snowflake-managed MCP server (Snowflake docs)](sources/snowflake-managed-mcp-server-docs.md): supports only tool capabilities, not MCP resources or prompts; response truncation at 250 KB; max 50 tools; recursion depth 10. (user-story-mapping)
- [Descriptor Format of Catalog Entities (Backstage)](sources/backstage-descriptor-format.md): Kubernetes-style envelope (`apiVersion`, `kind`, `metadata` name/title/description/tags/links/labels/annotations, `spec`); relations are generated, not hand-written. (user-story-mapping)
- [Descriptor Format of Catalog Entities (Backstage)](sources/backstage-descriptor-format.md): required fields include `spec.owner` and `spec.lifecycle` (experimental, production, deprecated, extensible); System groups components, Domain groups systems (a built-in grouping hierarchy). (user-story-mapping)
- [MADR: Markdown Architectural Decision Records](sources/adr-madr-template.md): location `docs/decisions/`, name `NNNN-title-with-dashes.md`; frontmatter `status` (proposed, accepted, rejected, deprecated, superseded), `date`, `decision-makers`, `consulted`, `informed`. (user-story-mapping)
- [Diátaxis: a systematic approach to technical documentation](sources/diataxis-framework.md): four types matched to user needs; organises content, style and architecture; the site claims adoption in hundreds of projects (vendor/self-reported). (user-story-mapping)
- [Gherkin Reference (Cucumber)](sources/cucumber-gherkin-reference.md): one Feature per `.feature` file; keywords Feature, Rule, Example/Scenario, Given/When/Then, Background, Scenario Outline; examples double as tests via step definitions. (user-story-mapping)
- [PROV-Overview (W3C)](sources/w3c-prov-overview.md): provenance defined as information about entities, activities and people producing a thing; PROV-DM conceptual model with PROV-O/N/XML serialisations. (user-story-mapping)
- [C2PA and Content Credentials Explainer](sources/c2pa-explainer.md): assertions are grouped into a signed claim, bundled into a manifest bound to the asset by hash; each edit adds a manifest referencing the previous one. (user-story-mapping)
- [PRD template (Confluence)](sources/atlassian-confluence-prd-template.md): named sections: basics and roles, objective, success metrics, assumptions, options (requirement, user story, importance, Jira issues), supporting docs, open questions with answer date, out of scope. (user-story-mapping)
- [Project poster template (Confluence)](sources/atlassian-confluence-project-poster-template.md): Team Playbook project poster: problem space, what we know vs still need to answer, solution and scope, reference links; a living page upstream of the PRD. (user-story-mapping)
- [DACI decision template (Confluence)](sources/atlassian-confluence-daci-decision-template.md): decision record fields: status, impact, DACI roles, due date, background, options with pros/cons/cost, action items, outcome. (user-story-mapping)

## docs-as-code-prd: PRDs and specs as files in the repo
Whether product specs live as markdown in git and how consistent that practice is.
- [Spec Kit and spec-driven.md (GitHub)](sources/github-spec-kit-sdd.md): spec is declared the source of truth ('Specifications don't serve code' is the doc's own framing); lives in git, one branch per feature. (user-story-mapping)
- [Specs (Kiro docs)](sources/kiro-specs-docs.md): specs are plain markdown files the agent keeps updated (task status); storage path not stated on the page fetched. (user-story-mapping)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](sources/fowler-bockeler-sdd-kiro-speckit-tessl.md): three levels (spec-first, spec-anchored, spec-as-source); all tools are spec-first, few commit to spec-anchored; spec-kit creates a branch per spec so specs behave like change requests. (user-story-mapping)
- [MADR: Markdown Architectural Decision Records](sources/adr-madr-template.md): sections Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome (Consequences, Confirmation), Pros/Cons; versioned with code. (user-story-mapping)
- [Cursor is a much better product manager (Lenny's Newsletter)](sources/lenny-cursor-better-product-manager.md): blurb lists 'Why source-controlled markdown files might replace traditional SaaS tools' and a chapter on creating PRDs in Cursor with source control (anecdote; no detail). (user-story-mapping)

## pm-tool-connectivity: Reaching PM tools from agents
MCP/auth/permission reality of getting agents into analytics, research and docs tools, plus tool-sprawl evidence.
- [Resources (MCP specification 2025-06-18)](sources/mcp-spec-resources.md): spec says resources are application-driven (host decides how to include context) and access controls SHOULD be implemented; Snowflake's managed server supports tools only (see snowflake note), showing resources are not universally (user-story-mapping)
- [Amplitude MCP in Claude Code (Amplitude docs)](sources/amplitude-mcp-claude-code-docs.md): `claude mcp add -t http -s user Amplitude https://mcp.amplitude.com/mcp`, then OAuth via /mcp; EU customers use a different URL and must re-run and re-authenticate to switch. (user-story-mapping)
- [Dovetail MCP (Dovetail developer docs)](sources/dovetail-mcp-server-docs.md): hosted endpoint https://dovetail.com/api/mcp; OAuth 2.1 with protected-resource metadata, or Bearer API token; DCR and CIMD unsupported so some clients must use tokens. (user-story-mapping)
- [Dovetail MCP (Dovetail developer docs)](sources/dovetail-mcp-server-docs.md): read covers search, projects, folders, data entries, docs as markdown, highlights, comments, themes, tags, file URLs; write covers create projects/docs/highlights/comments/tags; docs list no update or delete tools and no rate limi (user-story-mapping)
- [Snowflake-managed MCP server (Snowflake docs)](sources/snowflake-managed-mcp-server-docs.md): server is a database object created by an admin via `CREATE MCP SERVER ... FROM SPECIFICATION`; OAuth security integration must be created manually (no dynamic client registration). (user-story-mapping)
- [Notion MCP (Notion developer docs)](sources/notion-mcp-developer-docs.md): remote MCP hosted by Notion; connection by OAuth; search, read, create, update pages and databases; Claude Code, Cursor and Codex named as clients. (user-story-mapping)
- [Use Looker with MCP, Gemini CLI and other Agents (Google Cloud docs)](sources/google-looker-mcp-toolbox-docs.md): setup needs Looker URL, client ID and secret env vars, or an OAuth application; Google also mentions a Looker-managed MCP server for managed setups (details not read). (user-story-mapping)
- [Trends Shaping Product Management in 2025 (ProductPlan)](sources/productplan-trends-product-management-2025.md): more respondents than 2024 prefer to consolidate; top reasons standardising tools across teams, budget, data silos/poor visibility; strategy, roadmapping, prioritisation most often wanted in one tool. (user-story-mapping)
- [Call the Teamwork Graph API](sources/atlassian-teamwork-graph-call-the-api.md): the graph is 'available through Forge's Preview release phase', callable only from a Forge app (api.asUser().requestTeamworkGraph), with 1-month breaking-change notice; not a direct OAuth endpoint for an external harness. (user-story-mapping)
- [Limitations and considerations (Teamwork Graph)](sources/atlassian-teamwork-graph-limitations.md): Forge apps only, installed in Jira or Confluence, org-admin install; Atlassian intends controls so graph data 'is not egressed from the Atlassian platform'. (user-story-mapping)
- [Atlassian Rovo MCP server: supported tools](sources/atlassian-rovo-mcp-server-supported-tools.md): v2 exposes a few Primary tools plus discover/executeRead/executeWrite/executeDestructive; delete_jira and manage_jira 'disabled by default. An admin must enable'; Confluence has archive but no delete tool. (user-story-mapping)

- [Open a Jira work item in an AI coding tool](sources/atlassian-jira-open-work-item-in-coding-tool.md): optional Rovo MCP lets the local agent read Jira and Confluence and update the work item (user-story-mapping)
## project-taxonomy: How 'project' is defined
Initiative/project/epic/space taxonomies across tools and conventions.
- [Initiatives (Linear docs)](sources/linear-initiatives-docs.md): Initiatives are curated groups of projects tied to a company objective; sub-initiatives allowed; projects can be collected by filters; initiative health on track/at risk/off track from updates; documents attach via a Resources pro (user-story-mapping)
- [Create a space (Confluence)](sources/atlassian-confluence-create-a-space.md): a space is 'a container ... for work related to a shared project or initiative' with a purpose of Collaboration, Knowledge base or Custom, one owner and a permissions scheme; it is a third 'project'-like container beside Jira spaces and Atlassian Home projects. (user-story-mapping)

## product-artifact-primitives: Native PM artifact objects and project containers across platforms
What each platform treats as its first-class product-work objects (idea, initiative, project, space, spec, insight, document, skill) and how a 'project' is bounded. Matters for deciding whether a product meta-harness defines its own primitives or maps onto existing ones.
- [Teamwork Graph glossary (Atlassian developer docs)](sources/atlassian-teamwork-graph-glossary.md): Object = single item of data (Jira work item, Confluence page, Google Drive file); each belongs to an object type that defines structure, properties and possible relationships. (user-story-mapping)
- [Teamwork Graph object types (Atlassian developer docs)](sources/atlassian-teamwork-graph-object-types.md): Queryable API object types named on the page: Jira work items and Users. (user-story-mapping)
- [Getting started with the Atlassian Rovo MCP server](sources/atlassian-rovo-mcp-server-getting-started.md): Server URL https://mcp.atlassian.com/v2/mcp; v1 usage moves to v2 tools on 2027-03-01 (per the page). (user-story-mapping)
- [Atlassian Rovo MCP server: supported tools](sources/atlassian-rovo-mcp-server-supported-tools.md): Jira read: work items, projects, boards, sprints, filters, dashboards, comments, changelogs, worklogs, statuses, versions, components. Write: create/edit/transition work items, comments, links, versio (user-story-mapping)
- [What is a Jira space (formerly project)](sources/atlassian-jira-space-definition.md): 'A Jira space is a collection of related work items' for a product, team, service or project; items carry a space key prefix (e.g. GDT-1). (user-story-mapping)
- [What is a Confluence space](sources/atlassian-confluence-space-definition.md): A space is a container for creating, storing and collaborating on work tied to a team, shared project or initiative; examples: a knowledge base, or a space per launch or campaign. (user-story-mapping)
- [What is an idea (Jira Product Discovery docs)](sources/atlassian-jira-product-discovery-ideas.md): Idea = basic unit of work in a JPD space; fields such as goals, team, priority score, impact. (user-story-mapping)
- [Working with databases (Notion API docs)](sources/notion-api-databases-data-sources.md): Database = container holding data sources and views; does not carry the schema in current API versions. (user-story-mapping)
- [Notion MCP supported tools](sources/notion-mcp-supported-tools.md): Search (up to 50 results), connector search across Slack/Drive/GitHub, memory search over saved agent memories. (user-story-mapping)
- [Projects (Linear docs)](sources/linear-docs-projects.md): Project = 'a grouping of issues that have a clear outcome or planned completion date'. (user-story-mapping)
- [Initiatives (Linear docs)](sources/linear-docs-initiatives.md): Initiatives are workspace-level containers for projects tied to a shared objective; IDs like I-<n>. (user-story-mapping)
- [Documents (Linear docs)](sources/linear-docs-documents.md): Documents attach to projects, initiatives, teams, issues or cycles; same editor as issues; realtime collaboration; version history including agent edits; templates at workspace/team level. (user-story-mapping)
- [Linear for Agents (developer docs)](sources/linear-developers-agents.md): Agents can be @mentioned, assigned issues, comment, and collaborate on projects and documents; installed agents are not billable users. (user-story-mapping)
- [Connect a coding agent to Spark via MCP (Productboard support)](sources/productboard-mcp-server-spark.md): Beta, included with Spark-enabled workspaces at no extra cost; admins enable it under Settings > MCP Server and choose roles. (user-story-mapping)
- [Add features to your hierarchy (Productboard support)](sources/productboard-product-hierarchy.md): Hierarchy: Product > Component > Feature > Subfeature. Features can be imported from spreadsheet, Jira or Zapier. (user-story-mapping)
- [Build on Dovetail (docs)](sources/dovetail-build-on-dovetail.md): Three options: MCP server, REST API (default 200 requests/min per workspace), CLI 'dt' for bulk import from Notion, Confluence, Google Drive and files (no sync after import). (user-story-mapping)
- [github/spec-kit (README)](sources/github-spec-kit-readme.md): Workflow: /speckit-constitution (once per project), then per feature /speckit-specify, -plan, -tasks, -implement, -converge. Runs as skills in the agent's chat. (user-story-mapping)
- [Spec-Driven Development (spec-kit spec-driven.md)](sources/github-spec-kit-spec-driven.md): Each feature lives in specs/<NNN-branch-name>/ with spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md ([P] marks parallel tasks). (user-story-mapping)
- [About Projects (GitHub Docs)](sources/github-docs-about-projects.md): Project = adaptable table, board and roadmap integrating issues and PRs, at user or organisation level; two-way sync with issues. (user-story-mapping)
- [What are projects? (Claude Help Center)](sources/anthropic-claude-projects-support.md): Project = self-contained workspace: knowledge base (documents, text, code), custom instructions, own chat history; memory mentioned only for a beta version. (user-story-mapping)
- [How Claude remembers your project (Claude Code docs)](sources/anthropic-claude-code-memory-docs.md): Locations: managed policy (e.g. /Library/Application Support/ClaudeCode/CLAUDE.md), user, project (./CLAUDE.md or ./.claude/CLAUDE.md), local (CLAUDE.local.md). (user-story-mapping)
- [Organize work with projects (Claude Cowork docs)](sources/anthropic-cowork-projects-docs.md): Project holds: description (Dispatch reads it to choose a project for a task), folders (one or more local), instructions, links, linked Chat projects, memory. (user-story-mapping)
- [Glean Enterprise Graph (product page)](sources/glean-enterprise-graph-product-page.md): Enterprise Graph = relationships among people, projects, teams, products and processes, plus indexed content metadata; personal graphs infer the tasks and projects behind a person's activity. (user-story-mapping)
- [Scopes (Teamwork Graph API)](sources/atlassian-teamwork-graph-scopes.md): the full API object-type list (one read scope each) covers Jira, Confluence (page, blogpost, comment, database, folder, space, whiteboard), Atlassian Home (goal, goal update, project, project update, tag, comment), Loom, Compass, Focus, Talent and 29 External* connector types; still no idea, PRD, spec, insight or decision type. (user-story-mapping)
- [Relationships (Teamwork Graph)](sources/atlassian-teamwork-graph-relationships.md): four relationship kinds (canonical, activity, logical, inferred); logical ones like AtlassianUserCreatedDocuments unify Confluence pages and external documents under one edge. (user-story-mapping)
- [PRD template (Confluence)](sources/atlassian-confluence-prd-template.md): Atlassian's PRD is a page template whose Options table holds user story, importance and 'Jira issues' as embedded links via /jira; no typed PRD-to-work-item relationship, no JPD or Home link. (user-story-mapping)
- [Atlassian MCP enhancements blog](sources/atlassian-blog-mcp-enhancements-jpd.md): July 2026 blog claims agents can find a JPD idea and link it to a delivery issue, but the supported-tools page names no JPD tool. (user-story-mapping)
- [Open-Inspect README](sources/github-open-inspect-background-agents.md): the session is 'the core unit of work'; it stores messages, events, 'Artifacts | PRs created, screenshots captured', participants and sandbox state; no project object, grouping is by repository, environment and team; Linear holds the project mapping. (user-story-mapping)
- [Why We Built Our Own Background Agent (Ramp Builders)](sources/ramp-builders-why-we-built-our-own-background-agent.md): Inspect's unit is the session (own SQLite DB, shareable by URL) and its output is the PR with before/after screenshots; no spec, PRD, project or folder concept described. (user-story-mapping)
- [What is a goal? (Atlassian Goals)](sources/atlassian-goals-what-is-a-goal.md): Goal = name, owner, target date, status, monthly update, sub-goals; Home projects sync with epics (user-story-mapping)
- [Link an idea to a Jira work item (JPD)](sources/atlassian-jpd-link-idea-to-work-item.md): idea shows a Delivery progress bar from linked work items (user-story-mapping)
## agent-factory-sdlc: Agents across the whole product development loop
- [Generate code from a work item in Jira (Jira Coding Agent)](sources/atlassian-jira-coding-agent-generate-code.md): assign a work item to Jira Coding Agent or Start work from Agent sessions; one sandbox session per repo; output is a draft PR it never merges (user-story-mapping)
- [How we're evolving Jira for AI-native software development](sources/atlassian-blog-jira-ai-native-software-development.md): July 2026 launch spans Planner (spec), Jira for Slack and Loom prompts (intake), agents in Jira, Coding Agent, agent sessions, coding-agent automations, DX cost per PR (user-story-mapping)
- [Using Jira for agentic engineering](sources/atlassian-jira-agentic-engineering-guide.md): vendor lifecycle is plan, orchestrate, review, scale (user-story-mapping)
- [Using the Ops Expert agent](sources/atlassian-rovo-ops-expert-agent.md): operate step: alert/incident triage, PIR drafted as a Jira work item or Confluence page (user-story-mapping)
- [Work with Rovo Dev in Bitbucket Pipelines](sources/atlassian-rovo-dev-bitbucket-pipelines.md): release step (beta): change summaries from commits, work items and deployment data; failed-build explanations (user-story-mapping)
- [Rovo Dev in Jira launch blog](sources/atlassian-blog-rovo-dev-in-jira.md): agent proposes a plan to review, then executes, tests and opens PRs in a cloud sandbox (user-story-mapping)
## opportunity-to-code-chain: Opportunity → problem → goal → intent → plan → code
- [Link an idea to a Jira work item (JPD)](sources/atlassian-jpd-link-idea-to-work-item.md): idea to epic/task via the Delivery tab; optional 'Embed the idea description and fields into the work item' is the only documented way idea content reaches the work item an agent reads (user-story-mapping)
- [Record for AI agents (Loom)](sources/atlassian-loom-record-for-agent.md): screen recording becomes an agent prompt and, for Atlassian accounts, Jira work items 'for agents to act on' (user-story-mapping)
- [Check acceptance criteria in a code review](sources/atlassian-rovo-dev-acceptance-criteria-code-review.md): review reads AC from the work item matched by the key in the branch name (user-story-mapping)
- [Introducing Jira Planner](sources/atlassian-blog-introducing-jira-planner.md): finalized plan becomes sequenced work items each with AC and plan context; 'agent orchestration takes over' (user-story-mapping)
- [Open a Jira work item in an AI coding tool](sources/atlassian-jira-open-work-item-in-coding-tool.md): deep link passes summary and description (support doc) or also linked docs (blog) (user-story-mapping)
- [What is a goal? (Atlassian Goals)](sources/atlassian-goals-what-is-a-goal.md): goals link sub-goals, projects, Jira epics and work items; Teamwork Graph has a work-item-contributes-to-goal relationship (user-story-mapping)
- [Using the Ops Expert agent](sources/atlassian-rovo-ops-expert-agent.md): PIR action items become Jira work items, closing the operate-to-backlog loop (user-story-mapping)
## task-context-isolation: Isolation by task context, not only by user permission
- [Generate code from a work item in Jira (Jira Coding Agent)](sources/atlassian-jira-coding-agent-generate-code.md): only the selected repo is cloned; in automations the agent runs 'restricted' with no Teamwork Graph or Confluence context (user-story-mapping)
## agent-control-plane: Agent control planes above vendors
- [View and manage agents in your Jira space](sources/atlassian-jira-manage-agents-in-space.md): one Agents page per space for Atlassian, Studio and third-party agents with triggers, prompt, sources and role (user-story-mapping)
- [How we're evolving Jira for AI-native software development](sources/atlassian-blog-jira-ai-native-software-development.md): assign to Claude Code, Cursor, Copilot (Codex soon) and Jira Coding Agent; Copilot, Cursor and Claude as automation action steps (user-story-mapping)
- [Using Jira for agentic engineering](sources/atlassian-jira-agentic-engineering-guide.md): agents triggered by assignment, workflow transition, board column or automation rule (user-story-mapping)
## scoped-governance-containers: Governance scoped to a project or workspace
- [View and manage agents in your Jira space](sources/atlassian-jira-manage-agents-in-space.md): agents are members of a space with a role; private spaces grant nothing without one (user-story-mapping)
## evals-autonomy-trust: Evals, autonomy sliders and earned trust
- [View and manage agents in your Jira space](sources/atlassian-jira-manage-agents-in-space.md): field-level autonomy controls exist only for the Jira Triage Agent so far (user-story-mapping)
- [RovoDev Code Reviewer (ICSE 2026)](sources/arxiv-rovodev-code-reviewer-icse26.md): LLM judge filters wrong comments; classifier ranks actionability; 38.70% resolution vs 44.45% for humans (user-story-mapping)
## agent-led-intent-shaping: Agents shape intent, not only execute it
- [Introducing Jira Planner](sources/atlassian-blog-introducing-jira-planner.md): asks follow-up questions on scope, constraints and success; PMs named in the audience (Early Access) (user-story-mapping)
## spec-edge-case-review: Agents for spec edge-case review
- [Introducing Jira Planner](sources/atlassian-blog-introducing-jira-planner.md): 'tells you whether your spec is detailed enough for execution, with specific suggestions for what's missing' (user-story-mapping)
## outcome-measurement-gap: Nobody can yet measure PM-agent outcomes
- [RovoDev Code Reviewer (ICSE 2026)](sources/arxiv-rovodev-code-reviewer-icse26.md): outcomes measured as comment resolution and PR cycle time, not quality or customer impact (user-story-mapping)
## tacit-knowledge-capture: Capturing tacit knowledge from people for agents
- [Record for AI agents (Loom)](sources/atlassian-loom-record-for-agent.md): captures narration, clicks, visited URLs, console and network logs into an agent prompt (user-story-mapping)
## ai-synthesis-hallucination-risk: AI synthesis can invent or merge facts
- [Make Rovo your research assistant - Deep research mode](sources/atlassian-rovo-deep-research.md): inline citations added after evaluation found claims hard to verify (user-story-mapping)
## cost-control-routing: Cost metering and model routing built into the harness
- [Using the Ops Expert agent](sources/atlassian-rovo-ops-expert-agent.md): Rovo credits charged for Teamwork Graph context reads, including by Claude or ChatGPT via MCP or CLI, from December 3, 2026 (user-story-mapping)
- [How we're evolving Jira for AI-native software development](sources/atlassian-blog-jira-ai-native-software-development.md): DX cost management estimates cost per PR across Claude, Cursor, Copilot and Jira (user-story-mapping)
## human-judgment-pm-jobs: PM jobs that stay human-led
- [Using Jira for agentic engineering](sources/atlassian-jira-agentic-engineering-guide.md): 'Set the goal (people decide what and why; Jira turns it into a plan)' (user-story-mapping)
## status-update-agents: Status updates and 'ask the org' Q&A as an agent job
- [Work with Jira Delivery agent](sources/atlassian-rovo-jira-delivery-agent.md): stakeholder summaries, daily digests, stale-work follow-ups, usable in automation (user-story-mapping)
- [What is a goal? (Atlassian Goals)](sources/atlassian-goals-what-is-a-goal.md): goal updates are human-written monthly (reminder on the 1st, released on the 8th) (user-story-mapping)
- [Work with Rovo Dev in Bitbucket Pipelines](sources/atlassian-rovo-dev-bitbucket-pipelines.md): release change summaries; Release Notes Drafter from up to 20 Jira issues (user-story-mapping)
## enterprise-admin-controls: Enterprise admin controls across harnesses
- [Work with Rovo Dev in Bitbucket Pipelines](sources/atlassian-rovo-dev-bitbucket-pipelines.md): not yet governed by the org AI early-access toggle; only the workspace Rovo Dev switch (user-story-mapping)
## one-job-per-agent: One job per agent
- [Work with Jira Delivery agent](sources/atlassian-rovo-jira-delivery-agent.md): out-of-the-box agent scoped to delivery state with its own tool set (user-story-mapping)
