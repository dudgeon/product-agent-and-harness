---
title: "How We Use Golden Paths to Solve Fragmentation in Our Software Ecosystem"
source_url: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem
author: Gary Niemen (Spotify)
publisher: Spotify Engineering
published: 2020-08-17
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [platform-as-a-product, tacit-knowledge-capture, dependency-knowledge-carriers]
relevance: low
---

## Relevance to the project
The origin account of the "golden path": Spotify's opinionated, supported route for building a backend service, website or data pipeline, written as a tutorial in Backstage, created because engineers were learning how to do things by "rumour-driven development". It is optional, but leaving it means losing support. Beacon pattern only: it assumes one engineering organisation with one set of blessed tools, not a product team crossing many platforms owned by different divisions, each with its own controls.

## Themes
- tacit-knowledge-capture: before golden paths engineers relied on "rumour-driven development", which did not scale.
- platform-as-a-product: the path is "opinionated and supported"; leaving it is allowed, but "then you will not have the same support".
- dependency-knowledge-carriers: content ownership is spread across many teams, which created coordination gaps the team was still addressing.

## Key points
- First golden path: a backend tutorial written in a Hack Week about six years before 2020.
- One tutorial per engineering discipline, written with TechDocs, shown in Backstage; tutorials updated when a tool changes; new-joiner feedback keeps them current.
- Golden State: aim to get most of engineering onto the path.
