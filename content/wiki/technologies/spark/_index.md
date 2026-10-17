---
title: "Apache Spark"
description: "Tài liệu tham khảo về Apache Spark dành cho Data Engineer."
draft: false
contentType: "hub"
weight: 9
---

Spark giúp chia công việc xử lý dữ liệu thành nhiều task. Bắt đầu bằng ví dụ PySpark cục bộ, rồi đọc cách thực thi và những điểm cần kiểm tra khi job chậm. Bộ ví dụ dùng Spark 3.5.6, Python 3.12 và JDK 17; đã kiểm tra trên macOS Intel. Ví dụ local không chứng minh hiệu năng hoặc khả năng chịu lỗi của cluster.

## Bắt đầu

- [Spark là gì?]({{< relref "/wiki/technologies/spark/overview.md" >}})

## Khái niệm chính

- [Kiến trúc Spark]({{< relref "/wiki/technologies/spark/architecture.md" >}})
- [RDD trong Spark]({{< relref "/wiki/technologies/spark/rdd.md" >}})
- [DataFrame trong Spark]({{< relref "/wiki/technologies/spark/dataframe.md" >}})
- [Phân vùng trong Spark]({{< relref "/wiki/technologies/spark/partition.md" >}})

## Thực thi và tối ưu

- [Shuffle trong Spark]({{< relref "/wiki/technologies/spark/shuffle.md" >}})
- [Bộ tối ưu Catalyst]({{< relref "/wiki/technologies/spark/catalyst.md" >}})
- [Các chiến lược JOIN trong Spark]({{< relref "/wiki/technologies/spark/join-strategies.md" >}})

## Xử lý luồng

- [Structured Streaming trong Spark]({{< relref "/wiki/technologies/spark/structured-streaming.md" >}})

## Lộ trình liên quan

- [Spark & Lakehouse — lộ trình đang lên kế hoạch]({{< relref "/learning-paths/spark-lakehouse/_index.md" >}})
