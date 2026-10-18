# Consumer group: cùng luồng, tiến độ riêng

Báo cáo doanh thu và hệ thống giao hàng đều cần đọc tất cả đơn. Nếu đặt chúng vào cùng consumer group, chúng sẽ chia việc đọc partition, không phải mỗi bên đều nhận toàn bộ sự kiện. Hai ứng dụng có mục đích độc lập cần group ID riêng.

## Chia việc trong một group

Với cơ chế subscribe/group assignment thông thường, một partition được giao cho một consumer trong group tại một thời điểm. Consumer có thể nhận nhiều partition. Các group khác nhau có thể đọc cùng partition độc lập.

Ví dụ kiểm tra bằng tay với topic có ba partition:

| Group | Consumer | Assignment minh họa |
| --- | --- | --- |
| revenue | R1 | P0, P1 |
| revenue | R2 | P2 |
| shipping | S1 | P0, P1, P2 |

R1 và R2 cùng tạo đầu vào cho báo cáo; S1 vẫn đọc cả ba partition. Assignment thật phụ thuộc assignor/protocol, không bảo đảm đúng bố cục bảng này. Nếu thêm R3 và R4, tối đa ba consumer có partition; một consumer có thể rảnh.

## Tiến độ thuộc group, không thuộc tên máy

Group lưu committed offset theo topic-partition. Khi consumer khác nhận partition, nó có thể bắt đầu từ vị trí đã commit. Đổi group ID giống tạo một nhóm có tiến độ riêng; đừng làm điều đó để “sửa lag” mà chưa xác định cần replay từ đâu.

Kafka 4.0 có classic và consumer group protocol. Cấu hình heartbeat/assignment khác nhau; bài này giải thích mô hình chia partition, không giả định mọi hệ thống dùng cùng giao thức. Không lẫn mô hình này với các tính năng chia record kiểu share group ở các phiên bản khác.

## Khi consumer vẫn chạy nhưng lag tăng

Consumer có thể poll liên tục nhưng xử lý sink quá chậm. Xem tốc độ xử lý, số partition được giao, lỗi ghi output và committed offset. Lag tính theo số record không tự là số phút dữ liệu trễ; còn cần timestamp nghiệp vụ và thời điểm output xuất hiện.

Trong [ví dụ local]({{< relref "/wiki/technologies/kafka/overview.md" >}}), `cafe-reader-v1` là group thực hành. `--from-beginning` không ghi đè committed offset đã tồn tại; dùng group mới nếu muốn đọc lại từ đầu trong một bài học mới. Đọc [offset]({{< relref "/wiki/technologies/kafka/offset.md" >}}) trước khi thay chính sách commit.

## Tài liệu gốc

[Consumer configs 4.0](https://kafka.apache.org/40/configuration/consumer-configs/) mô tả group ID, protocol và offset reset. [Basic operations](https://kafka.apache.org/40/operations/basic-kafka-operations/) hướng dẫn quan sát assignment/lag. Đối chiếu ngày 1/10/2026.

