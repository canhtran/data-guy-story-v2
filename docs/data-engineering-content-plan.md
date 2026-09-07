# Data Engineering content plan

## Purpose

This document defines the future content structure for `content/wiki/data-engineering/`.

The section should help a reader move from understanding what a Data Engineer does to reasoning about a production Data Pipeline. It is a concept reference, not a tool-based course. Kafka, Spark, Flink, Airflow and similar tools may appear as examples, but their implementation details belong under `content/wiki/technologies/`.

The section remains flat. Each concept has its own article directly under `content/wiki/data-engineering/`. Use frontmatter `weight`, `prerequisites`, `related` and `topics` to express order and relationships instead of creating nested folders.

## Target audience

The primary reader has:

- Read the articles under `content/wiki/bat-dau/`.
- Understood the role of a Data Engineer and the basic path data takes through a system.
- Learned, or is learning, basic SQL and Database concepts.
- Little or no experience operating Data Pipelines in production.

Readers who do not yet understand the role should be directed to `/wiki/bat-dau/`. Readers looking for implementation details for a specific technology should be directed to `/wiki/technologies/`.

## Content principles

Every article should:

1. Explain one primary concept.
2. Begin with a concrete problem instead of a formal definition.
3. Reuse the food-order dataset where it remains natural.
4. Keep the English technical term and explain its Vietnamese meaning at first use only.
5. Include a vertical Mermaid diagram that remains readable on a phone when a diagram helps.
6. Show actual data using a table, SQL, JSON or pipeline state.
7. Start with the simplest working approach.
8. Show at least one way that approach can fail.
9. Explain when the concept becomes necessary and when it does not.
10. Link prerequisite and related concepts through frontmatter and relevant inline links.

Avoid introducing a technology before explaining the problem it solves. Avoid diagrams that spread horizontally, unexplained abbreviations, abstract architecture without sample data, and lists of tools without a decision context.

## Recommended article order

The sidebar uses one flat list ordered by frontmatter `weight`. The Data Engineering landing page may present the same list through three audience entry points, but these are not subdirectories.

### Level 1: Build the first working data system

This level targets beginners and career switchers. Completing it should give the reader a working mental model from Source System to trustworthy output.

| Weight | Article | File | Reader outcome |
| ---: | --- | --- | --- |
| 1 | Data Pipeline là gì? | `data-pipeline.md` | Identify the source, processing steps, destination, consumer and failure points of a pipeline. |
| 2 | Data Ingestion là gì? | `data-ingestion.md` | Understand how data leaves a Source System and enters the data platform. |
| 3 | Data Warehouse là gì? | `data-warehouse.md` | Understand why analytical data needs storage separate from an application Database. |
| 4 | ETL và ELT khác nhau thế nào? | `etl-elt.md` | Understand where transformation happens and why the destination affects the choice. |
| 5 | Batch Processing là gì? | `batch-processing.md` | Understand scheduled processing and bounded input. |
| 6 | Data Orchestration là gì? | `orchestration.md` | Understand schedules, dependencies, execution order and failure handling. |
| 7 | Data Quality là gì? | `data-quality.md` | Decide whether pipeline output is complete, valid and trustworthy enough to use. |

The conceptual flow is:

```text
Get data
  → store it
  → transform it
  → run repeatedly
  → coordinate the steps
  → check the result
```

Level 1 is the minimum useful release for the Data Engineering section.

### Level 2: Operate pipelines in production

This level targets Junior Data Engineers who can build a pipeline and are beginning to encounter failures, historical corrections and changing requirements.

| Weight | Article | File | Reader outcome |
| ---: | --- | --- | --- |
| 8 | Idempotency là gì? | `idempotency.md` | Understand why rerunning work must not create unintended duplicate results. |
| 9 | Retry hoạt động như thế nào? | `retry.md` | Distinguish retryable failures and understand why unlimited retry is unsafe. |
| 10 | Backfill là gì? | `backfill.md` | Process missing or historical data safely. |
| 11 | Data Observability là gì? | `data-observability.md` | Detect late, missing, broken or unusual data and pipeline behavior. |
| 12 | Metadata là gì? | `metadata.md` | Understand information that describes tables, fields, owners and update times. |
| 13 | Data Lineage là gì? | `data-lineage.md` | Trace data from its source through transformations to downstream consumers. |
| 14 | Data Catalog là gì? | `data-catalog.md` | Discover available data and understand how it should be used. |
| 15 | Data Contract là gì? | `data-contract.md` | Understand agreements between data producers and consumers. |
| 16 | Schema Evolution là gì? | `schema-evolution.md` | Change fields and structures without silently breaking consumers. |

The dependency order matters:

- Retry follows Idempotency because retrying unsafe work can duplicate data.
- Backfill follows both because a backfill is controlled reprocessing.
- Data Observability follows pipeline operation because the reader first needs something to observe.
- Metadata leads to Data Lineage, which leads to Data Catalog.
- Data Contract precedes Schema Evolution because safe change requires an agreement.

### Level 3: Choose architectures for larger systems

This level targets readers who understand regular Batch Pipelines and need different latency, storage or scale characteristics.

| Weight | Article | File | Reader outcome |
| ---: | --- | --- | --- |
| 17 | Batch và Streaming khác nhau thế nào? | `batch-vs-streaming.md` | Compare bounded and unbounded processing before choosing a model. |
| 18 | Stream Processing là gì? | `stream-processing.md` | Understand continuous processing, events, latency, state and ordering. |
| 19 | Change Data Capture — CDC là gì? | `change-data-capture.md` | Capture Database changes without repeatedly reading the entire table. |
| 20 | Data Lake là gì? | `data-lake.md` | Understand why organizations retain large volumes of raw and varied data. |
| 21 | Lakehouse là gì? | `lakehouse.md` | Understand the problems addressed when analytical workloads run on a Data Lake. |
| 22 | File Format: CSV, JSON và Parquet | `file-formats.md` | Understand how physical format affects size, speed and compatibility. |
| 23 | Table Format: Iceberg, Delta Lake và Hudi | `table-formats.md` | Understand how tables on object storage gain transactions, schema evolution and snapshots. |

Keep the Batch-versus-Streaming comparison separate from the detailed Batch and Stream Processing articles. The comparison helps the reader choose a direction; the detailed articles explain how each model works.

## Landing-page entry points

The sidebar remains flat. The landing page should help readers choose where to enter based on experience:

```text
New to Data Engineering?
Start with Data Pipeline → Data Quality.

Already building pipelines?
Start with Idempotency → Schema Evolution.

Working with larger or real-time systems?
Start with Batch vs Streaming → Table Formats.
```

Do not make these entry points into folders. They are reading guidance only.

## Existing placeholders

Reuse these existing files, updating titles, descriptions, weights and frontmatter as each article is written:

| Existing file | Planned article |
| --- | --- |
| `etl-elt.md` | ETL và ELT khác nhau thế nào? |
| `batch-processing.md` | Batch Processing là gì? |
| `stream-processing.md` | Stream Processing là gì? |
| `change-data-capture.md` | Change Data Capture — CDC là gì? |
| `data-warehouse.md` | Data Warehouse là gì? |
| `data-lake.md` | Data Lake là gì? |
| `lakehouse.md` | Lakehouse là gì? |
| `data-quality.md` | Data Quality là gì? |
| `orchestration.md` | Data Orchestration là gì? |
| `metadata-lineage.md` | Replace with separate `metadata.md` and `data-lineage.md` articles. |

Create new files only when work begins on their articles. Do not add another large set of empty placeholders.

## Scope boundaries

Keep these topics under `content/wiki/nen-tang/`:

- Database fundamentals
- SQL
- Relational and dimensional Data Modeling
- Distributed Systems fundamentals

Keep these topics under `content/wiki/technologies/`:

- Kafka implementation details
- Flink implementation details
- Spark implementation details
- Tool-specific configuration, architecture and operations

Keep Data Mesh as optional context in `content/wiki/bat-dau/data-engineer-la-gi.md` until a dedicated advanced article is justified.

Potential future Data Engineering articles, after the planned 23, include:

- Data Governance
- Data Security and Access Control
- Data Privacy
- Data Retention
- Cost Optimization
- Data SLA and SLO
- Disaster Recovery
- Data Platform

Add them only when they can answer a distinct reader question. Do not combine unrelated concepts simply to reduce the article count.

## Writing template

Use this outline when it fits the concept:

```markdown
---
title: "English term là gì?"
description: "One specific sentence describing the reader outcome."
draft: true
contentType: "concept"
weight: 1
level: "beginner"
topics: ["data-engineering"]
prerequisites: []
related: []
---

Opening problem using a concrete order example.

## English term là gì?

Define the English term and provide its Vietnamese meaning once.

## A concrete example

Show actual rows, SQL, JSON or pipeline states.

## How it works

Use a vertical Mermaid diagram where it improves comprehension.

## What can go wrong?

Show at least one realistic failure.

## When is it needed?

Compare a case that needs the concept with one that does not.

## Summary

Restate the decision or mental model the reader should retain.
```

Adapt headings to the subject instead of forcing identical headings into every page.

## Publishing phases

### Phase 1

Write and review articles 1–7. Publish the Data Engineering landing page when all seven are ready. At that point, update the Wiki landing page to link to the section.

### Phase 2

Write and review articles 8–16. Update the Data Engineer foundation learning path only after every linked article is published.

### Phase 3

Write and review articles 17–23. Link technology-specific follow-ups only when those pages are also published.

Draft pages must not be referenced by published pages through Hugo `relref`, because production excludes drafts and treats the unresolved reference as a build error.

## Definition of done for an article

An article is ready to change from `draft: true` to `draft: false` when:

- The title and description state one clear topic and reader outcome.
- Every specialist English term is explained in Vietnamese at first use.
- Examples are understandable without knowledge introduced later in the sequence.
- Diagrams are vertical and readable on a phone.
- Tables remain useful on narrow screens.
- The article contains no TODO text.
- Prerequisites and related links point only to existing content.
- The Markdown output is readable without the HTML theme.
- The development Hugo build passes.
- The production Hugo build passes with drafts excluded.
- The article appears correctly in `/llms.txt` after publication.

## Research references

The ordering is informed by these open-source curricula while remaining concept-first and independent of particular tools:

- [DataTalksClub Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp): ingestion, orchestration, warehousing, analytics engineering, data platforms, Batch Processing and Stream Processing.
- [The Data Engineering Cookbook](https://github.com/andkret/Cookbook/blob/master/sections/01-Introduction.md): Connect, Buffer, Process, Store and Visualize platform model, plus storage selection, monitoring and production concerns.
- [Data Engineering Handbook](https://github.com/DataExpert-io/data-engineer-handbook): broader beginner and intermediate Data Engineering learning resources.

Review these references for coverage and teaching ideas. Do not copy their wording, examples or course structure.
