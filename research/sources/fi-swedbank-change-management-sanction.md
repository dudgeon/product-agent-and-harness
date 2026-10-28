---
title: "Decision: Remark and administrative fine, Swedbank AB (FI Ref. 22-18430)"
source_url: https://www.fi.se/contentassets/ee66531f570f4e738f897d4c15a4b257/beslut-swedbank-2023-03-14-eng.pdf
author: Finansinspektionen (Swedish Financial Supervisory Authority)
publisher: Finansinspektionen
published: 2023-03-14
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [regulatory-drivers-of-process, human-review-gates, policy-enforcement-fail-open, process-governance-load, coordination-cost-and-waiting]
relevance: high
---

## Relevance to the project
The Swedish regulator fined Swedbank SEK 850 million because a change to a business-critical payments system, rushed to implement an EU sanctions decision, bypassed the bank's change process: no CAB approval for a change outside the service window, no risk and impact assessment, no recovery plan, no formal change request or approval, and no notice to the third-party supplier who had already voiced doubts. About 960,000 customers saw wrong balances. It is the counterweight to "CAB is theatre": regulators punish change gates that can be bypassed, so any dependency agent must make the gate easier to satisfy, never easier to skip, and the fix the bank chose was to build process compliance into the system itself.

## Themes
- regulatory-drivers-of-process: the change "should have been assessed and approved by Swedbank's Change Advisory Board (CAB) ... since the change was being made outside of the bank's so-called service window. This was not done" (2.1.2, p. 4); FI found a violation of the requirement on internal control (2.2.3).
- human-review-gates: the CAB must consider "the potential effects in the event a change in the IT environment is not successful", impact on key channels, and "whether the timing of the change in question is appropriate, in part based on when salary payments are made" (2.1.2, p. 4).
- policy-enforcement-fail-open: it "had been possible for employees to assess, decide on, and implement the change in question without control measures or involvement from persons higher up within the organisation" despite first-, second- and third-line review of the change process (bank's statement, 2.2.2).
- process-governance-load: remediation included building "a functionality in the system in question to ensure compliance with the change management process" and more extensive mandatory annual training (2.2.2).
- coordination-cost-and-waiting: the bank "did not inform the third-party supplier that had developed the system ... despite the supplier at an earlier stage having expressed at least uncertainty about the intended change" (2.1.2, p. 5).

## Key points
- Incident 28-29 April 2022: about 1.7 million deposit transactions stopped for about 1.1 million accounts belonging to almost 960,000 customers; about 160,000 customers could not make payments; secondary errors delayed 2.1 million Bank Giro payments and doubled some cash deposits (2.1.3, p. 5).
- Trigger: a manual parameter error while adapting the system to an EU sanctions regulation (2.1.1).
- Deviations listed: no CAB approval, no risk and impact assessment, no recovery plan, no formal change request, requirement specification or formal approval (2.1.2).
- Sanction: remark plus SEK 850 million administrative fine; Swedbank described as systemically important.

## Notable quotes
- "The change was also implemented without Swedbank having conducted any risk and impact assessment and preparing a recovery plan." (2.1.2)
