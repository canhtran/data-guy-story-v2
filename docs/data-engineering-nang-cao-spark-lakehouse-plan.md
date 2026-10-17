# Data Engineering nâng cao: Spark & Lakehouse — Learning Path Plan

Updated: 1 October 2026. Status: proposed curriculum. Follows [Nhập môn](nhap-mon-data-engineering-plan.md) and [Data Engineering thực chiến](data-engineering-thuc-chien-plan.md). Labs, fixtures and course packs must be authored and piloted before publication.

## Audience and outcome

For learners who can already build a scheduled, tested batch warehouse and explain incremental loads, dimensional modeling and recovery. An entry challenge asks them to rebuild one corrected business date, reconcile two sources and explain an execution plan; targeted Wiki remediation supports gaps. The learner finishes able to design, build and troubleshoot a distributed batch lakehouse on a single computer, including table changes, partitioning, query plans, skew, replay and measured tradeoffs. The course does not claim that one computer reproduces multi-machine scale or availability.

Proposed pace: **8 weeks at 8–10 hours (64–80 total)**, including two weeks for one final project. Pilot setup and tuning time before publishing this estimate. Start with the AI mentor in the first session. The Wiki is its canonical reference; the learner runs all tools locally and uses fixture results to validate AI suggestions. Direct website study remains available.

## Local environment and AI setup flow

Proposed stack: pinned Java-compatible Spark distribution, Spark standalone master plus two worker processes, Python/PySpark, a local S3-compatible object store, a compatible Iceberg catalog, and one local SQL query interface. Run them in containers with persistent volumes. Use Spark SQL as the primary query path; add a separate query engine only if pilot machines can run it comfortably. The author must pin and verify exact versions, connector jars, catalog configuration and CPU/RAM/disk limits together. [Spark standalone documentation](https://spark.apache.org/docs/latest/spark-standalone.html) permits multiple daemons on one machine, and [Iceberg's Spark configuration](https://iceberg.apache.org/docs/latest/spark-configuration/) documents catalog integration; these are implementation references, not a tested course bundle.

The mentor first asks the learner's operating system, CPU architecture, memory, disk and installed container/Java/Python versions. It guides one bounded installation or configuration step, explains its purpose, gives a check command and waits for output. Learners verify container health, Spark workers, object store read/write, catalog table creation and a small distributed job before loading the full fixture. For failures, the mentor requests the exact command, error and relevant redacted configuration, proposes one diagnostic check and revises its hypothesis from the result. The setup journal records versions, ports, health checks, data volume paths and restart instructions. Include one deliberate catalog-connection fault and recovery. Setup time counts toward week 1. No cloud account or locally hosted AI model is required.

## Guiding project: Phân tích chuỗi bán lẻ nhiều kênh

A fictional retailer combines point-of-sale transactions, web orders, returns, product history and customer activity events. The business wants daily channel sales, return-adjusted revenue and repeat-customer cohorts. The prior café warehouse is conceptual preparation; this project includes its own data and starter code.

```text
Versioned synthetic CSV/JSON/Parquet batches → local object storage → Spark bronze validation
→ Iceberg silver facts and history → Spark SQL gold marts → supplied CSV/HTML report
```

Provide a hand-checkable 20-row fixture, medium local benchmark fixtures at two documented sizes, late/corrected batches, schema changes and independent expected answers. No personal data. Source manifest identifies each file and checksum. Business time zone is `Asia/Ho_Chi_Minh`; money is integer VND. Order-line grain determines sales; returns link to original lines and have their own event date. The learner defines order-cohort and activity-date views separately. Product category history uses half-open validity intervals. Missing partitions are distinct from valid empty partitions.

Store immutable raw batches, then publish Iceberg tables for cleaned line items, returns and product history. Gold marts serve business date, channel and product category, plus a customer cohort. Required reruns use stable business keys and source versions, compare to full rebuild results for identical cutoff, and retain a recoverable table snapshot before replacement. Do not claim that a format alone guarantees correct deduplication or exactly-once outcomes. Define a bounded late-arrival window and route older corrections to explicit backfill. Tests check reference metrics, schema contracts, duplicate keys, historical joins and untouched dates.

Performance work has a decision record: collect input rows/bytes, partition and file counts, job duration and Spark plan before and after each change. Use a fixture large enough to expose a shuffle or skew on tested machines; do not present a speedup from a tiny sample as a general rule. Learners explain when a single-node warehouse would be simpler.

## Weekly journey

| Week | Guided work | Checkpoint evidence |
| --- | --- | --- |
| 1 — Setup and first slice | AI guides installation, service checks, local cluster inspection and a small bronze-to-gold run. Review worker, executor and task roles. | Setup journal, two visible workers, verified object-store/catalog operation, tiny answer fixture. |
| 2 — Distributed transforms | Build bronze/silver jobs, inspect partitions and stage boundaries, compare join strategies. | Correct line and return totals; explain one shuffle from the Spark plan. |
| 3 — Lakehouse tables | Create Iceberg facts/history and gold marts; inspect snapshots, schema evolution and atomic table updates. | Historical fixture matches reference; failed write leaves the previous published table readable. |
| 4 — Incremental correctness | Apply versions, late events and tombstones; compute affected partitions and bounded backfill. | Incremental and full rebuild outputs agree at the same cutoff; rerun is idempotent. |
| 5 — Performance and recovery | Diagnose skew and small files, change partitioning/broadcast policy, fail a worker/job and resume. | Before/after measurements, plan interpretation, recovered output and tradeoff note. |
| 6 — Operate and explain | Package a reproducible local release, run scheduled batch with the established local orchestration pattern, add freshness/lineage/runbook. | Freshness and failure signal, clean reinstall, snapshot recovery, documented storage/compute choice. |
| 7 — Final project design/build | Choose domain with AI; confirm source contract, table grains, acceptance matrix; build first end-to-end result. | Brief, architecture decision and tiny fixture pass. |
| 8 — Final verification | Add corrections, performance investigation, fault/replay and presentation. | Full acceptance evidence and unseen input variation. |

Each week follows question → prediction → targeted Wiki source → local attempt → evidence review → one variation → progress note. AI may propose code and tests; the learner explains, executes and independently verifies them. The mentor never treats a proposed command as a successful run.

## Final projects

Choose one of three bounded, synthetic domains. Each has three input feeds, one changing dimension, two fact grains, a corrected batch, historical backfill and an author-verified tiny answer fixture. Reuse generic setup and report scaffolding; learners implement domain transformations.

| Option | Required question and hard case |
| --- | --- |
| **Library borrowing** | Loans, returns and branch moves: which titles have high overdue rates? A return arrives late and a branch changes region. Denominator is loans due by cutoff; a renewed loan uses its latest valid due date. |
| **Urban bike trips** | Trips, station history and repair events: which stations have high trip demand and downtime? A corrected trip end time crosses a business-day boundary; station-region attribution uses trip start. |
| **Workshop commerce** | Tickets, attendance and refunds: which events fill seats and retain revenue? Multiple check-ins cannot increase unique attendees; a late refund changes money metrics but not attendance. |

AI helps select a domain, compare two designs, define table grains/metric rules and split the work. The learner confirms the brief before coding. Deliverables: reproducible repository, source contract, Bronze/Silver/Gold tables, report, tested replay, performance decision record, recovery runbook and short walkthrough. Optional independent domain proposals must meet the same fixture and workload constraints.

Score eight dimensions 0–2: metric correctness, table/grain design, incremental equivalence, history/schema handling, distributed execution understanding, measured performance reasoning, recovery/reproducibility and explanation/AI verification. Proposed pass: **13/16** with correctness, incremental equivalence and recovery each at 2. Final evidence includes a changed input not seen during guided work. AI assessment is advisory.

## Wiki and release work

Reuse [Spark overview](../content/wiki/technologies/spark/overview.md), [DataFrame](../content/wiki/technologies/spark/dataframe.md), [architecture](../content/wiki/technologies/spark/architecture.md), [partition](../content/wiki/technologies/spark/partition.md), [shuffle](../content/wiki/technologies/spark/shuffle.md), [join strategies](../content/wiki/technologies/spark/join-strategies.md), [file formats](../content/wiki/data-engineering/file-formats.md), [lakehouse](../content/wiki/data-engineering/lakehouse.md), [table formats](../content/wiki/data-engineering/table-formats.md), [idempotency](../content/wiki/data-engineering/idempotency.md) and [backfill](../content/wiki/data-engineering/backfill.md). These existing files require depth and runnable-example review. Add canonical lessons on Iceberg snapshots/catalogs, skew diagnosis, local cluster resource limits, change application and performance measurement; tool configuration belongs under Công nghệ. The pack embeds reviewed source text and scenario contracts, not just links.

Release in units: tested local stack and week-1 pilot; correctness/modeling weeks 2–4; performance/recovery weeks 5–6; all three final packs and a two-week learner pilot. Verify memory/disk demands on supported machines, exact connector versions, restart persistence, failure fixtures and answer files. Keep partial availability explicit.
