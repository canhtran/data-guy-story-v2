---
title: "Parallelism trong Flink: thêm subtask có hết nghẽn?"
description: "Hiểu giới hạn source, key skew, slot và khả năng rescale state."
draft: false
contentType: "concept"
weight: 4
level: "beginner"
topics: ["flink"]
prerequisites: []
related: []
---

Một operator có parallelism 4 nhưng một subtask nhận gần hết record. Nếu 90% sự kiện thuộc cửa hàng A và job keyBy cửa hàng, A vẫn được xử lý bởi một subtask tại một thời điểm. Thêm subtask không tự tách một key nặng.

## Chia việc theo operator

Parallelism là số instance song song của operator/task. Các operator có thể có mức khác nhau. **Maximum parallelism** của keyed state liên quan tới key groups và khả năng phân phối state khi rescale; nó khác số subtask đang chạy.

Ví dụ kiểm tra bằng tay: A có 900 record/giây, B và C mỗi cửa hàng 50. Nếu A đi vào subtask 0, thêm ba subtask không chia 900 record A thành bốn phần. Nếu phép tổng hợp cho phép cộng kết quả trung gian, có thể thiết kế tổng hợp hai tầng; điều đó cần đổi thuật toán, không chỉ config.

## Nguồn và sink giới hạn trước

Với Kafka source thông thường đọc topic có hai partition, đặt source parallelism 8 không tạo tám partition nguồn. Một số reader có thể không được giao split. Nếu sink database chỉ chịu 200 write/giây, tăng upstream có thể làm backlog tăng nhanh hơn.

Slot sẵn có, bộ nhớ state, network và checkpoint cũng giới hạn triển khai. Parallelism lớn có thêm overhead; chỉ tăng sau khi đo throughput, phân bố key và bottleneck theo subtask.

## Rescale cần giữ được state

Khi đổi parallelism của job stateful, cần checkpoint/savepoint tương thích và ánh xạ operator/state đúng. Không coi restart với con số mới là bảo đảm state cũ tự chuyển được trong mọi trường hợp. UID, serializer, max parallelism và loại state đều có thể ảnh hưởng.

Nếu job chờ slot, kiểm tra tài nguyên trước khi kiểm tra logic. Nếu một subtask luôn chậm, so record rate, state size, busy time và I/O giữa các subtask. Đọc [backpressure]({{< relref "/wiki/technologies/flink/backpressure.md" >}}) để tìm operator gây nghẽn từ phía sink.

Bài này là mô hình theo Flink 1.20.3, không có benchmark hay rescale cluster đã chạy.

## Tài liệu gốc

[Tài liệu Apache Flink 1.20 — parallel](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/execution/parallel/) là nguồn đối chiếu cơ chế trong bài.
