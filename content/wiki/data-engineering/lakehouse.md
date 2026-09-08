---
title: "Khi Data Lake cần cách quản lý như Warehouse"
description: "Hiểu vì sao table format và compute engine được kết hợp để chạy workload kiểu warehouse trên Data Lake."
draft: false
contentType: "concept"
weight: 21
level: "advanced"
topics: ["data-engineering"]
prerequisites: ["data-lake"]
related: ["table-formats", "data-warehouse"]
---

Data Lake lưu Parquet rẻ và linh hoạt, nhưng nhiều job cùng sửa file dễ làm người đọc thấy trạng thái dở dang. Team cũng cần Update, Delete, schema evolution và lịch sử snapshot.

**Lakehouse** là cách xây khả năng quản lý table kiểu Data Warehouse trên storage của Data Lake, thường bằng object storage, table format và một hay nhiều compute engine.

```mermaid
flowchart TD
 A["Object Storage<br/>Parquet files"] --> B["Table Format<br/>Metadata và snapshots"]
 B --> C["Compute Engine"]
 C --> D["SQL, BI, ML"]
```

## Table không chỉ là một thư mục file

Table format theo dõi file nào thuộc snapshot hiện tại. Writer tạo file mới rồi commit metadata; reader thấy snapshot trước hoặc sau commit, không thấy nửa chừng.

| Khả năng | Thư mục Parquet | Table được quản lý |
| --- | --- | --- |
| Atomic commit | Khó | Có cơ chế commit |
| Update/Delete | Tự viết lại và theo dõi | Được table format hỗ trợ |
| Time travel | Không có sẵn | Đọc snapshot cũ |
| Schema evolution | Dễ không nhất quán | Có rule và metadata |

Lakehouse không phải một sản phẩm duy nhất. Iceberg, Delta Lake và Hudi là table format với thiết kế khác nhau; Spark, Flink hoặc query engine là compute.

## Khi nào cần?

Lakehouse hữu ích khi data lớn nằm trên object storage, nhiều workload cần dùng chung table và team cần transaction hoặc snapshot. Nếu warehouse hiện tại đáp ứng chi phí, performance và governance, chuyển kiến trúc chỉ để có tên mới hiếm khi tạo giá trị.

Sự linh hoạt cũng mang thêm việc vận hành: compact small files, dọn snapshot cũ, chọn partition, kiểm soát catalog và compatibility giữa engine. Hãy đánh giá những trách nhiệm này cùng lợi ích storage mở.
