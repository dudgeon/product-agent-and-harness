---
title: "Assigning Trust to Wikipedia Content"
source_url: https://tr.soe.ucsc.edu/sites/default/files/technical-reports/UCSC-SOE-08-07.pdf
author: B. Thomas Adler, Krishnendu Chatterjee, Luca de Alfaro, Marco Faella, Ian Pye, Vishwanath Raman
publisher: UC Santa Cruz technical report UCSC-SOE-08-07 (WikiSym 2008)
published: 2008-05
retrieved: 2026-10-31
type: paper
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms]
relevance: high
---

## Relevance to the project
WikiTrust is the most worked-out "trust by use with corrections" mechanism: each word's trust comes from the reputation of its author and of everyone who later edited near it without removing it, so text gains trust only by surviving scrutiny by several people. It bears directly on which trust mechanism to use for written-back context, and it supplies measurable definitions (precision and recall of low-trust labels against later deletions). Its key limit: it is validated against stability, not truth, and the authors say so. The evaluation is by the system's builders.

## Themes
- context-trust-mechanisms: text in the bottom half of trust values is only 3.4% of article text but 66% of text deleted in the next revision; it has a 33% chance of being deleted in the very next version against 1.9% for text in general, rising to 62% for the bottom 20% (section 1, summary of results; section 5). Measured on 1,000 random English Wikipedia articles with at least 200 revisions.

## Key points
- Mechanism: author reputation comes from how long the author's edits survive (content-driven reputation, Adler and de Alfaro, WWW 2007); word trust combines the original author's reputation with that of later editors who left the text in place; deleted text is tracked so it cannot be laundered by delete and re-insert (sections 2-3).
- Design rule worth copying: "high trust requires consensus": a single author cannot raise an article's trust much on their own, and high reputation cannot be acquired quickly (section 3).
- Measured results: 90% of all text had trust of at least 76%, while deleted text averaged 33%; the highest-trust words have an expected future lifespan 4.5 times longer than words with no trust (section 1, section 5).
- Four evaluation measures the project could reuse for its own records: recall of deletions, precision of deletions, average trust of all vs deleted text, and trust as a predictor of lifespan (section 1.2).
- Stated limit: "truth" is poorly defined and expensive to assess by humans, so the system measures predicted stability instead (section 1.2). A record that is wrong but nobody touches will look trusted. In an enterprise store where few people revisit a platform card, stability will mostly mean neglect.
- The authors report only anecdotal evidence that visitors found the coloured trust display useful (abstract).

## Notable quotes
- "high trust should be associated with stability" (section 1.2).
