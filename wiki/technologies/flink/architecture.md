# Kiến trúc Flink: JobManager, TaskManager và slot

Job vẫn hiện RUNNING nhưng một operator không có throughput. Để tìm nguyên nhân, cần biết operator đang chạy ở TaskManager nào và nó có đang chờ dữ liệu hay bị sink phía sau giữ lại.

## Ai điều phối, ai thực thi?

JobManager phối hợp thực thi; trong kiến trúc Flink, Dispatcher nhận job, ResourceManager quản lý tài nguyên và JobMaster điều phối một job. TaskManager chạy các task/subtask, trao đổi dữ liệu và giữ state đang sử dụng. Client gửi chương trình, không nhất thiết là nơi thực thi lâu dài.

Slot là đơn vị phân bổ tài nguyên trong TaskManager, không phải một CPU core được dành riêng. Slot sharing cho phép các task phù hợp từ cùng job dùng chung slot. Vì vậy không tính tổng mọi subtask rồi kết luận đó là số slot luôn cần.

## Một bài tập phân bổ

Giả sử job có source, map và sink cùng parallelism 2, cùng slot sharing group và đủ điều kiện chain. Một deployment có thể dùng hai slot cho hai pipeline song song. Nếu tách các operator sang slot sharing group khác, nhu cầu slot có thể tăng.

Bài tập này minh họa khái niệm, không đảm bảo scheduler luôn chọn bố cục đó. Muốn biết thực tế, xem execution graph, operator chain và slot sharing group của job.

## State nằm ở đâu khi lỗi?

Trong lúc chạy, state được truy cập qua state backend. Checkpoint storage giữ snapshot để phục hồi. TaskManager mất thì state đang chạy ở đó có thể mất; job cần checkpoint hoàn tất và nguồn replay được để khôi phục phần việc.

Một cluster có nhiều TaskManager nhưng snapshot nằm trên đĩa local đã mất không tạo khả năng phục hồi bạn mong đợi. Cần storage bền vững và đường dẫn các node đều truy cập được; tính khả dụng của JobManager còn phụ thuộc cấu hình high availability.

## Chẩn đoán

Job chờ tài nguyên: kiểm tra slot yêu cầu và slot sẵn có. Subtask restart: đọc log TaskManager chứa nó. Checkpoint lỗi storage: kiểm tra đường dẫn/quyền và dung lượng trước. CPU thấp không có nghĩa còn dư năng lực nếu task đang chờ I/O.

Bài này đối chiếu Flink 1.20.3; chưa thử failover cluster. Đọc [job/operator/task/subtask]({{< relref "/wiki/technologies/flink/job-operator-task-subtask.md" >}}) để hiểu execution graph.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — flink-architecture](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/flink-architecture/) là nguồn đối chiếu cơ chế trong bài.

