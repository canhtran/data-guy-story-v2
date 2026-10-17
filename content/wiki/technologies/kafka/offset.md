---
title: "Offset: consumer đã đọc đến đâu, đã xử lý đến đâu?"
description: "Phân biệt vị trí đọc, committed offset và ranh giới ghi output."
draft: false
contentType: "concept"
weight: 5
level: "beginner"
topics: ["kafka"]
prerequisites: ["/wiki/technologies/kafka/overview"]
related: []
---

Consumer đã đọc record offset 42 nhưng chưa ghi xong vào database. Nếu commit luôn 43 rồi process chết, lần khởi động sau có thể bỏ qua record 42. Offset không phải biên nhận “database đã đúng”; ứng dụng phải chọn thời điểm commit phù hợp.

## Ba vị trí cần tách

Offset là vị trí record trong partition. Consumer position là vị trí lần đọc tiếp theo của consumer đang chạy. **Committed offset** là vị trí group dùng khi phục hồi; thông thường commit vị trí record tiếp theo, không phải offset record cuối đã xử lý.

Ví dụ kiểm tra bằng tay, một partition có record 40, 41, 42. Đã ghi bền vững record 40 và 41; record 42 còn đang xử lý. Vị trí an toàn để commit là 42. Nếu commit 43, bạn đang nói rằng lần sau không cần đọc lại 42.

## Ghi xong rồi commit vẫn có cửa sổ duplicate

Trình tự: đọc 42 → database commit → process chết trước Kafka commit. Consumer mới đọc lại 42. Đây là hành vi at-least-once thường gặp. Dùng `event_id` duy nhất và upsert/transaction ở sink để lần xử lý lại không thêm kết quả ngoài ý muốn.

Nếu xử lý bất đồng bộ, record 43 xong trước 42 không có nghĩa được commit 44. Cần theo dõi dải offset đã xử lý liên tục theo từng partition. Nếu bỏ qua “lỗ hổng” 42, restart sẽ mất công việc đó.

## Reset và retention

`auto.offset.reset` có tác dụng khi không có committed offset hợp lệ hoặc vị trí không còn trong log; nó không ép consumer luôn đọc từ đầu. Retention có thể xóa dữ liệu consumer chưa đọc. Chính sách reset về latest trong trường hợp đó có thể bỏ lịch sử; earliest chỉ bắt đầu ở dữ liệu còn giữ được.

Trong ví dụ đã xử lý 40–41, log end offset là 50 và commit là 42: lag minh họa là 8 vị trí. Không suy ra chính xác tám sự kiện nghiệp vụ chưa hoàn tất trong mọi trường hợp: transaction, compaction và offset gaps làm cách diễn giải phức tạp hơn.

Khi cần replay, dừng/điều phối consumer, xác định khoảng còn giữ, quy định output idempotent rồi mới reset. Không chỉnh offset production như một cách xóa cảnh báo.

## Tài liệu gốc

[KafkaConsumer 4.0 API](https://kafka.apache.org/40/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html) giải thích position và commit. [Consumer configs](https://kafka.apache.org/40/configuration/consumer-configs/) mô tả auto commit và reset. Đây là ví dụ suy luận, không phải kiểm thử hai hệ thống với crash thực tế. Đối chiếu ngày 1/10/2026.
