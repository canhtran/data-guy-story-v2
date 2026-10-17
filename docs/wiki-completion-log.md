# Wiki completion log

Updated: 1 October 2026 (Asia/Singapore).

## User request and scope

Fill all missing Wiki articles. If the current run approaches its token limit, continue at 06:40 in Asia/Singapore. Preserve existing user edits, authored introductions and historical Blog content. No commits or deployment requested.

Use `docs/wiki-structure-and-coverage-plan.md` as the full scope map, and `docs/editorial-standards-plan.md` for the writing/review standard. Existing article scaffolds are the first priority; after those, reconcile topics listed in the coverage plan and Wiki landing page that lack files. Do not mistake zero TODOs for complete coverage of the broader outline.

## Completed in this run

22 existing placeholders now have introductory content and are available in the production build:

- SQL: overview, JOIN, window functions, CTE, query optimization (5).
- Database: overview, OLTP/OLAP, index, transaction, isolation, ACID (6).
- Data modeling: overview, fact/dimension, star, snowflake, SCD (5).
- Distributed systems: overview, partitioning, replication, consistency, CAP, fault tolerance (6).

Foundation root and four subject hubs are available. Wiki landing links to the foundation hub, labels unfinished future topics, and preserves the personal introduction.

The original plan's section 9 is a historical baseline; these 22 rows are no longer placeholders. Existing 30 authored articles were not rewritten or retrospectively certified.

## Verification

- `python3 scripts/check-wiki-examples.py` passes on SQLite 3.53.4. Verifies query outputs, transactions, rejected foreign key, NULL count, duplicate prices, index plan and modeling examples against explicit expected results.
- Shared synthetic dataset: `static/examples/wiki/sql/cafe.sql` (cafe-v1). CLI minimum is SQLite 3.25. Examples were run with Python's SQLite, not a PostgreSQL installation.
- PostgreSQL 18 isolation explanation is a documented conceptual schedule, not a tested two-session runtime lab.
- Distributed examples are thought experiments; the modulo example is plain Python. They do not claim a real cluster was fault-tested.
- Production and development Hugo builds pass. 4-topic foundation links and dataset download checked under `/project/` base URL.
- Browser visual QA is still pending because the browser tool was unavailable earlier.

## Original scaffold backlog — completed

The 29 technology article files below now contain introductory content. Use primary documentation with a stated version, conversational Vietnamese, worked examples, constraints, prerequisites and troubleshooting. Choose tool versions deliberately; do not invent verification or claim a local setup was tested when it was not. Keep a content draft until required example checks pass; only publish completed content and parent hubs when their links resolve in production.

- [x] `content/wiki/technologies/flink/architecture.md`
- [x] `content/wiki/technologies/flink/backpressure.md`
- [x] `content/wiki/technologies/flink/checkpoint.md`
- [x] `content/wiki/technologies/flink/event-time.md`
- [x] `content/wiki/technologies/flink/exactly-once.md`
- [x] `content/wiki/technologies/flink/job-operator-task-subtask.md`
- [x] `content/wiki/technologies/flink/overview.md`
- [x] `content/wiki/technologies/flink/parallelism.md`
- [x] `content/wiki/technologies/flink/savepoint.md`
- [x] `content/wiki/technologies/flink/state.md`
- [x] `content/wiki/technologies/flink/watermark.md`
- [x] `content/wiki/technologies/kafka/consumer-group.md`
- [x] `content/wiki/technologies/kafka/delivery-semantics.md`
- [x] `content/wiki/technologies/kafka/offset.md`
- [x] `content/wiki/technologies/kafka/overview.md`
- [x] `content/wiki/technologies/kafka/producer.md`
- [x] `content/wiki/technologies/kafka/rebalancing.md`
- [x] `content/wiki/technologies/kafka/replication.md`
- [x] `content/wiki/technologies/kafka/topic-partition.md`
- [x] `content/wiki/technologies/kafka/transactions.md`
- [x] `content/wiki/technologies/spark/architecture.md`
- [x] `content/wiki/technologies/spark/catalyst.md`
- [x] `content/wiki/technologies/spark/dataframe.md`
- [x] `content/wiki/technologies/spark/join-strategies.md`
- [x] `content/wiki/technologies/spark/overview.md`
- [x] `content/wiki/technologies/spark/partition.md`
- [x] `content/wiki/technologies/spark/rdd.md`
- [x] `content/wiki/technologies/spark/shuffle.md`
- [x] `content/wiki/technologies/spark/structured-streaming.md`

## After existing scaffolds

Audit the full coverage plan sections 4.2–4.4 against actual source files. Add missing articles in practical order: data basics (reuse the two legacy introductions with deliberate URL handling), Python, computing/terminal/Git/AI debugging, SQL/database gaps; then DE architecture, security, testing, operations and streaming; then local tools including Docker, PostgreSQL, DuckDB, dbt, Airflow, Iceberg and storage. Update this file with each batch and keep unfinished coverage explicit on hubs. Do not create empty pages to claim coverage. Learning-path course modules remain a separate scope.

## Continuation handoff

On the scheduled run, reread this log and inspect actual current files before editing. Continue autonomously, preserve unrelated modifications, run relevant example checks and production/development builds, and check internal links. If another run is needed, schedule the next continuation at 06:40 Asia/Singapore and record it here. Stop creating continuations when the mapped missing articles are filled and verified. Report meaningful completed work or a real blocker; do not emit unchanged status notifications.

One-time thread continuation created: `continue-filling-the-wiki`, ACTIVE, 06:40 local time (Asia/Singapore), 1 October 2026. It is attached to this thread and will resume from this log.


## Continuation on 1 October 2026, 06:40 Asia/Singapore

Reconciled actual files before editing: all 29 technology scaffold files already contained prose; Spark and Flink were available, Kafka was draft pending runtime verification. Preserved this work.

- Re-ran all nine exact Spark examples via `scripts/check-spark-examples.py` using PySpark 3.5.6 / Python 3.12 / JDK 17: all passed, including query-plan assertions and Structured Streaming checkpoint example. These are local checks, not a real cluster fault test.
- Added `scripts/check-kafka-examples.py`. Kafka 4.0.2 / JDK 17 one-node KRaft example passed produce/read, independent-group replay, and stop/restart persistence. It creates isolated temporary storage and stops its own broker. Published the nine Kafka articles and hub; no claims of multi-broker or transactional fault testing.
- Kafka overview now uses an explicit localhost-only practice configuration with dedicated ports 19092/19093 and separate data directory.
- Flink's 11 articles remain conceptual, explicitly distinguishing hand-checked examples from missing local connector/restart labs.
- Added Python overview, files-and-json, errors-and-logging and their hub. Exact code ran on Python 3.12; tested successful outputs, rejected duplicate key and invalid money. Linked the hub and added readings to the introductory NotebookLM source.
- All original TODO article scaffolds are filled. This does not complete the broader topic map. Next priority: data basics (reuse legacy pages carefully), remaining Python modules/environments/database/HTTP, computing foundations, then the practical DE and tool gaps in section 5 of the coverage plan.
- Production/development Hugo builds pass; local link targets checked across Wiki and NotebookLM pages under a `/project/` base URL.

The active user also requested the full NotebookLM page experience. Finished v0.2: six copyable prompts at the top, public source URL copy, accessible manual-selection fallback, first local Python/SQLite session with four verified scenarios, checkpoint map, project brief guidance and copyable journal. The page explicitly says the full PostgreSQL/pipeline course labs remain unfinished. Live HTML verified; clipboard branches checked in JavaScript; browser visual inspection unavailable due CUA initialization failure. Do not treat this page as proof the six-week course is complete.

Continuation rescheduled through the app: `continue-filling-the-wiki`, ACTIVE, one occurrence on Friday 2 October 2026 at 06:40 Asia/Singapore.

## Công nghệ continuation — DuckDB, 1 October 2026

Preserved the completed Spark/Kafka/Flink articles and the existing NotebookLM/Python work. Added four introductory DuckDB articles and a populated hub:

- `content/wiki/technologies/duckdb/overview.md`: installation, embedded execution, first SQL query and scope.
- `content/wiki/technologies/duckdb/query-files.md`: explicit CSV schema, leading-zero identifiers, NULL, JSON and Parquet round-trip.
- `content/wiki/technologies/duckdb/python-pipeline.md`: parameterized values, repeat-run replacement, rollback on duplicate ID, file persistence.
- `content/wiki/technologies/duckdb/performance-and-errors.md`: EXPLAIN, threads/memory/temp configuration and bounded troubleshooting.

Verified exact published Python blocks with `scripts/check-duckdb-examples.py` on DuckDB 1.4.3 / Python 3.12 / macOS Intel. All four pass, plus independent rejected NULL/negative/malformed-money checks. Source references use DuckDB's 1.4 LTS documentation reviewed on 1 October. No claims of tested Linux/Windows, actual spill, production benchmark or multi-process writing.

Updated Wiki/technology navigation to include DuckDB, while PostgreSQL and other absent groups remain explicitly unfinished. Corrected Kafka overview's stale troubleshooting port to match its existing 19092/19093 setup. Production and development Hugo builds pass; Wiki, technology hub and all DuckDB link targets verified under `/project/`. The existing Hugo `.Site.Data` deprecation warning remains. Browser visual QA attempted but the in-app browser timed out; rendered HTML and link checks passed, visual review remains pending.

Updated the existing heartbeat prompt to prioritize the user's current Công nghệ scope: Docker, PostgreSQL, Airflow, HDFS, MinIO, dbt, Iceberg and Flink local connector/restart labs. Preserve the existing single continuation on Friday 2 October 2026, 06:40 Asia/Singapore. Do not repeat already verified article batches or assume broader Wiki coverage is finished. No commit or deployment performed.

## Công nghệ continuation — dbt, 2 October 2026

Added `technologies/dbt` hub and two articles: `overview.md` (isolated local setup, seed/ref/models, rerun, correction and troubleshooting) and `data-tests.md` (unique/not-null/singular tests, duplicate and negative-money failures, downstream skip, recovery and stale-output limits). Linked from the technology hub. Preserved NotebookLM v0.2 and unrelated work.

Installed an isolated runtime in `/private/tmp/dgs-dbt-runtime`: Python 3.12, dbt Core 1.10.18, dbt-duckdb 1.10.0, DuckDB 1.4.3 on macOS Intel. `scripts/check-dbt-examples.py` extracts the exact published project files into a temporary directory. Passed baseline totals (100000/50000), identical rerun, duplicate unique failure + downstream SKIP, negative-money test failure, correction to 55000 and recovery. This does not verify other adapters, platforms or production orchestration. No database server/cloud needed.

Production (including /project/ baseURL) and development Hugo builds passed; rendered dbt page internal links resolved. Existing upstream .Site.Data deprecation warning remains. No browser visual QA performed for this prose-only batch.

Remaining: dbt incremental, snapshots/source freshness and operations; Docker, PostgreSQL, Airflow, HDFS, MinIO, Iceberg; Flink real local connector/restart labs. Broader foundations map remains unfinished. Do not call the technology batch complete or rerun unrelated verified suites without reason.

Attempted to update the existing thread heartbeat for Saturday 3 October 2026, 06:40 Asia/Singapore, but the automation tool rejected the update: “MCP tool call requires approval, but approval policy is never”. No new continuation was scheduled or confirmed; existing configuration was not changed by this attempt. Scheduling requires user/app action. No commit or deployment.

## Công nghệ continuation — dbt incremental, 15 October 2026

Added `content/wiki/technologies/dbt/incremental.md` and linked it from the dbt hub. The local DuckDB exercise uses a unique order key and adapter-specific `delete+insert` strategy to demonstrate initial load, safe rerun, insertion, correction of the latest key, a missed correction to an older key, and recovery with `--full-refresh`. The article states that incremental behavior and strategy are adapter-dependent, and explains late-data/backfill risks rather than claiming this is a general CDC solution.

Recreated the disposable runtime at `/private/tmp/dgs-dbt-runtime-oct` (Python 3.12, dbt Core 1.10.18, dbt-duckdb 1.10.0, DuckDB 1.4.3). `scripts/check-dbt-incremental.py` extracts the published SQL and seed, then verifies all six states above; it passed on macOS Intel. Production Hugo build with `/project/` base URL and development build passed; rendered dbt internal links resolved. The pre-existing Hugo `.Site.Data` deprecation warning remains.

Remaining technology coverage is substantial: Docker/PostgreSQL local setup; Airflow; HDFS; MinIO; Iceberg; dbt snapshots, source freshness, documentation/macros and operations; and executable Flink connector/restart labs. The installed host has no Docker or PostgreSQL CLI, so no claims were made about those local runtimes. Broader foundations coverage also remains. No commit or deployment.

A continuation is still needed. Earlier scheduling attempt was rejected by the automation tool because approval was required while policy was set to never; no new run has been confirmed. Scheduling therefore remains an app/tool limitation. This run did not alter the heartbeat configuration.

After the earlier failed attempt noted above, the existing automation was successfully updated on 15 October 2026. It is ACTIVE for one continuation on Friday 16 October 2026 at 06:40 Asia/Singapore, attached to this thread, with the remaining technology scope above. The earlier rejection did not prevent this later update. No commit or deployment.
