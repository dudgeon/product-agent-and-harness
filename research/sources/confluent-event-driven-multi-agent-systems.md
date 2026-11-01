---
title: "A Distributed State of Mind: Event-Driven Multi-Agent Systems"
source_url: https://www.confluent.io/blog/event-driven-multi-agent-systems/
author: Sean Falconer, Andrew Sellers (Confluent)
publisher: Confluent blog (first published on InfoWorld, 2025-01-28)
published: 2025-02-19
retrieved: 2026-10-31
type: article
evidence: vendor-claim
filed_by: research-agent-handoff-models
themes: [event-triggered-agents, process-artifacts-as-coordination, agent-frameworks, one-job-per-agent]
relevance: medium
---

## Relevance to the project
The most cited statement of event-driven multi-agent design: four coordination patterns (orchestrator-worker, hierarchical, blackboard, market-based) rebuilt on Kafka topics, consumer groups and a replayable log, so agents never call each other and only react to events. It is the cleanest form of "agents never talk; they read and write the same records" at the infrastructure layer, and it shows what that layer does not give: the post says nothing about humans in the loop, identity, audit or waits that last weeks. A Kafka vendor's argument, with no deployment evidence.

## Themes
- event-triggered-agents: agents "don't divine action"; each has input (consume an event or command), processing, output (emit an event); request/response is cast as the bottleneck (section "Event-driven agents").
- process-artifacts-as-coordination: the blackboard pattern makes "the shared blackboard ... a data streaming topic"; keys or payload fields record which agent originated each event (Blackboard section).
- agent-frameworks: orchestrator-worker becomes keyed command messages spread across partitions; workers form a consumer group; on worker failure "the log can be replayed from a given partition for a saved offset"; "the orchestrator no longer needs bespoke logic for managing workers" (Orchestrator-worker section).
- one-job-per-agent: hierarchical pattern is the same decomposition applied recursively, topics as "logical swimlanes"; market-based pattern uses bid, ask and trade topics and "eliminates the quadratic connections" between solver agents.

## Key points
- What wakes an agent: a new message on a topic or partition it consumes. What it receives: a standardised payload (e.g. JSON) acting as a command or a context update. Where state lives: the immutable log ("permanent and unchangeable") plus whatever stateful worker a consistent key routes to.
- Named challenges: context sharing, scale and fault tolerance, integration, fresh data, safety and validation; the last is listed but no mechanism is given.
- Not covered: human approval, who an agent acts as, audit as a distinct concern, and any wait measured in days or weeks. The log is described for coordination and recovery, not as a compliance record.

## Notable quotes
- "the log can be replayed from a given partition for a saved offset"
- "eliminates the quadratic connections" (market-based pattern)

## Could not verify
- Any production system using these patterns; the post is architectural argument. The companion Confluent ebook and Falconer's Current 2025 talk were not read.
- Read via WebFetch (model-summarised view); re-check quotes before publication.
