# Kafka transactions: output và offset cùng một commit

Pipeline đọc đơn từ Kafka, tính phí giao hàng rồi ghi sang topic mới. Nếu output đã ghi nhưng offset input chưa commit, restart có thể tạo output lần nữa. Kafka transaction cho phép gom output Kafka và offset của consumer group vào cùng ranh giới commit.

## Trình tự ở mức cơ chế

Đây là quy trình khái niệm cho client hỗ trợ transactional API, không phải đoạn code có thể copy chạy:

1. Khởi tạo transactional producer với `transactional.id` được quản lý đúng theo instance logic.
2. Consumer đọc input, không auto commit offset độc lập.
3. Bắt đầu transaction, gửi các record output.
4. Đưa offset tiếp theo của input cùng metadata group vào transaction.
5. Commit transaction; nếu thất bại thì xử lý abort/retry theo loại lỗi client.

Consumer của topic output dùng `isolation.level=read_committed` để không nhìn thấy record từ transaction đã abort. Với `read_uncommitted`, atomicity đối với người đọc không có ý nghĩa giống vậy.

## Một ví dụ để tự đối chiếu

Input P0 offset 7 là đơn 101. Transaction T ghi phí giao hàng của đơn đó và offset tiếp theo 8. Nếu T abort, người đọc read_committed không nhận output của T, và offset input không tiến bởi transaction ấy. Nếu T commit, output và offset gắn trong transaction được commit cùng nhau.

“Không nhận output aborted” không có nghĩa record bị xóa vật lý ngay. Consumer isolation quyết định record nào được trả về; transaction đang mở còn có thể trì hoãn việc nhìn thấy phần log phía sau theo last stable offset.

## Transactional ID và lỗi

Transactional ID giúp quản lý producer theo vòng đời, và fencing ngăn instance cũ tiếp tục hoạt động trái phép khi instance mới thay thế. Nếu hai instance không được phối hợp dùng cùng ID, chúng có thể fencing nhau. Không tạo ID mới ngẫu nhiên sau mọi restart rồi mặc định đã có phục hồi đúng.

Phân loại lỗi recoverable, abortable và fatal theo API client. Không retry vô hạn một producer đã bị fenced. Theo dõi transaction timeout, thời gian xử lý và độ dài transaction; giữ transaction mở quá lâu có thể ảnh hưởng consumer read_committed.

## Ngoài Kafka vẫn cần thiết kế riêng

Nếu pipeline còn gửi email hoặc ghi database, những side effect đó không được rollback bởi abort Kafka. Dùng outbox, idempotency hoặc cơ chế transaction của connector đã được kiểm chứng tùy hệ thống. Không gọi mọi pipeline có `transactional.id` là exactly-once đầu cuối.

Ví dụ trên được đối chiếu bằng cơ chế tài liệu, chưa chạy fault-injection transaction trong đợt này. [Bài local]({{< relref "/wiki/technologies/kafka/overview.md" >}}) chỉ gửi/đọc record thông thường.

## Tài liệu gốc

[KafkaProducer API 4.0](https://kafka.apache.org/40/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html) mô tả transaction lifecycle/fencing. [Consumer configs](https://kafka.apache.org/40/configuration/consumer-configs/) mô tả isolation. Đối chiếu ngày 1/10/2026.

