---
title: "RDD trong Spark: transformation, action và lineage"
description: "Dùng ví dụ tổng tiền theo key để hiểu RDD và giới hạn phục hồi."
draft: false
contentType: "concept"
weight: 3
level: "beginner"
topics: ["spark"]
prerequisites: []
related: []
---

RDD (Resilient Distributed Dataset) là tập phần tử chia thành partition, có thể xử lý song song. Một RDD mới được tạo từ transformation của RDD trước; bạn không sửa trực tiếp từng phần tử trong RDD cũ. Với dữ liệu có cột và schema, DataFrame thường là điểm bắt đầu thuận tiện hơn.

## Tính tổng theo cửa hàng

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}). Mỗi tuple là một đơn đã thanh toán; tiền tính bằng đồng nguyên.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[2]").appName("rdd-v1").getOrCreate()
orders = spark.sparkContext.parallelize([("A", 40000), ("A", 35000), ("B", 50000)], 2)
totals = orders.reduceByKey(lambda left, right: left + right)
print(sorted(totals.collect()))
print(orders.getNumPartitions())
spark.stop()
```

Kết quả: `[('A', 75000), ('B', 50000)]` và `2`. `reduceByKey` có thể cộng một phần ngay ở phía nguồn trước khi trao đổi dữ liệu. `groupByKey` gom toàn bộ giá trị theo key nên có thể phải chuyển và giữ nhiều dữ liệu hơn. Dùng reduce chỉ khi phép toán phù hợp, chẳng hạn phép cộng có tính kết hợp và giao hoán.

## Lineage giúp tính lại, không làm side effect an toàn

`parallelize → reduceByKey → collect` tạo quan hệ phụ thuộc, gọi là **lineage**. Nếu mất một partition tính được từ nguồn còn truy cập được, Spark có thể chạy lại các phép biến đổi cần thiết. Điều này không cứu được file nguồn đã bị xóa hoặc một nguồn đã thay đổi mà bạn không giữ snapshot.

Task có thể được chạy lại. Nếu trong `map` bạn gửi email hay gọi API thu tiền, hành động đó có thể xảy ra hơn một lần. Không coi khả năng phục hồi RDD là bảo đảm exactly-once cho dịch vụ ngoài. Tách side effect ra nơi có idempotency key hoặc transaction phù hợp.

## Cache khi nào?

Khi nhiều action dùng cùng một kết quả đắt tiền, `persist()` có thể tránh tính lại các phần đã lưu. Nó chỉ có hiệu lực khi dữ liệu được materialize bởi action; executor mất đi có thể mất cache. Cache không phải backup. Sau khi dùng xong gọi `unpersist()` để trả tài nguyên.

Không dùng `collect()` để xem toàn bộ dữ liệu lớn: kết quả tập trung ở driver. Ví dụ ở đây chỉ có hai tổng nên kiểm tra bằng collect an toàn. Nếu Python worker lỗi, kiểm tra `PYSPARK_PYTHON` và môi trường worker trước khi sửa logic reduce.

## Khi nào cần RDD?

RDD hữu ích khi cần thao tác thấp hơn trên đối tượng hoặc thuật toán khó biểu diễn bằng hàm SQL. Đổi lại, Spark SQL không nhìn được đầy đủ ý nghĩa của lambda Python để tối ưu như với biểu thức DataFrame. Không chuyển sang RDD chỉ vì muốn “chạy phân tán”; DataFrame cũng đã thực thi phân tán.

## Tài liệu gốc

[RDD programming guide 3.5.6](https://spark.apache.org/docs/3.5.6/rdd-programming-guide.html) mô tả transformation/action, shuffle, persistence và xử lý closure. Đối chiếu ngày 1/10/2026.
