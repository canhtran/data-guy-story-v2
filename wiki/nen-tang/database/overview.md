# Cơ sở dữ liệu là gì?

Một file CSV có thể lưu danh sách đơn hàng. Nhưng nếu hai người cùng sửa, một người nhập mã khách không tồn tại, rồi máy tắt giữa lúc ghi file, mình cần xử lý rất nhiều thứ. Hệ quản trị cơ sở dữ liệu giúp quản lý việc đọc, ghi, ràng buộc và phục hồi thay vì để từng ứng dụng tự làm hết.

“Database” là nơi tổ chức dữ liệu; “DBMS” là phần mềm quản lý nó. Trong cách nói hằng ngày hai từ thường được dùng gần nhau. Bài này tập trung database quan hệ, nơi dữ liệu được tổ chức thành bảng có cột và quan hệ giữa các bảng.

## Bảng cần nói rõ mỗi dòng là gì

Với [dữ liệu café của nhóm SQL]({{< relref "/wiki/nen-tang/sql/overview.md" >}}), một dòng `orders` là một đơn; `order_id` nhận diện đơn đó. Một dòng `payments` là một lần thử thanh toán, nên một đơn có thể có nhiều dòng payment.

Schema mô tả cấu trúc và quy tắc: tên cột, kiểu dữ liệu, khóa và ràng buộc. Các ví dụ có `PRIMARY KEY`, `NOT NULL`, `CHECK` và khóa ngoại. Khóa ngoại giúp tránh việc một payment tham chiếu tới đơn không tồn tại; nó không tự đảm bảo đơn đã thanh toán đủ tiền.

## Thử một dữ liệu sai

Mở database `cafe.db` bằng SQLite theo bài SQL, bật kiểm tra khóa ngoại cho **kết nối hiện tại** rồi chạy:

```sql
PRAGMA foreign_keys = ON;
INSERT INTO payments VALUES (99,999,'success');
```

Bạn cần nhận lỗi `FOREIGN KEY constraint failed`; mã đơn 999 chưa tồn tại. Chạy `SELECT COUNT(*) FROM payments;`: vẫn có **4** lần thử, vì dòng lỗi không được thêm. Trong SQLite, đừng giả định mọi kết nối đều đã bật kiểm tra khóa ngoại. PostgreSQL thực thi các khóa ngoại đã khai báo mà không dùng PRAGMA này.

## Database không tự hiểu nghiệp vụ

`CHECK (amount_vnd >= 0)` có thể chặn số tiền âm, nhưng không biết 40000 là giá đúng hay bạn quên nhập một chữ số. `NOT NULL` chặn giá trị thiếu, nhưng không chặn chuỗi rỗng. `UNIQUE` có thể bảo vệ một khóa, nhưng bạn vẫn phải chọn khóa phù hợp với điều đang nhận diện.

Dữ liệu có thể hợp lệ về schema mà vẫn sai đối với báo cáo. Vì thế cần kiểm tra nghiệp vụ và [data quality]({{< relref "/wiki/data-engineering/data-quality.md" >}}) bên cạnh ràng buộc database.

## Khi nào file vẫn đủ dùng?

Một bộ dữ liệu nhỏ, ít thay đổi và không có nhiều người ghi có thể dùng file rất tốt. Khi cần cập nhật đồng thời, truy vấn linh hoạt hoặc nhiều quy tắc nhất quán, database thường hợp lý hơn. Nó cũng mang thêm việc quản lý quyền, backup, dung lượng và vận hành; không phải cứ thêm database là hệ thống tốt hơn.

Đọc tiếp [transaction]({{< relref "/wiki/nen-tang/database/transaction.md" >}}) để hiểu cách gom nhiều thay đổi. Tham khảo: [PostgreSQL concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html), [constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html).

