---
title: "Apache Kafka"
description: "Tài liệu tham khảo về Apache Kafka dành cho Data Engineer."
draft: false
contentType: "hub"
weight: 7
---

Kafka lưu luồng sự kiện để các hệ thống đọc theo tiến độ riêng. Bắt đầu từ topic và partition, rồi theo dõi producer, consumer và ranh giới commit. Các bài đối chiếu Kafka 4.0; bài thực hành dùng 4.0.2. Kịch bản lỗi nhiều broker và transaction là mô hình giải thích, chưa được fault-test.

## Bắt đầu

- [Kafka là gì?]({{< relref "/wiki/technologies/kafka/overview.md" >}})

## Khái niệm chính

- [Topic và Partition trong Kafka]({{< relref "/wiki/technologies/kafka/topic-partition.md" >}})
- [Kafka Producer]({{< relref "/wiki/technologies/kafka/producer.md" >}})
- [Kafka Consumer Group]({{< relref "/wiki/technologies/kafka/consumer-group.md" >}})
- [Offset trong Kafka]({{< relref "/wiki/technologies/kafka/offset.md" >}})

## Cơ chế và độ tin cậy

- [Sao chép dữ liệu trong Kafka]({{< relref "/wiki/technologies/kafka/replication.md" >}})
- [Tái cân bằng trong Kafka]({{< relref "/wiki/technologies/kafka/rebalancing.md" >}})
- [Ngữ nghĩa chuyển giao trong Kafka]({{< relref "/wiki/technologies/kafka/delivery-semantics.md" >}})
- [Giao dịch trong Kafka]({{< relref "/wiki/technologies/kafka/transactions.md" >}})

## Lộ trình liên quan

- [Streaming Engineering — lộ trình đang lên kế hoạch]({{< relref "/learning-paths/streaming-engineering/_index.md" >}})
