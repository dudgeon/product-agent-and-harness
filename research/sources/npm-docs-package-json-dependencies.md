---
title: package.json (npm CLI documentation): dependencies and devDependencies
source_url: https://docs.npmjs.com/cli/v10/configuring-npm/package-json
author: npm, Inc.
publisher: npm Docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: define-shaping-and-dependency-agents
themes: [dependency-term-collision]
relevance: medium
---

## Relevance to the project

The canonical statement of what "dependency" means to a software engineer: a package name mapped to a version range, resolved at install time. The project's second module is about delivery dependencies (what another team must build, grant, decide, fund, align or tell), so this note is the reference for the sense the name "delivery dependency mapping" has to be distinguished from. It bears on the naming note in the concept brief and on how the module is introduced to engineers.

## Themes

- **dependency-term-collision**: §dependencies: "Dependencies are specified in a simple object that maps a package name to a version range"; the version range follows semver; tarball and git URLs are also allowed and are "downloaded and installed locally to your package at install time". §devDependencies: tooling the module's consumers do not need, installed on `npm install` from the package root.

## Key points

- "dependencies" is a map from package name to version range; semver governs the range.
- Dependencies can be a registry version, a tarball URL, a git URL or a local path; the install resolves and fetches them.
- "devDependencies", "peerDependencies" and "optionalDependencies" are variations on the same idea: code this package needs, at build or run time.
- Nothing on the page concerns people, approvals, funding, calendars or knowledge; the word means code the build must fetch.
