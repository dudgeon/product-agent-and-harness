---
title: "Black Swan Farming using Cost of Delay"
source_url: https://blackswanfarming.com/black-swan-farming-using-cost-of-delay
author: Joshua J. Arnold, Özlem Yüce
publisher: Black Swan Farming (IEEE-format paper, Agile 2013)
published: 2013-08-01
retrieved: 2026-10-28
type: paper
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [coordination-cost-and-waiting, dependency-value-evidence]
relevance: high
---

## Relevance to the project
The best-documented flow case found from a large traditional enterprise: at Maersk Line, average end-to-end lead time for IT requirements was 150 days, and one mapped feature needed 82 hours of development and test inside a 46-week journey, of which over 38 weeks were waiting (29 in the "fuzzy front end" before work started). Pricing the delay showed that feature costing about $210,000 a week. After introducing cost of delay, smaller batches and queue limits, cycle time on one system roughly halved (208 to about 105 days) and another fell from 168 to 60 days. Written by the consultants who led the work, so it is a vendor claim, but it is unusually specific about where the time goes.

## Themes
- coordination-cost-and-waiting: 82 hours of develop-and-test in 46 weeks end to end, "over 38 weeks" of waiting, 29 weeks in the fuzzy front end (value stream map). By calculation (not in the paper) active time is roughly 4% of elapsed time.
- dependency-value-evidence: cost of delay for the example feature about $210,000 per week, so roughly $8 million over 38 weeks of waiting; the top 25% of requirements were worth about 1,000 times the bottom 25% (power-law distribution).

## Key points
- Baseline: average lead time 150 days over the two years before October 2010; about 24% of requirements took over a year; over 450 enhancements took longer than 510 days.
- Results (authors' figures): GCSS cycle time 208 to 108 days (104 elsewhere in the paper); FACT end-to-end lead time 168 to 60 days; GCSS defects down 88%, delays down 80%, patches down 85%, throughput up 22%.
- FACT survey (1-10): "relative priority is clear" rose from 4.3 to 8.9.
- Changes bundled together (cost of delay and CD3 prioritisation plus other "starter pack" practices), so no single cause is isolated.

## Could not verify
- Independent confirmation by Maersk; internal inconsistencies (108 vs 104 days; ROI given as multiples and as dollars). Publication date approximate (Agile 2013 conference).
