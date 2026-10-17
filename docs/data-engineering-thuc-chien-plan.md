# Data Engineering thực chiến — Learning Path Plan

Updated: 27 September 2026.

Status: proposed component plan following the [general website plan](website-general-plan.md), [introductory path](nhap-mon-data-engineering-plan.md), and [Wiki coverage plan](wiki-structure-and-coverage-plan.md). Defines the curriculum and materials to author; datasets, lessons, course packs, and executable labs are not yet delivered by this document. Duration and environment requirements need learner pilots.

## 1. Promise, audience, and scope

> Học cách thiết kế, xây dựng và vận hành hệ thống dữ liệu qua một dự án hoàn chỉnh, với AI đồng hành từ buổi đầu tiên.

Completion outcome: translate a reporting need into source contracts and an architecture, integrate changing data from multiple sources, model historical facts, publish verified results, and recover the system when something fails. Learners defend their choices using local evidence and explain where their design stops being appropriate.

Entry: complete Nhập môn Data Engineering or demonstrate equivalent skills. The entry exercise asks learners to join order/item records without inflating totals, implement a Python file loader, explain a transaction, and rerun a daily pipeline safely. Supply short remediation tasks with Wiki sources for gaps. Basic terminal use is assumed; Git commits, environment configuration, and reading logs receive a short onboarding lab.

**Proposed pace: eight weeks, 8–10 hours per week (64–80 hours total)**. Six guided milestones plus two final-project weeks. This is a scope estimate, not an accelerated job-readiness promise. A typical guided week allows 1–2 hours of mentoring and targeted reading, 4–5 hours of implementation, 2 hours of verification, and 1 hour of explanation and follow-up. Pilot modeling and recovery weeks especially; extend the pace if needed rather than removing correctness checks.

| Progression from Nhập môn | Required depth here |
| --- | --- |
| One day's complete file snapshot | Multiple interfaces, source cursors, changes, late records, replay |
| Simple reporting tables | Explicit facts/dimensions, one historical dimension, multiple fact grains |
| Manual date-based pipeline | Scheduled dependencies, retries, bounded backfills, overlap control |
| Check totals and safe reruns | Source reconciliation, contract changes, freshness, incident recovery |
| Local setup supplied | Versioned build, separate development/release configuration, tested deployment and rollback |
| Explain a query | Defend architecture, storage and processing choices with measured evidence |

Core is batch data engineering on one machine. Compare warehouse, lake and lakehouse designs; implement one bounded architecture. Distributed execution, Kafka/Flink streaming, log-based CDC, Kubernetes, shared platforms, are later local learning branches. Cloud infrastructure is outside the course scope. A separate Spark lab may follow completion; it is not another required engine hidden inside the eight weeks.

## 2. AI-assisted first: the learner experience

The learner starts with AI in the first session. **The Wiki supplies canonical explanations; the mentor guides tasks; executable project evidence establishes completion.** Reading is introduced when a question needs it. Direct website study remains a complete alternative.

1. Open the path overview, inspect the finished report example, and obtain the versioned starter/course pack.
2. Load the pack into the learning companion established in the introductory path; paste the mentor prompt and share the entry-check results.
3. Start with a stakeholder question, inspect a few records, and predict an answer before writing code.
4. Ask AI to help explore designs, scaffold code, explain a concept, or debug a specific failure.
5. Run locally; compare output with independent fixtures, inspect the diff, explain a decision, and apply a small change.
6. Save the checkpoint, evidence, unresolved questions, and next action in a learner-owned journal.

Two complementary roles use the same course version:

| Role | Purpose | Evidence boundary |
| --- | --- | --- |
| Learning mentor | Wiki-grounded explanation, progressive hints, design questions, reflection | Reviews supplied results; does not claim access to local files or execution |
| Optional coding assistant | Read project context, propose changes, generate tests, help interpret logs | Actual file/terminal access depends on the learner's tool; proposed and executed work must be distinguished |

No particular paid coding assistant is required. The core accepts generated code, but the learner must understand contracts, inspect changes, run checks, and adapt the result. Record one consequential AI suggestion accepted or corrected per milestone. Tests generated from the same code are insufficient on their own: use author-verified answers and independent invariants.

Vietnamese starter prompt:

> Bạn là mentor của tôi trong lộ trình Data Engineering thực chiến. Dùng Wiki và brief trong course pack đúng phiên bản làm nguồn chính, dẫn mục liên quan khi giải thích. Hỏi từng câu để xác định checkpoint, hệ điều hành, cấu hình máy và công cụ đã cài. Hướng dẫn tôi cài đặt và cấu hình từng công cụ trên máy theo hướng dẫn đã kiểm thử trong course pack: mỗi lần một bước, nêu lệnh kiểm tra và chờ tôi gửi kết quả trước khi tiếp tục. Nếu cài đặt lỗi, hỏi lệnh và thông báo lỗi đầy đủ, đưa một phép kiểm tra để tìm nguyên nhân, rồi giúp tôi sửa và xác nhận dịch vụ chạy được. Bắt đầu bằng câu hỏi nghiệp vụ và vài bản ghi nhỏ, rồi cùng tôi thiết kế, triển khai và kiểm chứng từng bước. Cho phép tôi dùng AI để viết code, nhưng yêu cầu tôi giải thích grain, công thức, trạng thái và cách phục hồi. Khi debug, hỏi lệnh đã chạy, lỗi, input nhỏ và kết quả mong đợi; phân biệt giả thuyết với bằng chứng. Không tự đổi metric contract hoặc tuyên bố đã chạy code khi chưa có kết quả. Nếu thiếu tài liệu, nói rõ. Sau mỗi checkpoint, đưa một biến thể để tôi áp dụng và giúp tôi lưu tiến độ.

Example opening: “Ba cửa hàng gửi số bán hàng, cổng thanh toán gửi tiền thu và hoàn tiền. Vì sao hai tổng này có thể khác nhau? Hãy xem một đơn trước khi chọn kiến trúc.”

The pack contains actual selected lesson text, contracts, small examples, progressive hints, and assessment rules, not merely a list of links. Generate it from a manifest with source revisions and stable section IDs; keep full solutions separate. Export onboarding and import verification follow the introductory plan, with service behavior rechecked during implementation. Proposed route: `/learning-paths/data-engineering-thuc-chien/ai-source/`; not a published page. Split into versioned milestone packs if retrieval becomes unreliable.

Journal fields: course version, milestone, brief version, command and fixture IDs, result/artifact location, design choice, AI suggestion verified, unresolved issue, next task. Resume from this record when switching conversations. Do not share real credentials or customer data; all course data is synthetic.

## 3. Guiding project: Một nguồn số liệu đáng tin cho chuỗi cà phê

A fictional three-store café chain needs a daily operations report. Store sales, payment records, and store assignments arrive separately and can change. The operations manager asks: “Hôm qua bán bao nhiêu, tiền thu có khớp không, và số nào vẫn đang chờ dữ liệu?”

The project is independently runnable; completing or retaining the introductory café code is unnecessary. Supply 60 days of synthetic data, a hand-checkable fixture, deterministic change scenarios, and a preview report.

```text
POS database changes + mock payment/refund API + store-history CSV
                              ↓ Python extraction
           Immutable raw batches + manifests + source cursors
                              ↓ validation and normalization
             PostgreSQL staging → facts and dimensions
                              ↓ dbt transformations and checks
            Candidate marts → reconciliation → published release
                              ↓
                  CSV + supplied HTML operations report

Airflow coordinates the batch; a run ledger records inputs, state and checks.
```

### AI-guided local installation and troubleshooting

Local means the learner installs and operates the data tools on their own computer, following the AI mentor’s instructions. It does not require a locally hosted AI model. The mentor can run in the established learning companion; the learner executes commands and shares relevant output.

1. Ask for operating system, CPU architecture, available memory/disk, installed tools and versions before choosing a tested setup recipe.
2. Explain the purpose of the next dependency or service, provide one bounded installation/configuration step, and wait for the learner’s result.
3. Verify each step: version output, service health, database connection and a tiny read/write operation. Introduce services when the milestone needs them.
4. If a step fails, collect the exact command, error and relevant configuration with secrets removed. Form a hypothesis, request one diagnostic check, then revise from the result.
5. Practice one supplied recoverable configuration fault, such as an incorrect connection port. The learner diagnoses it with AI and records the fix.
6. Save a setup journal with versions, commands, configuration choices, successful checks and restart instructions. Demonstrate stopping and restarting services without losing project data.

The course provides verified OS-specific recipes, pinned compatibility information, expected outputs and troubleshooting notes. AI adapts explanations and diagnostics to the learner’s evidence. Setup is a learning checkpoint inside the weekly time budget, not an assumed preinstalled environment or an unbounded installation exercise. Pilot installation effort and adjust the schedule if it exceeds the estimate.

### Proposed teaching stack and limits

- Python for extraction, validation, control state, and service interaction.
- PostgreSQL for source simulation and analytical tables, with separate databases/roles for source and warehouse.
- Local immutable files for replayable raw JSON/CSV batches. A Parquet comparison exercise teaches format and column selection without adding an object-storage service to the core.
- dbt Core with a compatible PostgreSQL adapter for SQL models, dependencies, and data tests.
- Airflow for scheduling, task dependencies, retries, and backfill exercises; supply its infrastructure configuration.
- Docker Compose and Git for a reproducible environment, versioned changes, and release drills. A provided CSV/HTML renderer keeps frontend development outside the course.

These are proposed teaching choices, not a tested compatibility matrix. Pin and verify the complete environment when writing the lab. dbt's [SQL model documentation](https://docs.getdbt.com/docs/build/sql-models) and [incremental-model documentation](https://docs.getdbt.com/docs/build/incremental-models) are implementation references; validate supported adapter behavior before prescribing an incremental strategy. Airflow's [core concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/) inform the orchestration lab. References checked during planning on 27 September 2026; use release-specific instructions in the executable pack.

Provide a minimal Compose profile before introducing Airflow in milestone 5. Measure memory, disk, setup time and run duration on pilot machines; publish tested minimums before release. A constrained machine may run stages sequentially; successful orchestration evidence is still required. All course services and deployment exercises run on the learner’s computer; no cloud account or remote server is required. The learner installs and configures the environment with AI guidance using tested course recipes.

### Source and metric contract

| Source | Grain and identity | Change behavior |
| --- | --- | --- |
| POS orders | One order, `order_id` | Status and timestamps can change; explicit cancellation/tombstone records |
| POS items | One line, `(order_id, line_id)` | Quantity or sale price corrections with source version |
| Payment API | One transaction, `transaction_id`, linked to order | Captures and refunds are separate records with status; paginated change feed |
| Store history CSV | One store/effective-from pair | Complete authoritative history with nonoverlapping effective intervals |

Every changing entity carries a monotonic source version and source update time. Extract ordered change records using a stable composite cursor, bounded by a captured high-water mark; the simulator supplies deterministic pagination. Retain tombstones and previous batch manifests. This is polling a supplied change feed, not implementing database-log CDC. Introduce the distinction explicitly.

Core contract:

- Business timezone `Asia/Ho_Chi_Minh`; source timestamps include offsets. Money uses integer VND. No tax, tips, FX, item discounts, inventory, or profit in core fixtures.
- Completed-order sales = sum of quantity × price at sale across nondeleted lines for completed, nondeleted orders. Count orders at order grain, not payment or item grain.
- Successful captures and successful refunds are separate measures; failed/pending attempts do not contribute. Net collected = captures − refunds. Several captures per order are permitted; never deduplicate on order ID.
- Order-cohort reconciliation groups all known successful transactions by the linked order's business date. Sales minus captures flags unpaid/overpaid differences; sales minus refunds is a separately labeled post-refund sales measure. Do not require sales and net collected to always match.
- A second cash-activity view groups captures/refunds by their own transaction business dates. Never compare its daily total to same-day order sales as an equality check.
- Store-region attribution uses the store history effective at order time. Use half-open intervals `[valid_from, valid_to)`; reject overlaps and missing required coverage. Corrected history rebuilds affected dates. One Type 2 dimension is required; other dimensions may use current attributes.
- Reporting cutoff: previous day, with data known at the run's explicit `as_of` time. Daily target is 08:00 local time in the simulation. Report the latest successful extraction time and coverage for each source, not merely the report build time.
- Automatic replay revisits affected dates for changes within seven days; older changes are detected and queued for an explicit bounded backfill. Never silently drop them. Each replay reads the relevant preserved batches; acquisition state and published-report state are separate.
- Missing expected batches mean incomplete data. Explicit zero-record manifests mean valid empty data. Late but valid data produces a labeled provisional result; malformed values, conflicting versions, missing references, or failed reconciliation invariants block trusted publication.

Small reference case: completed orders A = 100,000 VND and B = 60,000 VND; A has successful captures of 60,000 + 40,000 and a next-day refund of 20,000; B has a pending capture only. At a cutoff after that refund, order-cohort sales = 160,000, captures = 100,000, refunds = 20,000, net collected = 80,000, and unpaid difference = 60,000. The cash-activity view puts the refund on its actual transaction day. Author independently verifies both views before shipping fixtures.

### Required output

The report shows sales, completed orders, captures/refunds, outstanding differences, store comparison using historical regions, and exception rows for investigation. Every page identifies business dates, cutoff, report version, source coverage and check results. Distinguish provisional, trusted, and stale states. Include one observation and one limitation, with no unsupported claims about profitability or why customers behaved a certain way.

Model facts at order-line and payment-transaction grain. Aggregate each to the required grain before joining. Dimensions include store history and product; the marts serve business-date/store totals and order reconciliation.

Raw files are immutable and checksummed. Commit extraction cursors only after their batches are durably recorded; downstream failure must remain replayable from those batches. Stage candidate outputs, check them, then atomically update the active publication pointer in PostgreSQL. Build the HTML in a temporary location and atomically replace it only after validation; retain its release ID and retry export on failure. A failure must not label an old report as fresh. Serialize core publishing/backfill runs to prevent competing writers; broader concurrency is an extension.

## 4. Eight-week learning journey

Wiki groups in section 7 are mentor source material, introduced as tasks require them. Each guided checkpoint includes the listed follow-up and an AI review of actual evidence.

| Week | Goal and guided work | Completion evidence | “Quản lý hỏi thêm…” |
| --- | --- | --- | --- |
| **1. Từ yêu cầu đến lát cắt đầu tiên** | Meet mentor, pass entry check, install and verify the minimal local stack with AI guidance, define metrics and grains; compare batch/storage options. Use supplied adapters to run tiny data through staging to a first report. | Setup journal with tool versions and health checks; brief, source-to-report diagram, one architecture decision record, hand-checked reference case. | “Hai báo cáo lệch nhau: khác công thức hay thiếu dữ liệu?” Trace one order across both views. |
| **2. Thu thập dữ liệu thay đổi** | Implement database change-feed and API ingestion, pagination, manifests, cursors, bounded retry and replay; ingest history CSV. | Resume after a page failure; repeat delivery preserves logical rows; every raw batch traceable. | “API lỗi ở trang 3, rồi gửi lại trang 2?” Predict cursor and duplicate behavior before running. |
| **3. Mô hình hóa và biến đổi** | Build fact/dimension models in dbt; historical store attribution, payment aggregation, window-based version selection and metrics. | Grain/relationship tests; two store-region periods; multi-capture/refund fixture matches answers. | “Cửa hàng đổi vùng: báo cáo tháng trước có đổi không?” Explain effective-time attribution and corrections. |
| **4. Tăng dần, chất lượng và xử lý dữ liệu** | Implement affected-date rebuilds, schema policy, candidate publication, source reconciliation; inspect query plans and compare full/incremental work. | Full rebuild and incremental results agree for same inputs/cutoff; late update and tombstone handled; bad data blocks release. Record rows scanned and elapsed time. | “Sửa một đơn từ ba tuần trước thì sao?” Queue and replay a bounded backfill. |
| **5. Điều phối và vận hành** | Integrate jobs into Airflow; logical date/cutoff, dependencies, retry boundaries, overlap prevention, freshness checks and local alert sink. | Scheduled run, failed dependency blocking publication, retry recovery, and multi-day backfill with unchanged adjacent dates. | “Backfill đang chạy thì lịch hằng ngày đến?” Demonstrate the chosen serialization policy. |
| **6. Triển khai, sự cố và bàn giao** | Package a tagged release, run checks through supplied CI scaffold, deploy to isolated release configuration, inject failure and rehearse rollback. | Clean-environment reproduction; run ledger/alert; recovery without losing raw history; runbook, lineage map and incident note. | “Job xanh nhưng báo cáo vẫn cũ?” Detect source freshness versus execution success. |
| **7. Chọn và xây dự án cuối khóa** | Choose a new domain with AI, confirm bounded brief, architecture and acceptance matrix; build an end-to-end baseline. | Reviewed brief, first correct output, schema and tests, documented decisions. | Mentor challenges an ambiguous metric or grain before implementation grows. |
| **8. Kiểm chứng và bảo vệ dự án** | Finish incremental path, schedule/deploy, inject failure, replay a correction, demonstrate and explain. | All common acceptance scenarios, final rubric, reproducible release and walkthrough. | Explain and implement a small unseen variation using available references and AI. |

Supply tested setup recipes and configuration templates, an API simulator, a renderer, and orchestration/check-runner skeletons. Learners install, configure, start and verify these services with AI guidance; CI-style checks run locally without a hosted CI dependency. Learners implement source-state logic, contracts, SQL models, checks, task wiring and recovery behavior. Progressive starter checkpoints allow recovery from setup problems without presenting completed core logic as an exercise.

Deployment means a reproducible isolated release environment on the same machine for the required lab; demonstrate configuration separation and a previous code release running against compatible state. State migrations need a documented restore/forward-fix strategy; resetting data is not a rollback demonstration. High availability and continuous hosted operation are outside this completion claim.

## 5. Failure and acceptance matrix

Ship deterministic fixtures and a runner with independently checked expected outputs. Milestones introduce cases gradually; final projects use the same scenario categories with domain-specific answers.

| Scenario | Required behavior/evidence |
| --- | --- |
| Repeat batch / duplicate API page | Same logical rows and metrics; recorded duplicate handling |
| Same key with older source version | Does not overwrite a newer version; conflicting equal versions rejected |
| Extractor stops after raw write, before cursor commit | Resume safely, preserving discoverable batches without losing changes |
| Source schema adds an optional field | Preserve raw field; existing supported metrics continue |
| Required field removed or changes type | Clear contract failure; quarantine details; no trusted release |
| Late refund / corrected record / tombstone | Correct affected facts and dates; full rebuild comparison agrees |
| Historical store boundary | Correct assignment at the exact boundary; overlap rejected |
| Missing source / explicitly empty source | Distinct status; missing source cannot masquerade as zero |
| Transformation or export crashes | Last successful artifact remains identifiable; retry publishes consistent release |
| Retry and backfill overlap | Serialize or reject overlap; demonstrate unchanged adjacent dates |
| Job succeeds on stale source data | Freshness signal fails independently of task success; local alert includes run and source |
| Clean setup and release rollback | Documented repeatable result; compatible state or tested restore process |

Reference outputs are bound to dataset version and `as_of`. Changing a cutoff changes the expected answer deliberately. Supply source totals, metric answers, and invariants; do not compare wall-clock-dependent runs to a fixed answer accidentally.

## 6. Final projects: choose a domain, own the decisions

Reserve **16–20 hours across weeks 7–8**: 2–3 hours to choose and define, 7–9 to implement, 5–6 to test and recover, and 2 to document and present. Reuse the environment and generic extraction/report helpers. Provide no finished domain transformations. All options use synthetic datasets, dictionaries, deterministic source simulators, tiny verified answers, larger practice data and failure fixtures.

Common scope: two source interfaces, three to five source entities, one historical dimension, two fact grains, two or three business questions, one scheduled batch, a bounded backfill, and one report. Cap at the guiding project's dataset scale. Optional ideas go into a backlog. Learners may propose their own domain only if it meets the same contract and fixture requirements without adding new infrastructure.

### A. Đơn hàng và hoàn trả của cửa hàng online

Question: “Đơn nào đã bán, đã thu tiền và còn đang hoàn trả?”

- Inputs: changing order/order-line exports, paginated payment/refund API, and product-category history. Grain: order line, payment transaction, product/effective-from.
- Required metrics: completed-order sales, successful captures minus refunds, and outstanding collection by order cohort. Report refunds by transaction day separately. Historical category attribution uses order time.
- Required challenge: partial refund arrives late; a product changes category; multiple transactions must not multiply line totals.
- Boundaries: one currency, no tax, shipping allocation, inventory or profit. Use the guiding project's clearly separated sales/cash semantics, but implement new source adapters and product history.

### B. Theo dõi giao hàng và cam kết dịch vụ

Question: “Đơn nào giao trễ, đơn nào chưa giao, và khu vực nào cần kiểm tra?”

- Inputs: shipment updates, paginated delivery-attempt API, and depot-region history. Grain: shipment, attempt, depot/effective-from. Each shipment has promised time, creation time and optional cancellation time.
- Required metrics: due shipments at cutoff, delivered-on-time count divided by eligible due shipments, and undelivered overdue count. Eligibility excludes shipments cancelled before the promised time; late cancellation remains visible. First successful attempt determines delivery time. Attribute region at shipment creation.
- Required challenge: repeated attempts, an out-of-order success record, and a late correction to promised time. Deduplicate by attempt ID/version, never by shipment ID alone.
- Boundaries: one timezone and one carrier; no routing optimization or real-time tracking. Separate not-yet-due from overdue; absent events are not proof of delivery. Supply exact-cutoff examples and a zero-denominator rule (unavailable).

### C. Vận hành workshop và hoàn tiền

Question: “Workshop nào có người đăng ký thật, tham dự thật, và tiền hoàn còn chờ?”

- Inputs: changing registrations, paginated payment/refund transactions, versioned check-in exports, and workshop-venue history. Grain: registration, transaction, check-in event, workshop/effective-from.
- Required metrics: active registrations at event start; distinct attended registrations divided by that eligible cohort; successful collected amount minus refunds. Qualifying attendance requires a valid check-in in the supplied event window and an eligible registration. Attribute venue as of event start.
- Required challenge: duplicate check-ins with distinct event IDs, cancellation effective before event start but arriving later, and a next-day refund. Count attended registrations once while preserving raw events.
- Boundaries: synthetic participant IDs, fixed-price single-session events, no capacity planning or multi-session passes. Separate cohort attendance and cash-activity dates. Define zero eligible registrations as an unavailable attendance rate.

### AI-assisted final-project journey

Choose → brainstorm answerable questions → confirm metric/source contract → compare two reasonable designs → build a thin end-to-end slice → verify and add recovery → present and adapt.

The mentor helps the learner choose a domain and draft `project-brief.md`; the learner confirms scope and owns decisions. The author-provided core metric definitions remain fixed for assessment. A different metric may be an explicitly labeled extension, not a silent replacement. AI may generate implementation and tests, but reference fixtures and reviewer scenarios remain independent.

Final-project prompt:

> Tôi đã hoàn thành dự án chuỗi cà phê. Hãy giúp tôi chọn dự án cửa hàng online, giao hàng hoặc workshop theo điều tôi muốn tìm hiểu. Cùng tôi xác định người dùng báo cáo, hai hoặc ba câu hỏi, grain, thời gian, công thức, failure cases và tiêu chí hoàn thành. Giữ phạm vi hai tuần và các metric bắt buộc. Để tôi xác nhận brief, rồi hỗ trợ từng bước theo bằng chứng thực thi. Cuối cùng yêu cầu tôi trình bày một quyết định, một gợi ý AI đã kiểm chứng hoặc sửa lại, một sự cố phục hồi và một thay đổi nhỏ chưa gặp trước đó.

Deliverables: confirmed brief; architecture and lineage diagrams; two short design decision records; source/model contracts; versioned runnable repository; checks and acceptance evidence; scheduled workflow; CSV/HTML report with freshness; deployment/recovery runbook; incident note; AI verification log; walkthrough with a changed input. One decision addresses storage/processing, the other incremental state or recovery.

### Assessment

Score each dimension 0 (missing/incorrect), 1 (partial), or 2 (complete with reproducible evidence).

| Dimension | Score 2 requires |
| --- | --- |
| Requirements and architecture | Answerable questions, explicit boundaries, defended storage/processing choice |
| Metric and modeling correctness | Reference answers agree; grains, historical joins and denominators correct |
| Ingestion and incremental state | Pagination, source versions, duplicates, corrections and cursor recovery demonstrated |
| Quality and publication | Contract failures block trusted release; reconciliation and freshness are visible |
| Orchestration and recovery | Retry, scheduling, overlap control and bounded backfill work without corruption |
| Reproducible release | Clean environment, pinned dependencies, documented deployment/rollback behavior |
| Engineering judgment | Measured processing comparison, decision tradeoffs and limitations explained |
| Ownership and handover | Useful runbook; learner explains, verifies and adapts AI-assisted work |

Proposed pass: at least **13/16**, with correctness, ingestion/state, quality/publication, orchestration/recovery and reproducible release each scoring 2. Evidence may be reviewed manually; an AI-generated score is advisory. Give targeted revision tasks for failed dimensions. This is course completion, not a certification of production readiness.

## 7. Wiki sources and authoring gaps

Existing paths below identify canonical homes, not release-ready endorsements. Review their depth and runnable examples against the checkpoints. Proposed titles are authoring backlog entries, not links to nonexistent articles. Reuse the introductory AI, Python, Git and SQL foundations rather than duplicating them.

| Group / first use | Existing canonical sources | Required additions or deeper treatment |
| --- | --- | --- |
| W1 — requirements and architecture / week 1 | [Pipeline](../content/wiki/data-engineering/data-pipeline.md), [ETL/ELT](../content/wiki/data-engineering/etl-elt.md), [Warehouse](../content/wiki/data-engineering/data-warehouse.md), [Lake](../content/wiki/data-engineering/data-lake.md), [OLTP/OLAP](../content/wiki/nen-tang/database/oltp-vs-olap.md) | From business question to metric contract; choosing batch cadence and storage; short architecture decision records |
| W2 — source integration / week 2 | [Ingestion](../content/wiki/data-engineering/data-ingestion.md), [Idempotency](../content/wiki/data-engineering/idempotency.md), [Retry](../content/wiki/data-engineering/retry.md), [CDC](../content/wiki/data-engineering/change-data-capture.md) | API pagination and rate limits; source versions, durable cursors, tombstones and polling-versus-log CDC |
| W3 — modeling / week 3 | [Facts/dimensions](../content/wiki/nen-tang/data-modeling/fact-and-dimension.md), [Star schema](../content/wiki/nen-tang/data-modeling/star-schema.md), [SCD](../content/wiki/nen-tang/data-modeling/slowly-changing-dimension.md), [Window functions](../content/wiki/nen-tang/sql/window-function.md) | Historical interval joins, independently aggregated facts, effective time versus arrival time |
| W4 — correctness and processing / week 4 | [Quality](../content/wiki/data-engineering/data-quality.md), [Contracts](../content/wiki/data-engineering/data-contract.md), [Schema evolution](../content/wiki/data-engineering/schema-evolution.md), [File formats](../content/wiki/data-engineering/file-formats.md), [Query optimization](../content/wiki/nen-tang/sql/query-optimization.md) | Full versus incremental equivalence; affected-date rebuilds; staged publication; measured format/query comparison |
| W5 — operation / week 5 | [Orchestration](../content/wiki/data-engineering/orchestration.md), [Backfill](../content/wiki/data-engineering/backfill.md), [Observability](../content/wiki/data-engineering/data-observability.md) | Logical run dates, freshness/coverage targets, concurrent writers and actionable alerts |
| W6 — delivery / week 6 | [Lineage](../content/wiki/data-engineering/data-lineage.md), [Metadata](../content/wiki/data-engineering/metadata.md), [Transactions](../content/wiki/nen-tang/database/transaction.md) | Testing layers, CI, environment/secrets configuration, compatible releases, incident notes and runbooks |
| T — technology / introduced progressively | Existing technology section; new canonical pages needed | Python API/database clients; PostgreSQL upsert and query plans; dbt models/tests/incremental strategies; Airflow dates/retries/backfills; Compose and CI recipes |
| A — AI practices / every week | Reuse proposed AI learning/debugging/verification articles in the [introductory source map](nhap-mon-data-engineering-plan.md#7-wiki-titles-for-this-lộ-trình) | Reviewing generated changes; separating reference answers from generated tests; evidence-based design review |

Map W1/A to week 1, W2/A to week 2, W3/A to week 3, W4/A to week 4, W5/A to week 5, and W6/A to week 6. Technology sections arrive with the corresponding lab; final weeks reuse all groups. Concepts belong under Data Engineering or Nền tảng; tool recipes belong under Công nghệ. Do not delay a partial release for optional Spark, lakehouse or streaming material.

## 8. Authoring and release plan

| Release unit | Materials to produce | Release gate |
| --- | --- | --- |
| Contract and reference system | Dataset generator, dictionaries, tiny answers, as-of/change scenarios, reference implementation | Independent review verifies metrics and every failure fixture |
| Milestones 1–2 pilot | Entry/remediation lab, minimal environment, source simulators, first report, mentor pack and journal | Learner starts with AI, completes a thin slice and resumes failed extraction |
| Milestones 3–4 | Wiki lessons, dbt skeleton, historical fixtures, candidate publication and comparison harness | Incremental/full rebuild equivalence; historical joins and blocked publication verified |
| Milestones 5–6 | Airflow profile, schedule/failure fixtures, CI scaffold, release drill, runbook examples | Clean setup, scheduled run, recovery, stale-data detection and rollback demonstrated |
| Final-project packs | All three briefs, synthetic sources, verified answers, challenge variants and common rubric | Pilot each option within 16–20 hours using scaffolding but no worked transformations |
| Full path | Reviewed source manifest, generated packs, download/version policy, overview and eight module pages | Tested resource requirements, working links, complete learner journey and corrected workload estimate |

Pilot both an introductory-path graduate and a reader entering through the skill check. Record setup time, implementation/debugging time, AI unsupported claims, premature answer reveals, missed contract rules, and evidence quality. Test source citations, pack-version recognition, journal-based resumption, and direct website fallback. Do not advertise eight completed weeks while only early milestones are available.

Suggested future material layout: a course starter containing `contracts/`, `fixtures/`, `ingestion/`, `models/`, `orchestration/`, `checks/`, `reports/`, and `runbooks/`; project options receive separate input packs and briefs. These are proposed artifacts, not files created by this plan.

## 9. Boundaries and next paths

A successful learner can deliver and explain a small, scheduled, changing-data system and investigate failures. Large-scale performance, multi-tenant access, always-on infrastructure and real business production deployments require additional experience.

Streaming Engineering can reuse the business questions while replacing batch arrivals with continuous events, event-time behavior and stateful recovery. Data Platform Engineering can reuse the completed pipelines as workloads for provisioning, access control, shared deployment and observability. Neither branch is a prerequisite for this path.

This plan creates no published navigation or lesson pages. Reconcile the future path URL with existing drafts during website implementation. Keep the introductory six-week completion boundary intact; this path supplies its own entry fixtures and environment.
