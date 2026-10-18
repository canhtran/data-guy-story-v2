# Topic, partition và key: Kafka giữ thứ tự ở đâu?

Đơn 101 có hai sự kiện: `created` rồi `paid`. Bạn muốn consumer nhìn thấy chúng theo đúng thứ tự. Kafka có thứ tự offset trong từng partition; không có một thứ tự toàn cục giữa mọi partition của topic.

## Topic chứa nhiều log

Topic là tên luồng, chẳng hạn `order-events`. Partition là một log bên trong topic. Một record có key và value; producer chọn partition theo cơ chế partitioning của client, trừ khi ứng dụng chỉ định partition trực tiếp.

Giả sử ta đã gán như sau, đây là ví dụ kiểm tra bằng tay, không phải kết quả hash mặc định:

| Partition | Offset | Key | Sự kiện |
| --- | ---: | --- | --- |
| P0 | 0 | 101 | created |
| P0 | 1 | 101 | paid |
| P1 | 0 | 102 | created |
| P1 | 1 | 102 | cancelled |

Consumer P0 đọc created trước paid. Nhưng không thể so offset 1 của P0 với offset 0 của P1 để kết luận sự kiện nào xảy ra trước. Offset chỉ có nghĩa trong một topic-partition.

## Chọn key theo điều cần giữ cùng nhau

Nếu cần thứ tự thay đổi của từng đơn, `order_id` thường là key phù hợp. Nếu key là cửa hàng, tất cả đơn của cửa hàng lớn có thể dồn về một partition và tạo điểm nóng. Nếu không có key, đừng dựa vào việc các sự kiện cùng đơn tự đi về cùng partition.

Ngay cả với key, vẫn phải kiểm tra producer/client, số partition và cách gửi. Tăng số partition có thể đổi ánh xạ key cho record mới; dữ liệu cũ không tự chuyển nơi. Hai producer cũng có thể gửi các sự kiện theo thứ tự khác thời gian nghiệp vụ. Giữ partition order không có nghĩa timestamp luôn tăng.

## Đối chiếu trước khi tăng partition

Trong bảng trên có hai partition, consumer group kiểu thông thường có tối đa hai consumer cùng đọc tích cực. Thêm consumer thứ ba không chia một partition thành hai phần. Muốn xử lý nhanh hơn cần xem key, số partition, tốc độ sink và chiến lược xử lý trong consumer.

Bài [tổng quan]({{< relref "/wiki/technologies/kafka/overview.md" >}}) dùng một partition nên hai record giữ thứ tự ghi. Nó không kiểm chứng mọi partitioner hoặc client. Khi gặp thứ tự sai, kiểm tra key, partition, retries và thứ tự gửi trước khi sort tất cả theo timestamp.

## Tài liệu gốc

[Kafka producer configuration 4.0](https://kafka.apache.org/40/configuration/producer-configs/) mô tả partitioner, key và điều kiện giữ thứ tự khi retry. Đối chiếu ngày 1/10/2026.

