---
title: "Các mức cô lập giao dịch"
description: "Isolation: khi hai giao dịch cùng đọc và ghi"
draft: false
contentType: "concept"
weight: 5
level: "beginner"
topics: ["database"]
prerequisites: ["/wiki/nen-tang/database/overview"]
related: []
---

Kho còn một túi cà phê. Hai giao dịch cùng đọc “còn 1”, cả hai đều quyết định bán, rồi ghi lại “còn 0”. Từng câu UPDATE có thể chạy được nhưng hệ thống đã bán hai túi. Khi nhiều giao dịch cùng làm việc, mình cần hiểu chúng thấy dữ liệu nào và database bảo vệ xung đột đến đâu.

Isolation là mức cô lập giữa các transaction. Bài này giải thích bằng lịch chạy; không phải hướng dẫn chạy bốn mức isolation trên SQLite, vì SQLite không cung cấp chúng giống PostgreSQL.

## Những hiện tượng cần nhận ra

- **Dirty read:** đọc thay đổi của giao dịch chưa commit, rồi thay đổi đó bị rollback.
- **Non-repeatable read:** đọc lại cùng một dòng và nhận giá trị khác do giao dịch khác đã commit.
- **Phantom:** chạy lại điều kiện tìm kiếm và thấy tập dòng phù hợp thay đổi.
- **Serialization anomaly:** kết quả của các giao dịch đồng thời không tương đương bất kỳ thứ tự chạy lần lượt nào.

Các mức theo chuẩn SQL đặt giới hạn cho các hiện tượng. Engine có thể bảo vệ nhiều hơn mức tối thiểu của chuẩn, nên cần đọc tài liệu cụ thể.

## Ví dụ theo PostgreSQL 18

Giả sử dòng tồn kho bắt đầu là 1:

| Bước | Kết nối A | Kết nối B |
| --- | --- | --- |
| 1 | BEGIN, đọc tồn kho: 1 | |
| 2 | | Cập nhật thành 0, COMMIT |
| 3 | Đọc lại tồn kho | |

Ở **Read Committed**, truy vấn mới của A có thể thấy 0: mỗi câu lệnh lấy snapshot mới. Ở **Repeatable Read**, nếu snapshot đã được thiết lập từ lần đọc đầu, A vẫn đọc 1 từ snapshot của mình. Điều này không có nghĩa A có thể cập nhật an toàn mà không gặp xung đột.

PostgreSQL dùng Read Committed mặc định; Read Uncommitted hoạt động như Read Committed. Repeatable Read của PostgreSQL cũng ngăn phantom, nhưng vẫn có thể có serialization anomaly. Serializable thêm bảo vệ để các giao dịch commit tương đương một thứ tự nối tiếp, và có thể hủy một giao dịch khi phát hiện xung đột. Ứng dụng cần retry toàn bộ transaction, không chỉ câu SQL cuối.

## Đừng chỉ “đọc rồi ghi”

Với bán tồn kho, có thể dùng một cập nhật có điều kiện: `UPDATE ... SET stock = stock - 1 WHERE stock > 0`, rồi kiểm tra số dòng cập nhật. Cách cụ thể còn phụ thuộc schema, engine và yêu cầu của giao dịch. Khóa dòng hoặc isolation mạnh hơn là những công cụ khác; chúng có thể làm giao dịch chờ nhau hoặc cần retry.

Bài tập: nếu B rollback thay vì commit ở bước 2, A có nên đọc được giá trị 0 do B tạo ra không? Với các mức của PostgreSQL ở trên, câu trả lời là không. Thử phân biệt điều này với việc A đọc lại một giá trị đã được B commit.

## SQLite có giới hạn riêng

SQLite thường chỉ có một writer tại một thời điểm; chế độ WAL cho reader nhìn snapshot trong khi writer hoạt động. Cố nâng một snapshot đọc cũ thành giao dịch ghi có thể thất bại. Không suy ra hành vi của PostgreSQL từ một bài thử SQLite.

Tham khảo: [PostgreSQL transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html), [SQLite isolation](https://www.sqlite.org/isolation.html). Đọc trước [transaction]({{< relref "/wiki/nen-tang/database/transaction.md" >}}) nếu còn mới với BEGIN, COMMIT và ROLLBACK.
