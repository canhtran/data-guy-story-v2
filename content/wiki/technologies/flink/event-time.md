---
title: "Event time trong Flink: doanh thu thuộc phút nào?"
description: "Tách thời gian xảy ra và thời gian nhận, quy định timezone và cửa sổ."
draft: false
contentType: "concept"
weight: 8
level: "beginner"
topics: ["flink"]
prerequisites: []
related: []
---

Đơn thanh toán lúc 10:04:50 nhưng mạng chậm, đến engine lúc 10:06:10. Báo cáo theo thời điểm thanh toán phải đưa đơn vào khoảng 10:00–10:05, không phải khoảng 10:05–10:10.

## Hai chiếc đồng hồ

**Event time** là thời điểm sự kiện xảy ra do dữ liệu cung cấp. **Processing time** là thời gian engine xử lý. Event time hữu ích khi cần kết quả theo nghiệp vụ dù arrival order thay đổi; processing time thuận tiện cho hành vi theo đồng hồ hệ thống nhưng kết quả có thể khác khi replay.

Trong ví dụ này, timestamp có offset `+07:00`; ngày nghiệp vụ theo Asia/Ho_Chi_Minh. Khoảng năm phút dùng biên trái đóng, biên phải mở: `[10:00,10:05)`. Một đơn đúng 10:05:00 thuộc cửa sổ sau.

## Bài tập cửa sổ

| Event | Event time (+07:00) | Arrival time (+07:00) | Amount đồng |
| --- | --- | --- | ---: |
| E1 | 10:04:50 | 10:06:10 | 40000 |
| E2 | 10:05:00 | 10:05:02 | 35000 |

Nếu cả hai còn được chính sách late-data chấp nhận, cửa sổ đầu có 40000, cửa sổ sau có 35000. Arrival order E2 rồi E1 không đổi việc phân cửa sổ theo event time. Tổng output thực tế còn phụ thuộc watermark và thời điểm state bị dọn.

## Timestamp cần là hợp đồng

Epoch seconds và epoch milliseconds không thể đổi chỗ. Timestamp không có timezone có thể mơ hồ. Chọn rõ nguồn thời gian: thời điểm thanh toán, thời điểm ứng dụng phát event hay thời điểm broker ghi nhận. Chúng trả lời các câu hỏi khác nhau.

Đối với Flink SQL, phân biệt kiểu timestamp và timestamp với múi giờ local, cùng session timezone. Với DataStream, cần timestamp assignment và watermark strategy. Chỉ có một cột tên `event_time` không tự bật xử lý event time.

Nếu output nằm sai ngày, kiểm tra đơn vị timestamp, offset và business timezone trước. Nếu cửa sổ chưa emit, đọc [watermark]({{< relref "/wiki/technologies/flink/watermark.md" >}}); đồng hồ thật trôi qua không tự làm mọi event-time window kết thúc.

Bài tập được tính tay theo cơ chế Flink 1.20.3, chưa chạy window job với connector thật.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — time](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/time/) là nguồn đối chiếu cơ chế trong bài.
