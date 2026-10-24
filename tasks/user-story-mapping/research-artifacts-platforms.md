# How platforms handle PM artifacts and project structure (implications for a product meta-harness)

Filed by user-story-mapping, 2026-10-24. Source notes are in `../../research/sources/`; theme `product-artifact-primitives` added to `../../research/THEMES.md`. Almost everything is first-party documentation fetched via WebFetch (model-summarised, not verbatim). Existing atlassian-*, notion-*, linear-*, productboard-*, dovetail-* notes (mostly vendor marketing and adoption claims) were not redone.

## Per platform

**Atlassian (Jira, Confluence, Rovo, Teamwork Graph)**
- Native objects: Jira work items (renamed from issues) in a "space" (renamed from project), with work types, workflows, team-managed vs company-managed config; Confluence pages/whiteboards/databases in spaces; Jira Product Discovery ideas (custom idea types, insights, delivery links to work items); Atlassian Home goals and projects (a second, different "project").
- "Project": split three ways: Jira space = collection of work items; Confluence space = doc container; Home project = a strategy-tracking object. Joined by links, not one object.
- Graph model: generic objects with object types, directional typed relationships (canonical, activity, inferred), ARIs, per-object ACLs, GraphQL/Cypher. Connector types are generic (Work item, Document, Project, Space, Design, Deal...), with no PRD/spec/insight type.
- Agent access: remote Rovo MCP (OAuth 2.1, user permissions, Rovo credits); can read and write work items, pages, goals, projects. Delete and project-admin tools are off by default.
- Gaps: unstable vocabulary; JPD not in the MCP tool list; the Teamwork Graph API appears limited-access (unverified).
- Notes: [glossary](../../research/sources/atlassian-teamwork-graph-glossary.md), [object types](../../research/sources/atlassian-teamwork-graph-object-types.md), [MCP start](../../research/sources/atlassian-rovo-mcp-server-getting-started.md), [MCP tools](../../research/sources/atlassian-rovo-mcp-server-supported-tools.md), [Jira space](../../research/sources/atlassian-jira-space-definition.md), [Confluence space](../../research/sources/atlassian-confluence-space-definition.md), [JPD idea](../../research/sources/atlassian-jira-product-discovery-ideas.md).

**Notion**
- Objects: database (container) > data source (schema) > page (row plus free-form body); views; comments; folders; Skills; Custom Agent sessions.
- "Project": no first-class object; a convention built on databases (from general knowledge, unverified here).
- Access: hosted MCP, OAuth. The broadest surface: query/SQL across data sources, views, meeting notes, agent memories, skills upload, spawn and read agent sessions. Many tools are gated to Business/Enterprise with Notion AI. Query caps at 100 rows with no cursor.
- Notes: [API model](../../research/sources/notion-api-databases-data-sources.md), [MCP tools](../../research/sources/notion-mcp-supported-tools.md).

**Linear**
- Objects: issue, project (bounded outcome/date, lead team, milestones, resources), initiative (workspace strategy container, health from latest update), documents (attach to project/initiative/team/issue/cycle), project updates.
- Agents: agents install as OAuth apps and are workspace members; an issue is *delegated* (human stays assignee); agent-session webhooks; scopes app:assignable / app:mentionable. MCP (mcp.linear.app) covers issues, projects, comments (initiatives/documents not confirmed).
- Gap: strongly issue-centric; long-form specs are second-class.
- Notes: [projects](../../research/sources/linear-docs-projects.md), [initiatives](../../research/sources/linear-docs-initiatives.md), [documents](../../research/sources/linear-docs-documents.md), [agents](../../research/sources/linear-developers-agents.md).

**Productboard**
- Objects: product > component > feature > subfeature; insights/notes linked to features; objective > initiative layer (partly from search summary); Spark adds a Specification tab on initiatives/features/subfeatures and an "Agent Knowledge" document area.
- Access: beta remote MCP (browser sign-in, user's view only, admin role control): read/edit specs, comment, status, manage documents. Documented for Claude Cowork, Claude Code, Cursor. This is the clearest PM-tool-to-coding-agent spec handoff.
- Notes: [MCP/Spark](../../research/sources/productboard-mcp-server-spark.md), [hierarchy](../../research/sources/productboard-product-hierarchy.md).

**Dovetail**
- Objects: projects, docs, data/transcripts, highlights, contacts, channels (feedback streams). MCP, REST (200 req/min/workspace) and CLI all act as the user. Channel endpoints were still being added. The full object model (notes vs insights) is unconfirmed.
- Note: [build on Dovetail](../../research/sources/dovetail-build-on-dovetail.md).

**GitHub (Spec Kit, Projects)**
- Spec Kit: artifacts are repo files. Project-level constitution plus `.specify/` state; per feature `specs/NNN-name/` with spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md. Extensions for bug-fixing and idea assessment (intake, research, define, shape, decide, with go/kill output). Runs as agent skills across many agents.
- GitHub Projects: thin table/board/roadmap over issues and PRs with up to 50 custom fields; the long-form artifacts live in the repo.
- Gap: nothing upstream of spec (roadmap, insight, initiative) except the assess extension.
- Notes: [Spec Kit README](../../research/sources/github-spec-kit-readme.md), [SDD doc](../../research/sources/github-spec-kit-spec-driven.md), [Projects](../../research/sources/github-docs-about-projects.md).

**Anthropic (Projects, Cowork, Claude Code memory, Skills)**
- claude.ai project: knowledge files + instructions + chats; shareable on Team/Enterprise; RAG when large; being redefined in a beta.
- Cowork project: description, local folders, instructions, links, linked Chat projects, project-scoped memory; local only, not shareable.
- Claude Code: layered CLAUDE.md (managed, user, project, local), `.claude/rules/`, @imports, AGENTS.md fallback, separate model-written auto memory. Treated as context, not enforced; hooks enforce.
- Skills: already covered by existing notes (skills docs, agentskills spec).
- Gaps: no typed product artifacts; sharing is split (shareable project is files-only, local project is not shareable).
- Notes: [Projects](../../research/sources/anthropic-claude-projects-support.md), [Cowork projects](../../research/sources/anthropic-cowork-projects-docs.md), [Claude Code memory](../../research/sources/anthropic-claude-code-memory-docs.md).

**Glean-style context layers**
- Infers entities (projects, people, customers, products) with ML over 275+ connectors, plus personal graphs; exposes agents via MCP (existing note). Vendor claims only, no schema found.
- Note: [Enterprise Graph](../../research/sources/glean-enterprise-graph-product-page.md).

## Ramp Glass and Geoff's intent docs (existing notes, re-read)
- Glass does not appear to define its own artifact types. Its "project" is a per-project cost meter; knowledge is pulled from Linear, Notion, Google, Slack and Gong; memory is files written by a 24-hour pipeline; Dojo skills are Git-backed markdown ([Goddijn](../../research/sources/x-sebgoddijn-glass-article.md), [Buchan](../../research/sources/x-shanebuchan-how-we-built-glass.md), [Eglyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md)). Users made 6,500+ edits to shared knowledge.
- "Organization legible to agents": Charles's Gadget maps questions onto the formal record, with the roadmap and specs in Notion, tickets in Linear, plus Slack and customer calls; the claim is that 85% of PM questions are answered by AI ([transcript](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.transcript.md) around 11:25-14:08). Ramp uses Notion and Linear as the record, not a custom store.
- Geoff's docs: [intent factory](../../research/sources/geoff-building-accelerating-intent-factory.md) calls for an agent-ready intent standard (completeness gate), one versioned shaping skill with a named source per question, and a shared plain-text context repo with domain owners where "evidence, not yet fact" is written back. [Risk docs](../../research/sources/geoff-intent-shaping-well-managed-environment.md) call for a canonical spec artifact plus a MECE risk taxonomy. These are primitives he implies (intent/spec, evidence, risk taxonomy, shaping skill) but does not name as a schema.

## Implications for a product meta-harness
1. Every platform's "project" differs; Atlassian alone has three. A harness should define a thin project descriptor (as Cowork does: description, sources, instructions, memory) that points at platform objects, not a competing store.
2. Typed PM objects are weakly standardised: no vendor graph has native spec/insight/decision types (Atlassian maps them to Document/Work item). Only Spec Kit gives a file-level spec set, and Productboard holds specs on features. Candidate primitives: intent/spec, evidence, decision, risk, status update.
3. MCP with user-scoped OAuth is the common access path (Atlassian, Notion, Linear, Productboard, Dovetail, Glean). Linear's delegate-not-assignee and Atlassian's off-by-default delete are reusable governance patterns.
4. File-in-repo (Spec Kit, CLAUDE.md, Geoff's context repo) and platform-object (Notion, Productboard) models coexist; the harness boundary question is which one is canonical.

## What's unverified
- All platform pages were read through a summarising fetch, not verbatim; re-check before quoting.
- Teamwork Graph API availability (limited/early access) and Home entity types: from search summaries only; relationship-types page 404'd.
- Productboard objective > initiative layer and notes inbox: search summaries only. Productboard MCP full tool list not fetched.
- Dovetail object model (notes vs insights) and hosted-MCP auth (sources conflict).
- Linear MCP omitting initiatives/documents: from one page, may be stale.
- Spec Kit: README vs spec-driven.md differ on command names and layout; star count and "1.0" from the page, unchecked.
- GitHub MCP, sub-issues, GitHub Copilot spec workflows not researched (GitHub MCP needs auth).
- Claude Code memory page read partially; claude.ai Projects beta is moving.
- Notion "project" as a convention: general knowledge, not sourced. Confluence space types and permissions not fetched.
- Glean graph claims are vendor marketing; no technical docs found.
- Ramp Glass: no source states a project/artifact schema; absence is from existing notes, not a full re-read of all Glass transcripts.
- Not covered: Jira Product Discovery MCP access, Asana/ClickUp/monday, Aha!, Figma, Anthropic Skills beyond existing notes.

## Audit additions (2026-10-24, Fable pass)

Targeted verification of the Atlassian and Ramp findings above. Atlassian pages were re-read verbatim (curl download, tags stripped) rather than through a summarising fetch; exceptions are noted. New source notes are linked; the four existing Atlassian notes, the Open-Inspect note and the Glyman essay note each gained a dated "Verification" section.

### Atlassian: verified vs corrected

Verified (verbatim on the live pages):
- Rovo MCP v2 supported tools: `delete_jira` and `manage_jira` are "disabled by default. An admin must enable". Destructive calls go through a separate `executeDestructive` pathway "used to apply agent-level confirmation". Jira write tools (create/edit/transition work items, comments, worklogs, issue links, remote links to Confluence pages, versions, sprints, boards, attachments, entity properties, hierarchy conversion), Confluence read/write (pages, blogs, live docs, whiteboards, databases, folders, embeds, smart links, comments, versions and diffs, permissions, restriction state, public links, templates, tasks, "space instructions"), Goals and Projects read/write, plus Focus areas, Teams, Talent, Capacity planning and a `read_teamwork_graph` group (getTeamworkGraphContext, getTeamworkGraphObject, getWorkPortfolio, getWorkActivity, getPeopleInfo, getPullRequests; "1-10 Rovo credits per call"). ([MCP tools](../../research/sources/atlassian-rovo-mcp-server-supported-tools.md))
- Teamwork Graph vocabulary (object, object type, ARI, directional typed relationships, per-object ACLs, GraphQL plus Cypher) is as the earlier note said. ([glossary](../../research/sources/atlassian-teamwork-graph-glossary.md))
- Connector object-type lists (indexed and not-indexed) match the earlier note exactly. ([object types](../../research/sources/atlassian-teamwork-graph-object-types.md))

Corrections to the earlier text:
- "Teamwork Graph API appears limited-access (unverified)": wrong as of 2026-09-15. It is in Forge **Preview** ("available to all users and receive the same level of support as generally available features", 1-month breaking-change notice), **read-only** ("there is no write access to the graph through this API"), callable only from a **Forge app** installed in Jira or Confluence by an **org admin**, with one `read:graph:<object>:<product>` scope per object type, admin-toggleable, and fail-closed (a missing scope returns success and empty rows). Atlassian states intent to prevent egress of graph data from its platform. So it is not a data path for an external harness; the MCP server is. ([scopes](../../research/sources/atlassian-teamwork-graph-scopes.md), [call the API](../../research/sources/atlassian-teamwork-graph-call-the-api.md), [limitations](../../research/sources/atlassian-teamwork-graph-limitations.md))
- "Home entity types from search summaries only": now verified on the Scopes page. API object types include Confluence (Page, BlogPost, Comment, Database, Folder, Space, Whiteboard), Atlassian Home (Goal, GoalUpdate, Project, ProjectUpdate, HomeTag, HomeComment), Team/TeamType/User, AssetsObject, Loom, Compass, Focus (FocusArea, StatusUpdate, ChangeProposal), Talent, and 29 External* types. Still no idea, PRD, spec, insight or decision type.
- Relationship kinds: four (canonical, activity, **logical**, inferred), not three. Logical relationships (e.g. `AtlassianUserCreatedDocuments`) unify Confluence pages and external documents under one edge. ([relationships](../../research/sources/atlassian-teamwork-graph-relationships.md))
- "JPD not in the MCP tool list": confirmed, zero mentions on the supported-tools page. But a July 2026 Atlassian blog claims "With Jira Product Discovery support, agents can connect high-level ideas ... to the delivery work" with a sample prompt that finds a JPD idea and links it to a delivery issue. Most likely path: JPD ideas are Jira issues, reachable through the generic work-item tools. Unconfirmed on a live site. ([blog](../../research/sources/atlassian-blog-mcp-enhancements-jpd.md))
- Earlier claim "generated infographics cost 15-30 Rovo credits" was not found on the current page; drop it.
- Confluence sharing model (earlier gap, now filed): space "purpose" at creation is Collaboration, Knowledge base or Custom with a permissions scheme and one owner ([create a space](../../research/sources/atlassian-confluence-create-a-space.md)); role-based space access is GA with default roles Admin / Manager / Collaborator / Viewer and custom roles, and public links, guest access and anonymous access are separate admin grants ([roles](../../research/sources/atlassian-confluence-roles-space-permissions.md)); per-item restrictions are open, edit-restricted, restricted, or restricted-by-parent, view restrictions inherit down the tree, edit restrictions do not, none on the free plan ([page restrictions](../../research/sources/atlassian-confluence-page-restrictions.md)). The MCP server can read and set restriction state, content permissions and public links, so an agent can share a PRD with a sub-team programmatically.
- Where PRDs/specs/decisions live (earlier gap, now filed): Atlassian's guidance is **page templates in a Confluence space**, linked to Jira by embedded `/jira` issue links in tables, not typed relationships. PRD template sections: basics and roles, objective, success metrics, assumptions, options (requirement, user story, importance, Jira issues), supporting docs, open questions, out of scope ([PRD](../../research/sources/atlassian-confluence-prd-template.md)). Project poster: problem space, known facts vs open questions, solution and scope, reference links ([poster](../../research/sources/atlassian-confluence-project-poster-template.md)). DACI decision page: status, impact, roles, options with pros/cons/cost, action items, outcome, single approver ([DACI](../../research/sources/atlassian-confluence-daci-decision-template.md)). None of the three mentions JPD ideas or Atlassian Home projects. A new detail worth noting for the harness: Confluence spaces now carry "space instructions" that agents read (`getConfluenceSpaceInstructions`), a per-container instruction file analogous to CLAUDE.md.

### Ramp: does the claim hold?

Claim tested: "Ramp Glass defines no artifact schema or project structure of its own; Notion and Linear are the formal record; Glass projects are per-project cost meters."

Local evidence (grep of all ramp-/x-/transcript notes for spec, PRD, formal record, Notion, Linear, folder, decision, project):
- Charles, Lenny summit talk, [11:38-11:52]: "A gadget essentially understands the intent of these questions and connects it to the formal record, the road map in Notion, the specs in Notion, the customer calls in Notion, Slack, Linear, our tickets." [13:50-13:52]: the small-loop agent "matches it with your backlog in linear. It dedupes." [6:59-7:05]: Glass "understands our product strategy. It understands how we define product specs." [7:38-7:52]: engineers "don't want your long spec ... They want the combination of qualitative and quantitative data ..., the actual requirements that they can use for their coding agents, and a prototype". ([transcript](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.transcript.md))
- Goddijn: Glass memory "gives every chat session context on the people they work with and their active projects, along with references to relevant Slack channels, Notion documents, Linear tickets"; a 24-hour pipeline mines "Slack, Notion, and Calendar"; skills are markdown files in the Dojo marketplace; files the agent creates open as tabs (markdown, HTML, CSV, images, code). No project or artifact schema named. ([Goddijn](../../research/sources/x-sebgoddijn-glass-article.md) lines 70-96)
- Glyman launch essay (X and ramp.com/blog, identical text): "Every project has a meter, like a taxi."; "A meter on every project. See what it costs. Set limits before they're crossed."; knowledge sources "Linear, Notion, Google, Slack, Gong, and dozens more"; sharing is session-level ("She shares her Glass session."). ([Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md))
- Pragmatic Summit talk [27:46-27:53], [29:34-29:47]: Inspect pulls in "a Slack message ..., a Notion doc" and "context documents that product teams have put together"; sessions are kicked off "via a Kanban UI, we have an API, and then also a Slack thread". ([transcript](../../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.transcript.md))
- Charles AI-pilled article: Glass auto-connects "Salesforce, Snowflake, Gong, Slack, Notion, Google Workspace, Figma". ([Charles](../../research/sources/x-geoffintech-ai-pilled-article.md))

Web evidence this pass:
- ramp.com/glass is a sign-up page: tagline and "Request early access" only. ramp.com/blog/introducing-glass is the Glyman essay (quoted above). builders.ramp.com has no Glass post reachable (the index renders empty; search found none).
- Ramp Builders, "Why We Built Our Own Background Agent" (Bruggeman, Quense, Sengottuvelu, 2026-01-12; body read via WebFetch because the page is a JS shell): Inspect's unit is the session (own SQLite database, "Send your session to any colleague, and they can help take it home."), inputs are Slack threads, PR comments, web UI, Chrome extension, outputs are PRs with before/after screenshots; no specs, PRDs, projects or folders mentioned. ([builders post](../../research/sources/ramp-builders-why-we-built-our-own-background-agent.md))
- Open-Inspect (ColeMurray/background-agents, MIT, 3,395 stars; "inspired by Ramp's Inspect", not Ramp's code; `ramp/open-inspect` does not exist): "A session is the core unit of work"; a session stores messages, events, "Artifacts | PRs created, screenshots captured", participants, sandbox state; no project object (grouping by repository, environment, team); the Linear bot maps Linear team and project to repo or environment, i.e. the project record lives in Linear. ([Open-Inspect](../../research/sources/github-open-inspect-background-agents.md))

Verdict: the claim **holds on the available evidence, with one caveat**. No Ramp source (eleven local notes and transcripts, the launch blog, the Builders post, the Open-Inspect docs) describes a Glass or Inspect artifact schema; the named records are Notion (roadmap, specs, customer calls), Linear (tickets, backlog, project mapping), Slack, Gong, Snowflake, GitHub (PRs). The unit Ramp does define is the session (shareable, multiplayer, attributed) and, for Glass, skills and memory as files. The caveat: "Glass projects are per-project cost meters" is an inference from Glyman's two sentences; no source says what a Glass project contains besides a meter and limits, and Goddijn's "their active projects" could refer to Linear/Notion projects surfaced through memory. Treat "project = meter only" as unestablished rather than confirmed; "no artifact schema; Notion and Linear are the record" is supported.

### Still unverified
- JPD idea access through the Atlassian MCP server (tool path, which idea fields, insights, delivery links); not tested on a live site.
- The Teamwork Graph API relationship-type reference and per-type object pages (index URLs 404; individual type pages exist per search but were not read).
- Exact permission sets inside Confluence's default roles (collapsed sections not captured); global/product-level permissions page not read.
- The Confluence template bodies as inserted into a space (only the marketing/how-to pages were read).
- Ramp Builders post full text (WebFetch summary only); Ramp Builders index (empty render); whether any Glass engineering post exists on builders.ramp.com.
- What a Glass "project" is beyond a meter; whether Glass sessions can be grouped, searched or attached to a Notion/Linear project.
- Open-Inspect docs/AUTH.md and whether past sessions are searchable (not stated in README or HOW_IT_WORKS).
- Pragmatic Engineer newsletter "Why Ramp built Inspect" (newsletter.pragmaticengineer.com/p/why-ramp-built-inspect) was not read; it may hold more on Inspect's internal organisation.
