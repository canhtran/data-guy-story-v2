---
title: "Tối ưu truy vấn SQL"
description: "Tối ưu SQL: đo trước khi sửa"
draft: false
contentType: "concept"
weight: 5
level: "beginner"
topics: ["sql"]
prerequisites: ["/wiki/nen-tang/sql/overview"]
related: []
---

Bạn viết truy vấn đúng, nhưng báo cáo chạy lâu. Thêm index ngay có thể giúp, cũng có thể không. Mình thường bắt đầu bằng hai câu hỏi: truy vấn đang đọc bao nhiêu dữ liệu, và phần nào khiến nó làm nhiều việc nhất?

Ví dụ dùng **cafe-v1**, SQLite 3.25 trở lên; xem [bài SQL đầu tiên]({{< relref "/wiki/nen-tang/sql/overview.md" >}}). Dữ liệu bốn dòng chỉ để đọc kế hoạch, không đủ để kết luận nhanh hơn bao nhiêu.

## Xem engine định làm gì

```sql
EXPLAIN QUERY PLAN
SELECT order_id, amount_vnd
FROM orders
WHERE customer_id = 1;
```

Với schema ban đầu, bạn sẽ thấy phần mô tả có `SCAN orders`. Engine dự kiến đọc bảng để tìm khách 1. Thử tạo index:

```sql
CREATE INDEX orders_customer_idx ON orders(customer_id);
EXPLAIN QUERY PLAN
SELECT order_id, amount_vnd
FROM orders
WHERE customer_id = 1;
```

Trong môi trường kiểm tra của ví dụ, mô tả chuyển sang `SEARCH orders USING INDEX orders_customer_idx`. Định dạng và lựa chọn kế hoạch có thể khác theo phiên bản, thống kê và kích thước dữ liệu. Scan trên bảng rất nhỏ không phải dấu hiệu có lỗi.

Truy vấn thật vẫn trả đơn 101 giá 40000 và đơn 102 giá 60000. Một thay đổi tối ưu phải giữ kết quả đúng trước khi mình nhìn thời gian chạy.

## Index giải quyết câu hỏi nào?

Index này giúp tìm đơn theo khách. Nó không tự giải quyết việc cộng toàn bộ doanh thu theo ngày. Với index nhiều cột, thứ tự cột và điều kiện truy vấn có ý nghĩa; không nên tạo index cho mọi cột. Mỗi index chiếm chỗ và làm thêm việc khi ghi dữ liệu.

Nếu một truy vấn nối bảng làm số dòng tăng từ một triệu lên một trăm triệu, sửa quan hệ JOIN có thể quan trọng hơn chọn index. Tương tự, chỉ lấy cột cần dùng và lọc đúng phạm vi trước các bước đắt tiền thường giúp giảm công việc. Engine có thể tự đẩy điều kiện xuống, nhưng bạn vẫn cần kiểm tra kế hoạch.

## Đo bằng dữ liệu có ý nghĩa

Ghi lại truy vấn, phiên bản engine, số dòng, kích thước dữ liệu và cách đo. Chạy nhiều lần để phân biệt ảnh hưởng cache; so sánh cùng điều kiện. Kiểm tra cả khách ít đơn và khách rất nhiều đơn, vì phân bố lệch có thể khiến một kế hoạch tốt với nhóm này lại tệ với nhóm khác.

Trong PostgreSQL, `EXPLAIN` cho kế hoạch dự kiến; `EXPLAIN (ANALYZE, BUFFERS)` thực thi truy vấn để đưa số liệu thực tế. Với lệnh thay đổi dữ liệu, ANALYZE cũng thực hiện thay đổi, nên đừng dùng như thể nó chỉ xem trước. SQLite `EXPLAIN QUERY PLAN` không phải bộ đo thời gian thực thi tương đương.

## Một checklist nhỏ

- Kết quả và số dòng có đúng, đặc biệt sau JOIN không?
- Dòng được đọc nhiều hơn dòng trả về đến mức nào?
- Có sort hoặc tổng hợp lớn, hay cột lọc bị bọc trong hàm làm index khó dùng?
- Thống kê có phản ánh dữ liệu hiện tại không?
- Chi phí ghi và dung lượng index có đáng đổi lấy tốc độ đọc không?

Tham khảo: [SQLite EXPLAIN QUERY PLAN](https://www.sqlite.org/eqp.html), [PostgreSQL Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html). Đọc thêm [JOIN]({{< relref "/wiki/nen-tang/sql/join.md" >}}) nếu truy vấn chạy lâu vì nhân dòng.
