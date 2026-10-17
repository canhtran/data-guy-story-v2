---
title: "Delivery semantics: nhận một lần hay tạo kết quả một lần?"
description: "So sánh cửa sổ lỗi giữa đọc, ghi output và commit tiến độ."
draft: false
contentType: "concept"
weight: 8
level: "beginner"
topics: ["kafka"]
prerequisites: ["/wiki/technologies/kafka/overview"]
related: []
---

Một record chỉ có một offset trong Kafka nhưng database có hai dòng cho cùng sự kiện. Điều này có thể xảy ra khi consumer ghi xong rồi chết trước commit offset. “Kafka lưu một record” và “hệ thống ngoài tạo một kết quả” là hai bảo đảm khác nhau.

## Đặt lỗi vào giữa hai bước

Giả sử record E1 cần ghi vào database. Các trình tự dưới đây là ví dụ suy luận, chưa phải crash test:

| Cách làm | Crash giữa hai bước | Hệ quả |
| --- | --- | --- |
| Commit offset rồi ghi DB | Commit xong, DB chưa ghi | Có thể mất output: at-most-once |
| Ghi DB rồi commit offset | DB xong, offset chưa commit | Có thể ghi lại: at-least-once |
| Ghi DB idempotent rồi commit | Replay E1 dùng lại key | Có thể giữ một kết quả nghiệp vụ |

At-most-once chấp nhận khả năng bỏ công việc. At-least-once chấp nhận lặp xử lý để giảm khả năng mất. Exactly-once phải xác định phạm vi: state của engine, Kafka output hay cả hệ thống ngoài?

## Idempotency cần key và transaction đúng

Nếu DB có uniqueness theo `event_id`, hai lần nhận E1 có thể đưa về cùng row. Nhưng nếu output là phép tăng `revenue = revenue + amount`, dùng upsert không tự loại lặp phép tăng. Có thể cần ledger sự kiện và cập nhật tổng trong cùng transaction.

Hai sự kiện thanh toán khác nhau cho cùng đơn không nhất thiết là duplicate. Chọn `order_id` làm key deduplicate có thể làm mất một payment hợp lệ. Định nghĩa identity và grain trước khi thiết kế retry.

## Kafka transactions có phạm vi cụ thể

Trong pipeline đọc Kafka → xử lý → ghi Kafka, transaction có thể gắn output và offset input vào cùng commit; consumer phía sau cần đọc `read_committed`. Nó không tự đưa một transaction PostgreSQL hay HTTP request vào transaction Kafka.

Producer idempotence chỉ xử lý một lớp duplicate do retry gửi, không deduplicate toàn bộ sự kiện nghiệp vụ. Checkpoint hoặc auto commit cũng không thay thế cam kết ở sink.

Trước khi dùng từ exactly-once, ghi rõ: nguồn replay được bao lâu, identity là gì, ai commit output, output lặp được xử lý thế nào và điều gì xảy ra nếu crash ngay trước/sau commit. Đọc [transactions]({{< relref "/wiki/technologies/kafka/transactions.md" >}}) cho trường hợp Kafka-to-Kafka.

## Tài liệu gốc

[Kafka design: delivery semantics](https://kafka.apache.org/40/design/design/#message-delivery-semantics) giải thích các ranh giới bảo đảm; [KafkaProducer API](https://kafka.apache.org/40/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html) mô tả transaction. Đối chiếu ngày 1/10/2026.
