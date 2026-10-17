---
title: "Chỉ mục trong cơ sở dữ liệu"
description: "Index: tìm ít dòng hơn, đổi lại ghi nhiều việc hơn"
draft: false
contentType: "concept"
weight: 3
level: "beginner"
topics: ["database"]
prerequisites: ["/wiki/nen-tang/database/overview"]
related: []
---

Trong cuốn sách, mục lục giúp mình tìm một phần mà không lật từ trang đầu. Index trong database cũng là một cấu trúc tra cứu, nhưng phải được cập nhật cùng dữ liệu và chỉ hữu ích với một số cách tìm kiếm.

Đừng coi index là bản sao toàn bộ bảng được sắp xếp đẹp hơn. Nó giữ khóa tra cứu và thông tin để tìm dữ liệu; chi tiết phụ thuộc loại index và engine.

## Thử tìm đơn theo khách

Dùng SQLite 3.25 trở lên và [cafe-v1]({{< relref "/wiki/nen-tang/sql/overview.md" >}}), chưa tạo index cho khách:

```sql
EXPLAIN QUERY PLAN
SELECT order_id FROM orders WHERE customer_id = 1;

CREATE INDEX IF NOT EXISTS orders_customer_idx ON orders(customer_id);

EXPLAIN QUERY PLAN
SELECT order_id FROM orders WHERE customer_id = 1;
```

Trong môi trường SQLite 3.53.4 dùng để kiểm tra, kế hoạch đầu có `SCAN orders`; kế hoạch sau dùng `orders_customer_idx`. Nếu đã chạy ví dụ tối ưu SQL, index tồn tại rồi nên cả hai có thể cùng dùng index. `IF NOT EXISTS` giúp không lỗi khi chạy lại lệnh tạo.

Trên bốn dòng, thay đổi này chỉ minh họa cơ chế, không chứng minh lợi ích tốc độ. Optimizer có thể chọn scan khi nhiều dòng phù hợp hoặc bảng rất nhỏ.

## Chọn cột theo truy vấn

Giả sử thường tìm đơn của một khách trong một khoảng ngày. Index `(customer_id, business_date)` có thể phù hợp hơn index ngày đơn lẻ. Nếu thường tìm mọi đơn của một ngày, thứ tự đó chưa chắc là lựa chọn tốt nhất. B-tree thường hữu ích với tìm bằng và khoảng; không nên áp dụng trực giác đó cho mọi loại index.

Một index có đủ các cột truy vấn cần có thể giảm việc đọc bảng, nhưng khả năng thực hiện phụ thuộc engine. Trong PostgreSQL còn có điều kiện về khả năng nhìn thấy dòng khi dùng index-only scan; không phải thêm cột là mọi lần đọc bảng đều biến mất.

## Chi phí nằm ở lúc ghi

Mỗi đơn mới cần cập nhật các index liên quan. Nhiều index có thể làm ingest chậm hơn, tăng dung lượng và thời gian bảo trì. Index không sửa được JOIN sai, dữ liệu trùng hoặc báo cáo tính sai đơn vị.

Trước khi thêm, ghi lại truy vấn cần cải thiện, đọc kế hoạch, đo với dữ liệu đại diện và kiểm tra chi phí ghi. Trước khi bỏ, kiểm tra index có phục vụ constraint hoặc truy vấn khác không.

Đọc tiếp [tối ưu SQL]({{< relref "/wiki/nen-tang/sql/query-optimization.md" >}}). Tham khảo: [PostgreSQL indexes](https://www.postgresql.org/docs/18/indexes.html), [SQLite EXPLAIN QUERY PLAN](https://www.sqlite.org/eqp.html).
