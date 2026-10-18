# Giao dịch trong cơ sở dữ liệu

Khách thanh toán xong, ứng dụng cần cập nhật trạng thái đơn và thêm bản ghi thanh toán. Nếu bước đầu thành công mà bước sau lỗi, database có thể nói đơn đã trả tiền nhưng không có thanh toán tương ứng.

Transaction gom các thay đổi vào một đơn vị: commit nếu chấp nhận toàn bộ, rollback nếu bỏ chúng. Nó không tự đảm bảo code chọn đúng đơn hay số tiền; các câu lệnh trong transaction vẫn cần đúng nghiệp vụ.

## Thử rollback rồi commit

Dùng SQLite 3.25 trở lên và một bản mới của [cafe-v1]({{< relref "/wiki/nen-tang/sql/overview.md" >}}). Đơn 104 hiện đang hủy; trong ví dụ giả lập, mình thử đổi trạng thái nhưng chưa chấp nhận thay đổi:

```sql
BEGIN;
UPDATE orders SET status = 'paid' WHERE order_id = 104;
SELECT status FROM orders WHERE order_id = 104;
ROLLBACK;
SELECT status FROM orders WHERE order_id = 104;
```

Hai kết quả lần lượt là **paid** trong transaction và **cancelled** sau rollback. Kết nối của bạn thấy thay đổi chưa commit của chính nó.

Bây giờ thử chấp nhận cả hai thay đổi:

```sql
BEGIN;
UPDATE orders SET status = 'paid' WHERE order_id = 104;
INSERT INTO payments VALUES (5,104,'success');
COMMIT;
SELECT status FROM orders WHERE order_id = 104;
SELECT COUNT(*) FROM payments WHERE order_id = 104;
```

Kết quả là **paid** và **1** payment. Chỉ chạy phần này một lần trên dữ liệu mới. Lần hai sẽ lỗi khóa payment 5; cần rollback transaction đang mở trước khi thử lại với database khác.

## Lỗi một câu lệnh có tự rollback hết không?

Không nên giả định như vậy. SQLite thường hủy câu lệnh bị lỗi, còn transaction có thể vẫn mở; loại lỗi và chế độ conflict có thể làm hành vi khác. PostgreSQL đánh dấu transaction lỗi và yêu cầu rollback hoặc xử lý qua savepoint. Ứng dụng cần xử lý ngoại lệ và quyết định rollback rõ ràng, không tiếp tục commit như thể mọi bước đều đã thành công.

## Ranh giới chỉ bao gồm những gì tham gia

Database transaction không tự rollback email đã gửi, file đã ghi hoặc API thanh toán bên ngoài. Nếu transaction database bị rollback sau khi API nhận tiền, bạn cần cơ chế phối hợp khác: mã yêu cầu để tránh xử lý trùng, ghi sự kiện trong cùng transaction rồi gửi sau, hoặc quy trình bù trừ.

Giữ transaction đủ ngắn để tránh giữ tài nguyên lâu. Đừng mở transaction rồi chờ người dùng trả lời hoặc một API chậm nếu không có lý do rõ ràng.

Đọc tiếp [ACID]({{< relref "/wiki/nen-tang/database/acid.md" >}}) và [isolation]({{< relref "/wiki/nen-tang/database/isolation-level.md" >}}). Tham khảo: [SQLite transactions](https://www.sqlite.org/lang_transaction.html), [PostgreSQL transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html).

