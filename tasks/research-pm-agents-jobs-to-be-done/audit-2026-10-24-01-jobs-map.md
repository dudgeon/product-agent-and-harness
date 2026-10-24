# Audit of 01-jobs-to-be-done-map.md (2026-10-24)

Scope: every claim, figure and quote in the map was checked against its linked source note, and then against the original page (fetched read-only with WebFetch on 2026-10-24). Five Opus subagents did the checking: four fact-check batches and one gap search. Quotes come from WebFetch's extraction, which reads pages through a summarising model, so they are near-verbatim; check against the page before printing any as exact.

## Counts

- **Claims checked:** about 150, across 31 sources.
  - Batch A (Lenny's, Productboard, UXCam, Productside): about 30.
  - Batch B (Atlassian State of Product, Product Focus, ProductPlan, Haberlah): about 25.
  - Batch C (SVPG, Torres, Pragmatic, Samek, Mind the Product, echai): about 35.
  - Batch D (Atlassian/Gupta, Gamma, Reforge, JTBD sources, persona sources, vendor blogs, skill listing): about 60.
- **Errors corrected in the map:** 31. 29 are claim errors (listed below); 2 are structural matrix fixes.
- **Source notes corrected:** 31. All 31 linked notes were touched, with published dates and authors filled where the page shows them.
- **New source notes:** 9 (S32 to S40).
- **Items still unverified:** 16 (listed at the end).

## Errors found (before → after, and why)

### Surveys

1. **Lenny's, S4.**
   - Before: "at least half a day per week" (all respondents).
   - After: more than half of respondents, on their most important tasks.
   - Why: the original limits it to a majority and to their most important tasks.
   - In the note: "over 70% quality gains" was given as a PM figure; it is PMs and founders combined. "Designers 47.5%" is the share of designers saving 4+ hours. Published 2025-12-23.
   - All other S4 figures confirmed: 1,750; 21.5/19.8/18.5/4.7/1.1%; +27.2pp; 19.8 to 44.4%; 63%/83%; 32.9%; 22.3/17.4%; 51%.
2. **Productboard, S5.**
   - Before: "presentations are the top time-saver".
   - After: presentations head the list of top time-savers, but the list is not ranked.
   - Other figures confirmed: 379; 4 hours per task; 98%; 58/54%; 40%; 65% policy; the Turnitin quote. Published 2025-10-22.
3. **Atlassian State of Product sample, S2.**
   - Before: "1,000+ / 1,200+ respondents".
   - After: 700 manager-level respondents (US, Germany, France), fieldwork by Wakefield Research, plus a separate Atlassian AI survey of 521 PMs. 700 + 521 = 1,221, which explains "1,200+".
   - The S2 row in section 3 now says this is a vendor survey; before, it was not flagged as one.
4. **Atlassian time saved, S3.**
   - Before: "close to two hours a day gained".
   - After: half of PMs save 10 to 60 minutes a day; "up to 2 hours" is the top bucket.
   - Why: the event page is dead, and the report's own figures contradict the event copy.
5. **Atlassian burnout, S3.**
   - Before: "burnout rising".
   - After: many feel burnt out.
   - Why: it is a single-wave survey, so it measures no trend.
6. **Atlassian 49%, S2.**
   - Before: "49% insufficient strategy time (search summary only)".
   - After: confirmed in the report PDF as 49% lacking time for strategic planning and roadmap development. "Deep analysis" is a separate item.
7. **Product Focus, S29.**
   - Before: all figures "search summary only".
   - After: the PDF was read and 677, 40 countries, 97%, 64% and 85% are all confirmed.
   - The 97% is "some" improvement; only 32% say significant. The sample is 83% Europe and Product Focus is a training vendor.
8. **ProductPlan.** Before: "37% of companies include product ops (ProductPlan 2024)". After: marked as likely misattributed and not used. Why: no such figure exists in ProductPlan material.
9. **Haberlah, S28.** Before: "638 practitioner voices". After: 638 pieces of content, analysed with LLM help, not 638 people. This is still from search-engine extracts only.

### Frameworks and practitioners

10. **Cagan, S9.**
    - Before: "ownership of value and viability risk is what survives" (written as Cagan's statement).
    - After: a paraphrase of "responsible for value and viability" and "non-creator PMs will be left behind".
    - Why: the "what survives" phrase is not on the page. The other S9 claims were confirmed (published 2025-05-27).
11. **"Product management theater".**
    - Before: attributed to vendor coverage (S10, airfocus).
    - After: attributed to Cagan's own post (S32, 2024-01-30).
    - Why: airfocus never uses the word. What airfocus does support: product leaders should drive the AI discussion, and the delivery-process product-owner role is easy for an AI assistant to dent.
12. **"AI summaries miss 20 to 40%".** Before: shown as "unconfirmed". After: removed, and the removal is noted in the map. Why: the figure was found in no source.
13. **Torres-versus-Claude synthesis comparison.**
    - Before: attributed to echai (S12).
    - After: attributed to Torres's own article (S33, 2025-10-08). It reports that ChatGPT got about 30% of direct quotes wrong or missing.
    - echai is a founder-community resource list, not a Torres summary.
14. **Mind the Product, S30.** Before: "Torres's own piece". After: Eira Hayward's 2021-04-16 write-up of Torres's keynote. The note's evidence field changed from first-party to independent.
15. **Pragmatic, S21.**
    - Before: "Market problems and win/loss" were cited to the article, and the 7 category names to a third-party page.
    - After: both come from Pragmatic's own framework page (https://pragmaticinstitute.com/product/framework/), which lists 37 boxes in 7 categories.
    - The article does confirm 37 activities and "complete each one and hand it off".
16. **Samek, S13.** Before: "one-page interview snapshots". After: "interview snapshots". Why: "one-page" is not stated.
17. **Torres podcast, S11.**
    - Before: "expert plus AI beats either alone".
    - After: beginner plus AI beats nothing, and the real gains come from expert plus AI.
    - Why: the source never compares expert plus AI with an expert alone. The other S11 claims were confirmed (published 2025-12-02).
18. **Gupta, S14.** Before: "deciding what to build" listed as a human-held task. After: removed. Why: the phrase is not in that article; it belongs to S15. Human-held per S14 is governance and review "where judgment still matters".
19. **Gamma, S15.**
    - The 1:10 comparison and "discernment" are the Atlassian author's narration, not the Gamma co-founder's words.
    - "Alignment on priorities remains a persistent challenge" was a paraphrase; it is now worded as the article's closing question.
    - Speakers: Jon Noronha (Gamma) interviewed by Tamar Yehoshua. Byline Peter Morris, 2026-05-06.
20. **Reforge, S16.**
    - The "more valuable" and "less protected" lists are the map author's synthesis; the page gives no such lists. "Feature-level execution" is not on the page.
    - "Agents do not yet supply project state" is an inference.
    - Date 2026-07-31; no byline.
21. **JTBD Radio, S18.** Before: "jobs are verbs" (Traynor). After: Bob Moesta's line, which Traynor endorses.
22. **CustomerThink, S19.** Importance/satisfaction ratings and the "5x success" claim are not on the page; both are now marked (unverified). Author: Ulwick (Strategyn), posted by Chris Lawer, 2010.
23. **The Technical PM, S22.** Before: "technical PM owns developer experience". After: "writes detailed technical requirements". Why: developer experience is not on the page.
24. **Parallel, S23.** Before: "owns tool stack". After: "manages and standardises tools". Also, the single source of truth is for the roadmap, not for feedback.
25. **LaunchNotes, S24.** Board communication and product-ops bench-building are not on the page. Board communication is now marked (unverified) in P2, and the J2 outputs were corrected.
26. **Product School, S25.** Before: PMM owns positioning, messaging and tiering, with PM and engineering as partners; pricing shared; a "launch measurement plan" as an output. After: a checklist addressed to PMMs, with only timing named as a PMM decision and the other items listed without owners. Why: the earlier claims are not supported by the page.
27. **CleverX, S26.** Goals and acceptance criteria are not on the page. PRD contents corrected to user stories, KPIs, edge cases and out-of-scope.
28. **Claude skill listing, S31.**
    - Before: outputs listed as bug escalations and discovery inputs.
    - After: a ranked pain-point table, opportunity areas, a sentiment split and suggested experiments.
    - The second skill's URL was added: https://claudskills.com/skills/customer-feedback-triage/.
29. **MindStudio, S27.**
    - The 80% claim is now quoted exactly and marked uncited (unverified).
    - Its synthesis agent clusters themes, flags urgent issues and writes weekly summaries. It does not produce "bug escalations".

### Matrix and structure (reasoning check)

30. **J3 row.** Before: four leads in one job (PM, tech PM, design, engineering). After: design and engineering marked C with the risk they own named, and the legend explains this.
31. **Product-ops persona row.** J10 was missing even though the J10 card cites product ops; it has been added.

### Confirmed with no change needed

- SVPG Four Big Risks: confirmed (2017-12-04; "Product Lead Engineer").
- SVPG Discovery – Judgement (2020-09-10): the feasibility warning is confirmed, replacing the earlier "search summary".
- UXCam: 157, 34 countries, 99%, 70%, 70%/6% all confirmed. No date shown; the size of the leaders sub-sample is unknown.
- Productside: 250+, 4 in 5, 1 in 4 confirmed.
- Gupta: "70 to 80% of emails" is quoted correctly.
- ProductPlan: "over 60%" confirmed as marketing copy.
- Torres podcast: 15 interviews confirmed.

## Reasoning check: findings

- **Vendor claims and independent evidence were mixed together.**
  - The S2 survey row was unflagged as vendor-run.
  - Section 7 listed vendor-hosted statements (S14, S15, S26) alongside practitioner ones with no weighting; it now carries a weighting note.
  - Several "practitioner" statements were really the map author's synthesis (Reforge lists, the Gupta task sort). They are now labelled as synthesis.
- **Judgment ratings vs. job cards.** The ranking table matched the job cards. I added a caveat below the table:
  - The High rating for PRD first drafts is about effort, not value. S34 shows PMs hold specs back as accountability-heavy, and S35 calls faster PRD output the weak-team pattern.
  - The Low rating for strategy is contested by S40, Lenny's 2024 opinion piece, which rates strategy and goals the most AI-disrupted PM tasks (4/5).
- **Gaps filled.** The map had no first-hand Cagan writing on AI, no Torres article of her own, no Lenny "AI and the PM job" piece, and no experimentation source. All four are now covered (S32 to S40). Microsoft's study of 885 PMs with telemetry (S34) is the only source in the set backed by usage logs. It reports lower AI use for research (22%) and prototyping (12%) than the map's "High" ratings for J1 and J3 might suggest.
- **No Pendo or Product School first-party report with readable figures was found.** Pendo figures exist only on secondary blogs. No independent survey of how PM time splits across jobs exists in what we found.

## New source notes (filed_by research-pm-agents-jobs-to-be-done, filed_note audit 2026-10-24)

S32 svpg-product-management-theater · S33 producttalk-customer-interview-analysis-ai · S34 arxiv-pm-delegating-work-to-genai · S35 svpg-ai-productivity-paradox · S36 svpg-experimentation-ai-product-model · S37 svpg-prototypes-vs-products · S38 producttalk-generative-ai-discovery · S39 producttalk-ai-playbook-first-ai-product · S40 lenny-how-ai-will-impact-product-management.

Each has one INDEX.md line and THEMES.md bullets under its frontmatter themes.

Candidates read but not filed: SVPG "A Fresh Definition of The Product Role" (2026-08-10), SVPG "AI Product Management 2 Years In", and Lenny "Why PMs are best positioned to thrive in an AI world" (summarised inside S40).

## Library housekeeping

- **THEMES.md.** The coordinator had re-added the 31 notes' bullets and the four missing theme sections. I corrected 23 bullets where these fixes changed the claim, and appended 32 bullets for the new notes.
- **INDEX.md.** The 9 new lines are appended. The existing INDEX lines for the 31 corrected notes still show "unknown" published dates, and some gists are now stale (for example Product Focus, Mind the Product Torres, and echai). I left them because the README makes INDEX append-only. The director may want to allow a one-off refresh.
- **Duplicate Torres podcast note.** Already merged by the coordinator. The survivor is producttalk-torres-customer-interview-analysis-podcast.

## Still unverified, and why

1. Mind the Product's own wording of the 49% sentence: the page is mostly script and the sentence could not be extracted. The report figure is confirmed.
2. The Atlassian event page's "close to two hours a day": the page now redirects to an error. The figure was replaced with the report's numbers.
3. ProductPlan's over-60% measure and sample: the report is gated; only marketing copy was confirmed.
4. Haberlah (S28), all claims: Medium returns 403 and mirrors fail; search-engine extracts only. Author probably David Haberlah; date unknown.
5. Gupta's "70 to 80% of emails": quoted correctly, but there is no evidence for the effect.
6. Pragmatic's "hand off to the next function": the sentence was cut off in extraction.
7. ODI importance/satisfaction ratings and Strategyn's "5x success": not on the CustomerThink page.
8. Intercom Job Stories as "context and trigger rather than persona": secondary summary only.
9. Product School "roadmaps giving way to principles": a secondary WebProNews claim.
10. haveignition.com PMM postings: search-summarised only.
11. CPO board communication: not on S24.
12. MindStudio's "80% of customer feedback never gets analyzed": the vendor gives no citation.
13. HBS: the product-category half of the segmentation point is a paraphrase.
14. Atlassian State of Teams 2026 (89% / 6%): cited secondhand by Cagan in S35, not read.
15. S32 and S33 quotes: read through a summarising extraction, and S33 is partly paywalled.
16. Torres's "15 interviews" (podcast) vs the 17 transcripts in her glossary post vs the two transcripts with numbers in S39: possibly different experiments, not reconciled.
