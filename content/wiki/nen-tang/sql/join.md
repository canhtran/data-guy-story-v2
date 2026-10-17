---
title: "Kết hợp dữ liệu với JOIN"
description: "JOIN và lý do báo cáo có thể bị cộng tiền hai lần"
draft: false
contentType: "concept"
weight: 2
level: "beginner"
topics: ["sql"]
prerequisites: ["/wiki/nen-tang/sql/overview"]
related: []
---

Bạn có mã khách trong bảng đơn hàng, tên khách trong bảng khách hàng. JOIN nối những dòng phù hợp để mình đọc chúng cùng nhau. Nhưng nếu một đơn khớp với nhiều dòng phía bên kia, đơn đó cũng xuất hiện nhiều lần trong kết quả.

Bài này dùng **cafe-v1**, SQLite 3.25 trở lên. Làm bước tạo database trong [bài SQL đầu tiên]({{< relref "/wiki/nen-tang/sql/overview.md" >}}) trước khi chạy các truy vấn.

## Nối đơn với khách

`orders` có một dòng mỗi đơn. `customers` có một dòng mỗi khách, khóa `customer_id` không trùng.

```sql
SELECT o.order_id, c.customer_name, o.amount_vnd
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
ORDER BY o.order_id;
```

Kết quả có 4 dòng: 101–An–40000, 102–An–60000, 103–Bình–50000, 104–NULL–30000. LEFT JOIN giữ cả đơn không tìm được khách. INNER JOIN chỉ giữ các cặp khớp, nên trường hợp này còn 3 dòng. Cả hai đều có ích; lựa chọn phụ thuộc bạn có muốn giữ những đơn chưa xác định khách hay không.

## Một đơn có hai lần thử thanh toán

Trong `payments`, đơn 101 có một lần thất bại rồi một lần thành công. Nếu nối trực tiếp và cộng tiền đơn:

```sql
SELECT SUM(o.amount_vnd) AS wrong_revenue
FROM orders AS o
JOIN payments AS p ON o.order_id = p.order_id
WHERE o.status = 'paid';
```

Kết quả là **190000**, trong khi tổng ba đơn đã thanh toán chỉ là **150000**. Đơn 101 xuất hiện hai lần. Đây không phải engine cộng sai; mình đã đổi số dòng mà không để ý.

Không sửa bằng `SUM(DISTINCT amount_vnd)`: hai đơn khác nhau có thể cùng giá tiền, và khi đó bạn lại cộng thiếu. Cũng đừng dùng `DISTINCT` cả truy vấn chỉ để che việc khóa nối không duy nhất.

## Nếu chỉ cần biết có thanh toán thành công

```sql
SELECT SUM(o.amount_vnd) AS revenue_vnd
FROM orders AS o
WHERE o.status = 'paid'
  AND EXISTS (
    SELECT 1 FROM payments AS p
    WHERE p.order_id = o.order_id AND p.status = 'success'
  );
```

Kết quả **150000**. EXISTS kiểm tra có dòng phù hợp, không tạo thêm dòng đơn. Nếu cần số lần thử, hãy gom `payments` thành một dòng mỗi `order_id` rồi mới JOIN.

## Điều kiện đặt ở đâu?

Sau LEFT JOIN, `WHERE p.status = 'success'` sẽ loại những dòng không có payment vì phía `p` là NULL. Nếu muốn giữ tất cả đơn, đưa điều kiện này vào `ON`. Tuy nhiên, nhiều payment thành công vẫn có thể làm nhân dòng; vị trí điều kiện không thay thế việc hiểu quan hệ một–nhiều.

Trước khi nối, mình thường hỏi: mỗi bảng có một dòng cho thứ gì, khóa có trùng không, và kết quả cần một dòng cho thứ gì? Sau đó kiểm tra số dòng và vài khóa cụ thể, không chỉ tổng cuối cùng.

Thử thêm một đơn đã trả tiền giá 40000 đồng: cách dùng EXISTS phải tăng tổng lên 190000; `SUM(DISTINCT...)` sẽ không tăng đúng. Đây là một ca kiểm tra nhỏ để phát hiện cách sửa sai.

Đọc thêm: [PostgreSQL: Joins between tables](https://www.postgresql.org/docs/18/tutorial-join.html). Bước tiếp theo là dùng [CTE]({{< relref "/wiki/nen-tang/sql/cte.md" >}}) để tách các mức tổng hợp.
