---
title: "Phân vùng dữ liệu"
description: "Partitioning: chia dữ liệu để chia việc"
draft: false
contentType: "concept"
weight: 2
level: "beginner"
topics: ["distributed-systems"]
prerequisites: ["/wiki/nen-tang/distributed-systems/overview"]
related: []
---

Nếu mọi đơn hàng nằm trên một máy, dung lượng và khả năng xử lý của máy đó có giới hạn. Partitioning chia dữ liệu thành các phần để lưu hoặc xử lý riêng. Phần được đặt trên các node khác nhau thường được gọi là shard.

Partition dữ liệu khác với network partition — tình trạng các nhóm máy không liên lạc được. Đừng nhầm hai ý nghĩa chỉ vì cùng một từ.

## Thử chia sáu khách

Một quy tắc học đơn giản là `customer_id % 3`: khách 1 và 4 vào phần 1, khách 2 và 5 vào phần 2, khách 3 và 6 vào phần 0. Muốn lấy tất cả đơn của khách 4, mình biết phần cần tìm. Muốn cộng doanh thu toàn bộ, phải đọc cả ba phần rồi gom.

Bạn có thể tự kiểm tra bằng Python 3, không cần thư viện ngoài:

```python
parts = {0: [], 1: [], 2: []}
for customer_id in range(1, 7):
    parts[customer_id % 3].append(customer_id)
print(parts)
```

Kết quả: `{0: [3, 6], 1: [1, 4], 2: [2, 5]}`.

## Khóa đều chưa chắc tải đều

Sáu khách chia đều, nhưng nếu khách 4 có một triệu đơn còn người khác chỉ có vài đơn, phần 1 vẫn quá tải. Chọn khóa cần nhìn phân bố dữ liệu và truy vấn thật. Chia theo ngày tiện cho lọc thời gian, nhưng ngày hôm nay có thể nhận hầu hết các lượt ghi.

Chia theo khoảng giữ các khóa gần nhau cùng phần, giúp truy vấn khoảng. Chia bằng hash thường phân tán khóa hơn, nhưng truy vấn khoảng có thể phải tìm nhiều phần. Một phép JOIN giữa hai bộ dữ liệu được chia theo khóa khác nhau có thể cần chuyển rất nhiều dòng qua mạng.

## Thêm phần không chỉ sửa một con số

Với quy tắc modulo, chuyển từ 3 sang 4 làm nhiều khóa đổi nơi. Nếu reader dùng quy tắc mới trước khi dữ liệu đã chuyển, nó có thể tìm sai chỗ. Hệ thống thật cần cơ chế định tuyến, di chuyển và kiểm soát trong giai đoạn chuyển tiếp. Consistent hashing là một hướng để giảm lượng di chuyển, không loại bỏ mọi việc vận hành.

Bài tập: tính phần của khách 4 khi đổi từ 3 sang 4. Kết quả đổi từ 1 sang 0. Dữ liệu cũ cần được tìm ở đâu trong lúc chưa chuyển xong?

Partitioning không tạo bản sao để chịu mất dữ liệu; đó là vai trò khác của [replication]({{< relref "/wiki/nen-tang/distributed-systems/replication.md" >}}). Tham khảo thiết kế partition trong [Dynamo paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf).
