# Goal

Create the initial Hugo content structure for **dataguystory.com** using the planned Wiki + Learning Path model.

Do not write full article content yet.

The goal of this task is to scaffold the content folders and Markdown files so future agents can fill them incrementally.

Tech stack:

- Hugo
- Hextra
- Markdown-first content
- GitHub-hosted

---

# Principles

The site has two content layers:

1. Wiki / reference content
2. Learning Paths that reuse and link to wiki articles

Do not duplicate article content inside Learning Paths.

Each technology should have:

- a hub page
- an overview article
- concept articles
- a separate learning path page

Use `_index.md` for hub / section landing pages.

Use normal `.md` files for actual wiki articles.

---

# Target Content Structure

Create the following structure under:

```text
content/
```

```text
content/
├── _index.md
│
├── bat-dau/
│   ├── _index.md
│   ├── data-engineer-la-gi.md
│   ├── hoc-data-engineering-tu-dau.md
│   └── data-engineering-roadmap.md
│
├── learning-paths/
│   ├── _index.md
│   ├── data-engineer-foundation.md
│   ├── kafka.md
│   ├── flink.md
│   ├── spark.md
│   └── streaming-engineer.md
│
├── nen-tang/
│   ├── _index.md
│   │
│   ├── database/
│   │   ├── _index.md
│   │   ├── overview.md
│   │   ├── oltp-vs-olap.md
│   │   ├── index.md
│   │   ├── transaction.md
│   │   ├── isolation-level.md
│   │   └── acid.md
│   │
│   ├── sql/
│   │   ├── _index.md
│   │   ├── overview.md
│   │   ├── join.md
│   │   ├── window-function.md
│   │   ├── cte.md
│   │   └── query-optimization.md
│   │
│   ├── data-modeling/
│   │   ├── _index.md
│   │   ├── overview.md
│   │   ├── fact-and-dimension.md
│   │   ├── star-schema.md
│   │   ├── snowflake-schema.md
│   │   └── slowly-changing-dimension.md
│   │
│   └── distributed-systems/
│       ├── _index.md
│       ├── overview.md
│       ├── partitioning.md
│       ├── replication.md
│       ├── consistency.md
│       ├── cap-theorem.md
│       └── fault-tolerance.md
│
├── data-engineering/
│   ├── _index.md
│   ├── etl-elt.md
│   ├── batch-processing.md
│   ├── stream-processing.md
│   ├── change-data-capture.md
│   ├── data-warehouse.md
│   ├── data-lake.md
│   ├── lakehouse.md
│   ├── data-quality.md
│   ├── orchestration.md
│   └── metadata-lineage.md
│
├── technologies/
│   ├── _index.md
│   │
│   ├── kafka/
│   │   ├── _index.md
│   │   ├── overview.md
│   │   ├── topic-partition.md
│   │   ├── producer.md
│   │   ├── consumer-group.md
│   │   ├── offset.md
│   │   ├── replication.md
│   │   ├── rebalancing.md
│   │   ├── delivery-semantics.md
│   │   └── transactions.md
│   │
│   ├── flink/
│   │   ├── _index.md
│   │   ├── overview.md
│   │   ├── architecture.md
│   │   ├── job-operator-task-subtask.md
│   │   ├── parallelism.md
│   │   ├── state.md
│   │   ├── checkpoint.md
│   │   ├── savepoint.md
│   │   ├── event-time.md
│   │   ├── watermark.md
│   │   ├── backpressure.md
│   │   └── exactly-once.md
│   │
│   └── spark/
│       ├── _index.md
│       ├── overview.md
│       ├── architecture.md
│       ├── rdd.md
│       ├── dataframe.md
│       ├── partition.md
│       ├── shuffle.md
│       ├── catalyst.md
│       ├── join-strategies.md
│       └── structured-streaming.md
│
└── stories/
    ├── _index.md
    │
    ├── architecture/
    │   └── _index.md
    │
    ├── incidents/
    │   └── _index.md
    │
    ├── migrations/
    │   └── _index.md
    │
    └── scaling/
        └── _index.md
```

---

# File Responsibilities

## `_index.md`

Use `_index.md` only for section or hub pages.

Examples:

```text
technologies/kafka/_index.md
```

Purpose:

- introduce the section
- explain what the technology is at a high level
- list article groups
- link to the technology learning path
- act as navigation

Do not use it as the full "Kafka là gì?" article.

---

## `overview.md`

Each major topic or technology may have an `overview.md`.

Examples:

```text
technologies/kafka/overview.md
technologies/flink/overview.md
nen-tang/database/overview.md
```

This is the actual wiki article.

Example responsibility:

```text
Kafka là gì?
Kafka giải quyết vấn đề gì?
Architecture tổng quan
Use cases
When to use
When not to use
```

---

# Minimal Frontmatter

Every generated Markdown file should include valid Hugo frontmatter.

Use this minimal format:

```yaml
---
title: ""
description: ""
draft: true
---
```

For real wiki articles, also add:

```yaml
type: concept
level: beginner
topics: []
prerequisites: []
related: []
```

Example:

```yaml
---
title: "Kafka Consumer Group"
description: ""
draft: true

type: concept
level: beginner

topics:
  - kafka

prerequisites:
  - kafka-topic-partition

related:
  - kafka-offset
  - kafka-rebalancing
---
```

Do not attempt to fully populate all metadata yet.

Use sensible placeholders where relationships are obvious.

---

# Hub Page Frontmatter

For `_index.md` files use:

```yaml
---
title: ""
description: ""
draft: true
type: hub
---
```

Example:

```yaml
---
title: "Apache Kafka"
description: "Kiến thức về Apache Kafka dành cho Data Engineer."
draft: true
type: hub
---
```

---

# Learning Path Files

Learning Path pages are not article duplicates.

They should contain:

- short introduction
- ordered list of steps
- links to existing wiki pages
- optional prerequisite section
- optional next path section

Example structure for:

```text
learning-paths/kafka.md
```

```markdown
---
title: "Học Kafka từ đầu"
description: ""
draft: true
type: learning-path
---

# Học Kafka từ đầu

## Phù hợp với ai?

TODO

## Nên biết trước

TODO

## Lộ trình

1. Kafka là gì?
2. Topic & Partition
3. Producer
4. Consumer Group
5. Offset
6. Replication
7. Rebalancing
8. Delivery Semantics

## Tiếp theo

TODO
```

Use relative or Hugo-friendly internal links where possible.

---

# Kafka Hub Placeholder

Create:

```text
technologies/kafka/_index.md
```

with headings:

```markdown
# Apache Kafka

TODO introduction.

## Bắt đầu

- Kafka là gì?

## Core Concepts

- Topic & Partition
- Producer
- Consumer Group
- Offset

## How Kafka Works

- Replication
- Rebalancing
- Delivery Semantics
- Transactions

## Learning Path

- Học Kafka từ đầu

## Chuyện thực tế

TODO
```

---

# Flink Hub Placeholder

Create:

```text
technologies/flink/_index.md
```

with:

```markdown
# Apache Flink

TODO introduction.

## Bắt đầu

- Flink là gì?

## Core Concepts

- Architecture
- Job / Operator / Task / Subtask
- Parallelism
- State

## Time & Streaming

- Event Time
- Watermark

## Fault Tolerance

- Checkpoint
- Savepoint
- Exactly Once

## Production

- Backpressure

## Learning Path

- Học Flink từ đầu
```

---

# Spark Hub Placeholder

Create:

```text
technologies/spark/_index.md
```

with:

```markdown
# Apache Spark

TODO introduction.

## Bắt đầu

- Spark là gì?

## Core Concepts

- Architecture
- RDD
- DataFrame
- Partition

## Execution

- Shuffle
- Catalyst
- Join Strategies

## Streaming

- Structured Streaming

## Learning Path

- Học Spark từ đầu
```

---

# Stories Structure

Do not create fake case-study articles yet.

Only create category hubs:

```text
stories/
stories/architecture/
stories/incidents/
stories/migrations/
stories/scaling/
```

Each `_index.md` should explain the section briefly.

Example:

```markdown
---
title: "Production Incidents"
description: ""
draft: true
type: hub
---

# Production Incidents

Các câu chuyện về sự cố production,
nguyên nhân, cách xử lý và bài học dành cho Data Engineer.

Các bài trong section này phải dẫn nguồn rõ ràng.
```

---

# Homepage Placeholder

Create:

```text
content/_index.md
```

Structure:

```markdown
---
title: "Data Guy Story"
description: "Data Engineering Wiki dành cho người Việt."
draft: true
---

# Data Guy Story

Data Engineering Wiki dành cho người Việt.

## Tôi muốn học Data Engineering

- Data Engineer Foundation
- Streaming Engineer
- Kafka
- Flink
- Spark

## Tôi muốn tra cứu

### Nền tảng

- Database
- SQL
- Data Modeling
- Distributed Systems

### Data Engineering

- ETL / ELT
- Batch Processing
- Stream Processing
- CDC
- Data Warehouse
- Lakehouse

### Công nghệ

- Kafka
- Flink
- Spark

## Chuyện thực tế

TODO
```

Do not spend time styling the homepage yet.

---

# Naming Rules

Use:

- lowercase file names
- kebab-case
- English slugs for technical terminology where natural
- Vietnamese titles inside Markdown

Examples:

```text
consumer-group.md
change-data-capture.md
slowly-changing-dimension.md
```

Avoid Vietnamese diacritics in file names.

---

# Do Not Do Yet

Do not:

- write full articles
- redesign Hextra
- build custom Hugo layouts
- implement llms.txt
- implement custom Markdown output
- implement learning path UI components
- build SEO schema
- migrate every existing blog article
- create hundreds of empty technology folders

This phase is only about establishing a clean content skeleton.

---

# Existing Content

Before creating files:

1. inspect the current `content/` directory
2. identify existing articles
3. do not delete existing content
4. do not overwrite files with the same path
5. preserve existing URLs where possible

If an existing article clearly maps to the new structure, leave it untouched for now unless moving it is explicitly required.

Generate a migration report instead of moving content automatically.

---

# Migration Report

Create:

```text
docs/content-migration-plan.md
```

It should contain:

```text
Existing page
Current path
Suggested new section
Suggested future path
Migration risk
Notes
```

Do not perform redirects or URL migration in this task.

---

# Expected Result

After completion, the repository should have:

1. the initial Wiki taxonomy
2. Kafka / Flink / Spark technology hubs
3. placeholder concept pages
4. Learning Path pages
5. foundation sections
6. Data Engineering concept section
7. Stories section
8. no duplicated learning content
9. no existing content deleted
10. a migration plan for old articles

---

# Definition of Done

The task is complete when:

- Hugo can build successfully
- Hextra can render the new sections
- all newly created Markdown files have valid frontmatter
- no existing content has been deleted
- Kafka, Flink, and Spark each have a hub + overview + concept pages
- Learning Paths link conceptually to the Wiki pages
- `docs/content-migration-plan.md` exists
- no full article content has been generated