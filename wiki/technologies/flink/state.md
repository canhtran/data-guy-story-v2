# State trong Flink: nhớ thông tin giữa các sự kiện

E1 của cửa hàng A là 40.000 đồng. Khi E2 của A đến với 35.000 đồng, job cần nhớ 40.000 trước đó để tạo tổng 75.000. Thông tin nhớ qua nhiều record là state.

## Keyed state và operator state

Sau `keyBy(shop)`, keyed state thuộc từng key: A có tổng riêng, B có tổng riêng. Flink quản lý phân bố key/state cho subtask. Operator state thuộc instance operator, thường dùng trong những cơ chế như lưu tiến độ nguồn; khả năng phân phối lại khi rescale tùy loại state.

Ví dụ kiểm tra bằng tay: E1/A/40000 → A=40000; E2/B/50000 → A=40000,B=50000; E3/A/35000 → A=75000,B=50000. Nếu restart mà không phục hồi state, E4/A/10000 chỉ tạo A=10000 thay vì 85000.

## State backend khác checkpoint storage

State backend quyết định cách truy cập/lưu state khi job chạy. Checkpoint storage giữ snapshot phục hồi. Dùng backend trên đĩa không tự làm snapshot bền vững qua mất máy. Chọn backend theo dung lượng, latency và đặc điểm workload, rồi đo checkpoint/restore với dữ liệu đại diện.

Biến Python/Java trong bộ nhớ user code không tự trở thành managed state. Nếu job cần phục hồi nó, phải dùng API state phù hợp hoặc cơ chế snapshot rõ ràng.

## State cần có vòng đời

Deduplicate bằng `event_id` mà giữ mọi ID vô hạn có thể làm state tăng mãi. TTL giới hạn thời gian giữ state, nhưng record replay sau khi ID hết hạn có thể lại được tính là mới. TTL state trong DataStream ở phiên bản này dựa trên processing time, không tự đồng nghĩa với cửa sổ event time.

Giới hạn giữ ID phải phù hợp retention/replay và nghiệp vụ sửa dữ liệu. Nếu cần lịch sử dài, có thể cần ledger bền vững ở ngoài thay vì mọi thứ nằm trong state streaming.

Khi state size tăng, kiểm tra key cardinality, cleanup, timer và dữ liệu đến muộn. Đừng chỉ tăng RAM mà chưa biết thông tin nào được phép xóa. Đọc [checkpoint]({{< relref "/wiki/technologies/flink/checkpoint.md" >}}) để hiểu state trở về đâu sau lỗi.

Ví dụ là phép tính tay, đối chiếu Flink 1.20.3; chưa đo backend hay restore thực tế.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — state](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/fault-tolerance/state/) là nguồn đối chiếu cơ chế trong bài.

