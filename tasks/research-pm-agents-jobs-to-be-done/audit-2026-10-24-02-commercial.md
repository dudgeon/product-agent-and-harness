# Audit of 02-commercial-pm-agents.md (2026-10-24)

Scope: every claim, number, customer name and quote in [02-commercial-pm-agents.md](02-commercial-pm-agents.md). I checked each one against the 45 source notes it links to, then against the original source_url and the extra URLs folded into each note. All web access was read-only (WebFetch/WebSearch).

How the work was split:
- Six opus subagents each re-fetched and corrected one group of notes.
- A seventh opus subagent researched the gaps.
- I applied all changes to the deliverable, INDEX.md and THEMES.md myself, with small line-level edits. I only rewrote lines filed by this task; other tasks' lines were left alone.

## Totals

| | Count |
|---|---|
| Claims checked | about 277 (cases 1/2/6/7/10: 48; 3/4/14/15/23: 58; 5/11/12: 38; 8/9/19/20: 62; 13/21/22: 33; 16/17/18: 38) |
| Errors found and fixed | 57 |
| Still unverified, after re-fetch attempts | 35 claim-level items; 15 "(unverified)" markers in the deliverable |
| Evidence labels changed in notes | 7 (all `independent` to `anecdote`) |
| Other frontmatter fixes | 2 type changes, 1 source_url fixed, 2 source_urls updated, many titles/authors/published dates filled |
| Deliverable ratings changed | 4 (cases 1, 5, 8, 14); rating scale reworded |
| Source notes fixed | 45 of 45. Each now carries an "Audit 2026-10-24" line instead of the "search-result summaries" boilerplate. |
| INDEX lines corrected | about 45; THEMES bullets corrected: about 60 |
| New notes filed | 13, each with an INDEX line and THEMES bullets |

Consistency check after the edits (scripted): all 58 notes (45 existing plus 13 new) have complete frontmatter and non-empty Relevance/Themes/Key points sections. Each has exactly one INDEX line, and its THEMES bullets sit under exactly the theme slugs in its frontmatter.

## Errors found (before -> after, why)

### Cases 1, 2, 6, 7, 10 (Atlassian, Productboard, Aha!, Linear, Zeda)
1. **Procore, beta and OVO figures misattributed** (deviniti-atlassian-ai-statistics-2026).
   - Before: Procore "1 hour to 15 minutes" and the beta "1-2 hours/week" were "relayed secondhand" by Deviniti.
   - Deviniti contains none of them.
   - All three come from Atlassian's own blog, 2025-01-14: Procore Staff TPM Noemi Flores; beta "early feedback" from "thousands", no method. I verified this myself.
   - The deliverable numbers were right in substance; the source and evidence type were wrong (first-party vendor, not partner relay).
   - Filed the new note atlassian-blog-helping-every-team-succeed-ai-era.
   - Deviniti relevance: medium -> low.
2. **"44% accuracy figure has no cited source"**: wrong. It comes from Atlassian's Teamwork Graph blog (Jamil Valliani, 2026-05-06): "Per our benchmarks… 44% more accurate… 48% fewer tokens", with no method. Filed atlassian-blog-teamwork-graph-team-26.
3. **Tempo "3x"**
   - Before: the banner applied to Rovo generally.
   - After: per Tempo's own page, the 3x is one agent (Structure View Builder) on Tempo's own Jira apps.
   - Tempo is an Atlassian Platinum Marketplace Partner.
   - No baseline, sample or method anywhere.
4. **Seibert quote**: the phrase "out of thin air with absolute confidence" is not in Seibert. Seibert says "confidently invented releases". The "absolute confidence" phrase is in Slite, attributed to a community post.
5. **Rovo outages "March 2026"**
   - One community thread, 2026-03-17. Support said "internal issues… resolved".
   - Seen via search only, so marked unverified.
6. **Slite runbook report**: it is a community post relayed by Slite, not Slite's own finding.
7. **Spark** (productboard-introducing-spark)
   - "No named customer metrics" is wrong: the product page has named testimonials, e.g. Praxedo "saved 1 week of work in just 90 minutes".
   - "Post-launch analytics" is not a listed job.
   - The note's source_url is actually "Spark Ignites…" (2026-01-27, public beta), not the October launch.
   - The rfp.wiki quote covers Pulse/Spark, not Productboard AI generally.
8. **Linear**
   - The /docs/product-intelligence URL is dead (404); the feature was renamed Triage Intelligence.
   - Plan gating confirmed: Business/Enterprise, Gong Enterprise-only.
   - BuildBetter's "Linear can't read Gong transcripts" is contradicted by Linear's 2025-12-11 changelog.
9. **G2 "12 reviews"**: these belong to a different G2 page (Aha! AI text generation), per search summaries. Marked unverified; G2 returned 403.
10. **Zeda "linked to roadmap"**: not on the page. Marked unverified; the page also looks stale (©2024).

### Cases 3, 4, 14, 15, 23 (Amplitude, Pendo, Intercom, Mixpanel, Kraftful/Birdie)
11. **Amplitude's agents**
    - Before: "four scheduled agents (dashboard monitoring, session replay, feedback synthesis, web conversion)".
    - After: four specialized always-on agents: Dashboard Monitoring, Session Replay, Web Experimentation, AI Feedback.
    - Launched 2026-02-17.
12. **AskNicely "75% less analysis time"**
    - It is one self-reported example: a dashboard built in under an hour instead of about half a day.
    - It was written by an AskNicely VP on Amplitude's blog (2026-01-06).
    - It credits Amplitude AI Agents and predates the Global Agent.
13. **4,500 vs 4,900 customers**: not a contradiction. They are figures from different dates.
14. **Pendo**
    - "Informing prompt tuning" (the Pushpay story) is not in any source; removed.
    - GA is 2025-12-17.
    - The Novus "early access" claim rests only on site banners; marked unverified.
15. **Pendo-Zelta "per CB Insights"**: wrong attribution. CB Insights doesn't mention it. The acquisition is confirmed by Pendo's 2024-07-31 press release.
16. **Mixpanel "GPT-3.5"**: not on Mixpanel's page. Only a search summary of BigDATAwire supports it; marked unverified. Spark's date is now exact: 2023-07-06.
17. **Intercom**
    - The note missed the Anthropic page's "up to 86%" headline and its 25,000+ customers.
    - The AWS 56% figure being "older" is unverified (the page is undated).

### Cases 5, 11, 12 (Dovetail, Maze, Sprig)
18. **CleverX** (fabricated claim)
    - Before: "a competitor warns of fabricated quotes and silent omission".
    - The CleverX article contains no such warning; it was checked twice, by keyword.
    - Its real criticisms: cost, no participant recruitment, weak AI value on small datasets. No test.
    - The agent-failure-modes theme was removed from the note and its THEMES bullet deleted (this log is the record).
    - The deliverable's cross-cutting "silent omission" now says unverified.
19. **Dovetail Forrester**
    - Before: "Forrester-verified ROI (30 hours/user/week) not located".
    - After: a Forrester Consulting TEI exists (April 2025) and was commissioned by Dovetail, so it counts as vendor-claim.
    - It reports 236% ROI from a composite of four interviewees, and 36,000 hours over 3 years (about 2.3 h/user/week).
    - The Enterprise page's "30 hrs/user/week" tile is not in the TEI summary; marked unverified.
20. **Notion PM "100 hours to 10" and GrandPad "about half"**: these are in Dovetail's Oct 2024 launch release, not on the Enterprise page.
21. **AWS/Instawork**: "Magic search and cluster" is wrong. The page credits Dovetail's AI features generally (Emi Fogg: "around 1-2 hours per project").
22. **arXiv 2508.09458**
    - Long, Gin et al., 2025-08-13, a preprint.
    - It measured data extraction from 187 published papers for a scoping review, not interview synthesis. The deliverable now says so.
23. **Maze "200 interviews in 10 days"**
    - Not in the linked post; it is in Maze's April 2026 "AI moderator, expanded" post.
    - "No named customer" is wrong: LCS is named, though with no after-figure.
24. **Sprig Square**: the figure is on Sprig's Square customer page, not /ai-insights, and that page does not mention AI.
25. **Sprig aggregator figures**
    - Nova Credit +47% is confirmed on sprig.com and involves no AI.
    - Chipper Cash and Shift were not found on sprig.com; marked unverified.
26. **G2 Sprig**
    - "Best for high-traffic sites" came from Screeb/TrustRadius, not G2.
    - The G2 snippets were seen via search only.

### Cases 8, 9, 19, 20 (Notion, ChatPRD, Cowork, Cursor)
27. **Notion internal use and Braintrust**
    - "Used internally for Slack questions and feedback routing" is from Fast Company SA (Sept 2025), not ecommercenews.
    - Braintrust "significant time savings" is not in the source. Notion's own customer story says "20+ minutes saved per Slack update".
28. **Notion ROI date**: "Published May 2026" was the study date; the page shows no publication date. source_url switched to the English page.
29. **Aakash Gupta guide**
    - "Sponsored" is wrong: the post says "This is not a sponsored post."
    - "Co-written with ChatPRD founders" is wrong: Gupta is the sole byline and "collaborated with the ChatPRD team".
    - The 2h -> 30min claim is verified as "in my testing".
30. **Banani**
    - "ChatGPT with example PRDs can match it" is wrong: Banani says it works but is less convenient.
    - The BuildBetter "memory/consistency issues" claim is wrong: BuildBetter says ChatPRD has no customer-evidence layer.
    - "Generic output when context is thin" is not stated by either source. The deliverable's cross-cutting line now says unverified.
31. **InfoQ**: the article never mentions plugins. The plugin contents were re-sourced to the anthropics/knowledge-work-plugins repo README, and the list was incomplete (it now adds competitive briefs and brainstorming).
32. **Lenny / Chime "20 minutes"**
    - Not in the Lenny piece, which is a How I AI podcast episode hosted by Claire Vo, ChatPRD's founder, published 2025-10-27.
    - It appears only in Builder.io's "Claude Code for PMs" post, and is about Claude Code, not Cursor.
    - "Prototypes can be generic": not found anywhere; marked unverified.

### Cases 13, 21, 22 (Gong, Enterpret, Unwrap)
33. **Unwrap "$180k/yr for 10 PMs"**: a hypothetical $75/hour calculation in the CEO's blog, not a GitHub Copilot result. The 4-5 h/week and Sunrun 10x claims are verified.
34. **TheCXLead "independent review"**: wrong. It is an affiliate site that runs Unwrap partner-spotlight content. Its pages return 403; seen via search only.
35. **Enterpret draft-PRD use case**: not in the launch release. It is on a separate use-case page with anonymised examples.
36. **Enterpret Canva**
    - "In a few hours" -> "in hours".
    - The 125M user count was not found.
    - The quote attributed to both Canva and Notion was not found; marked unverified.
    - The Notion "360%" claim is verified (undefined); the body gives 2 weeks -> 3 days.
37. **Gong**
    - The ?p=41718 URL now opens the Gong homepage; the recipe content was seen only via the search index.
    - The integrations come from marketplace listings.
38. **TrustRadius "missed accents"**: wrong. The only accent mention on TrustRadius is positive; accent complaints are on G2/Capterra.

### Cases 16, 17, 18 (Figma Make, v0, Lovable)
39. **Lovable "most teams moved to Figma/Stitch/Cursor"**: wrong. About half (5 of 11) moved design work to Figma, Stitch, a design system or a designer; Cursor was only suggested by one team (EQS).
40. **Lovable "a student team abandoned it"**: wrong. A student abandoned the Supabase integration, not Lovable, and her team won demo day.
41. **Avalara**
    - source_url pointed to Vercel's case-study index; now the actual story (Nic Vargus, 2026-02-28).
    - "Within months" -> "roughly 60 days".
42. **Playcode**
    - The URL now 301-redirects to a Lovable-vs-Playcode page.
    - The "no hands-on test" claim is supported only by search summaries; marked unverified.
    - Playcode is a competitor.
43. **Zendesk "six weeks to three hours"**: it is in tech.eu and Lovable's Series B post (Jorge Luthe). The note had said it was only on an unfetched Lovable page.

(The count of 57 errors includes smaller wording and date fixes recorded in each note's own audit line, not all listed above.)

## Evidence-label changes (notes)
- playcode-figma-make-vs-lovable: independent -> anecdote. Competitor opinion, no test.
- banani-chatprd-ai-review: independent -> anecdote. Content marketing by an adjacent-tool vendor, no test.
- cleverx-dovetail-review-2026: independent -> anecdote. Competitor (it sells a participant panel).
- thecxlead-unwrap-review: independent -> anecdote. Affiliate site with Unwrap partner content.
- slite-atlassian-rovo-ai-review: independent -> anecdote. Competitor; the author is a Slite employee.
- buildbetter-linear-ai-agents-guide: independent -> anecdote. Competitor.
- g2-productboard-zeda-aha-compare: independent -> anecdote. User reviews.
- Type changes: vercel-case-studies-avalara other -> article; lenny-cursor-better-product-manager article -> podcast.
- Kept, with reasons in the notes:
  - Fireside PM: independent (unaffiliated author, disclosed loose test).
  - Product Talk: independent (states no compensation and no Lovable input).
  - arXiv: independent (academic preprint).
  - Salesdorado and Arteeva: independent, each with a bias note (Arteeva sells a course).
  - Aakash Gupta guide: vendor-claim (made with ChatPRD).
  - Notion ROI: vendor-claim.
  - Dovetail Forrester TEI: treated as vendor-claim because Dovetail commissioned it.

## Rating changes in the deliverable
The original scale put "named customer … vendor-adjacent" at MED. That let vendor-published customer stories and a vendor-commissioned study prop up mid ratings. I reworded the scale: anything vendor-published or vendor-commissioned is LOW, and LOW-MED is reserved for a single disinterested informal test. The deliverable notes the change.

| Case | Before | After | Why |
|---|---|---|---|
| 1 Rovo | LOW-MED | LOW | Every number is published by Atlassian or a partner; the limits come from competitor/partner sources |
| 5 Dovetail | LOW-MED | LOW | Customer quotes published by Dovetail and AWS; Forrester TEI commissioned by Dovetail |
| 8 Notion | MED-LOW | LOW | Vendor-published study; commissioning of MeasuringU not stated |
| 14 Intercom Fin | LOW-MED | LOW | All vendor/partner figures |
| 9 ChatPRD | LOW-MED | unchanged | Rests on the disinterested Fireside PM test; vendor stories added as LOW context |
| 18 Lovable | MED | unchanged | Disinterested practitioner roundup, self-reported |

I also reordered the cross-cutting evidence ladder. Single-author disinterested tests now sit above all vendor-published material; they had been ranked below named-customer vendor stories.

## Other fixes
- Added `docs-as-code-prd` to lenny-cursor-better-product-manager's frontmatter themes, plus a matching Themes bullet in the note. The THEMES.md bullet already existed, filed by user-story-mapping.
- In INDEX.md, link titles were updated to each source's own title where the agents found the real title, and published dates were filled.
- The deliverable's method line now points to this log. The old gaps bullet ("only four pages were fetched") was replaced with the list of sources that still could not be read in full.

## Gaps filled (13 new notes, all filed_by research-pm-agents-jobs-to-be-done)
- **Analysts**
  - forrester-agentic-software-development-sdlc-agents (independent): the only readable analyst text; PMs are framed inside SDLC orchestration.
  - Gartner's "Market Guide for AI Product Management Platforms" (2026-05-06) and its Peer Insights market exist but returned 403. They are recorded in the gaps list as unverified, with no note filed.
- **Independent head-to-heads**: none found with a disclosed method. ideaplan-best-free-ai-prd-generators-2026 is a competitor-published "tested" list, filed as anecdote and discounted.
- **Rovo**:
  - cbtw-atlassian-rovo-real-world-feedback: an Atlassian Platinum Partner admits inconsistent backlog analysis and JQL.
  - devto-tschimev-why-atlassian-rovo-failed-us: a single-team anecdote.
  - No press hands-on test found.
- **Spark**:
  - productboard-spark-support-article: "now generally available", updated 2026-10-22, exact GA date unknown.
  - productboard-introducing-spark-agentic-product-system: June 2026 relaunch.
  - productboard-pricing-spark: credit-metered pricing.
  - The existing productboard-mcp-server-spark note is now linked.
- **Linear**: linear-how-we-use-linear-agent-at-linear, Linear's own dogfooding post with no numbers. None of Linear's 18 customer stories mentions these features.
- **ChatPRD**:
  - chatprd-customer-stories: LaunchDarkly about 50%, Autodesk, CallRail about 90%; all vendor-published, no method.
  - chatprd-claire-full-time-on-chatprd: 50k users in June 2025 vs an undated 250k+; "users" never defined.
- **Chorus**: zoominfo-chorus-product-page. No PM workflow or outcome data.
- **Origins of misattributed claims**: atlassian-blog-helping-every-team-succeed-ai-era and atlassian-blog-teamwork-graph-team-26, both fetched by me.
- Headline unchanged: no independent, controlled evaluation of any PM agent doing a PM job was found.

## What remains unverified, and why
- **Blocked pages (403)**: G2 (Aha! "12 reviews", Sprig snippets), TrustRadius (Gong "missed context"), TheCXLead (Unwrap outcome wording), Gartner (all), Business Wire (Amplitude and Enterpret releases; checked via republications instead). Content was seen only via search summaries.
- **Pages that do not render for WebFetch**: Atlassian customer-page bodies (Tempo body text, current Procore story figures) and community threads (the Rovo outage thread, runbook and "absolute confidence" posts).
- **Pages that moved**: Playcode, where the "no hands-on test" wording, author and date are lost and no Wayback copy was reachable. The Gong recipe URL now opens the homepage.
- **Claims absent from the original**:
  - Mixpanel "GPT-3.5".
  - Pendo Novus "early access" (banners only).
  - Zeda "roadmap linking".
  - Dovetail "30 hrs/user/week" (not in the TEI summary; full TEI PDF not downloaded, as downloads were out of scope).
  - Sprig Chipper Cash +194% and Shift +340% on sprig.com.
  - Enterpret's cross-attributed quote and the 125M figure.
  - "Cursor prototypes are generic".
  - Linear's Slack agent.
  - Spark's "separate workspace" and exact GA date.
  - Whether Notion paid MeasuringU.
  - The AWS Intercom "older" date.
  - Claire Vo's LaunchDarkly role (search result only).
- **Method note**: WebFetch returns a model-summarised view of each page, so short verbatim quotes should be spot-checked before external publication. The gap-research subagent reported that the permission system blocked its curl attempt to work around Gartner's 403; it stopped there.

## Not changed, but worth knowing
- [00-brief.md](00-brief.md) still carries the old ratings: Notion "Med-low", Rovo customers "Low-med", Anthropic "Low-med". It also relays "hallucinated content and outages in Rovo reports (file 02)". Those lines should be brought into line with this audit; I did not edit the brief because it was outside this audit's scope.
- The THEMES slug agent-failure-modes lost one bullet (CleverX) because the claim was fabricated.
