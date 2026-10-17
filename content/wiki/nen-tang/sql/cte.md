---
title: "Biểu thức bảng chung (CTE)"
description: "CTE: chia một truy vấn thành những bước dễ đọc"
draft: false
contentType: "concept"
weight: 4
level: "beginner"
topics: ["sql"]
prerequisites: ["/wiki/nen-tang/sql/overview"]
related: []
---

Một truy vấn vừa nối nhiều bảng vừa tổng hợp vừa lọc thường khó kiểm tra. Mình thích đặt tên cho từng bước: lấy đơn đã thanh toán, tính tổng mỗi khách, rồi chọn khách cần xem. CTE, viết bằng `WITH`, cho phép làm việc đó trong một câu SQL.

Ví dụ dùng **cafe-v1**, SQLite 3.25 trở lên. Xem [cách tạo database]({{< relref "/wiki/nen-tang/sql/overview.md" >}}) nếu bạn chưa có dữ liệu.

## Đặt tên cho kết quả trung gian

```sql
WITH paid_orders AS (
  SELECT customer_id, amount_vnd
  FROM orders
  WHERE status = 'paid'
), customer_totals AS (
  SELECT customer_id, SUM(amount_vnd) AS total_vnd
  FROM paid_orders
  GROUP BY customer_id
)
SELECT c.customer_name, t.total_vnd
FROM customer_totals AS t
JOIN customers AS c ON t.customer_id = c.customer_id
WHERE t.total_vnd >= 80000
ORDER BY c.customer_id;
```

Kết quả có một dòng: **An, 100000**. Tên `paid_orders` nói rõ dữ liệu còn lại sau bước lọc. `customer_totals` có một dòng mỗi khách, nên bước JOIN sau đó dễ kiểm tra hơn.

CTE chỉ có tên trong câu lệnh này. Nó không tạo một bảng lưu lâu dài. Truy vấn kế tiếp không thể `SELECT * FROM paid_orders` trừ khi bạn đã tạo một bảng hoặc view mang tên đó.

## Kiểm tra từng bước

Giữ phần WITH và thay SELECT cuối bằng `SELECT * FROM paid_orders;`: bạn cần thấy ba đơn đã trả tiền. Đổi sang `SELECT * FROM customer_totals ORDER BY customer_id;`: phải thấy khách 1 là 100000, khách 2 là 50000.

Đây là cách rất hữu ích khi AI gợi ý một truy vấn dài. Hãy hỏi nó mỗi CTE có một dòng đại diện cho điều gì, rồi tự chạy kiểm tra. Một câu SQL trông gọn không đảm bảo phép tính đúng.

## CTE không tự làm truy vấn nhanh hơn

Engine có thể nhập CTE vào kế hoạch lớn hoặc tính kết quả trung gian, tùy hệ quản trị, phiên bản và cách truy vấn dùng nó. Vì vậy không nên coi WITH là “bảng tạm miễn phí” hay một cách tối ưu mặc định. Khi hiệu năng quan trọng, đọc [kế hoạch truy vấn]({{< relref "/wiki/nen-tang/sql/query-optimization.md" >}}).

Nếu kết quả cần dùng cho nhiều lần truy vấn, cân nhắc view hoặc bảng đã tính sẵn. View thường lưu định nghĩa; bảng lưu dữ liệu và cần cách cập nhật. Chúng giải quyết một nhu cầu khác với việc chia một câu SQL cho dễ đọc.

## Còn recursive CTE?

CTE đệ quy có một phần khởi đầu và một phần tạo thêm dòng từ kết quả trước. Nó hữu ích cho cây danh mục hoặc đường đi. Nhưng cần điều kiện dừng và xử lý chu trình, nếu không có thể tạo rất nhiều dòng. Bài này tập trung CTE thông thường; đừng thêm đệ quy chỉ vì muốn duyệt vài bảng liên quan.

Bài tập: đổi ngưỡng thành 50000. Kết quả phải có An 100000 và Bình 50000. Sau đó thêm một đơn hủy giá 90000 cho Bình: tổng đã thanh toán của Bình vẫn là 50000.

Tham khảo: [SQLite WITH](https://www.sqlite.org/lang_with.html) và [PostgreSQL WITH queries](https://www.postgresql.org/docs/18/queries-with.html).
