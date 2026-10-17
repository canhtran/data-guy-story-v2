# Nhập môn Data Engineering — Learning Path Plan

Updated: 27 September 2026.

Status: proposed component plan. Follows the [general website plan](website-general-plan.md) and [Wiki structure and coverage plan](wiki-structure-and-coverage-plan.md). Defines the learner journey, projects, reporting experience, exercises, required Wiki titles, and an AI mentoring experience grounded in those Wiki articles. Duration and workload need a beginner pilot before publication.

## 1. Audience and completion outcome

Reader-facing promise:

> Học Data Engineering qua một dự án thực tế, với AI đồng hành: giải thích khi chưa hiểu, gợi ý khi mắc kẹt, và giúp bạn kiểm chứng điều mình đã làm.

Completion outcome: tự xây được một pipeline nhỏ, từ dữ liệu đầu vào đến báo cáo, và giải thích được vì sao kết quả đúng.

For beginners who can use a computer and manage ordinary files. Prior SQL, Python, database, and terminal knowledge is not required. Provide setup guidance and short prerequisite lessons inside the schedule. Readers with prior experience may skip instruction after passing the relevant checkpoint.

By completion, readers can clarify a small reporting request, inspect source records, query and model data, write a Python ingestion job, generate a useful report, check correctness, rerun safely, and explain a demonstrated failure and recovery.

Proposed pace: **6 weeks, 6–8 hours per week (36–48 hours total)**: five guided milestones and one bounded independent final project. Weeks are a suggested pace, not deadlines; a complete beginner may need longer. Validate this estimate in a beginner pilot before advertising it as a completion promise.

**Start with AI from the first session.** The learner imports the course pack, meets the mentor, and starts a small project task. The mentor uses the Wiki to explain concepts when needed, asks questions, and points to a specific passage for deeper reading. Learners do not have to read a parallel list of full articles before each conversation. The Wiki is the knowledge foundation, AI is the primary guided interface, and local project evidence demonstrates learning. Direct website study remains available.

The shorter path reduces required scope rather than assuming AI eliminates practice time. Supply tested environment setup instructions, database connection scaffolding, the report renderer, and test harnesses. Learners implement and explain the core SQL, parsing/validation, loading behavior, and pipeline sequence. Formal star-schema design, scheduling, extended charting, and broader operational topics become optional extensions. The final project reuses the environment and renderer with a new dataset and metrics.

A typical week reserves about 1–1.5 hours for mentor dialogue and targeted reading, 3–4 hours for local work, 0.5–1 hour for a follow-up, and 1–1.5 hours for debugging and reflection. Week 6 uses that whole budget for the final assignment. The Python and ingestion milestones need particular pilot attention.

## 2. Guiding project: Bản tin quán cà phê mỗi sáng

A fictional café exports orders every day. The owner wants a morning brief about yesterday's business and confidence that the numbers are usable. Learners build the system behind that brief while responding to the owner's follow-up questions.

The report is due at 08:00 local time for the previous calendar day. This is a learning requirement for a local demonstration; the course does not promise an always-on hosted service.

```text
Daily orders and order items (CSV) + product catalog (JSON)
                            ↓
              Python: read, validate, load
                            ↓
              PostgreSQL: source tables
                            ↓
              SQL: facts and reporting marts
                            ↓
           Quality checks and reconciliation
                            ↓
              CSV + HTML morning brief
```

### Technology and scope

Local setup is part of learning: the learner follows the AI mentor to install, configure and verify tools on their own computer. The mentor first checks OS, hardware and installed versions, then uses the course’s tested recipes one step at a time. The learner runs commands and shares results; for failures, the mentor asks for the exact command/error, proposes a diagnostic check and waits for evidence before suggesting a fix. Record versions and successful checks in a setup journal, including a service restart and one recoverable connection fault. Include this work in week 1 and the workload pilot. This requirement applies to the data infrastructure; it does not require running the AI model locally. No cloud data services are part of the course.

- Python for file handling, validation, database access, logs, and pipeline entry point.
- PostgreSQL for relational learning, transformations, and reporting tables.
- SQL for metrics, joins, modeling, and checks.
- A supplied HTML/chart template for the report. Learners populate a documented reporting-data interface; frontend development is not a prerequisite.
- Git offered as an optional workflow extension; saving project files and a local progress journal is sufficient for the core.
- A supplied local database setup and an optional OS-appropriate scheduling recipe. Select and pin tested versions when authoring the executable lab. If Docker Compose is selected for setup, provide the necessary short tool guide and troubleshooting; container internals remain optional.

One command accepts a business date and runs ingestion, transformation, validation, and export in order. An optional scheduling extension invokes that same command; a successful manual date-based run completes the core. The local project uses small files and requires no paid services or external data accounts. The AI companion uses a free-access option such as the learner's own NotebookLM account, subject to current availability and limits; no paid subscription is required, and the same lessons and checkpoints remain usable directly on the website. Verify free access during the release pilot.

Defer APIs, cloud deployment, distributed processing, streaming, SCD, complex incremental loading, and dedicated orchestration frameworks to later paths. Introduce warehouse and orchestration concepts at the depth needed to explain this system.

## 3. Dataset and metric contract

Use synthetic data without personal information. Begin with a hand-checkable fixture of roughly 10 orders, then provide at least four weeks of daily files for trends. The author supplies versioned fixtures, a data dictionary, and independently verified expected results.

| Input | Grain and key | Essential fields |
| --- | --- | --- |
| `orders.csv` | One row per order; `order_id` | Order timestamp, status (`completed` or `cancelled`) |
| `order_items.csv` | One row per order line; `(order_id, line_id)` | Product ID, quantity, unit price at sale |
| `products.json` | One row per product; `product_id` | Product name and category |
| Daily manifest | One row per business date | Expected filenames and source row counts, including explicit empty exports |

Daily order and item files are complete snapshots for their business date. For the introductory project, orders are finalized before export, and the catalog is fixed across the exercise. Corrections are supplied as replacement snapshots. This makes replacement of one day a defined operation rather than an assumed incremental merge.

Contract rules:

- Business timezone: `Asia/Ho_Chi_Minh`. Include offsets in source timestamps; derive reporting dates and hours in that timezone.
- Currency: VND represented as integer đồng. Use unit price recorded on the order line, not a current catalog price.
- Sales: sum of quantity × unit price for completed orders. No refunds, tax, discounts, or profit calculation in the core dataset.
- Completed orders: count distinct completed order IDs. Items sold: sum quantities on completed orders. Average order value: sales divided by completed orders; show unavailable when there are no completed orders.
- Product rankings: separate units sold from sales value; define a deterministic tie order.
- Hourly activity: completed-order count by order creation hour, not line-item count.
- Comparison: previous business date versus exactly seven days earlier. Missing baseline means unavailable; zero baseline means percentage change unavailable, with absolute change shown. Do not silently convert either to zero percent.
- A day is validly empty only when the expected files and manifest confirm zero records. Missing files mean missing data.

Introduce deliberate fixtures for cancelled orders, multi-item orders, missing product references, malformed values, duplicate keys, repeated file delivery, missing input, empty input, and corrected daily snapshots. Each fixture has an intended outcome and expected checks.

Invalid rows are recorded with filename, row number, and reason. Learners may inspect provisional valid-row results, but any blocking validation failure prevents publication of a fresh trusted report. Preserve the last successful artifact and show its actual business date and generation time.

## 4. Reporting experience

The report answers “What happened, what deserves attention, and can I trust the data?” Numerical examples in teaching materials must come from verified fixtures.

| Section | Reader-facing title | Contents and behavior |
| --- | --- | --- |
| Daily overview | **Hôm qua quán mình thế nào?** | Sales, completed orders, average order value, and same-weekday comparison |
| Activity chart (optional) | **Khung giờ nào đông khách?** | Completed orders by hour; weekday × hour heatmap is an optional extension |
| Product rankings | **Món nào bán chạy, món nào mang về nhiều tiền?** | Separate rankings for units and sales |
| Trend (optional) | **Tuần này có gì thay đổi?** | Daily sales over several weeks; visibly mark missing days |
| Data status | **Số liệu này đã đủ tin cậy chưa?** | Business date, input coverage, generation time, rejected rows, and check status |
| Short interpretation | **Một điều đáng chú ý hôm nay** | A learner-written observation, investigation question, and limitation |

Use a supplied template with readable labels, explicit units, simple charts, and a table or text equivalent. It must work locally without a frontend build workflow. Early weeks show SQL tables; later weeks populate the final HTML report.

Do not infer causation, profitability, stock requirements, or staffing needs from sales alone. “Morning orders increased; investigate queue times” is appropriate. “Hire another barista” needs additional evidence.

## 5. Weekly learning journey

Wiki IDs refer to section 7. The material column identifies **the mentor's source material**, not a separate full-article reading assignment. Include the relevant introductory sections in the pack; the mentor introduces them as a task needs them. Completion depends on demonstrated skills, not reading every page or finishing a prescribed number of chat turns.

Each session follows: a concrete question → learner attempt → targeted explanation or hint → local execution → evidence review → one transfer question → progress note.

| Suggested week / milestone | Wiki material used by the mentor | Guided work and interaction | Completion evidence |
| --- | --- | --- | --- |
| **1. Gặp mentor và khám phá dữ liệu quán cà phê** | O1, O2, A1, F1, F2, D1, T2, S1, S2, S3 | Meet the mentor; with AI guidance, install and verify the local environment one step at a time, then inspect three orders, calculate sales by hand, and use SELECT/filtering to check the answer. Introduce only the setup concepts required to proceed. | Show a working local connection and setup journal; explain what a record represents; reproduce the filtered fixture and distinguish completed from cancelled orders. |
| **2. Trả lời câu hỏi của chủ quán bằng SQL** | S4, S5, F3, S6, A2, A3, M2 | Build daily metrics and product rankings, diagnose an inflated join, and compare with the same weekday last week. The mentor asks for a prediction before executing a query. | Correct totals, order/item counts, and absent/zero baseline behavior; explain a changed query. |
| **3. Đọc file và tìm dữ liệu lỗi bằng Python** | P1, P2, P3, P4; revisit A2, A3 | Use a supplied project skeleton; implement file reading, conversion, validation, and rejection details. Ask for hints or code examples, then run and explain them. | Process valid CSV/JSON and identify malformed rows using small fixtures; adapt one validation rule independently. |
| **4. Ghép thành pipeline và tạo bản tin đầu tiên** | E1, P5, P6, D2, D3, S7, E6; revisit M2 | Use connection and renderer scaffolding; implement loading and SQL summary tables, then connect read → load → transform → export. Introduce transactions through a supplied failure exercise. | A selected business date produces a reconciled CSV/HTML report; rollback prevents a partially committed load. |
| **5. Kiểm chứng, chạy lại và giải thích kết quả** | E4, E5, P7, P8; revisit D3 | Implement safe daily replacement, reject missing/invalid input, run supplied checks, fix a failed day, and write operating instructions. Mentor reviews local evidence and asks for one variation. | Repeated input preserves totals; corrected input updates the intended day; failed checks block fresh publication; clean setup reproduces the report. |
| **6. Chọn dự án của bạn, cùng AI thiết kế và hoàn thành** | Reuse prior material; no new required concepts | Choose personal finance, online shopping, or electricity usage. Brainstorm with the mentor, confirm a bounded brief, then reuse the environment and helpers while implementing new transformations and metrics. | A learner-owned brief, verified source-to-report result, edge-case demonstration, and concise handover meeting the common rubric. |

Optional extension material: O3 (foundations and AI), T1 (Git workflow), M1/M3/M4 (formal modeling and star schema), E2/E3 (ETL/ELT and warehouse context), S8 (CTEs), E7/T3 (orchestration and scheduling), E8 (broader backfill concepts). These are available for deeper questions and later study; they are excluded from the six-week completion gate. SQL window functions and distributed/streaming systems remain outside this path.

## 6. Follow-up questions and independent practice

Each guided milestone ends with **“Chủ quán hỏi thêm…”**. Reserve 30–60 minutes for one required follow-up; stretch tasks are optional. The mentor presents the question, waits for an attempt, and adapts its hints to the learner's evidence.

| Milestone | Owner's question | Independent task and completion check | Optional stretch |
| --- | --- | --- | --- |
| 1 | “Một đơn có hai món thì em đang nhìn một đơn hay hai dòng?” | Trace one order across the files and explain their grains and cancellation filter. | Identify a question the dataset cannot answer. |
| 2 | “Món bán chạy nhất có phải món mang về nhiều tiền nhất không?” | Produce separate unit and sales rankings and explain their difference. | Add hourly activity or diagnose another inflated join. |
| 3 | “File hôm nay có một dòng lỗi. Làm sao biết dòng nào?” | Emit filename, row number, and reason; change a validation rule and verify the result. | Handle a second malformed-value type. |
| 4 | “Nạp được nửa file thì chương trình dừng. Database còn những gì?” | Inject a failure, show rollback, and explain what was committed. | Explain why per-row commits change recovery behavior. |
| 5 | “Chị gửi lại file hôm qua rồi. Báo cáo có bị tính hai lần không?” | Verify repeat delivery, corrected input, and unchanged adjacent days. | Add scheduling or write a short incident note. |

Exercise format: owner's question → inputs → learner attempt → progressive hints → local checks → explanation and small variation. Keep worked solutions separate. AI assistance and generated code are allowed, but learners must run, verify, explain, and adapt what they use. The mentor's praise or confidence does not establish completion.

## 7. Wiki titles for this lộ trình

This is the Wiki source map for core mentoring and optional extensions, not a claim that every article is required or available. The core selections are identified in section 5; optional source articles need not block the first release. Existing titles and paths are preserved. **Content** means prose exists, with review pending; **Placeholder** means the existing draft must be written; **New** means a proposed article. Paths for new subjects identify editorial homes rather than links to nonexistent pages.

### Bắt đầu

| ID | Wiki title | State / canonical file |
| --- | --- | --- |
| O1 | Data Engineer là gì? | Content — [article](../content/wiki/bat-dau/data-engineer-la-gi.md) |
| O2 | Data đi qua một hệ thống như thế nào? | Content — [article](../content/wiki/bat-dau/du-lieu-di-qua-he-thong-nhu-the-nao.md) |
| O3 | Có AI rồi, còn cần học nền tảng không? | Content; optional — [article](../content/wiki/bat-dau/ai-va-kien-thuc-nen-tang.md) |

### Nền tảng — dữ liệu và môi trường làm việc

| ID | Wiki title | State / scope |
| --- | --- | --- |
| F1 | Dữ liệu là gì? Bản ghi, trường dữ liệu và schema | New, `nen-tang/data-basics/`; review and reuse legacy [Dữ liệu là gì](../content/docs/foundation/data-la-gi.md) and [Các loại dữ liệu](../content/docs/foundation/cac-loai-du-lieu.md) before choosing canonical destination. |
| F2 | File, đường dẫn và terminal: những thao tác đầu tiên | New, `nen-tang/computing/`; navigate files and run a command, with small examples. |
| F3 | Ngày giờ, múi giờ và cách biểu diễn thời gian | New, `nen-tang/data-basics/`; business date, timestamp, timezone, and missing periods. |

### Nền tảng — học và làm việc cùng AI

These reusable practices belong under proposed `nen-tang/computing/`. They complement O3 rather than repeating its discussion of why foundations matter. NotebookLM-specific setup belongs in the learning path's onboarding guide.

| ID | Wiki title | State / scope |
| --- | --- | --- |
| A1 | Học Data Engineering cùng AI: hỏi, thử và kiểm chứng | New; ask focused questions, attempt a task, request hints, verify claims, and record progress. First used in week 1. |
| A2 | Nhờ AI hỗ trợ debug: cần cung cấp những gì? | New; minimal example, exact error, command, environment, expected versus actual behavior, and removing credentials before sharing. First used in week 2. |
| A3 | Kiểm chứng SQL và code do AI gợi ý | New; hand-checkable fixtures, join cardinality, edge cases, local execution, and explaining and adapting generated code. First used in week 2; revisit for Python. |

### Nền tảng — cơ sở dữ liệu và SQL

| ID | Wiki title | State / scope |
| --- | --- | --- |
| D1 | Cơ sở dữ liệu là gì? | Placeholder — [article](../content/wiki/nen-tang/database/overview.md) |
| D2 | Khóa chính, khóa ngoại và ràng buộc dữ liệu | New, `nen-tang/database/`; identity, references, required fields, uniqueness. |
| D3 | Giao dịch trong cơ sở dữ liệu | Placeholder — [article](../content/wiki/nen-tang/database/transaction.md); commit, rollback, atomic loading. |
| S1 | SQL là gì? | Placeholder — [article](../content/wiki/nen-tang/sql/overview.md) |
| S2 | Đọc, lọc và sắp xếp dữ liệu với SELECT, WHERE, ORDER BY | New, `nen-tang/sql/`. |
| S3 | NULL và logic điều kiện trong SQL | New, `nen-tang/sql/`; include CASE, missing versus zero, safe division. |
| S4 | Tổng hợp dữ liệu với GROUP BY và các hàm tổng hợp | New, `nen-tang/sql/`; COUNT, COUNT DISTINCT, SUM, averages and denominator choices. |
| S5 | Kết hợp dữ liệu với JOIN | Placeholder — [article](../content/wiki/nen-tang/sql/join.md); include one-to-many cardinality and inflated totals. |
| S6 | Xử lý ngày giờ trong SQL | New, `nen-tang/sql/`; apply F3 to grouping hours, days, and date comparisons. |
| S7 | Tạo bảng và thêm, sửa, xóa dữ liệu bằng SQL | New, `nen-tang/sql/`; introductory DDL/DML for transformations and date replacement. Earlier loading uses supplied setup SQL. |
| S8 | Biểu thức bảng chung (CTE) | Placeholder; optional — [article](../content/wiki/nen-tang/sql/cte.md) |

### Nền tảng — lập trình với Python

All titles below are new, under proposed `nen-tang/python/`. Keep introductory articles short and worked examples small. Deep reference sections are optional. Week 3 needs a beginner pilot to check conversation and practice load.

| ID | Wiki title | Scope |
| --- | --- | --- |
| P1 | Bắt đầu với Python: môi trường chạy, biến và kiểu dữ liệu | Run a script, virtual environment, pinned dependencies, strings and numbers; integer/decimal money versus floating point. |
| P2 | Điều kiện, vòng lặp và cấu trúc dữ liệu trong Python | Lists, dictionaries, conditions, iteration over records. |
| P3 | Hàm và module: tổ chức một chương trình Python | Separate reading, validation, and output into understandable functions. |
| P4 | Đọc CSV, JSON và xử lý dữ liệu không hợp lệ | File resources, conversions, exceptions, and useful rejection details. |
| P5 | Đọc cấu hình và sử dụng biến môi trường | Local configuration, database credentials, and keeping secrets out of Git. |
| P6 | Kết nối và truy vấn cơ sở dữ liệu bằng Python | Parameterized SQL, transaction handling, closing connections; tested PostgreSQL driver example. |
| P7 | Kiểm thử chương trình xử lý dữ liệu | Small fixtures, expected results, failure cases, and rerun assertions. |
| P8 | Ghi log và tổ chức chương trình thành job có thể chạy lại | Date argument, stage logs, run outcome, exit code, and a single entry point. |

### Nền tảng — mô hình hóa dữ liệu

| ID | Wiki title | State / canonical file |
| --- | --- | --- |
| M1 | Mô hình hóa dữ liệu là gì? | Placeholder — [article](../content/wiki/nen-tang/data-modeling/overview.md) |
| M2 | Grain: mỗi dòng dữ liệu đại diện cho điều gì? | New, `nen-tang/data-modeling/`; order, item, day, and aggregation boundaries. |
| M3 | Bảng Fact và Dimension | Placeholder — [article](../content/wiki/nen-tang/data-modeling/fact-and-dimension.md) |
| M4 | Mô hình ngôi sao | Placeholder; optional — [article](../content/wiki/nen-tang/data-modeling/star-schema.md) |

### Data Engineering

Use the beginner portions of these existing articles. Review examples against the project contract; link advanced sections as optional.

| ID | Wiki title | State / canonical file |
| --- | --- | --- |
| E1 | Data Ingestion: đưa data ra khỏi Source System | Content — [article](../content/wiki/data-engineering/data-ingestion.md) |
| E2 | ETL và ELT khác nhau thế nào? | Content — [article](../content/wiki/data-engineering/etl-elt.md) |
| E3 | Vì sao cần Data Warehouse? | Content — [article](../content/wiki/data-engineering/data-warehouse.md) |
| E4 | Data Quality: làm sao biết data đủ tin cậy? | Content — [article](../content/wiki/data-engineering/data-quality.md) |
| E5 | Idempotency: chạy lại pipeline mà không tạo duplicate | Content — [article](../content/wiki/data-engineering/idempotency.md) |
| E6 | Một Data Pipeline hoạt động ra sao? | Content — [article](../content/wiki/data-engineering/data-pipeline.md) |
| E7 | Data Orchestration khi nhiều job phụ thuộc nhau | Content — [article](../content/wiki/data-engineering/orchestration.md); optional context for sequencing and failure propagation. |
| E8 | Sửa lại data trong quá khứ với Backfill | Content; optional — [article](../content/wiki/data-engineering/backfill.md) |

### Công nghệ — công cụ hỗ trợ thực hành

| ID | Wiki title | State / scope |
| --- | --- | --- |
| T1 | Git cho dự án đầu tiên: lưu và xem lại thay đổi | New, `technologies/git/`; tool commands for init, status, diff, add, commit, and ignore. General version-control concepts belong in Nền tảng. |
| T2 | Chạy PostgreSQL trên máy cá nhân và kết nối lần đầu | New, `technologies/postgresql/`; tested setup, SQL client, connection checks, teardown, and common errors. |
| T3 | Lên lịch chạy Python job trên máy cá nhân | New, `technologies/`; author tool-specific OS recipes after selecting the supported environments; paths, environment, logs, and sleeping-machine limitations. |

The report template, café-specific metrics, exercise data, expected outputs, and week-by-week integration instructions belong to the learning path. They are not additional Wiki articles. New titles refine the coverage plan's subjects; they do not require publishing every advanced subtopic or creating empty placeholders.

## 8. Final project: Chọn dự án của bạn, cùng AI thiết kế và hoàn thành

Learners choose **one of three projects**, then work with the AI mentor from brainstorming through verification. Independence means owning decisions and explaining the result; AI assistance and generated code are allowed.

Reserve week 6 (6–8 hours), including brainstorming and handover. Each option uses two or three supplied input tables, two or three core questions, one local batch pipeline, and one CSV/HTML report. Reuse the environment, database helpers, report renderer, and check harness. Learners implement the domain transformations and checks; do not supply a finished implementation. Optional features start only after the core passes.

Provide synthetic datasets, a data dictionary, an explicit reporting period or cutoff, a tiny hand-checkable fixture with author-verified answers, a larger practice fixture, and failure/correction fixtures for every option. No scraping, bank integration, live utility tariffs, or external accounts are required. Personal data is an optional later extension and is not needed for mentoring or assessment.

### Option A — Chi tiêu và mục tiêu tiết kiệm

Question: “Tiền của mình đi đâu, và tháng này có đạt mục tiêu tiết kiệm không?”

- Inputs: `transactions` (one row per transaction ID), `category_budgets` (one row per month/category), and `savings_goals` (one row per month).
- Transactions include date, type, positive integer VND amount, category, and an original transaction reference for refunds. Explicit types distinguish income, expense, refund, and internal transfer; use provided categories rather than an AI classification requirement.
- Core report: net spending by category; spending versus category budget; monthly income minus net spending compared with the savings goal. Label the last metric as a period surplus, not a bank balance or investment return.
- Rules: exclude internal transfers from income and spending; subtract refunds from expenses in the refund's posting month using the original expense category. Provide the original references needed by the fixture. Missing budget means unavailable, not zero; allow negative net category spending when refunds exceed current-period expenses.
- Challenge: a transfer between two owned accounts must not change spending or surplus. A repeated import must not duplicate either side.
- Optional extension: a monthly trend or custom category mapping.

### Option B — Mua hàng online: giá rẻ có thật sự rẻ?

Question: “Sau giảm giá, phí giao hàng và hoàn tiền, mình thực sự đã trả bao nhiêu?”

- Inputs: `orders` (one row per order ID with purchase date, merchant, order discount, shipping fee), `order_items` (one row per order/line with quantity and original unit price), and `refunds` (one row per refund ID with order reference, posting date, and amount).
- Core report: final purchase cost by order as of a stated cutoff; total cost by merchant for the selected purchase cohort; orders with full or partial refunds and refunded amounts.
- Rules: final cost = item subtotal − order-level discount + shipping − refunds posted by cutoff. Amounts are integer VND; the fixture contains paid orders only and no taxes or currency conversion. Refund amount is the actual returned money, including any shipping refund; do not infer extra deductions. Future refunds do not affect an earlier cutoff.
- Challenge: aggregate items and refunds to order grain before joining so multiple items and refund records do not multiply money. Charge shipping and the order discount once.
- Do not claim that a promotion was cheaper than another retailer without comparative price data. The core measures actual cost rather than market-wide savings.
- Optional extension: compare merchants over time using the supplied history.

### Option C — Điện nhà mình: tiền tăng vì đâu?

Question: “Tiền điện thay đổi vì dùng nhiều hơn hay vì đơn giá khác đi?”

- Inputs: `meter_readings` (one cumulative reading per meter/timestamp), `tariff_periods` (one fictional flat VND/kWh rate per monthly period), and `billing_periods` (one row per period with required start/end boundaries).
- Core report: monthly kWh consumed; estimated monthly charge; a two-period comparison separating consumption and rate effects.
- Rules: use one meter, exact monthly boundary readings, and a simplified fictional flat tariff. Consumption = ending reading − starting reading; estimated charge = consumption × rate. No tax, tiered pricing, standing charges, or real utility-bill claims. Use fixture values with exact arithmetic or specify decimal rounding in the contract.
- Missing boundary readings make the period incomplete, not zero usage; do not interpolate in the core. Reject duplicate reading keys, negative deltas, and missing/overlapping tariff coverage. Meter resets are outside scope and must be flagged.
- For two complete periods, let usage be q1/q2 and rates p1/p2: consumption effect = (q2 − q1) × p1; rate effect = q2 × (p2 − p1). Their sum equals the charge difference. Supply this identity and a small worked example in the brief; choosing the decomposition is not a prerequisite.
- Challenge: explain why a missing reading cannot support a “zero usage” report and verify the charge-difference reconciliation.
- Optional extension: daily usage from an additional supplied fixture.

### AI-assisted final-project journey

| Stage | Mentor role | Learner-owned output |
| --- | --- | --- |
| **Choose** | Ask which everyday question interests the learner, explain the three options and comparable scope, and help choose one. | Selected project and intended report user. |
| **Brainstorm** | Explore two or three useful questions, inspect available fields, and distinguish answerable questions from those needing new data. Keep extra ideas in a later-work list. | Core questions and one optional extension. |
| **Define** | Ask about grains, dates, formulas, edge cases, and what a correct answer looks like. Help draft a brief and ask the learner to confirm it before coding. | `project-brief.md`: inputs, grains, metric rules, report sketch, checks, and scope. |
| **Build** | Help split work into small steps; offer hints, examples, and debugging based on shared local evidence. Refer to the existing Wiki sources as needed. | Working ingestion → transformation → report, with incremental checks. |
| **Challenge** | Introduce a supplied edge case or changed input and ask for a prediction before rerunning. Compare outputs to the fixed reference contract. | Correct local results, repeat-run evidence, and a demonstrated failure/recovery. |
| **Present** | Ask the learner to explain a decision, an AI suggestion they verified or corrected, an observation, and a limitation. Review against the common rubric. | README, report, progress record, and short written or recorded walkthrough. |

Suggested week-6 budget: 1 hour to choose and define, 3–4 hours to build, 1–2 hours to verify, and 1 hour to present. Scope down optional work if needed; if the core exceeds the budget in pilots, adjust the estimate rather than skipping checks.

The fixed dataset and metric contracts provide reliable reference answers. Brainstorming personalizes the report emphasis and optional features; it does not silently change required metric definitions. Any intentional alternative definition must be labeled separately and cannot replace the reference checks.

Example opening:

> “Bạn muốn hiểu cách mình tiêu tiền, mua sắm hay sử dụng điện? Sau khi xem báo cáo, bạn muốn biết điều gì để đưa ra quyết định?”

Example follow-up for personal finance:

> “Bạn chuyển 500.000 đồng giữa hai tài khoản của mình. Theo bạn, khoản này có làm tăng chi tiêu không? Hãy ghi quy tắc đó vào brief và tạo một ví dụ để kiểm tra.”

Common deliverables: confirmed brief, source-to-report diagram, executable pipeline, CSV/HTML report, automated checks, safe rerun and failure/recovery demonstration, README, and walkthrough. Require one observation, one investigation question, one limitation, and an example of an AI suggestion verified or corrected. Learners must run, explain, test, and adapt their work. AI feedback is advisory; executable evidence and the rubric establish completion.

### Assessment

Score each dimension 0 (missing or incorrect), 1 (partially demonstrated), or 2 (complete with evidence).

| Dimension | Evidence for score 2 |
| --- | --- |
| Correctness | Matches the chosen project’s reference fixture and metric contract; handles its required edge cases correctly. |
| Reproducibility | Runs from the documented clean environment and supplied inputs. |
| Safe rerun and recovery | Repeat input preserves results; demonstrated failure is recoverable without partial published output. |
| Data quality | Detects invalid input and distinguishes missing data from valid empty results. |
| Modeling and reporting | Explicit grains, correct denominators, useful report, visible date and freshness. |
| Explanation | Clear README, reasoned design decision, observation, and limitation. |

Proposed completion gate: at least 9/12, with correctness, reproducibility, and safe rerun/recovery each scoring 2. Failed dimensions receive targeted revision tasks. This is a course completion rubric.

## 9. AI learning companion and Wiki-derived course pack

### Content ownership

**The Wiki is the canonical source for technical learning content.** Author and review explanations, examples, and reusable troubleshooting there. The learning path owns sequencing, project requirements, datasets, follow-ups, hints, mentoring instructions, and assessment. The course pack is generated from these two sources; it is not a separately authored textbook.

```text
Canonical Wiki articles + learning-path briefs and exercises
                            ↓
             Versioned, generated course pack
                            ↓
            Learner imports it into NotebookLM
                            ↓
       Discuss → attempt locally → share evidence → verify
                            ↓
                Save progress and continue
```

Learners begin with the mentor and a small task; standalone Wiki reading is offered when useful rather than assigned as a parallel course. The mentor is asked to ground technical explanations in the imported Wiki material and cite its sections. When the material does not support an answer, it should identify that gap, distinguish a hypothesis from a documented explanation, and suggest what evidence or reference is needed. It must not invent course requirements or expected results.

### Dedicated link and onboarding

The path overview offers **Học cùng AI**, a copyable course-source URL, and a copyable Vietnamese mentor prompt. Proposed route: `/learning-paths/nhap-mon-data-engineering/ai-source/`; this is a planning example, not an existing published URL or a decision to rename the current path.

1. Learner opens the course page and downloads the local starter materials.
2. Learner creates a personal NotebookLM notebook and imports the course-source URL.
3. Learner checks that the imported source contains the expected version, available weeks, lesson text, and a sample code block.
4. Learner selects Learning Guide or configures a custom role, then pastes the mentor prompt explicitly.
5. Mentor asks about prior SQL/Python experience, operating system, available study time, and current checkpoint, one question at a time. A newcomer starts with week 1; experienced readers demonstrate the entry checkpoint.
6. Learner builds locally, shares relevant evidence for feedback, and saves a progress journal before leaving.
7. After the café checkpoints, the mentor introduces the three final-project options and follows the choose → brainstorm → define → build → challenge → present journey in section 8.

Google's [source-import documentation](https://support.google.com/notebooklm/answer/16215270?hl=en) states that web imports capture the supplied HTML page's text, not nested webpages. Therefore a list of Wiki links is insufficient: the export must contain the actual selected lesson text, examples, project contract, exercises, and troubleshooting. Google's [chat documentation](https://support.google.com/gemininotebook/answer/16179559) describes Learning Guide and Custom styles. These capabilities were checked during planning on 27 September 2026; recheck labels, limits, and import behavior during the pilot.

### Export requirements

- Generate from an explicit manifest of canonical article paths and selected sections, plus the path's owned materials. Preserve each section's title, stable ID, original URL, and source revision.
- Render essential content as accessible static HTML text, including code, tables, and text descriptions of diagrams. Downloads and linked pages are not assumed to have been imported.
- Include course version, build date, available weeks, required environment versions, metric definitions, small input/output examples, and completion criteria. The full datasets and local checks remain downloadable project assets.
- Include only reviewed, available lessons for the advertised scope. Label a first-two-milestone pack accordingly; never replace missing lessons with unexplained links or TODOs.
- Include all three final-project briefs, source contracts, small verified examples, assessment criteria, and the final-project mentoring instructions. The mentor focuses on the chosen option; full datasets remain project downloads.
- Keep complete worked solutions outside the default pack. Provide acceptance results and progressive hints; make solution import an explicit learner choice. Prompt instructions are guidance, not a guarantee against revealing answers.
- Regenerate when canonical content changes; do not hand-edit duplicated lesson text. Keep versioned releases and a change log so a learner can finish a stable course version.
- Tell learners to check their imported version and replace/re-import the source when upgrading; do not assume a website update reaches an existing notebook automatically.
- Pilot the single-link export against current service limits and retrieval quality. If it becomes unwieldy, preserve one onboarding page with clearly labeled module-pack URLs and a downloadable text/Markdown fallback.

### Mentor behavior and starter prompt

The mentor teaches, coaches, troubleshoots, and reviews. It asks one focused question at a time, offers progressively stronger hints, and asks for explanation or a small variation after a successful fix. A source document containing these instructions does not configure the assistant by itself; the learner must paste the prompt into chat or custom configuration.

Proposed Vietnamese starter prompt:

> Bạn là người hướng dẫn của tôi trong lộ trình Nhập môn Data Engineering. Dùng nội dung Wiki và yêu cầu dự án trong course pack đã nhập làm tài liệu chính; dẫn tên bài hoặc mục liên quan khi giải thích. Bắt đầu bằng việc hỏi từng câu để biết kinh nghiệm, hệ điều hành, cấu hình máy, công cụ đã cài và checkpoint hiện tại của tôi. Hướng dẫn tôi cài đặt và cấu hình các công cụ trên máy theo hướng dẫn đã kiểm thử: mỗi lần một bước, kèm lệnh kiểm tra, rồi chờ tôi gửi kết quả trước khi tiếp tục. Nếu lỗi cài đặt, hỏi lệnh đã chạy và thông báo lỗi đầy đủ, đề xuất một phép kiểm tra, giúp tôi sửa rồi xác nhận kết nối hoạt động. Mỗi lần giao một bước vừa sức, để tôi thử trước và gợi ý dần khi tôi mắc kẹt. Khi debug, hỏi code hoặc câu lệnh liên quan, lỗi đầy đủ, kết quả mong đợi và thực tế; đề xuất một bước kiểm tra rồi chờ kết quả. Nhắc tôi bỏ mật khẩu và thông tin bí mật trước khi gửi. Phân biệt giả thuyết với kết quả đã kiểm chứng; nói rõ khi tài liệu chưa đủ để trả lời. Nếu đưa code mẫu, giải thích và yêu cầu tôi chạy, kiểm tra, rồi thử một thay đổi nhỏ. Chỉ nhận xét checkpoint dựa trên bằng chứng tôi cung cấp; không nói rằng bạn đã chạy code trên máy tôi. Cuối buổi, giúp tôi ghi lại tiến độ, điều chưa rõ và bước tiếp theo.

Example coaching exchange:

> Learner: “Em JOIN hai bảng rồi mà doanh thu tăng gấp đôi.”
>
> Mentor: “Mỗi dòng trong hai bảng đại diện cho điều gì? Em thử lọc một order_id có nhiều món và gửi các dòng sau JOIN nhé.”
>
> After the learner explains and fixes the duplication: “Nếu cần tính cả số đơn và số món bán được, em sẽ tính hai chỉ số đó như thế nào?”

Importing a course link does not give the mentor access to the learner's local files or terminal. Troubleshooting uses the code, commands, errors, environment details, and results that the learner shares. A suggested correction becomes verified only after local execution and relevant checks. Do not let a plausible explanation or an AI-generated score substitute for correct output.

### Switching to final-project mentoring

At milestone 6, explicitly move from the café's prescribed tasks to learner-led design within the selected brief. Carry forward the learner's demonstrated skills and unresolved gaps. Add this prompt to the conversation:

> Tôi đã hoàn thành các checkpoint của dự án quán cà phê. Hãy giúp tôi chọn một trong ba dự án cuối khóa: chi tiêu và mục tiêu tiết kiệm, mua hàng online, hoặc sử dụng điện. Hỏi về điều tôi muốn tìm hiểu, rồi cùng tôi brainstorm hai hoặc ba câu hỏi phù hợp với dữ liệu được cung cấp. Giúp tôi làm rõ grain, công thức, thời gian báo cáo, trường hợp lỗi và tiêu chí hoàn thành trong project-brief.md; để tôi xác nhận trước khi viết code. Giữ các quy tắc bắt buộc của đề bài, đưa ý tưởng ngoài phạm vi vào danh sách làm thêm. Sau đó hướng dẫn từng bước theo bằng chứng tôi chạy trên máy, giúp debug và yêu cầu tôi giải thích, kiểm chứng rồi thử một thay đổi nhỏ. Cuối cùng cùng tôi đối chiếu kết quả với rubric và ghi lại điều còn hạn chế.

### Progress and assessment

Provide a learner-owned `learning-journal.md` template with course-pack version, current week/checkpoint, completed evidence, concepts explained, unresolved issue, and next action. For the final project, also record the selected option, brief version, confirmed definitions, deferred ideas, and checks passed. Save it locally at the end of a session and paste the relevant entry when resuming or changing notebooks. Chat memory is a convenience, not the progress record.

AI use is an explicit learning skill throughout the course. Learners may request explanations, diagnostics, examples, and generated code. Required evidence remains the same: run it, verify it against the fixture, explain it, and adapt it. Keep the fixed skill checkpoints while allowing the mentor to adjust explanation depth and practice pace.

### First-two-milestone pilot

Test with beginners before extending the companion to all six milestones. Verify that:

- One URL imports actual lesson text, code, metric definitions, and exercise requirements with the correct version.
- The mentor cites relevant source sections, asks useful diagnostic questions, and distinguishes missing context from a confirmed cause.
- A learner can diagnose the duplicate-JOIN exercise, run the corrected query locally, and explain why it works.
- A new session can resume using the saved progress note.
- The mentor handles unsupported questions without inventing requirements and does not treat unrun code as a passed checkpoint.
- Learners can use the website and local checks when AI access is unavailable.

Record task completion, hint usefulness, unsupported claims, premature solution reveals, and actual study time. Revise the pack and prompt from observed behavior; do not promise consistent mentoring merely because the prompt requests it.

## 10. Materials and release sequence

Prepare these materials alongside the relevant articles:

1. Versioned tiny and multiweek datasets, dictionaries, manifests, failure fixtures, and verified answer files.
2. Tested environment instructions, initial SQL fixture, and a preview of the completed report.
3. Progressive starter checkpoints that preserve learner work, with worked solutions stored separately.
4. HTML/chart template and documented report-data interface, including unavailable and failed-data states.
5. Weekly briefs, required follow-ups, optional hints, acceptance checks, and troubleshooting.
6. Three final-project briefs and synthetic dataset packs, each with dictionary, verified fixtures, edge cases, and reviewer notes; shared brief template, rubric, and AI brainstorming/mentoring prompt.
7. Wiki-to-pack manifest and generator, versioned import page, mentor prompt, onboarding instructions, and progress-journal template.

Author and release in coherent units:

| Unit | Authoring priority | Release gate |
| --- | --- | --- |
| Milestones 1–2 | Dataset contract, setup, core Wiki sections, mentor onboarding, first course pack | Beginner starts with AI, reproduces correct SQL metrics, and completes the companion pilot in section 9. |
| Milestones 3–4 | Python, loading, transactions, summary tables, report template | Beginner builds the first end-to-end report and explains invalid input and rollback. |
| Milestone 5 | Quality checks, safe replacement, local job operation | Guiding project passes clean-setup and failure/recovery checks. |
| Milestone 6 | Three bounded project options, starter harness, verified fixtures, common rubric, and final-project mentor flow | Pilot every option: learners can choose, confirm a brief with AI, build and verify the new problem within the proposed budget without a worked implementation. |

Pilot with beginners and record setup time, mentor dialogue and targeted reading time, exercise time, and recurring misunderstandings. Adjust duration or split overloaded weeks before advertising the complete path. Partial releases must state which weeks are available, and required links must resolve to usable content.

During later site implementation, reconcile the existing draft [foundation path](../content/learning-paths/data-engineer-foundation.md) with the title **Nhập môn Data Engineering**. Decide URL preservation explicitly. This planning document creates no lesson pages and changes no published navigation.

## 11. Transition to Data Engineering thực chiến

The [Data Engineering thực chiến plan](data-engineering-thuc-chien-plan.md) develops the café domain into a multi-store system while supplying an independent starter dataset. It introduces requirements that exceed this local daily-snapshot project: multiple sources, payments and refunds, incremental changes, historical corrections, richer modeling, storage choices, deployment, observability, and operational tradeoffs.

The introductory completion boundary remains concrete: a learner can build, verify, run, repair, and explain a small source-to-report pipeline, and apply those skills independently to a changed business problem.
