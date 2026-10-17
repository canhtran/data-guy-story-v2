---
title: "Backpressure trong Flink: chậm ở sink, dấu hiệu ở source"
description: "Tìm bottleneck qua tốc độ, busy time và hàng đợi có giới hạn."
draft: false
contentType: "concept"
weight: 10
level: "beginner"
topics: ["flink"]
prerequisites: []
related: []
---

Source đọc được 1.000 record/giây, nhưng database chỉ ghi được 200. Hàng đợi không thể tăng vô hạn. Khi buffer phía sau đầy, operator phía trước bị hạn chế đẩy dữ liệu; áp lực truyền ngược về source gọi là backpressure.

## Tính backlog

Bài tập đơn giản: input ổn định 1.000 record/giây, sink 200, chưa có retry hoặc filter. Chênh lệch 800 record/giây; sau 60 giây backlog tăng 48.000 record. Buffer lớn hơn chỉ trì hoãn lúc đầy, không tăng throughput của database.

Trong hệ thống thật, backlog có thể nằm ở Kafka hoặc ở các buffer/state bên trong, tùy nguồn và cơ chế flow control. Không suy từ một con số queue length ra toàn bộ dữ liệu chưa hoàn tất.

## Đi từ downstream ngược lên

Trong UI, so busy, idle và backpressured time của các subtask. Operator upstream bị backpressure có thể đang chờ operator phía sau; điểm bị báo đỏ không nhất thiết là nguyên nhân gốc. Nếu sink bận/chậm mà upstream bị chặn, xem latency ghi, connection pool, khóa database và rate limit.

Nếu chỉ một subtask chậm, kiểm tra key skew hoặc partition phân bố lệch. CPU thấp có thể do chờ network/I/O; CPU cao có thể do serialize hoặc user code. Cần ghép metrics với log và record rate.

## Điều chỉnh có mục đích

Batch write có thể giảm số round trip, nhưng thay latency và ranh giới transaction. Async I/O có thể tăng số request đang chờ, nhưng cần giới hạn concurrency và đảm bảo hệ thống ngoài chịu được. Tăng sink parallelism chỉ hữu ích khi sink ngoài có thêm capacity.

Checkpoint duration/alignment có thể tăng khi backpressure kéo dài. Unaligned checkpoint là lựa chọn riêng cho một số workload, không biến sink 200 record/giây thành sink 1.000 record/giây.

Nếu output freshness trễ, theo dõi thời gian từ event đến output bên cạnh lag/count; record rate giống nhau vẫn có thể đi cùng backlog cũ. Đặt cảnh báo theo tiến độ và tuổi checkpoint cuối thay vì chỉ trạng thái RUNNING.

Bài này đối chiếu Flink 1.20.3; phép tính backlog là mô hình, chưa có benchmark sink hay load test cluster.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — back_pressure](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/ops/monitoring/back_pressure/) là nguồn đối chiếu cơ chế trong bài.
