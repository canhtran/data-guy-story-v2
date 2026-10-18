# Lỗi và logging: biết dòng nào sai, vì sao job dừng

Job hiện “thành công”, nhưng đã bỏ qua một nửa số đơn. Đôi khi nguyên nhân là một khối `except` quá rộng: lỗi gì cũng bỏ qua, không ghi lại dòng hoặc lý do. Mình cần quy tắc về lỗi trước khi quyết định tiếp tục.

Dữ liệu không hợp lệ, file không tồn tại, database mất kết nối và bug trong code là những lỗi khác nhau. Một dòng tiền sai có thể được đưa vào danh sách để xem lại. Mất toàn bộ file đầu vào thường không nên biến thành báo cáo 0 đồng.

## Một lỗi dự kiến, một thông báo hữu ích

Lưu ví dụ thành file Python và chạy cục bộ bằng Python 3.12. Nó dùng dữ liệu giả lập, không cần thư viện ngoài. Mỗi dòng là một khoản tiền của một đơn riêng; ví dụ tập trung chuyển kiểu, chưa xử lý trùng khóa.

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
rows = [(101, "40000"), (102, "không rõ"), (103, "60000")]
accepted = []
rejected = []
for order_id, raw_amount in rows:
    try:
        amount = int(raw_amount)
        if amount < 0:
            raise ValueError("amount must be non-negative")
    except ValueError:
        rejected.append((order_id, "invalid_amount"))
        logging.warning("order_id=%s reason=invalid_amount", order_id)
        continue
    accepted.append((order_id, amount))
logging.info("accepted=%s rejected=%s", len(accepted), len(rejected))
print(sum(amount for _, amount in accepted))
print(rejected)
```

Kết quả chuẩn: tổng **100000**, danh sách loại **[(102, 'invalid_amount')]**. Log có một WARNING cho đơn 102 và một INFO với `accepted=2 rejected=1`. Logging mặc định gửi sang stderr, còn `print` gửi stdout; khi gom hai luồng, thứ tự hiển thị có thể khác.

Đây là **tổng của các dòng được chấp nhận**, không tự là doanh thu đầy đủ. Người dùng báo cáo phải biết có dòng bị loại; nếu yêu cầu không được thiếu đơn, job cần dừng hoặc đánh dấu báo cáo chưa sẵn sàng.

## Bắt đúng loại lỗi

Khối try chỉ bao quanh phần chuyển kiểu có thể tạo `ValueError`. Nếu viết sai tên biến ở chỗ khác, chương trình nên báo lỗi để mình sửa, không nuốt nó như dữ liệu xấu. Khi log rồi ném lỗi tiếp, `logging.exception` bên trong except giúp giữ traceback; cân nhắc log có chứa dữ liệu nhạy cảm hay không.

Không ghi nguyên request, token hoặc tất cả dữ liệu khách hàng chỉ vì đang debug. Một mã nhiệm vụ, mã dòng và mã lý do thường đủ để tìm ca cần điều tra. Với dữ liệu thật, cả ID cũng cần tuân theo quyền truy cập và chính sách giữ log.

## Kiểm tra hành vi sau lỗi

Đổi `không rõ` thành `50000`: tổng thành 150000 và danh sách loại rỗng. Đổi thành `-1`: vẫn phải bị loại. Nếu thêm lỗi lập trình như gọi một hàm chưa tồn tại, nó phải làm chương trình thất bại; không được xuất báo cáo bình thường.

Tham khảo: [Python exceptions](https://docs.python.org/3/tutorial/errors.html), [Logging HOWTO](https://docs.python.org/3/howto/logging.html).

