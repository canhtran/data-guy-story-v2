# Flink là gì? Xử lý luồng có trạng thái

Báo cáo cần cập nhật ngay khi đơn đến, nhưng một đơn có thể đến muộn hoặc được gửi lại. Nếu chỉ cộng mỗi record vừa nhận vào một biến, restart có thể mất tổng cũ, còn retry có thể cộng trùng. Flink là engine xử lý dữ liệu hỗ trợ state và cơ chế phục hồi để xây các phép xử lý như vậy.

Bộ bài này đối chiếu **Flink 1.20.3** ngày 1/10/2026, không coi đây là phiên bản mới nhất. Các ví dụ là mô hình kiểm tra bằng tay, không phải kết quả đã chạy cluster. Hướng dẫn cài local và lab restart có connector thật còn đang biên soạn; chưa có tuyên bố hỗ trợ một tổ hợp OS/JDK đã kiểm thử.

## Theo dõi một phép tổng hợp

Mỗi sự kiện là một lần thanh toán, có `event_id` riêng, cửa hàng và số tiền nguyên đồng. Nhận lần lượt E1/A/40000, E2/B/50000, E3/A/35000. Với key cửa hàng, state sau ba record là A=75000, B=50000. Bạn có thể cộng tay để kiểm tra.

Nếu E1 đến thêm lần nữa và job chỉ cộng tiền, A thành 115000. Exactly-once của state khi phục hồi không tự hiểu hai record E1 là cùng một sự kiện nghiệp vụ. Muốn deduplicate cần lưu identity và định nghĩa thời hạn giữ identity phù hợp với khả năng replay.

## Các thành phần cần hiểu

Source đọc dữ liệu, operator biến đổi/tổng hợp, sink ghi output. State giữ thông tin qua nhiều record. Event time quyết định sự kiện thuộc khoảng thời gian nào; watermark giúp job tiến triển dù dữ liệu không đến đúng thứ tự. Checkpoint ghi nhận state và tiến độ nguồn để phục hồi.

Flink không tự thay database lưu trữ lâu dài hay Kafka giữ lịch sử sự kiện. State backend và checkpoint storage cũng là hai vai trò khác nhau: nơi truy cập state khi chạy và nơi lưu snapshot phục hồi.

## Khi nào đáng dùng?

Flink phù hợp khi cần xử lý luồng có trạng thái, cửa sổ thời gian, join sự kiện và kiểm soát phục hồi. Nếu chỉ chạy một truy vấn tổng hợp mỗi ngày, batch SQL có thể đơn giản hơn. Streaming thêm trách nhiệm về dữ liệu muộn, state tăng, checkpoint, sink và nâng cấp job.

Khi output ngừng cập nhật, không mặc định tăng parallelism: watermark có thể bị giữ bởi một input im lặng, sink có thể bị nghẽn hoặc job đang restart. Đọc [kiến trúc]({{< relref "/wiki/technologies/flink/architecture.md" >}}), [state]({{< relref "/wiki/technologies/flink/state.md" >}}) rồi [event time]({{< relref "/wiki/technologies/flink/event-time.md" >}}).

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — stateful-stream-processing](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/stateful-stream-processing/) là nguồn đối chiếu cơ chế trong bài.

