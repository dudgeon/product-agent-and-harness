# Audit log: 03-in-practice-cases-and-failures.md

Date: 2026-10-24. Scope: every number, quote, attribution and date in the deliverable, checked against its source note and, where the note was thin or summary-based, against the original URL (read-only WebFetch/WebSearch). Atlassian claims checked against the primary transcript (`lenny-podcast-tamar-yehoshua-roles-expanding.transcript.md`); Ramp claims against the Charles transcript and Glyman's launch post.

## Counts
- Claims checked: about 115 discrete claims (numbers, quotes, attributions, dates, quality labels) across the 20 cases, the headline, the failures section and the gaps list.
- Errors fixed in the deliverable: 21 (listed below).
- Quality/type labels changed: 6.
- Source notes corrected: 29 (all filed by this task; Ramp notes from competitive-teardown-ramp-glass were read but not edited; one THEMES bullet appended for the Charles note).
- New notes: 2 (`mit-nanda-genai-divide-2025`, `stanford-cheng-sycophantic-ai-science-2026`), each with an INDEX line and THEMES bullets. `producttalk-customer-interview-analysis-ai` was filed concurrently by another audit; it is now linked from case 14.
- INDEX: 25 of this task's lines refreshed (titles, dates, wrong gists); 2 appended. THEMES: 11 of this task's bullets corrected; 6 appended.

## Errors fixed (before -> after, why)
1. **Ramp 85% (headline, table #1, case 1).** Before: Glass answers 85% of PM-directed questions. After: "85% of questions that are being asked to PMs now are fully answered with AI" (13:01) is credited to Gadget, the coordination agent, not Glass. Why: in the transcript the 85% closes the Gadget/coordination section (11:00-13:05), after Glass (6:30-7:55).
2. **Ramp ~20k/month (case 2).** Confirmed (about 300 hand-entered into Salesforce -> 20,000/month; 5,000+ emails; 323 employees, 6,500+ edits; Router 30%). Added that ramp.com/blog/introducing-glass is the same Glyman text dated 2026-10-13; quality Med -> Med-low (CEO launch claim).
3. **Atlassian weekly-update agent (table #3, case 3).** Before: "PM-built Rovo weekly-status agent". After: an agent the PM built inside Rovoclaw, the 0-to-1 product (the transcript says Rovoclaw "was not a feature on Rovo"). The 900+ items came from Jira user-study videos.
4. **Meta author and title.** Before: Lenny Rachitsky; "Meta VP's personal agents". After: Nikhyl Singhal (The Skip), cross-posted by Lenny; "How Meta Is Reinventing Product Management", 2026-06-24.
5. **Meta "sponsored".** Before: "sponsored". After: the post has a "Brought to you by" block (Glean, Framer); the content is not labelled sponsored and does not tie the agents to the sponsors.
6. **Meta PRD.** Before: "PRD replaced by problem statement + prototype + evals". After: a paragraph + prototype, with an eval set for ML-heavy work. The intro's "every team" overstates the body.
7. **Meta tuning.** Before: "about six months of tuning". After: the system compares its predicted comments with his real ones each night, and "Six months in, it's accurate". Added that it is his personal "N of one" system and runs only in parts of his org. The dropped source links are confirmed.
8. **Intercom "100+ skills" (table #9).** Not in the Intercom post or the Lenny page; found only in a secondary newsletter about engineering. Marked unverified.
9. **Intercom Lenny episode.** Before: Lenny Rachitsky, date unknown. After: Claire Vo's How I AI with Brian Scanlan, 2026-04-20. The "wrong-source errors noted" wording was softened: the post describes a fix process, not an incident.
10. **Torres quote (case 14).** Before: "AI sifts and sorts, humans understand and decide" given as Torres's words. After: this is Vistaly page copy on Product Talk (Torres designs Vistaly's AI), not a Torres quote. It is not on the glossary page.
11. **Torres sample size (coordinator item).** Before: 17 (glossary) and 15 (podcast) given without reconciling them. After: these are separate pages: the glossary says ChatGPT on 17 transcripts; the podcast show notes (2025-12-02) say 15 interviews through ChatGPT and Claude. A third page, "Where AI Helps and Hurts" (2025-10-08), says about 30% of ChatGPT's direct quotes were incorrect. No page says whether 15 and 17 are one experiment, so both figures stay with their sources and the link is marked unverified. Both notes are updated, and the deliverable now links the merged `-torres-` podcast note.
12. **Linear (table #18, case 18).** The essay is now read (2026-10-15). It never says "additive drift": that was the Spanish summary's wording. "Losing learning from struggle" is not in the essay; it is from the PMS summit write-up.
13. **Cagan (table #19, case 19).** Before: "AI exposes PM theater", "PMs not essential everywhere", "no first-party text". After: Modern CTO #950 (2026-06-03) is Cagan's own words, from the transcript: the bottleneck is deciding what to build; "theater" is people with the title but no control over what is built; one-click AI PRDs can "speed up a bad process". "Not essential everywhere" overstated him.
14. **Krieger and Dill attribution.** Before: note.com was the source for "100% right", "every bet needs one decision owner" and "make editing a job". After: only "You were 100% right" is in note.com (2026-10-10). The decision-owner, editing, Saarinen-struggle and Cagan "avoid thinking" lines are from the PMS write-up (André Marquet, 2026-09-28).
15. **Vercel (table #16, case 16).** The real title is "What we learned building agents at Vercel" (Ubl, Dodds, 2025-11-06). The 10->1 lead triage and the 59% cut in time to ticket closing are confirmed (baseline unstated). The post does not mention d0 (d0 "most popular" is from SaaStr) and names no "GTM engineer, data scientist, SME" builder team, so that is marked unverified.
16. **Atticus Li.** Before: "user stories fitting any product, obvious metrics, missing error states"; "course incentives". After: the post says AI PRDs "read well but often lack the specificity". It blames mostly context and partly model habits, says AI is good at edge cases, and the author sells CRO consulting. Date 2026-04-07.
17. **404 Media.** The Kiro leaderboard shutdown is not on the visible (paywalled) page, so it is marked unverified. Author Emanuel Maiberg, 2026-06-09. The tool is described as an AI coding product.
18. **MIT NANDA.** Before: "press only, contested method", read via Fortune. After: the primary was read through a PDF text extraction. The report says "95% of organizations are getting zero return"; success means beyond pilot with measurable KPIs at six months, self-reported. Method: 52 interviews, 153 surveys, 300+ public initiatives, Jan-Jun 2025. The report's own limitations admit selection bias and "directionally accurate" figures. External ~67% vs internal ~33% (so "about 2x" holds), as correlation, not causation. Fortune's sample (150/350) does not match the report.
19. **Gartner.** Before: forecast from secondary coverage, date 2025-06. After: press release 2025-06-25 (URL recorded; returned 403). Causes: escalating costs, unclear value, inadequate risk controls. About 130 "real" agentic vendors. It is an analyst prediction with no stated method; the only data is a January 2025 webinar poll of 3,412.
20. **Microsoft (table #12, case 12).** The blog body still does not render. Orchestrator detail, internal-vs-reference status, Punch List and the Nadella remark are all marked unverified, and quality goes Low-med -> Low. A first-party GEM post (2026-09-08) was found but also does not render (unverified).
21. **Block (table #11, case 11).** "8 to 10 hours weekly" is a chapter teaser on a paywalled page; PMs are not mentioned, so the PM-comms use is marked unverified and quality goes Low-med -> Low. Date 2025-10-26.

Also confirmed without change: NN/g findings and date (2024-06-21); ISPOR "11%-25%" (now read directly: Copilot, 10 payer interviews, denominator unstated); Turku (17 expert interviews, DeepSeek R1; abstract only); Notion co-founder feedback agent (confirmed verbatim; the standup/OKR customer examples in the note were wrong and are corrected); Zapier 89% / 800+ (page moved to claude.com, undated); Anthropic Managed Agents post (Jess Yan, 2026-04-29); Cowork (2026-01-30, 11 plugins, research preview); Anthropic teams (2025-07-24); Brex 3-4x (2025-10-30); Spotify shortcuts (2026-03-18); Raviv checklist (visible part); all Atlassian transcript figures in the correction box.

## Label changes
- Table #2 Med -> Med-low; #11 Low-med -> Low; #12 Low-med -> Low; #18 Med -> Med (opinion), source "Essay via summary" -> "Essay (read)"; #19 source "Summaries" -> "Podcast transcript (read)".
- `moderncto-marty-cagan-2026` type article -> podcast.
- No `evidence:` labels changed; all checked as honest.

## Reasoning check
- **Vendor/speaker claims as success.** The table labelled most of them, but the headline and case 1 gave Ramp's 85% to Glass. I added a framing paragraph: none of the 20 cases is an independently measured success, and nearly all numbers are self-reported.
- **Gaps filled:**
  - METR RCT: existing note linked, with the felt-vs-measured speed paragraph.
  - Sycophancy: new Science/Stanford note.
  - Torres's 2025 "Helps and Hurts" article: ~30% wrong quotes, linked.
  - Cagan on AI PRDs: from the podcast transcript.
  - MIT primary: new note.
- **Still not found after re-search:** first-party PM-agent write-ups from Shopify, Figma, Duolingo or Amazon (PRFAQ results are third-party skills only), and no SVPG article on AI PRDs.

## Notes fixed
404media-amazon-employees-mock-ai-slop, anthropic-cowork-plugins-product-management, anthropic-customer-story-zapier, anthropic-how-teams-use-claude-code, anthropic-product-development-agentic-era, atticusli-ai-prd-generation, bisbee-synthetic-replacements-survey-data, buildbetter-ramp-ai-product-factory (superseded line added to Relevance), claude-brex-claude-code, dealroom-ramp-ai-build-factory-summary (Gadget attribution), fortune-mit-nanda-95-percent-pilots, gartner-agentic-ai-40-percent-cancelled, infoq-spotify-honk, intercom-we-gave-claude-code-to-everyone, ispor-2025-ai-thematic-analysis-payer-interviews, lenny-newsletter-how-intercom-2xd-engineering, lenny-newsletter-meta-chawla-pm-leader-agents, lenny-newsletter-tal-raviv-pm-agents, lenny-podcast-block-dhanji-goose, linear-saarinen-someone-behind-the-software, microsoft-feedback-noise-multi-agent, moderncto-marty-cagan-2026, note-krieger-pm-summit-remarks, notion-introducing-custom-agents, productmanagementsociety-ten-things-lenny-summit, producttalk-ai-hallucination-glossary, producttalk-torres-customer-interview-analysis-podcast (plus missing human-judgment-pm-jobs THEMES bullet), utu-turku-llm-qualitative-analysis, vercel-sweet-spot-agentic-ai.

The Dealroom Atlassian, Dealroom Ramp and PMS notes already said they were superseded by the primaries. BuildBetter now says so too.

## Remaining unverified (and why)
- Microsoft feedback system, Punch List, Nadella remark, GEM: the pages render only a title, or the reports were not read.
- Intercom "100+ skills": secondary newsletter only.
- Block PM usage: paywalled.
- Kiro leaderboard: paywalled.
- Vercel builder roles: not on the page.
- Zapier and Brex PM job posts: not re-checked.
- Gartner release (403) and Stanford/Science paper (403): content from search snippets of the abstracts and releases.
- Turku: portal bot-blocks fetches, so title and authors are unconfirmed.
- Bisbee: full text unread.
- Torres: whether 15 and 17 are one experiment is not stated anywhere.
- Publish dates still unknown for Zapier, Microsoft, Turku, Product Talk glossary (last updated 2026-09-02), Dealroom x2, BuildBetter.
- Atlassian State of Product 2027: unread.
