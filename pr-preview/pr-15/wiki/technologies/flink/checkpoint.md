# Checkpoint trong Flink: snapshot nhất quán để phục hồi

Job đã cộng được A=75000 thì một TaskManager mất. Nếu chỉ restart từ đầu với state trống, hoặc giữ tổng mới nhưng đọc lại tất cả nguồn, kết quả sẽ sai. Checkpoint ghi nhận một điểm phục hồi nhất quán của state và tiến độ nguồn.

## Snapshot cần nhất quán

Checkpoint coordinator khởi phát checkpoint; barrier đi cùng luồng để phân định record thuộc phía trước/sau snapshot. Trong aligned checkpoint, operator nhiều input có thể phải chờ barrier các input tương ứng trước khi hoàn thành phần snapshot phù hợp.

Checkpoint chỉ dùng để phục hồi sau khi hoàn tất thành công. Có một checkpoint đang chạy không có nghĩa đã có một điểm phục hồi mới bền vững.

## Tính lại sau lỗi

Bài tập: checkpoint C hoàn tất sau E1/A/40000 và E2/A/35000. State tại C là 75000, nguồn ghi nhận vị trí đọc tiếp E3. E3/A/10000 được xử lý nhưng job chết trước checkpoint kế tiếp.

Khôi phục C: state về 75000, nguồn replay E3, tổng trở lại 85000. Không bắt đầu bằng 85000 rồi cộng lại E3; cũng không bắt đầu 0 tại E3. Đây là lập luận về state/source, chưa chứng minh output database không bị ghi lặp.

## Storage và chi phí

Checkpoint cần storage bền vững và truy cập được khi restore. Interval ngắn giảm khoảng replay nhưng tăng I/O/overhead; interval dài có thể tăng thời gian bắt kịp. Xem checkpoint duration, failed checkpoints, alignment time, state size và tuổi checkpoint hoàn tất cuối.

Backpressure có thể làm barrier di chuyển chậm. Unaligned checkpoint có thể giúp một số trường hợp bằng cách snapshot dữ liệu đang trên đường truyền; nó có thể tăng lượng snapshot và không sửa sink chậm. Chọn sau khi đo và kiểm tra giới hạn phiên bản.

## Sink vẫn là một phần riêng

Exactly-once state cần nguồn replay được. Exactly-once đầu cuối còn cần sink giao dịch hoặc idempotent theo cơ chế connector. Gọi API bên ngoài trong operator không tự được rollback khi restore checkpoint.

Ví dụ là mô hình theo Flink 1.20.3, chưa fault-test TaskManager. Đọc [exactly-once]({{< relref "/wiki/technologies/flink/exactly-once.md" >}}) và [savepoint]({{< relref "/wiki/technologies/flink/savepoint.md" >}}) trước khi thiết kế phục hồi/nâng cấp.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — checkpoints](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/state/checkpoints/) là nguồn đối chiếu cơ chế trong bài.

