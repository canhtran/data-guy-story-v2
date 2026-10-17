# Wiki Structure and Coverage Plan

Updated: 27 September 2026.

Status: proposed component plan for review. Follows the [general website plan](website-general-plan.md), including its four Wiki categories and five learning paths. This document defines the content map and writing priorities; it does not publish articles, move pages, or change navigation.

## 1. Purpose and scope

Build a Vietnamese reference library that readers can use to learn a subject, solve a specific problem, or revisit an engineering decision. The Wiki must support beginner learning while developing depth beyond the learning paths.

The unit of coverage is a reader question with a canonical article, an appropriate depth, prerequisites, and an example. A file existing in the repository does not mean the subject is covered.

Keep technical titles recognizable and explain English terms in conversational Vietnamese. Learning paths own weekly sequencing, project instructions, milestones, and assessment. The Wiki owns reusable knowledge, small worked examples, and reference material.

## 2. Current coverage

Repository snapshot, including current local edits. Counts exclude hubs from article totals. `draft: false` describes source configuration, not verified deployment or technical approval.

| Category | Hubs | Articles with content, `draft: false` | Draft article placeholders | Main gap |
| --- | ---: | ---: | ---: | --- |
| Bắt đầu | 1 | 7 | 0 | Review the transition into technical foundations |
| Nền tảng | 5 | 0 | 22 | All four existing subjects need writing; programming and computing basics are absent |
| Data Engineering | 1 | 23 | 0 | Introductory explanations exist; implementation depth, architecture, security, and operations need expansion |
| Công nghệ | 4 | 0 | 29 | Kafka, Flink, and Spark are scaffolds; beginner tooling is absent |
| **Total** | **11** | **30** | **51** | **81 article files; most are not yet usable readings** |

There is also a Wiki root hub. The complete article inventory is in section 9.

Two useful legacy articles remain under `content/docs/foundation/`: `data-la-gi.md` and `cac-loai-du-lieu.md`. Review and reuse these before writing equivalent explanations. The legacy foundation hub describes a 19-article sequence, but only these two article files exist there; that sequence is not current coverage.

The general plan references three component documents that are absent in the current working tree: `data-engineering-content-plan.md`, `content-migration-plan.md`, and `ai-content-guidelines.md`. This plan does not assume their contents or restore them. The older scaffold proposal is historical context; its technology-specific learning paths do not override the five-path direction.

## 3. Category boundaries

| Category | Owns | Boundary example |
| --- | --- | --- |
| Bắt đầu | Profession, responsibilities, collaboration, orientation, how to learn | Explain why DEs build pipelines; link to the pipeline article for engineering detail |
| Nền tảng | Reusable data, programming, database, modeling, and computing foundations | Explain transactions and isolation independent of a particular product |
| Data Engineering | Designing, building, and operating data systems; choices across tools | Explain ingestion checkpoints and replay without requiring Kafka or Airflow |
| Công nghệ | A named tool's architecture, APIs, setup, configuration, troubleshooting, and operation | Explain Kafka offsets or PostgreSQL transaction behavior with versioned examples |

Use one canonical explanation per concept. An article may summarize a prerequisite in a few sentences and link onward; it should not reproduce the prerequisite article.

Specific boundary decisions:

- **Data modeling:** grain, keys, normalization, facts, dimensions, and SCD belong in Nền tảng. Applying models to transformation and serving requirements belongs in Data Engineering.
- **SQL optimization:** query plans and general reasoning belong in Nền tảng; engine-specific commands and tuning belong in Công nghệ.
- **File formats:** practical format selection and pipeline effects remain in the existing Data Engineering article. Basic types and serialization are foundation prerequisites; product configuration belongs in Công nghệ.
- **Distributed systems:** replication, partitioning, consistency, and failure models belong in Nền tảng. Streaming delivery guarantees belong in Data Engineering; Kafka/Flink guarantees explain their implementation and limits.
- **Platform engineering:** shared capabilities, tenancy, interfaces, and service ownership belong in Data Engineering. Linux/networking foundations belong in Nền tảng; Terraform or Kubernetes instructions belong in Công nghệ if selected.
- **Data Mesh:** retain the existing Bắt đầu article as optional orientation about roles. A future Data Engineering article would address organizational architecture, ownership, and tradeoffs, linking back rather than duplicating the introduction.

## 4. Proposed subject map — Danh mục chủ đề bằng tiếng Việt

Danh mục gồm nội dung hiện có và nội dung cần bổ sung. Mỗi chủ đề có thể phát triển thành một hoặc vài bài tùy độ sâu; danh mục này không đồng nghĩa với danh sách bài đã xuất bản. Trạng thái các bài hiện có nằm ở mục 9, thứ tự ưu tiên nằm ở mục 5.

Giữ nguyên bốn phần chính và URL hiện có. Các nhóm trong Data Engineering trước hết là nhóm biên tập trên trang hub, không yêu cầu chuyển các file hiện tại sang thư mục mới. Chỉ tạo thư mục nền tảng mới khi có nội dung hữu ích để đưa vào.

### 4.1. Bắt đầu

Giúp người đọc hiểu nghề, hiểu công việc và chọn điểm bắt đầu. Giữ sáu bài định hướng chính và bài đọc thêm về Data Mesh; phần này không trở thành một giáo trình kỹ thuật riêng.

1. **Data Engineer là gì?** Công việc và sự khác nhau với Data Analyst, Data Scientist, Analytics Engineer.
2. **Dữ liệu đi qua một hệ thống như thế nào?** Từ ứng dụng đến báo cáo và các sản phẩm sử dụng dữ liệu.
3. **Data Engineer xây những hệ thống gì?** Pipeline, kho dữ liệu, hệ thống streaming và nền tảng dữ liệu.
4. **Một data team làm việc với nhau như thế nào?** Trách nhiệm, phối hợp và trao đổi yêu cầu.
5. **Có AI rồi, còn cần học nền tảng không?** Sử dụng AI và kiểm chứng kết quả.
6. **Học Data Engineering từ đâu?** Kiến thức cần học, cách thực hành và cách sử dụng Wiki.
7. **Data Engineer trong Data Mesh** — bài đọc thêm về vai trò khi các domain sở hữu dữ liệu.

### 4.2. Nền tảng

Kiến thức sử dụng xuyên suốt nhiều công nghệ và nhiều kiểu hệ thống. Python là ngôn ngữ đề xuất ban đầu để minh họa lập trình, chưa phải quyết định cuối cùng về công nghệ của lộ trình.

#### 4.2.1. Dữ liệu cơ bản — đề xuất `data-basics/`

- Dữ liệu là gì?
- Dữ liệu có cấu trúc, bán cấu trúc và phi cấu trúc.
- Bản ghi, trường dữ liệu, bảng và schema.
- Kiểu dữ liệu và chuyển đổi kiểu.
- Giá trị thiếu, `NULL`, giá trị rỗng và giá trị mặc định.
- Số nguyên, số thực và độ chính xác khi tính tiền.
- Chuỗi ký tự, Unicode và mã hóa văn bản.
- Ngày giờ, múi giờ và cách biểu diễn thời gian.
- Dữ liệu trùng lặp và cách nhận diện một bản ghi.
- Biểu diễn dữ liệu trong file và quá trình serialization.

Rà soát và tái sử dụng hai bài giới thiệu dữ liệu trong `content/docs/foundation/` trước khi viết bài tương đương.

#### 4.2.2. SQL — hiện có `sql/`

- SQL là gì? Cách suy nghĩ khi truy vấn dữ liệu.
- Đọc, lọc và sắp xếp dữ liệu với `SELECT`, `WHERE`, `ORDER BY`.
- Tổng hợp dữ liệu với `GROUP BY`, `HAVING` và các hàm tổng hợp.
- `NULL` và logic điều kiện trong SQL.
- Kết hợp bảng bằng `JOIN`.
- Quan hệ một–một, một–nhiều, nhiều–nhiều và hiện tượng nhân bản dữ liệu khi JOIN.
- Kết hợp tập kết quả với `UNION`, `INTERSECT`, `EXCEPT`.
- Truy vấn con và CTE.
- Hàm cửa sổ — Window Functions.
- Xử lý chuỗi, ngày giờ và điều kiện với `CASE`.
- Tạo bảng, khai báo kiểu và ràng buộc dữ liệu.
- Thêm, sửa, xóa và hợp nhất dữ liệu.
- View và Materialized View.
- Đọc kế hoạch thực thi truy vấn.
- Nguyên tắc tối ưu truy vấn.
- Kiểm tra tính đúng đắn của kết quả SQL.

#### 4.2.3. Lập trình với Python — đề xuất `python/`

- Python trong công việc Data Engineering.
- Biến, kiểu dữ liệu và các cấu trúc dữ liệu cơ bản.
- Điều kiện, vòng lặp và cách tổ chức luồng xử lý.
- Hàm, module và tổ chức một chương trình.
- Đọc và ghi file.
- Làm việc với CSV và JSON.
- Xử lý ngày giờ và chuyển đổi kiểu dữ liệu.
- Xử lý lỗi và quản lý tài nguyên.
- Ghi log để hiểu chương trình đang làm gì.
- Môi trường chạy, package và quản lý dependency.
- Đọc cấu hình và sử dụng biến môi trường.
- Gọi HTTP API.
- Kết nối và truy vấn cơ sở dữ liệu.
- Iterator, generator và xử lý dữ liệu theo từng phần.
- Kiểm thử chương trình xử lý dữ liệu.
- Tổ chức một chương trình thành job có thể chạy lại và bảo trì.

Phạm vi tập trung vào việc viết và duy trì data job; không xây dựng tài liệu tham chiếu cho toàn bộ ngôn ngữ Python.

#### 4.2.4. Cơ sở dữ liệu — hiện có `database/`

- Cơ sở dữ liệu là gì? Khi nào file không còn đủ?
- Mô hình dữ liệu quan hệ.
- Khóa chính, khóa ngoại và ràng buộc dữ liệu.
- OLTP và OLAP.
- Cơ sở dữ liệu lưu và đọc dữ liệu như thế nào?
- Lưu theo hàng và lưu theo cột.
- Chỉ mục — Index.
- Giao dịch — Transaction.
- Các thuộc tính ACID.
- Truy cập đồng thời và các mức cô lập giao dịch.
- Khóa, deadlock và kiểm soát đồng thời.
- NoSQL là gì? Các mô hình key-value, document, wide-column và graph.
- Chọn cơ sở dữ liệu theo đặc điểm truy cập và yêu cầu hệ thống.

#### 4.2.5. Mô hình hóa dữ liệu — hiện có `data-modeling/`

- Mô hình hóa dữ liệu là gì?
- Chuyển khái niệm nghiệp vụ thành thực thể và quan hệ.
- Mô hình khái niệm, logic và vật lý.
- Grain: mỗi dòng dữ liệu đại diện cho điều gì?
- Business Key và Surrogate Key.
- Chuẩn hóa và phi chuẩn hóa dữ liệu.
- Bảng Fact và Dimension.
- Các loại Fact và cách tổng hợp chỉ số.
- Mô hình ngôi sao — Star Schema.
- Mô hình bông tuyết — Snowflake Schema.
- Dimension thay đổi chậm — SCD.
- Mô hình hóa quan hệ nhiều–nhiều.
- Mô hình hóa lịch sử và dữ liệu có hiệu lực theo thời gian.
- Dữ liệu đến muộn trong mô hình phân tích.
- Kiểm tra mô hình bằng câu hỏi nghiệp vụ và truy vấn thực tế.

#### 4.2.6. Nền tảng máy tính và phát triển phần mềm — đề xuất `computing/`

- File, thư mục, đường dẫn và hệ thống file.
- Sử dụng terminal và các lệnh shell cơ bản.
- Process, exit code và chương trình chạy nền.
- Người dùng, nhóm và quyền truy cập file.
- Biến môi trường, cấu hình và thông tin bí mật.
- Git: commit, branch, merge và xử lý xung đột.
- HTTP: request, response, method và status code.
- DNS, địa chỉ IP, port và kết nối TCP.
- CPU, bộ nhớ, ổ đĩa và mạng ảnh hưởng đến chương trình như thế nào?
- Phân biệt lỗi chương trình, lỗi môi trường và lỗi kết nối.
- Dependency, phiên bản và môi trường có thể tái tạo.

Giải thích khái niệm Git tại đây; quy trình dùng một dịch vụ Git cụ thể thuộc phần Công nghệ nếu cần.

#### 4.2.7. Hệ thống phân tán — hiện có `distributed-systems/`

- Hệ thống phân tán là gì? Vì sao cần nhiều máy?
- Phân vùng dữ liệu — Partitioning.
- Sao chép dữ liệu — Replication.
- Tính nhất quán — Consistency.
- Định lý CAP và phạm vi áp dụng.
- Lỗi từng phần, timeout và sự không chắc chắn.
- Khả năng chịu lỗi và phục hồi.
- Thứ tự sự kiện và đồng hồ trong hệ thống phân tán.
- Điều phối, bầu leader và đồng thuận.
- Các đánh đổi nền tảng khi giao nhận thông điệp qua mạng.
- Đánh đổi giữa độ trễ, thông lượng, tính sẵn sàng và tính đúng đắn.

Đây là kiến thức trung cấp và nâng cao, không phải điều kiện để bắt đầu pipeline đơn giản đầu tiên. Phần Data Engineering sở hữu bài giải thích đầy đủ về bảo đảm giao nhận trong pipeline streaming.

### 4.3. Data Engineering

Kiến thức về thiết kế, xây dựng và vận hành hệ thống dữ liệu, độc lập với một sản phẩm cụ thể. Các bài hiện có tiếp tục là điểm đến chính thức cho khái niệm tương ứng; chỉ tách bài chuyên sâu khi có câu hỏi riêng cần trả lời.

#### 4.3.1. Yêu cầu và kiến trúc hệ thống

- Một Data Pipeline hoạt động ra sao?
- Chuyển nhu cầu nghiệp vụ thành yêu cầu dữ liệu.
- Xác định nguồn, người sử dụng và đầu ra của hệ thống.
- Yêu cầu về độ mới, độ trễ, khối lượng và chất lượng dữ liệu.
- Lựa chọn Batch hay Streaming.
- Thiết kế các lớp ingestion, storage, transformation và serving.
- Đánh đổi giữa độ phức tạp, chi phí và khả năng mở rộng.
- Xác định ranh giới, dependency và điểm có thể xảy ra lỗi.
- Ghi lại và đánh giá quyết định kiến trúc.

#### 4.3.2. Thu thập và tích hợp dữ liệu

- Data Ingestion: đưa dữ liệu ra khỏi hệ thống nguồn.
- Đọc dữ liệu từ file, database và API.
- Full Load và Incremental Load.
- Theo dõi tiến độ lấy dữ liệu bằng cursor và watermark.
- API pagination, rate limit và retry.
- Change Data Capture — CDC.
- Kết hợp snapshot ban đầu với dòng thay đổi.
- Xử lý cập nhật và xóa dữ liệu từ nguồn.
- Đối soát dữ liệu giữa nguồn và đích.
- Kiểm soát tải tác động lên hệ thống nguồn.
- Xử lý dữ liệu sai định dạng hoặc không hợp lệ khi tiếp nhận.

#### 4.3.3. Lưu trữ và phục vụ dữ liệu

- Data Warehouse.
- Data Lake.
- Lakehouse.
- Object Storage và những đặc điểm cần hiểu.
- File Format: CSV, JSON, Avro, Parquet và cách lựa chọn.
- Table Format: vai trò và tiêu chí lựa chọn.
- Tổ chức thư mục, bảng và partition.
- Partition Pruning và giảm dữ liệu phải đọc.
- Small Files và Compaction.
- Snapshot, Time Travel và vòng đời dữ liệu.
- Retention, lưu trữ dài hạn và xóa dữ liệu.
- Data Mart và các cách cung cấp dữ liệu cho người sử dụng.
- Semantic Layer và định nghĩa chỉ số dùng chung.

#### 4.3.4. Biến đổi và xử lý dữ liệu

- ETL và ELT.
- Batch Processing.
- Stream Processing — bài tổng quan, liên kết đến nhóm streaming chuyên sâu.
- Làm sạch, chuẩn hóa và kết hợp dữ liệu.
- Xử lý trùng lặp và lựa chọn bản ghi hợp lệ.
- Biến đổi dữ liệu tăng dần — Incremental Transformation.
- Áp dụng mô hình dữ liệu vào pipeline.
- Dependency giữa các bước biến đổi.
- Xử lý phân tán: task, partition và trao đổi dữ liệu.
- Shuffle, Data Skew và các điểm nghẽn.
- Lựa chọn tài nguyên và kiểm soát chi phí xử lý.
- Tái tạo kết quả khi chạy lại cùng dữ liệu và logic.

#### 4.3.5. Điều phối và vận hành đáng tin cậy

- Data Orchestration.
- Lịch chạy, dependency và điều kiện kích hoạt job.
- Múi giờ, khoảng dữ liệu xử lý và thời điểm chạy.
- Idempotency: chạy lại mà không tạo kết quả ngoài ý muốn.
- Retry, timeout và backoff.
- Backfill và xử lý lại dữ liệu quá khứ.
- Quản lý trạng thái và tiến độ của pipeline.
- Kiểm thử logic, tích hợp và toàn bộ pipeline.
- Triển khai thay đổi và rollback.
- Tách môi trường phát triển, kiểm thử và production.
- Data Observability: log, metric và dấu hiệu bất thường.
- SLI, SLO và kỳ vọng về dịch vụ dữ liệu.
- Cảnh báo có thể hành động được.
- Runbook và xử lý sự cố.
- Sao lưu, khôi phục và Disaster Recovery.

#### 4.3.6. Chất lượng và metadata

- Data Quality: dữ liệu có phù hợp với mục đích sử dụng không?
- Data Profiling: hiểu dữ liệu trước khi xử lý.
- Kiểm tra schema, từng bản ghi và toàn bộ dataset.
- Đối soát số lượng, giá trị và chỉ số nghiệp vụ.
- Đặt ngưỡng và quản lý vòng đời quy tắc chất lượng.
- Cách ly dữ liệu lỗi và xử lý ngoại lệ.
- Metadata.
- Data Lineage.
- Data Catalog.
- Data Contract.
- Schema Evolution và tính tương thích.
- Trách nhiệm sở hữu dữ liệu và xử lý vấn đề chất lượng.

Bài đối soát nguồn–đích thuộc nhóm tích hợp; nhóm này liên kết đến bài đó và tập trung vào tính đúng đắn nghiệp vụ. Quyền sở hữu dữ liệu dùng chung một bài với nhóm quản trị.

#### 4.3.7. Bảo mật và quản trị dữ liệu

- Phân loại dữ liệu và nhận diện dữ liệu nhạy cảm.
- Xác thực, phân quyền và nguyên tắc quyền tối thiểu.
- Quản lý credential và secret.
- Mã hóa dữ liệu khi truyền và khi lưu.
- Che giấu, thay thế và hạn chế lộ dữ liệu nhạy cảm.
- Kiểm soát truy cập theo bảng, dòng và cột.
- Audit Log và truy vết truy cập.
- Chính sách lưu giữ và xóa dữ liệu xuyên suốt các hệ thống.
- Quyền sở hữu, trách nhiệm và quy trình cấp quyền.
- Đưa các yêu cầu quản trị vào thiết kế pipeline.

Phần này giải thích thực hành kỹ thuật; hướng dẫn tuân thủ theo pháp luật cụ thể cần được nghiên cứu và rà soát riêng. Chính sách lưu giữ liên kết đến cơ chế thực hiện ở nhóm lưu trữ.

#### 4.3.8. Hệ thống streaming

- Event và mô hình dữ liệu sự kiện.
- Event Time và Processing Time.
- Window và phép tổng hợp trên dòng dữ liệu.
- Watermark và dữ liệu đến muộn.
- Thứ tự sự kiện và dữ liệu đến sai thứ tự.
- Stateful Processing.
- At-most-once, At-least-once và Exactly-once.
- Phạm vi bảo đảm đúng đắn từ nguồn đến đích.
- Duplicate, deduplication và idempotent sink.
- Checkpoint và khôi phục trạng thái.
- Replay và xử lý lại lịch sử.
- Stream–Stream Join và Stream–Table Join.
- Backpressure, độ trễ và giới hạn công suất.
- Thay đổi schema và nâng cấp ứng dụng streaming.

Watermark theo dõi tiến độ nguồn trong ingestion và watermark thời gian sự kiện phải được phân biệt rõ. Các bài streaming dẫn về khái niệm idempotency, schema evolution và hệ thống phân tán thay vì giải thích lại toàn bộ.

#### 4.3.9. Nền tảng dữ liệu dùng chung

- Data Platform là gì? Ai sử dụng nền tảng?
- Phân biệt xây một pipeline và xây khả năng dùng chung.
- Các năng lực cốt lõi của nền tảng dữ liệu.
- Giao diện, API và quy ước cho người sử dụng.
- Self-service và quy trình onboarding.
- Template và các quy trình triển khai chuẩn.
- Cấp phát tài nguyên và Infrastructure as Code.
- Quản lý môi trường và quy trình triển khai.
- Multi-tenancy và cách ly workload.
- Quota, quản lý công suất và phân bổ chi phí.
- Quyền truy cập và quản lý secret dùng chung.
- Giám sát và độ tin cậy của nền tảng.
- Data Product, quyền sở hữu theo domain và Data Mesh.
- Đánh giá mức độ sử dụng và giá trị nền tảng mang lại.

Các bài platform tập trung vào khả năng phục vụ nhiều người hoặc nhiều team, liên kết đến khái niệm vận hành và bảo mật chung. Huấn luyện mô hình ML, phát triển ứng dụng tổng quát và toàn bộ nội dung chứng chỉ cloud nằm ngoài phạm vi kế hoạch.

### 4.4. Công nghệ

Giữ cấu trúc hiện tại: **mỗi công nghệ có một hub riêng**, với đường dẫn trực tiếp như `/wiki/technologies/spark/`. Mở rộng phạm vi Wiki để bao phủ Spark, Flink, Kafka, Airflow, HDFS, MinIO và Docker. Việc một công nghệ thuộc phạm vi Wiki không bắt buộc nó phải xuất hiện trong một lộ trình học hoặc cùng một dự án.

Kafka, Flink và Spark đã có cấu trúc trong repository nhưng các bài còn là placeholder. Airflow, HDFS, MinIO và Docker là các mục cần bổ sung vào kế hoạch nội dung; không tạo hàng loạt hub rỗng ngay trong giai đoạn lập kế hoạch. Các sản phẩm khác được bổ sung theo nhu cầu tra cứu, thực hành và khả năng duy trì ví dụ.

**Các dòng chủ đề bên dưới là phạm vi cần bao phủ, không phải yêu cầu mỗi dòng phải có một bài riêng.** Bắt đầu bằng các bài đủ liền mạch để người đọc hiểu và thực hành, rồi tách bài chuyên sâu khi cần.

#### Cách nhóm công nghệ trên trang hub

| Nhóm điều hướng | Công nghệ / hướng mở rộng |
| --- | --- |
| Xử lý dữ liệu | Spark, Flink |
| Điều phối và biến đổi | Airflow; dbt là ứng viên bổ sung |
| Lưu trữ | HDFS, MinIO; các hệ thống lưu trữ và table format khác bổ sung dần |
| Truyền sự kiện và tích hợp | Kafka; công cụ CDC chọn sau |
| Cơ sở dữ liệu và truy vấn | PostgreSQL, DuckDB và các engine khác theo nhu cầu |
| Môi trường và hạ tầng | Docker; công cụ platform bổ sung dần |

Các nhóm chỉ phục vụ điều hướng trên trang Công nghệ. Không thêm tầng thư mục nhóm vào URL và không tạo thêm lộ trình chính theo từng công nghệ.

#### Độ lớn và cấu trúc bài viết

Mỗi công nghệ có thể bắt đầu với khoảng **4–6 bài**, tùy độ phức tạp. Đây là quy mô tham khảo, không phải chỉ tiêu cố định hay giới hạn dài hạn.

| Nhóm bài | Nội dung cần bao phủ |
| --- | --- |
| Tổng quan | Vấn đề công nghệ giải quyết, khi nào dùng và khi nào không |
| Kiến trúc và khái niệm chính | Các thành phần, vai trò và cách phối hợp |
| Thực hành đầu tiên | Môi trường tối thiểu, ví dụ chạy được và cách kiểm tra kết quả |
| Sử dụng trong hệ thống dữ liệu | Đọc/ghi, tích hợp và các cách sử dụng phổ biến |
| Vận hành và xử lý lỗi | Cấu hình, giám sát, bảo mật, lỗi thường gặp và phục hồi |
| Chuyên sâu | Hiệu năng, cơ chế nội bộ hoặc tình huống phức tạp khi có nhu cầu |

Có thể gộp các nhóm gần nhau hoặc phát triển nhiều bài trong một nhóm. Hub chỉ giới thiệu, sắp xếp và dẫn đến bài viết; không lặp lại toàn bộ bài tổng quan. Ví dụ cần ghi phiên bản và môi trường đã kiểm chứng.

Chỉ tách một bài riêng khi nó trả lời được một câu hỏi độc lập, có ví dụ hoặc tình huống riêng, và hữu ích để tra cứu trực tiếp. Nếu người đọc phải mở nhiều trang ngắn mới hiểu được một cơ chế, ưu tiên giải thích liền mạch trong cùng bài.

Ví dụ áp dụng:

- Docker: giải thích image, container và vòng đời container cùng nhau; đưa volume và network vào bài thực hành môi trường dữ liệu.
- Flink: giới thiệu state, checkpoint và savepoint trong bài về phục hồi; tách cơ chế checkpoint hoặc nâng cấp job bằng savepoint khi phát triển nội dung sâu hơn.
- Spark: giải thích luồng thực thi tổng thể trước; shuffle và tối ưu có thể thành bài riêng khi có ví dụ đủ sâu.
- Airflow: giới thiệu DAG và task cùng nhau; scheduling, data interval và backfill có thể thành một bài liền mạch trước khi mở rộng từng tình huống.

Các placeholder hiện có là bản kiểm kê chủ đề, không phải cấu trúc bài bắt buộc. Khi viết, chọn bài chính cho từng nhóm và cập nhật liên kết để tránh lặp nội dung. Mọi việc gộp, chuyển hoặc bỏ trang hiện có phải được xử lý trong bước triển khai, kiểm tra liên kết và giữ URL đã công bố hoặc có redirect; kế hoạch này không thay đổi file nội dung.

#### 4.4.1. Apache Kafka — hiện có `kafka/`

- Kafka là gì? Khi nào nên sử dụng?
- Kiến trúc Kafka.
- Topic, Partition và Key.
- Producer.
- Consumer và Consumer Group.
- Offset và quản lý tiến độ đọc.
- Replication.
- Rebalancing.
- Delivery Semantics.
- Transactions.
- Retention và Log Compaction.
- Schema và khả năng tương thích.
- Kết nối Kafka với hệ thống khác.
- Bảo mật và phân quyền.
- Theo dõi lag, thông lượng và tình trạng cluster.
- Tuning, xử lý sự cố và phục hồi.

#### 4.4.2. Apache Flink — hiện có `flink/`

- Flink là gì? Khi nào nên sử dụng?
- Kiến trúc Flink.
- Job, Operator, Task và Subtask.
- Parallelism.
- State.
- Event Time.
- Window.
- Watermark.
- Checkpoint.
- Savepoint.
- Exactly-once và điều kiện để đạt được.
- Source, Sink và Connector.
- Backpressure.
- Khôi phục, nâng cấp và thay đổi mức song song.
- Giám sát, quản lý tài nguyên và xử lý sự cố.

#### 4.4.3. Apache Spark — hiện có `spark/`

- Spark là gì? Khi nào nên sử dụng?
- Kiến trúc Spark.
- Job, Stage và Task.
- RDD.
- DataFrame và Spark SQL.
- Partition.
- Shuffle.
- Catalyst.
- Các chiến lược JOIN.
- Data Skew.
- Cache và Persist.
- Đọc, ghi và tổ chức dữ liệu.
- Structured Streaming.
- Checkpoint và phục hồi streaming query.
- Đọc Spark UI và kế hoạch thực thi.
- Quản lý tài nguyên, tối ưu và xử lý sự cố.

#### 4.4.4. Docker và công nghệ phục vụ thực hành nhập môn

| Công nghệ | Nhóm chủ đề |
| --- | --- |
| PostgreSQL | Cài đặt; kết nối; schema và bảng; nhập/xuất dữ liệu; truy vấn; transaction; index và query plan; quyền truy cập; sao lưu/khôi phục |
| DuckDB | Truy vấn file cục bộ; CSV/JSON/Parquet; phân tích bằng SQL; tích hợp Python; giới hạn tài nguyên và phạm vi sử dụng |
| Docker | Image và container; volume; network; cấu hình; Docker Compose; log; môi trường thực hành có thể tái tạo |

Docker thuộc phạm vi Wiki đã thống nhất; mức độ sử dụng trong dự án Nhập môn được quyết định riêng. Chọn PostgreSQL và/hoặc DuckDB cho dự án theo yêu cầu thực hành, đồng thời có thể phát triển tài liệu tra cứu độc lập. Bài Blog Docker hiện có là góc nhìn cá nhân bổ trợ, không thay thế bài hướng dẫn kỹ thuật.

#### 4.4.5. Airflow và công nghệ biến đổi, điều phối

| Công nghệ | Nhóm chủ đề |
| --- | --- |
| dbt | Model; source và dependency; materialization; incremental model; test; tài liệu; macro; môi trường và triển khai |
| Airflow | DAG; task; lịch chạy và data interval; dependency; retry; backfill; connection và secret; kiểm thử; triển khai và giám sát |

Airflow thuộc phạm vi Wiki đã thống nhất; dbt là ứng viên bổ sung. Việc lựa chọn công nghệ cho lộ trình Data Engineering thực chiến được quyết định riêng, không giới hạn phạm vi tra cứu của Wiki.

#### 4.4.6. HDFS, MinIO và công nghệ lưu trữ, truy vấn

HDFS và MinIO thuộc phạm vi Wiki cần phát triển, mỗi công nghệ có hub riêng như `hdfs/` và `minio/`. Dùng các nhóm chủ đề sau để thiết kế bài liền mạch theo quy mô tham khảo 4–6 bài, không tạo một trang cho mỗi thuật ngữ.

| Công nghệ | Nhóm chủ đề cần bao phủ |
| --- | --- |
| HDFS | Vai trò và phạm vi sử dụng; kiến trúc NameNode/DataNode; block và replication; luồng đọc/ghi; thực hành thao tác file; quyền truy cập; tích hợp với hệ thống xử lý; theo dõi dung lượng, lỗi và phục hồi |
| MinIO | Vai trò của object storage; bucket, object và API tương thích S3; môi trường thực hành; upload/download và SDK; quyền truy cập; tích hợp với engine xử lý; quản lý vòng đời dữ liệu; giám sát, bảo vệ dữ liệu và phục hồi |

Giải thích đặc điểm của từng hệ thống và liên kết đến khái niệm lưu trữ chung trong Data Engineering. Các lựa chọn mở rộng:
- Table Format: chọn nội dung chuyên sâu cho Iceberg, Delta Lake hoặc Hudi.
- Query Engine: chọn theo nhu cầu truy vấn và kiến trúc dự án.
- Data Warehouse chuyên dụng: chọn khi cần so sánh kiến trúc; bài thực hành của các lộ trình vẫn chạy trên máy người học.
- Công cụ CDC và tích hợp dữ liệu: chọn theo nguồn và đích thực tế.

Với mỗi công nghệ được chọn, nội dung gồm kiến trúc, ví dụ tối thiểu, thao tác đọc/ghi, tích hợp, bảo mật, hiệu năng và phục hồi. Các bài so sánh khái niệm và tiêu chí lựa chọn vẫn thuộc Data Engineering.

#### 4.4.7. Công nghệ nền tảng và vận hành — lựa chọn sau

- Công cụ Infrastructure as Code.
- Hệ thống CI/CD.
- Công nghệ triển khai và điều phối container.
- Công cụ quản lý secret.
- Công cụ thu thập log, metric và cảnh báo.
- Công cụ Data Catalog và Lineage.
- Công cụ kiểm tra Data Quality.
- Công cụ chạy tại máy cá nhân phục vụ compute, storage, networking và access control.

Chọn sản phẩm cụ thể theo yêu cầu của Data Platform Engineering, khả năng chạy trên máy người học và chi phí duy trì ví dụ. Các bài thực hành bắt buộc không phụ thuộc tài khoản cloud.

## 5. Initial gap backlog

Topics below describe coverage and writing actions, not a mandatory one-topic-per-file structure. Group related technology topics into coherent articles under section 4.4; split deeper references only when they answer independent questions. Titles and proposed slugs can be refined before writing. Existing destinations in section 9 take precedence over creating another page with equivalent content.

Priority means writing order, not importance: **P0** closes immediate foundation gaps; **P1** deepens practical system design; **P2** develops specialist and reference coverage. P2 work can proceed independently when expertise or reader demand justifies it.

| Priority | Canonical home | Proposed articles / actions | Needed before |
| --- | --- | --- | --- |
| P0 | Nền tảng / data-basics | Review/reuse legacy Data là gì and Các loại dữ liệu; add `records-schema-types` covering null, dates, precision, encoding | First SQL and ingestion examples |
| P0 | Nền tảng / SQL | Fill `overview`; add `select-filter-sort`, `aggregation`, `null-semantics`, `ddl-dml-constraints`; fill `join` | Quality queries, transformations, and modeling examples |
| P0 | Nền tảng / database | Fill `overview` and `oltp-vs-olap`; add `keys-and-constraints`; fill `transaction` and `acid` at introductory depth | Reliable reads/writes and basic warehouse reasoning |
| P0 | Nền tảng / Python | Add `overview`, `functions-and-modules`, `files-and-json`, `errors-and-logging`, `environments`, `database-and-http-clients` | A reproducible small ingestion job |
| P0 | Nền tảng / computing | Add `shell-and-files`, `git-basics`, `http-basics`, `configuration-and-secrets` | Setup, API access, safe configuration, versioned work |
| P0 | Nền tảng / modeling | Fill `overview`, `fact-and-dimension`, `star-schema`; add `grain-and-keys` | Correct joins and trustworthy measures |
| P0 | Data Engineering | Review seven introductory articles; add `incremental-extraction` and `pipeline-testing`; review idempotency/retry/backfill examples | Candidate readings for Nhập môn, subject to its scope |
| P0 | Công nghệ / Docker and beginner tools | Group Docker fundamentals and environment practice into coherent articles; provide setup, read/write examples and failure diagnosis for the chosen local database stack | Required examples that a beginner can actually run |
| P1 | Nền tảng | Fill CTE/window/optimization, indexes/isolation, SCD/snowflake; add normalization and NoSQL tradeoffs | Practical DE decisions and performance work |
| P1 | Data Engineering / architecture | Add `data-system-requirements`, `architecture-tradeoffs`, `serving-patterns` | Designing an end-to-end system for a business need |
| P1 | Data Engineering / ingestion and processing | Add `api-ingestion`, `source-reconciliation`, `incremental-transformation`, `distributed-processing` | Reliable ingestion, change handling, execution choices |
| P1 | Data Engineering / storage | Add `object-storage`, `data-layout-and-compaction`, `retention-and-deletion`; deepen file/table format coverage | Analytical storage design and lifecycle operations |
| P1 | Data Engineering / operations | Add `pipeline-deployment`, `data-slos`, `incident-response`, `disaster-recovery`; deepen quality/observability/contracts | Deployment, service ownership, recovery evidence |
| P1 | Data Engineering / governance | Add `data-access-control`, `sensitive-data-handling`, `data-ownership-and-audit` | Shared access and responsible operation |
| P1 | Công nghệ | Develop substantial introductory and practical article groups for Spark, Airflow, HDFS and MinIO; add transformation tools as needed. Wiki coverage is broader than any one path stack | Implementation of practical DE concepts |
| P2 | Nền tảng / distributed systems | Fill six existing articles; add `partial-failures`, `ordering-and-clocks`, `coordination-and-consensus` | Specialist streaming/platform explanations |
| P2 | Data Engineering / streaming | Add `event-time-and-windows`, `state-and-recovery`, `delivery-guarantees`, `replay-and-late-data`, `backpressure` | Canonical foundations for Kafka/Flink/Spark streaming articles |
| P2 | Data Engineering / platforms | Add `data-platform-capabilities`, `self-service-and-onboarding`, `multi-tenancy-and-isolation`, `provisioning-and-deployment`, `platform-cost-and-capacity` | Platform specialization and independent reference |
| P2 | Công nghệ | Develop coherent Kafka/Flink article groups; deepen Spark, Airflow, HDFS, MinIO and Docker with operations, security and troubleshooting references; add platform tools as needed | Advanced reference beyond any single curriculum |

Do not create all these files as placeholders now. Turn the next selected topic into an article brief with one reader question, concrete scope, prerequisites, example, and completion check.

## 6. Reference relationships

Prerequisites mean knowledge actually needed to understand the article. Related links mean useful adjacent reading. Neither should be used simply to encode a recommended reading order. For example, data quality does not inherently require orchestration, even though its current metadata lists it as a prerequisite.

Use these dependency chains to guide review, not as a new weekly curriculum:

| Destination | Knowledge to establish first | Follow-on reference |
| --- | --- | --- |
| JOIN and analytical metrics | Tables, keys, nulls, grain | Fact/dimension, quality checks, join strategies |
| Incremental extraction | SQL filters, time representation, ingestion | CDC, idempotency, backfill |
| Reliable writes | Keys, transactions, failure handling | Retry, reconciliation, recovery |
| Warehouse transformations | SQL, modeling, warehouse and ETL/ELT concepts | Incremental transformation, orchestration, testing |
| Kafka delivery semantics | Partitioning, ordering, delivery guarantees | Kafka offsets, producer behavior, transactions |
| Flink recovery | Event time, state, delivery guarantees | Checkpoint, savepoint, exactly-once boundaries |
| Spark performance | Partitioning, distributed processing, query plans | Shuffle, skew, Catalyst, join strategies |
| Platform access and tenancy | Processes, networks, permissions, security concepts | Chosen provisioning/deployment tools and isolation mechanisms |

Use full content paths in planning records to disambiguate repeated names such as `overview` and `replication`. The current site uses `contentType`, `level`, `topics`, `prerequisites`, and `related`; preserve that convention during future edits. A site-wide metadata resolver or schema change belongs in the editorial/website implementation plans.

A hub should provide a short subject map, suggested starting points, reference groupings, and honest availability. It should not duplicate its overview article. Link required readings only after the target and its prerequisites are available in the normal site build.

## 7. Review and delivery priorities

### First: make a coherent foundation available

1. Review the six orientation articles and optional Data Mesh article for boundaries and onward links, preserving the author's current edits.
2. Review the seven introductory Data Engineering articles: pipeline, ingestion, warehouse, ETL/ELT, batch, orchestration, quality. Identify assumed SQL/programming/modeling knowledge before marking them suitable for beginners.
3. Write the P0 SQL, database, modeling, programming, and computing material in dependency order. Reuse the two legacy data introductions after review.
4. Plan Nhập môn's project and select the minimal tool examples. Reconcile its required reading list against this backlog; a topic marked P0 is a candidate, not a commitment to include it in the path.
5. Release coherent groups with all required readings available. Continue broader coverage alongside path development.

### Next: turn introductions into dependable references

Review the remaining 16 Data Engineering articles against their claims. Short overview articles may remain short; advanced labels alone do not establish advanced coverage. Add separate deep dives only where they answer a distinct question.

Check examples for visible assumptions and failure cases. In particular, review SQL null behavior in quality checks, transaction boundaries in idempotent writes, and tool-specific architecture implied by generic table-format diagrams. These are review targets from a content inspection, not a completed technical audit.

Resolve discovery gaps during later website work: the Wiki root currently describes Data Engineering as forthcoming even though that hub and 23 articles have `draft: false`; foundation and technology hubs remain drafts. Review normal-build links and visibility before exposing newly completed groups.

### Then: grow specialist coverage

Develop streaming and platform prerequisites independently. Schedule reference topics not used by paths—such as NoSQL tradeoffs, advanced isolation, temporal modeling, and product troubleshooting—based on reader questions and maintenance capacity. Do not make completion of all 81 current files a release gate.

## 8. Coverage and completion rules

Track articles using these editorial states:

- **Placeholder:** file exists, but explanation/examples are missing.
- **Draft with content:** written, awaiting technical/editorial verification.
- **Reviewed:** scope, prerequisites, examples, terminology, and links checked.
- **Available:** reviewed article confirmed accessible in the normal site build.
- **Needs revision:** known gap, stale version, or failing example recorded.

Existing `draft: false` articles are recorded as content present, review pending; this plan does not retrospectively certify them. Future tracking should record canonical path, reader question, depth, prerequisites, status, priority, reviewed date, and tested tool version where relevant.

An article is ready when it answers its stated question, explains assumptions, provides a concrete example appropriate to its purpose, identifies limitations, and links to available prerequisites. Executable examples need documented environments and expected results. Technology articles also need version information and primary documentation references.

A subject has introductory coverage when a newcomer can understand its overview and complete its basic example using available prerequisites. It has practical coverage when the reader can make and test a relevant implementation decision, including a failure case. Reference depth requires troubleshooting, limits, and advanced decisions; it is tracked separately from introductory availability.

Before any later move of legacy content, choose the canonical destination, preserve the old URL or add a deliberate redirect, update internal links, and verify both routes. Keep current URLs until that migration is implemented and checked. Do not copy the same article into both trees.

Decisions deferred to other plans: weekly duration and assessments; final project stack; navigation implementation; detailed editorial templates; product-specific version support. The proposed category boundaries and coverage priorities here are ready for review without those decisions.

## 9. Existing article inventory

Paths below are relative to `content/wiki/`. **Content** means body text exists with `draft: false`, with technical review still pending. **Placeholder** means a draft containing TODO content. Hubs are excluded. Titles are taken from the current files; proposed work does not rename them.

### Bắt đầu

| Article | Current file | State |
| --- | --- | --- |
| Có AI rồi, còn cần học nền tảng không? | [`bat-dau/ai-va-kien-thuc-nen-tang.md`](../content/wiki/bat-dau/ai-va-kien-thuc-nen-tang.md) | Content |
| Data Engineer là gì? | [`bat-dau/data-engineer-la-gi.md`](../content/wiki/bat-dau/data-engineer-la-gi.md) | Content |
| Data Engineer trong Data Mesh | [`bat-dau/data-engineer-trong-data-mesh.md`](../content/wiki/bat-dau/data-engineer-trong-data-mesh.md) | Content |
| Data Engineer xây những hệ thống gì? | [`bat-dau/data-engineer-xay-he-thong-gi.md`](../content/wiki/bat-dau/data-engineer-xay-he-thong-gi.md) | Content |
| Một data team làm việc với nhau như thế nào? | [`bat-dau/data-team-lam-viec-voi-nhau.md`](../content/wiki/bat-dau/data-team-lam-viec-voi-nhau.md) | Content |
| Data đi qua một hệ thống như thế nào? | [`bat-dau/du-lieu-di-qua-he-thong-nhu-the-nao.md`](../content/wiki/bat-dau/du-lieu-di-qua-he-thong-nhu-the-nao.md) | Content |
| Học Data Engineering từ đâu? | [`bat-dau/hoc-data-engineering-tu-dau.md`](../content/wiki/bat-dau/hoc-data-engineering-tu-dau.md) | Content |

### Nền tảng

| Article | Current file | State |
| --- | --- | --- |
| Bảng Fact và Dimension | [`nen-tang/data-modeling/fact-and-dimension.md`](../content/wiki/nen-tang/data-modeling/fact-and-dimension.md) | Placeholder |
| Mô hình hóa dữ liệu là gì? | [`nen-tang/data-modeling/overview.md`](../content/wiki/nen-tang/data-modeling/overview.md) | Placeholder |
| Dimension thay đổi chậm (SCD) | [`nen-tang/data-modeling/slowly-changing-dimension.md`](../content/wiki/nen-tang/data-modeling/slowly-changing-dimension.md) | Placeholder |
| Mô hình bông tuyết | [`nen-tang/data-modeling/snowflake-schema.md`](../content/wiki/nen-tang/data-modeling/snowflake-schema.md) | Placeholder |
| Mô hình ngôi sao | [`nen-tang/data-modeling/star-schema.md`](../content/wiki/nen-tang/data-modeling/star-schema.md) | Placeholder |
| Các thuộc tính ACID | [`nen-tang/database/acid.md`](../content/wiki/nen-tang/database/acid.md) | Placeholder |
| Chỉ mục trong cơ sở dữ liệu | [`nen-tang/database/database-index.md`](../content/wiki/nen-tang/database/database-index.md) | Placeholder |
| Các mức cô lập giao dịch | [`nen-tang/database/isolation-level.md`](../content/wiki/nen-tang/database/isolation-level.md) | Placeholder |
| OLTP và OLAP | [`nen-tang/database/oltp-vs-olap.md`](../content/wiki/nen-tang/database/oltp-vs-olap.md) | Placeholder |
| Cơ sở dữ liệu là gì? | [`nen-tang/database/overview.md`](../content/wiki/nen-tang/database/overview.md) | Placeholder |
| Giao dịch trong cơ sở dữ liệu | [`nen-tang/database/transaction.md`](../content/wiki/nen-tang/database/transaction.md) | Placeholder |
| Định lý CAP | [`nen-tang/distributed-systems/cap-theorem.md`](../content/wiki/nen-tang/distributed-systems/cap-theorem.md) | Placeholder |
| Tính nhất quán dữ liệu | [`nen-tang/distributed-systems/consistency.md`](../content/wiki/nen-tang/distributed-systems/consistency.md) | Placeholder |
| Khả năng chịu lỗi | [`nen-tang/distributed-systems/fault-tolerance.md`](../content/wiki/nen-tang/distributed-systems/fault-tolerance.md) | Placeholder |
| Hệ thống phân tán là gì? | [`nen-tang/distributed-systems/overview.md`](../content/wiki/nen-tang/distributed-systems/overview.md) | Placeholder |
| Phân vùng dữ liệu | [`nen-tang/distributed-systems/partitioning.md`](../content/wiki/nen-tang/distributed-systems/partitioning.md) | Placeholder |
| Sao chép dữ liệu | [`nen-tang/distributed-systems/replication.md`](../content/wiki/nen-tang/distributed-systems/replication.md) | Placeholder |
| Biểu thức bảng chung (CTE) | [`nen-tang/sql/cte.md`](../content/wiki/nen-tang/sql/cte.md) | Placeholder |
| Kết hợp dữ liệu với JOIN | [`nen-tang/sql/join.md`](../content/wiki/nen-tang/sql/join.md) | Placeholder |
| SQL là gì? | [`nen-tang/sql/overview.md`](../content/wiki/nen-tang/sql/overview.md) | Placeholder |
| Tối ưu truy vấn SQL | [`nen-tang/sql/query-optimization.md`](../content/wiki/nen-tang/sql/query-optimization.md) | Placeholder |
| Hàm cửa sổ trong SQL | [`nen-tang/sql/window-function.md`](../content/wiki/nen-tang/sql/window-function.md) | Placeholder |

### Data Engineering

| Article | Current file | State |
| --- | --- | --- |
| Sửa lại data trong quá khứ với Backfill | [`data-engineering/backfill.md`](../content/wiki/data-engineering/backfill.md) | Content |
| Xử lý data theo từng Batch | [`data-engineering/batch-processing.md`](../content/wiki/data-engineering/batch-processing.md) | Content |
| Batch hay Streaming? | [`data-engineering/batch-vs-streaming.md`](../content/wiki/data-engineering/batch-vs-streaming.md) | Content |
| Theo dõi thay đổi trong Database với CDC | [`data-engineering/change-data-capture.md`](../content/wiki/data-engineering/change-data-capture.md) | Content |
| Tìm đúng data với Data Catalog | [`data-engineering/data-catalog.md`](../content/wiki/data-engineering/data-catalog.md) | Content |
| Data Contract giữa producer và consumer | [`data-engineering/data-contract.md`](../content/wiki/data-engineering/data-contract.md) | Content |
| Data Ingestion: đưa data ra khỏi Source System | [`data-engineering/data-ingestion.md`](../content/wiki/data-engineering/data-ingestion.md) | Content |
| Lưu raw data ở quy mô lớn với Data Lake | [`data-engineering/data-lake.md`](../content/wiki/data-engineering/data-lake.md) | Content |
| Data Lineage: data đã đi qua đâu? | [`data-engineering/data-lineage.md`](../content/wiki/data-engineering/data-lineage.md) | Content |
| Data Observability: theo dõi sức khoẻ của pipeline | [`data-engineering/data-observability.md`](../content/wiki/data-engineering/data-observability.md) | Content |
| Một Data Pipeline hoạt động ra sao? | [`data-engineering/data-pipeline.md`](../content/wiki/data-engineering/data-pipeline.md) | Content |
| Data Quality: làm sao biết data đủ tin cậy? | [`data-engineering/data-quality.md`](../content/wiki/data-engineering/data-quality.md) | Content |
| Vì sao cần Data Warehouse? | [`data-engineering/data-warehouse.md`](../content/wiki/data-engineering/data-warehouse.md) | Content |
| ETL và ELT khác nhau thế nào? | [`data-engineering/etl-elt.md`](../content/wiki/data-engineering/etl-elt.md) | Content |
| File Format: chọn giữa CSV, JSON và Parquet | [`data-engineering/file-formats.md`](../content/wiki/data-engineering/file-formats.md) | Content |
| Idempotency: chạy lại pipeline mà không tạo duplicate | [`data-engineering/idempotency.md`](../content/wiki/data-engineering/idempotency.md) | Content |
| Khi Data Lake cần cách quản lý như Warehouse | [`data-engineering/lakehouse.md`](../content/wiki/data-engineering/lakehouse.md) | Content |
| Metadata: data để hiểu data | [`data-engineering/metadata.md`](../content/wiki/data-engineering/metadata.md) | Content |
| Data Orchestration khi nhiều job phụ thuộc nhau | [`data-engineering/orchestration.md`](../content/wiki/data-engineering/orchestration.md) | Content |
| Retry hoạt động như thế nào? | [`data-engineering/retry.md`](../content/wiki/data-engineering/retry.md) | Content |
| Schema Evolution mà không làm hỏng downstream | [`data-engineering/schema-evolution.md`](../content/wiki/data-engineering/schema-evolution.md) | Content |
| Stream Processing: xử lý data liên tục | [`data-engineering/stream-processing.md`](../content/wiki/data-engineering/stream-processing.md) | Content |
| Table Format: chọn giữa Iceberg, Delta Lake và Hudi | [`data-engineering/table-formats.md`](../content/wiki/data-engineering/table-formats.md) | Content |

### Công nghệ

| Article | Current file | State |
| --- | --- | --- |
| Kiến trúc Flink | [`technologies/flink/architecture.md`](../content/wiki/technologies/flink/architecture.md) | Placeholder |
| Áp lực ngược trong Flink | [`technologies/flink/backpressure.md`](../content/wiki/technologies/flink/backpressure.md) | Placeholder |
| Checkpoint trong Flink | [`technologies/flink/checkpoint.md`](../content/wiki/technologies/flink/checkpoint.md) | Placeholder |
| Thời gian sự kiện trong Flink | [`technologies/flink/event-time.md`](../content/wiki/technologies/flink/event-time.md) | Placeholder |
| Xử lý đúng một lần trong Flink | [`technologies/flink/exactly-once.md`](../content/wiki/technologies/flink/exactly-once.md) | Placeholder |
| Job, Operator, Task và Subtask | [`technologies/flink/job-operator-task-subtask.md`](../content/wiki/technologies/flink/job-operator-task-subtask.md) | Placeholder |
| Flink là gì? | [`technologies/flink/overview.md`](../content/wiki/technologies/flink/overview.md) | Placeholder |
| Mức độ song song trong Flink | [`technologies/flink/parallelism.md`](../content/wiki/technologies/flink/parallelism.md) | Placeholder |
| Savepoint trong Flink | [`technologies/flink/savepoint.md`](../content/wiki/technologies/flink/savepoint.md) | Placeholder |
| Trạng thái trong Flink | [`technologies/flink/state.md`](../content/wiki/technologies/flink/state.md) | Placeholder |
| Watermark trong Flink | [`technologies/flink/watermark.md`](../content/wiki/technologies/flink/watermark.md) | Placeholder |
| Kafka Consumer Group | [`technologies/kafka/consumer-group.md`](../content/wiki/technologies/kafka/consumer-group.md) | Placeholder |
| Ngữ nghĩa chuyển giao trong Kafka | [`technologies/kafka/delivery-semantics.md`](../content/wiki/technologies/kafka/delivery-semantics.md) | Placeholder |
| Offset trong Kafka | [`technologies/kafka/offset.md`](../content/wiki/technologies/kafka/offset.md) | Placeholder |
| Kafka là gì? | [`technologies/kafka/overview.md`](../content/wiki/technologies/kafka/overview.md) | Placeholder |
| Kafka Producer | [`technologies/kafka/producer.md`](../content/wiki/technologies/kafka/producer.md) | Placeholder |
| Tái cân bằng trong Kafka | [`technologies/kafka/rebalancing.md`](../content/wiki/technologies/kafka/rebalancing.md) | Placeholder |
| Sao chép dữ liệu trong Kafka | [`technologies/kafka/replication.md`](../content/wiki/technologies/kafka/replication.md) | Placeholder |
| Topic và Partition trong Kafka | [`technologies/kafka/topic-partition.md`](../content/wiki/technologies/kafka/topic-partition.md) | Placeholder |
| Giao dịch trong Kafka | [`technologies/kafka/transactions.md`](../content/wiki/technologies/kafka/transactions.md) | Placeholder |
| Kiến trúc Spark | [`technologies/spark/architecture.md`](../content/wiki/technologies/spark/architecture.md) | Placeholder |
| Bộ tối ưu Catalyst | [`technologies/spark/catalyst.md`](../content/wiki/technologies/spark/catalyst.md) | Placeholder |
| DataFrame trong Spark | [`technologies/spark/dataframe.md`](../content/wiki/technologies/spark/dataframe.md) | Placeholder |
| Các chiến lược JOIN trong Spark | [`technologies/spark/join-strategies.md`](../content/wiki/technologies/spark/join-strategies.md) | Placeholder |
| Spark là gì? | [`technologies/spark/overview.md`](../content/wiki/technologies/spark/overview.md) | Placeholder |
| Phân vùng trong Spark | [`technologies/spark/partition.md`](../content/wiki/technologies/spark/partition.md) | Placeholder |
| RDD trong Spark | [`technologies/spark/rdd.md`](../content/wiki/technologies/spark/rdd.md) | Placeholder |
| Shuffle trong Spark | [`technologies/spark/shuffle.md`](../content/wiki/technologies/spark/shuffle.md) | Placeholder |
| Structured Streaming trong Spark | [`technologies/spark/structured-streaming.md`](../content/wiki/technologies/spark/structured-streaming.md) | Placeholder |
