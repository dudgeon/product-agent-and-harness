---
title: "How this PM uses MCPs to automate his meeting prep, CRM updates, and customer feedback synthesis | Reid Robinson (Zapier)"
source_url: https://www.lennysnewsletter.com/p/how-this-pm-uses-mcps-to-automate
author: Claire Vo (host), Reid Robinson (Principal AI Product Strategist, Zapier)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-02-02
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [pm-tool-connectivity, feedback-triage-agents, org-context-grounding, human-review-gates, work-structure-spectrum, enterprise-admin-controls]
relevance: medium
---

## Relevance to the project
A Zapier PM's own PM workflows built on Zapier MCP plus Claude Projects: daily meeting prep with internal usage lookups, post-meeting CRM and research-log updates, customer interview prep from a data-team lookup, and a support-ticket loop that proposes knowledge-base FAQs for human approval. For the project it is a concrete example of the "analyst agents in" edge and of PM tool connectivity: a per-client, admin-curated tool bundle, and a Claude Project used as a workflow instruction container ("which order it should use tools"). Robinson sells Zapier MCP, so the framing is promotional, but the workflows are his own.

## Themes
- pm-tool-connectivity: Zapier MCP exposes ~8,000 apps and ~30,000 searches/actions; you create multiple servers, each a tool collection for one client (Claude, ChatGPT, Cursor), and can restrict tools, e.g. Coda to certain docs, Evernote to certain notebooks; Claude sees "a single Zapier connector" (4:17-7:40). Vo notes tool-name collisions across MCPs in Cursor ("Always calls the wrong MCP") and calls for tool priority controls (7:40).
- org-context-grounding: Claude Projects hold per-workflow instructions: which tools, in which order, which CRM custom fields mean what (9:08, 14:07); meeting prep pulls the attendee's and company's product usage and past sales interactions, plus Glean search of Slack and CSM notes (11:25-12:56). Big-company users often run "base models with like no additional context" (22:04).
- feedback-triage-agents: every closed support ticket or bot transcript is analyzed for the core issue and fix, checked against the knowledge base, and a new FAQ is proposed; Robinson reviews, edits and approves into the live database (27:11-28:43); the team also auto-generates Coda review pages on emerging feedback trends (25:38); an internal RAG chatbot lets sales, PMMs and designers query feedback (25:38-27:11).
- human-review-gates: the FAQ loop has an explicit human approval step before anything reaches the customer-facing bot (28:43).
- work-structure-spectrum: Vo contrasts her deterministic Zapier flow for the same CRM task with Robinson's natural-language agent instructions (15:26); Robinson: MCP calls "can't take that long", so a seven-minute data lookup belongs in a deterministic workflow, which he uses for interview prep with a Gemini step for file handling (17:02, 20:33-24:09).
- enterprise-admin-controls: enterprises rolling out Claude want each employee, on connecting Zapier, to get "the tools that they should need for their role", created by an ops admin (18:33).

## Key points
- Interview prep: a Databricks-backed lookup (given an email, a write-up of the person and company) runs per meeting; output appended to the Coda page for that interview, where he also takes notes (20:33-22:04).
- "Idea Jammer" Claude Project checks whether similar ideas were explored before and challenges him with set methods (17:02-18:33).
- Vo's prompt for finding use cases: what would "the perfect team with infinite time" do? Robinson's version: "if you could run ChatGPT in your sleep" (29:16-30:54). Zapier found a Mad Libs-style guided prompt helped users discover use cases and pain points (30:54).

## Notable quotes
- "It really just is like app integrations for your AI tools." (Robinson, 0:05)

## Could not verify
- Full transcript read. Demo ran partly against a demo database; production behavior not shown. No reliability or time-saved figures given.
- Published 2026-02-02 per the post; some references suggest it was recorded earlier.
