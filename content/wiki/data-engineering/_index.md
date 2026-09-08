---
title: "Data Engineering"
description: "Các khái niệm cốt lõi để xây, vận hành và lựa chọn kiến trúc cho một hệ thống data."
draft: false
contentType: "hub"
weight: 3
aliases:
  - /data-engineering/
---

Phần này đi sâu vào những khái niệm xuất hiện trong công việc Data Engineering. Bạn không cần đọc hết một lượt. Hãy chọn điểm bắt đầu gần với việc mình đang làm nhất.

## Mới tìm hiểu Data Engineering

Bảy bài đầu theo một Data Pipeline từ lúc lấy data về đến khi output đủ tin cậy để sử dụng.

1. [Data Pipeline là gì?]({{< relref "/wiki/data-engineering/data-pipeline.md" >}})
2. [Data Ingestion là gì?]({{< relref "/wiki/data-engineering/data-ingestion.md" >}})
3. [Data Warehouse là gì?]({{< relref "/wiki/data-engineering/data-warehouse.md" >}})
4. [ETL và ELT khác nhau thế nào?]({{< relref "/wiki/data-engineering/etl-elt.md" >}})
5. [Batch Processing là gì?]({{< relref "/wiki/data-engineering/batch-processing.md" >}})
6. [Data Orchestration là gì?]({{< relref "/wiki/data-engineering/orchestration.md" >}})
7. [Data Quality là gì?]({{< relref "/wiki/data-engineering/data-quality.md" >}})

Nếu vẫn chưa rõ Data Engineer làm gì, hãy đọc phần [Bắt đầu]({{< relref "/wiki/bat-dau/" >}}) trước.

## Đã bắt đầu xây Data Pipeline

Nhóm bài này tập trung vào những vấn đề chỉ xuất hiện rõ khi pipeline được chạy nhiều lần và có người phụ thuộc vào nó.

8. [Idempotency là gì?]({{< relref "/wiki/data-engineering/idempotency.md" >}})
9. [Retry hoạt động như thế nào?]({{< relref "/wiki/data-engineering/retry.md" >}})
10. [Backfill là gì?]({{< relref "/wiki/data-engineering/backfill.md" >}})
11. [Data Observability là gì?]({{< relref "/wiki/data-engineering/data-observability.md" >}})
12. [Metadata là gì?]({{< relref "/wiki/data-engineering/metadata.md" >}})
13. [Data Lineage là gì?]({{< relref "/wiki/data-engineering/data-lineage.md" >}})
14. [Data Catalog là gì?]({{< relref "/wiki/data-engineering/data-catalog.md" >}})
15. [Data Contract là gì?]({{< relref "/wiki/data-engineering/data-contract.md" >}})
16. [Schema Evolution là gì?]({{< relref "/wiki/data-engineering/schema-evolution.md" >}})

## Đang làm việc với hệ thống lớn hơn

Bắt đầu từ việc chọn Batch hay Streaming, sau đó mới đi vào cách lưu và quản lý data trên Data Lake.

17. [Batch và Streaming khác nhau thế nào?]({{< relref "/wiki/data-engineering/batch-vs-streaming.md" >}})
18. [Stream Processing là gì?]({{< relref "/wiki/data-engineering/stream-processing.md" >}})
19. [Change Data Capture — CDC là gì?]({{< relref "/wiki/data-engineering/change-data-capture.md" >}})
20. [Data Lake là gì?]({{< relref "/wiki/data-engineering/data-lake.md" >}})
21. [Lakehouse là gì?]({{< relref "/wiki/data-engineering/lakehouse.md" >}})
22. [File Format: CSV, JSON và Parquet]({{< relref "/wiki/data-engineering/file-formats.md" >}})
23. [Table Format: Iceberg, Delta Lake và Hudi]({{< relref "/wiki/data-engineering/table-formats.md" >}})

Các nhóm trên chỉ là gợi ý đọc. Sidebar vẫn giữ một danh sách phẳng để mỗi khái niệm có một trang riêng và dễ tra cứu lại.
