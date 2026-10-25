# Commercial PM agents and the evidence they work

Research date: 2026-10-24. Method: web search plus a few page fetches (read-only). Search-result summaries were relied on for most vendor pages; items I did not open in full are flagged. No logins, no downloads.

Re-checked 2026-10-24: every linked source was re-fetched where reachable and claims corrected in place; anything still unconfirmed is marked "(unverified)". Ratings were re-applied with the revised scale below; 13 sources were added to fill gaps.

Evidence-quality scale (revised in the 2026-10-24 re-check): HIGH = independent, method disclosed, named numbers. MED = disinterested third-party or practitioner write-up with named numbers, though self-reported. LOW-MED = a single disinterested but informal test or opinion. LOW = anything the vendor published or commissioned (including named-customer stories and vendor-commissioned studies), partner or competitor write-ups, anonymous testimonials, review-site snippets. The original scale let vendor-published named-customer stories rate MED ("vendor-adjacent"); under the revised scale they are LOW, which lowered cases 1, 5, 8 and 14.

Headline finding: across all 23 cases I found NO independent, controlled evaluation of a PM agent doing a PM job. Strongest evidence is (a) Teresa Torres's disinterested practitioner roundup on Lovable prototyping (MED, with candid failure reports; all results self-reported) and (b) Notion's study run with MeasuringU (LOW under the revised scale because Notion published it and the commissioning is not stated, but the only vendor claim with a partly disclosed method). Everything else is vendor marketing or anecdote. No analyst (Gartner, Forrester) evaluation of any of the 23 products as a PM agent was readable.

## Summary table

| # | Product | PM job(s) | Org type | Best evidence | Rating |
|---|---|---|---|---|---|
| 1 | Atlassian Rovo agents | PRD/roadmap-item drafting, search, ticket work | Platform vendor | Procore quote (1h to 15m) and Tempo claim, both vendor-published; hallucination complaints | LOW (was LOW-MED) |
| 2 | Productboard Spark | Discovery, opportunity ID, spec writing | PM-tool vendor | Vendor GA statement; 6 named testimonials, no method | LOW |
| 3 | Amplitude AI agents / MCP / AI Feedback | Metrics review, feedback synthesis | Analytics vendor | AskNicely self-report (75% faster dashboard build), Replit quote | LOW |
| 4 | Pendo Agent Analytics / Novus | Metrics on AI agents; product-fix agent | Analytics vendor | Pushpay beta story; Novus no customers | LOW |
| 5 | Dovetail Magic AI | Research synthesis | Research vendor | Instawork 1-2h/project; Forrester TEI is Dovetail-commissioned | LOW (was LOW-MED) |
| 6 | Aha! AI (Elle, Builder) | Roadmap, prototypes | PM-tool vendor | None found | LOW |
| 7 | Linear Product Intelligence / Agent | Triage, dedupe, feedback-to-issue | Issue tracker | Vendor docs and dogfooding post only | LOW |
| 8 | Notion Custom Agents | Feedback routing, workflows | Workspace vendor | 218-person study, 93% vs 59% (vendor-published) | LOW (was MED-LOW) |
| 9 | ChatPRD | PRD writing/review | Startup | One-author 5-tool test (2nd of 5); vendor customer stories | LOW-MED |
| 10 | Zeda.io | Feedback collection/categorization | Startup | Product page only | LOW |
| 11 | Maze AI moderator | Research moderation | Research vendor | Unattributed "200 interviews in 10 days"; LCS named, unquantified | LOW |
| 12 | Sprig AI | In-product research/surveys | Research vendor | Named stories via aggregator | LOW |
| 13 | Gong (product insights) | Voice-of-customer from calls | Revenue-intel vendor | Recipes; user reviews; Chorus page | LOW |
| 14 | Intercom Fin | Customer-feedback source / support agent | Support vendor | Resolution rate claims; Anthropic page | LOW (was LOW-MED; for support, not PM) |
| 15 | Mixpanel Spark / Agent / MCP | Metrics Q&A, KPI monitoring | Analytics vendor | Vendor pages only | LOW |
| 16 | Figma Make | Prototyping | Design vendor | Practitioner review blogs | LOW |
| 17 | Vercel v0 | Prototyping | Dev-tool vendor | Avalara story (not PM-specific) | LOW |
| 18 | Lovable | PM prototyping | Startup | Product Talk 11-practitioner roundup; Zendesk quote | MED |
| 19 | Claude Cowork PM plugin | Specs, roadmap, stakeholder updates | Model vendor | Vendor repo README only | LOW |
| 20 | Cursor / Claude Code for PMs | PRD vs codebase, prototypes | Dev-tool vendors | Chime PM anecdote (How I AI episode; 20-min claim from Builder.io) | LOW |
| 21 | Enterpret | Feedback taxonomy/synthesis | Startup | Canva, Notion pages (vendor) | LOW |
| 22 | Unwrap.ai | Feedback analysis | Startup | GitHub Copilot team 4-5h/wk (vendor blog) | LOW |
| 23 | Kraftful (now Amplitude), Birdie | Feedback analysis | Startups | Replit quote; Birdie nothing | LOW |

---

Evidence and per-source detail now live in the research library; each section below is a short synthesis with links to the source notes (themes: [vendor-claims-vs-independent-evidence](../../research/THEMES.md), prd-agents, prototyping-agents-limits, research-synthesis-agents, feedback-triage-agents, metrics-review-agents).

## 1. Atlassian Rovo agents (Jira / Confluence)
AI teammates inside Atlassian tools, including custom agents from Rovo Studio. PM jobs: PRD and roadmap-item drafting, cross-tool search, ticket work. Evidence LOW (was LOW-MED; every number is vendor- or partner-published): Tempo (an Atlassian Platinum Marketplace Partner) claims 30% faster task completion with its Rovo Studio agents and 3x time savings from one agent (Structure View Builder), for its own Jira apps, with no baseline, sample or method published by Atlassian or Tempo; Procore roadmap items about 1 hour to about 15 minutes (Procore TPM quote) and a 1-2 hours/week beta "early feedback" figure, both published by Atlassian itself (Jan 2025 blog) with no method; OVO Energy qualitative. Limits: a competitor review (Slite) relays an Atlassian community report of invented runbook steps, a Marketplace partner (Seibert, Dec 2025) reported a custom agent that "confidently invented releases", and one community thread reported a team-wide Rovo failure on 2026-03-17 (support said internal issues, resolved; seen via search only, unverified); a "44% more accurate" Teamwork Graph figure comes from Atlassian's own undisclosed benchmarks (May 2026). An Atlassian Platinum Partner (CBTW, Apr 2026) reports backlog analysis and precise JQL are "inconsistent" and unconfigured use "half baked" (no named clients or numbers; notable because it comes from a partner); a single-team DEV post says Rovo missed team conventions (anecdote, engineering use). No press hands-on test or analyst note found.

Key URL: https://www.atlassian.com/customers/tempo ; https://www.atlassian.com/blog/announcements/team-24-eu-ai-updates ; https://techcrunch.com/2024/05/01/atlassian-launches-rovo-its-new-ai-teammate

Sources: [Tempo](../../research/sources/atlassian-tempo-customer-page.md) · [Atlassian blog, Procore/beta](../../research/sources/atlassian-blog-helping-every-team-succeed-ai-era.md) · [Atlassian blog, 44%](../../research/sources/atlassian-blog-teamwork-graph-team-26.md) · [Deviniti stats (does not contain these figures)](../../research/sources/deviniti-atlassian-ai-statistics-2026.md) · [Slite review](../../research/sources/slite-atlassian-rovo-ai-review.md) · [CBTW](../../research/sources/cbtw-atlassian-rovo-real-world-feedback.md) · [DEV post](../../research/sources/devto-tschimev-why-atlassian-rovo-failed-us.md)

## 2. Productboard Spark
Specialized PM agent: feedback analysis, product briefs, competitive analysis, spec writing; specs pulled into coding agents via MCP (product page). Private beta Oct 2025 (press release 2025-10-02); public beta Jan 2026 (CEO post 2026-01-27); relaunched June 2026 with key features still labelled beta; stated "now generally available" in Productboard's support article (updated 2026-10-22; no GA press release found, exact GA date unknown); standard on new Business/Enterprise workspaces, credit-metered. Evidence LOW: vendor material only; six named-customer testimonials on the product page (e.g. Praxedo "saved 1 week of work in just 90 minutes") with no method; post-release impact measurement still "rolling out progressively after GA"; an AI-assisted review aggregator (rfp.wiki) calls Pulse/Spark insights uneven depending on feedback volume and setup.

Key URL: https://www.productboard.com/blog/introducing-spark-ai-product-management-agent/

Sources: [Spark public-beta post](../../research/sources/productboard-introducing-spark.md) · [Support/GA](../../research/sources/productboard-spark-support-article.md) · [June 2026 relaunch](../../research/sources/productboard-introducing-spark-agentic-product-system.md) · [Pricing](../../research/sources/productboard-pricing-spark.md) · [MCP](../../research/sources/productboard-mcp-server-spark.md)

## 3. Amplitude AI agents, MCP, AI Feedback
Global Agent plus four specialized always-on agents (Dashboard Monitoring, Session Replay, Web Experimentation, AI Feedback) and MCP (launched 2026-02-17); jobs: metrics review, feedback synthesis. Evidence LOW: AskNicely story (75% is one self-reported example: a dashboard built in under an hour instead of about half a day, credited to Amplitude AI Agents before Global Agent launched), Replit quote without a number, customer counts that rise over time (4,500 in Feb 2026 coverage, 4,900 in current boilerplate). No limits found, reflecting lack of independent coverage.

Key URL: https://amplitude.com/blog/amplitude-ai-agents-launch

Sources: [Launch](../../research/sources/amplitude-ai-agents-launch.md) · [AskNicely](../../research/sources/amplitude-asknicely-story.md) · [AI Feedback coverage](../../research/sources/siliconangle-amplitude-ai-feedback.md)

## 4. Pendo Agent Analytics / Novus
Agent Analytics measures a company's own AI agents (GA 2025-12-17), not a PM agent; Novus is the PM-adjacent product-fix agent (sign-up/early access per Pendo site banners, unverified; no named customers; runs on Claude Managed Agents, built with the Agent SDK; self-reported 90% success on PM-reviewed evals). Evidence LOW: Pushpay beta story and a vendor figure of 350+ agents / 2.5M prompts per week (method not given).

Key URL: https://www.pendo.io/news/pendo-lands-on-the-2026-fast-company-most-innovative-companies-list-for-breakthrough-launch-of-agent-analytics/

Sources: [Fast Company/Pendo](../../research/sources/pendo-agent-analytics-fast-company.md) · [Claude customer page](../../research/sources/claude-customers-pendo-qa.md)

## 5. Dovetail (Magic AI, Channels, Ask)
Research synthesis: transcription, summaries, highlight clustering, auto-analysis. Evidence LOW (was LOW-MED; all numbers vendor-published or vendor-commissioned): Instawork 1-2 hours per project (AWS case study), Notion PM 100 hours to 10 and GrandPad about half per interview (Dovetail's Oct 2024 launch release), and a Dovetail-commissioned Forrester TEI (April 2025; 236% ROI from a composite of four interviewees; the Enterprise page's "30 hours/user/week" tile is not in the TEI summary, unverified). Limits: no independent accuracy audit; a competitor review (CleverX) criticises cost, lack of recruitment and weak AI value on small datasets, but reports no test; an arXiv preprint (Long et al., Aug 2025; not Dovetail) found AI inaccuracies of 1.51% vs 4.37% for humans when extracting data from published papers for a literature review, a different task from interview synthesis.

Key URL: https://dovetail.com/blog/news-dovetail-announces-world-first-ai-customer-insights-hub ; https://arxiv.org/abs/2508.09458v1

Sources: [Launch](../../research/sources/dovetail-ai-customer-insights-hub.md) · [AWS case study](../../research/sources/aws-dovetail-case-study.md) · [Enterprise page](../../research/sources/dovetail-enterprise-page.md) · [CleverX review](../../research/sources/cleverx-dovetail-review-2026.md) · [arXiv study](../../research/sources/arxiv-llm-qualitative-extraction-error-rates.md)

## 6. Aha! AI (Elle, Builder, deep research)
Assistant, prototype builder, AI roadmap presentations. No evidence found; G2 user-review data on Aha!'s AI features is thin: one G2 page rates Aha! AI text generation on 12 reviews, and the comparison page shows "Not enough data" for most generative-AI rows (from search summaries; G2 blocked fetch; unverified). LOW.

Key URL: https://www.g2.com/compare/productboard-vs-zeda-io-zeda-io-vs-aha

Sources: [G2 comparison](../../research/sources/g2-productboard-zeda-aha-compare.md)

## 7. Linear Product Intelligence / Linear Agent
Triage suggestions, duplicate detection, agent filing issues from Gong, Intercom/Zendesk and Slack. Job: feedback intake and triage, not discovery. Evidence LOW: docs, changelog and Linear's own dogfooding post (Apr 2026: CX feedback-to-issue via Intercom, dedupe and labels, PM theming and PRDs, human-approved PRs; no figures); none of Linear's 18 customer stories mentions these features; a competitor (BuildBetter) says strong on triage/dedupe, weak on upstream customer discovery (partly out of date: it says Linear can't read Gong transcripts, which the Dec 2025 changelog contradicts). Plan-gated (Business/Enterprise; Gong Enterprise-only). Product Intelligence has been renamed Triage Intelligence.

Key URL: https://linear.app/docs/triage-intelligence (old /docs/product-intelligence returns 404)

Sources: [Docs](../../research/sources/linear-product-intelligence-docs.md) · [BuildBetter guide](../../research/sources/buildbetter-linear-ai-agents-guide.md) · [Dogfooding post](../../research/sources/linear-how-we-use-linear-agent-at-linear.md)

## 8. Notion AI / Custom Agents
Scheduled/triggered agents (public beta Feb 2026); used internally for Slack questions and feedback routing. Evidence LOW (was MED-LOW; vendor-published study, commissioning of MeasuringU not stated): Notion Research "in partnership with" MeasuringU, 218 participants, six markets, four workflows, May 2026: task success 93% vs 59%, 38% less time; Notion-published, workflows unnamed, no significance tests or randomization stated, full report behind a form. Pigment about 70% of employees using them (trade-press relay) and Braintrust "20+ minutes saved per Slack update" (Notion's own customer story) are vendor claims. Internal use for Slack questions and feedback routing is from Fast Company SA (Sept 2025, COO quote), before the beta. Not PM-specific.

Key URL: https://www.notion.com/resources/roi-of-notion-agents

Sources: [ROI study](../../research/sources/notion-roi-of-notion-agents.md) · [Custom Agents coverage](../../research/sources/ecommercenews-notion-custom-agents.md)

## 9. ChatPRD
PRD writing and review. Evidence LOW-MED: Fireside PM (2025-12-15) tested five tools on one PRD task, ChatPRD second behind Claude; qualitative, no rubric, single scenario, author sells coaching. A guide by Aakash Gupta made in collaboration with the ChatPRD team (stated as not sponsored) says "in my testing" PRD time drops from 2 hours to 30 minutes. A competitor (BuildBetter) says ChatPRD lacks a customer-evidence layer, so output depends on what the PM types in; Banani (an AI design-tool vendor) says ChatGPT primed with example PRDs works but needs more setup. Vendor-published named stories: LaunchDarkly (~50% less PRD time; founder Claire Vo's past LaunchDarkly CPO role undisclosed, per search result, unverified), Autodesk (hours to minutes), CallRail (~90%); user counts range from 50k (founder, June 2025) to an undated 250k+, never defined. A competitor list (IdeaPlan) repeats an unsourced Aakash Gupta grading (Claude and ChatPRD both B+, ChatGPT C) with no rubric and ranks its own tool first, so it is discounted. No controlled test. Rating stays LOW-MED only because of the disinterested Fireside PM test.

Key URL: https://firesidepm.substack.com/p/i-tested-5-ai-tools-to-write-a-prdheres

Sources: [Fireside PM test](../../research/sources/fireside-pm-tested-5-ai-tools-prd.md) · [Aakash Gupta guide](../../research/sources/aakashg-chatprd-guide.md) · [Banani review](../../research/sources/banani-chatprd-ai-review.md) · [Customer stories](../../research/sources/chatprd-customer-stories.md) · [Founder post](../../research/sources/chatprd-claire-full-time-on-chatprd.md) · [IdeaPlan](../../research/sources/ideaplan-best-free-ai-prd-generators-2026.md)

## 10. Zeda.io
Feedback collection and AI auto-categorization; roadmap linking not described on the page (unverified); page appears stale (©2024). Product page only; LOW.

Key URL: https://zeda.io/product/collect

Sources: [Product page](../../research/sources/zeda-collect-product-page.md)

## 11. Maze AI (AI moderator)
AI-moderated interviews and analysis. Only an unattributed "200 interviews in 10 days" claim (in Maze's April 2026 "AI moderator, expanded" post, not the linked launch post) and one named customer, LCS, who says it saves "hours of analysis time" with no figure. LOW.

Key URL: https://maze.co/blog/ai-moderator/

Sources: [Maze](../../research/sources/maze-ai-moderator.md)

## 12. Sprig AI
In-product surveys with AI analysis. Evidence LOW: Square "over 100 actionable insights across 5 product areas in its first 6 months" (Sprig customer page; survey outcome, no AI mentioned); aggregator-listed results (Chipper Cash +194%, Nova Credit +47%, Shift +340%) are survey outcomes, not AI outcomes (Nova Credit confirmed on sprig.com; the other two not found there, unverified); G2 snippets (seen only via search; G2 blocked fetch; unverified) cite confusing pricing, oversold no-code event setup and two "data inaccuracy" tags.

Key URL: https://sprig.com/ai-insights

Sources: [Sprig](../../research/sources/sprig-ai-insights.md) · [Aggregator](../../research/sources/casestudies-sprig.md) · [G2 reviews](../../research/sources/g2-sprig-reviews.md)

## 13. Gong (product-insight use)
Voice of customer from calls via Smart Trackers, Streams and integrations to Productboard/Canny. Vendor recipes; TrustRadius reviews mention pricing and occasional transcription errors (accent complaints appear on G2/Capterra, not verified on TrustRadius). LOW. Chorus (ZoomInfo) offers similar call-based voice-of-customer "market intelligence" but its page shows no PM workflow, agent or outcome data (vendor-claim).

Key URL: https://gong.io/?p=41718 (now resolves to the Gong homepage; recipe content seen via search index only) ; https://collective.gong.io/integrations/productboard

Sources: [Gong](../../research/sources/gong-product-insights.md) · [TrustRadius](../../research/sources/trustradius-gong-reviews.md) · [Chorus](../../research/sources/zoominfo-chorus-product-page.md)

## 14. Intercom Fin
Support agent, relevant to PMs only as a feedback source. Resolution claims conflict (51% average / up to 86% Anthropic, 56% within 30 days AWS (undated, 4,000+ customers), 76% across 12,000+ customers Intercom homepage; Lightspeed up to 65%, Synthesia 6,000+ conversations and 1,300+ hours saved in six months); all vendor/partner. LOW (was LOW-MED) for support; no evidence it improves PM decisions.

Key URL: https://www.anthropic.com/customers/intercom

Sources: [Anthropic story](../../research/sources/anthropic-customers-intercom.md)

## 15. Mixpanel Spark / Agent / MCP
Metrics Q&A (Spark, July 2023, now Mixpanel Agent), KPI Monitoring and Root Cause Analysis agents, MCP with Verified Mode (limits AI to admin-approved data). Vendor pages only; LOW.

Key URL: https://mixpanel.com/ai

Sources: [Mixpanel](../../research/sources/mixpanel-spark-agent-mcp.md)

## 16. Figma Make
Prompt-to-prototype on Figma designs. Practitioner reviews: edge is reading Figma files, prototype-only, credit quotas strictly enforced per licence since 18 March 2026; a comparison by competitor Playcode reportedly ran no hands-on test (page now redirects; seen only via search summaries, unverified). LOW.

Key URL: https://salesdorado.com/ia/avis-figma-make/

Sources: [Salesdorado](../../research/sources/salesdorado-figma-make-review.md) · [Playcode](../../research/sources/playcode-figma-make-vs-lovable.md)

## 17. Vercel v0
Prompt-to-UI/app. Avalara story (two patent-pending products in roughly 60 days; vendor customer story) is not PM-specific; a practitioner moved Bolt to v0 to Lovable. LOW.

Key URL: https://vercel.com/customers/how-avalara-turns-pipedreams-into-patent-pending-with-v0

Sources: [Avalara](../../research/sources/vercel-case-studies-avalara.md) · [Arteeva](../../research/sources/annaarteeva-choosing-ai-prototyping-stack.md)

## 18. Lovable (and Bolt)
Prompt-to-app for non-engineers; PM job: prototypes for intent shaping, alignment, concept tests. Evidence MED: Product Talk (2025-08-13), 11 named practitioners, unsponsored (article states no compensation and no Lovable input). Results (EQS about 1 hour vs about a week; TimelyCare about 6 hours; Kallidus UI about 5 minutes; Shankaran 11 days idea to validation, setup time down up to 75% estimated), all self-reported. Limits: brand inconsistency, breakage with complexity, Supabase login slowdowns at TimelyCare (0.5s to 25s), claimed-but-unmade fixes, prototypes too real, about half (5 of 11) moved design work to Figma, Stitch or a design system for production; Cursor was only suggested by one team. Vendor side LOW: Zendesk six weeks to three hours (Lovable Series B post, repeated by tech.eu), unnamed ride-share firm six weeks to five days, 50% bids a goal.

Key URL: https://www.producttalk.org/ai-prototyping-lovable/

Sources: [Product Talk roundup](../../research/sources/producttalk-ai-prototyping-lovable.md) · [tech.eu](../../research/sources/techeu-lovable-330m-raise.md)

## 19. Claude Cowork / product-management plugin
Role plugin (anthropics/knowledge-work-plugins, verified against the repo README): specs/PRDs, roadmaps, stakeholder updates, research synthesis, competitive briefs, metrics review, brainstorming. LOW: vendor docs only, no outcome data; InfoQ covers the Cowork launch (2026-01-20), not the plugins; Claude ranked first in the single Fireside PM test.

Key URL: https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management ; https://www.infoq.com/news/2026/01/claude-cowork

Sources: [InfoQ](../../research/sources/infoq-claude-cowork-plugins.md) · [Fireside PM test](../../research/sources/fireside-pm-tested-5-ai-tools-prd.md)

## 20. Cursor / Claude Code for PMs
PRDs against the real codebase, MCP push to Confluence/Notion, Jira tickets, prototypes. LOW: Chime PM Dennis Yang uses Cursor for PRDs, Jira tickets and status reports (How I AI episode, host Claire Vo, who also founded ChatPRD, 2025-10-27); Builder.io (a competing-tool seller) says he turned a PRD into a running prototype with Claude Code in about 20 minutes. Claim that Cursor prototypes are generic (unverified). No failure threads retrieved.

Key URL: https://www.lennysnewsletter.com/p/cursor-is-a-much-better-product-manager

Sources: [Lenny/Builder.io](../../research/sources/lenny-cursor-better-product-manager.md)

## 21. Enterpret
Feedback taxonomy across 50+ channels, agentic platform (Oct 2025), draft-PRD-from-evidence (separate vendor use-case page, anonymised examples). LOW: Canva (hundreds of thousands of survey responses analysed "in hours"), Notion (headline "360%" time saved, undefined; body: monthly report 2 weeks to 3 days); Canva user count varies across versions of the story (170M/200M+/220M); Perplexity named only. A quote attributed to both Canva and Notion could not be found (unverified).

Key URL: https://www.enterpret.com/customers/canva

Sources: [Launch](../../research/sources/enterpret-agentic-feedback-platform-launch.md) · [Canva](../../research/sources/enterpret-canva-customer-story.md) · [Notion](../../research/sources/enterpret-notion-customer-story.md)

## 22. Unwrap.ai
Feedback analytics. LOW: vendor CEO's blog (2025-03-21) cites its GitHub Copilot case study (PMs save 4-5 hours/week) and Sunrun (10x actionable insights); its $180k/yr for 10 PMs is a hypothetical $75/hour calculation, not a customer result. An affiliate review site (TheCXLead, which also runs Unwrap partner content) praises traceability; no outcomes tested.

Key URL: https://www.unwrap.ai/post/unwrap-roi

Sources: [Vendor ROI](../../research/sources/unwrap-roi-blog.md) · [TheCXLead](../../research/sources/thecxlead-unwrap-review.md)

## 23. Kraftful (Amplitude) and Birdie
Kraftful's AI Feedback became Amplitude AI Feedback (Replit quote only); Birdie has no case study; Pendo acquired Zelta AI on 2024-07-31 (Pendo press release; not in CB Insights as previously stated); Kraftful acquired by Amplitude July 2025. LOW.

Key URL: https://www.cbinsights.com/company/birdie-2/alternatives-competitors

Sources: [Amplitude AI Feedback](../../research/sources/siliconangle-amplitude-ai-feedback.md) · [CB Insights](../../research/sources/cbinsights-birdie-alternatives.md)

---

## Cross-cutting observations
- Evidence ladder as found: independent/disinterested practitioner roundup (Lovable, MED) > single-author disinterested test (ChatPRD, LOW-MED) > everything vendor-published, all LOW: vendor study with an outside firm or commissioned analyst (Notion/MeasuringU, Dovetail/Forrester TEI) > named-customer vendor stories (Dovetail, Procore on Rovo, Unwrap, ChatPRD) > vendor launch material/testimonials (Spark, Amplitude, Mixpanel, Pendo Novus). The re-check moved single-author tests above vendor stories: a disinterested informal test is weak but not self-interested.
- Analysts frame PM agents as part of SDLC orchestration (Forrester, June 2026 blog) or an "AI product management platform" category (Gartner Market Guide, May 2026, paywalled; seen only via search), not as standalone agents; no analyst evaluation of these products was readable.
- Time-saved claims are almost all "hours per task" self-reports; none measure decision quality, prioritisation correctness, or product outcomes.
- Reported failure modes are consistent: hallucinated or invented content (Rovo, relayed by competitor/partner sources), silent omission (research synthesis, general; unverified: the CleverX source cited for it contains no such warning), brittleness as prototype complexity grows (Lovable), generic output when context is thin (ChatPRD, Cursor; unverified: the sources only say ChatPRD output depends on PM-supplied context), outages (Rovo).
- Jobs best covered by agents: prototyping and intent shaping (Lovable), feedback intake/synthesis (Enterpret, Unwrap, Dovetail, Linear), first-draft specs (ChatPRD, Spark, Rovo). Weakest evidence: prioritization and stakeholder comms as agent jobs.

## Could not verify / gaps
- Gartner: a Peer Insights market "AI product management platforms" and a "Market Guide for AI Product Management Platforms" (2026-05-06, Nabeeha Ahmed; https://www.gartner.com/en/documents/7814917) exist, and a "Hype Cycle for Chief Product Officers, 2026"; all Gartner pages returned 403, so no vendor list, ratings or findings were read (search summaries only, unverified). Forrester: no PM-software Wave/Landscape found; its only readable relevant text is a June 2026 blog ([Forrester](../../research/sources/forrester-agentic-software-development-sdlc-agents.md)) saying PMs vibe-prototype and generate specs within orchestrated SDLC agents, and that coding-only AI lifts team productivity under 10% (unsourced). No analyst has evaluated any of the 23 products as a PM agent.
- No G2 or other independent head-to-head of AI PM tools with a disclosed rubric, task set or n was found; "tested" roundups found were all vendor- or competitor-published. Dovetail's Forrester TEI located but Dovetail-commissioned (vendor-claim); its 30 hours/user/week tile not found in the TEI summary.
- Tempo/Rovo metrics: neither Atlassian nor Tempo discloses a baseline, sample or method.
- Spark exact GA date and any Spark-specific G2/Capterra review not found.
- Aha! AI, Zeda.io, Mixpanel, Pendo Novus, Birdie, Kraftful: no customer outcome data found. Maze AI: one named customer (LCS) but no quantified outcome.
- Figma Make and v0: no PM-specific named customer stories.
- Bolt not researched individually. Reddit threads not retrieved (search tool returned none).
- Originally most vendor pages were read via search-result summaries. In the 2026-10-24 audit every linked source was re-fetched; these could not be read in full and rest on search summaries or mirrors: G2 (403), TrustRadius (403), TheCXLead (403), Business Wire (403; checked via republications), Gartner (403), Playcode (URL now redirects), Gong recipe (URL now opens homepage), Atlassian customer-page bodies and community threads (do not render), Dovetail launch blog (404; checked via reprint), Linear Product Intelligence docs (404; renamed page read).
- Sprig named results come from an aggregator and are survey-product outcomes, not AI (Nova Credit checked on sprig.com; Chipper Cash and Shift not found there).
