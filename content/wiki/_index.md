---
title: "Wiki"
description: "Kiến thức và tài liệu tra cứu dành cho Data Engineer."
draft: false
contentType: "hub"
weight: 1
sidebar:
  hide: true
cascade:
  type: docs
---

Chào bạn,

Đây là chỗ mình ghi lại những thứ đã học được trong quá trình làm Data Engineer. Có thứ rất căn bản như SQL, database. Có thứ đi làm vài năm rồi mình vẫn phải mở tài liệu ra đọc lại, như checkpoint, transaction hay mấy kiểu join của Spark.

Mình gom chúng vào đây, viết lại bằng tiếng Việt và cố gắng giải thích theo cách mà ngày trước mình cũng muốn được nghe. Chỗ nào cần giữ tiếng Anh thì mình vẫn giữ, vì trước sau gì đi làm cũng gặp.

{{< wiki-categories >}}

## Bạn đang ở đâu?

### Mới tìm hiểu Data Engineering

Nếu chưa rõ Data Engineer làm gì, cần học những gì, hoặc đang đứng giữa một rừng roadmap trên mạng mà không biết tin cái nào, bắt đầu ở đây.

→ [Bắt đầu với Data Engineering]({{< relref "/wiki/bat-dau/_index.md" >}})

### Các phần tiếp theo

Dưới đây là các phần bạn có thể đọc tiếp. Mình vẫn bổ sung bài mới; những chủ đề chưa có bài được ghi rõ để bạn dễ phân biệt.

#### Nền tảng

Những kiến thức giúp mình hiểu và kiểm chứng việc các công cụ đang làm.

- **Dữ liệu cơ bản — đang biên soạn:** bản ghi, schema, kiểu dữ liệu, giá trị thiếu, thời gian và múi giờ.
- **SQL:** lọc, tổng hợp, JOIN, CTE, window functions và kế hoạch thực thi.
- **Python:** [script đầu tiên, đọc CSV/JSON và logging]({{< relref "/wiki/nen-tang/python/_index.md" >}}). Phần kết nối database/API đang được bổ sung.
- **Cơ sở dữ liệu:** khóa, ràng buộc, transaction, isolation và index.
- **Mô hình hóa dữ liệu:** grain, fact, dimension, star schema và lịch sử thay đổi.
- **Hệ thống phân tán:** partitioning, replication, consistency và phục hồi khi có lỗi.
- **Môi trường làm việc và AI — đang biên soạn:** terminal, Git, cài đặt công cụ, hỏi để debug và kiểm chứng code AI gợi ý.

→ [Đọc các bài nền tảng]({{< relref "/wiki/nen-tang/_index.md" >}})

#### Data Engineering — Đã có các bài khái niệm

Cách thiết kế, xây và vận hành hệ thống đưa dữ liệu đến nơi có thể sử dụng.

- **Thu thập và tích hợp:** ingestion, batch, CDC, ETL/ELT và data contract.
- **Lưu trữ và xử lý:** warehouse, lake, lakehouse, file format và table format.
- **Độ tin cậy:** data quality, idempotency, retry, schema evolution và backfill.
- **Vận hành:** orchestration, observability, độ mới dữ liệu và phục hồi pipeline.
- **Hiểu dữ liệu trong hệ thống:** metadata, catalog và lineage.
- **Nội dung mở rộng đang biên soạn:** kiến trúc, streaming, bảo mật, kiểm thử và nền tảng tự phục vụ cho nhiều team.

→ [Đọc các khái niệm Data Engineering]({{< relref "/wiki/data-engineering/_index.md" >}})

#### Công nghệ — Đã có bài Spark và Flink

Đi từ cơ chế của công cụ đến cách đọc kế hoạch, kiểm tra kết quả và chẩn đoán lỗi.

- **Spark:** 9 bài và ví dụ PySpark cục bộ đã kiểm tra, từ DataFrame đến shuffle, JOIN và Structured Streaming.
- **Flink:** 11 bài khái niệm với ví dụ kiểm tra bằng tay về state, thời gian và phục hồi; lab local đang biên soạn.
- **Kafka:** 9 bài đã viết, đang kiểm tra hướng dẫn local trước khi mở liên kết.
- **DuckDB:** 4 bài và ví dụ SQL/Python đã kiểm tra về truy vấn file, transaction và xử lý lỗi.
- **Đang biên soạn:** Docker, PostgreSQL, Airflow, dbt, HDFS, MinIO, Iceberg và các công cụ vận hành.

→ [Đọc các bài công nghệ]({{< relref "/wiki/technologies/_index.md" >}})


## Chuyện cái Sổ tay này

Khoảng 5 năm trước, trong một video trên kênh YouTube cũ, mình từng nói:

> *“Mình sẽ làm một cái sổ tay về Data, ghi lại tất cả những gì mình học được, để ai muốn vào nghề có cái mà đọc.”*

Nói xong rồi để đó tận mấy năm. Công việc, dự án, pipeline lỗi, đủ thứ chen vào. Bây giờ mình làm lại, chậm thôi nhưng làm cho tới.

Sổ tay chắc chắn còn thiếu và cũng có thể có chỗ sai. Nếu bạn bắt gặp, cứ góp ý thẳng. Có người chịu đọc và chỉ ra chỗ chưa ổn là điều đáng quý rồi.

— Cảnh
