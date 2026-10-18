# SQL là gì?

Quán cà phê có bốn đơn hàng. Bạn muốn biết ngày nào bán được bao nhiêu tiền, nhưng không muốn cộng cả đơn đã hủy. Đây là một câu hỏi nhỏ mà SQL làm rất tốt.

SQL là ngôn ngữ để làm việc với dữ liệu trong các hệ quản trị cơ sở dữ liệu và nhiều công cụ phân tích. Với truy vấn, mình mô tả dữ liệu muốn lấy; engine chọn cách thực hiện. Viết đúng cú pháp mới chỉ là bước đầu. Mình còn phải biết mỗi dòng là gì và “doanh thu” được tính thế nào.

## Thử ngay trên máy của bạn

Các ví dụ trong nhóm SQL dùng **SQLite 3.25 trở lên**, chạy cục bộ và không cần tài khoản. Mình đã kiểm tra chúng với SQLite 3.53.4 qua Python; đây là ví dụ học SQL, không phải đề xuất dùng SQLite cho mọi warehouse.

Gõ `sqlite3 --version` trong terminal. Nếu chưa có lệnh này, xem [hướng dẫn CLI của SQLite](https://www.sqlite.org/cli.html) để chọn bản dành cho hệ điều hành của bạn. Nếu máy đã có Python 3, kiểm tra engine bằng `python3 -c "import sqlite3; print(sqlite3.sqlite_version)"`.

Tải [file dữ liệu cafe.sql](../../../../examples/wiki/sql/cafe.sql), lưu vào thư mục riêng rồi mở terminal tại đó:

```sh
sqlite3 cafe.db < cafe.sql
sqlite3 cafe.db
```

Chỉ chạy bước nhập một lần với một file `cafe.db` mới. Nếu nhận lỗi `table already exists`, dữ liệu đã được tạo; mở database thay vì nhập lại. Trong cửa sổ SQLite, gõ `.headers on` và `.mode column` để dễ đọc; `.quit` để thoát. Cần làm lại thì dùng tên database mới, chẳng hạn `cafe-lan-2.db`.

### File dữ liệu

<a href="../../../../examples/wiki/sql/cafe.sql" download>Tải cafe.sql</a>. Dữ liệu hoàn toàn giả lập, mã fixture **cafe-v1**. Mỗi dòng `orders` là một đơn, khóa `order_id`; mỗi dòng `customers` là một khách; mỗi dòng `payments` là một lần thử thanh toán. `business_date` là ngày kinh doanh theo giờ Việt Nam đã được xác định sẵn, không phải timestamp UTC. Số tiền dùng số nguyên đồng.

## Lọc trước, cộng sau

```sql
SELECT business_date, COUNT(*) AS order_count,
       SUM(amount_vnd) AS revenue_vnd
FROM orders
WHERE status = 'paid'
GROUP BY business_date
ORDER BY business_date;
```

Bạn sẽ thấy ngày `2026-09-01` có 2 đơn, 100000 đồng; ngày `2026-09-02` có 1 đơn, 50000 đồng. Đơn 104 bị hủy nên không nằm trong phép tính.

`WHERE` chọn dòng trước khi gom nhóm. `GROUP BY` tạo một dòng cho mỗi ngày. Nếu muốn chỉ giữ ngày có doanh thu từ 80000 đồng, thêm `HAVING SUM(amount_vnd) >= 80000` trước `ORDER BY`. `ORDER BY` là điều bạn cần viết khi thứ tự kết quả có ý nghĩa; không nên dựa vào thứ tự tình cờ engine trả về.

## NULL không phải số không

Đơn 104 không có khách được nhận diện. Tìm nó bằng `WHERE customer_id IS NULL`, không phải `customer_id = NULL`. Giá trị chưa biết khác với khách có mã 0, chuỗi rỗng hoặc số tiền bằng 0. Thử `SELECT COUNT(*), COUNT(customer_id) FROM orders;`: kết quả là **4 và 3**, vì phép đếm cột bỏ qua NULL.

Khi dữ liệu rỗng, `COUNT(*)` trả 0 nhưng `SUM` có thể trả NULL. Chỉ dùng `COALESCE(..., 0)` khi định nghĩa báo cáo thật sự cho phép hiểu “không có dữ liệu” thành số không.

## Học tiếp

Khi câu hỏi cần tên khách, đọc [JOIN]({{< relref "/wiki/nen-tang/sql/join.md" >}}). Khi muốn giữ từng đơn nhưng thêm tổng của khách, xem [window functions]({{< relref "/wiki/nen-tang/sql/window-function.md" >}}).

Tham khảo: [SQLite SELECT](https://www.sqlite.org/lang_select.html) và [PostgreSQL SQL tutorial](https://www.postgresql.org/docs/18/tutorial-sql.html). Cú pháp cơ bản khá giống nhau; kiểu dữ liệu và tính năng nâng cao cần kiểm tra theo engine bạn dùng.

