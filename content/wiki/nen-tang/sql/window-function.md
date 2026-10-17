---
title: "Hàm cửa sổ trong SQL"
description: "Window function: tính thêm mà vẫn giữ từng dòng"
draft: false
contentType: "concept"
weight: 3
level: "beginner"
topics: ["sql"]
prerequisites: ["/wiki/nen-tang/sql/overview"]
related: []
---

Báo cáo cần từng đơn của An, kèm tổng tiền An đã mua. Nếu GROUP BY khách, hai đơn sẽ bị gom thành một dòng. Window function cho mình tính trên nhóm dòng liên quan mà vẫn giữ từng dòng ban đầu.

Ví dụ dùng **cafe-v1**, SQLite 3.25 trở lên; tạo database theo [bài SQL đầu tiên]({{< relref "/wiki/nen-tang/sql/overview.md" >}}).

## Tổng của khách trên từng đơn

```sql
SELECT order_id, customer_id, amount_vnd,
       SUM(amount_vnd) OVER (
         PARTITION BY customer_id
       ) AS customer_total
FROM orders
WHERE status = 'paid'
ORDER BY customer_id, order_id;
```

| order_id | customer_id | amount_vnd | customer_total |
| --- | --- | --- | --- |
| 101 | 1 | 40000 | 100000 |
| 102 | 1 | 60000 | 100000 |
| 103 | 2 | 50000 | 50000 |

`PARTITION BY` chia các dòng thành nhóm để tính. Nó không phải partition trên đĩa. Tổng của An lặp lại ở hai dòng, nên **không cộng cột customer_total lần nữa** để tìm doanh thu toàn quán.

## Tổng lũy kế cần một thứ tự rõ ràng

```sql
SELECT order_id, customer_id,
       SUM(amount_vnd) OVER (
         PARTITION BY customer_id
         ORDER BY business_date, order_id
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM orders
WHERE status = 'paid'
ORDER BY customer_id, business_date, order_id;
```

Lần lượt là 40000, 100000 và 50000. `ROWS` ở đây nói lấy các dòng từ đầu nhóm đến dòng hiện tại. Thêm `order_id` giúp thứ tự xác định khi nhiều đơn có cùng ngày. Thứ tự trong `OVER` phục vụ phép tính; `ORDER BY` ngoài cùng phục vụ cách hiển thị.

Nếu chỉ sắp xếp theo ngày và để frame mặc định, các dòng đồng hạng có thể cùng nhận tổng đến hết nhóm đồng hạng. Vì vậy, nên viết frame mình muốn khi tính lũy kế. Tổng theo thứ tự mã đơn là ví dụ học cơ chế; trong hệ thống thật, bạn cần timestamp và quy tắc khi timestamp trùng.

## Lấy một đơn mỗi khách

```sql
WITH ranked AS (
  SELECT order_id, customer_id,
         ROW_NUMBER() OVER (
           PARTITION BY customer_id
           ORDER BY business_date DESC, order_id DESC
         ) AS rn
  FROM orders
  WHERE status = 'paid'
)
SELECT order_id, customer_id
FROM ranked
WHERE rn = 1
ORDER BY customer_id;
```

Kết quả là đơn 102 của khách 1, đơn 103 của khách 2. Mình tính số thứ tự trong CTE rồi lọc ở ngoài; không dùng alias `rn` trong WHERE của cùng mức truy vấn. `ROW_NUMBER` chọn một dòng, còn `RANK` có thể giữ nhiều dòng đồng hạng nếu lọc hạng 1.

Khi dùng cách này để bỏ trùng, phải có quy tắc chọn bản ghi mới nhất: thời gian cập nhật, số phiên bản, rồi tiêu chí phá hòa. “Chọn dòng đầu” khi thứ tự không xác định có thể làm kết quả thay đổi qua mỗi lần chạy.

Thử bỏ `WHERE status = 'paid'`: bạn sẽ có thêm nhóm khách NULL. Đây là lý do phải quyết định phạm vi dữ liệu trước khi tính window.

Tham khảo: [SQLite window functions](https://www.sqlite.org/windowfunctions.html) và [PostgreSQL window tutorial](https://www.postgresql.org/docs/18/tutorial-window.html).
