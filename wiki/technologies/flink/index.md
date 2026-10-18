# Apache Flink

Flink xử lý luồng dữ liệu có trạng thái. Các bài dưới đây đi từ execution graph tới event time và phục hồi. Nội dung đối chiếu Flink 1.20.3 với ví dụ kiểm tra bằng tay. Hướng dẫn cài local, connector và lab phục hồi thực tế còn đang biên soạn; chưa coi đây là bộ lab đã kiểm thử.

## Bắt đầu

- [Flink là gì?]({{< relref "/wiki/technologies/flink/overview.md" >}})

## Khái niệm chính

- [Kiến trúc Flink]({{< relref "/wiki/technologies/flink/architecture.md" >}})
- [Job, Operator, Task và Subtask]({{< relref "/wiki/technologies/flink/job-operator-task-subtask.md" >}})
- [Mức độ song song trong Flink]({{< relref "/wiki/technologies/flink/parallelism.md" >}})
- [Trạng thái trong Flink]({{< relref "/wiki/technologies/flink/state.md" >}})

## Thời gian và luồng dữ liệu

- [Thời gian sự kiện trong Flink]({{< relref "/wiki/technologies/flink/event-time.md" >}})
- [Watermark trong Flink]({{< relref "/wiki/technologies/flink/watermark.md" >}})

## Phục hồi khi lỗi

- [Checkpoint trong Flink]({{< relref "/wiki/technologies/flink/checkpoint.md" >}})
- [Savepoint trong Flink]({{< relref "/wiki/technologies/flink/savepoint.md" >}})
- [Xử lý đúng một lần trong Flink]({{< relref "/wiki/technologies/flink/exactly-once.md" >}})

## Vận hành

- [Áp lực ngược trong Flink]({{< relref "/wiki/technologies/flink/backpressure.md" >}})

## Lộ trình liên quan

- [Streaming Engineering — lộ trình đang lên kế hoạch]({{< relref "/learning-paths/streaming-engineering/_index.md" >}})

