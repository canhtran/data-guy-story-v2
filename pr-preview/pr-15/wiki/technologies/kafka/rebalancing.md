# Rebalancing: partition đổi consumer thì chuyện gì xảy ra?

R1 đang xử lý P0 thì R2 vào group. Group có thể phân phối lại partition. Rebalance là thay đổi assignment, không phải di chuyển dữ liệu topic sang broker khác. Việc đổi consumer phải phối hợp với tiến độ và output đang ghi.

## Một tình huống có thể kiểm tra bằng tay

Topic có P0 và P1. Ban đầu R1 đọc cả hai. Sau khi R2 vào, giả sử P1 được giao cho R2. R1 đã ghi xong P1 offset 10, nhưng offset 11 còn đang chạy.

Nếu committed offset P1 là 11, R2 có thể đọc lại record 11. Đây là lựa chọn phục hồi hợp lý; sink cần idempotency. Nếu R1 commit 12 trước khi record 11 ghi xong, R2 có thể bỏ qua công việc chưa hoàn tất.

## Không phải giao thức nào cũng dừng toàn bộ group

Classic eager rebalance, cooperative assignment và consumer protocol có cơ chế thu hồi/giao lại khác nhau. Kafka 4.0 hỗ trợ classic và consumer protocol; các cấu hình heartbeat không được áp dụng giống nhau. Vì vậy, không kết luận mọi rebalance luôn dừng tất cả partition cùng lúc.

Với client dùng callback assignment/revocation, cần quản lý phần việc theo từng partition. Dừng hoặc hoàn tất công việc cũ phù hợp trước khi partition được giao lại. Công việc bất đồng bộ vẫn tiếp tục ghi sau khi mất assignment có thể gây cạnh tranh với consumer mới; Kafka assignment không tự khóa database ngoài.

## Vì sao rebalance liên tục?

Consumer mất kết nối, vượt giới hạn thời gian giữa các poll, restart liên tục hoặc subscription/partition thay đổi có thể làm assignment thay đổi. Kiểm tra log group, processing time của lô và lỗi sink. Tăng `max.poll.interval.ms` có thể phù hợp với xử lý dài, nhưng cũng kéo dài thời gian phát hiện consumer không còn tiến triển.

Giảm `max.poll.records`, tách tác vụ nặng và quản lý hàng đợi có giới hạn có thể giúp. Không tạo worker vô hạn để giữ poll nhanh nếu output không theo kịp. Static membership có thể giảm một số thay đổi không cần thiết; nó không sửa consumer bị deadlock.

Bài này chưa fault-test một group thật. Khi xây lab, kiểm tra assignment trước/sau, record replay và tổng output, không chỉ nhìn consumer có restart được hay không. Đọc [offset]({{< relref "/wiki/technologies/kafka/offset.md" >}}) để thiết kế ranh giới commit.

## Tài liệu gốc

[Consumer configs 4.0](https://kafka.apache.org/40/configuration/consumer-configs/) giải thích poll interval, membership và protocol. [Kafka design](https://kafka.apache.org/40/design/design/) mô tả quản lý consumer. Đối chiếu ngày 1/10/2026.

