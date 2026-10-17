---
title: "Kiến trúc Spark: driver, executor, job, stage và task"
description: "Theo dõi một action từ driver tới các task và đọc ranh giới shuffle."
draft: false
contentType: "concept"
weight: 2
level: "beginner"
topics: ["spark"]
prerequisites: []
related: []
---

Bạn gọi `groupBy(...).sum(...)`, nhưng máy vẫn chưa đọc toàn bộ dữ liệu. Đến khi gọi `collect()` hoặc ghi file, Spark mới thực thi công việc cần thiết. Để tìm lỗi đúng chỗ, ta cần phân biệt chương trình điều phối và phần thực thi.

## Ai làm gì?

| Thành phần | Vai trò |
| --- | --- |
| Driver | Chạy chương trình chính, xây kế hoạch và điều phối task |
| Cluster manager | Cấp tài nguyên cho application, chẳng hạn YARN hoặc Kubernetes |
| Executor | Chạy task và giữ dữ liệu cache/shuffle cho application |
| Task | Một phần công việc của một stage, xử lý một partition |

Worker node là máy có thể chạy executor; nó không đồng nghĩa với một task. Ở `local[2]`, các vai trò thực thi nằm trên cùng máy nên bạn không quan sát được mạng và lỗi node như trên cluster.

## Từ action đến task

**Transformation** như `filter` xây kế hoạch. **Action** như `count` yêu cầu kết quả, kích hoạt job; một action có thể kéo theo nhiều job tùy kế hoạch. Job được chia thành **stage**. Khi dữ liệu phải trao đổi giữa partition qua shuffle, Spark tạo ranh giới stage. Trong một stage, nhiều task có thể chạy song song hoặc chờ tài nguyên.

Ví dụ bốn partition nguồn cùng chứa đơn của A. Bước lọc có thể chạy riêng trên từng partition; tổng cuối theo A cần tập hợp thông tin từ nhiều partition. Chỗ trao đổi đó là shuffle, không phải việc đọc file ban đầu.

## Nhìn kế hoạch trên máy

Dùng môi trường trong [bài tổng quan]({{< relref "/wiki/technologies/spark/overview.md" >}}).

```python
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder.master("local[2]").appName("stages-v1")
         .config("spark.sql.adaptive.enabled", "false")
         .config("spark.sql.shuffle.partitions", "2").getOrCreate())
source = spark.range(0, 8, 1, 4)
result = source.withColumn("shop", F.col("id") % 2).groupBy("shop").count()
result.explain()
print([(r.shop, r["count"]) for r in result.orderBy("shop").collect()])
spark.stop()
```

Kết quả là `[(0, 4), (1, 4)]`. Kế hoạch có `Exchange`: dữ liệu/tổng cục bộ cần được phân phối lại theo `shop`. Ví dụ tắt Adaptive Query Execution (AQE) để dễ đọc kế hoạch, không đề xuất tắt AQE cho production.

Khi application còn chạy, Spark UI thường ở cổng 4040 trên driver. Tab Jobs/Stages cho biết task đang chạy, thất bại hoặc chậm. Khi chương trình đã `stop()`, UI không còn phục vụ; muốn xem sau đó cần event log và History Server được cấu hình riêng.

## Tìm lỗi ở đúng thành phần

Nếu `collect()` đưa hàng triệu dòng về driver, tăng bộ nhớ executor không giải quyết được bộ nhớ driver. Nếu một task chậm còn các task khác đã xong, kiểm tra kích thước partition, skew và spill. Nếu executor liên tục mất kết nối, kiểm tra log executor, bộ nhớ và đường mạng tới driver; một dòng lỗi cuối trên driver thường chưa đủ kết luận.

Ví dụ local chỉ xác nhận kết quả và kế hoạch thực thi. Nó không kiểm chứng khả năng chịu lỗi của cluster hay tốc độ tăng khi thêm máy.

## Tài liệu gốc

[Cluster overview 3.5.6](https://spark.apache.org/docs/3.5.6/cluster-overview.html) định nghĩa các vai trò và job/stage/task. [Monitoring](https://spark.apache.org/docs/3.5.6/monitoring.html) giải thích Spark UI và event log. Đối chiếu ngày 1/10/2026.
