---
title: "Các thuộc tính ACID"
description: "ACID bảo vệ giao dịch đến đâu?"
draft: false
contentType: "concept"
weight: 6
level: "beginner"
topics: ["database"]
prerequisites: ["/wiki/nen-tang/database/overview"]
related: []
---

Một transaction có thể chứa nhiều câu SQL. ACID là bốn thuộc tính thường dùng để mô tả những gì hệ quản trị bảo vệ khi transaction chạy và dữ liệu được lưu. Nhưng nghe “database có ACID” chưa đủ để kết luận cả pipeline đúng.

## Đi qua một ca cụ thể

Giả sử đơn 104 được cập nhật sang `paid`, đồng thời thêm payment tương ứng. [Bài transaction]({{< relref "/wiki/nen-tang/database/transaction.md" >}}) có ví dụ SQLite chạy được.

| Thuộc tính | Câu hỏi trong ca này |
| --- | --- |
| Atomicity — nguyên tử | Hai thay đổi được chấp nhận cùng nhau hay chỉ một phần? |
| Consistency — nhất quán | Trạng thái sau giao dịch có tuân thủ các ràng buộc đã định nghĩa không? |
| Isolation — cô lập | Giao dịch khác nhìn thấy và tương tác với thay đổi này thế nào? |
| Durability — bền vững | Sau khi báo commit thành công, thay đổi có được giữ theo cam kết của hệ thống không? |

Consistency ở đây gắn với ràng buộc và logic giao dịch, không phải cam kết “mọi replica luôn thấy dữ liệu mới nhất”. Hai cách dùng chữ consistency này cần phân biệt.

## Những gì ACID không biết

Nếu code cập nhật nhầm đơn 103, transaction vẫn có thể commit hoàn toàn hợp lệ. Nếu schema cho phép số tiền sai, database không biết giá bán đúng để chặn. Và nếu ghi database rồi ghi file ở hai bước tách biệt, ACID của database không tự bao trùm file đó.

Isolation có nhiều mức; không phải mọi giao dịch đều được thực thi như chạy lần lượt. Durability cũng phụ thuộc cấu hình, cách đồng bộ xuống storage và giả định về phần cứng. Tắt cơ chế đồng bộ để tăng tốc có thể thay đổi mức bảo vệ khi máy mất điện.

## Một bài kiểm tra bằng tay

Bắt đầu với đơn chưa thanh toán, chạy cập nhật đơn rồi chủ động rollback trước khi thêm payment. Đơn phải trở lại trạng thái cũ. Thử thêm payment với mã đơn không tồn tại khi khóa ngoại đã bật: lệnh phải bị từ chối.

Hai kiểm tra này cho mình bằng chứng về rollback và constraint trong ca cụ thể. Chúng **không** chứng minh đầy đủ tính bền vững khi mất điện hoặc mọi tình huống giao dịch đồng thời. Muốn kiểm tra các thuộc tính đó cần môi trường, cấu hình và ca lỗi phù hợp, không chỉ một truy vấn chạy thành công.

## Dùng ACID khi trao đổi thiết kế

Hãy nói rõ transaction nằm ở đâu, dữ liệu nào được commit chung, mức isolation nào, và điều gì xảy ra nếu hệ thống báo timeout sau commit. Timeout không luôn có nghĩa giao dịch thất bại: client có thể chưa nhận được phản hồi của một commit đã thành công. Chạy lại cần [idempotency]({{< relref "/wiki/data-engineering/idempotency.md" >}}) hoặc cách kiểm tra trạng thái.

Tham khảo: [SQLite atomic commit](https://www.sqlite.org/atomiccommit.html), [PostgreSQL transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html). Xem tiếp [isolation]({{< relref "/wiki/nen-tang/database/isolation-level.md" >}}).
