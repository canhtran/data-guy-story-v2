---
title: "Sao chép dữ liệu"
description: "Replication: có bản sao chưa chắc đã có dữ liệu mới nhất"
draft: false
contentType: "concept"
weight: 3
level: "beginner"
topics: ["distributed-systems"]
prerequisites: ["/wiki/nen-tang/distributed-systems/overview"]
related: []
---

Database ghi đơn mới trên node A, sau đó chuyển thay đổi sang node B. B có thể phục vụ đọc hoặc được dùng khi A lỗi. Replication là việc duy trì các bản sao dữ liệu; mỗi cách sao chép có một thời điểm xác nhận và quy tắc phục hồi khác nhau.

## Một ca đọc bị cũ

Giả sử ban đầu A và B cùng có đơn ở trạng thái `pending`:

| Bước | A | B |
| --- | --- | --- |
| 1 | Ghi `paid`, trả thành công cho client | Chưa nhận thay đổi |
| 2 | | Client đọc thấy `pending` |
| 3 | | Nhận thay đổi, thành `paid` |

Đây là một lịch chạy minh họa replication bất đồng bộ. Khoảng giữa bước 1 và 3 là lúc đọc có thể bị cũ. Nếu A mất dữ liệu trước khi B nhận thay đổi, một ghi đã được client xác nhận có thể chưa có trên B.

## Chờ bản sao hay trả sớm?

Với sao chép đồng bộ, writer có thể chờ một số replica xác nhận trước khi trả thành công. Điều cần hỏi là xác nhận **đã nhận, đã ghi bền vững hay đã áp dụng**. Các mức này không giống nhau; chờ áp dụng còn có liên quan tới việc đọc replica thấy dữ liệu nào.

Chờ thêm replica có thể tăng độ trễ hoặc khiến lượt ghi không hoàn thành khi replica cần thiết bị lỗi. Trả sớm giảm thời gian chờ nhưng có rủi ro dữ liệu chưa tới bản sao. Cấu hình phải khớp mức mất dữ liệu và độ trễ mà ứng dụng chấp nhận.

## Đổi leader cần bảo vệ gì?

Khi A chậm, không được đơn giản cho B nhận ghi rồi để A tiếp tục nhận ghi độc lập. Hai nơi có thể tạo trạng thái xung đột. Quy trình failover cần xác định node có quyền ghi và ngăn node cũ hành động khi quyền đó đã mất. Bầu leader là một phần; bảo vệ writer cũ cũng là một phần.

## Replication không thay backup

Lệnh DELETE nhầm có thể được sao chép sang mọi replica rất nhanh. Backup có lịch sử và khả năng phục hồi về thời điểm trước lỗi giải quyết một nhu cầu khác. Muốn tin backup, phải thử khôi phục và đo thời gian, không chỉ thấy file tồn tại.

Bài tập: nếu yêu cầu sau khi ghi người dùng luôn đọc thấy trạng thái mình vừa ghi, bạn sẽ đọc ở đâu hoặc chờ điều kiện gì? “Có replica” chưa đủ để trả lời.

Tham khảo: [PostgreSQL standby and replication](https://www.postgresql.org/docs/18/warm-standby.html). Đọc tiếp [consistency]({{< relref "/wiki/nen-tang/distributed-systems/consistency.md" >}}).
